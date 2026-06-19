from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import request_json

GMAIL_BASE = "https://gmail.googleapis.com/gmail/v1/users"


def gmail_get_profile(userId: str = "me") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/profile"
    return request_json("GET", url)


def gmail_messages_list(
    userId: str = "me",
    *,
    labelIds: Optional[List[str]] = None,
    q: Optional[str] = None,
    maxResults: int = 10,
    pageToken: Optional[str] = None,
    includeSpamTrash: Optional[bool] = None,
) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages"
    params: Dict[str, Any] = {"maxResults": maxResults}
    if labelIds:
        params["labelIds"] = labelIds
    if q is not None:
        params["q"] = q
    if pageToken is not None:
        params["pageToken"] = pageToken
    if includeSpamTrash is not None:
        params["includeSpamTrash"] = includeSpamTrash
    return request_json("GET", url, params=params)


def gmail_messages_get(
    userId: str = "me",
    messageId: str = "",
    *,
    format: str = "full",
    metadataHeaders: Optional[List[str]] = None,
) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages/{messageId}"
    params: Dict[str, Any] = {"format": format}
    if metadataHeaders:
        params["metadataHeaders"] = metadataHeaders
    return request_json("GET", url, params=params)


def gmail_labels_create(
    userId: str = "me",
    *,
    name: str,
    labelListVisibility: Optional[str] = None,
    messageListVisibility: Optional[str] = None,
) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/labels"
    body: Dict[str, Any] = {"name": name}
    if labelListVisibility is not None:
        body["labelListVisibility"] = labelListVisibility
    if messageListVisibility is not None:
        body["messageListVisibility"] = messageListVisibility
    return request_json("POST", url, json_body=body)


def gmail_drafts_create(
    userId: str = "me",
    *,
    message: Dict[str, Any],
) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/drafts"
    body = {"message": message}
    return request_json("POST", url, json_body=body)
