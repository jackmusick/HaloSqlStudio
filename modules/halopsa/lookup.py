"""modules.halopsa_split.lookup — Lookup endpoints + DTOs."""

from __future__ import annotations

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

from modules.halopsa._common import _HaloAPIClient, DotDict, SDKError

@dataclass
class Lookup:
    intent: Optional[str] = None
    lookupid: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    originalvalue: Optional[str] = None
    value2: Optional[str] = None
    value2_guid: Optional[str] = None
    value2_bool: Optional[bool] = None
    value3: Optional[str] = None
    value3_bool: Optional[bool] = None
    value4: Optional[str] = None
    value4_bool: Optional[bool] = None
    value5: Optional[str] = None
    value5_bool: Optional[bool] = None
    value6: Optional[str] = None
    value6_bool: Optional[bool] = None
    value7: Optional[str] = None
    value7_bool: Optional[bool] = None
    value8: Optional[str] = None
    value8_bool: Optional[bool] = None
    value9: Optional[str] = None
    value9_bool: Optional[bool] = None
    value10: Optional[str] = None
    value10_bool: Optional[bool] = None
    rates: Optional[List[ChargeRate]] = None
    contract_ref: Optional[str] = None
    overriding_rate_id: Optional[int] = None
    _isnewcode: Optional[bool] = None
    _isimport: Optional[bool] = None
    _importtype: Optional[str] = None
    kashflow_tenant: Optional[str] = None
    email_template_name: Optional[str] = None
    sla_name: Optional[str] = None
    access_control: Optional[List[AccessControl]] = None
    access_control_level: Optional[int] = None
    custom1: Optional[str] = None
    custom1_bool: Optional[bool] = None
    custom2: Optional[str] = None
    tax_rate_name: Optional[str] = None
    xero_tenant_name: Optional[str] = None
    surcharge_item_name: Optional[str] = None
    dynamics_company_name: Optional[str] = None
    valueint1: Optional[int] = None
    linked_item: Optional[str] = None
    sequence: Optional[int] = None
    sub_lookup: Optional[List[Lookup]] = None
    translations: Optional[List[LanguagePackTranslationsCustom]] = None
    _warning: Optional[str] = None
    inactive: Optional[bool] = None
    column_profile_name: Optional[str] = None
    jira_instance_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Lookup':
        if data is None:
            return None
        return cls(**{'intent': data.get('intent'), 'lookupid': data.get('lookupid'), 'id': data.get('id'), 'name': data.get('name'), 'originalvalue': data.get('originalvalue'), 'value2': data.get('value2'), 'value2_guid': data.get('value2_guid'), 'value2_bool': data.get('value2_bool'), 'value3': data.get('value3'), 'value3_bool': data.get('value3_bool'), 'value4': data.get('value4'), 'value4_bool': data.get('value4_bool'), 'value5': data.get('value5'), 'value5_bool': data.get('value5_bool'), 'value6': data.get('value6'), 'value6_bool': data.get('value6_bool'), 'value7': data.get('value7'), 'value7_bool': data.get('value7_bool'), 'value8': data.get('value8'), 'value8_bool': data.get('value8_bool'), 'value9': data.get('value9'), 'value9_bool': data.get('value9_bool'), 'value10': data.get('value10'), 'value10_bool': data.get('value10_bool'), 'rates': data.get('rates'), 'contract_ref': data.get('contract_ref'), 'overriding_rate_id': data.get('overriding_rate_id'), '_isnewcode': data.get('_isnewcode'), '_isimport': data.get('_isimport'), '_importtype': data.get('_importtype'), 'kashflow_tenant': data.get('kashflow_tenant'), 'email_template_name': data.get('email_template_name'), 'sla_name': data.get('sla_name'), 'access_control': data.get('access_control'), 'access_control_level': data.get('access_control_level'), 'custom1': data.get('custom1'), 'custom1_bool': data.get('custom1_bool'), 'custom2': data.get('custom2'), 'tax_rate_name': data.get('tax_rate_name'), 'xero_tenant_name': data.get('xero_tenant_name'), 'surcharge_item_name': data.get('surcharge_item_name'), 'dynamics_company_name': data.get('dynamics_company_name'), 'valueint1': data.get('valueint1'), 'linked_item': data.get('linked_item'), 'sequence': data.get('sequence'), 'sub_lookup': data.get('sub_lookup'), 'translations': data.get('translations'), '_warning': data.get('_warning'), 'inactive': data.get('inactive'), 'column_profile_name': data.get('column_profile_name'), 'jira_instance_name': data.get('jira_instance_name')})

def list_lookups(client, **kwargs) -> List[Lookup]:
    """List of Lookup"""
    url = f'{client.base_url}/Lookup'
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

def create_lookup(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Lookup"""
    url = f'{client.base_url}/Lookup'
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

def create_clear_cache_2(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Lookup/ClearCache"""
    url = f'{client.base_url}/Lookup/ClearCache'
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

def get_lookup(client, id: str, **kwargs):
    """Get one Lookup"""
    url = f'{client.base_url}/Lookup/{id}'
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

def delete_lookup(client, id: str, **kwargs):
    """DELETE /Lookup/{id}"""
    url = f'{client.base_url}/Lookup/{id}'
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
