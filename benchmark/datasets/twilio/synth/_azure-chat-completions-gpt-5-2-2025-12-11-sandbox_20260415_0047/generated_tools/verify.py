"""Twilio Verify API v2 tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import verify_delete, verify_get, verify_post


def verify_services_create(*, friendly_name: str, code_length: Optional[int] = None) -> Dict[str, Any]:
    """Create a Verify Service (VA...)."""
    data: Dict[str, Any] = {"FriendlyName": friendly_name}
    if code_length is not None:
        data["CodeLength"] = code_length
    return verify_post("/Services", data=data)


def verify_services_list(*, page_size: int = 50) -> Dict[str, Any]:
    """List Verify services."""
    return verify_get("/Services", params={"PageSize": page_size})


def verify_services_fetch(*, service_sid: str) -> Dict[str, Any]:
    """Fetch a Verify service by SID."""
    return verify_get(f"/Services/{service_sid}")


def verify_services_update(
    *,
    service_sid: str,
    friendly_name: Optional[str] = None,
    code_length: Optional[int] = None,
) -> Dict[str, Any]:
    """Update a Verify service."""
    data: Dict[str, Any] = {}
    if friendly_name is not None:
        data["FriendlyName"] = friendly_name
    if code_length is not None:
        data["CodeLength"] = code_length
    return verify_post(f"/Services/{service_sid}", data=data)


def verify_services_delete(*, service_sid: str) -> Dict[str, Any]:
    """Delete a Verify service."""
    return verify_delete(f"/Services/{service_sid}")


def verifications_create(
    *,
    service_sid: str,
    to: str,
    channel: str,
    locale: Optional[str] = None,
) -> Dict[str, Any]:
    """Start a verification (send OTP)."""
    data: Dict[str, Any] = {"To": to, "Channel": channel}
    if locale is not None:
        data["Locale"] = locale
    return verify_post(f"/Services/{service_sid}/Verifications", data=data)


def verification_checks_create(
    *,
    service_sid: str,
    to: str,
    code: str,
) -> Dict[str, Any]:
    """Check a verification code."""
    data: Dict[str, Any] = {"To": to, "Code": code}
    return verify_post(f"/Services/{service_sid}/VerificationCheck", data=data)
