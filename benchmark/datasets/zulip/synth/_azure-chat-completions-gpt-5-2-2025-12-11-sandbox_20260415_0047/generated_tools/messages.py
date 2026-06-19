"""Message-related Zulip tools."""

from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional, Sequence, Union

from .http import zulip_request


JsonDict = Dict[str, Any]


def send_message(
    *,
    type: str,
    to: Union[str, int, Sequence[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> JsonDict:
    """POST /messages

    Send a channel/stream message or a direct message.

    Args:
        type: One of "direct", "private", "stream", "channel".
        to: For channel messages, channel name or ID. For direct messages, list of user IDs or emails.
        content: Message content.
        topic: Topic for channel messages.
    """
    data: Dict[str, Any] = {
        "type": type,
        "to": to,
        "content": content,
        "topic": topic,
        "queue_id": queue_id,
        "local_id": local_id,
        "read_by_sender": read_by_sender,
    }
    return zulip_request("POST", "/messages", data=data)


def update_message(
    *,
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    stream_id: Optional[int] = None,
    prev_content_sha256: Optional[str] = None,
) -> JsonDict:
    """PATCH /messages/{message_id}

    Edit message content and/or topic.
    """
    data: Dict[str, Any] = {
        "content": content,
        "topic": topic,
        "propagate_mode": propagate_mode,
        "send_notification_to_old_thread": send_notification_to_old_thread,
        "send_notification_to_new_thread": send_notification_to_new_thread,
        "stream_id": stream_id,
        "prev_content_sha256": prev_content_sha256,
    }
    return zulip_request("PATCH", f"/messages/{message_id}", data=data)


def delete_message(*, message_id: int) -> JsonDict:
    """DELETE /messages/{message_id}"""
    return zulip_request("DELETE", f"/messages/{message_id}")


def get_message(*, message_id: int, apply_markdown: Optional[bool] = None) -> JsonDict:
    """GET /messages/{message_id}"""
    params: Dict[str, Any] = {"apply_markdown": apply_markdown}
    return zulip_request("GET", f"/messages/{message_id}", params=params)


def get_messages(
    *,
    anchor: Union[int, str] = "newest",
    num_before: int = 50,
    num_after: int = 0,
    narrow: Optional[List[Mapping[str, Any]]] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
) -> JsonDict:
    """GET /messages

    Fetch messages with optional narrow.
    """
    params: Dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "narrow": narrow,
        "client_gravatar": client_gravatar,
        "apply_markdown": apply_markdown,
    }
    return zulip_request("GET", "/messages", params=params)


def get_message_history(*, message_id: int) -> JsonDict:
    """GET /messages/{message_id}/history"""
    return zulip_request("GET", f"/messages/{message_id}/history")


def render_message(*, content: str) -> JsonDict:
    """POST /messages/render"""
    return zulip_request("POST", "/messages/render", data={"content": content})


def check_messages_match_narrow(*, msg_ids: Sequence[int], narrow: List[Mapping[str, Any]]) -> JsonDict:
    """GET /messages/matches_narrow"""
    params: Dict[str, Any] = {"msg_ids": list(msg_ids), "narrow": narrow}
    return zulip_request("GET", "/messages/matches_narrow", params=params)


def update_message_flags(*, messages: Sequence[int], op: str, flag: str) -> JsonDict:
    """POST /messages/flags

    op: "add" or "remove".
    flag: e.g. "read", "starred".
    """
    data: Dict[str, Any] = {"messages": list(messages), "op": op, "flag": flag}
    return zulip_request("POST", "/messages/flags", data=data)


def update_message_flags_for_narrow(*, narrow: List[Mapping[str, Any]], op: str, flag: str) -> JsonDict:
    """POST /messages/flags/narrow"""
    data: Dict[str, Any] = {"narrow": narrow, "op": op, "flag": flag}
    return zulip_request("POST", "/messages/flags/narrow", data=data)


def mark_all_as_read() -> JsonDict:
    """POST /mark_all_as_read"""
    return zulip_request("POST", "/mark_all_as_read")


def mark_stream_as_read(*, stream_id: int) -> JsonDict:
    """POST /mark_stream_as_read"""
    return zulip_request("POST", "/mark_stream_as_read", data={"stream_id": stream_id})


def mark_topic_as_read(*, stream_id: int, topic_name: str) -> JsonDict:
    """POST /mark_topic_as_read"""
    return zulip_request("POST", "/mark_topic_as_read", data={"stream_id": stream_id, "topic_name": topic_name})


def get_read_receipts(*, message_id: int) -> JsonDict:
    """GET /messages/{message_id}/read_receipts"""
    return zulip_request("GET", f"/messages/{message_id}/read_receipts")


def report_message(*, message_id: int, reason: str) -> JsonDict:
    """POST /messages/{message_id}/report"""
    return zulip_request("POST", f"/messages/{message_id}/report", data={"reason": reason})
