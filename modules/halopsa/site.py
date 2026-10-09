"""modules.halopsa_split.site — Site endpoints + DTOs."""

from __future__ import annotations

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

from modules.halopsa._common import _HaloAPIClient, DotDict, SDKError

@dataclass
class BusinessCentralCustomer:
    odataetag: Optional[str] = None
    id: Optional[str] = None
    number: Optional[str] = None
    display_name: Optional[str] = None
    type: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    salesperson_code: Optional[str] = None
    balance_due: Optional[float] = None
    credit_limit: Optional[int] = None
    tax_liable: Optional[bool] = None
    tax_area_id: Optional[str] = None
    tax_area_display_name: Optional[str] = None
    tax_registration_number: Optional[str] = None
    currency_id: Optional[str] = None
    currency_code: Optional[str] = None
    payment_terms_id: Optional[str] = None
    shipment_method_id: Optional[str] = None
    payment_method_id: Optional[str] = None
    blocked: Optional[str] = None
    last_modified_date_time: Optional[str] = None
    template_code: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BusinessCentralCustomer':
        if data is None:
            return None
        return cls(**{'odataetag': data.get('odataetag'), 'id': data.get('id'), 'number': data.get('number'), 'display_name': data.get('displayName'), 'type': data.get('type'), 'address_line1': data.get('addressLine1'), 'address_line2': data.get('addressLine2'), 'city': data.get('city'), 'state': data.get('state'), 'country': data.get('country'), 'postal_code': data.get('postalCode'), 'phone_number': data.get('phoneNumber'), 'email': data.get('email'), 'website': data.get('website'), 'salesperson_code': data.get('salespersonCode'), 'balance_due': data.get('balanceDue'), 'credit_limit': data.get('creditLimit'), 'tax_liable': data.get('taxLiable'), 'tax_area_id': data.get('taxAreaId'), 'tax_area_display_name': data.get('taxAreaDisplayName'), 'tax_registration_number': data.get('taxRegistrationNumber'), 'currency_id': data.get('currencyId'), 'currency_code': data.get('currencyCode'), 'payment_terms_id': data.get('paymentTermsId'), 'shipment_method_id': data.get('shipmentMethodId'), 'payment_method_id': data.get('paymentMethodId'), 'blocked': data.get('blocked'), 'last_modified_date_time': data.get('lastModifiedDateTime'), 'template_code': data.get('templateCode')})

@dataclass
class Site:
    accountsid: Optional[str] = None
    accountsfirstname: Optional[str] = None
    accountslastname: Optional[str] = None
    accountsemailaddress: Optional[str] = None
    accountsccemailaddress: Optional[str] = None
    accountsbccemailaddress: Optional[str] = None
    sitephonenumberint: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    client_id: Optional[float] = None
    client_name: Optional[str] = None
    clientsite_name: Optional[str] = None
    inactive: Optional[bool] = None
    sla_id: Optional[int] = None
    phonenumber: Optional[str] = None
    colour: Optional[str] = None
    timezone: Optional[str] = None
    invoice_address_isdelivery: Optional[bool] = None
    notes: Optional[str] = None
    isstocklocation: Optional[bool] = None
    messagegroup_id: Optional[int] = None
    item_quantity_in_stock: Optional[float] = None
    item_serialised_assets_in_stock: Optional[float] = None
    item_quantity_reserved: Optional[float] = None
    item_quantity_reserved_on_order: Optional[float] = None
    item_quantity_available: Optional[float] = None
    datecreated: Optional[str] = None
    text: Optional[float] = None
    globx: Optional[float] = None
    globy: Optional[float] = None
    style: Optional[float] = None
    inuseby: Optional[int] = None
    upwho: Optional[float] = None
    uptimestamp: Optional[str] = None
    xrefsite: Optional[float] = None
    zoffsetx: Optional[int] = None
    zoffsety: Optional[int] = None
    zoomx: Optional[float] = None
    zoomy: Optional[float] = None
    smallx: Optional[int] = None
    smally: Optional[int] = None
    bigx: Optional[int] = None
    bigy: Optional[int] = None
    ldapstring: Optional[str] = None
    emaildomain: Optional[str] = None
    deliverby: Optional[int] = None
    isinvoicesite: Optional[bool] = None
    refnumber: Optional[int] = None
    defaultdelivery: Optional[bool] = None
    seriousnesslevel: Optional[int] = None
    geocoord1: Optional[float] = None
    geocoord2: Optional[float] = None
    todomain: Optional[str] = None
    defaultstocklocation: Optional[int] = None
    stopped: Optional[int] = None
    sitetimeoffset: Optional[int] = None
    sitedateformat: Optional[int] = None
    disclaimermatchstring: Optional[str] = None
    emailsubjectprefix: Optional[str] = None
    regionaldirector: Optional[int] = None
    facilitiesmanager: Optional[int] = None
    actguid: Optional[str] = None
    teamviewerpassword: Optional[str] = None
    contractlastchecked: Optional[str] = None
    wildcardref: Optional[str] = None
    monthlyreportlastrun: Optional[str] = None
    monthlyreportinclude: Optional[bool] = None
    monthlyreportemailmanager: Optional[bool] = None
    accountmanagertech: Optional[bool] = None
    monthlyreportemaildirect: Optional[bool] = None
    language_id: Optional[int] = None
    language_name: Optional[str] = None
    snowname: Optional[str] = None
    linked_organisation_id: Optional[int] = None
    slocked: Optional[bool] = None
    newsite_contactname: Optional[str] = None
    newsite_contactemail: Optional[str] = None
    newsite_contactphonenumber: Optional[str] = None
    newsite_contacttitle: Optional[str] = None
    newsite_web_access_level: Optional[int] = None
    newsite_sendwelcomeemail: Optional[bool] = None
    delivery_address: Optional[AddressStore] = None
    invoice_address: Optional[AddressStore] = None
    popup_notes: Optional[List[AreaPopup]] = None
    _reassign_all_to_user: Optional[int] = None
    fields: Optional[List[FieldHelper]] = None
    open_ticket_count: Optional[int] = None
    onhold_ticket_count: Optional[int] = None
    total_ticket_count: Optional[int] = None
    opened_thismonth_count: Optional[int] = None
    guid: Optional[str] = None
    sitecontacts: Optional[List[SiteContact]] = None
    _isimport: Optional[bool] = None
    cautomateid: Optional[int] = None
    ninjarmmid: Optional[int] = None
    _importtype: Optional[str] = None
    _isxero: Optional[bool] = None
    _match_first_site: Optional[bool] = None
    servicenowid: Optional[str] = None
    isnhserveremaildefault: Optional[bool] = None
    device42id: Optional[int] = None
    datto_id: Optional[str] = None
    datto_alternate_id: Optional[int] = None
    datto_url: Optional[str] = None
    connectwiseid: Optional[int] = None
    azuretenantid: Optional[str] = None
    autotaskid: Optional[int] = None
    pagerdutywildcard: Optional[str] = None
    ateraid: Optional[int] = None
    slastupdate: Optional[str] = None
    site_service_tax_code: Optional[int] = None
    site_prepay_tax_code: Optional[int] = None
    site_contract_tax_code: Optional[int] = None
    site_item_tax_code_name: Optional[str] = None
    site_service_tax_code_name: Optional[str] = None
    site_contract_tax_code_name: Optional[str] = None
    site_prepay_tax_code_name: Optional[str] = None
    site_sales_tax_code: Optional[int] = None
    site_purchase_tax_code: Optional[int] = None
    site_purchase_tax_code_name: Optional[str] = None
    syncroid: Optional[int] = None
    third_party_client_name: Optional[str] = None
    auvik_id: Optional[str] = None
    faqlists: Optional[List[FaqListHead]] = None
    all_faqlists_allowed: Optional[bool] = None
    hubspot_id: Optional[str] = None
    passportal_id: Optional[int] = None
    import_site_mapping: Optional[int] = None
    _warning: Optional[str] = None
    issitedetails: Optional[bool] = None
    hudu_url: Optional[str] = None
    liongardid: Optional[int] = None
    kaseyaid: Optional[str] = None
    surchargeid: Optional[int] = None
    country_code: Optional[str] = None
    region_code: Optional[int] = None
    ncentral_details_id: Optional[int] = None
    new_external_link: Optional[ExternalLinkList] = None
    _match_thirdparty_id: Optional[str] = None
    _match_integration_id: Optional[int] = None
    _match_integration_name: Optional[str] = None
    import_details_id: Optional[int] = None
    hasitemsinstock: Optional[bool] = None
    _dont_fire_automations: Optional[bool] = None
    sqlimport_id: Optional[int] = None
    matching_value: Optional[str] = None
    lapsafe_default_installation_name: Optional[str] = None
    lapsafe_default_installation_obj: Optional[KeyPair2] = None
    external_links: Optional[List[ExternalLinkList]] = None
    extratabs: Optional[List[Tabname]] = None
    businesscentral_area_company_id: Optional[int] = None
    businesscentral_billing_client: Optional[BusinessCentralCustomer] = None
    _convert_phonenumbers: Optional[bool] = None
    sequence: Optional[int] = None
    authrocket_locale: Optional[str] = None
    taxable: Optional[int] = None
    default_currency_code_name: Optional[str] = None
    clients: Optional[List[Area]] = None
    audit_log: Optional[List[Audit]] = None
    maintenance_windows: Optional[List[Holidays]] = None
    runbook_button_id: Optional[int] = None
    use: Optional[str] = None
    customfields: Optional[List[CustomField]] = None
    site_fields: Optional[List[FieldHelper]] = None
    gfisiteid: Optional[int] = None
    delivery_address_line1: Optional[str] = None
    delivery_address_line2: Optional[str] = None
    delivery_address_line3: Optional[str] = None
    delivery_address_line4: Optional[str] = None
    delivery_address_line5: Optional[str] = None
    invoice_address_line1: Optional[str] = None
    invoice_address_line2: Optional[str] = None
    invoice_address_line3: Optional[str] = None
    invoice_address_line4: Optional[str] = None
    invoice_address_line5: Optional[str] = None
    itglue_id: Optional[str] = None
    client_itglue_id: Optional[str] = None
    custombuttons: Optional[List[CustomButton]] = None
    stockbin_id: Optional[int] = None
    stockbin_name: Optional[str] = None
    country_code_name: Optional[str] = None
    region_code_name: Optional[str] = None
    ref: Optional[str] = None
    lapsafe_default_installation: Optional[str] = None
    maincontact_id: Optional[int] = None
    maincontact_name: Optional[str] = None
    site_item_tax_code: Optional[int] = None
    stockbins: Optional[List[StockBin]] = None
    default_currency_code: Optional[int] = None
    default_client_currency_code: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Site':
        if data is None:
            return None
        return cls(**{'accountsid': data.get('accountsid'), 'accountsfirstname': data.get('accountsfirstname'), 'accountslastname': data.get('accountslastname'), 'accountsemailaddress': data.get('accountsemailaddress'), 'accountsccemailaddress': data.get('accountsccemailaddress'), 'accountsbccemailaddress': data.get('accountsbccemailaddress'), 'sitephonenumberint': data.get('sitephonenumberint'), 'id': data.get('id'), 'name': data.get('name'), 'client_id': data.get('client_id'), 'client_name': data.get('client_name'), 'clientsite_name': data.get('clientsite_name'), 'inactive': data.get('inactive'), 'sla_id': data.get('sla_id'), 'phonenumber': data.get('phonenumber'), 'colour': data.get('colour'), 'timezone': data.get('timezone'), 'invoice_address_isdelivery': data.get('invoice_address_isdelivery'), 'notes': data.get('notes'), 'isstocklocation': data.get('isstocklocation'), 'messagegroup_id': data.get('messagegroup_id'), 'item_quantity_in_stock': data.get('item_quantity_in_stock'), 'item_serialised_assets_in_stock': data.get('item_serialised_assets_in_stock'), 'item_quantity_reserved': data.get('item_quantity_reserved'), 'item_quantity_reserved_on_order': data.get('item_quantity_reserved_on_order'), 'item_quantity_available': data.get('item_quantity_available'), 'datecreated': data.get('datecreated'), 'text': data.get('text'), 'globx': data.get('globx'), 'globy': data.get('globy'), 'style': data.get('style'), 'inuseby': data.get('inuseby'), 'upwho': data.get('upwho'), 'uptimestamp': data.get('uptimestamp'), 'xrefsite': data.get('xrefsite'), 'zoffsetx': data.get('zoffsetx'), 'zoffsety': data.get('zoffsety'), 'zoomx': data.get('zoomx'), 'zoomy': data.get('zoomy'), 'smallx': data.get('smallx'), 'smally': data.get('smally'), 'bigx': data.get('bigx'), 'bigy': data.get('bigy'), 'ldapstring': data.get('ldapstring'), 'emaildomain': data.get('emaildomain'), 'deliverby': data.get('deliverby'), 'isinvoicesite': data.get('isinvoicesite'), 'refnumber': data.get('refnumber'), 'defaultdelivery': data.get('defaultdelivery'), 'seriousnesslevel': data.get('seriousnesslevel'), 'geocoord1': data.get('geocoord1'), 'geocoord2': data.get('geocoord2'), 'todomain': data.get('todomain'), 'defaultstocklocation': data.get('defaultstocklocation'), 'stopped': data.get('stopped'), 'sitetimeoffset': data.get('sitetimeoffset'), 'sitedateformat': data.get('sitedateformat'), 'disclaimermatchstring': data.get('disclaimermatchstring'), 'emailsubjectprefix': data.get('emailsubjectprefix'), 'regionaldirector': data.get('regionaldirector'), 'facilitiesmanager': data.get('facilitiesmanager'), 'actguid': data.get('actguid'), 'teamviewerpassword': data.get('teamviewerpassword'), 'contractlastchecked': data.get('contractlastchecked'), 'wildcardref': data.get('wildcardref'), 'monthlyreportlastrun': data.get('monthlyreportlastrun'), 'monthlyreportinclude': data.get('monthlyreportinclude'), 'monthlyreportemailmanager': data.get('monthlyreportemailmanager'), 'accountmanagertech': data.get('accountmanagertech'), 'monthlyreportemaildirect': data.get('monthlyreportemaildirect'), 'language_id': data.get('language_id'), 'language_name': data.get('language_name'), 'snowname': data.get('snowname'), 'linked_organisation_id': data.get('linked_organisation_id'), 'slocked': data.get('slocked'), 'newsite_contactname': data.get('newsite_contactname'), 'newsite_contactemail': data.get('newsite_contactemail'), 'newsite_contactphonenumber': data.get('newsite_contactphonenumber'), 'newsite_contacttitle': data.get('newsite_contacttitle'), 'newsite_web_access_level': data.get('newsite_web_access_level'), 'newsite_sendwelcomeemail': data.get('newsite_sendwelcomeemail'), 'delivery_address': data.get('delivery_address'), 'invoice_address': data.get('invoice_address'), 'popup_notes': data.get('popup_notes'), '_reassign_all_to_user': data.get('_reassign_all_to_user'), 'fields': data.get('fields'), 'open_ticket_count': data.get('open_ticket_count'), 'onhold_ticket_count': data.get('onhold_ticket_count'), 'total_ticket_count': data.get('total_ticket_count'), 'opened_thismonth_count': data.get('opened_thismonth_count'), 'guid': data.get('guid'), 'sitecontacts': data.get('sitecontacts'), '_isimport': data.get('_isimport'), 'cautomateid': data.get('cautomateid'), 'ninjarmmid': data.get('ninjarmmid'), '_importtype': data.get('_importtype'), '_isxero': data.get('_isxero'), '_match_first_site': data.get('_match_first_site'), 'servicenowid': data.get('servicenowid'), 'isnhserveremaildefault': data.get('isnhserveremaildefault'), 'device42id': data.get('device42id'), 'datto_id': data.get('datto_id'), 'datto_alternate_id': data.get('datto_alternate_id'), 'datto_url': data.get('datto_url'), 'connectwiseid': data.get('connectwiseid'), 'azuretenantid': data.get('azuretenantid'), 'autotaskid': data.get('autotaskid'), 'pagerdutywildcard': data.get('pagerdutywildcard'), 'ateraid': data.get('ateraid'), 'slastupdate': data.get('slastupdate'), 'site_service_tax_code': data.get('site_service_tax_code'), 'site_prepay_tax_code': data.get('site_prepay_tax_code'), 'site_contract_tax_code': data.get('site_contract_tax_code'), 'site_item_tax_code_name': data.get('site_item_tax_code_name'), 'site_service_tax_code_name': data.get('site_service_tax_code_name'), 'site_contract_tax_code_name': data.get('site_contract_tax_code_name'), 'site_prepay_tax_code_name': data.get('site_prepay_tax_code_name'), 'site_sales_tax_code': data.get('site_sales_tax_code'), 'site_purchase_tax_code': data.get('site_purchase_tax_code'), 'site_purchase_tax_code_name': data.get('site_purchase_tax_code_name'), 'syncroid': data.get('syncroid'), 'third_party_client_name': data.get('third_party_client_name'), 'auvik_id': data.get('auvik_id'), 'faqlists': data.get('faqlists'), 'all_faqlists_allowed': data.get('all_faqlists_allowed'), 'hubspot_id': data.get('hubspot_id'), 'passportal_id': data.get('passportal_id'), 'import_site_mapping': data.get('import_site_mapping'), '_warning': data.get('_warning'), 'issitedetails': data.get('issitedetails'), 'hudu_url': data.get('hudu_url'), 'liongardid': data.get('liongardid'), 'kaseyaid': data.get('kaseyaid'), 'surchargeid': data.get('surchargeid'), 'country_code': data.get('country_code'), 'region_code': data.get('region_code'), 'ncentral_details_id': data.get('ncentral_details_id'), 'new_external_link': data.get('new_external_link'), '_match_thirdparty_id': data.get('_match_thirdparty_id'), '_match_integration_id': data.get('_match_integration_id'), '_match_integration_name': data.get('_match_integration_name'), 'import_details_id': data.get('import_details_id'), 'hasitemsinstock': data.get('hasitemsinstock'), '_dont_fire_automations': data.get('_dont_fire_automations'), 'sqlimport_id': data.get('sqlimport_id'), 'matching_value': data.get('matching_value'), 'lapsafe_default_installation_name': data.get('lapsafe_default_installation_name'), 'lapsafe_default_installation_obj': data.get('lapsafe_default_installation_obj'), 'external_links': data.get('external_links'), 'extratabs': data.get('extratabs'), 'businesscentral_area_company_id': data.get('businesscentral_area_company_id'), 'businesscentral_billing_client': data.get('businesscentral_billing_client'), '_convert_phonenumbers': data.get('_convert_phonenumbers'), 'sequence': data.get('sequence'), 'authrocket_locale': data.get('authrocket_locale'), 'taxable': data.get('taxable'), 'default_currency_code_name': data.get('default_currency_code_name'), 'clients': data.get('clients'), 'audit_log': data.get('audit_log'), 'maintenance_windows': data.get('maintenance_windows'), 'runbook_button_id': data.get('runbook_button_id'), 'use': data.get('use'), 'customfields': data.get('customfields'), 'site_fields': data.get('site_fields'), 'gfisiteid': data.get('gfisiteid'), 'delivery_address_line1': data.get('delivery_address_line1'), 'delivery_address_line2': data.get('delivery_address_line2'), 'delivery_address_line3': data.get('delivery_address_line3'), 'delivery_address_line4': data.get('delivery_address_line4'), 'delivery_address_line5': data.get('delivery_address_line5'), 'invoice_address_line1': data.get('invoice_address_line1'), 'invoice_address_line2': data.get('invoice_address_line2'), 'invoice_address_line3': data.get('invoice_address_line3'), 'invoice_address_line4': data.get('invoice_address_line4'), 'invoice_address_line5': data.get('invoice_address_line5'), 'itglue_id': data.get('itglue_id'), 'client_itglue_id': data.get('client_itglue_id'), 'custombuttons': data.get('custombuttons'), 'stockbin_id': data.get('stockbin_id'), 'stockbin_name': data.get('stockbin_name'), 'country_code_name': data.get('country_code_name'), 'region_code_name': data.get('region_code_name'), 'ref': data.get('ref'), 'lapsafe_default_installation': data.get('lapsafe_default_installation'), 'maincontact_id': data.get('maincontact_id'), 'maincontact_name': data.get('maincontact_name'), 'site_item_tax_code': data.get('site_item_tax_code'), 'stockbins': data.get('stockbins'), 'default_currency_code': data.get('default_currency_code'), 'default_client_currency_code': data.get('default_client_currency_code')})

@dataclass
class SiteContact:
    id: Optional[int] = None
    site: Optional[int] = None
    uid: Optional[int] = None
    user_name: Optional[str] = None
    user_email: Optional[str] = None
    type: Optional[int] = None
    type_name: Optional[str] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SiteContact':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'site': data.get('site'), 'uid': data.get('uid'), 'user_name': data.get('user_name'), 'user_email': data.get('user_email'), 'type': data.get('type'), 'type_name': data.get('type_name'), '_warning': data.get('_warning')})

@dataclass
class SiteList:
    id: Optional[int] = None
    name: Optional[str] = None
    client_id: Optional[float] = None
    client_name: Optional[str] = None
    clientsite_name: Optional[str] = None
    inactive: Optional[bool] = None
    sla_id: Optional[int] = None
    phonenumber: Optional[str] = None
    colour: Optional[str] = None
    timezone: Optional[str] = None
    invoice_address_isdelivery: Optional[bool] = None
    notes: Optional[str] = None
    isstocklocation: Optional[bool] = None
    messagegroup_id: Optional[int] = None
    item_quantity_in_stock: Optional[float] = None
    item_serialised_assets_in_stock: Optional[float] = None
    item_quantity_reserved: Optional[float] = None
    item_quantity_reserved_on_order: Optional[float] = None
    item_quantity_available: Optional[float] = None
    use: Optional[str] = None
    customfields: Optional[List[CustomField]] = None
    site_fields: Optional[List[FieldHelper]] = None
    gfisiteid: Optional[int] = None
    delivery_address_line1: Optional[str] = None
    delivery_address_line2: Optional[str] = None
    delivery_address_line3: Optional[str] = None
    delivery_address_line4: Optional[str] = None
    delivery_address_line5: Optional[str] = None
    invoice_address_line1: Optional[str] = None
    invoice_address_line2: Optional[str] = None
    invoice_address_line3: Optional[str] = None
    invoice_address_line4: Optional[str] = None
    invoice_address_line5: Optional[str] = None
    itglue_id: Optional[str] = None
    client_itglue_id: Optional[str] = None
    custombuttons: Optional[List[CustomButton]] = None
    stockbin_id: Optional[int] = None
    stockbin_name: Optional[str] = None
    country_code_name: Optional[str] = None
    region_code_name: Optional[str] = None
    ref: Optional[str] = None
    lapsafe_default_installation: Optional[str] = None
    maincontact_id: Optional[int] = None
    maincontact_name: Optional[str] = None
    isinvoicesite: Optional[bool] = None
    site_item_tax_code: Optional[int] = None
    stockbins: Optional[List[StockBin]] = None
    default_currency_code: Optional[int] = None
    default_client_currency_code: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SiteList':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name'), 'client_id': data.get('client_id'), 'client_name': data.get('client_name'), 'clientsite_name': data.get('clientsite_name'), 'inactive': data.get('inactive'), 'sla_id': data.get('sla_id'), 'phonenumber': data.get('phonenumber'), 'colour': data.get('colour'), 'timezone': data.get('timezone'), 'invoice_address_isdelivery': data.get('invoice_address_isdelivery'), 'notes': data.get('notes'), 'isstocklocation': data.get('isstocklocation'), 'messagegroup_id': data.get('messagegroup_id'), 'item_quantity_in_stock': data.get('item_quantity_in_stock'), 'item_serialised_assets_in_stock': data.get('item_serialised_assets_in_stock'), 'item_quantity_reserved': data.get('item_quantity_reserved'), 'item_quantity_reserved_on_order': data.get('item_quantity_reserved_on_order'), 'item_quantity_available': data.get('item_quantity_available'), 'use': data.get('use'), 'customfields': data.get('customfields'), 'site_fields': data.get('site_fields'), 'gfisiteid': data.get('gfisiteid'), 'delivery_address_line1': data.get('delivery_address_line1'), 'delivery_address_line2': data.get('delivery_address_line2'), 'delivery_address_line3': data.get('delivery_address_line3'), 'delivery_address_line4': data.get('delivery_address_line4'), 'delivery_address_line5': data.get('delivery_address_line5'), 'invoice_address_line1': data.get('invoice_address_line1'), 'invoice_address_line2': data.get('invoice_address_line2'), 'invoice_address_line3': data.get('invoice_address_line3'), 'invoice_address_line4': data.get('invoice_address_line4'), 'invoice_address_line5': data.get('invoice_address_line5'), 'itglue_id': data.get('itglue_id'), 'client_itglue_id': data.get('client_itglue_id'), 'custombuttons': data.get('custombuttons'), 'stockbin_id': data.get('stockbin_id'), 'stockbin_name': data.get('stockbin_name'), 'country_code_name': data.get('country_code_name'), 'region_code_name': data.get('region_code_name'), 'ref': data.get('ref'), 'lapsafe_default_installation': data.get('lapsafe_default_installation'), 'maincontact_id': data.get('maincontact_id'), 'maincontact_name': data.get('maincontact_name'), 'isinvoicesite': data.get('isinvoicesite'), 'site_item_tax_code': data.get('site_item_tax_code'), 'stockbins': data.get('stockbins'), 'default_currency_code': data.get('default_currency_code'), 'default_client_currency_code': data.get('default_client_currency_code')})

@dataclass
class SiteView:
    page_no: Optional[int] = None
    page_size: Optional[int] = None
    record_count: Optional[int] = None
    sites: Optional[List[SiteList]] = None
    columns_id: Optional[int] = None
    columns_tilehtml: Optional[str] = None
    columns: Optional[List[ViewColumnsDetails]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SiteView':
        if data is None:
            return None
        return cls(**{'page_no': data.get('page_no'), 'page_size': data.get('page_size'), 'record_count': data.get('record_count'), 'sites': data.get('sites'), 'columns_id': data.get('columns_id'), 'columns_tilehtml': data.get('columns_tilehtml'), 'columns': data.get('columns')})

@dataclass
class StockBin:
    id: Optional[int] = None
    name: Optional[str] = None
    site_id: Optional[int] = None
    _warning: Optional[str] = None
    dont_add_to_order: Optional[bool] = None
    parent_id: Optional[int] = None
    parent_name: Optional[str] = None
    sequence: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'StockBin':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name'), 'site_id': data.get('site_id'), '_warning': data.get('_warning'), 'dont_add_to_order': data.get('dont_add_to_order'), 'parent_id': data.get('parent_id'), 'parent_name': data.get('parent_name'), 'sequence': data.get('sequence')})

def list_sites(client, **kwargs):
    """List of Site"""
    url = f'{client.base_url}/Site'
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

def create_site(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Site"""
    url = f'{client.base_url}/Site'
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

def list_stock_bins(client, **kwargs) -> List[SiteList]:
    """GET /Site/StockBins"""
    url = f'{client.base_url}/Site/StockBins'
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

def get_site(client, id: str, **kwargs):
    """Get one Site"""
    url = f'{client.base_url}/Site/{id}'
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

def delete_site(client, id: str, **kwargs):
    """DELETE /Site/{id}"""
    url = f'{client.base_url}/Site/{id}'
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
