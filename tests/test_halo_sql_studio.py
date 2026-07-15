import asyncio
from pathlib import Path
from types import SimpleNamespace

import yaml

from functions import halo_sql_studio


def test_execute_query_replaces_unresolved_agent_variable(monkeypatch):
    captured: dict[str, str] = {}

    async def resolve_actor():
        return {"id": 42, "email": "dispatcher@example.com"}

    async def execute_report(sql):
        captured["sql"] = sql
        return {"report": {"rows": []}}

    monkeypatch.setattr(halo_sql_studio, "_resolve_actor", resolve_actor)
    monkeypatch.setattr(halo_sql_studio, "_execute_report", execute_report)

    result = asyncio.run(
        halo_sql_studio.execute_query("SELECT * FROM actions WHERE who = $agentid")
    )

    assert captured["sql"].endswith("who = 42")
    assert result == {"available_columns": [], "report": {"rows": []}}


def test_execute_query_skips_actor_lookup_without_agent_variable(monkeypatch):
    async def resolve_actor():
        raise AssertionError("actor cache should not be read")

    async def execute_report(sql):
        assert sql == "SELECT 1 AS result"
        return {
            "available_columns": [{"name": "result"}],
            "report": {"rows": [{"result": "1"}], "table_html": "unused"},
            "sql": sql,
        }

    monkeypatch.setattr(halo_sql_studio, "_resolve_actor", resolve_actor)
    monkeypatch.setattr(halo_sql_studio, "_execute_report", execute_report)

    result = asyncio.run(halo_sql_studio.execute_query("SELECT 1 AS result"))

    assert result == {
        "available_columns": [{"name": "result"}],
        "report": {"rows": [{"result": "1"}]},
    }


def test_refresh_schema_normalizes_rows_for_table_cache(monkeypatch):
    captured: dict[str, object] = {}

    async def execute_report(sql):
        assert sql == halo_sql_studio.SCHEMA_SQL
        return {
            "report": {
                "rows": [
                    {
                        "name": "FAULTS",
                        "column_name": "faultid",
                        "data_type": "int",
                        "ordinal_position": 1,
                    }
                ]
            }
        }

    async def replace_table(table_name, cache_type, documents):
        captured.update(
            table_name=table_name,
            cache_type=cache_type,
            documents=documents,
        )
        return len(documents)

    monkeypatch.setattr(halo_sql_studio, "_execute_report", execute_report)
    monkeypatch.setattr(halo_sql_studio, "_replace_table", replace_table)

    count = asyncio.run(halo_sql_studio._refresh_schema())

    assert count == 1
    assert captured["table_name"] == "halo_sql_schema_cache"
    assert captured["cache_type"] == "schema"
    assert captured["documents"] == [
        {
            "id": "FAULTS",
            "data": {
                "name": "FAULTS",
                "column_count": 1,
                "columns": [
                    {
                        "name": "faultid",
                        "data_type": "int",
                        "ordinal_position": 1,
                    }
                ],
            },
        }
    ]


def test_actor_cache_miss_refreshes_agents(monkeypatch):
    queries = 0
    refreshed = 0

    async def query(table_name, **kwargs):
        nonlocal queries
        queries += 1
        assert table_name == "halo_sql_agents"
        assert kwargs["where"] == {"email_lower": "dispatcher@example.com"}
        if queries == 1:
            return SimpleNamespace(documents=[])
        return SimpleNamespace(documents=[SimpleNamespace(data={"id": 7})])

    async def refresh_agents():
        nonlocal refreshed
        refreshed += 1
        return 1

    monkeypatch.setattr(
        halo_sql_studio,
        "context",
        SimpleNamespace(email="Dispatcher@Example.com"),
    )
    monkeypatch.setattr(halo_sql_studio.tables, "query", query)
    monkeypatch.setattr(halo_sql_studio, "_refresh_agents", refresh_agents)

    actor = asyncio.run(halo_sql_studio._resolve_actor())

    assert actor["id"] == 7
    assert refreshed == 1


def test_daily_schedule_targets_cache_refresh_workflow():
    root = Path(__file__).resolve().parents[1]
    workflows = yaml.safe_load((root / ".bifrost/workflows.yaml").read_text())["workflows"]
    events = yaml.safe_load((root / ".bifrost/events.yaml").read_text())["events"]
    refresh_id = next(
        workflow_id
        for workflow_id, item in workflows.items()
        if item["function_name"] == "refresh_cache"
    )
    schedule = next(iter(events.values()))

    assert schedule["cron_expression"] == "23 3 * * *"
    assert schedule["timezone"] == "America/New_York"
    assert schedule["subscriptions"][0]["workflow_id"] == refresh_id
