from typing import Any, Dict, Optional

from .twilio_client import TwilioClient, accounts_base_url


def send_message(
    to: str,
    *,
    body: Optional[str] = None,
    from_: Optional[str] = None,
    messaging_service_sid: Optional[str] = None,
    media_url: Optional[str] = None,
    status_callback: Optional[str] = None,
    provide_feedback: Optional[bool] = None,
    validity_period: Optional[int] = None,
    max_price: Optional[float] = None,
    attempt: Optional[int] = None,
) -> Dict[str, Any]:
    """POST /Messages.json - Send an SMS/MMS/WhatsApp/etc message.

    Requires: to, and one of (from_, messaging_service_sid), and one of (body, media_url).
    """
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/Messages.json"
    data: Dict[str, Any] = {
        "To": to,
        "Body": body,
        "From": from_,
        "MessagingServiceSid": messaging_service_sid,
        "MediaUrl": media_url,
        "StatusCallback": status_callback,
        "ProvideFeedback": provide_feedback,
        "ValidityPeriod": validity_period,
        "MaxPrice": max_price,
        "Attempt": attempt,
    }
    return client.request("POST", url, data=data)


def fetch_message(message_sid: str) -> Dict[str, Any]:
    """GET /Messages/{Sid}.json - Fetch a specific message."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/Messages/{message_sid}.json"
    return client.request("GET", url)


def list_messages(
    *,
    to: Optional[str] = None,
    from_: Optional[str] = None,
    date_sent: Optional[str] = None,
    page_size: int = 50,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /Messages.json - List messages.

    Note: Twilio uses PageSize/Page for classic 2010-04-01 list endpoints.
    """
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/Messages.json"
    params: Dict[str, Any] = {
        "To": to,
        "From": from_,
        "DateSent": date_sent,
        "PageSize": page_size,
        "Page": page,
    }
    return client.request("GET", url, params=params)


def delete_message(message_sid: str) -> Dict[str, Any]:
    """DELETE /Messages/{Sid}.json - Delete a message record."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/Messages/{message_sid}.json"
    return client.request("DELETE", url)


def update_message(
    message_sid: str,
    *,
    body: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /Messages/{Sid}.json - Update/redact message body (where supported)."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/Messages/{message_sid}.json"
    data: Dict[str, Any] = {"Body": body}
    return client.request("POST", url, data=data)
