from typing import Any, Dict, Optional

from .http import request_json

GMAIL_BASE = "https://gmail.googleapis.com/gmail/v1/users/{userId}"


def gmail_messages_list(userId: str = "me", *, maxResults: Optional[int] = None, pageToken: Optional[str] = None, q: Optional[str] = None, labelIds: Optional[list[str]] = None, includeSpamTrash: Optional[bool] = None) -> Any:
    url = GMAIL_BASE.format(userId=userId) + "/messages"
    params: Dict[str, Any] = {}
    if maxResults is not None:
        params["maxResults"] = maxResults
    if pageToken is not None:
        params["pageToken"] = pageToken
    if q is not None:
        params["q"] = q
    if labelIds is not None:
        params["labelIds"] = labelIds
    if includeSpamTrash is not None:
        params["includeSpamTrash"] = includeSpamTrash
    return request_json("GET", url, params=params)


def gmail_messages_get(userId: str = "me", *, id: str, format: Optional[str] = None, metadataHeaders: Optional[list[str]] = None) -> Any:
    url = GMAIL_BASE.format(userId=userId) + f"/messages/{id}"
    params: Dict[str, Any] = {}
    if format is not None:
        params["format"] = format
    if metadataHeaders is not None:
        params["metadataHeaders"] = metadataHeaders
    return request_json("GET", url, params=params)
