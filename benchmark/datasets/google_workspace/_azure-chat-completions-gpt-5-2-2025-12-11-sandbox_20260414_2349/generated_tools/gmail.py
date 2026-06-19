import base64
from email.message import EmailMessage
from typing import Any, Dict, List, Optional

from .http import request_json, request_bytes

GMAIL_BASE = "https://gmail.googleapis.com/gmail/v1/users"


def gmail_get_profile(userId: str = "me") -> Any:
    """GET /gmail/v1/users/{userId}/profile"""
    return request_json("GET", f"{GMAIL_BASE}/{userId}/profile")


def gmail_messages_list(
    userId: str = "me",
    *,
    labelIds: Optional[List[str]] = None,
    q: Optional[str] = None,
    maxResults: int = 100,
    pageToken: Optional[str] = None,
    includeSpamTrash: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {"maxResults": maxResults}
    if labelIds:
        params["labelIds"] = labelIds
    if q is not None:
        params["q"] = q
    if pageToken is not None:
        params["pageToken"] = pageToken
    if includeSpamTrash is not None:
        params["includeSpamTrash"] = includeSpamTrash
    return request_json("GET", f"{GMAIL_BASE}/{userId}/messages", params=params)


def gmail_messages_get(
    userId: str = "me",
    id: str = "",
    *,
    format: str = "full",
    metadataHeaders: Optional[List[str]] = None,
) -> Any:
    params: Dict[str, Any] = {"format": format}
    if metadataHeaders:
        params["metadataHeaders"] = metadataHeaders
    return request_json("GET", f"{GMAIL_BASE}/{userId}/messages/{id}", params=params)


def gmail_messages_send(
    userId: str = "me",
    *,
    to: str,
    subject: str,
    body: str,
    cc: Optional[str] = None,
    bcc: Optional[str] = None,
    threadId: Optional[str] = None,
) -> Any:
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    if cc:
        msg["Cc"] = cc
    if bcc:
        msg["Bcc"] = bcc
    msg.set_content(body)
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    payload: Dict[str, Any] = {"raw": raw}
    if threadId:
        payload["threadId"] = threadId
    return request_json("POST", f"{GMAIL_BASE}/{userId}/messages/send", json_body=payload)


def gmail_messages_modify(
    userId: str = "me",
    id: str = "",
    *,
    addLabelIds: Optional[List[str]] = None,
    removeLabelIds: Optional[List[str]] = None,
) -> Any:
    body: Dict[str, Any] = {}
    if addLabelIds is not None:
        body["addLabelIds"] = addLabelIds
    if removeLabelIds is not None:
        body["removeLabelIds"] = removeLabelIds
    return request_json("POST", f"{GMAIL_BASE}/{userId}/messages/{id}/modify", json_body=body)


def gmail_messages_trash(userId: str = "me", id: str = "") -> Any:
    return request_json("POST", f"{GMAIL_BASE}/{userId}/messages/{id}/trash")


def gmail_messages_untrash(userId: str = "me", id: str = "") -> Any:
    return request_json("POST", f"{GMAIL_BASE}/{userId}/messages/{id}/untrash")


def gmail_messages_delete(userId: str = "me", id: str = "") -> Any:
    return request_json("DELETE", f"{GMAIL_BASE}/{userId}/messages/{id}")


def gmail_messages_batchDelete(userId: str = "me", *, ids: List[str]) -> Any:
    return request_json("POST", f"{GMAIL_BASE}/{userId}/messages/batchDelete", json_body={"ids": ids})


def gmail_messages_batchModify(
    userId: str = "me", *, ids: List[str], addLabelIds: Optional[List[str]] = None, removeLabelIds: Optional[List[str]] = None
) -> Any:
    body: Dict[str, Any] = {"ids": ids}
    if addLabelIds is not None:
        body["addLabelIds"] = addLabelIds
    if removeLabelIds is not None:
        body["removeLabelIds"] = removeLabelIds
    return request_json("POST", f"{GMAIL_BASE}/{userId}/messages/batchModify", json_body=body)


def gmail_messages_insert(userId: str = "me", *, raw_rfc2822_base64url: str, internalDateSource: Optional[str] = None) -> Any:
    params = {}
    if internalDateSource:
        params["internalDateSource"] = internalDateSource
    return request_json("POST", f"{GMAIL_BASE}/{userId}/messages/insert", params=params, json_body={"raw": raw_rfc2822_base64url})


def gmail_messages_attachments_get(userId: str = "me", messageId: str = "", id: str = "") -> Any:
    return request_json("GET", f"{GMAIL_BASE}/{userId}/messages/{messageId}/attachments/{id}")


def gmail_threads_list(userId: str = "me", *, labelIds: Optional[List[str]] = None, q: Optional[str] = None, maxResults: int = 100, pageToken: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"maxResults": maxResults}
    if labelIds:
        params["labelIds"] = labelIds
    if q is not None:
        params["q"] = q
    if pageToken is not None:
        params["pageToken"] = pageToken
    return request_json("GET", f"{GMAIL_BASE}/{userId}/threads", params=params)


def gmail_threads_get(userId: str = "me", id: str = "", *, format: str = "full", metadataHeaders: Optional[List[str]] = None) -> Any:
    params: Dict[str, Any] = {"format": format}
    if metadataHeaders:
        params["metadataHeaders"] = metadataHeaders
    return request_json("GET", f"{GMAIL_BASE}/{userId}/threads/{id}", params=params)


def gmail_threads_modify(userId: str = "me", id: str = "", *, addLabelIds: Optional[List[str]] = None, removeLabelIds: Optional[List[str]] = None) -> Any:
    body: Dict[str, Any] = {}
    if addLabelIds is not None:
        body["addLabelIds"] = addLabelIds
    if removeLabelIds is not None:
        body["removeLabelIds"] = removeLabelIds
    return request_json("POST", f"{GMAIL_BASE}/{userId}/threads/{id}/modify", json_body=body)


def gmail_threads_trash(userId: str = "me", id: str = "") -> Any:
    return request_json("POST", f"{GMAIL_BASE}/{userId}/threads/{id}/trash")


def gmail_threads_delete(userId: str = "me", id: str = "") -> Any:
    return request_json("DELETE", f"{GMAIL_BASE}/{userId}/threads/{id}")


def gmail_labels_list(userId: str = "me") -> Any:
    return request_json("GET", f"{GMAIL_BASE}/{userId}/labels")


def gmail_labels_get(userId: str = "me", id: str = "") -> Any:
    return request_json("GET", f"{GMAIL_BASE}/{userId}/labels/{id}")


def gmail_labels_create(
    userId: str = "me",
    *,
    name: str,
    labelListVisibility: Optional[str] = None,
    messageListVisibility: Optional[str] = None,
) -> Any:
    body: Dict[str, Any] = {"name": name}
    if labelListVisibility is not None:
        body["labelListVisibility"] = labelListVisibility
    if messageListVisibility is not None:
        body["messageListVisibility"] = messageListVisibility
    return request_json("POST", f"{GMAIL_BASE}/{userId}/labels", json_body=body)


def gmail_labels_update(userId: str = "me", id: str = "", *, body: Dict[str, Any]) -> Any:
    return request_json("PUT", f"{GMAIL_BASE}/{userId}/labels/{id}", json_body=body)


def gmail_labels_delete(userId: str = "me", id: str = "") -> Any:
    return request_json("DELETE", f"{GMAIL_BASE}/{userId}/labels/{id}")


def gmail_drafts_list(userId: str = "me", *, maxResults: int = 100, pageToken: Optional[str] = None, q: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"maxResults": maxResults}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if q is not None:
        params["q"] = q
    return request_json("GET", f"{GMAIL_BASE}/{userId}/drafts", params=params)


def gmail_drafts_get(userId: str = "me", id: str = "", *, format: str = "full") -> Any:
    params = {"format": format}
    return request_json("GET", f"{GMAIL_BASE}/{userId}/drafts/{id}", params=params)


def gmail_drafts_create(userId: str = "me", *, to: str, subject: str, body: str, cc: Optional[str] = None, bcc: Optional[str] = None) -> Any:
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    if cc:
        msg["Cc"] = cc
    if bcc:
        msg["Bcc"] = bcc
    msg.set_content(body)
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    return request_json("POST", f"{GMAIL_BASE}/{userId}/drafts", json_body={"message": {"raw": raw}})


def gmail_drafts_update(userId: str = "me", id: str = "", *, to: str, subject: str, body: str, cc: Optional[str] = None, bcc: Optional[str] = None) -> Any:
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    if cc:
        msg["Cc"] = cc
    if bcc:
        msg["Bcc"] = bcc
    msg.set_content(body)
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    return request_json("PUT", f"{GMAIL_BASE}/{userId}/drafts/{id}", json_body={"message": {"raw": raw}})


def gmail_drafts_send(userId: str = "me", id: str = "") -> Any:
    return request_json("POST", f"{GMAIL_BASE}/{userId}/drafts/send", json_body={"id": id})


def gmail_drafts_delete(userId: str = "me", id: str = "") -> Any:
    return request_json("DELETE", f"{GMAIL_BASE}/{userId}/drafts/{id}")


def gmail_history_list(userId: str = "me", *, startHistoryId: str, historyTypes: Optional[List[str]] = None, labelId: Optional[str] = None, maxResults: int = 100, pageToken: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"startHistoryId": startHistoryId, "maxResults": maxResults}
    if historyTypes:
        params["historyTypes"] = historyTypes
    if labelId is not None:
        params["labelId"] = labelId
    if pageToken is not None:
        params["pageToken"] = pageToken
    return request_json("GET", f"{GMAIL_BASE}/{userId}/history", params=params)


def gmail_settings_getAutoForwarding(userId: str = "me") -> Any:
    return request_json("GET", f"{GMAIL_BASE}/{userId}/settings/autoForwarding")


def gmail_settings_getImap(userId: str = "me") -> Any:
    return request_json("GET", f"{GMAIL_BASE}/{userId}/settings/imap")


def gmail_settings_getPop(userId: str = "me") -> Any:
    return request_json("GET", f"{GMAIL_BASE}/{userId}/settings/pop")


def gmail_settings_getVacation(userId: str = "me") -> Any:
    return request_json("GET", f"{GMAIL_BASE}/{userId}/settings/vacation")


def gmail_settings_updateVacation(userId: str = "me", *, body: Dict[str, Any]) -> Any:
    return request_json("PUT", f"{GMAIL_BASE}/{userId}/settings/vacation", json_body=body)
