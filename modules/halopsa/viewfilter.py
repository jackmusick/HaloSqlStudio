"""modules.halopsa_split.viewfilter — ViewFilter endpoints + DTOs."""

from __future__ import annotations

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

from modules.halopsa._common import _HaloAPIClient, DotDict, SDKError

@dataclass
class ViewFilter:
    id: Optional[int] = None
    guid: Optional[str] = None
    intent: Optional[str] = None
    name: Optional[str] = None
    agent_id: Optional[int] = None
    team_id: Optional[int] = None
    type: Optional[int] = None
    type_name: Optional[str] = None
    sys_id: Optional[str] = None
    show_on_portal: Optional[bool] = None
    filters: Optional[List[ViewFilterDetails]] = None
    _temp: Optional[bool] = None
    access_control: Optional[List[AccessControl]] = None
    access_control_level: Optional[int] = None
    translations: Optional[List[LanguagePackTranslationsCustom]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ViewFilter':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'guid': data.get('guid'), 'intent': data.get('intent'), 'name': data.get('name'), 'agent_id': data.get('agent_id'), 'team_id': data.get('team_id'), 'type': data.get('type'), 'type_name': data.get('type_name'), 'sys_id': data.get('sys_id'), 'show_on_portal': data.get('show_on_portal'), 'filters': data.get('filters'), '_temp': data.get('_temp'), 'access_control': data.get('access_control'), 'access_control_level': data.get('access_control_level'), 'translations': data.get('translations')})

def list_view_filters(client, **kwargs):
    """List of ViewFilter"""
    url = f'{client.base_url}/ViewFilter'
    response = client._request_with_retry('GET', url, params=kwargs)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        body = e.response.text[:1000] if e.response is not None else 'No response body'
        raise SDKError(f'HTTP {e.response.status_code}: {body}', status_code=e.response.status_code, response_body=body)
    try:
        result = response.json() if response.content else None
    except requests.exceptions.JSONDecodeError:
        raise SDKError(f'Invalid JSON response (HTTP {response.status_code}): {response.text[:500]}', status_code=response.status_code, response_body=response.text[:1000])
    return client._auto_convert(result)

def create_view_filter(client, data: Dict[str, Any]=None, **kwargs):
    """POST /ViewFilter"""
    url = f'{client.base_url}/ViewFilter'
    response = client._request_with_retry('POST', url, json=data, params=kwargs)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        body = e.response.text[:1000] if e.response is not None else 'No response body'
        raise SDKError(f'HTTP {e.response.status_code}: {body}', status_code=e.response.status_code, response_body=body)
    try:
        result = response.json() if response.content else None
    except requests.exceptions.JSONDecodeError:
        raise SDKError(f'Invalid JSON response (HTTP {response.status_code}): {response.text[:500]}', status_code=response.status_code, response_body=response.text[:1000])
    return client._auto_convert(result)

def get_view_filter(client, id: str, **kwargs):
    """Get one ViewFilter"""
    url = f'{client.base_url}/ViewFilter/{id}'
    response = client._request_with_retry('GET', url, params=kwargs)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        body = e.response.text[:1000] if e.response is not None else 'No response body'
        raise SDKError(f'HTTP {e.response.status_code}: {body}', status_code=e.response.status_code, response_body=body)
    try:
        result = response.json() if response.content else None
    except requests.exceptions.JSONDecodeError:
        raise SDKError(f'Invalid JSON response (HTTP {response.status_code}): {response.text[:500]}', status_code=response.status_code, response_body=response.text[:1000])
    return client._auto_convert(result)

def delete_view_filter(client, id: str, **kwargs):
    """DELETE /ViewFilter/{id}"""
    url = f'{client.base_url}/ViewFilter/{id}'
    response = client._request_with_retry('DELETE', url, params=kwargs)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        body = e.response.text[:1000] if e.response is not None else 'No response body'
        raise SDKError(f'HTTP {e.response.status_code}: {body}', status_code=e.response.status_code, response_body=body)
    try:
        result = response.json() if response.content else None
    except requests.exceptions.JSONDecodeError:
        raise SDKError(f'Invalid JSON response (HTTP {response.status_code}): {response.text[:500]}', status_code=response.status_code, response_body=response.text[:1000])
    return client._auto_convert(result)
