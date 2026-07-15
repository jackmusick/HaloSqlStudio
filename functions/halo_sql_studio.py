"""Halo reporting workflows and reference caches for Halo SQL Studio."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from bifrost import context, integrations, tables, workflow
from modules import halopsa
from modules.halopsa.reporting import request_json


SCHEMA_SQL = (
    "SELECT TABLE_NAME as name, COLUMN_NAME as column_name, "
    "DATA_TYPE as data_type, ORDINAL_POSITION as ordinal_position "
    "FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dbo'"
)
REPORTS_SQL = (
    "SELECT APid [Id], fvalue [Group], APTitle [Name], APSQL [SQL] "
    "FROM AnalyzerProfile JOIN LOOKUP ON (APGroupID + 1) = fcode AND fid = 41"
)


def _plain(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _items(value: Any, *keys: str) -> list[dict[str, Any]]:
    data = _plain(value)
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        for key in keys:
            candidate = data.get(key)
            if isinstance(candidate, list):
                return [item for item in candidate if isinstance(item, dict)]
    return []


async def _all_documents(table_name: str) -> list[Any]:
    documents: list[Any] = []
    offset = 0
    while True:
        result = await tables.query(table_name, limit=1000, offset=offset)
        documents.extend(result.documents)
        if len(result.documents) < 1000:
            return documents
        offset += len(result.documents)


async def _replace_table(
    table_name: str,
    cache_type: str,
    documents: list[dict[str, Any]],
) -> int:
    current = await _all_documents(table_name)
    for start in range(0, len(documents), 25):
        await tables.upsert_batch(table_name, documents[start : start + 25])
    new_ids = {document["id"] for document in documents}
    stale_ids = [document.id for document in current if document.id not in new_ids]
    for start in range(0, len(stale_ids), 25):
        await tables.delete_batch(table_name, stale_ids[start : start + 25])

    refreshed_at = datetime.now(timezone.utc).isoformat()
    await tables.upsert(
        "halo_sql_cache_state",
        cache_type,
        {
            "cache_type": cache_type,
            "refreshed_at": refreshed_at,
            "record_count": len(documents),
            "status": "ready",
        },
    )
    return len(documents)


async def _execute_report(sql: str) -> dict[str, Any]:
    result = _plain(
        await request_json(
            "POST",
            "/Report",
            [{"sql": sql, "_testonly": True, "_loadreportonly": True}],
        )
    )
    return result if isinstance(result, dict) else {"report": {"rows": []}}


def _compact_report(result: dict[str, Any]) -> dict[str, Any]:
    """Keep only the reporting fields consumed by the browser."""
    report = result.get("report")
    report = report if isinstance(report, dict) else {}
    compact_report: dict[str, Any] = {"rows": _items(report.get("rows"), "rows")}
    if report.get("load_error"):
        compact_report["load_error"] = report["load_error"]
    return {
        "available_columns": _items(result.get("available_columns"), "available_columns"),
        "report": compact_report,
    }


async def _refresh_environment() -> str:
    integration = await integrations.get("HaloPSA")
    if not integration:
        raise RuntimeError("The HaloPSA connection is not configured for this Solution")
    halo_base_url = str((integration.config or {}).get("base_url") or "").rstrip("/").removesuffix("/api")
    if not halo_base_url:
        raise RuntimeError("The HaloPSA connection does not define a base URL")
    await tables.upsert(
        "halo_sql_cache_state",
        "environment",
        {
            "cache_type": "environment",
            "refreshed_at": datetime.now(timezone.utc).isoformat(),
            "record_count": 1,
            "status": "ready",
            "halo_base_url": halo_base_url,
        },
    )
    return halo_base_url


async def _refresh_agents() -> int:
    cache = _plain(await halopsa.list_client_caches(iscachebuild=True))
    rows = _items(cache, "agents") if not isinstance(cache, dict) else _items(cache.get("agents"), "agents")
    documents = []
    for row in rows:
        normalized = _plain(row)
        normalized["email_lower"] = str(normalized.get("email") or "").strip().lower()
        documents.append({"id": str(normalized["id"]), "data": normalized})
    return await _replace_table("halo_sql_agents", "agents", documents)


async def _refresh_schema() -> int:
    result = await _execute_report(SCHEMA_SQL)
    rows = _items((result.get("report") or {}).get("rows"), "rows")
    grouped: dict[str, list[dict[str, Any]]] = {}
    for index, row in enumerate(rows):
        table_name = str(row.get("name") or row.get("TABLE_NAME") or "").strip()
        column_name = str(row.get("column_name") or row.get("COLUMN_NAME") or "").strip()
        if not table_name or not column_name:
            continue
        ordinal = int(row.get("ordinal_position") or row.get("ORDINAL_POSITION") or index)
        grouped.setdefault(table_name, []).append(
            {
                "name": column_name,
                "data_type": str(row.get("data_type") or row.get("DATA_TYPE") or "unknown"),
                "ordinal_position": ordinal,
            }
        )
    documents = [
        {
            "id": table_name,
            "data": {
                "name": table_name,
                "column_count": len(columns),
                "columns": sorted(columns, key=lambda column: column["ordinal_position"]),
            },
        }
        for table_name, columns in grouped.items()
    ]
    return await _replace_table("halo_sql_schema_cache", "schema", documents)


async def _resolve_actor() -> dict[str, Any]:
    email = str(getattr(context, "email", None) or "").strip().lower()
    if not email:
        raise RuntimeError("The calling Bifrost user does not have an email address")
    result = await tables.query("halo_sql_agents", where={"email_lower": email}, limit=2)
    if not result.documents:
        await _refresh_agents()
        result = await tables.query("halo_sql_agents", where={"email_lower": email}, limit=2)
    if not result.documents:
        raise RuntimeError(f"No Halo agent matches Bifrost user {email}")
    return result.documents[0].data


@workflow(category="Halo SQL Studio")
async def refresh_cache(cache_type: str = "all", reason: str = "daily") -> dict[str, Any]:
    """Refresh cached Halo agents, reporting schema, or both."""
    if cache_type not in {"all", "agents", "schema"}:
        raise ValueError(f"Unsupported cache type: {cache_type}")
    counts: dict[str, int] = {}
    halo_base_url: str | None = None
    if cache_type in {"all", "agents"}:
        counts["agents"] = await _refresh_agents()
        halo_base_url = await _refresh_environment()
    if cache_type in {"all", "schema"}:
        counts["schema"] = await _refresh_schema()
    return {
        "cache_type": cache_type,
        "reason": reason,
        "counts": counts,
        "halo_base_url": halo_base_url,
        "refreshed_at": datetime.now(timezone.utc).isoformat(),
    }


@workflow(category="Halo SQL Studio")
async def execute_query(sql: str, agent_id: int | None = None) -> dict[str, Any]:
    """Execute SQL through Halo's reporting API as the calling Bifrost user."""
    if not sql.strip():
        raise ValueError("SQL is required")
    processed_sql = sql
    if "$agentid" in sql:
        if agent_id is None:
            actor = await _resolve_actor()
            agent_id = int(actor["id"])
        processed_sql = sql.replace("$agentid", str(agent_id))
    return _compact_report(await _execute_report(processed_sql))


@workflow(category="Halo SQL Studio")
async def list_reports() -> dict[str, Any]:
    """Load current Halo report definitions."""
    return _compact_report(await _execute_report(REPORTS_SQL))


@workflow(category="Halo SQL Studio")
async def save_report(
    sql: str,
    name: str,
    description: str = "",
    report_id: int | None = None,
) -> dict[str, Any]:
    """Create or update a Halo report."""
    payload: dict[str, Any] = {"sql": sql, "name": name, "description": description}
    if report_id is not None:
        payload["id"] = report_id
    result = _plain(await request_json("POST", "/report", [payload]))
    items = _items(result)
    saved = items[0] if items else result
    if not isinstance(saved, dict) or saved.get("id") is None:
        raise RuntimeError("Halo returned an invalid report save response")
    return {"id": str(saved["id"])}
