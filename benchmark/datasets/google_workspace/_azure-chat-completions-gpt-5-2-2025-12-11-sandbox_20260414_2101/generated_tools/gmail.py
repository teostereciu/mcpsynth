from typing import Any, Dict, List, Optional

from .http import request_json, rfc2822_message
from .server import mcp

GMAIL_BASE = "https://gmail.googleapis.com/gmail/v1/users"


@mcp.tool()
def gmail_get_profile(userId: str = "me") -> Dict[str, Any]:
    """Get the current user's Gmail profile."""
    url = f"{GMAIL_BASE}/{userId}/profile"
    return request_json("GET", url)


@mcp.tool()
def gmail_messages_list(
    userId: str = "me",
    labelIds: Optional[List[str]] = None,
    q: Optional[str] = None,
    maxResults: int = 10,
    pageToken: Optional[str] = None,
    includeSpamTrash: bool = False,
) -> Dict[str, Any]:
    """List messages in the user's mailbox."""
    url = f"{GMAIL_BASE}/{userId}/messages"
    params: Dict[str, Any] = {
        "maxResults": maxResults,
        "includeSpamTrash": includeSpamTrash,
    }
    if labelIds:
        params["labelIds"] = labelIds
    if q:
        params["q"] = q
    if pageToken:
        params["pageToken"] = pageToken
    return request_json("GET", url, params=params)


@mcp.tool()
def gmail_messages_get(
    userId: str = "me",
    id: str = "",
    format: str = "full",
    metadataHeaders: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Get a message by ID."""
    url = f"{GMAIL_BASE}/{userId}/messages/{id}"
    params: Dict[str, Any] = {"format": format}
    if metadataHeaders:
        params["metadataHeaders"] = metadataHeaders
    return request_json("GET", url, params=params)


@mcp.tool()
def gmail_labels_list(userId: str = "me") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/labels"
    return request_json("GET", url)


@mcp.tool()
def gmail_labels_get(userId: str = "me", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/labels/{id}"
    return request_json("GET", url)


@mcp.tool()
def gmail_labels_create(
    userId: str = "me",
    name: str = "",
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


@mcp.tool()
def gmail_labels_update(userId: str = "me", id: str = "", label: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/labels/{id}"
    return request_json("PUT", url, json_body=label or {})


@mcp.tool()
def gmail_labels_delete(userId: str = "me", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/labels/{id}"
    return request_json("DELETE", url)


@mcp.tool()
def gmail_drafts_list(userId: str = "me", maxResults: int = 10, pageToken: Optional[str] = None, q: Optional[str] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/drafts"
    params: Dict[str, Any] = {"maxResults": maxResults}
    if pageToken:
        params["pageToken"] = pageToken
    if q:
        params["q"] = q
    return request_json("GET", url, params=params)


@mcp.tool()
def gmail_drafts_get(userId: str = "me", id: str = "", format: str = "full") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/drafts/{id}"
    params = {"format": format}
    return request_json("GET", url, params=params)


@mcp.tool()
def gmail_drafts_create(
    userId: str = "me",
    to: Optional[str] = None,
    subject: Optional[str] = None,
    body: Optional[str] = None,
    raw: Optional[str] = None,
    threadId: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a draft. Provide either raw (base64url RFC2822) or to+subject+body."""
    url = f"{GMAIL_BASE}/{userId}/drafts"
    if raw is None:
        if to is None or subject is None or body is None:
            return {"error": "Provide raw or (to, subject, body)", "status": 400}
        raw = rfc2822_message(to, subject, body)
    msg: Dict[str, Any] = {"raw": raw}
    if threadId:
        msg["threadId"] = threadId
    return request_json("POST", url, json_body={"message": msg})


@mcp.tool()
def gmail_drafts_update(userId: str = "me", id: str = "", draft: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/drafts/{id}"
    return request_json("PUT", url, json_body=draft or {})


@mcp.tool()
def gmail_drafts_send(userId: str = "me", id: Optional[str] = None, draft: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/drafts/send"
    body: Dict[str, Any] = {}
    if id is not None:
        body["id"] = id
    if draft is not None:
        body["draft"] = draft
    return request_json("POST", url, json_body=body)


@mcp.tool()
def gmail_drafts_delete(userId: str = "me", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/drafts/{id}"
    return request_json("DELETE", url)


@mcp.tool()
def gmail_messages_send(
    userId: str = "me",
    to: Optional[str] = None,
    subject: Optional[str] = None,
    body: Optional[str] = None,
    raw: Optional[str] = None,
    threadId: Optional[str] = None,
) -> Dict[str, Any]:
    """Send a message. Provide either raw or to+subject+body."""
    url = f"{GMAIL_BASE}/{userId}/messages/send"
    if raw is None:
        if to is None or subject is None or body is None:
            return {"error": "Provide raw or (to, subject, body)", "status": 400}
        raw = rfc2822_message(to, subject, body)
    msg: Dict[str, Any] = {"raw": raw}
    if threadId:
        msg["threadId"] = threadId
    return request_json("POST", url, json_body=msg)


@mcp.tool()
def gmail_messages_modify(userId: str = "me", id: str = "", addLabelIds: Optional[List[str]] = None, removeLabelIds: Optional[List[str]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages/{id}/modify"
    body: Dict[str, Any] = {}
    if addLabelIds is not None:
        body["addLabelIds"] = addLabelIds
    if removeLabelIds is not None:
        body["removeLabelIds"] = removeLabelIds
    return request_json("POST", url, json_body=body)


@mcp.tool()
def gmail_messages_trash(userId: str = "me", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages/{id}/trash"
    return request_json("POST", url, json_body={})


@mcp.tool()
def gmail_messages_untrash(userId: str = "me", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages/{id}/untrash"
    return request_json("POST", url, json_body={})


@mcp.tool()
def gmail_messages_delete(userId: str = "me", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages/{id}"
    return request_json("DELETE", url)


@mcp.tool()
def gmail_messages_batchDelete(userId: str = "me", ids: Optional[List[str]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages/batchDelete"
    return request_json("POST", url, json_body={"ids": ids or []})


@mcp.tool()
def gmail_messages_batchModify(userId: str = "me", ids: Optional[List[str]] = None, addLabelIds: Optional[List[str]] = None, removeLabelIds: Optional[List[str]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages/batchModify"
    body: Dict[str, Any] = {"ids": ids or []}
    if addLabelIds is not None:
        body["addLabelIds"] = addLabelIds
    if removeLabelIds is not None:
        body["removeLabelIds"] = removeLabelIds
    return request_json("POST", url, json_body=body)


@mcp.tool()
def gmail_threads_list(userId: str = "me", labelIds: Optional[List[str]] = None, q: Optional[str] = None, maxResults: int = 10, pageToken: Optional[str] = None, includeSpamTrash: bool = False) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/threads"
    params: Dict[str, Any] = {"maxResults": maxResults, "includeSpamTrash": includeSpamTrash}
    if labelIds:
        params["labelIds"] = labelIds
    if q:
        params["q"] = q
    if pageToken:
        params["pageToken"] = pageToken
    return request_json("GET", url, params=params)


@mcp.tool()
def gmail_threads_get(userId: str = "me", id: str = "", format: str = "full", metadataHeaders: Optional[List[str]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/threads/{id}"
    params: Dict[str, Any] = {"format": format}
    if metadataHeaders:
        params["metadataHeaders"] = metadataHeaders
    return request_json("GET", url, params=params)


@mcp.tool()
def gmail_threads_modify(userId: str = "me", id: str = "", addLabelIds: Optional[List[str]] = None, removeLabelIds: Optional[List[str]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/threads/{id}/modify"
    body: Dict[str, Any] = {}
    if addLabelIds is not None:
        body["addLabelIds"] = addLabelIds
    if removeLabelIds is not None:
        body["removeLabelIds"] = removeLabelIds
    return request_json("POST", url, json_body=body)


@mcp.tool()
def gmail_threads_trash(userId: str = "me", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/threads/{id}/trash"
    return request_json("POST", url, json_body={})


@mcp.tool()
def gmail_threads_delete(userId: str = "me", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/threads/{id}"
    return request_json("DELETE", url)


@mcp.tool()
def gmail_history_list(userId: str = "me", startHistoryId: Optional[str] = None, historyTypes: Optional[List[str]] = None, labelId: Optional[str] = None, maxResults: int = 100, pageToken: Optional[str] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/history"
    params: Dict[str, Any] = {"maxResults": maxResults}
    if startHistoryId:
        params["startHistoryId"] = startHistoryId
    if historyTypes:
        params["historyTypes"] = historyTypes
    if labelId:
        params["labelId"] = labelId
    if pageToken:
        params["pageToken"] = pageToken
    return request_json("GET", url, params=params)


@mcp.tool()
def gmail_messages_attachments_get(userId: str = "me", messageId: str = "", id: str = "") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/messages/{messageId}/attachments/{id}"
    return request_json("GET", url)


@mcp.tool()
def gmail_settings_getAutoForwarding(userId: str = "me") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/settings/autoForwarding"
    return request_json("GET", url)


@mcp.tool()
def gmail_settings_getImap(userId: str = "me") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/settings/imap"
    return request_json("GET", url)


@mcp.tool()
def gmail_settings_getPop(userId: str = "me") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/settings/pop"
    return request_json("GET", url)


@mcp.tool()
def gmail_settings_getVacation(userId: str = "me") -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/settings/vacation"
    return request_json("GET", url)


@mcp.tool()
def gmail_settings_updateVacation(userId: str = "me", vacationSettings: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{GMAIL_BASE}/{userId}/settings/vacation"
    return request_json("PUT", url, json_body=vacationSettings or {})
