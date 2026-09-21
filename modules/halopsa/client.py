"""modules.halopsa_split.client — Client endpoints + DTOs."""

from __future__ import annotations

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

from modules.halopsa._common import _HaloAPIClient, DotDict, SDKError

@dataclass
class AddressStore:
    id: Optional[int] = None
    type: Optional[int] = None
    description: Optional[str] = None
    note: Optional[str] = None
    line1: Optional[str] = None
    line2: Optional[str] = None
    line3: Optional[str] = None
    line4: Optional[str] = None
    postcode: Optional[str] = None
    primary: Optional[bool] = None
    inactive: Optional[bool] = None
    date_active: Optional[str] = None
    date_inactive: Optional[str] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    client_name: Optional[str] = None
    site_id: Optional[int] = None
    site_name: Optional[str] = None
    user_id: Optional[int] = None
    user_name: Optional[str] = None
    user_email: Optional[str] = None
    _isimport: Optional[bool] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AddressStore':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'type': data.get('type'), 'description': data.get('description'), 'note': data.get('note'), 'line1': data.get('line1'), 'line2': data.get('line2'), 'line3': data.get('line3'), 'line4': data.get('line4'), 'postcode': data.get('postcode'), 'primary': data.get('primary'), 'inactive': data.get('inactive'), 'date_active': data.get('date_active'), 'date_inactive': data.get('date_inactive'), 'lat': data.get('lat'), 'long': data.get('long'), 'client_name': data.get('client_name'), 'site_id': data.get('site_id'), 'site_name': data.get('site_name'), 'user_id': data.get('user_id'), 'user_name': data.get('user_name'), 'user_email': data.get('user_email'), '_isimport': data.get('_isimport'), '_warning': data.get('_warning')})

@dataclass
class Area:
    pax8monthlyinvoice: Optional[int] = None
    pax8annualinvoice: Optional[int] = None
    quickbookstaxexemptionreasonid: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    toplevel_id: Optional[int] = None
    toplevel_name: Optional[str] = None
    inactive: Optional[bool] = None
    colour: Optional[str] = None
    confirmemail: Optional[int] = None
    actionemail: Optional[int] = None
    clearemail: Optional[int] = None
    messagegroup_id: Optional[int] = None
    from_address_override: Optional[str] = None
    override_org_logo: Optional[bool] = None
    override_org_name: Optional[str] = None
    override_org_address: Optional[AddressStore] = None
    override_org_phone: Optional[str] = None
    override_org_email: Optional[str] = None
    override_org_website: Optional[str] = None
    override_org_portalurl: Optional[str] = None
    mailbox_override: Optional[int] = None
    default_mailbox_id: Optional[int] = None
    calldate: Optional[str] = None
    item_tax_code: Optional[int] = None
    service_tax_code: Optional[int] = None
    prepay_tax_code: Optional[int] = None
    contract_tax_code: Optional[int] = None
    customfields: Optional[List[CustomField]] = None
    custombuttons: Optional[List[CustomButton]] = None
    attachments: Optional[List[Attachment]] = None
    site_fields: Optional[List[FieldHelper]] = None
    pritech: Optional[int] = None
    sectech: Optional[int] = None
    accountmanagertech: Optional[int] = None
    notes: Optional[str] = None
    thirdpartynhdapiurl: Optional[str] = None
    xeroid: Optional[str] = None
    open_ticket_count: Optional[int] = None
    opps_ticket_count: Optional[int] = None
    main_site_id: Optional[int] = None
    accountsemailaddress: Optional[str] = None
    accountsccemailaddress: Optional[str] = None
    accountsfirstname: Optional[str] = None
    accountslastname: Optional[str] = None
    datecreated: Optional[str] = None
    createdfrom_id: Optional[int] = None
    announce: Optional[str] = None
    announcedate: Optional[str] = None
    pritech_name: Optional[str] = None
    sectech_name: Optional[str] = None
    prinotify: Optional[bool] = None
    secnotify: Optional[bool] = None
    priassign: Optional[bool] = None
    secassign: Optional[bool] = None
    accountmanagertech_name: Optional[str] = None
    accountmanagertech_email: Optional[str] = None
    chargeperiod: Optional[int] = None
    chargehours: Optional[float] = None
    chargecarryover: Optional[float] = None
    invoiceyes: Optional[bool] = None
    fluserdef1: Optional[str] = None
    fluserdef2: Optional[str] = None
    fluserdef3: Optional[str] = None
    fluserdef4: Optional[str] = None
    fluserdef5: Optional[str] = None
    floverride: Optional[bool] = None
    fluserdef1hide: Optional[bool] = None
    fluserdef2hide: Optional[bool] = None
    fluserdef3hide: Optional[bool] = None
    fluserdef4hide: Optional[bool] = None
    fluserdef5hide: Optional[bool] = None
    fluserdef1mand: Optional[bool] = None
    fluserdef2mand: Optional[bool] = None
    fluserdef3mand: Optional[bool] = None
    fluserdef4mand: Optional[bool] = None
    fluserdef5mand: Optional[bool] = None
    includeactions: Optional[bool] = None
    needsinvoice: Optional[bool] = None
    startdate: Optional[str] = None
    startbalance: Optional[float] = None
    hourlyrate: Optional[float] = None
    periodcharge: Optional[float] = None
    dontinvoice: Optional[bool] = None
    invoicetemplate: Optional[str] = None
    invoicecomment: Optional[str] = None
    lastinvoiceenddate: Optional[str] = None
    showslaonweb: Optional[bool] = None
    item_tax_code_name: Optional[str] = None
    service_tax_code_name: Optional[str] = None
    contract_tax_code_name: Optional[str] = None
    prepay_tax_code_name: Optional[str] = None
    imageindex: Optional[int] = None
    chargehours2: Optional[float] = None
    hourlyrate2: Optional[float] = None
    cat2: Optional[str] = None
    cat3: Optional[str] = None
    cat4: Optional[str] = None
    cat5: Optional[str] = None
    enddate: Optional[str] = None
    ucemail: Optional[int] = None
    fcemail: Optional[int] = None
    actguid: Optional[str] = None
    smsbalance: Optional[int] = None
    html: Optional[str] = None
    hv: Optional[float] = None
    hvdate: Optional[str] = None
    emailinvoice: Optional[bool] = None
    dont_auto_send_invoices: Optional[bool] = None
    seriousnesslevel: Optional[int] = None
    defcat1: Optional[str] = None
    defcat2: Optional[str] = None
    defcat3: Optional[str] = None
    defcat4: Optional[str] = None
    thresholdbreached: Optional[int] = None
    monthlyreportinclude: Optional[bool] = None
    monthlyreportlastrun: Optional[str] = None
    monthlyreportemaildirect: Optional[bool] = None
    monthlyreportemailmanager: Optional[bool] = None
    monthlyreportshowonweb: Optional[bool] = None
    areatype: Optional[int] = None
    unmatchedcombinations: Optional[int] = None
    prepayrecurringchargenextdate: Optional[str] = None
    billforrecurringprepayamount: Optional[bool] = None
    prepayrecurringcharge: Optional[float] = None
    prepayrecurringhours: Optional[float] = None
    prepayrecurringchargebp: Optional[int] = None
    disclaimermatchstring: Optional[str] = None
    paymentterms: Optional[int] = None
    showallnonbillable: Optional[bool] = None
    billinggroup: Optional[int] = None
    autotopupthreshhold: Optional[float] = None
    autotopuptoamount: Optional[float] = None
    autotopupcostperhour: Optional[float] = None
    autotopupbyamount: Optional[float] = None
    surchargeid: Optional[int] = None
    billingtemplate_id: Optional[int] = None
    billingtemplate_name: Optional[str] = None
    overidegreeting: Optional[str] = None
    clientpackage: Optional[int] = None
    scopeofbusiness: Optional[int] = None
    preferredagent: Optional[int] = None
    callhandlingnotes: Optional[str] = None
    automatic_callscript_id: Optional[int] = None
    automatic_callscript_name: Optional[str] = None
    teamviewerpassword: Optional[str] = None
    customertype_new: Optional[str] = None
    discountperc: Optional[float] = None
    showfaqfortoplevel: Optional[bool] = None
    isopportunity: Optional[int] = None
    snowname: Optional[str] = None
    main_site_name: Optional[str] = None
    linked_organisation_id: Optional[int] = None
    all_organisations_allowed: Optional[bool] = None
    allowed_organisations: Optional[List[Organisation]] = None
    override_signature: Optional[str] = None
    contractaccountsdesc: Optional[str] = None
    prepayaccountsdesc: Optional[str] = None
    site_update: Optional[List[Site]] = None
    newclient_sitename: Optional[str] = None
    newclient_phonenumber: Optional[str] = None
    newclient_domain: Optional[str] = None
    newclient_timezone: Optional[str] = None
    newclient_contactname: Optional[str] = None
    newclient_contactemail: Optional[str] = None
    newclient_contactphonenumber: Optional[str] = None
    newclient_contacttitle: Optional[str] = None
    newclient_web_access_level: Optional[int] = None
    newclient_sendwelcomeemail: Optional[bool] = None
    newclient_delivery_address: Optional[AddressStore] = None
    newclient_countrycode: Optional[str] = None
    newclient_regioncode: Optional[int] = None
    faqlists: Optional[List[FaqListHead]] = None
    popup_notes: Optional[List[AreaPopup]] = None
    _reassign_all_to_user: Optional[int] = None
    allowall_tickettypes: Optional[bool] = None
    allowed_tickettypes: Optional[List[RequestTypeList]] = None
    allowall_category1: Optional[bool] = None
    allowed_category1: Optional[List[CategoryRestriction]] = None
    allowall_category2: Optional[bool] = None
    allowed_category2: Optional[List[CategoryRestriction]] = None
    allowall_category3: Optional[bool] = None
    allowed_category3: Optional[List[CategoryRestriction]] = None
    allowall_category4: Optional[bool] = None
    alocked: Optional[bool] = None
    allowed_category4: Optional[List[CategoryRestriction]] = None
    onhold_ticket_count: Optional[int] = None
    total_ticket_count: Optional[int] = None
    opened_thismonth_count: Optional[int] = None
    billingplans: Optional[List[ContractDetail]] = None
    overriding_rates: Optional[List[ChargeRate]] = None
    allowallchargerates: Optional[bool] = None
    chargerates: Optional[List[ChargeRateArea]] = None
    newclient_siteguid: Optional[str] = None
    _isimport: Optional[bool] = None
    _importtype: Optional[str] = None
    allow_api_access: Optional[bool] = None
    api_access_clientid: Optional[str] = None
    api_access_clientsecret: Optional[str] = None
    thirdpartynhdauthurl: Optional[str] = None
    thirdpartynhdtenant: Optional[str] = None
    thirdpartynhdapiclientid: Optional[str] = None
    new_thirdpartynhdapiclientsecret: Optional[str] = None
    areaitems: Optional[List[AreaItem]] = None
    portal_logo: Optional[str] = None
    override_portalcolour: Optional[bool] = None
    portalcolour: Optional[str] = None
    portalbackgroundimageurl: Optional[str] = None
    ninjarmmid: Optional[int] = None
    sales_tax_type: Optional[str] = None
    purchase_tax_type: Optional[str] = None
    isarchived_xero: Optional[bool] = None
    sales_tax_code: Optional[int] = None
    purchase_tax_code: Optional[int] = None
    purchase_tax_code_name: Optional[str] = None
    prepayhistory: Optional[List[PrepayHistory]] = None
    periods: Optional[List[PrepayPeriod]] = None
    prepayrecurringminimumdeduction: Optional[float] = None
    prepayrecurringminimumdeductiononlyactive: Optional[bool] = None
    prepayrecurringautomaticdeduction: Optional[float] = None
    prepaytotal: Optional[float] = None
    prepayused: Optional[float] = None
    prepaybalance: Optional[float] = None
    preferreddeliverymethod: Optional[int] = None
    qbodefaulttax: Optional[int] = None
    default_contract: Optional[int] = None
    device42id: Optional[int] = None
    xerodetails_id: Optional[int] = None
    xero_tenant_name: Optional[str] = None
    xero_tracking_category_1_name: Optional[str] = None
    xero_tracking_category_2_name: Optional[str] = None
    servicenowid: Optional[str] = None
    isnhserveremaildefault: Optional[bool] = None
    datto_id: Optional[str] = None
    datto_alternate_id: Optional[int] = None
    datto_url: Optional[str] = None
    dattocommerce_tenantid: Optional[int] = None
    qbodefaulttaxcode: Optional[int] = None
    qbodefaulttaxcodename: Optional[str] = None
    qbo_default_tax_code: Optional[KeyPair2] = None
    connectwiseid: Optional[int] = None
    autotaskid: Optional[int] = None
    import_address: Optional[AddressStore] = None
    import_notes: Optional[List[AreaNote]] = None
    ateraid: Optional[int] = None
    kashflowid: Optional[int] = None
    kashflow_tenant_name: Optional[str] = None
    website: Optional[str] = None
    alastupdate: Optional[str] = None
    group_service_access: Optional[List[CriteriaGroup]] = None
    group_service_subscriptions: Optional[List[CriteriaGroup]] = None
    snelstart_id: Optional[str] = None
    default_currency_code_name: Optional[str] = None
    _apply_billingtemplate: Optional[bool] = None
    recalculate_billing: Optional[bool] = None
    recalculate_billing_start: Optional[str] = None
    recalculate_billing_end: Optional[str] = None
    datto_commerce_id: Optional[int] = None
    datto_commerce_url: Optional[str] = None
    import_azure_tenant: Optional[CspCustomer] = None
    syncroid: Optional[int] = None
    kbentries: Optional[List[KbEntryList]] = None
    auvik_id: Optional[str] = None
    hubspot_id: Optional[str] = None
    hubspot_url: Optional[str] = None
    hubspot_dont_sync: Optional[bool] = None
    hubspot_archived: Optional[bool] = None
    domain: Optional[str] = None
    passportal_id: Optional[int] = None
    update_licences: Optional[bool] = None
    prepayasamount: Optional[bool] = None
    synced_to_intacct: Optional[bool] = None
    qbo_company_name: Optional[str] = None
    oppid: Optional[int] = None
    tax_number: Optional[str] = None
    isclientdetails: Optional[bool] = None
    hubspot_lifecycle: Optional[str] = None
    hudu_url: Optional[str] = None
    prepayrecurringexpirymonths: Optional[int] = None
    accountsbccemailaddress: Optional[str] = None
    defaultcontractoverride: Optional[int] = None
    defaultcontractoverride_ref: Optional[str] = None
    sqlimport_id: Optional[int] = None
    external_links: Optional[List[ExternalLinkList]] = None
    new_external_link: Optional[ExternalLinkList] = None
    _match_thirdparty_id: Optional[str] = None
    _match_integration_id: Optional[int] = None
    _match_integration_name: Optional[str] = None
    _warning: Optional[str] = None
    donotimport: Optional[bool] = None
    liongardid: Optional[int] = None
    liongard_url: Optional[str] = None
    sync_to_liongard: Optional[bool] = None
    regmanagertech_name: Optional[str] = None
    logmanagertech_name: Optional[str] = None
    salesreptech_name: Optional[str] = None
    default_team_to_salesrep_override: Optional[bool] = None
    default_team_to_salesrep_override_team: Optional[str] = None
    cxmleadtech_name: Optional[str] = None
    portalchatprofile: Optional[str] = None
    portalchatprofile_name: Optional[str] = None
    kaseyaid: Optional[str] = None
    trading_name: Optional[str] = None
    dbc_company_name: Optional[str] = None
    salesforce_dontsync: Optional[bool] = None
    stripe_customer_id: Optional[str] = None
    stripe_payment_method_id: Optional[str] = None
    stripe_payment_method_name: Optional[str] = None
    stripe_paymentmethod: Optional[StripePaymentMethod] = None
    current_licences: Optional[str] = None
    servicenow_url: Optional[str] = None
    servicenow_locale: Optional[str] = None
    servicenow_username: Optional[str] = None
    new_servicenowkey: Optional[str] = None
    servicenow_priority_mappings: Optional[List[IntegrationFieldMapping]] = None
    servicenow_status_mappings: Optional[List[IntegrationFieldMapping]] = None
    servicenow_impact_mappings: Optional[List[IntegrationFieldMapping]] = None
    servicenow_urgency_mappings: Optional[List[IntegrationFieldMapping]] = None
    servicenow_category_mappings: Optional[List[IntegrationFieldMapping]] = None
    servicenow_service_mappings: Optional[List[ServiceMapping]] = None
    servicenow_assignment_group: Optional[str] = None
    servicenow_assignment_group_name: Optional[str] = None
    servicenow_assignmentgroup: Optional[KeyPair2] = None
    servicenow_defaultuser_id: Optional[str] = None
    servicenow_defaultuser_name: Optional[str] = None
    servicenow_defaultuser: Optional[KeyPair2] = None
    test_servicenow: Optional[bool] = None
    sage_business_cloud_details_id: Optional[int] = None
    sage_business_cloud_details_name: Optional[str] = None
    exact_division: Optional[int] = None
    exact_division_name: Optional[str] = None
    ncentral_details_id: Optional[int] = None
    currencyisocode: Optional[str] = None
    intacct_location_id: Optional[str] = None
    intacct_location_id_list: Optional[List[KeyPair2]] = None
    intacct_location_type: Optional[str] = None
    new_categories: Optional[List[str]] = None
    jira_url: Optional[str] = None
    jira_username: Optional[str] = None
    new_jirakey: Optional[str] = None
    test_jira: Optional[bool] = None
    jira_servicedesk_id: Optional[str] = None
    jira_servicedesk_name: Optional[str] = None
    jira_servicedesk: Optional[KeyPair2] = None
    jira_requesttype_mappings: Optional[List[IntegrationFieldMapping]] = None
    jira_user_id: Optional[str] = None
    jira_user_name: Optional[str] = None
    jira_user: Optional[KeyPair2] = None
    jira_priority_mappings: Optional[List[IntegrationFieldMapping]] = None
    jira_status_mappings: Optional[List[IntegrationFieldMapping]] = None
    jira_status_after_update: Optional[int] = None
    create_jira_webhook: Optional[bool] = None
    jira_webhook_created: Optional[bool] = None
    defaultpdftemplateinvoicetickets: Optional[int] = None
    defaultpdftemplateinvoiceorders: Optional[int] = None
    defaultpdftemplateinvoicerecurring: Optional[int] = None
    defaultpdftemplateinvoicetickets_name: Optional[str] = None
    defaultpdftemplateinvoiceorders_name: Optional[str] = None
    defaultpdftemplateinvoicerecurring_name: Optional[str] = None
    intacct_invoice_save_location: Optional[str] = None
    ingram_micro_details_id: Optional[int] = None
    _dont_fire_automations: Optional[bool] = None
    main_delivery_address: Optional[AddressStore] = None
    main_invoice_address: Optional[AddressStore] = None
    main_contact_name: Optional[str] = None
    main_contact_email: Optional[str] = None
    main_contact_phonenumber: Optional[str] = None
    main_contact_id: Optional[int] = None
    main_phonenumber: Optional[str] = None
    auvik_site_inactive: Optional[bool] = None
    invoice_class: Optional[str] = None
    new_icon: Optional[str] = None
    fortnox_tenant: Optional[int] = None
    fortnox_tenant_name: Optional[str] = None
    servicenow_enable_webhook: Optional[bool] = None
    new_servicenow_webhooksecret: Optional[str] = None
    servicenow_webhook_user: Optional[int] = None
    servicenow_webhook_user_name: Optional[str] = None
    servicenow_webhook_tickettype: Optional[int] = None
    servicenow_webhook_tickettype_name: Optional[str] = None
    myob_tenant: Optional[int] = None
    myob_tenant_name: Optional[str] = None
    sync_servicenow_attachments: Optional[int] = None
    twilio_subaccount_name: Optional[str] = None
    twilio_subaccount_created: Optional[bool] = None
    twilio_subaccount_sid: Optional[str] = None
    twilio_subaccount_status: Optional[str] = None
    twilio_subaccount_authtoken: Optional[str] = None
    _create_twilio_subaccount: Optional[bool] = None
    _close_twilio_subaccount: Optional[bool] = None
    _pauseunpause_twilio_subaccount: Optional[bool] = None
    _create_twilio_recurringinvoice: Optional[bool] = None
    twilio_recurring_invoice_id: Optional[int] = None
    override_layout_id: Optional[int] = None
    override_layout_name: Optional[str] = None
    extratabs: Optional[List[Tabname]] = None
    servicenow_team_mappings: Optional[List[IntegrationFieldMapping]] = None
    servicenow_ticket_sync: Optional[str] = None
    servicenow_ticket_sync_list: Optional[List[KeyPair2]] = None
    servicenow_fieldmappings: Optional[List[IntegrationFieldMapping]] = None
    matching_value: Optional[str] = None
    jira_webhook_user: Optional[int] = None
    jira_webhook_username: Optional[str] = None
    avalara_code: Optional[str] = None
    avalara_tenant_name: Optional[str] = None
    avalara_id: Optional[str] = None
    invoice_mailbox_override: Optional[int] = None
    quote_mailbox_override: Optional[int] = None
    _merge_client_into: Optional[int] = None
    invoice_tickets_seperately_override: Optional[bool] = None
    servicenow_authtype: Optional[int] = None
    portal_title_override: Optional[bool] = None
    portal_title: Optional[str] = None
    reply_address_override: Optional[str] = None
    auto_redirect_failed_login: Optional[bool] = None
    exclude_ai_profiling: Optional[bool] = None
    dynamics_365_crm_details_id: Optional[int] = None
    test_thirdpartynhd: Optional[bool] = None
    thirdpartynhd_validated: Optional[bool] = None
    thirdpartynhdcustomfieldmappings: Optional[List[IntegrationFieldMapping]] = None
    thirdpartynhd_status_mappings: Optional[List[IntegrationFieldMapping]] = None
    thirdpartynhd_category_mappings: Optional[List[IntegrationFieldMapping]] = None
    thirdpartynhd_tickettype_mappings: Optional[List[IntegrationFieldMapping]] = None
    thirdpartynhd_outcome_mappings: Optional[List[IntegrationFieldMapping]] = None
    thirdpartynhd_status: Optional[int] = None
    thirdpartynhd_status_name: Optional[str] = None
    thirdpartynhd_category: Optional[int] = None
    thirdpartynhd_category_name: Optional[str] = None
    thirdpartynhd_tickettype: Optional[int] = None
    thirdpartynhd_tickettype_name: Optional[str] = None
    thirdpartynhd_outcome: Optional[int] = None
    thirdpartynhd_outcome_name: Optional[str] = None
    thirdpartynhd_attachments: Optional[int] = None
    apiversion: Optional[str] = None
    audit_log: Optional[List[Audit]] = None
    jira_allow_webhooks: Optional[bool] = None
    jira_webhook_authentication: Optional[int] = None
    new_jira_webhook_secret: Optional[str] = None
    servicenow_sync_child: Optional[bool] = None
    dbc_dimensions: Optional[List[BusinessCentralDimensions]] = None
    dbc_template: Optional[str] = None
    dynamics_dimensions_enabled: Optional[bool] = None
    dynamics_bc_synced: Optional[bool] = None
    runbook_button_id: Optional[int] = None
    use: Optional[str] = None
    key: Optional[int] = None
    table: Optional[TableEnum] = None
    logo: Optional[str] = None
    regmanagertech: Optional[int] = None
    logmanagertech: Optional[int] = None
    salesreptech: Optional[int] = None
    accountownertech: Optional[int] = None
    cxmleadtech: Optional[int] = None
    xero_tenant_id: Optional[str] = None
    accountsid: Optional[str] = None
    excludefrominvoicesync: Optional[bool] = None
    gficlientid: Optional[str] = None
    overridepdftemplateinvoice: Optional[int] = None
    overridepdftemplateinvoice_name: Optional[str] = None
    kashflow_tenant_id: Optional[int] = None
    client_to_invoice: Optional[int] = None
    client_to_invoice_name: Optional[str] = None
    invoiceduedaysextraclient: Optional[int] = None
    itglue_id: Optional[str] = None
    clientcurrency: Optional[str] = None
    sentinel_subscription_id: Optional[str] = None
    sentinel_workspace_name: Optional[str] = None
    sentinel_resource_group_name: Optional[str] = None
    sentinel_tenant_id: Optional[int] = None
    sentinel_tenant_name: Optional[str] = None
    default_currency_code: Optional[int] = None
    client_to_invoice_recurring: Optional[int] = None
    client_to_invoice_recurring_name: Optional[str] = None
    azure_tenants: Optional[List[AreaAzureTenant]] = None
    azure_tenant_id: Optional[str] = None
    snow_id: Optional[int] = None
    snow_licences: Optional[List[SnowLicenseAbstract]] = None
    qbo_company_id: Optional[str] = None
    automatic_sales_tax: Optional[bool] = None
    cautomateid: Optional[int] = None
    dbc_company_id: Optional[str] = None
    stopped: Optional[int] = None
    customertype: Optional[int] = None
    customer_relationship: Optional[List[KeyPair]] = None
    customer_relationship_list: Optional[str] = None
    servicenow_validated: Optional[bool] = None
    sentinel_default_user_override: Optional[int] = None
    sentinel_default_user_override_name: Optional[str] = None
    jira_validated: Optional[bool] = None
    ref: Optional[str] = None
    ticket_invoices_for_each_site: Optional[bool] = None
    intacct_save_location: Optional[str] = None
    is_vip: Optional[bool] = None
    accountownertech_name: Optional[str] = None
    taxable: Optional[bool] = None
    quickbooks_details: Optional[QuickBooksDetails] = None
    percentage_to_survey: Optional[int] = None
    billing_plan_text: Optional[str] = None
    overridepdftemplatequote: Optional[int] = None
    overridepdftemplatequote_name: Optional[str] = None
    avalara_tenant: Optional[int] = None
    due_date_type: Optional[int] = None
    toplevel_quote_currency: Optional[int] = None
    is_account: Optional[bool] = None
    exclude_ai_functionality: Optional[bool] = None
    xero_default_payment_nominalcode: Optional[str] = None
    _importtypeid: Optional[int] = None
    _importthirdpartyid: Optional[str] = None
    import_details_id: Optional[int] = None
    _isupdateimport: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Area':
        if data is None:
            return None
        return cls(**{'pax8monthlyinvoice': data.get('pax8monthlyinvoice'), 'pax8annualinvoice': data.get('pax8annualinvoice'), 'quickbookstaxexemptionreasonid': data.get('quickbookstaxexemptionreasonid'), 'id': data.get('id'), 'name': data.get('name'), 'toplevel_id': data.get('toplevel_id'), 'toplevel_name': data.get('toplevel_name'), 'inactive': data.get('inactive'), 'colour': data.get('colour'), 'confirmemail': data.get('confirmemail'), 'actionemail': data.get('actionemail'), 'clearemail': data.get('clearemail'), 'messagegroup_id': data.get('messagegroup_id'), 'from_address_override': data.get('from_address_override'), 'override_org_logo': data.get('override_org_logo'), 'override_org_name': data.get('override_org_name'), 'override_org_address': data.get('override_org_address'), 'override_org_phone': data.get('override_org_phone'), 'override_org_email': data.get('override_org_email'), 'override_org_website': data.get('override_org_website'), 'override_org_portalurl': data.get('override_org_portalurl'), 'mailbox_override': data.get('mailbox_override'), 'default_mailbox_id': data.get('default_mailbox_id'), 'calldate': data.get('calldate'), 'item_tax_code': data.get('item_tax_code'), 'service_tax_code': data.get('service_tax_code'), 'prepay_tax_code': data.get('prepay_tax_code'), 'contract_tax_code': data.get('contract_tax_code'), 'customfields': data.get('customfields'), 'custombuttons': data.get('custombuttons'), 'attachments': data.get('attachments'), 'site_fields': data.get('site_fields'), 'pritech': data.get('pritech'), 'sectech': data.get('sectech'), 'accountmanagertech': data.get('accountmanagertech'), 'notes': data.get('notes'), 'thirdpartynhdapiurl': data.get('thirdpartynhdapiurl'), 'xeroid': data.get('xeroid'), 'open_ticket_count': data.get('open_ticket_count'), 'opps_ticket_count': data.get('opps_ticket_count'), 'main_site_id': data.get('main_site_id'), 'accountsemailaddress': data.get('accountsemailaddress'), 'accountsccemailaddress': data.get('accountsccemailaddress'), 'accountsfirstname': data.get('accountsfirstname'), 'accountslastname': data.get('accountslastname'), 'datecreated': data.get('datecreated'), 'createdfrom_id': data.get('createdfrom_id'), 'announce': data.get('announce'), 'announcedate': data.get('announcedate'), 'pritech_name': data.get('pritech_name'), 'sectech_name': data.get('sectech_name'), 'prinotify': data.get('prinotify'), 'secnotify': data.get('secnotify'), 'priassign': data.get('priassign'), 'secassign': data.get('secassign'), 'accountmanagertech_name': data.get('accountmanagertech_name'), 'accountmanagertech_email': data.get('accountmanagertech_email'), 'chargeperiod': data.get('chargeperiod'), 'chargehours': data.get('chargehours'), 'chargecarryover': data.get('chargecarryover'), 'invoiceyes': data.get('invoiceyes'), 'fluserdef1': data.get('fluserdef1'), 'fluserdef2': data.get('fluserdef2'), 'fluserdef3': data.get('fluserdef3'), 'fluserdef4': data.get('fluserdef4'), 'fluserdef5': data.get('fluserdef5'), 'floverride': data.get('floverride'), 'fluserdef1hide': data.get('fluserdef1hide'), 'fluserdef2hide': data.get('fluserdef2hide'), 'fluserdef3hide': data.get('fluserdef3hide'), 'fluserdef4hide': data.get('fluserdef4hide'), 'fluserdef5hide': data.get('fluserdef5hide'), 'fluserdef1mand': data.get('fluserdef1mand'), 'fluserdef2mand': data.get('fluserdef2mand'), 'fluserdef3mand': data.get('fluserdef3mand'), 'fluserdef4mand': data.get('fluserdef4mand'), 'fluserdef5mand': data.get('fluserdef5mand'), 'includeactions': data.get('includeactions'), 'needsinvoice': data.get('needsinvoice'), 'startdate': data.get('startdate'), 'startbalance': data.get('startbalance'), 'hourlyrate': data.get('hourlyrate'), 'periodcharge': data.get('periodcharge'), 'dontinvoice': data.get('dontinvoice'), 'invoicetemplate': data.get('invoicetemplate'), 'invoicecomment': data.get('invoicecomment'), 'lastinvoiceenddate': data.get('lastinvoiceenddate'), 'showslaonweb': data.get('showslaonweb'), 'item_tax_code_name': data.get('item_tax_code_name'), 'service_tax_code_name': data.get('service_tax_code_name'), 'contract_tax_code_name': data.get('contract_tax_code_name'), 'prepay_tax_code_name': data.get('prepay_tax_code_name'), 'imageindex': data.get('imageindex'), 'chargehours2': data.get('chargehours2'), 'hourlyrate2': data.get('hourlyrate2'), 'cat2': data.get('cat2'), 'cat3': data.get('cat3'), 'cat4': data.get('cat4'), 'cat5': data.get('cat5'), 'enddate': data.get('enddate'), 'ucemail': data.get('ucemail'), 'fcemail': data.get('fcemail'), 'actguid': data.get('actguid'), 'smsbalance': data.get('smsbalance'), 'html': data.get('html'), 'hv': data.get('hv'), 'hvdate': data.get('hvdate'), 'emailinvoice': data.get('emailinvoice'), 'dont_auto_send_invoices': data.get('dont_auto_send_invoices'), 'seriousnesslevel': data.get('seriousnesslevel'), 'defcat1': data.get('defcat1'), 'defcat2': data.get('defcat2'), 'defcat3': data.get('defcat3'), 'defcat4': data.get('defcat4'), 'thresholdbreached': data.get('thresholdbreached'), 'monthlyreportinclude': data.get('monthlyreportinclude'), 'monthlyreportlastrun': data.get('monthlyreportlastrun'), 'monthlyreportemaildirect': data.get('monthlyreportemaildirect'), 'monthlyreportemailmanager': data.get('monthlyreportemailmanager'), 'monthlyreportshowonweb': data.get('monthlyreportshowonweb'), 'areatype': data.get('areatype'), 'unmatchedcombinations': data.get('unmatchedcombinations'), 'prepayrecurringchargenextdate': data.get('prepayrecurringchargenextdate'), 'billforrecurringprepayamount': data.get('billforrecurringprepayamount'), 'prepayrecurringcharge': data.get('prepayrecurringcharge'), 'prepayrecurringhours': data.get('prepayrecurringhours'), 'prepayrecurringchargebp': data.get('prepayrecurringchargebp'), 'disclaimermatchstring': data.get('disclaimermatchstring'), 'paymentterms': data.get('paymentterms'), 'showallnonbillable': data.get('showallnonbillable'), 'billinggroup': data.get('billinggroup'), 'autotopupthreshhold': data.get('autotopupthreshhold'), 'autotopuptoamount': data.get('autotopuptoamount'), 'autotopupcostperhour': data.get('autotopupcostperhour'), 'autotopupbyamount': data.get('autotopupbyamount'), 'surchargeid': data.get('surchargeid'), 'billingtemplate_id': data.get('billingtemplate_id'), 'billingtemplate_name': data.get('billingtemplate_name'), 'overidegreeting': data.get('overidegreeting'), 'clientpackage': data.get('clientpackage'), 'scopeofbusiness': data.get('scopeofbusiness'), 'preferredagent': data.get('preferredagent'), 'callhandlingnotes': data.get('callhandlingnotes'), 'automatic_callscript_id': data.get('automatic_callscript_id'), 'automatic_callscript_name': data.get('automatic_callscript_name'), 'teamviewerpassword': data.get('teamviewerpassword'), 'customertype_new': data.get('customertype_new'), 'discountperc': data.get('discountperc'), 'showfaqfortoplevel': data.get('showfaqfortoplevel'), 'isopportunity': data.get('isopportunity'), 'snowname': data.get('snowname'), 'main_site_name': data.get('main_site_name'), 'linked_organisation_id': data.get('linked_organisation_id'), 'all_organisations_allowed': data.get('all_organisations_allowed'), 'allowed_organisations': data.get('allowed_organisations'), 'override_signature': data.get('override_signature'), 'contractaccountsdesc': data.get('contractaccountsdesc'), 'prepayaccountsdesc': data.get('prepayaccountsdesc'), 'site_update': data.get('site_update'), 'newclient_sitename': data.get('newclient_sitename'), 'newclient_phonenumber': data.get('newclient_phonenumber'), 'newclient_domain': data.get('newclient_domain'), 'newclient_timezone': data.get('newclient_timezone'), 'newclient_contactname': data.get('newclient_contactname'), 'newclient_contactemail': data.get('newclient_contactemail'), 'newclient_contactphonenumber': data.get('newclient_contactphonenumber'), 'newclient_contacttitle': data.get('newclient_contacttitle'), 'newclient_web_access_level': data.get('newclient_web_access_level'), 'newclient_sendwelcomeemail': data.get('newclient_sendwelcomeemail'), 'newclient_delivery_address': data.get('newclient_delivery_address'), 'newclient_countrycode': data.get('newclient_countrycode'), 'newclient_regioncode': data.get('newclient_regioncode'), 'faqlists': data.get('faqlists'), 'popup_notes': data.get('popup_notes'), '_reassign_all_to_user': data.get('_reassign_all_to_user'), 'allowall_tickettypes': data.get('allowall_tickettypes'), 'allowed_tickettypes': data.get('allowed_tickettypes'), 'allowall_category1': data.get('allowall_category1'), 'allowed_category1': data.get('allowed_category1'), 'allowall_category2': data.get('allowall_category2'), 'allowed_category2': data.get('allowed_category2'), 'allowall_category3': data.get('allowall_category3'), 'allowed_category3': data.get('allowed_category3'), 'allowall_category4': data.get('allowall_category4'), 'alocked': data.get('alocked'), 'allowed_category4': data.get('allowed_category4'), 'onhold_ticket_count': data.get('onhold_ticket_count'), 'total_ticket_count': data.get('total_ticket_count'), 'opened_thismonth_count': data.get('opened_thismonth_count'), 'billingplans': data.get('billingplans'), 'overriding_rates': data.get('overriding_rates'), 'allowallchargerates': data.get('allowallchargerates'), 'chargerates': data.get('chargerates'), 'newclient_siteguid': data.get('newclient_siteguid'), '_isimport': data.get('_isimport'), '_importtype': data.get('_importtype'), 'allow_api_access': data.get('allow_api_access'), 'api_access_clientid': data.get('api_access_clientid'), 'api_access_clientsecret': data.get('api_access_clientsecret'), 'thirdpartynhdauthurl': data.get('thirdpartynhdauthurl'), 'thirdpartynhdtenant': data.get('thirdpartynhdtenant'), 'thirdpartynhdapiclientid': data.get('thirdpartynhdapiclientid'), 'new_thirdpartynhdapiclientsecret': data.get('new_thirdpartynhdapiclientsecret'), 'areaitems': data.get('areaitems'), 'portal_logo': data.get('portal_logo'), 'override_portalcolour': data.get('override_portalcolour'), 'portalcolour': data.get('portalcolour'), 'portalbackgroundimageurl': data.get('portalbackgroundimageurl'), 'ninjarmmid': data.get('ninjarmmid'), 'sales_tax_type': data.get('sales_tax_type'), 'purchase_tax_type': data.get('purchase_tax_type'), 'isarchived_xero': data.get('isarchived_xero'), 'sales_tax_code': data.get('sales_tax_code'), 'purchase_tax_code': data.get('purchase_tax_code'), 'purchase_tax_code_name': data.get('purchase_tax_code_name'), 'prepayhistory': data.get('prepayhistory'), 'periods': data.get('periods'), 'prepayrecurringminimumdeduction': data.get('prepayrecurringminimumdeduction'), 'prepayrecurringminimumdeductiononlyactive': data.get('prepayrecurringminimumdeductiononlyactive'), 'prepayrecurringautomaticdeduction': data.get('prepayrecurringautomaticdeduction'), 'prepaytotal': data.get('prepaytotal'), 'prepayused': data.get('prepayused'), 'prepaybalance': data.get('prepaybalance'), 'preferreddeliverymethod': data.get('preferreddeliverymethod'), 'qbodefaulttax': data.get('qbodefaulttax'), 'default_contract': data.get('default_contract'), 'device42id': data.get('device42id'), 'xerodetails_id': data.get('xerodetails_id'), 'xero_tenant_name': data.get('xero_tenant_name'), 'xero_tracking_category_1_name': data.get('xero_tracking_category_1_name'), 'xero_tracking_category_2_name': data.get('xero_tracking_category_2_name'), 'servicenowid': data.get('servicenowid'), 'isnhserveremaildefault': data.get('isnhserveremaildefault'), 'datto_id': data.get('datto_id'), 'datto_alternate_id': data.get('datto_alternate_id'), 'datto_url': data.get('datto_url'), 'dattocommerce_tenantid': data.get('dattocommerce_tenantid'), 'qbodefaulttaxcode': data.get('qbodefaulttaxcode'), 'qbodefaulttaxcodename': data.get('qbodefaulttaxcodename'), 'qbo_default_tax_code': data.get('qbo_default_tax_code'), 'connectwiseid': data.get('connectwiseid'), 'autotaskid': data.get('autotaskid'), 'import_address': data.get('import_address'), 'import_notes': data.get('import_notes'), 'ateraid': data.get('ateraid'), 'kashflowid': data.get('kashflowid'), 'kashflow_tenant_name': data.get('kashflow_tenant_name'), 'website': data.get('website'), 'alastupdate': data.get('alastupdate'), 'group_service_access': data.get('group_service_access'), 'group_service_subscriptions': data.get('group_service_subscriptions'), 'snelstart_id': data.get('snelstart_id'), 'default_currency_code_name': data.get('default_currency_code_name'), '_apply_billingtemplate': data.get('_apply_billingtemplate'), 'recalculate_billing': data.get('recalculate_billing'), 'recalculate_billing_start': data.get('recalculate_billing_start'), 'recalculate_billing_end': data.get('recalculate_billing_end'), 'datto_commerce_id': data.get('datto_commerce_id'), 'datto_commerce_url': data.get('datto_commerce_url'), 'import_azure_tenant': data.get('import_azure_tenant'), 'syncroid': data.get('syncroid'), 'kbentries': data.get('kbentries'), 'auvik_id': data.get('auvik_id'), 'hubspot_id': data.get('hubspot_id'), 'hubspot_url': data.get('hubspot_url'), 'hubspot_dont_sync': data.get('hubspot_dont_sync'), 'hubspot_archived': data.get('hubspot_archived'), 'domain': data.get('domain'), 'passportal_id': data.get('passportal_id'), 'update_licences': data.get('update_licences'), 'prepayasamount': data.get('prepayasamount'), 'synced_to_intacct': data.get('synced_to_intacct'), 'qbo_company_name': data.get('qbo_company_name'), 'oppid': data.get('oppid'), 'tax_number': data.get('tax_number'), 'isclientdetails': data.get('isclientdetails'), 'hubspot_lifecycle': data.get('hubspot_lifecycle'), 'hudu_url': data.get('hudu_url'), 'prepayrecurringexpirymonths': data.get('prepayrecurringexpirymonths'), 'accountsbccemailaddress': data.get('accountsbccemailaddress'), 'defaultcontractoverride': data.get('defaultcontractoverride'), 'defaultcontractoverride_ref': data.get('defaultcontractoverride_ref'), 'sqlimport_id': data.get('sqlimport_id'), 'external_links': data.get('external_links'), 'new_external_link': data.get('new_external_link'), '_match_thirdparty_id': data.get('_match_thirdparty_id'), '_match_integration_id': data.get('_match_integration_id'), '_match_integration_name': data.get('_match_integration_name'), '_warning': data.get('_warning'), 'donotimport': data.get('donotimport'), 'liongardid': data.get('liongardid'), 'liongard_url': data.get('liongard_url'), 'sync_to_liongard': data.get('sync_to_liongard'), 'regmanagertech_name': data.get('regmanagertech_name'), 'logmanagertech_name': data.get('logmanagertech_name'), 'salesreptech_name': data.get('salesreptech_name'), 'default_team_to_salesrep_override': data.get('default_team_to_salesrep_override'), 'default_team_to_salesrep_override_team': data.get('default_team_to_salesrep_override_team'), 'cxmleadtech_name': data.get('cxmleadtech_name'), 'portalchatprofile': data.get('portalchatprofile'), 'portalchatprofile_name': data.get('portalchatprofile_name'), 'kaseyaid': data.get('kaseyaid'), 'trading_name': data.get('trading_name'), 'dbc_company_name': data.get('dbc_company_name'), 'salesforce_dontsync': data.get('salesforce_dontsync'), 'stripe_customer_id': data.get('stripe_customer_id'), 'stripe_payment_method_id': data.get('stripe_payment_method_id'), 'stripe_payment_method_name': data.get('stripe_payment_method_name'), 'stripe_paymentmethod': data.get('stripe_paymentmethod'), 'current_licences': data.get('current_licences'), 'servicenow_url': data.get('servicenow_url'), 'servicenow_locale': data.get('servicenow_locale'), 'servicenow_username': data.get('servicenow_username'), 'new_servicenowkey': data.get('new_servicenowkey'), 'servicenow_priority_mappings': data.get('servicenow_priority_mappings'), 'servicenow_status_mappings': data.get('servicenow_status_mappings'), 'servicenow_impact_mappings': data.get('servicenow_impact_mappings'), 'servicenow_urgency_mappings': data.get('servicenow_urgency_mappings'), 'servicenow_category_mappings': data.get('servicenow_category_mappings'), 'servicenow_service_mappings': data.get('servicenow_service_mappings'), 'servicenow_assignment_group': data.get('servicenow_assignment_group'), 'servicenow_assignment_group_name': data.get('servicenow_assignment_group_name'), 'servicenow_assignmentgroup': data.get('servicenow_assignmentgroup'), 'servicenow_defaultuser_id': data.get('servicenow_defaultuser_id'), 'servicenow_defaultuser_name': data.get('servicenow_defaultuser_name'), 'servicenow_defaultuser': data.get('servicenow_defaultuser'), 'test_servicenow': data.get('test_servicenow'), 'sage_business_cloud_details_id': data.get('sage_business_cloud_details_id'), 'sage_business_cloud_details_name': data.get('sage_business_cloud_details_name'), 'exact_division': data.get('exact_division'), 'exact_division_name': data.get('exact_division_name'), 'ncentral_details_id': data.get('ncentral_details_id'), 'currencyisocode': data.get('currencyisocode'), 'intacct_location_id': data.get('intacct_location_id'), 'intacct_location_id_list': data.get('intacct_location_id_list'), 'intacct_location_type': data.get('intacct_location_type'), 'new_categories': data.get('new_categories'), 'jira_url': data.get('jira_url'), 'jira_username': data.get('jira_username'), 'new_jirakey': data.get('new_jirakey'), 'test_jira': data.get('test_jira'), 'jira_servicedesk_id': data.get('jira_servicedesk_id'), 'jira_servicedesk_name': data.get('jira_servicedesk_name'), 'jira_servicedesk': data.get('jira_servicedesk'), 'jira_requesttype_mappings': data.get('jira_requesttype_mappings'), 'jira_user_id': data.get('jira_user_id'), 'jira_user_name': data.get('jira_user_name'), 'jira_user': data.get('jira_user'), 'jira_priority_mappings': data.get('jira_priority_mappings'), 'jira_status_mappings': data.get('jira_status_mappings'), 'jira_status_after_update': data.get('jira_status_after_update'), 'create_jira_webhook': data.get('create_jira_webhook'), 'jira_webhook_created': data.get('jira_webhook_created'), 'defaultpdftemplateinvoicetickets': data.get('defaultpdftemplateinvoicetickets'), 'defaultpdftemplateinvoiceorders': data.get('defaultpdftemplateinvoiceorders'), 'defaultpdftemplateinvoicerecurring': data.get('defaultpdftemplateinvoicerecurring'), 'defaultpdftemplateinvoicetickets_name': data.get('defaultpdftemplateinvoicetickets_name'), 'defaultpdftemplateinvoiceorders_name': data.get('defaultpdftemplateinvoiceorders_name'), 'defaultpdftemplateinvoicerecurring_name': data.get('defaultpdftemplateinvoicerecurring_name'), 'intacct_invoice_save_location': data.get('intacct_invoice_save_location'), 'ingram_micro_details_id': data.get('ingram_micro_details_id'), '_dont_fire_automations': data.get('_dont_fire_automations'), 'main_delivery_address': data.get('main_delivery_address'), 'main_invoice_address': data.get('main_invoice_address'), 'main_contact_name': data.get('main_contact_name'), 'main_contact_email': data.get('main_contact_email'), 'main_contact_phonenumber': data.get('main_contact_phonenumber'), 'main_contact_id': data.get('main_contact_id'), 'main_phonenumber': data.get('main_phonenumber'), 'auvik_site_inactive': data.get('auvik_site_inactive'), 'invoice_class': data.get('invoice_class'), 'new_icon': data.get('new_icon'), 'fortnox_tenant': data.get('fortnox_tenant'), 'fortnox_tenant_name': data.get('fortnox_tenant_name'), 'servicenow_enable_webhook': data.get('servicenow_enable_webhook'), 'new_servicenow_webhooksecret': data.get('new_servicenow_webhooksecret'), 'servicenow_webhook_user': data.get('servicenow_webhook_user'), 'servicenow_webhook_user_name': data.get('servicenow_webhook_user_name'), 'servicenow_webhook_tickettype': data.get('servicenow_webhook_tickettype'), 'servicenow_webhook_tickettype_name': data.get('servicenow_webhook_tickettype_name'), 'myob_tenant': data.get('myob_tenant'), 'myob_tenant_name': data.get('myob_tenant_name'), 'sync_servicenow_attachments': data.get('sync_servicenow_attachments'), 'twilio_subaccount_name': data.get('twilio_subaccount_name'), 'twilio_subaccount_created': data.get('twilio_subaccount_created'), 'twilio_subaccount_sid': data.get('twilio_subaccount_sid'), 'twilio_subaccount_status': data.get('twilio_subaccount_status'), 'twilio_subaccount_authtoken': data.get('twilio_subaccount_authtoken'), '_create_twilio_subaccount': data.get('_create_twilio_subaccount'), '_close_twilio_subaccount': data.get('_close_twilio_subaccount'), '_pauseunpause_twilio_subaccount': data.get('_pauseunpause_twilio_subaccount'), '_create_twilio_recurringinvoice': data.get('_create_twilio_recurringinvoice'), 'twilio_recurring_invoice_id': data.get('twilio_recurring_invoice_id'), 'override_layout_id': data.get('override_layout_id'), 'override_layout_name': data.get('override_layout_name'), 'extratabs': data.get('extratabs'), 'servicenow_team_mappings': data.get('servicenow_team_mappings'), 'servicenow_ticket_sync': data.get('servicenow_ticket_sync'), 'servicenow_ticket_sync_list': data.get('servicenow_ticket_sync_list'), 'servicenow_fieldmappings': data.get('servicenow_fieldmappings'), 'matching_value': data.get('matching_value'), 'jira_webhook_user': data.get('jira_webhook_user'), 'jira_webhook_username': data.get('jira_webhook_username'), 'avalara_code': data.get('avalara_code'), 'avalara_tenant_name': data.get('avalara_tenant_name'), 'avalara_id': data.get('avalara_id'), 'invoice_mailbox_override': data.get('invoice_mailbox_override'), 'quote_mailbox_override': data.get('quote_mailbox_override'), '_merge_client_into': data.get('_merge_client_into'), 'invoice_tickets_seperately_override': data.get('invoice_tickets_seperately_override'), 'servicenow_authtype': data.get('servicenow_authtype'), 'portal_title_override': data.get('portal_title_override'), 'portal_title': data.get('portal_title'), 'reply_address_override': data.get('reply_address_override'), 'auto_redirect_failed_login': data.get('auto_redirect_failed_login'), 'exclude_ai_profiling': data.get('exclude_ai_profiling'), 'dynamics_365_crm_details_id': data.get('dynamics_365_crm_details_id'), 'test_thirdpartynhd': data.get('test_thirdpartynhd'), 'thirdpartynhd_validated': data.get('thirdpartynhd_validated'), 'thirdpartynhdcustomfieldmappings': data.get('thirdpartynhdcustomfieldmappings'), 'thirdpartynhd_status_mappings': data.get('thirdpartynhd_status_mappings'), 'thirdpartynhd_category_mappings': data.get('thirdpartynhd_category_mappings'), 'thirdpartynhd_tickettype_mappings': data.get('thirdpartynhd_tickettype_mappings'), 'thirdpartynhd_outcome_mappings': data.get('thirdpartynhd_outcome_mappings'), 'thirdpartynhd_status': data.get('thirdpartynhd_status'), 'thirdpartynhd_status_name': data.get('thirdpartynhd_status_name'), 'thirdpartynhd_category': data.get('thirdpartynhd_category'), 'thirdpartynhd_category_name': data.get('thirdpartynhd_category_name'), 'thirdpartynhd_tickettype': data.get('thirdpartynhd_tickettype'), 'thirdpartynhd_tickettype_name': data.get('thirdpartynhd_tickettype_name'), 'thirdpartynhd_outcome': data.get('thirdpartynhd_outcome'), 'thirdpartynhd_outcome_name': data.get('thirdpartynhd_outcome_name'), 'thirdpartynhd_attachments': data.get('thirdpartynhd_attachments'), 'apiversion': data.get('apiversion'), 'audit_log': data.get('audit_log'), 'jira_allow_webhooks': data.get('jira_allow_webhooks'), 'jira_webhook_authentication': data.get('jira_webhook_authentication'), 'new_jira_webhook_secret': data.get('new_jira_webhook_secret'), 'servicenow_sync_child': data.get('servicenow_sync_child'), 'dbc_dimensions': data.get('dbc_dimensions'), 'dbc_template': data.get('dbc_template'), 'dynamics_dimensions_enabled': data.get('dynamics_dimensions_enabled'), 'dynamics_bc_synced': data.get('dynamics_bc_synced'), 'runbook_button_id': data.get('runbook_button_id'), 'use': data.get('use'), 'key': data.get('key'), 'table': data.get('table'), 'logo': data.get('logo'), 'regmanagertech': data.get('regmanagertech'), 'logmanagertech': data.get('logmanagertech'), 'salesreptech': data.get('salesreptech'), 'accountownertech': data.get('accountownertech'), 'cxmleadtech': data.get('cxmleadtech'), 'xero_tenant_id': data.get('xero_tenant_id'), 'accountsid': data.get('accountsid'), 'excludefrominvoicesync': data.get('excludefrominvoicesync'), 'gficlientid': data.get('gficlientid'), 'overridepdftemplateinvoice': data.get('overridepdftemplateinvoice'), 'overridepdftemplateinvoice_name': data.get('overridepdftemplateinvoice_name'), 'kashflow_tenant_id': data.get('kashflow_tenant_id'), 'client_to_invoice': data.get('client_to_invoice'), 'client_to_invoice_name': data.get('client_to_invoice_name'), 'invoiceduedaysextraclient': data.get('invoiceduedaysextraclient'), 'itglue_id': data.get('itglue_id'), 'clientcurrency': data.get('clientcurrency'), 'sentinel_subscription_id': data.get('sentinel_subscription_id'), 'sentinel_workspace_name': data.get('sentinel_workspace_name'), 'sentinel_resource_group_name': data.get('sentinel_resource_group_name'), 'sentinel_tenant_id': data.get('sentinel_tenant_id'), 'sentinel_tenant_name': data.get('sentinel_tenant_name'), 'default_currency_code': data.get('default_currency_code'), 'client_to_invoice_recurring': data.get('client_to_invoice_recurring'), 'client_to_invoice_recurring_name': data.get('client_to_invoice_recurring_name'), 'azure_tenants': data.get('azure_tenants'), 'azure_tenant_id': data.get('azure_tenant_id'), 'snow_id': data.get('snow_id'), 'snow_licences': data.get('snowLicences'), 'qbo_company_id': data.get('qbo_company_id'), 'automatic_sales_tax': data.get('automatic_sales_tax'), 'cautomateid': data.get('cautomateid'), 'dbc_company_id': data.get('dbc_company_id'), 'stopped': data.get('stopped'), 'customertype': data.get('customertype'), 'customer_relationship': data.get('customer_relationship'), 'customer_relationship_list': data.get('customer_relationship_list'), 'servicenow_validated': data.get('servicenow_validated'), 'sentinel_default_user_override': data.get('sentinel_default_user_override'), 'sentinel_default_user_override_name': data.get('sentinel_default_user_override_name'), 'jira_validated': data.get('jira_validated'), 'ref': data.get('ref'), 'ticket_invoices_for_each_site': data.get('ticket_invoices_for_each_site'), 'intacct_save_location': data.get('intacct_save_location'), 'is_vip': data.get('is_vip'), 'accountownertech_name': data.get('accountownertech_name'), 'taxable': data.get('taxable'), 'quickbooks_details': data.get('quickbooks_details'), 'percentage_to_survey': data.get('percentage_to_survey'), 'billing_plan_text': data.get('billing_plan_text'), 'overridepdftemplatequote': data.get('overridepdftemplatequote'), 'overridepdftemplatequote_name': data.get('overridepdftemplatequote_name'), 'avalara_tenant': data.get('avalara_tenant'), 'due_date_type': data.get('due_date_type'), 'toplevel_quote_currency': data.get('toplevel_quote_currency'), 'is_account': data.get('is_account'), 'exclude_ai_functionality': data.get('exclude_ai_functionality'), 'xero_default_payment_nominalcode': data.get('xero_default_payment_nominalcode'), '_importtypeid': data.get('_importtypeid'), '_importthirdpartyid': data.get('_importthirdpartyid'), 'import_details_id': data.get('import_details_id'), '_isupdateimport': data.get('_isupdateimport')})

@dataclass
class AreaAzureTenant:
    id: Optional[int] = None
    details_id: Optional[int] = None
    client_id: Optional[int] = None
    azure_tenant_id: Optional[str] = None
    azure_tenant_name: Optional[str] = None
    new_access_token: Optional[str] = None
    token_expiry: Optional[str] = None
    client_name: Optional[str] = None
    details_name: Optional[str] = None
    azure_tenant_domain: Optional[str] = None
    licence_import_type: Optional[int] = None
    relationship_type: Optional[int] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AreaAzureTenant':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'details_id': data.get('details_id'), 'client_id': data.get('client_id'), 'azure_tenant_id': data.get('azure_tenant_id'), 'azure_tenant_name': data.get('azure_tenant_name'), 'new_access_token': data.get('new_access_token'), 'token_expiry': data.get('token_expiry'), 'client_name': data.get('client_name'), 'details_name': data.get('details_name'), 'azure_tenant_domain': data.get('azure_tenant_domain'), 'licence_import_type': data.get('licence_import_type'), 'relationship_type': data.get('relationship_type'), '_warning': data.get('_warning')})

@dataclass
class AreaItem:
    id: Optional[int] = None
    client_id: Optional[int] = None
    item_id: Optional[int] = None
    quantity: Optional[float] = None
    areaitemdesc: Optional[str] = None
    billingperiod_id: Optional[int] = None
    startdate: Optional[str] = None
    invoicenumber: Optional[str] = None
    lastinvoicedate: Optional[str] = None
    nextinvoicedate: Optional[str] = None
    autorenew: Optional[bool] = None
    note: Optional[str] = None
    costprice: Optional[float] = None
    sellingprice: Optional[float] = None
    accounts_id: Optional[str] = None
    numberdayswarning: Optional[int] = None
    dsite: Optional[int] = None
    ddevnum: Optional[int] = None
    technician: Optional[int] = None
    billingcategory_id: Optional[int] = None
    site_id: Optional[int] = None
    dontinvoice: Optional[bool] = None
    enddate: Optional[str] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AreaItem':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'client_id': data.get('client_id'), 'item_id': data.get('item_id'), 'quantity': data.get('quantity'), 'areaitemdesc': data.get('areaitemdesc'), 'billingperiod_id': data.get('billingperiod_id'), 'startdate': data.get('startdate'), 'invoicenumber': data.get('invoicenumber'), 'lastinvoicedate': data.get('lastinvoicedate'), 'nextinvoicedate': data.get('nextinvoicedate'), 'autorenew': data.get('autorenew'), 'note': data.get('note'), 'costprice': data.get('costprice'), 'sellingprice': data.get('sellingprice'), 'accounts_id': data.get('accounts_id'), 'numberdayswarning': data.get('numberdayswarning'), 'dsite': data.get('dsite'), 'ddevnum': data.get('ddevnum'), 'technician': data.get('technician'), 'billingcategory_id': data.get('billingcategory_id'), 'site_id': data.get('site_id'), 'dontinvoice': data.get('dontinvoice'), 'enddate': data.get('enddate'), '_warning': data.get('_warning')})

@dataclass
class AreaPopup:
    id: Optional[int] = None
    client_id: Optional[int] = None
    site_id: Optional[int] = None
    user_id: Optional[int] = None
    date_created: Optional[str] = None
    note: Optional[str] = None
    dismissable: Optional[bool] = None
    read_status: Optional[int] = None
    displaymodal: Optional[bool] = None
    displayhtml: Optional[bool] = None
    limitdaterange: Optional[bool] = None
    startdate: Optional[str] = None
    enddate: Optional[str] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AreaPopup':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'client_id': data.get('client_id'), 'site_id': data.get('site_id'), 'user_id': data.get('user_id'), 'date_created': data.get('date_created'), 'note': data.get('note'), 'dismissable': data.get('dismissable'), 'read_status': data.get('read_status'), 'displaymodal': data.get('displaymodal'), 'displayhtml': data.get('displayhtml'), 'limitdaterange': data.get('limitdaterange'), 'startdate': data.get('startdate'), 'enddate': data.get('enddate'), '_warning': data.get('_warning')})

@dataclass
class AreaList:
    id: Optional[int] = None
    name: Optional[str] = None
    toplevel_id: Optional[int] = None
    toplevel_name: Optional[str] = None
    inactive: Optional[bool] = None
    colour: Optional[str] = None
    confirmemail: Optional[int] = None
    actionemail: Optional[int] = None
    clearemail: Optional[int] = None
    messagegroup_id: Optional[int] = None
    from_address_override: Optional[str] = None
    override_org_logo: Optional[bool] = None
    override_org_name: Optional[str] = None
    override_org_address: Optional[AddressStore] = None
    override_org_phone: Optional[str] = None
    override_org_email: Optional[str] = None
    override_org_website: Optional[str] = None
    override_org_portalurl: Optional[str] = None
    mailbox_override: Optional[int] = None
    default_mailbox_id: Optional[int] = None
    calldate: Optional[str] = None
    item_tax_code: Optional[int] = None
    service_tax_code: Optional[int] = None
    prepay_tax_code: Optional[int] = None
    contract_tax_code: Optional[int] = None
    customfields: Optional[List[CustomField]] = None
    custombuttons: Optional[List[CustomButton]] = None
    attachments: Optional[List[Attachment]] = None
    site_fields: Optional[List[FieldHelper]] = None
    pritech: Optional[int] = None
    sectech: Optional[int] = None
    accountmanagertech: Optional[int] = None
    notes: Optional[str] = None
    thirdpartynhdapiurl: Optional[str] = None
    xeroid: Optional[str] = None
    open_ticket_count: Optional[int] = None
    opps_ticket_count: Optional[int] = None
    main_site_id: Optional[int] = None
    accountsemailaddress: Optional[str] = None
    accountsccemailaddress: Optional[str] = None
    accountsfirstname: Optional[str] = None
    accountslastname: Optional[str] = None
    use: Optional[str] = None
    key: Optional[int] = None
    table: Optional[TableEnum] = None
    logo: Optional[str] = None
    regmanagertech: Optional[int] = None
    logmanagertech: Optional[int] = None
    salesreptech: Optional[int] = None
    accountownertech: Optional[int] = None
    cxmleadtech: Optional[int] = None
    xero_tenant_id: Optional[str] = None
    accountsid: Optional[str] = None
    excludefrominvoicesync: Optional[bool] = None
    gficlientid: Optional[str] = None
    overridepdftemplateinvoice: Optional[int] = None
    overridepdftemplateinvoice_name: Optional[str] = None
    kashflow_tenant_id: Optional[int] = None
    client_to_invoice: Optional[int] = None
    client_to_invoice_name: Optional[str] = None
    invoiceduedaysextraclient: Optional[int] = None
    itglue_id: Optional[str] = None
    clientcurrency: Optional[str] = None
    sentinel_subscription_id: Optional[str] = None
    sentinel_workspace_name: Optional[str] = None
    sentinel_resource_group_name: Optional[str] = None
    sentinel_tenant_id: Optional[int] = None
    sentinel_tenant_name: Optional[str] = None
    default_currency_code: Optional[int] = None
    client_to_invoice_recurring: Optional[int] = None
    client_to_invoice_recurring_name: Optional[str] = None
    azure_tenants: Optional[List[AreaAzureTenant]] = None
    azure_tenant_id: Optional[str] = None
    snow_id: Optional[int] = None
    snow_licences: Optional[List[SnowLicenseAbstract]] = None
    qbo_company_id: Optional[str] = None
    automatic_sales_tax: Optional[bool] = None
    cautomateid: Optional[int] = None
    dbc_company_id: Optional[str] = None
    stopped: Optional[int] = None
    customertype: Optional[int] = None
    customer_relationship: Optional[List[KeyPair]] = None
    customer_relationship_list: Optional[str] = None
    servicenow_validated: Optional[bool] = None
    sentinel_default_user_override: Optional[int] = None
    sentinel_default_user_override_name: Optional[str] = None
    jira_validated: Optional[bool] = None
    ref: Optional[str] = None
    ticket_invoices_for_each_site: Optional[bool] = None
    intacct_save_location: Optional[str] = None
    is_vip: Optional[bool] = None
    accountownertech_name: Optional[str] = None
    taxable: Optional[bool] = None
    quickbooks_details: Optional[QuickBooksDetails] = None
    percentage_to_survey: Optional[int] = None
    billing_plan_text: Optional[str] = None
    overridepdftemplatequote: Optional[int] = None
    overridepdftemplatequote_name: Optional[str] = None
    avalara_tenant: Optional[int] = None
    due_date_type: Optional[int] = None
    toplevel_quote_currency: Optional[int] = None
    is_account: Optional[bool] = None
    exclude_ai_functionality: Optional[bool] = None
    xero_default_payment_nominalcode: Optional[str] = None
    website: Optional[str] = None
    _importtypeid: Optional[int] = None
    _importthirdpartyid: Optional[str] = None
    _importtype: Optional[str] = None
    new_external_link: Optional[ExternalLinkList] = None
    import_details_id: Optional[int] = None
    _isupdateimport: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AreaList':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name'), 'toplevel_id': data.get('toplevel_id'), 'toplevel_name': data.get('toplevel_name'), 'inactive': data.get('inactive'), 'colour': data.get('colour'), 'confirmemail': data.get('confirmemail'), 'actionemail': data.get('actionemail'), 'clearemail': data.get('clearemail'), 'messagegroup_id': data.get('messagegroup_id'), 'from_address_override': data.get('from_address_override'), 'override_org_logo': data.get('override_org_logo'), 'override_org_name': data.get('override_org_name'), 'override_org_address': data.get('override_org_address'), 'override_org_phone': data.get('override_org_phone'), 'override_org_email': data.get('override_org_email'), 'override_org_website': data.get('override_org_website'), 'override_org_portalurl': data.get('override_org_portalurl'), 'mailbox_override': data.get('mailbox_override'), 'default_mailbox_id': data.get('default_mailbox_id'), 'calldate': data.get('calldate'), 'item_tax_code': data.get('item_tax_code'), 'service_tax_code': data.get('service_tax_code'), 'prepay_tax_code': data.get('prepay_tax_code'), 'contract_tax_code': data.get('contract_tax_code'), 'customfields': data.get('customfields'), 'custombuttons': data.get('custombuttons'), 'attachments': data.get('attachments'), 'site_fields': data.get('site_fields'), 'pritech': data.get('pritech'), 'sectech': data.get('sectech'), 'accountmanagertech': data.get('accountmanagertech'), 'notes': data.get('notes'), 'thirdpartynhdapiurl': data.get('thirdpartynhdapiurl'), 'xeroid': data.get('xeroid'), 'open_ticket_count': data.get('open_ticket_count'), 'opps_ticket_count': data.get('opps_ticket_count'), 'main_site_id': data.get('main_site_id'), 'accountsemailaddress': data.get('accountsemailaddress'), 'accountsccemailaddress': data.get('accountsccemailaddress'), 'accountsfirstname': data.get('accountsfirstname'), 'accountslastname': data.get('accountslastname'), 'use': data.get('use'), 'key': data.get('key'), 'table': data.get('table'), 'logo': data.get('logo'), 'regmanagertech': data.get('regmanagertech'), 'logmanagertech': data.get('logmanagertech'), 'salesreptech': data.get('salesreptech'), 'accountownertech': data.get('accountownertech'), 'cxmleadtech': data.get('cxmleadtech'), 'xero_tenant_id': data.get('xero_tenant_id'), 'accountsid': data.get('accountsid'), 'excludefrominvoicesync': data.get('excludefrominvoicesync'), 'gficlientid': data.get('gficlientid'), 'overridepdftemplateinvoice': data.get('overridepdftemplateinvoice'), 'overridepdftemplateinvoice_name': data.get('overridepdftemplateinvoice_name'), 'kashflow_tenant_id': data.get('kashflow_tenant_id'), 'client_to_invoice': data.get('client_to_invoice'), 'client_to_invoice_name': data.get('client_to_invoice_name'), 'invoiceduedaysextraclient': data.get('invoiceduedaysextraclient'), 'itglue_id': data.get('itglue_id'), 'clientcurrency': data.get('clientcurrency'), 'sentinel_subscription_id': data.get('sentinel_subscription_id'), 'sentinel_workspace_name': data.get('sentinel_workspace_name'), 'sentinel_resource_group_name': data.get('sentinel_resource_group_name'), 'sentinel_tenant_id': data.get('sentinel_tenant_id'), 'sentinel_tenant_name': data.get('sentinel_tenant_name'), 'default_currency_code': data.get('default_currency_code'), 'client_to_invoice_recurring': data.get('client_to_invoice_recurring'), 'client_to_invoice_recurring_name': data.get('client_to_invoice_recurring_name'), 'azure_tenants': data.get('azure_tenants'), 'azure_tenant_id': data.get('azure_tenant_id'), 'snow_id': data.get('snow_id'), 'snow_licences': data.get('snowLicences'), 'qbo_company_id': data.get('qbo_company_id'), 'automatic_sales_tax': data.get('automatic_sales_tax'), 'cautomateid': data.get('cautomateid'), 'dbc_company_id': data.get('dbc_company_id'), 'stopped': data.get('stopped'), 'customertype': data.get('customertype'), 'customer_relationship': data.get('customer_relationship'), 'customer_relationship_list': data.get('customer_relationship_list'), 'servicenow_validated': data.get('servicenow_validated'), 'sentinel_default_user_override': data.get('sentinel_default_user_override'), 'sentinel_default_user_override_name': data.get('sentinel_default_user_override_name'), 'jira_validated': data.get('jira_validated'), 'ref': data.get('ref'), 'ticket_invoices_for_each_site': data.get('ticket_invoices_for_each_site'), 'intacct_save_location': data.get('intacct_save_location'), 'is_vip': data.get('is_vip'), 'accountownertech_name': data.get('accountownertech_name'), 'taxable': data.get('taxable'), 'quickbooks_details': data.get('quickbooks_details'), 'percentage_to_survey': data.get('percentage_to_survey'), 'billing_plan_text': data.get('billing_plan_text'), 'overridepdftemplatequote': data.get('overridepdftemplatequote'), 'overridepdftemplatequote_name': data.get('overridepdftemplatequote_name'), 'avalara_tenant': data.get('avalara_tenant'), 'due_date_type': data.get('due_date_type'), 'toplevel_quote_currency': data.get('toplevel_quote_currency'), 'is_account': data.get('is_account'), 'exclude_ai_functionality': data.get('exclude_ai_functionality'), 'xero_default_payment_nominalcode': data.get('xero_default_payment_nominalcode'), 'website': data.get('website'), '_importtypeid': data.get('_importtypeid'), '_importthirdpartyid': data.get('_importthirdpartyid'), '_importtype': data.get('_importtype'), 'new_external_link': data.get('new_external_link'), 'import_details_id': data.get('import_details_id'), '_isupdateimport': data.get('_isupdateimport')})

@dataclass
class AreaView:
    page_no: Optional[int] = None
    page_size: Optional[int] = None
    record_count: Optional[int] = None
    clients: Optional[List[AreaList]] = None
    columns_id: Optional[int] = None
    columns_tilehtml: Optional[str] = None
    columns: Optional[List[ViewColumnsDetails]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AreaView':
        if data is None:
            return None
        return cls(**{'page_no': data.get('page_no'), 'page_size': data.get('page_size'), 'record_count': data.get('record_count'), 'clients': data.get('clients'), 'columns_id': data.get('columns_id'), 'columns_tilehtml': data.get('columns_tilehtml'), 'columns': data.get('columns')})

@dataclass
class Audit:
    id: Optional[int] = None
    ticket_id: Optional[int] = None
    agent_id: Optional[int] = None
    date: Optional[str] = None
    value: Optional[str] = None
    to: Optional[str] = None
    from_: Optional[str] = None
    table_name: Optional[str] = None
    id1: Optional[int] = None
    id2: Optional[int] = None
    clientid: Optional[int] = None
    _warning: Optional[str] = None
    actoutcome: Optional[str] = None
    user_id: Optional[int] = None
    username: Optional[str] = None
    datetime_to: Optional[str] = None
    datetime_from: Optional[str] = None
    _redact: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Audit':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'ticket_id': data.get('ticket_id'), 'agent_id': data.get('agent_id'), 'date': data.get('date'), 'value': data.get('value'), 'to': data.get('to'), 'from_': data.get('from'), 'table_name': data.get('table_name'), 'id1': data.get('id1'), 'id2': data.get('id2'), 'clientid': data.get('clientid'), '_warning': data.get('_warning'), 'actoutcome': data.get('actoutcome'), 'user_id': data.get('user_id'), 'username': data.get('username'), 'datetime_to': data.get('datetime_to'), 'datetime_from': data.get('datetime_from'), '_redact': data.get('_redact')})

@dataclass
class BillingPlanCriteria:
    id: Optional[int] = None
    cdid: Optional[int] = None
    cdseq: Optional[int] = None
    field: Optional[str] = None
    table_name: Optional[str] = None
    field_name: Optional[str] = None
    value_type_id: Optional[int] = None
    type: Optional[int] = None
    value: Optional[str] = None
    value_type: Optional[str] = None
    value_display: Optional[str] = None
    value_int: Optional[int] = None
    value_datetime: Optional[str] = None
    value_double: Optional[float] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BillingPlanCriteria':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'cdid': data.get('cdid'), 'cdseq': data.get('cdseq'), 'field': data.get('field'), 'table_name': data.get('table_name'), 'field_name': data.get('field_name'), 'value_type_id': data.get('value_type_id'), 'type': data.get('type'), 'value': data.get('value'), 'value_type': data.get('value_type'), 'value_display': data.get('value_display'), 'value_int': data.get('value_int'), 'value_datetime': data.get('value_datetime'), 'value_double': data.get('value_double'), '_warning': data.get('_warning')})

@dataclass
class BusinessCentralDimensions:
    halo_id: Optional[int] = None
    id: Optional[str] = None
    dynamicstype: Optional[int] = None
    haloparentid: Optional[int] = None
    value_id: Optional[str] = None
    value_code: Optional[str] = None
    display_name: Optional[str] = None
    value_consolidation_code: Optional[str] = None
    value_display_name: Optional[str] = None
    last_modified_date_time: Optional[str] = None
    posting_value: Optional[str] = None
    code: Optional[str] = None
    consolidation_code: Optional[str] = None
    parent_type: Optional[str] = None
    dimension_value_code: Optional[str] = None
    _warning: Optional[str] = None
    parent_id: Optional[str] = None
    dimension_id: Optional[str] = None
    dimension_code: Optional[str] = None
    dimension_value_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BusinessCentralDimensions':
        if data is None:
            return None
        return cls(**{'halo_id': data.get('halo_id'), 'id': data.get('id'), 'dynamicstype': data.get('dynamicstype'), 'haloparentid': data.get('haloparentid'), 'value_id': data.get('valueId'), 'value_code': data.get('valueCode'), 'display_name': data.get('displayName'), 'value_consolidation_code': data.get('valueConsolidationCode'), 'value_display_name': data.get('valueDisplayName'), 'last_modified_date_time': data.get('lastModifiedDateTime'), 'posting_value': data.get('postingValue'), 'code': data.get('code'), 'consolidation_code': data.get('consolidationCode'), 'parent_type': data.get('parentType'), 'dimension_value_code': data.get('dimensionValueCode'), '_warning': data.get('_warning'), 'parent_id': data.get('parentId'), 'dimension_id': data.get('dimensionId'), 'dimension_code': data.get('dimensionCode'), 'dimension_value_id': data.get('dimensionValueId')})

@dataclass
class CspCustomer:
    id: Optional[str] = None
    company_profile: Optional[CspCustomerProfile] = None
    relationship_to_partner: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CspCustomer':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'company_profile': data.get('companyProfile'), 'relationship_to_partner': data.get('relationshipToPartner')})

@dataclass
class CspCustomerProfile:
    tenant_id: Optional[str] = None
    domain: Optional[str] = None
    company_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CspCustomerProfile':
        if data is None:
            return None
        return cls(**{'tenant_id': data.get('tenantId'), 'domain': data.get('domain'), 'company_name': data.get('companyName')})

@dataclass
class CategoryRestriction:
    id: Optional[int] = None
    type: Optional[int] = None
    client_id: Optional[int] = None
    tickettype_id: Optional[int] = None
    team_id: Optional[int] = None
    team_guid: Optional[str] = None
    service_id: Optional[int] = None
    category_id: Optional[int] = None
    category_guid: Optional[str] = None
    category_value: Optional[str] = None
    _warning: Optional[str] = None
    partial_match_category: Optional[bool] = None
    category_name_partial: Optional[str] = None
    is_integration: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CategoryRestriction':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'type': data.get('type'), 'client_id': data.get('client_id'), 'tickettype_id': data.get('tickettype_id'), 'team_id': data.get('team_id'), 'team_guid': data.get('team_guid'), 'service_id': data.get('service_id'), 'category_id': data.get('category_id'), 'category_guid': data.get('category_guid'), 'category_value': data.get('category_value'), '_warning': data.get('_warning'), 'partial_match_category': data.get('partial_match_category'), 'category_name_partial': data.get('category_name_partial'), 'is_integration': data.get('is_integration')})

@dataclass
class ChargeRate:
    id: Optional[int] = None
    area: Optional[int] = None
    contract_id: Optional[int] = None
    charge_id: Optional[int] = None
    startdate: Optional[str] = None
    expirydate: Optional[str] = None
    rate: Optional[float] = None
    mileage_rate: Optional[float] = None
    org: Optional[int] = None
    minimum: Optional[float] = None
    increment: Optional[float] = None
    oohmultiplier: Optional[float] = None
    holidaymultiplier: Optional[float] = None
    weekendmultiplier: Optional[float] = None
    surcharge: Optional[bool] = None
    round: Optional[int] = None
    useagentworkinghours: Optional[bool] = None
    use_budget_rate: Optional[bool] = None
    current: Optional[bool] = None
    current_rate: Optional[float] = None
    use_for_travel: Optional[bool] = None
    use_for_mileage: Optional[bool] = None
    travel_surchargeid: Optional[int] = None
    contractmultiplier: Optional[float] = None
    rateoverride: Optional[float] = None
    override_surcharge: Optional[bool] = None
    _warning: Optional[str] = None
    tree_id: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ChargeRate':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'area': data.get('area'), 'contract_id': data.get('contract_id'), 'charge_id': data.get('charge_id'), 'startdate': data.get('startdate'), 'expirydate': data.get('expirydate'), 'rate': data.get('rate'), 'mileage_rate': data.get('mileage_rate'), 'org': data.get('org'), 'minimum': data.get('minimum'), 'increment': data.get('increment'), 'oohmultiplier': data.get('oohmultiplier'), 'holidaymultiplier': data.get('holidaymultiplier'), 'weekendmultiplier': data.get('weekendmultiplier'), 'surcharge': data.get('surcharge'), 'round': data.get('round'), 'useagentworkinghours': data.get('useagentworkinghours'), 'use_budget_rate': data.get('use_budget_rate'), 'current': data.get('current'), 'current_rate': data.get('current_rate'), 'use_for_travel': data.get('use_for_travel'), 'use_for_mileage': data.get('use_for_mileage'), 'travel_surchargeid': data.get('travel_surchargeid'), 'contractmultiplier': data.get('contractmultiplier'), 'rateoverride': data.get('rateoverride'), 'override_surcharge': data.get('override_surcharge'), '_warning': data.get('_warning'), 'tree_id': data.get('tree_id')})

@dataclass
class ChargeRateArea:
    id: Optional[int] = None
    area: Optional[int] = None
    chargerate_id: Optional[int] = None
    tree_id: Optional[int] = None
    name: Optional[str] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ChargeRateArea':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'area': data.get('area'), 'chargerate_id': data.get('chargerate_id'), 'tree_id': data.get('tree_id'), 'name': data.get('name'), '_warning': data.get('_warning')})

@dataclass
class ContractDetail:
    client_id: Optional[int] = None
    seq: Optional[int] = None
    type: Optional[int] = None
    itil_requesttype: Optional[int] = None
    requesttype: Optional[int] = None
    requesttype_name: Optional[str] = None
    priority: Optional[int] = None
    chargerate_type: Optional[int] = None
    chargerate_id: Optional[int] = None
    chargerate_name: Optional[str] = None
    multiplier: Optional[float] = None
    plan_id: Optional[int] = None
    plan_contract_id: Optional[int] = None
    plan_name: Optional[str] = None
    category_1: Optional[str] = None
    partialmatchcategory: Optional[bool] = None
    category_2: Optional[str] = None
    partialmatchcategory2: Optional[bool] = None
    category_3: Optional[str] = None
    partialmatchcategory3: Optional[bool] = None
    category_4: Optional[str] = None
    partialmatchcategory4: Optional[bool] = None
    user_covered_billingdescription: Optional[int] = None
    site: Optional[int] = None
    site_name: Optional[str] = None
    allowallcontracts: Optional[bool] = None
    asset_covered_by_contract: Optional[bool] = None
    user_covered_by_contract: Optional[bool] = None
    work_hours_covered: Optional[int] = None
    _warning: Optional[str] = None
    order: Optional[int] = None
    billing_plan_desc: Optional[str] = None
    contract_type: Optional[int] = None
    contract_sub_type: Optional[int] = None
    not_included_in_contract: Optional[bool] = None
    contract_header_end_date: Optional[str] = None
    contract_header_start_date: Optional[str] = None
    plan_active: Optional[bool] = None
    extra_filters: Optional[List[BillingPlanCriteria]] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ContractDetail':
        if data is None:
            return None
        return cls(**{'client_id': data.get('client_id'), 'seq': data.get('seq'), 'type': data.get('type'), 'itil_requesttype': data.get('itil_requesttype'), 'requesttype': data.get('requesttype'), 'requesttype_name': data.get('requesttype_name'), 'priority': data.get('priority'), 'chargerate_type': data.get('chargerate_type'), 'chargerate_id': data.get('chargerate_id'), 'chargerate_name': data.get('chargerate_name'), 'multiplier': data.get('multiplier'), 'plan_id': data.get('plan_id'), 'plan_contract_id': data.get('plan_contract_id'), 'plan_name': data.get('plan_name'), 'category_1': data.get('category_1'), 'partialmatchcategory': data.get('partialmatchcategory'), 'category_2': data.get('category_2'), 'partialmatchcategory2': data.get('partialmatchcategory2'), 'category_3': data.get('category_3'), 'partialmatchcategory3': data.get('partialmatchcategory3'), 'category_4': data.get('category_4'), 'partialmatchcategory4': data.get('partialmatchcategory4'), 'user_covered_billingdescription': data.get('user_covered_billingdescription'), 'site': data.get('site'), 'site_name': data.get('site_name'), 'allowallcontracts': data.get('allowallcontracts'), 'asset_covered_by_contract': data.get('asset_covered_by_contract'), 'user_covered_by_contract': data.get('user_covered_by_contract'), 'work_hours_covered': data.get('work_hours_covered'), '_warning': data.get('_warning'), 'order': data.get('order'), 'billing_plan_desc': data.get('billing_plan_desc'), 'contract_type': data.get('contract_type'), 'contract_sub_type': data.get('contract_sub_type'), 'not_included_in_contract': data.get('not_included_in_contract'), 'contract_header_end_date': data.get('contract_header_end_date'), 'contract_header_start_date': data.get('contract_header_start_date'), 'plan_active': data.get('plan_active'), 'extra_filters': data.get('extra_filters'), 'end_date': data.get('end_date'), 'start_date': data.get('start_date')})

@dataclass
class CriteriaGroup:
    id: Optional[int] = None
    entity_id: Optional[int] = None
    entity_name: Optional[str] = None
    entity_id2: Optional[int] = None
    entity_guid2: Optional[str] = None
    entity_id3: Optional[int] = None
    type: Optional[int] = None
    desc: Optional[str] = None
    seq: Optional[int] = None
    allow_access: Optional[bool] = None
    subscriber_type: Optional[int] = None
    restrictions: Optional[List[FlowSubDetailRestriction]] = None
    visibility_conditions: Optional[List[CustomFieldVisibility]] = None
    user_access: Optional[List[ServiceRestriction]] = None
    subscribers: Optional[List[ServiceUser]] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CriteriaGroup':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'entity_id': data.get('entity_id'), 'entity_name': data.get('entity_name'), 'entity_id2': data.get('entity_id2'), 'entity_guid2': data.get('entity_guid2'), 'entity_id3': data.get('entity_id3'), 'type': data.get('type'), 'desc': data.get('desc'), 'seq': data.get('seq'), 'allow_access': data.get('allow_access'), 'subscriber_type': data.get('subscriber_type'), 'restrictions': data.get('restrictions'), 'visibility_conditions': data.get('visibility_conditions'), 'user_access': data.get('user_access'), 'subscribers': data.get('subscribers'), '_warning': data.get('_warning')})

@dataclass
class FlowSubDetailRestriction:
    id: Optional[int] = None
    criteriagroup_id: Optional[int] = None
    field_id: Optional[int] = None
    type: Optional[int] = None
    value_id: Optional[int] = None
    value_name: Optional[str] = None
    fieldname: Optional[str] = None
    value_type: Optional[str] = None
    value_type_id: Optional[int] = None
    value_int: Optional[int] = None
    valueint_guid: Optional[str] = None
    value_string: Optional[str] = None
    value_datetime: Optional[str] = None
    value_float: Optional[float] = None
    value_display: Optional[str] = None
    alt_value_display: Optional[str] = None
    tablename: Optional[str] = None
    timezonestring: Optional[str] = None
    match_after_start: Optional[bool] = None
    match_after_target: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FlowSubDetailRestriction':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'criteriagroup_id': data.get('criteriagroup_id'), 'field_id': data.get('field_id'), 'type': data.get('type'), 'value_id': data.get('value_id'), 'value_name': data.get('value_name'), 'fieldname': data.get('fieldname'), 'value_type': data.get('value_type'), 'value_type_id': data.get('value_type_id'), 'value_int': data.get('value_int'), 'valueint_guid': data.get('valueint_guid'), 'value_string': data.get('value_string'), 'value_datetime': data.get('value_datetime'), 'value_float': data.get('value_float'), 'value_display': data.get('value_display'), 'alt_value_display': data.get('alt_value_display'), 'tablename': data.get('tablename'), 'timezonestring': data.get('timezonestring'), 'match_after_start': data.get('match_after_start'), 'match_after_target': data.get('match_after_target')})

@dataclass
class IntegrationFieldMapping:
    id: Optional[int] = None
    fiid: Optional[int] = None
    name: Optional[str] = None
    thirdpartyname: Optional[str] = None
    msid: Optional[int] = None
    typeid: Optional[int] = None
    isassetfield: Optional[bool] = None
    subtypeid: Optional[int] = None
    newrecords: Optional[bool] = None
    xmvalue: Optional[str] = None
    third_party_friendly_name: Optional[str] = None
    sync: Optional[bool] = None
    synctype: Optional[int] = None
    product: Optional[int] = None
    dontupdate: Optional[bool] = None
    product_name: Optional[str] = None
    third_party_field_type: Optional[int] = None
    populateemptyvalue: Optional[bool] = None
    value_set: Optional[str] = None
    _warning: Optional[str] = None
    fiid2: Optional[int] = None
    name2: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'IntegrationFieldMapping':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'fiid': data.get('fiid'), 'name': data.get('name'), 'thirdpartyname': data.get('thirdpartyname'), 'msid': data.get('msid'), 'typeid': data.get('typeid'), 'isassetfield': data.get('isassetfield'), 'subtypeid': data.get('subtypeid'), 'newrecords': data.get('newrecords'), 'xmvalue': data.get('xmvalue'), 'third_party_friendly_name': data.get('third_party_friendly_name'), 'sync': data.get('sync'), 'synctype': data.get('synctype'), 'product': data.get('product'), 'dontupdate': data.get('dontupdate'), 'product_name': data.get('product_name'), 'third_party_field_type': data.get('third_party_field_type'), 'populateemptyvalue': data.get('populateemptyvalue'), 'value_set': data.get('value_set'), '_warning': data.get('_warning'), 'fiid2': data.get('fiid2'), 'name2': data.get('name2')})

@dataclass
class KeyPair:
    id: Optional[str] = None
    name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'KeyPair':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name')})

@dataclass
class Organisation:
    guid: Optional[str] = None
    intent: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    reply_address: Optional[str] = None
    messagegroup_id: Optional[int] = None
    address: Optional[AddressStore] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    logo: Optional[str] = None
    portal_logo: Optional[str] = None
    portalbackgroundimageurl: Optional[str] = None
    deliverysite: Optional[int] = None
    portalurl: Optional[str] = None
    portalcolour: Optional[str] = None
    portalfolderlocation: Optional[str] = None
    departments: Optional[List[TreeList]] = None
    linked_client_id: Optional[int] = None
    allowall_tickettypes: Optional[bool] = None
    allowed_tickettypes: Optional[List[RequestTypeList]] = None
    faqlists: Optional[List[FaqListHead]] = None
    customfields: Optional[List[CustomField]] = None
    _warning: Optional[str] = None
    isorganisationdetails: Optional[bool] = None
    bank_details_line_1: Optional[str] = None
    bank_details_line_2: Optional[str] = None
    bank_details_line_3: Optional[str] = None
    bank_details_line_4: Optional[str] = None
    bank_details_line_5: Optional[str] = None
    tax_number: Optional[str] = None
    new_icon: Optional[str] = None
    portal_title: Optional[str] = None
    user_faqlists: Optional[List[FaqListHead]] = None
    all_user_faqlists_allowed: Optional[bool] = None
    portal_chat_profile_override: Optional[str] = None
    portal_chat_profile_override_name: Optional[str] = None
    portal_forethought_widget_override: Optional[int] = None
    forethought_widget_override_name: Optional[str] = None
    kb_favourites: Optional[List[KbEntryFavourites]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Organisation':
        if data is None:
            return None
        return cls(**{'guid': data.get('guid'), 'intent': data.get('intent'), 'id': data.get('id'), 'name': data.get('name'), 'reply_address': data.get('reply_address'), 'messagegroup_id': data.get('messagegroup_id'), 'address': data.get('address'), 'phone': data.get('phone'), 'fax': data.get('fax'), 'email': data.get('email'), 'website': data.get('website'), 'logo': data.get('logo'), 'portal_logo': data.get('portal_logo'), 'portalbackgroundimageurl': data.get('portalbackgroundimageurl'), 'deliverysite': data.get('deliverysite'), 'portalurl': data.get('portalurl'), 'portalcolour': data.get('portalcolour'), 'portalfolderlocation': data.get('portalfolderlocation'), 'departments': data.get('departments'), 'linked_client_id': data.get('linked_client_id'), 'allowall_tickettypes': data.get('allowall_tickettypes'), 'allowed_tickettypes': data.get('allowed_tickettypes'), 'faqlists': data.get('faqlists'), 'customfields': data.get('customfields'), '_warning': data.get('_warning'), 'isorganisationdetails': data.get('isorganisationdetails'), 'bank_details_line_1': data.get('bank_details_line_1'), 'bank_details_line_2': data.get('bank_details_line_2'), 'bank_details_line_3': data.get('bank_details_line_3'), 'bank_details_line_4': data.get('bank_details_line_4'), 'bank_details_line_5': data.get('bank_details_line_5'), 'tax_number': data.get('tax_number'), 'new_icon': data.get('new_icon'), 'portal_title': data.get('portal_title'), 'user_faqlists': data.get('user_faqlists'), 'all_user_faqlists_allowed': data.get('all_user_faqlists_allowed'), 'portal_chat_profile_override': data.get('portal_chat_profile_override'), 'portal_chat_profile_override_name': data.get('portal_chat_profile_override_name'), 'portal_forethought_widget_override': data.get('portal_forethought_widget_override'), 'forethought_widget_override_name': data.get('forethought_widget_override_name'), 'kb_favourites': data.get('kb_favourites')})

@dataclass
class PrepayHistory:
    id: Optional[int] = None
    client_id: Optional[int] = None
    client_name: Optional[str] = None
    date: Optional[str] = None
    hours: Optional[float] = None
    description: Optional[str] = None
    invoicedate: Optional[str] = None
    invoice_id: Optional[str] = None
    amount: Optional[float] = None
    expirydate: Optional[str] = None
    expirychecked: Optional[bool] = None
    _warning: Optional[str] = None
    invoice_number: Optional[str] = None
    client_to_invoice_to_id: Optional[int] = None
    recalc_expiry_records: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PrepayHistory':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'client_id': data.get('client_id'), 'client_name': data.get('client_name'), 'date': data.get('date'), 'hours': data.get('hours'), 'description': data.get('description'), 'invoicedate': data.get('invoicedate'), 'invoice_id': data.get('invoice_id'), 'amount': data.get('amount'), 'expirydate': data.get('expirydate'), 'expirychecked': data.get('expirychecked'), '_warning': data.get('_warning'), 'invoice_number': data.get('invoice_number'), 'client_to_invoice_to_id': data.get('client_to_invoice_to_id'), 'recalc_expiry_records': data.get('recalc_expiry_records')})

@dataclass
class PrepayPeriod:
    id: Optional[int] = None
    contract_id: Optional[int] = None
    name: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    start_date_display: Optional[str] = None
    end_date_display: Optional[str] = None
    current: Optional[bool] = None
    hours_added: Optional[float] = None
    hours_expired: Optional[float] = None
    hours_remaining: Optional[float] = None
    hours_used_this_period: Optional[float] = None
    amount_added: Optional[float] = None
    amount_expired: Optional[float] = None
    amount_remaining: Optional[float] = None
    amount_used_this_period: Optional[float] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PrepayPeriod':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'contract_id': data.get('contract_id'), 'name': data.get('name'), 'start_date': data.get('start_date'), 'end_date': data.get('end_date'), 'start_date_display': data.get('start_date_display'), 'end_date_display': data.get('end_date_display'), 'current': data.get('current'), 'hours_added': data.get('hours_added'), 'hours_expired': data.get('hours_expired'), 'hours_remaining': data.get('hours_remaining'), 'hours_used_this_period': data.get('hours_used_this_period'), 'amount_added': data.get('amount_added'), 'amount_expired': data.get('amount_expired'), 'amount_remaining': data.get('amount_remaining'), 'amount_used_this_period': data.get('amount_used_this_period')})

@dataclass
class QuickBooksDetails:
    id: Optional[int] = None
    name: Optional[str] = None
    country: Optional[str] = None
    company_id: Optional[str] = None
    company_name: Optional[str] = None
    new_access_token: Optional[str] = None
    new_refresh_token: Optional[str] = None
    token_expiry: Optional[str] = None
    authorized: Optional[bool] = None
    redirect_uri: Optional[str] = None
    authorization_code: Optional[str] = None
    _exchangecode: Optional[bool] = None
    _disconnect: Optional[bool] = None
    _importtype: Optional[str] = None
    new_method: Optional[bool] = None
    automatic_sales_tax: Optional[bool] = None
    online_payments: Optional[bool] = None
    accept_credit_card: Optional[bool] = None
    accept_bank_transfer: Optional[bool] = None
    api_url: Optional[str] = None
    client_id: Optional[str] = None
    new_client_secret: Optional[str] = None
    default_tax_code_id: Optional[int] = None
    default_tax_code_name: Optional[str] = None
    default_tax_code: Optional[KeyPair2] = None
    zero_tax_rate_id: Optional[int] = None
    zero_tax_rate_name: Optional[str] = None
    zero_tax_rate: Optional[KeyPair2] = None
    client_top_level: Optional[int] = None
    client_top_level_name: Optional[str] = None
    client_name_field: Optional[int] = None
    inventory_item_group: Optional[int] = None
    inventory_item_group_name: Optional[str] = None
    non_inventory_item_group: Optional[int] = None
    non_inventory_item_group_name: Optional[str] = None
    service_item_group: Optional[int] = None
    service_item_group_name: Optional[str] = None
    enable_sync: Optional[bool] = None
    sync_entities: Optional[str] = None
    sync_entities_list: Optional[List[KeyPair2]] = None
    show_message: Optional[bool] = None
    deactivate_customers: Optional[bool] = None
    default_invoice_item: Optional[int] = None
    default_order_item: Optional[int] = None
    default_invoice_item_name: Optional[str] = None
    default_order_item_name: Optional[str] = None
    invoice_email_status: Optional[int] = None
    supplier_top_level: Optional[int] = None
    supplier_top_level_name: Optional[str] = None
    supplier_name_field: Optional[int] = None
    invoice_custom_po: Optional[KeyPair2] = None
    invoice_custom_po_id: Optional[int] = None
    invoice_custom_po_name: Optional[str] = None
    custom_po_suppliers_order_reference: Optional[KeyPair2] = None
    custom_po_suppliers_order_reference_id: Optional[int] = None
    custom_po_suppliers_order_reference_name: Optional[str] = None
    default_order_account_id: Optional[int] = None
    default_order_account_name: Optional[str] = None
    default_order_account: Optional[KeyPair2] = None
    order_email_status: Optional[int] = None
    multi_currency: Optional[bool] = None
    default_sales_account_id: Optional[int] = None
    default_sales_account_name: Optional[str] = None
    default_sales_account: Optional[KeyPair2] = None
    default_expense_account_id: Optional[int] = None
    default_expense_account_name: Optional[str] = None
    default_expense_account: Optional[KeyPair2] = None
    default_asset_account_id: Optional[int] = None
    default_asset_account_name: Optional[str] = None
    default_asset_account: Optional[KeyPair2] = None
    receive_client_created: Optional[bool] = None
    receive_client_updated: Optional[bool] = None
    receive_payment_created: Optional[bool] = None
    receive_payment_updated: Optional[bool] = None
    receive_payment_deleted_and_voided: Optional[bool] = None
    sync_halo_invoice_id: Optional[bool] = None
    sync_invoice_class: Optional[bool] = None
    sync_invoice_bill_address: Optional[bool] = None
    sync_invoice_ship_address: Optional[bool] = None
    use_qbo_invoice_terms: Optional[bool] = None
    round_payments_to_2dp: Optional[bool] = None
    _warning: Optional[str] = None
    default_deferred_code_id: Optional[int] = None
    default_deferred_code_name: Optional[str] = None
    dont_post_item_quantities: Optional[bool] = None
    dont_sync_cost_tracking_lines: Optional[bool] = None
    remove_unapplied_payments: Optional[bool] = None
    default_deferred_account: Optional[KeyPair2] = None
    qbo_sitemappings: Optional[List[ExternalLinkList]] = None
    mark_as_void: Optional[bool] = None
    minor_version: Optional[int] = None
    sync_halo_po_id: Optional[bool] = None
    dont_sync_address: Optional[bool] = None
    sync_group_lines: Optional[bool] = None
    app_type: Optional[int] = None
    instance_type: Optional[int] = None
    get_invoice_link: Optional[bool] = None
    push_po_status: Optional[bool] = None
    close_period_date: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QuickBooksDetails':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name'), 'country': data.get('country'), 'company_id': data.get('company_id'), 'company_name': data.get('company_name'), 'new_access_token': data.get('new_access_token'), 'new_refresh_token': data.get('new_refresh_token'), 'token_expiry': data.get('token_expiry'), 'authorized': data.get('authorized'), 'redirect_uri': data.get('redirect_uri'), 'authorization_code': data.get('authorization_code'), '_exchangecode': data.get('_exchangecode'), '_disconnect': data.get('_disconnect'), '_importtype': data.get('_importtype'), 'new_method': data.get('new_method'), 'automatic_sales_tax': data.get('automatic_sales_tax'), 'online_payments': data.get('online_payments'), 'accept_credit_card': data.get('accept_credit_card'), 'accept_bank_transfer': data.get('accept_bank_transfer'), 'api_url': data.get('api_url'), 'client_id': data.get('client_id'), 'new_client_secret': data.get('new_client_secret'), 'default_tax_code_id': data.get('default_tax_code_id'), 'default_tax_code_name': data.get('default_tax_code_name'), 'default_tax_code': data.get('default_tax_code'), 'zero_tax_rate_id': data.get('zero_tax_rate_id'), 'zero_tax_rate_name': data.get('zero_tax_rate_name'), 'zero_tax_rate': data.get('zero_tax_rate'), 'client_top_level': data.get('client_top_level'), 'client_top_level_name': data.get('client_top_level_name'), 'client_name_field': data.get('client_name_field'), 'inventory_item_group': data.get('inventory_item_group'), 'inventory_item_group_name': data.get('inventory_item_group_name'), 'non_inventory_item_group': data.get('non_inventory_item_group'), 'non_inventory_item_group_name': data.get('non_inventory_item_group_name'), 'service_item_group': data.get('service_item_group'), 'service_item_group_name': data.get('service_item_group_name'), 'enable_sync': data.get('enable_sync'), 'sync_entities': data.get('sync_entities'), 'sync_entities_list': data.get('sync_entities_list'), 'show_message': data.get('show_message'), 'deactivate_customers': data.get('deactivate_customers'), 'default_invoice_item': data.get('default_invoice_item'), 'default_order_item': data.get('default_order_item'), 'default_invoice_item_name': data.get('default_invoice_item_name'), 'default_order_item_name': data.get('default_order_item_name'), 'invoice_email_status': data.get('invoice_email_status'), 'supplier_top_level': data.get('supplier_top_level'), 'supplier_top_level_name': data.get('supplier_top_level_name'), 'supplier_name_field': data.get('supplier_name_field'), 'invoice_custom_po': data.get('invoice_custom_po'), 'invoice_custom_po_id': data.get('invoice_custom_po_id'), 'invoice_custom_po_name': data.get('invoice_custom_po_name'), 'custom_po_suppliers_order_reference': data.get('custom_po_suppliers_order_reference'), 'custom_po_suppliers_order_reference_id': data.get('custom_po_suppliers_order_reference_id'), 'custom_po_suppliers_order_reference_name': data.get('custom_po_suppliers_order_reference_name'), 'default_order_account_id': data.get('default_order_account_id'), 'default_order_account_name': data.get('default_order_account_name'), 'default_order_account': data.get('default_order_account'), 'order_email_status': data.get('order_email_status'), 'multi_currency': data.get('multi_currency'), 'default_sales_account_id': data.get('default_sales_account_id'), 'default_sales_account_name': data.get('default_sales_account_name'), 'default_sales_account': data.get('default_sales_account'), 'default_expense_account_id': data.get('default_expense_account_id'), 'default_expense_account_name': data.get('default_expense_account_name'), 'default_expense_account': data.get('default_expense_account'), 'default_asset_account_id': data.get('default_asset_account_id'), 'default_asset_account_name': data.get('default_asset_account_name'), 'default_asset_account': data.get('default_asset_account'), 'receive_client_created': data.get('receive_client_created'), 'receive_client_updated': data.get('receive_client_updated'), 'receive_payment_created': data.get('receive_payment_created'), 'receive_payment_updated': data.get('receive_payment_updated'), 'receive_payment_deleted_and_voided': data.get('receive_payment_deleted_and_voided'), 'sync_halo_invoice_id': data.get('sync_halo_invoice_id'), 'sync_invoice_class': data.get('sync_invoice_class'), 'sync_invoice_bill_address': data.get('sync_invoice_bill_address'), 'sync_invoice_ship_address': data.get('sync_invoice_ship_address'), 'use_qbo_invoice_terms': data.get('use_qbo_invoice_terms'), 'round_payments_to_2dp': data.get('round_payments_to_2dp'), '_warning': data.get('_warning'), 'default_deferred_code_id': data.get('default_deferred_code_id'), 'default_deferred_code_name': data.get('default_deferred_code_name'), 'dont_post_item_quantities': data.get('dont_post_item_quantities'), 'dont_sync_cost_tracking_lines': data.get('dont_sync_cost_tracking_lines'), 'remove_unapplied_payments': data.get('remove_unapplied_payments'), 'default_deferred_account': data.get('default_deferred_account'), 'qbo_sitemappings': data.get('qbo_sitemappings'), 'mark_as_void': data.get('mark_as_void'), 'minor_version': data.get('minor_version'), 'sync_halo_po_id': data.get('sync_halo_po_id'), 'dont_sync_address': data.get('dont_sync_address'), 'sync_group_lines': data.get('sync_group_lines'), 'app_type': data.get('app_type'), 'instance_type': data.get('instance_type'), 'get_invoice_link': data.get('get_invoice_link'), 'push_po_status': data.get('push_po_status'), 'close_period_date': data.get('close_period_date')})

@dataclass
class RequestTypeList:
    id: Optional[int] = None
    guid: Optional[str] = None
    intent: Optional[str] = None
    name: Optional[str] = None
    use: Optional[str] = None
    sequence: Optional[int] = None
    default_sla: Optional[int] = None
    default_sla_guid: Optional[str] = None
    group_id: Optional[int] = None
    group_name: Optional[str] = None
    jira_issue_type: Optional[str] = None
    ticket_count: Optional[int] = None
    cancreate: Optional[bool] = None
    agentscanselect: Optional[bool] = None
    itilrequesttype: Optional[int] = None
    allow_all_clients: Optional[bool] = None
    allowattachments: Optional[bool] = None
    copyattachmentstochild: Optional[bool] = None
    copyattachmentstorelated: Optional[bool] = None
    is_sprint: Optional[bool] = None
    fieldidlist: Optional[List[int]] = None
    enduserscanselect: Optional[bool] = None
    anonymouscanselect: Optional[bool] = None
    hasmandatorytechfields: Optional[bool] = None
    hasmandatoryuserfields: Optional[bool] = None
    project_type: Optional[int] = None
    kanbanstatuschoice: Optional[List[KeyPair]] = None
    kanbanstatuschoice_list: Optional[str] = None
    email_start_tag: Optional[str] = None
    email_end_tag: Optional[str] = None
    default_agent: Optional[int] = None
    default_agent_name: Optional[str] = None
    default_team: Optional[str] = None
    workflow_name: Optional[str] = None
    overridewiththefollowingtemplatewhenloggingmanuallyname: Optional[str] = None
    default_priority: Optional[int] = None
    visible: Optional[bool] = None
    webhook_id: Optional[str] = None
    _error: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RequestTypeList':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'guid': data.get('guid'), 'intent': data.get('intent'), 'name': data.get('name'), 'use': data.get('use'), 'sequence': data.get('sequence'), 'default_sla': data.get('default_sla'), 'default_sla_guid': data.get('default_sla_guid'), 'group_id': data.get('group_id'), 'group_name': data.get('group_name'), 'jira_issue_type': data.get('jira_issue_type'), 'ticket_count': data.get('ticket_count'), 'cancreate': data.get('cancreate'), 'agentscanselect': data.get('agentscanselect'), 'itilrequesttype': data.get('itilrequesttype'), 'allow_all_clients': data.get('allow_all_clients'), 'allowattachments': data.get('allowattachments'), 'copyattachmentstochild': data.get('copyattachmentstochild'), 'copyattachmentstorelated': data.get('copyattachmentstorelated'), 'is_sprint': data.get('is_sprint'), 'fieldidlist': data.get('fieldidlist'), 'enduserscanselect': data.get('enduserscanselect'), 'anonymouscanselect': data.get('anonymouscanselect'), 'hasmandatorytechfields': data.get('hasmandatorytechfields'), 'hasmandatoryuserfields': data.get('hasmandatoryuserfields'), 'project_type': data.get('project_type'), 'kanbanstatuschoice': data.get('kanbanstatuschoice'), 'kanbanstatuschoice_list': data.get('kanbanstatuschoice_list'), 'email_start_tag': data.get('email_start_tag'), 'email_end_tag': data.get('email_end_tag'), 'default_agent': data.get('default_agent'), 'default_agent_name': data.get('default_agent_name'), 'default_team': data.get('default_team'), 'workflow_name': data.get('workflow_name'), 'overridewiththefollowingtemplatewhenloggingmanuallyname': data.get('overridewiththefollowingtemplatewhenloggingmanuallyname'), 'default_priority': data.get('default_priority'), 'visible': data.get('visible'), 'webhook_id': data.get('webhook_id'), '_error': data.get('_error')})

@dataclass
class SectionDetailList:
    id: Optional[int] = None
    guid: Optional[str] = None
    intent: Optional[str] = None
    name: Optional[str] = None
    sequence: Optional[int] = None
    forrequests: Optional[bool] = None
    foropps: Optional[bool] = None
    forprojects: Optional[bool] = None
    ticket_count: Optional[int] = None
    department_id: Optional[int] = None
    department_name: Optional[str] = None
    org_team_name: Optional[str] = None
    inactive: Optional[bool] = None
    override_column_id: Optional[int] = None
    agents: Optional[List[UnameList]] = None
    managers: Optional[List[Manager]] = None
    teamphotopath: Optional[str] = None
    last_modified: Optional[str] = None
    hide_agents_in_tree_if_no_tickets: Optional[bool] = None
    timesheet_approver: Optional[int] = None
    timesheet_approver_name: Optional[str] = None
    concurrent_lic_limit: Optional[int] = None
    use: Optional[str] = None
    department_guid: Optional[str] = None
    homescreendashboardid: Optional[int] = None
    homescreendashboardname: Optional[str] = None
    customfields: Optional[List[CustomField]] = None
    mailbox_override: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SectionDetailList':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'guid': data.get('guid'), 'intent': data.get('intent'), 'name': data.get('name'), 'sequence': data.get('sequence'), 'forrequests': data.get('forrequests'), 'foropps': data.get('foropps'), 'forprojects': data.get('forprojects'), 'ticket_count': data.get('ticket_count'), 'department_id': data.get('department_id'), 'department_name': data.get('department_name'), 'org_team_name': data.get('org_team_name'), 'inactive': data.get('inactive'), 'override_column_id': data.get('override_column_id'), 'agents': data.get('agents'), 'managers': data.get('managers'), 'teamphotopath': data.get('teamphotopath'), 'last_modified': data.get('last_modified'), 'hide_agents_in_tree_if_no_tickets': data.get('hide_agents_in_tree_if_no_tickets'), 'timesheet_approver': data.get('timesheet_approver'), 'timesheet_approver_name': data.get('timesheet_approver_name'), 'concurrent_lic_limit': data.get('concurrent_lic_limit'), 'use': data.get('use'), 'department_guid': data.get('department_guid'), 'homescreendashboardid': data.get('homescreendashboardid'), 'homescreendashboardname': data.get('homescreendashboardname'), 'customfields': data.get('customfields'), 'mailbox_override': data.get('mailbox_override')})

@dataclass
class ServiceMapping:
    id: Optional[int] = None
    module_id: Optional[int] = None
    entity_id: Optional[int] = None
    entity_type: Optional[int] = None
    halo_id: Optional[int] = None
    service_name: Optional[str] = None
    thirdparty_id: Optional[str] = None
    thirdparty_name: Optional[str] = None
    service_field_mappings: Optional[List[IntegrationFieldMapping]] = None
    _warning: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ServiceMapping':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'module_id': data.get('module_id'), 'entity_id': data.get('entity_id'), 'entity_type': data.get('entity_type'), 'halo_id': data.get('halo_id'), 'service_name': data.get('service_name'), 'thirdparty_id': data.get('thirdparty_id'), 'thirdparty_name': data.get('thirdparty_name'), 'service_field_mappings': data.get('service_field_mappings'), '_warning': data.get('_warning')})

@dataclass
class SnowDevice:
    id: Optional[int] = None
    name: Optional[str] = None
    organization: Optional[str] = None
    org_checksum: Optional[int] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    operating_system: Optional[str] = None
    operating_system_service_pack: Optional[str] = None
    is_virtual: Optional[bool] = None
    status: Optional[str] = None
    ip_addresses: Optional[str] = None
    last_scan_date: Optional[str] = None
    updated_by: Optional[str] = None
    updated_date: Optional[str] = None
    domain: Optional[str] = None
    total_disk_space: Optional[int] = None
    physical_memory: Optional[int] = None
    processor_type: Optional[str] = None
    processor_count: Optional[int] = None
    core_count: Optional[int] = None
    bios_serial_number: Optional[str] = None
    hypervisor_name: Optional[str] = None
    most_frequent_user_id: Optional[int] = None
    most_recent_user_id: Optional[int] = None
    hardware: Optional[SnowHardware] = None
    bios_version: Optional[str] = None
    bios_date: Optional[str] = None
    number_of_processors: Optional[int] = None
    cores_per_processor: Optional[int] = None
    physical_memory_mb: Optional[int] = None
    memory_slots: Optional[int] = None
    memory_slots_available: Optional[int] = None
    system_disk_space_mb: Optional[int] = None
    system_disk_space_available_mb: Optional[int] = None
    total_disk_space_mb: Optional[int] = None
    total_disk_space_available_mb: Optional[int] = None
    phone_number: Optional[str] = None
    mobile_device_type: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SnowDevice':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name'), 'organization': data.get('organization'), 'org_checksum': data.get('orgChecksum'), 'manufacturer': data.get('manufacturer'), 'model': data.get('model'), 'operating_system': data.get('operatingSystem'), 'operating_system_service_pack': data.get('operatingSystemServicePack'), 'is_virtual': data.get('isVirtual'), 'status': data.get('status'), 'ip_addresses': data.get('ipAddresses'), 'last_scan_date': data.get('lastScanDate'), 'updated_by': data.get('updatedBy'), 'updated_date': data.get('updatedDate'), 'domain': data.get('domain'), 'total_disk_space': data.get('totalDiskSpace'), 'physical_memory': data.get('physicalMemory'), 'processor_type': data.get('processorType'), 'processor_count': data.get('processorCount'), 'core_count': data.get('coreCount'), 'bios_serial_number': data.get('biosSerialNumber'), 'hypervisor_name': data.get('hypervisorName'), 'most_frequent_user_id': data.get('mostFrequentUserId'), 'most_recent_user_id': data.get('mostRecentUserId'), 'hardware': data.get('hardware'), 'bios_version': data.get('biosVersion'), 'bios_date': data.get('biosDate'), 'number_of_processors': data.get('numberOfProcessors'), 'cores_per_processor': data.get('coresPerProcessor'), 'physical_memory_mb': data.get('physicalMemoryMb'), 'memory_slots': data.get('memorySlots'), 'memory_slots_available': data.get('memorySlotsAvailable'), 'system_disk_space_mb': data.get('systemDiskSpaceMb'), 'system_disk_space_available_mb': data.get('systemDiskSpaceAvailableMb'), 'total_disk_space_mb': data.get('totalDiskSpaceMb'), 'total_disk_space_available_mb': data.get('totalDiskSpaceAvailableMb'), 'phone_number': data.get('phoneNumber'), 'mobile_device_type': data.get('mobileDeviceType')})

@dataclass
class SnowHardware:
    bios_serial_number: Optional[str] = None
    bios_version: Optional[str] = None
    bios_date: Optional[str] = None
    processor_type: Optional[str] = None
    number_of_processors: Optional[int] = None
    cores_per_processor: Optional[int] = None
    physical_memory_mb: Optional[int] = None
    memory_slots: Optional[int] = None
    memory_slots_available: Optional[int] = None
    system_disk_space_mb: Optional[int] = None
    system_disk_space_available_mb: Optional[int] = None
    total_disk_space_mb: Optional[int] = None
    total_disk_space_available_mb: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SnowHardware':
        if data is None:
            return None
        return cls(**{'bios_serial_number': data.get('biosSerialNumber'), 'bios_version': data.get('biosVersion'), 'bios_date': data.get('biosDate'), 'processor_type': data.get('processorType'), 'number_of_processors': data.get('numberOfProcessors'), 'cores_per_processor': data.get('coresPerProcessor'), 'physical_memory_mb': data.get('physicalMemoryMb'), 'memory_slots': data.get('memorySlots'), 'memory_slots_available': data.get('memorySlotsAvailable'), 'system_disk_space_mb': data.get('systemDiskSpaceMb'), 'system_disk_space_available_mb': data.get('systemDiskSpaceAvailableMb'), 'total_disk_space_mb': data.get('totalDiskSpaceMb'), 'total_disk_space_available_mb': data.get('totalDiskSpaceAvailableMb')})

@dataclass
class SnowLicenseAbstract:
    id: Optional[int] = None
    application_name: Optional[str] = None
    manufacturer_name: Optional[str] = None
    metric: Optional[str] = None
    assignment_type: Optional[str] = None
    purchase_date: Optional[str] = None
    quantity: Optional[int] = None
    is_incomplete: Optional[bool] = None
    updated_date: Optional[str] = None
    updated_by: Optional[str] = None
    snow_devices: Optional[List[SnowDevice]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SnowLicenseAbstract':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'application_name': data.get('applicationName'), 'manufacturer_name': data.get('manufacturerName'), 'metric': data.get('metric'), 'assignment_type': data.get('assignmentType'), 'purchase_date': data.get('purchaseDate'), 'quantity': data.get('quantity'), 'is_incomplete': data.get('isIncomplete'), 'updated_date': data.get('updatedDate'), 'updated_by': data.get('updatedBy'), 'snow_devices': data.get('snowDevices')})

@dataclass
class StripePaymentMethod:
    id: Optional[str] = None
    name: Optional[str] = None
    hint: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'StripePaymentMethod':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name'), 'hint': data.get('hint')})

@dataclass
class TreeList:
    id: Optional[int] = None
    guid: Optional[str] = None
    intent: Optional[str] = None
    name: Optional[str] = None
    accounts_override_mailbox: Optional[int] = None
    concurrent_lic_limit: Optional[int] = None
    organisation_id: Optional[int] = None
    organisation_guid: Optional[str] = None
    organisation_name: Optional[str] = None
    org_department_name: Optional[str] = None
    long_name: Optional[str] = None
    type: Optional[int] = None
    teams: Optional[List[SectionDetailList]] = None
    agent_members: Optional[List[UnameList]] = None
    managers: Optional[List[Manager]] = None
    user_count: Optional[int] = None
    open_ticket_count: Optional[int] = None
    onhold_ticket_count: Optional[int] = None
    total_ticket_count: Optional[int] = None
    opened_thismonth_count: Optional[int] = None
    customfields: Optional[List[CustomField]] = None
    agent_department: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TreeList':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'guid': data.get('guid'), 'intent': data.get('intent'), 'name': data.get('name'), 'accounts_override_mailbox': data.get('accounts_override_mailbox'), 'concurrent_lic_limit': data.get('concurrent_lic_limit'), 'organisation_id': data.get('organisation_id'), 'organisation_guid': data.get('organisation_guid'), 'organisation_name': data.get('organisation_name'), 'org_department_name': data.get('org_department_name'), 'long_name': data.get('long_name'), 'type': data.get('type'), 'teams': data.get('teams'), 'agent_members': data.get('agent_members'), 'managers': data.get('managers'), 'user_count': data.get('user_count'), 'open_ticket_count': data.get('open_ticket_count'), 'onhold_ticket_count': data.get('onhold_ticket_count'), 'total_ticket_count': data.get('total_ticket_count'), 'opened_thismonth_count': data.get('opened_thismonth_count'), 'customfields': data.get('customfields'), 'agent_department': data.get('agent_department')})

@dataclass
class UnameList:
    id: Optional[int] = None
    name: Optional[str] = None
    onlinestatus_actual: Optional[int] = None
    onlinestatus: Optional[int] = None
    is_online: Optional[bool] = None
    lastonline: Optional[str] = None
    team: Optional[str] = None
    isdisabled: Optional[bool] = None
    email: Optional[str] = None
    ad: Optional[str] = None
    lastlogindate: Optional[str] = None
    agentphotopath: Optional[str] = None
    initials: Optional[str] = None
    firstname: Optional[str] = None
    surname: Optional[str] = None
    colour: Optional[str] = None
    jobtitle: Optional[str] = None
    sms: Optional[str] = None
    extensionnumber: Optional[str] = None
    ticket_count: Optional[int] = None
    is_agent: Optional[bool] = None
    one_client: Optional[int] = None
    teams: Optional[List[UnameSection]] = None
    departments: Optional[List[UnameDepartment]] = None
    clients: Optional[List[UnameAreaRestriction]] = None
    tickettypes: Optional[List[UnameRequestType]] = None
    qualifications: Optional[List[UnameQualification]] = None
    qualification_weighting: Optional[int] = None
    qualified: Optional[bool] = None
    role_list: Optional[str] = None
    current_action_type: Optional[str] = None
    current_action_name: Optional[str] = None
    assettypes: Optional[List[UnameXtype]] = None
    googleemail: Optional[str] = None
    linemanager: Optional[int] = None
    linemanager_name: Optional[str] = None
    inboxes: Optional[int] = None
    exchange_authorized: Optional[bool] = None
    exchange_account: Optional[str] = None
    sentinel_authorized: Optional[bool] = None
    licence_type: Optional[int] = None
    named_licences_in_use: Optional[int] = None
    concurrent_licences_in_use: Optional[int] = None
    concurrent_agent_total: Optional[int] = None
    google_mail_authorized: Optional[bool] = None
    inbox_clientid: Optional[str] = None
    isapiagent: Optional[bool] = None
    splashtop_authorized: Optional[bool] = None
    gotoresolve_authorized: Optional[bool] = None
    use: Optional[str] = None
    assetfields: Optional[List[UnameField]] = None
    unamecustomfields: Optional[List[UnameCustom]] = None
    unameappointmenttypes: Optional[List[UnameAppointment]] = None
    _canupdate: Optional[bool] = None
    _canupdate_moreinfo: Optional[bool] = None
    logmeinid: Optional[str] = None
    allowbeyondtrustinvites: Optional[bool] = None
    jira_id: Optional[str] = None
    custombuttons: Optional[List[UnameButton]] = None
    namewithinactive: Optional[str] = None
    apptsync: Optional[int] = None
    okta_id: Optional[str] = None
    enableshifts: Optional[bool] = None
    sendemailerrors: Optional[bool] = None
    uname_usercustomfields: Optional[List[UnameCustom]] = None
    can_approve_purchaseorder: Optional[bool] = None
    can_approve_quote: Optional[bool] = None
    can_approve_invoice: Optional[bool] = None
    default_splashtop_channel: Optional[int] = None
    workday_id: Optional[int] = None
    workday_name: Optional[str] = None
    workday_timezone: Optional[str] = None
    timezone: Optional[str] = None
    costprice: Optional[float] = None
    chargerate: Optional[int] = None
    first_role_id: Optional[str] = None
    in_queried_team: Optional[bool] = None
    guid_string: Optional[str] = None
    third_party_guid: Optional[str] = None
    timesheet_approver: Optional[int] = None
    is_member_of_all_departments: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UnameList':
        if data is None:
            return None
        return cls(**{'id': data.get('id'), 'name': data.get('name'), 'onlinestatus_actual': data.get('onlinestatus_actual'), 'onlinestatus': data.get('onlinestatus'), 'is_online': data.get('is_online'), 'lastonline': data.get('lastonline'), 'team': data.get('team'), 'isdisabled': data.get('isdisabled'), 'email': data.get('email'), 'ad': data.get('ad'), 'lastlogindate': data.get('lastlogindate'), 'agentphotopath': data.get('agentphotopath'), 'initials': data.get('initials'), 'firstname': data.get('firstname'), 'surname': data.get('surname'), 'colour': data.get('colour'), 'jobtitle': data.get('jobtitle'), 'sms': data.get('sms'), 'extensionnumber': data.get('extensionnumber'), 'ticket_count': data.get('ticket_count'), 'is_agent': data.get('is_agent'), 'one_client': data.get('one_client'), 'teams': data.get('teams'), 'departments': data.get('departments'), 'clients': data.get('clients'), 'tickettypes': data.get('tickettypes'), 'qualifications': data.get('qualifications'), 'qualification_weighting': data.get('qualification_weighting'), 'qualified': data.get('qualified'), 'role_list': data.get('role_list'), 'current_action_type': data.get('current_action_type'), 'current_action_name': data.get('current_action_name'), 'assettypes': data.get('assettypes'), 'googleemail': data.get('googleemail'), 'linemanager': data.get('linemanager'), 'linemanager_name': data.get('linemanager_name'), 'inboxes': data.get('inboxes'), 'exchange_authorized': data.get('exchange_authorized'), 'exchange_account': data.get('exchange_account'), 'sentinel_authorized': data.get('sentinel_authorized'), 'licence_type': data.get('licence_type'), 'named_licences_in_use': data.get('named_licences_in_use'), 'concurrent_licences_in_use': data.get('concurrent_licences_in_use'), 'concurrent_agent_total': data.get('concurrent_agent_total'), 'google_mail_authorized': data.get('google_mail_authorized'), 'inbox_clientid': data.get('inbox_clientid'), 'isapiagent': data.get('isapiagent'), 'splashtop_authorized': data.get('splashtop_authorized'), 'gotoresolve_authorized': data.get('gotoresolve_authorized'), 'use': data.get('use'), 'assetfields': data.get('assetfields'), 'unamecustomfields': data.get('unamecustomfields'), 'unameappointmenttypes': data.get('unameappointmenttypes'), '_canupdate': data.get('_canupdate'), '_canupdate_moreinfo': data.get('_canupdate_moreinfo'), 'logmeinid': data.get('logmeinid'), 'allowbeyondtrustinvites': data.get('allowbeyondtrustinvites'), 'jira_id': data.get('jira_id'), 'custombuttons': data.get('custombuttons'), 'namewithinactive': data.get('namewithinactive'), 'apptsync': data.get('apptsync'), 'okta_id': data.get('okta_id'), 'enableshifts': data.get('enableshifts'), 'sendemailerrors': data.get('sendemailerrors'), 'uname_usercustomfields': data.get('uname_usercustomfields'), 'can_approve_purchaseorder': data.get('can_approve_purchaseorder'), 'can_approve_quote': data.get('can_approve_quote'), 'can_approve_invoice': data.get('can_approve_invoice'), 'default_splashtop_channel': data.get('default_splashtop_channel'), 'workday_id': data.get('workday_id'), 'workday_name': data.get('workday_name'), 'workday_timezone': data.get('workday_timezone'), 'timezone': data.get('timezone'), 'costprice': data.get('costprice'), 'chargerate': data.get('chargerate'), 'first_role_id': data.get('first_role_id'), 'in_queried_team': data.get('in_queried_team'), 'guid_string': data.get('guid_string'), 'third_party_guid': data.get('third_party_guid'), 'timesheet_approver': data.get('timesheet_approver'), 'is_member_of_all_departments': data.get('is_member_of_all_departments')})

def list_clients(client, **kwargs):
    """List of Area"""
    url = f'{client.base_url}/Client'
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

def create_client(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Client"""
    url = f'{client.base_url}/Client'
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

def create_new_accounts_id(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Client/NewAccountsId"""
    url = f'{client.base_url}/Client/NewAccountsId'
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

def create_payment_method_update(client, data: Dict[str, Any]=None, **kwargs):
    """POST /Client/PaymentMethodUpdate"""
    url = f'{client.base_url}/Client/PaymentMethodUpdate'
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

def list_mes_1(client, **kwargs):
    """GET /Client/me"""
    url = f'{client.base_url}/Client/me'
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

def get_client(client, id: str, **kwargs):
    """Get one Area"""
    url = f'{client.base_url}/Client/{id}'
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

def delete_client(client, id: str, **kwargs):
    """DELETE /Client/{id}"""
    url = f'{client.base_url}/Client/{id}'
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
