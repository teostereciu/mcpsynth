"""Twilio Phone Numbers API tools.

Covers:
- AvailablePhoneNumbers (Local/Mobile/TollFree)
- IncomingPhoneNumbers (purchase/manage)
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import core_delete, core_get, core_post


def available_phone_numbers_local_list(
    *,
    country_code: str,
    page_size: int = 50,
    area_code: Optional[int] = None,
    contains: Optional[str] = None,
    sms_enabled: Optional[bool] = None,
    mms_enabled: Optional[bool] = None,
    voice_enabled: Optional[bool] = None,
) -> Dict[str, Any]:
    """List available local phone numbers for purchase."""
    params: Dict[str, Any] = {"PageSize": page_size}
    if area_code is not None:
        params["AreaCode"] = area_code
    if contains is not None:
        params["Contains"] = contains
    if sms_enabled is not None:
        params["SmsEnabled"] = str(sms_enabled).lower()
    if mms_enabled is not None:
        params["MmsEnabled"] = str(mms_enabled).lower()
    if voice_enabled is not None:
        params["VoiceEnabled"] = str(voice_enabled).lower()
    return core_get(f"/AvailablePhoneNumbers/{country_code}/Local.json", params=params)


def incoming_phone_numbers_list(*, page_size: int = 50) -> Dict[str, Any]:
    """List incoming (owned) phone numbers."""
    return core_get("/IncomingPhoneNumbers.json", params={"PageSize": page_size})


def incoming_phone_numbers_fetch(*, incoming_phone_number_sid: str) -> Dict[str, Any]:
    """Fetch an incoming phone number by SID (PN...)."""
    return core_get(f"/IncomingPhoneNumbers/{incoming_phone_number_sid}.json")


def incoming_phone_numbers_create(
    *,
    phone_number: str,
    friendly_name: Optional[str] = None,
    sms_url: Optional[str] = None,
    voice_url: Optional[str] = None,
) -> Dict[str, Any]:
    """Purchase (create) an incoming phone number."""
    data: Dict[str, Any] = {"PhoneNumber": phone_number}
    if friendly_name is not None:
        data["FriendlyName"] = friendly_name
    if sms_url is not None:
        data["SmsUrl"] = sms_url
    if voice_url is not None:
        data["VoiceUrl"] = voice_url
    return core_post("/IncomingPhoneNumbers.json", data=data)


def incoming_phone_numbers_update(
    *,
    incoming_phone_number_sid: str,
    friendly_name: Optional[str] = None,
    sms_url: Optional[str] = None,
    voice_url: Optional[str] = None,
) -> Dict[str, Any]:
    """Update an incoming phone number."""
    data: Dict[str, Any] = {}
    if friendly_name is not None:
        data["FriendlyName"] = friendly_name
    if sms_url is not None:
        data["SmsUrl"] = sms_url
    if voice_url is not None:
        data["VoiceUrl"] = voice_url
    return core_post(f"/IncomingPhoneNumbers/{incoming_phone_number_sid}.json", data=data)


def incoming_phone_numbers_delete(*, incoming_phone_number_sid: str) -> Dict[str, Any]:
    """Release (delete) an incoming phone number."""
    return core_delete(f"/IncomingPhoneNumbers/{incoming_phone_number_sid}.json")
