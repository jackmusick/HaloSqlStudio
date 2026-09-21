"""modules.halopsa_split.viewlists — ViewLists endpoints + DTOs."""

from __future__ import annotations

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

from modules.halopsa._common import _HaloAPIClient, DotDict, SDKError

@dataclass
class ViewLists:
    guid: Optional[str] = None
    intent: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    use: Optional[str] = None
    agent_id: Optional[int] = None
    team_id: Optional[int] = None
    type: Optional[int] = None
    type_name: Optional[str] = None
    sequence: Optional[int] = None
    showcounts: Optional[bool] = None
    column_profile_id: Optional[int] = None
    column_profile_guid: Optional[str] = None
    filter_profile_id: Optional[int] = None
    filter_profile_guid: Optional[str] = None
    lock_view_type: Optional[int] = None
    connectedinstance_id: Optional[int] = None
    connectedinstance_list_id: Optional[int] = None
    show_in_team_tree: Optional[bool] = None
    show_in_team_tree_team_id: Optional[int] = None
    default_kanban_view: Optional[int] = None
    show_in_team_tree_team_name: Optional[str] = None
    ticket_count: Optional[int] = None
    connectedinstance_error: Optional[bool] = None
    column_profile_name: Optional[str] = None
    filter_profile_name: Optional[str] = None
    connectedinstance_name: Optional[str] = None
    filters: Optional[List[ViewFilterDetails]] = None
    group: Optional[int] = None
    group_name: Optional[str] = None
    group_seq: Optional[int] = None
    group_type: Optional[int] = None
    group_collapsed: Optional[bool] = None
    translations: Optional[List[LanguagePackTranslationsCustom]] = None
    access_control: Optional[List[AccessControl]] = None
    access_control_level: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ViewLists':
        if data is None:
            return None
        return cls(**{'guid': data.get('guid'), 'intent': data.get('intent'), 'id': data.get('id'), 'name': data.get('name'), 'use': data.get('use'), 'agent_id': data.get('agent_id'), 'team_id': data.get('team_id'), 'type': data.get('type'), 'type_name': data.get('type_name'), 'sequence': data.get('sequence'), 'showcounts': data.get('showcounts'), 'column_profile_id': data.get('column_profile_id'), 'column_profile_guid': data.get('column_profile_guid'), 'filter_profile_id': data.get('filter_profile_id'), 'filter_profile_guid': data.get('filter_profile_guid'), 'lock_view_type': data.get('lock_view_type'), 'connectedinstance_id': data.get('connectedinstance_id'), 'connectedinstance_list_id': data.get('connectedinstance_list_id'), 'show_in_team_tree': data.get('show_in_team_tree'), 'show_in_team_tree_team_id': data.get('show_in_team_tree_team_id'), 'default_kanban_view': data.get('default_kanban_view'), 'show_in_team_tree_team_name': data.get('show_in_team_tree_team_name'), 'ticket_count': data.get('ticket_count'), 'connectedinstance_error': data.get('connectedinstance_error'), 'column_profile_name': data.get('column_profile_name'), 'filter_profile_name': data.get('filter_profile_name'), 'connectedinstance_name': data.get('connectedinstance_name'), 'filters': data.get('filters'), 'group': data.get('group'), 'group_name': data.get('group_name'), 'group_seq': data.get('group_seq'), 'group_type': data.get('group_type'), 'group_collapsed': data.get('group_collapsed'), 'translations': data.get('translations'), 'access_control': data.get('access_control'), 'access_control_level': data.get('access_control_level')})

def list_view_lists(client, **kwargs):
    """List of ViewLists"""
    url = f'{client.base_url}/ViewLists'
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

def create_view_lists(client, data: Dict[str, Any]=None, **kwargs):
    """POST /ViewLists"""
    url = f'{client.base_url}/ViewLists'
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

def get_view_lists(client, id: str, **kwargs):
    """Get one ViewLists"""
    url = f'{client.base_url}/ViewLists/{id}'
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

def delete_view_lists(client, id: str, **kwargs):
    """DELETE /ViewLists/{id}"""
    url = f'{client.base_url}/ViewLists/{id}'
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
