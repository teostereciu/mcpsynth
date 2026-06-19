"""Gmail API v1 tools."""

from __future__ import annotations

import base64
from email.message import EmailMessage
from typing import Any, Dict, List, Optional

from .http import request_json

GMAIL_BASE = "https://gmail.googleapis.com/gmail/v1/users"


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")


def gmail_get_profile(user_id: str = "me") -> Any:
    """GET /gmail/v1/users/{userId}/profile"""
    return request_json("GET", f"{GMAIL_BASE}/{user_id}/profile")


def gmail_messages_list(
    user_id: str = "me",
    *,
    label_ids: Optional[List[str]] = None,
    q: Optional[str] = None,
    max_results: int = 100,
    page_token: Optional[str] = None,
    include_spam_trash: bool = False,
) -> Any:
    """List messages."""
    params: Dict[str, Any] = {
        "maxResults": max_results,
        "includeSpamTrash": include_spam_trash,
    }
    if label_ids:
        params["labelIds"] = label_ids
    if q:
        params["q"] = q
    if page_token:
        params["pageToken"] = page_token
    return request_json("GET", f"{GMAIL_BASE}/{user_id}/messages", params=params)


def gmail_messages_get(
    user_id: str = "me",
    message_id: str = "",
    *,
    format: str = "full",
    metadata_headers: Optional[List[str]] = None,
) -> Any:
    """Get a message by id."""
    params: Dict[str, Any] = {"format": format}
    if metadata_headers:
        params["metadataHeaders"] = metadata_headers
    return request_json("GET", f"{GMAIL_BASE}/{user_id}/messages/{message_id}", params=params)


def gmail_messages_send(
    user_id: str = "me",
    *,
    raw: Optional[str] = None,
    to: Optional[str] = None,
    subject: Optional[str] = None,
    body: Optional[str] = None,
    cc: Optional[str] = None,
    bcc: Optional[str] = None,
    from_email: Optional[str] = None,
    thread_id: Optional[str] = None,
) -> Any:
    """Send an email.

    Provide either `raw` (base64url RFC2822) or (to, subject, body).
    """

    if raw is None:
        if not (to and subject is not None and body is not None):
            return {"error": "Provide raw or (to, subject, body)", "status": None}
        msg = EmailMessage()
        msg["To"] = to
        if cc:
            msg["Cc"] = cc
        if bcc:
            msg["Bcc"] = bcc
        if from_email:
            msg["From"] = from_email
        msg["Subject"] = subject
        msg.set_content(body)
        raw = _b64url(msg.as_bytes())

    payload: Dict[str, Any] = {"raw": raw}
    if thread_id:
        payload["threadId"] = thread_id
    return request_json("POST", f"{GMAIL_BASE}/{user_id}/messages/send", json=payload)


def gmail_drafts_create(
    user_id: str = "me",
    *,
    raw: Optional[str] = None,
    to: Optional[str] = None,
    subject: Optional[str] = None,
    body: Optional[str] = None,
    cc: Optional[str] = None,
    bcc: Optional[str] = None,
    from_email: Optional[str] = None,
) -> Any:
    """Create a draft."""

    if raw is None:
        if not (to and subject is not None and body is not None):
            return {"error": "Provide raw or (to, subject, body)", "status": None}
        msg = EmailMessage()
        msg["To"] = to
        if cc:
            msg["Cc"] = cc
        if bcc:
            msg["Bcc"] = bcc
        if from_email:
            msg["From"] = from_email
        msg["Subject"] = subject
        msg.set_content(body)
        raw = _b64url(msg.as_bytes())

    payload = {"message": {"raw": raw}}
    return request_json("POST", f"{GMAIL_BASE}/{user_id}/drafts", json=payload)


def gmail_labels_create(
    user_id: str = "me",
    *,
    name: str,
    label_list_visibility: str = "labelShow",
    message_list_visibility: str = "show",
) -> Any:
    """Create a label."""
    payload = {
        "name": name,
        "labelListVisibility": label_list_visibility,
        "messageListVisibility": message_list_visibility,
    }
    return request_json("POST", f"{GMAIL_BASE}/{user_id}/labels", json=payload)
