from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="chat_post_message")
def chat_post_message(
    channel: str,
    text: Optional[str] = None,
    blocks: Optional[List[Dict[str, Any]]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    thread_ts: Optional[str] = None,
    reply_broadcast: Optional[bool] = None,
    mrkdwn: Optional[bool] = None,
    unfurl_links: Optional[bool] = None,
    unfurl_media: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Sends a message to a channel (chat.postMessage)."""

    payload: Dict[str, Any] = {"channel": channel}
    if text is not None:
        payload["text"] = text
    if blocks is not None:
        payload["blocks"] = blocks
    if attachments is not None:
        payload["attachments"] = attachments
    if thread_ts is not None:
        payload["thread_ts"] = thread_ts
    if reply_broadcast is not None:
        payload["reply_broadcast"] = reply_broadcast
    if mrkdwn is not None:
        payload["mrkdwn"] = mrkdwn
    if unfurl_links is not None:
        payload["unfurl_links"] = unfurl_links
    if unfurl_media is not None:
        payload["unfurl_media"] = unfurl_media
    if metadata is not None:
        payload["metadata"] = metadata

    try:
        return slack_api_call("chat.postMessage", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="chat_update")
def chat_update(
    channel: str,
    ts: str,
    text: Optional[str] = None,
    blocks: Optional[List[Dict[str, Any]]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    as_user: Optional[bool] = None,
) -> Dict[str, Any]:
    """Updates a message (chat.update)."""

    payload: Dict[str, Any] = {"channel": channel, "ts": ts}
    if text is not None:
        payload["text"] = text
    if blocks is not None:
        payload["blocks"] = blocks
    if attachments is not None:
        payload["attachments"] = attachments
    if as_user is not None:
        payload["as_user"] = as_user

    try:
        return slack_api_call("chat.update", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="chat_delete")
def chat_delete(channel: str, ts: str, as_user: Optional[bool] = None) -> Dict[str, Any]:
    """Deletes a message (chat.delete)."""

    payload: Dict[str, Any] = {"channel": channel, "ts": ts}
    if as_user is not None:
        payload["as_user"] = as_user

    try:
        return slack_api_call("chat.delete", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="chat_get_permalink")
def chat_get_permalink(channel: str, message_ts: str) -> Dict[str, Any]:
    """Gets a permalink to a message (chat.getPermalink)."""

    try:
        return slack_api_call(
            "chat.getPermalink",
            http_method="GET",
            params={"channel": channel, "message_ts": message_ts},
        )
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="chat_schedule_message")
def chat_schedule_message(
    channel: str,
    post_at: int,
    text: Optional[str] = None,
    blocks: Optional[List[Dict[str, Any]]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    thread_ts: Optional[str] = None,
) -> Dict[str, Any]:
    """Schedules a message (chat.scheduleMessage)."""

    payload: Dict[str, Any] = {"channel": channel, "post_at": post_at}
    if text is not None:
        payload["text"] = text
    if blocks is not None:
        payload["blocks"] = blocks
    if attachments is not None:
        payload["attachments"] = attachments
    if thread_ts is not None:
        payload["thread_ts"] = thread_ts

    try:
        return slack_api_call("chat.scheduleMessage", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="chat_scheduled_messages_list")
def chat_scheduled_messages_list(
    channel: Optional[str] = None,
    latest: Optional[int] = None,
    oldest: Optional[int] = None,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
) -> Dict[str, Any]:
    """Lists scheduled messages (chat.scheduledMessages.list)."""

    payload: Dict[str, Any] = {}
    if channel is not None:
        payload["channel"] = channel
    if latest is not None:
        payload["latest"] = latest
    if oldest is not None:
        payload["oldest"] = oldest
    if limit is not None:
        payload["limit"] = limit
    if cursor is not None:
        payload["cursor"] = cursor

    try:
        return slack_api_call("chat.scheduledMessages.list", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="chat_delete_scheduled_message")
def chat_delete_scheduled_message(channel: str, scheduled_message_id: str) -> Dict[str, Any]:
    """Deletes a scheduled message (chat.deleteScheduledMessage)."""

    try:
        return slack_api_call(
            "chat.deleteScheduledMessage",
            http_method="POST",
            json={"channel": channel, "scheduled_message_id": scheduled_message_id},
        )
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
