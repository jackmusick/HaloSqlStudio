"""modules.halopsa_split.category — Category endpoints + DTOs."""

from __future__ import annotations

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

from modules.halopsa._common import _HaloAPIClient, DotDict, SDKError

@dataclass
class CategoryDetail:
    guid: Optional[str] = None
    intent: Optional[str] = None
    id: Optional[int] = None
    value: Optional[str] = None
    category_name: Optional[str] = None
    type_id: Optional[int] = None
    sla_id: Optional[int] = None
    priority_id: Optional[int] = None
    chargerate: Optional[int] = None
    category_group_id: Optional[int] = None
    _isnew: Optional[bool] = None
    include_note: Optional[bool] = None
    note: Optional[str] = None
    user_note: Optional[str] = None
    itilrequesttype: Optional[int] = None
    _warning: Optional[str] = None
    is_integration: Optional[bool] = None
    translations: Optional[List[LanguagePackTranslationsCustom]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CategoryDetail':
        if data is None:
            return None
        return cls(**{'guid': data.get('guid'), 'intent': data.get('intent'), 'id': data.get('id'), 'value': data.get('value'), 'category_name': data.get('category_name'), 'type_id': data.get('type_id'), 'sla_id': data.get('sla_id'), 'priority_id': data.get('priority_id'), 'chargerate': data.get('chargerate'), 'category_group_id': data.get('category_group_id'), '_isnew': data.get('_isnew'), 'include_note': data.get('include_note'), 'note': data.get('note'), 'user_note': data.get('user_note'), 'itilrequesttype': data.get('itilrequesttype'), '_warning': data.get('_warning'), 'is_integration': data.get('is_integration'), 'translations': data.get('translations')})

def list_categories(client, **kwargs):
    """List of CategoryDetail"""
    url = f'{client.base_url}/Category'
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

def create_category(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Category"""
    url = f'{client.base_url}/Category'
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

def get_category(client, id: str, **kwargs):
    """Get one CategoryDetail"""
    url = f'{client.base_url}/Category/{id}'
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

def delete_category(client, id: str, **kwargs):
    """DELETE /Category/{id}"""
    url = f'{client.base_url}/Category/{id}'
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
