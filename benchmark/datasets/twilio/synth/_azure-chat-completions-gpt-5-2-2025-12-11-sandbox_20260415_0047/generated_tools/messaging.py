"""Twilio Messaging API tools (Messages, Media, Feedback, Services).

Docs:
- Messages: /2010-04-01/Accounts/{AccountSid}/Messages.json
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import core_delete, core_get, core_post


def messages_create(
    *,
    to: str,
    body: Optional[str] = None,
    from_: Optional[str] = None,
    messaging_service_sid: Optional[str] = None,
    media_url: Optional[str] = None,
    status_callback: Optional[str] = None,
) -> Dict[str, Any]:
    """Send an SMS/MMS message.

    Args:
        to: Recipient E.164 or channel address.
        body: Message body.
        from_: Sender E.164/channel address. Required if messaging_service_sid not provided.
        messaging_service_sid: Messaging Service SID (MG...).
        media_url: Optional media URL for MMS.
        status_callback: Optional webhook URL.
    """
    data: Dict[str, Any] = {"To": to}
    if body is not None:
        data["Body"] = body
    if from_ is not None:
        data["From"] = from_
    if messaging_service_sid is not None:
        data["MessagingServiceSid"] = messaging_service_sid
    if media_url is not None:
        data["MediaUrl"] = media_url
    if status_callback is not None:
        data["StatusCallback"] = status_callback
    return core_post("/Messages.json", data=data)


def messages_fetch(*, message_sid: str) -> Dict[str, Any]:
    """Fetch a message by SID (SM...)."""
    return core_get(f"/Messages/{message_sid}.json")


def messages_list(
    *,
    page_size: int = 50,
    to: Optional[str] = None,
    from_: Optional[str] = None,
    date_sent: Optional[str] = None,
) -> Dict[str, Any]:
    """List messages.

    Twilio uses PageSize and supports filters like To, From, DateSent.
    """
    params: Dict[str, Any] = {"PageSize": page_size}
    if to is not None:
        params["To"] = to
    if from_ is not None:
        params["From"] = from_
    if date_sent is not None:
        params["DateSent"] = date_sent
    return core_get("/Messages.json", params=params)


def messages_update(
    *,
    message_sid: str,
    body: Optional[str] = None,
) -> Dict[str, Any]:
    """Update/redact a message (limited support)."""
    data: Dict[str, Any] = {}
    if body is not None:
        data["Body"] = body
    return core_post(f"/Messages/{message_sid}.json", data=data)


def messages_delete(*, message_sid: str) -> Dict[str, Any]:
    """Delete a message by SID."""
    return core_delete(f"/Messages/{message_sid}.json")
