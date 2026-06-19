from typing import Any, Dict, Optional

from .twilio_client import TwilioClient, accounts_base_url


def list_incoming_phone_numbers(
    *,
    phone_number: Optional[str] = None,
    friendly_name: Optional[str] = None,
    page_size: int = 50,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /IncomingPhoneNumbers.json - List purchased/provisioned numbers."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/IncomingPhoneNumbers.json"
    params: Dict[str, Any] = {
        "PhoneNumber": phone_number,
        "FriendlyName": friendly_name,
        "PageSize": page_size,
        "Page": page,
    }
    return client.request("GET", url, params=params)


def fetch_incoming_phone_number(sid: str) -> Dict[str, Any]:
    """GET /IncomingPhoneNumbers/{Sid}.json - Fetch a purchased number."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/IncomingPhoneNumbers/{sid}.json"
    return client.request("GET", url)


def purchase_incoming_phone_number(
    *,
    phone_number: Optional[str] = None,
    area_code: Optional[str] = None,
    friendly_name: Optional[str] = None,
    voice_url: Optional[str] = None,
    sms_url: Optional[str] = None,
    status_callback: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /IncomingPhoneNumbers.json - Purchase/provision a phone number.

    Provide phone_number or area_code.
    """
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/IncomingPhoneNumbers.json"
    data: Dict[str, Any] = {
        "PhoneNumber": phone_number,
        "AreaCode": area_code,
        "FriendlyName": friendly_name,
        "VoiceUrl": voice_url,
        "SmsUrl": sms_url,
        "StatusCallback": status_callback,
    }
    return client.request("POST", url, data=data)


def update_incoming_phone_number(
    sid: str,
    *,
    friendly_name: Optional[str] = None,
    voice_url: Optional[str] = None,
    sms_url: Optional[str] = None,
    status_callback: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /IncomingPhoneNumbers/{Sid}.json - Update a purchased number."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/IncomingPhoneNumbers/{sid}.json"
    data: Dict[str, Any] = {
        "FriendlyName": friendly_name,
        "VoiceUrl": voice_url,
        "SmsUrl": sms_url,
        "StatusCallback": status_callback,
    }
    return client.request("POST", url, data=data)


def delete_incoming_phone_number(sid: str) -> Dict[str, Any]:
    """DELETE /IncomingPhoneNumbers/{Sid}.json - Release a phone number."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/IncomingPhoneNumbers/{sid}.json"
    return client.request("DELETE", url)


def search_available_local_numbers(
    country_code: str,
    *,
    area_code: Optional[int] = None,
    contains: Optional[str] = None,
    sms_enabled: Optional[bool] = None,
    mms_enabled: Optional[bool] = None,
    voice_enabled: Optional[bool] = None,
    exclude_all_address_required: Optional[bool] = None,
    exclude_local_address_required: Optional[bool] = None,
    exclude_foreign_address_required: Optional[bool] = None,
    near_number: Optional[str] = None,
    near_lat_long: Optional[str] = None,
    distance: Optional[int] = None,
    in_postal_code: Optional[str] = None,
    in_region: Optional[str] = None,
    in_rate_center: Optional[str] = None,
    in_lata: Optional[str] = None,
    in_locality: Optional[str] = None,
    fax_enabled: Optional[bool] = None,
    page_size: int = 50,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /AvailablePhoneNumbers/{CountryCode}/Local.json - Search available local numbers."""
    client = TwilioClient()
    url = (
        f"{accounts_base_url(client.account_sid)}/AvailablePhoneNumbers/{country_code}/Local.json"
    )
    params: Dict[str, Any] = {
        "AreaCode": area_code,
        "Contains": contains,
        "SmsEnabled": sms_enabled,
        "MmsEnabled": mms_enabled,
        "VoiceEnabled": voice_enabled,
        "ExcludeAllAddressRequired": exclude_all_address_required,
        "ExcludeLocalAddressRequired": exclude_local_address_required,
        "ExcludeForeignAddressRequired": exclude_foreign_address_required,
        "NearNumber": near_number,
        "NearLatLong": near_lat_long,
        "Distance": distance,
        "InPostalCode": in_postal_code,
        "InRegion": in_region,
        "InRateCenter": in_rate_center,
        "InLata": in_lata,
        "InLocality": in_locality,
        "FaxEnabled": fax_enabled,
        "PageSize": page_size,
        "Page": page,
    }
    return client.request("GET", url, params=params)
