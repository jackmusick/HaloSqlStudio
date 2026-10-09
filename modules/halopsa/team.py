"""modules.halopsa_split.team — Team endpoints + DTOs."""

from __future__ import annotations

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

from modules.halopsa._common import _HaloAPIClient, DotDict, SDKError

@dataclass
class TeamsChatMessageList:
    id: Optional[int] = None
    chat_id: Optional[str] = None
    message_id: Optional[str] = None
    external_link_id: Optional[int] = None
    note_html: Optional[str] = None
    note: Optional[str] = None
    who_azure_id: Optional[str] = None
    who: Optional[str] = None
    datetime: Optional[str] = None
    whoagent_id: Optional[int] = None
    whoagent_name: Optional[str] = None
    _sendmessage: Optional[bool] = None
    _warning: Optional[str] = None
    remote_session_id: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TeamsChatMessageList':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'chat_id': data.get('chat_id'), 'message_id': data.get('message_id'), 'external_link_id': data.get('external_link_id'), 'note_html': data.get('note_html'), 'note': data.get('note'), 'who_azure_id': data.get('who_azure_id'), 'who': data.get('who'), 'datetime': data.get('datetime'), 'whoagent_id': data.get('whoagent_id'), 'whoagent_name': data.get('whoagent_name'), '_sendmessage': data.get('_sendmessage'), '_warning': data.get('_warning'), 'remote_session_id': data.get('remote_session_id')})

@dataclass
class TeamsManifestCreate:
    name: Optional[str] = None
    short_description: Optional[str] = None
    long_description: Optional[str] = None
    icon_color: Optional[str] = None
    icon_outline: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TeamsManifestCreate':
        if data is None:
            return None
        return cls(**{'name': data.get('name'), 'short_description': data.get('shortDescription'), 'long_description': data.get('longDescription'), 'icon_color': data.get('iconColor'), 'icon_outline': data.get('iconOutline')})

def list_teams_1(client, **kwargs):
    """List of SectionDetail"""
    url = f'{client.base_url}/Team'
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

def create_team(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Team"""
    url = f'{client.base_url}/Team'
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

def list_trees(client, **kwargs):
    """GET /Team/Tree"""
    url = f'{client.base_url}/Team/Tree'
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

def get_team(client, id: str, **kwargs):
    """Get one SectionDetail"""
    url = f'{client.base_url}/Team/{id}'
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

def delete_team(client, id: str, **kwargs):
    """DELETE /Team/{id}"""
    url = f'{client.base_url}/Team/{id}'
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
