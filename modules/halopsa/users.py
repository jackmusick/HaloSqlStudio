"""modules.halopsa_split.users — Users endpoints + DTOs."""

from __future__ import annotations

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

from modules.halopsa._common import _HaloAPIClient, DotDict, SDKError

@dataclass
class Instance:
    id: Optional[int] = None
    hostname: Optional[str] = None
    envname: Optional[str] = None
    version: Optional[str] = None
    commits_ahead: Optional[int] = None
    commits_behind: Optional[int] = None
    syncid: Optional[str] = None
    offline: Optional[bool] = None
    insync: Optional[bool] = None
    versionmatch: Optional[bool] = None
    canmerge: Optional[bool] = None
    iscurrent: Optional[bool] = None
    nomergereason: Optional[str] = None
    isself: Optional[bool] = None
    isprod: Optional[bool] = None
    _restore_from_prod: Optional[bool] = None
    _restore_from_prod_result: Optional[str] = None
    source_instance_id: Optional[int] = None
    source_instance_name: Optional[str] = None
    last_merge_date: Optional[str] = None
    _update_source_instance_id: Optional[int] = None
    is_pipeline: Optional[bool] = None
    unsynced_sprint: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Instance':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'hostname': data.get('hostname'), 'envname': data.get('envname'), 'version': data.get('version'), 'commits_ahead': data.get('commits_ahead'), 'commits_behind': data.get('commits_behind'), 'syncid': data.get('syncid'), 'offline': data.get('offline'), 'insync': data.get('insync'), 'versionmatch': data.get('versionmatch'), 'canmerge': data.get('canmerge'), 'iscurrent': data.get('iscurrent'), 'nomergereason': data.get('nomergereason'), 'isself': data.get('isself'), 'isprod': data.get('isprod'), '_restore_from_prod': data.get('_restore_from_prod'), '_restore_from_prod_result': data.get('_restore_from_prod_result'), 'source_instance_id': data.get('source_instance_id'), 'source_instance_name': data.get('source_instance_name'), 'last_merge_date': data.get('last_merge_date'), '_update_source_instance_id': data.get('_update_source_instance_id'), 'is_pipeline': data.get('is_pipeline'), 'unsynced_sprint': data.get('unsynced_sprint')})

@dataclass
class MarketingUnsubscribe:
    id: Optional[int] = None
    mailcampaign_id: Optional[int] = None
    user_id: Optional[int] = None
    email_address: Optional[str] = None
    email_unsubscribed: Optional[int] = None
    date_unsubscribed: Optional[str] = None
    user_name: Optional[str] = None
    mailcampaign_name: Optional[str] = None
    email_unsubscribed_name: Optional[str] = None
    token: Optional[str] = None
    validate_token: Optional[bool] = None
    unsub_all: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MarketingUnsubscribe':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'mailcampaign_id': data.get('mailcampaign_id'), 'user_id': data.get('user_id'), 'email_address': data.get('email_address'), 'email_unsubscribed': data.get('email_unsubscribed'), 'date_unsubscribed': data.get('date_unsubscribed'), 'user_name': data.get('user_name'), 'mailcampaign_name': data.get('mailcampaign_name'), 'email_unsubscribed_name': data.get('email_unsubscribed_name'), 'token': data.get('token'), 'validate_token': data.get('validate_token'), 'unsub_all': data.get('unsub_all')})

@dataclass
class NHDClaim:
    type: Optional[str] = None
    value: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NHDClaim':
        if data is None:
            return None
        return cls(**{'type': data.get('type'), 'value': data.get('value')})

@dataclass
class NotificationConditions:
    id: Optional[int] = None
    rule_id: Optional[int] = None
    notification_guid: Optional[str] = None
    fieldname: Optional[str] = None
    fieldid: Optional[int] = None
    change_context: Optional[int] = None
    type: Optional[int] = None
    value_int: Optional[int] = None
    valueint_guid: Optional[str] = None
    value_string: Optional[str] = None
    value_display: Optional[str] = None
    value_type: Optional[str] = None
    timezonestring: Optional[str] = None
    tablename: Optional[str] = None
    _warning: Optional[str] = None
    fieldtype: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NotificationConditions':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'rule_id': data.get('rule_id'), 'notification_guid': data.get('notification_guid'), 'fieldname': data.get('fieldname'), 'fieldid': data.get('fieldid'), 'change_context': data.get('change_context'), 'type': data.get('type'), 'value_int': data.get('value_int'), 'valueint_guid': data.get('valueint_guid'), 'value_string': data.get('value_string'), 'value_display': data.get('value_display'), 'value_type': data.get('value_type'), 'timezonestring': data.get('timezonestring'), 'tablename': data.get('tablename'), '_warning': data.get('_warning'), 'fieldtype': data.get('fieldtype')})

@dataclass
class NotificationOutcome:
    id: Optional[int] = None
    notification_id: Optional[int] = None
    outcome_id: Optional[int] = None
    outcome_name: Optional[str] = None
    input: Optional[int] = None
    input_text: Optional[str] = None
    is_accept: Optional[bool] = None
    translations: Optional[List[LanguagePackTranslationsCustom]] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NotificationOutcome':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'notification_id': data.get('notification_id'), 'outcome_id': data.get('outcome_id'), 'outcome_name': data.get('outcome_name'), 'input': data.get('input'), 'input_text': data.get('input_text'), 'is_accept': data.get('is_accept'), 'translations': data.get('translations'), '_warning': data.get('_warning')})

@dataclass
class Supplier:
    id: Optional[int] = None
    name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Supplier':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name')})

@dataclass
class UnameNotification:
    guid: Optional[str] = None
    intent: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    agent_id: Optional[int] = None
    agent_name: Optional[str] = None
    team_id: Optional[int] = None
    team_guid: Optional[str] = None
    team_name: Optional[str] = None
    type: Optional[int] = None
    delivery_method: Optional[int] = None
    sendpushnotification: Optional[bool] = None
    sendpushnotificationbrowser: Optional[bool] = None
    popupinnotificationpane: Optional[bool] = None
    eventno: Optional[int] = None
    emailtemplate_id: Optional[int] = None
    emailtemplate_guid: Optional[str] = None
    emailtemplate_name: Optional[str] = None
    user_id: Optional[int] = None
    user_name: Optional[str] = None
    email_list: Optional[str] = None
    slack_id: Optional[int] = None
    interval: Optional[float] = None
    useworkinghours: Optional[int] = None
    restriction_type: Optional[int] = None
    restriction_department_id: Optional[int] = None
    restriction_department_guid: Optional[str] = None
    restriction_department_name: Optional[str] = None
    restriction_team_id: Optional[int] = None
    restriction_team_guid: Optional[str] = None
    restriction_team_name: Optional[str] = None
    webhook_id: Optional[str] = None
    agents: Optional[List[UnameNotificationLink]] = None
    condition_count: Optional[int] = None
    subscriber_count: Optional[int] = None
    role_id: Optional[str] = None
    role_name: Optional[str] = None
    conditions: Optional[List[NotificationConditions]] = None
    _canupdate: Optional[bool] = None
    slack_channel_name: Optional[str] = None
    teams_id: Optional[int] = None
    teams_channel_name: Optional[str] = None
    value1: Optional[int] = None
    value1_name: Optional[str] = None
    _iszapier: Optional[bool] = None
    filter_sitecontact: Optional[bool] = None
    sitecontact_type: Optional[int] = None
    _warning: Optional[str] = None
    roles: Optional[List[UnameNotificationLink]] = None
    mattermost_channelid: Optional[int] = None
    mattermost_channel_name: Optional[str] = None
    rule_id: Optional[int] = None
    rule_guid: Optional[str] = None
    rule_name: Optional[str] = None
    user_roles: Optional[List[UnameNotificationLink]] = None
    filter_type: Optional[int] = None
    customisecolour: Optional[bool] = None
    colour: Optional[str] = None
    access_control: Optional[List[AccessControl]] = None
    access_control_level: Optional[int] = None
    safe_instances: Optional[int] = None
    safe_instance_list: Optional[List[Instance]] = None
    twilio_details: Optional[int] = None
    twilio_number: Optional[str] = None
    flow_seq: Optional[int] = None
    flow_id: Optional[int] = None
    outcomes: Optional[List[NotificationOutcome]] = None
    acknowledge_type: Optional[int] = None
    acknowledge_complete: Optional[str] = None
    acknowledge_empty: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UnameNotification':
        if data is None:
            return None
        return cls(**{'guid': data.get('guid'), 'intent': data.get('intent'), 'id': data.get('id'), 'name': data.get('name'), 'agent_id': data.get('agent_id'), 'agent_name': data.get('agent_name'), 'team_id': data.get('team_id'), 'team_guid': data.get('team_guid'), 'team_name': data.get('team_name'), 'type': data.get('type'), 'delivery_method': data.get('delivery_method'), 'sendpushnotification': data.get('sendpushnotification'), 'sendpushnotificationbrowser': data.get('sendpushnotificationbrowser'), 'popupinnotificationpane': data.get('popupinnotificationpane'), 'eventno': data.get('eventno'), 'emailtemplate_id': data.get('emailtemplate_id'), 'emailtemplate_guid': data.get('emailtemplate_guid'), 'emailtemplate_name': data.get('emailtemplate_name'), 'user_id': data.get('user_id'), 'user_name': data.get('user_name'), 'email_list': data.get('email_list'), 'slack_id': data.get('slack_id'), 'interval': data.get('interval'), 'useworkinghours': data.get('useworkinghours'), 'restriction_type': data.get('restriction_type'), 'restriction_department_id': data.get('restriction_department_id'), 'restriction_department_guid': data.get('restriction_department_guid'), 'restriction_department_name': data.get('restriction_department_name'), 'restriction_team_id': data.get('restriction_team_id'), 'restriction_team_guid': data.get('restriction_team_guid'), 'restriction_team_name': data.get('restriction_team_name'), 'webhook_id': data.get('webhook_id'), 'agents': data.get('agents'), 'condition_count': data.get('condition_count'), 'subscriber_count': data.get('subscriber_count'), 'role_id': data.get('role_id'), 'role_name': data.get('role_name'), 'conditions': data.get('conditions'), '_canupdate': data.get('_canupdate'), 'slack_channel_name': data.get('slack_channel_name'), 'teams_id': data.get('teams_id'), 'teams_channel_name': data.get('teams_channel_name'), 'value1': data.get('value1'), 'value1_name': data.get('value1_name'), '_iszapier': data.get('_iszapier'), 'filter_sitecontact': data.get('filter_sitecontact'), 'sitecontact_type': data.get('sitecontact_type'), '_warning': data.get('_warning'), 'roles': data.get('roles'), 'mattermost_channelid': data.get('mattermost_channelid'), 'mattermost_channel_name': data.get('mattermost_channel_name'), 'rule_id': data.get('rule_id'), 'rule_guid': data.get('rule_guid'), 'rule_name': data.get('rule_name'), 'user_roles': data.get('user_roles'), 'filter_type': data.get('filter_type'), 'customisecolour': data.get('customisecolour'), 'colour': data.get('colour'), 'access_control': data.get('access_control'), 'access_control_level': data.get('access_control_level'), 'safe_instances': data.get('safe_instances'), 'safe_instance_list': data.get('safe_instance_list'), 'twilio_details': data.get('twilio_details'), 'twilio_number': data.get('twilio_number'), 'flow_seq': data.get('flow_seq'), 'flow_id': data.get('flow_id'), 'outcomes': data.get('outcomes'), 'acknowledge_type': data.get('acknowledge_type'), 'acknowledge_complete': data.get('acknowledge_complete'), 'acknowledge_empty': data.get('acknowledge_empty')})

@dataclass
class UnameNotificationLink:
    id: Optional[int] = None
    agent_id: Optional[int] = None
    agent_name: Optional[str] = None
    notification_id: Optional[int] = None
    notification_guid: Optional[str] = None
    notification_name: Optional[str] = None
    role_id: Optional[str] = None
    role_name: Optional[str] = None
    user_role_id: Optional[int] = None
    user_role_name: Optional[str] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UnameNotificationLink':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'agent_id': data.get('agent_id'), 'agent_name': data.get('agent_name'), 'notification_id': data.get('notification_id'), 'notification_guid': data.get('notification_guid'), 'notification_name': data.get('notification_name'), 'role_id': data.get('role_id'), 'role_name': data.get('role_name'), 'user_role_id': data.get('user_role_id'), 'user_role_name': data.get('user_role_name'), '_warning': data.get('_warning')})

@dataclass
class UserCompany:
    company_id: Optional[int] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserCompany':
        if data is None:
            return None
        return cls(**{'company_id': data.get('company_id'), 'user_id': data.get('user_id'), 'name': data.get('name'), '_warning': data.get('_warning')})

@dataclass
class UserDepartment:
    id: Optional[int] = None
    user_id: Optional[int] = None
    user_name: Optional[str] = None
    department_id: Optional[int] = None
    department_name: Optional[str] = None
    is_manager: Optional[bool] = None
    is_azure_department: Optional[bool] = None
    role_id: Optional[int] = None
    role_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserDepartment':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'user_id': data.get('user_id'), 'user_name': data.get('user_name'), 'department_id': data.get('department_id'), 'department_name': data.get('department_name'), 'is_manager': data.get('is_manager'), 'is_azure_department': data.get('is_azure_department'), 'role_id': data.get('role_id'), 'role_name': data.get('role_name')})

@dataclass
class UserPrefs:
    id: Optional[int] = None
    lang: Optional[int] = None
    theme: Optional[str] = None
    userdetails: Optional[Users] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserPrefs':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'lang': data.get('lang'), 'theme': data.get('theme'), 'userdetails': data.get('userdetails')})

@dataclass
class UserRoles:
    guid: Optional[str] = None
    intent: Optional[str] = None
    isimportantcontact2: Optional[bool] = None
    id: Optional[int] = None
    showmeonly: Optional[int] = None
    ischangeapprover2: Optional[bool] = None
    ispoapprover: Optional[bool] = None
    web_access_level: Optional[int] = None
    canadd: Optional[bool] = None
    canviewopps: Optional[bool] = None
    allowviewsitedocs: Optional[bool] = None
    allowviewclientdocs: Optional[bool] = None
    canviewcontracts: Optional[bool] = None
    canaccesscatalog: Optional[bool] = None
    cataloglevel: Optional[int] = None
    canaccessinvoices: Optional[bool] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    device_access_level: Optional[int] = None
    is_integration: Optional[bool] = None
    _warning: Optional[str] = None
    dontackemails2: Optional[bool] = None
    departments: Optional[List[UserDepartment]] = None
    notifications: Optional[List[UnameNotification]] = None
    canuploaddocuments: Optional[bool] = None
    quote_access_level: Optional[int] = None
    approver_note_hint: Optional[str] = None
    log_on_behalf_level: Optional[int] = None
    chat_profile_override: Optional[str] = None
    chat_profile_override_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserRoles':
        if data is None:
            return None
        return cls(**{'guid': data.get('guid'), 'intent': data.get('intent'), 'isimportantcontact2': data.get('isimportantcontact2'), 'id': data.get('id'), 'showmeonly': data.get('showmeonly'), 'ischangeapprover2': data.get('ischangeapprover2'), 'ispoapprover': data.get('ispoapprover'), 'web_access_level': data.get('web_access_level'), 'canadd': data.get('canadd'), 'canviewopps': data.get('canviewopps'), 'allowviewsitedocs': data.get('allowviewsitedocs'), 'allowviewclientdocs': data.get('allowviewclientdocs'), 'canviewcontracts': data.get('canviewcontracts'), 'canaccesscatalog': data.get('canaccesscatalog'), 'cataloglevel': data.get('cataloglevel'), 'canaccessinvoices': data.get('canaccessinvoices'), 'name': data.get('name'), 'notes': data.get('notes'), 'device_access_level': data.get('device_access_level'), 'is_integration': data.get('is_integration'), '_warning': data.get('_warning'), 'dontackemails2': data.get('dontackemails2'), 'departments': data.get('departments'), 'notifications': data.get('notifications'), 'canuploaddocuments': data.get('canuploaddocuments'), 'quote_access_level': data.get('quote_access_level'), 'approver_note_hint': data.get('approver_note_hint'), 'log_on_behalf_level': data.get('log_on_behalf_level'), 'chat_profile_override': data.get('chat_profile_override'), 'chat_profile_override_name': data.get('chat_profile_override_name')})

@dataclass
class UserThirdPartyGroup:
    id: Optional[int] = None
    userid: Optional[int] = None
    thirdpartyid: Optional[str] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserThirdPartyGroup':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'userid': data.get('userid'), 'thirdpartyid': data.get('thirdpartyid'), '_warning': data.get('_warning')})

@dataclass
class Users:
    is_comms_user: Optional[bool] = None
    ischangeapprover2: Optional[bool] = None
    sitephonenumberint: Optional[int] = None
    phonenumberint: Optional[int] = None
    homenumberint: Optional[int] = None
    mobileint: Optional[int] = None
    mobilenumber2int: Optional[int] = None
    faxint: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    site_id: Optional[float] = None
    site_id_int: Optional[int] = None
    site_name: Optional[str] = None
    client_name: Optional[str] = None
    firstname: Optional[str] = None
    surname: Optional[str] = None
    initials: Optional[str] = None
    title: Optional[str] = None
    emailaddress: Optional[str] = None
    email2: Optional[str] = None
    email3: Optional[str] = None
    phonenumber_preferred: Optional[str] = None
    sitephonenumber: Optional[str] = None
    phonenumber: Optional[str] = None
    homenumber: Optional[str] = None
    mobilenumber: Optional[str] = None
    mobilenumber2: Optional[str] = None
    fax: Optional[str] = None
    telpref: Optional[int] = None
    activedirectory_dn: Optional[str] = None
    onpremise_activedirectory_dn: Optional[str] = None
    container_dn: Optional[str] = None
    login: Optional[str] = None
    inactive: Optional[bool] = None
    colour: Optional[str] = None
    isimportantcontact: Optional[bool] = None
    other1: Optional[str] = None
    other2: Optional[str] = None
    other3: Optional[str] = None
    other4: Optional[str] = None
    other5: Optional[str] = None
    notes: Optional[str] = None
    neversendemails: Optional[bool] = None
    default_currency_code: Optional[int] = None
    site_guid: Optional[str] = None
    area_guid: Optional[str] = None
    site_cautomate_guid: Optional[str] = None
    priority_id: Optional[int] = None
    linked_agent_id: Optional[int] = None
    covered_by_contract: Optional[bool] = None
    contract_value: Optional[float] = None
    software_role_name: Optional[str] = None
    customfields: Optional[List[CustomField]] = None
    attachments: Optional[List[Attachment]] = None
    custombuttons: Optional[List[CustomButton]] = None
    relationship_id: Optional[int] = None
    user_relationships: Optional[List[XTypeRole]] = None
    uddevsite: Optional[int] = None
    uddevnum: Optional[int] = None
    uduserid: Optional[int] = None
    userdevicerolecount: Optional[int] = None
    site_hubspot_guid: Optional[str] = None
    isserviceaccount: Optional[bool] = None
    ignoreautomatedbilling: Optional[bool] = None
    isimportantcontact2: Optional[bool] = None
    connectwiseid: Optional[int] = None
    autotaskid: Optional[int] = None
    messagegroup_id: Optional[int] = None
    role_list: Optional[str] = None
    sitetimezone: Optional[str] = None
    client_account_manager_id: Optional[int] = None
    datecreated: Optional[str] = None
    inv1: Optional[int] = None
    inv2: Optional[int] = None
    inv3: Optional[int] = None
    inv4: Optional[int] = None
    slaid: Optional[int] = None
    new_password: Optional[str] = None
    dontackemails: Optional[bool] = None
    web_access_level: Optional[int] = None
    showmeonly: Optional[int] = None
    showrecentonly: Optional[int] = None
    inform: Optional[bool] = None
    inv1site: Optional[int] = None
    inv2site: Optional[int] = None
    inv3site: Optional[int] = None
    inv4site: Optional[int] = None
    inv5: Optional[int] = None
    inv6: Optional[int] = None
    inv7: Optional[int] = None
    inv8: Optional[int] = None
    inv9: Optional[int] = None
    inv10: Optional[int] = None
    inv5site: Optional[int] = None
    inv6site: Optional[int] = None
    inv7site: Optional[int] = None
    inv8site: Optional[int] = None
    inv9site: Optional[int] = None
    inv10site: Optional[int] = None
    informaction: Optional[bool] = None
    informclearance: Optional[bool] = None
    inv11: Optional[int] = None
    inv12: Optional[int] = None
    inv13: Optional[int] = None
    inv14: Optional[int] = None
    inv15: Optional[int] = None
    inv16: Optional[int] = None
    inv17: Optional[int] = None
    inv18: Optional[int] = None
    inv19: Optional[int] = None
    inv20: Optional[int] = None
    inv21: Optional[int] = None
    inv22: Optional[int] = None
    inv23: Optional[int] = None
    inv24: Optional[int] = None
    inv25: Optional[int] = None
    inv11site: Optional[int] = None
    inv12site: Optional[int] = None
    inv13site: Optional[int] = None
    inv14site: Optional[int] = None
    inv15site: Optional[int] = None
    inv16site: Optional[int] = None
    inv17site: Optional[int] = None
    inv18site: Optional[int] = None
    inv19site: Optional[int] = None
    inv20site: Optional[int] = None
    inv21site: Optional[int] = None
    inv22site: Optional[int] = None
    inv23site: Optional[int] = None
    inv24site: Optional[int] = None
    inv25site: Optional[int] = None
    showslatimes: Optional[bool] = None
    canadd: Optional[bool] = None
    allowviewsitedocs: Optional[bool] = None
    third_party_guid: Optional[str] = None
    third_party_sql: Optional[str] = None
    ischangeapprover: Optional[bool] = None
    cancreateuser: Optional[bool] = None
    department: Optional[str] = None
    isheadofdept: Optional[bool] = None
    deputysite: Optional[int] = None
    deputyusername: Optional[str] = None
    cat2: Optional[str] = None
    lastlogindate: Optional[str] = None
    iscontractcontact: Optional[bool] = None
    informnewarea: Optional[bool] = None
    informactionarea: Optional[bool] = None
    informclearancearea: Optional[bool] = None
    disclaimermatchstring: Optional[str] = None
    viewallcleared: Optional[bool] = None
    isexternal: Optional[bool] = None
    question1: Optional[int] = None
    question2: Optional[int] = None
    question3: Optional[int] = None
    question4: Optional[int] = None
    question5: Optional[int] = None
    dontaddtomailinglist: Optional[bool] = None
    caneditwebdetails: Optional[bool] = None
    cataloglevel: Optional[int] = None
    canaccesscatalog: Optional[bool] = None
    hasbeentrained: Optional[bool] = None
    admanager: Optional[str] = None
    canviewcontracts: Optional[bool] = None
    ispoapprover: Optional[bool] = None
    encmethod: Optional[int] = None
    adconnection: Optional[int] = None
    useadlogin: Optional[int] = None
    sendwelcomeemail: Optional[bool] = None
    welcomeemail_template_id: Optional[int] = None
    resetpassword: Optional[bool] = None
    _anonymise: Optional[bool] = None
    _reassign_all_to_user: Optional[int] = None
    ismaincontact: Optional[bool] = None
    primary_address: Optional[AddressStore] = None
    addresses: Optional[List[AddressStore]] = None
    departments: Optional[List[UserDepartment]] = None
    organisation_id: Optional[int] = None
    popup_notes: Optional[List[AreaPopup]] = None
    open_ticket_count: Optional[int] = None
    onhold_ticket_count: Optional[int] = None
    total_ticket_count: Optional[int] = None
    opened_thismonth_count: Optional[int] = None
    _isnew: Optional[bool] = None
    _isimport: Optional[bool] = None
    memberof: Optional[str] = None
    _importtype: Optional[str] = None
    usercompany: Optional[List[UserCompany]] = None
    supplier: Optional[Supplier] = None
    supplier_name: Optional[str] = None
    claims: Optional[List[NHDClaim]] = None
    app_colour: Optional[str] = None
    emailconfirmed: Optional[bool] = None
    agent_app_url: Optional[str] = None
    imagedata: Optional[str] = None
    webannouncement: Optional[str] = None
    cautomateid: Optional[int] = None
    azure_connectionid: Optional[int] = None
    _importtoken: Optional[str] = None
    jira_id: Optional[str] = None
    zapier_client_name: Optional[str] = None
    delegation_activated: Optional[bool] = None
    delegation_timebased: Optional[bool] = None
    delegation_start: Optional[str] = None
    delegation_end: Optional[str] = None
    delegation_user_id: Optional[int] = None
    delegation_user_name: Optional[str] = None
    googleworkplace_id: Optional[str] = None
    isnhserveremaildefault: Optional[bool] = None
    matchprimaryemail: Optional[bool] = None
    servicenow_id: Optional[str] = None
    servicenow_username: Optional[str] = None
    site_servicenow_id: Optional[str] = None
    sgatewayid: Optional[str] = None
    software: Optional[List[DeviceApplications]] = None
    canaccessinvoices: Optional[bool] = None
    samaccountname: Optional[str] = None
    oktaid: Optional[str] = None
    okta_status: Optional[str] = None
    authenticatorapp_configured: Optional[bool] = None
    _revoke_authenticatorapp: Optional[bool] = None
    ulastupdate: Optional[str] = None
    _isopp: Optional[bool] = None
    oppcompanyname: Optional[str] = None
    oppcontactname: Optional[str] = None
    oppemailaddress: Optional[str] = None
    assets: Optional[List[DeviceList]] = None
    locked: Optional[bool] = None
    site_guid2: Optional[str] = None
    allowviewclientdocs: Optional[bool] = None
    azure_tenant_id: Optional[str] = None
    azure_last_login_date: Optional[str] = None
    linked_user_id: Optional[int] = None
    linked_user_name: Optional[str] = None
    hubspot_id: Optional[str] = None
    hubspot_url: Optional[str] = None
    hubspot_dont_sync: Optional[bool] = None
    hubspot_archived: Optional[bool] = None
    passportal_id: Optional[int] = None
    passportal_client_id: Optional[int] = None
    opportunity_id: Optional[int] = None
    _warning: Optional[str] = None
    isuserdetails: Optional[bool] = None
    hudu_url: Optional[str] = None
    sqlimport_id: Optional[int] = None
    sqlimport_user: Optional[str] = None
    unsubscribed: Optional[bool] = None
    canviewopps: Optional[bool] = None
    azure_tenant_domain: Optional[str] = None
    servicenow_companyid: Optional[str] = None
    external_links: Optional[List[ExternalLinkList]] = None
    _match_thirdparty_id: Optional[str] = None
    _match_integration_id: Optional[int] = None
    _match_integration_name: Optional[str] = None
    salesforce_dontsync: Optional[bool] = None
    _hascontactsenabled: Optional[bool] = None
    new_site_name: Optional[str] = None
    _isbatch: Optional[bool] = None
    roles: Optional[List[UserRoles]] = None
    azure_roleid: Optional[int] = None
    add_roles: Optional[List[UserRoles]] = None
    facebook_id: Optional[int] = None
    facebook_username: Optional[str] = None
    twitter_id: Optional[int] = None
    twitter_username: Optional[str] = None
    _merge_user_into: Optional[int] = None
    _email_collision: Optional[int] = None
    _dont_fire_automations: Optional[bool] = None
    device_access_level: Optional[int] = None
    ticket_customfields: Optional[List[CustomField]] = None
    manager_email: Optional[str] = None
    _remove_licenses: Optional[bool] = None
    _remove_license_id: Optional[int] = None
    _new_usersite_only: Optional[bool] = None
    thirdpartygroups: Optional[List[UserThirdPartyGroup]] = None
    linked_sites: Optional[List[ExternalLinkList]] = None
    dontackemails2: Optional[bool] = None
    instagram_id: Optional[int] = None
    instagram_username: Optional[str] = None
    jira_instance: Optional[int] = None
    jira_instance_name: Optional[str] = None
    third_party_id: Optional[str] = None
    no_manager_roleid: Optional[int] = None
    matching_value: Optional[str] = None
    theme: Optional[str] = None
    lang: Optional[str] = None
    gocardless_customfields: Optional[Dict[str, Any]] = None
    service_account_overridden: Optional[bool] = None
    sendaccountsemails: Optional[bool] = None
    extratabs: Optional[List[Tabname]] = None
    informifack: Optional[bool] = None
    informnewareaifack: Optional[bool] = None
    marketing_unsubscribes: Optional[List[MarketingUnsubscribe]] = None
    new_account_name: Optional[str] = None
    prospect_account_id: Optional[int] = None
    open_opportunity_count: Optional[int] = None
    _convert_phonenumbers: Optional[bool] = None
    update_user_tickets: Optional[bool] = None
    check_update_user_tickets: Optional[bool] = None
    canuploaddocuments: Optional[bool] = None
    runbook_button_id: Optional[int] = None
    federated_identity_id: Optional[str] = None
    support_expires: Optional[str] = None
    date_licences_removed: Optional[str] = None
    dynamics_365_crm_details_id: Optional[int] = None
    reason: Optional[str] = None
    quote_access_level: Optional[int] = None
    supplier_id: Optional[int] = None
    azure_hasgroupedsitemappings: Optional[bool] = None
    azure_mapping_id: Optional[int] = None
    user_toplevel_id: Optional[int] = None
    out_of_office_start: Optional[str] = None
    out_of_office_end: Optional[str] = None
    out_of_office_message: Optional[str] = None
    use: Optional[str] = None
    key: Optional[int] = None
    table: Optional[TableEnum] = None
    client_id: Optional[int] = None
    item_tax_code: Optional[int] = None
    automatic_sales_tax: Optional[bool] = None
    client_taxable: Optional[bool] = None
    overridepdftemplatequote: Optional[int] = None
    overridepdftemplatequote_name: Optional[str] = None
    contract_end_date: Optional[str] = None
    okta_id: Optional[str] = None
    azure_id: Optional[str] = None
    user_with_clientsite: Optional[str] = None
    client_automatic_callscript_id: Optional[int] = None
    neversendmarketingemails: Optional[bool] = None
    is_prospect: Optional[bool] = None
    whatsapp_number: Optional[str] = None
    azureoid: Optional[str] = None
    approver_note_hint: Optional[str] = None
    language_id: Optional[int] = None
    date_of_birth: Optional[str] = None
    role_ids: Optional[List[int]] = None
    avalara_tenant: Optional[int] = None
    _importtypeid: Optional[int] = None
    _importthirdpartyid: Optional[str] = None
    new_external_link: Optional[ExternalLinkList] = None
    import_details_id: Optional[int] = None
    _isupdateimport: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Users':
        if data is None:
            return None
        return cls(**{'is_comms_user': data.get('is_comms_user'), 'ischangeapprover2': data.get('ischangeapprover2'), 'sitephonenumberint': data.get('sitephonenumberint'), 'phonenumberint': data.get('phonenumberint'), 'homenumberint': data.get('homenumberint'), 'mobileint': data.get('mobileint'), 'mobilenumber2int': data.get('mobilenumber2int'), 'faxint': data.get('faxint'), 'id': data.get('id'), 'name': data.get('name'), 'site_id': data.get('site_id'), 'site_id_int': data.get('site_id_int'), 'site_name': data.get('site_name'), 'client_name': data.get('client_name'), 'firstname': data.get('firstname'), 'surname': data.get('surname'), 'initials': data.get('initials'), 'title': data.get('title'), 'emailaddress': data.get('emailaddress'), 'email2': data.get('email2'), 'email3': data.get('email3'), 'phonenumber_preferred': data.get('phonenumber_preferred'), 'sitephonenumber': data.get('sitephonenumber'), 'phonenumber': data.get('phonenumber'), 'homenumber': data.get('homenumber'), 'mobilenumber': data.get('mobilenumber'), 'mobilenumber2': data.get('mobilenumber2'), 'fax': data.get('fax'), 'telpref': data.get('telpref'), 'activedirectory_dn': data.get('activedirectory_dn'), 'onpremise_activedirectory_dn': data.get('onpremise_activedirectory_dn'), 'container_dn': data.get('container_dn'), 'login': data.get('login'), 'inactive': data.get('inactive'), 'colour': data.get('colour'), 'isimportantcontact': data.get('isimportantcontact'), 'other1': data.get('other1'), 'other2': data.get('other2'), 'other3': data.get('other3'), 'other4': data.get('other4'), 'other5': data.get('other5'), 'notes': data.get('notes'), 'neversendemails': data.get('neversendemails'), 'default_currency_code': data.get('default_currency_code'), 'site_guid': data.get('site_guid'), 'area_guid': data.get('area_guid'), 'site_cautomate_guid': data.get('site_cautomate_guid'), 'priority_id': data.get('priority_id'), 'linked_agent_id': data.get('linked_agent_id'), 'covered_by_contract': data.get('covered_by_contract'), 'contract_value': data.get('contract_value'), 'software_role_name': data.get('software_role_name'), 'customfields': data.get('customfields'), 'attachments': data.get('attachments'), 'custombuttons': data.get('custombuttons'), 'relationship_id': data.get('relationship_id'), 'user_relationships': data.get('user_relationships'), 'uddevsite': data.get('uddevsite'), 'uddevnum': data.get('uddevnum'), 'uduserid': data.get('uduserid'), 'userdevicerolecount': data.get('userdevicerolecount'), 'site_hubspot_guid': data.get('site_hubspot_guid'), 'isserviceaccount': data.get('isserviceaccount'), 'ignoreautomatedbilling': data.get('ignoreautomatedbilling'), 'isimportantcontact2': data.get('isimportantcontact2'), 'connectwiseid': data.get('connectwiseid'), 'autotaskid': data.get('autotaskid'), 'messagegroup_id': data.get('messagegroup_id'), 'role_list': data.get('role_list'), 'sitetimezone': data.get('sitetimezone'), 'client_account_manager_id': data.get('client_account_manager_id'), 'datecreated': data.get('datecreated'), 'inv1': data.get('inv1'), 'inv2': data.get('inv2'), 'inv3': data.get('inv3'), 'inv4': data.get('inv4'), 'slaid': data.get('slaid'), 'new_password': data.get('new_password'), 'dontackemails': data.get('dontackemails'), 'web_access_level': data.get('web_access_level'), 'showmeonly': data.get('showmeonly'), 'showrecentonly': data.get('showrecentonly'), 'inform': data.get('inform'), 'inv1site': data.get('inv1site'), 'inv2site': data.get('inv2site'), 'inv3site': data.get('inv3site'), 'inv4site': data.get('inv4site'), 'inv5': data.get('inv5'), 'inv6': data.get('inv6'), 'inv7': data.get('inv7'), 'inv8': data.get('inv8'), 'inv9': data.get('inv9'), 'inv10': data.get('inv10'), 'inv5site': data.get('inv5site'), 'inv6site': data.get('inv6site'), 'inv7site': data.get('inv7site'), 'inv8site': data.get('inv8site'), 'inv9site': data.get('inv9site'), 'inv10site': data.get('inv10site'), 'informaction': data.get('informaction'), 'informclearance': data.get('informclearance'), 'inv11': data.get('inv11'), 'inv12': data.get('inv12'), 'inv13': data.get('inv13'), 'inv14': data.get('inv14'), 'inv15': data.get('inv15'), 'inv16': data.get('inv16'), 'inv17': data.get('inv17'), 'inv18': data.get('inv18'), 'inv19': data.get('inv19'), 'inv20': data.get('inv20'), 'inv21': data.get('inv21'), 'inv22': data.get('inv22'), 'inv23': data.get('inv23'), 'inv24': data.get('inv24'), 'inv25': data.get('inv25'), 'inv11site': data.get('inv11site'), 'inv12site': data.get('inv12site'), 'inv13site': data.get('inv13site'), 'inv14site': data.get('inv14site'), 'inv15site': data.get('inv15site'), 'inv16site': data.get('inv16site'), 'inv17site': data.get('inv17site'), 'inv18site': data.get('inv18site'), 'inv19site': data.get('inv19site'), 'inv20site': data.get('inv20site'), 'inv21site': data.get('inv21site'), 'inv22site': data.get('inv22site'), 'inv23site': data.get('inv23site'), 'inv24site': data.get('inv24site'), 'inv25site': data.get('inv25site'), 'showslatimes': data.get('showslatimes'), 'canadd': data.get('canadd'), 'allowviewsitedocs': data.get('allowviewsitedocs'), 'third_party_guid': data.get('third_party_guid'), 'third_party_sql': data.get('third_party_sql'), 'ischangeapprover': data.get('ischangeapprover'), 'cancreateuser': data.get('cancreateuser'), 'department': data.get('department'), 'isheadofdept': data.get('isheadofdept'), 'deputysite': data.get('deputysite'), 'deputyusername': data.get('deputyusername'), 'cat2': data.get('cat2'), 'lastlogindate': data.get('lastlogindate'), 'iscontractcontact': data.get('iscontractcontact'), 'informnewarea': data.get('informnewarea'), 'informactionarea': data.get('informactionarea'), 'informclearancearea': data.get('informclearancearea'), 'disclaimermatchstring': data.get('disclaimermatchstring'), 'viewallcleared': data.get('viewallcleared'), 'isexternal': data.get('isexternal'), 'question1': data.get('question1'), 'question2': data.get('question2'), 'question3': data.get('question3'), 'question4': data.get('question4'), 'question5': data.get('question5'), 'dontaddtomailinglist': data.get('dontaddtomailinglist'), 'caneditwebdetails': data.get('caneditwebdetails'), 'cataloglevel': data.get('cataloglevel'), 'canaccesscatalog': data.get('canaccesscatalog'), 'hasbeentrained': data.get('hasbeentrained'), 'admanager': data.get('admanager'), 'canviewcontracts': data.get('canviewcontracts'), 'ispoapprover': data.get('ispoapprover'), 'encmethod': data.get('encmethod'), 'adconnection': data.get('adconnection'), 'useadlogin': data.get('useadlogin'), 'sendwelcomeemail': data.get('sendwelcomeemail'), 'welcomeemail_template_id': data.get('welcomeemail_template_id'), 'resetpassword': data.get('resetpassword'), '_anonymise': data.get('_anonymise'), '_reassign_all_to_user': data.get('_reassign_all_to_user'), 'ismaincontact': data.get('ismaincontact'), 'primary_address': data.get('primary_address'), 'addresses': data.get('addresses'), 'departments': data.get('departments'), 'organisation_id': data.get('organisation_id'), 'popup_notes': data.get('popup_notes'), 'open_ticket_count': data.get('open_ticket_count'), 'onhold_ticket_count': data.get('onhold_ticket_count'), 'total_ticket_count': data.get('total_ticket_count'), 'opened_thismonth_count': data.get('opened_thismonth_count'), '_isnew': data.get('_isnew'), '_isimport': data.get('_isimport'), 'memberof': data.get('memberof'), '_importtype': data.get('_importtype'), 'usercompany': data.get('usercompany'), 'supplier': data.get('supplier'), 'supplier_name': data.get('supplier_name'), 'claims': data.get('claims'), 'app_colour': data.get('app_colour'), 'emailconfirmed': data.get('emailconfirmed'), 'agent_app_url': data.get('agent_app_url'), 'imagedata': data.get('imagedata'), 'webannouncement': data.get('webannouncement'), 'cautomateid': data.get('cautomateid'), 'azure_connectionid': data.get('azure_connectionid'), '_importtoken': data.get('_importtoken'), 'jira_id': data.get('jira_id'), 'zapier_client_name': data.get('zapier_client_name'), 'delegation_activated': data.get('delegation_activated'), 'delegation_timebased': data.get('delegation_timebased'), 'delegation_start': data.get('delegation_start'), 'delegation_end': data.get('delegation_end'), 'delegation_user_id': data.get('delegation_user_id'), 'delegation_user_name': data.get('delegation_user_name'), 'googleworkplace_id': data.get('googleworkplace_id'), 'isnhserveremaildefault': data.get('isnhserveremaildefault'), 'matchprimaryemail': data.get('matchprimaryemail'), 'servicenow_id': data.get('servicenow_id'), 'servicenow_username': data.get('servicenow_username'), 'site_servicenow_id': data.get('site_servicenow_id'), 'sgatewayid': data.get('sgatewayid'), 'software': data.get('software'), 'canaccessinvoices': data.get('canaccessinvoices'), 'samaccountname': data.get('samaccountname'), 'oktaid': data.get('oktaid'), 'okta_status': data.get('okta_status'), 'authenticatorapp_configured': data.get('authenticatorapp_configured'), '_revoke_authenticatorapp': data.get('_revoke_authenticatorapp'), 'ulastupdate': data.get('ulastupdate'), '_isopp': data.get('_isopp'), 'oppcompanyname': data.get('oppcompanyname'), 'oppcontactname': data.get('oppcontactname'), 'oppemailaddress': data.get('oppemailaddress'), 'assets': data.get('assets'), 'locked': data.get('locked'), 'site_guid2': data.get('site_guid2'), 'allowviewclientdocs': data.get('allowviewclientdocs'), 'azure_tenant_id': data.get('azure_tenant_id'), 'azure_last_login_date': data.get('azure_last_login_date'), 'linked_user_id': data.get('linked_user_id'), 'linked_user_name': data.get('linked_user_name'), 'hubspot_id': data.get('hubspot_id'), 'hubspot_url': data.get('hubspot_url'), 'hubspot_dont_sync': data.get('hubspot_dont_sync'), 'hubspot_archived': data.get('hubspot_archived'), 'passportal_id': data.get('passportal_id'), 'passportal_client_id': data.get('passportal_client_id'), 'opportunity_id': data.get('opportunity_id'), '_warning': data.get('_warning'), 'isuserdetails': data.get('isuserdetails'), 'hudu_url': data.get('hudu_url'), 'sqlimport_id': data.get('sqlimport_id'), 'sqlimport_user': data.get('sqlimport_user'), 'unsubscribed': data.get('unsubscribed'), 'canviewopps': data.get('canviewopps'), 'azure_tenant_domain': data.get('azure_tenant_domain'), 'servicenow_companyid': data.get('servicenow_companyid'), 'external_links': data.get('external_links'), '_match_thirdparty_id': data.get('_match_thirdparty_id'), '_match_integration_id': data.get('_match_integration_id'), '_match_integration_name': data.get('_match_integration_name'), 'salesforce_dontsync': data.get('salesforce_dontsync'), '_hascontactsenabled': data.get('_hascontactsenabled'), 'new_site_name': data.get('new_site_name'), '_isbatch': data.get('_isbatch'), 'roles': data.get('roles'), 'azure_roleid': data.get('azure_roleid'), 'add_roles': data.get('add_roles'), 'facebook_id': data.get('facebook_id'), 'facebook_username': data.get('facebook_username'), 'twitter_id': data.get('twitter_id'), 'twitter_username': data.get('twitter_username'), '_merge_user_into': data.get('_merge_user_into'), '_email_collision': data.get('_email_collision'), '_dont_fire_automations': data.get('_dont_fire_automations'), 'device_access_level': data.get('device_access_level'), 'ticket_customfields': data.get('ticket_customfields'), 'manager_email': data.get('manager_email'), '_remove_licenses': data.get('_remove_licenses'), '_remove_license_id': data.get('_remove_license_id'), '_new_usersite_only': data.get('_new_usersite_only'), 'thirdpartygroups': data.get('thirdpartygroups'), 'linked_sites': data.get('linked_sites'), 'dontackemails2': data.get('dontackemails2'), 'instagram_id': data.get('instagram_id'), 'instagram_username': data.get('instagram_username'), 'jira_instance': data.get('jira_instance'), 'jira_instance_name': data.get('jira_instance_name'), 'third_party_id': data.get('third_party_id'), 'no_manager_roleid': data.get('no_manager_roleid'), 'matching_value': data.get('matching_value'), 'theme': data.get('theme'), 'lang': data.get('lang'), 'gocardless_customfields': data.get('gocardless_customfields'), 'service_account_overridden': data.get('service_account_overridden'), 'sendaccountsemails': data.get('sendaccountsemails'), 'extratabs': data.get('extratabs'), 'informifack': data.get('informifack'), 'informnewareaifack': data.get('informnewareaifack'), 'marketing_unsubscribes': data.get('marketing_unsubscribes'), 'new_account_name': data.get('new_account_name'), 'prospect_account_id': data.get('prospect_account_id'), 'open_opportunity_count': data.get('open_opportunity_count'), '_convert_phonenumbers': data.get('_convert_phonenumbers'), 'update_user_tickets': data.get('update_user_tickets'), 'check_update_user_tickets': data.get('check_update_user_tickets'), 'canuploaddocuments': data.get('canuploaddocuments'), 'runbook_button_id': data.get('runbook_button_id'), 'federated_identity_id': data.get('federated_identity_id'), 'support_expires': data.get('support_expires'), 'date_licences_removed': data.get('date_licences_removed'), 'dynamics_365_crm_details_id': data.get('dynamics_365_crm_details_id'), 'reason': data.get('reason'), 'quote_access_level': data.get('quote_access_level'), 'supplier_id': data.get('supplier_id'), 'azure_hasgroupedsitemappings': data.get('azure_hasgroupedsitemappings'), 'azure_mapping_id': data.get('azure_mapping_id'), 'user_toplevel_id': data.get('user_toplevel_id'), 'out_of_office_start': data.get('out_of_office_start'), 'out_of_office_end': data.get('out_of_office_end'), 'out_of_office_message': data.get('out_of_office_message'), 'use': data.get('use'), 'key': data.get('key'), 'table': data.get('table'), 'client_id': data.get('client_id'), 'item_tax_code': data.get('item_tax_code'), 'automatic_sales_tax': data.get('automatic_sales_tax'), 'client_taxable': data.get('client_taxable'), 'overridepdftemplatequote': data.get('overridepdftemplatequote'), 'overridepdftemplatequote_name': data.get('overridepdftemplatequote_name'), 'contract_end_date': data.get('contract_end_date'), 'okta_id': data.get('okta_id'), 'azure_id': data.get('azure_id'), 'user_with_clientsite': data.get('user_with_clientsite'), 'client_automatic_callscript_id': data.get('client_automatic_callscript_id'), 'neversendmarketingemails': data.get('neversendmarketingemails'), 'is_prospect': data.get('is_prospect'), 'whatsapp_number': data.get('whatsapp_number'), 'azureoid': data.get('azureoid'), 'approver_note_hint': data.get('approver_note_hint'), 'language_id': data.get('language_id'), 'date_of_birth': data.get('date_of_birth'), 'role_ids': data.get('role_ids'), 'avalara_tenant': data.get('avalara_tenant'), '_importtypeid': data.get('_importtypeid'), '_importthirdpartyid': data.get('_importthirdpartyid'), 'new_external_link': data.get('new_external_link'), 'import_details_id': data.get('import_details_id'), '_isupdateimport': data.get('_isupdateimport')})

@dataclass
class UsersView:
    page_no: Optional[int] = None
    page_size: Optional[int] = None
    record_count: Optional[int] = None
    users: Optional[List[UsersList]] = None
    columns_id: Optional[int] = None
    columns_tilehtml: Optional[str] = None
    columns: Optional[List[ViewColumnsDetails]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UsersView':
        if data is None:
            return None
        return cls(**{'page_no': data.get('page_no'), 'page_size': data.get('page_size'), 'record_count': data.get('record_count'), 'users': data.get('users'), 'columns_id': data.get('columns_id'), 'columns_tilehtml': data.get('columns_tilehtml'), 'columns': data.get('columns')})

@dataclass
class XTypeRole:
    id: Optional[int] = None
    xtype_id: Optional[int] = None
    name: Optional[str] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'XTypeRole':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'xtype_id': data.get('xtype_id'), 'name': data.get('name'), '_warning': data.get('_warning')})

def list_users(client, **kwargs):
    """List of Users"""
    url = f'{client.base_url}/Users'
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

def create_users(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Users"""
    url = f'{client.base_url}/Users'
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

def list_mes_2(client, **kwargs):
    """GET /Users/me"""
    url = f'{client.base_url}/Users/me'
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

def create_prefs(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Users/prefs"""
    url = f'{client.base_url}/Users/prefs'
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

def get_users(client, id: str, **kwargs):
    """Get one Users"""
    url = f'{client.base_url}/Users/{id}'
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

def delete_users(client, id: str, **kwargs):
    """DELETE /Users/{id}"""
    url = f'{client.base_url}/Users/{id}'
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
