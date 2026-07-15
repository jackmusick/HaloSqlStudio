"""Small reporting API extension for the vendored HaloPSA client."""

from __future__ import annotations

from typing import Any

from modules.halopsa._common import SDKError
from modules.halopsa._lazy import _lazy


async def request_json(method: str, path: str, payload: Any = None) -> Any:
    """Call a Halo reporting endpoint using the integration-backed client."""
    client = await _lazy._ensure_client()
    url = f"{client.base_url}/{path.lstrip('/')}"
    response = client._request_with_retry(method, url, json=payload)
    if not response.ok:
        raise SDKError(
            f"Halo reporting API returned {response.status_code}",
            status_code=response.status_code,
            response_body=response.text[:2000],
        )
    if not response.content:
        return None
    return response.json()
