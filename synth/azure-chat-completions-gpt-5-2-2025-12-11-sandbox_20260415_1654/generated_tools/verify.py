from typing import Any, Dict, Optional

from .twilio_client import TwilioClient, verify_base_url


def start_verification(
    service_sid: str,
    to: str,
    channel: str,
    *,
    locale: Optional[str] = None,
    custom_friendly_name: Optional[str] = None,
    custom_code: Optional[str] = None,
    app_hash: Optional[str] = None,
    template_sid: Optional[str] = None,
    template_custom_substitutions: Optional[str] = None,
    risk_check: Optional[str] = None,
    tags: Optional[str] = None,
    enable_sna_client_token: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /Services/{ServiceSid}/Verifications - Start a new verification."""
    client = TwilioClient()
    url = f"{verify_base_url()}/Services/{service_sid}/Verifications"
    data: Dict[str, Any] = {
        "To": to,
        "Channel": channel,
        "Locale": locale,
        "CustomFriendlyName": custom_friendly_name,
        "CustomCode": custom_code,
        "AppHash": app_hash,
        "TemplateSid": template_sid,
        "TemplateCustomSubstitutions": template_custom_substitutions,
        "RiskCheck": risk_check,
        "Tags": tags,
        "EnableSnaClientToken": enable_sna_client_token,
    }
    return client.request("POST", url, data=data)


def check_verification(
    service_sid: str,
    *,
    code: Optional[str] = None,
    to: Optional[str] = None,
    verification_sid: Optional[str] = None,
    sna_client_token: Optional[str] = None,
    amount: Optional[str] = None,
    payee: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /Services/{ServiceSid}/VerificationCheck - Check a verification code."""
    client = TwilioClient()
    url = f"{verify_base_url()}/Services/{service_sid}/VerificationCheck"
    data: Dict[str, Any] = {
        "Code": code,
        "To": to,
        "VerificationSid": verification_sid,
        "SnaClientToken": sna_client_token,
        "Amount": amount,
        "Payee": payee,
    }
    return client.request("POST", url, data=data)
