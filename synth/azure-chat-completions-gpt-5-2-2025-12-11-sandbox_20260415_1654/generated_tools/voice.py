from typing import Any, Dict, Optional, List

from .twilio_client import TwilioClient, accounts_base_url


def create_call(
    to: str,
    from_: str,
    *,
    url: Optional[str] = None,
    twiml: Optional[str] = None,
    method: Optional[str] = None,
    status_callback: Optional[str] = None,
    status_callback_event: Optional[List[str]] = None,
    status_callback_method: Optional[str] = None,
    timeout: Optional[int] = None,
    record: Optional[bool] = None,
    recording_channels: Optional[str] = None,
    send_digits: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /Calls.json - Initiate an outbound call.

    Provide either url (TwiML URL) or twiml (inline TwiML).
    """
    client = TwilioClient()
    endpoint = f"{accounts_base_url(client.account_sid)}/Calls.json"
    data: Dict[str, Any] = {
        "To": to,
        "From": from_,
        "Url": url,
        "Twiml": twiml,
        "Method": method,
        "StatusCallback": status_callback,
        "StatusCallbackEvent": status_callback_event,
        "StatusCallbackMethod": status_callback_method,
        "Timeout": timeout,
        "Record": record,
        "RecordingChannels": recording_channels,
        "SendDigits": send_digits,
    }
    return client.request("POST", endpoint, data=data)


def fetch_call(call_sid: str) -> Dict[str, Any]:
    """GET /Calls/{Sid}.json - Fetch a call."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/Calls/{call_sid}.json"
    return client.request("GET", url)


def list_calls(
    *,
    to: Optional[str] = None,
    from_: Optional[str] = None,
    status: Optional[str] = None,
    start_time_after: Optional[str] = None,
    start_time_before: Optional[str] = None,
    page_size: int = 50,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /Calls.json - List calls."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/Calls.json"
    params: Dict[str, Any] = {
        "To": to,
        "From": from_,
        "Status": status,
        "StartTime>": start_time_after,
        "StartTime<": start_time_before,
        "PageSize": page_size,
        "Page": page,
    }
    return client.request("GET", url, params=params)


def update_call(
    call_sid: str,
    *,
    url: Optional[str] = None,
    method: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /Calls/{Sid}.json - Redirect or end an in-progress call.

    status can be 'canceled' or 'completed' depending on call state.
    """
    client = TwilioClient()
    endpoint = f"{accounts_base_url(client.account_sid)}/Calls/{call_sid}.json"
    data: Dict[str, Any] = {"Url": url, "Method": method, "Status": status}
    return client.request("POST", endpoint, data=data)


def delete_call(call_sid: str) -> Dict[str, Any]:
    """DELETE /Calls/{Sid}.json - Delete a call record."""
    client = TwilioClient()
    url = f"{accounts_base_url(client.account_sid)}/Calls/{call_sid}.json"
    return client.request("DELETE", url)
