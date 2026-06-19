import json
from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient, dumps_narrow


def send_message(
    type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /messages"""
    data: Dict[str, Any] = {"type": type, "to": to, "content": content}
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = read_by_sender
    return ZulipClient().request("POST", "/messages", data=data)


def get_messages(
    anchor: Union[int, str] = "newest",
    num_before: int = 30,
    num_after: int = 0,
    narrow: Optional[List[Dict[str, Any]]] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    use_first_unread_anchor: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /messages"""
    params: Dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
    }
    if narrow is not None:
        params["narrow"] = dumps_narrow(narrow)
    if client_gravatar is not None:
        params["client_gravatar"] = json.dumps(client_gravatar)
    if apply_markdown is not None:
        params["apply_markdown"] = json.dumps(apply_markdown)
    if use_first_unread_anchor is not None:
        params["use_first_unread_anchor"] = json.dumps(use_first_unread_anchor)
    return ZulipClient().request("GET", "/messages", params=params)


def get_message(message_id: int) -> Dict[str, Any]:
    """GET /messages/{message_id}"""
    return ZulipClient().request("GET", f"/messages/{message_id}")


def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
) -> Dict[str, Any]:
    """PATCH /messages/{message_id}"""
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = json.dumps(send_notification_to_old_thread)
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = json.dumps(send_notification_to_new_thread)
    return ZulipClient().request("PATCH", f"/messages/{message_id}", data=data)


def delete_message(message_id: int) -> Dict[str, Any]:
    """DELETE /messages/{message_id}"""
    return ZulipClient().request("DELETE", f"/messages/{message_id}")


def render_message(content: str) -> Dict[str, Any]:
    """POST /messages/render"""
    return ZulipClient().request("POST", "/messages/render", data={"content": content})


def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /messages/{message_id}/reactions"""
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return ZulipClient().request("POST", f"/messages/{message_id}/reactions", data=data)


def remove_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /messages/{message_id}/reactions"""
    params: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    return ZulipClient().request("DELETE", f"/messages/{message_id}/reactions", params=params)


def update_message_flags(
    messages: List[int],
    op: str,
    flag: str,
) -> Dict[str, Any]:
    """POST /messages/flags"""
    data = {"messages": json.dumps(messages), "op": op, "flag": flag}
    return ZulipClient().request("POST", "/messages/flags", data=data)


def mark_all_as_read() -> Dict[str, Any]:
    """POST /mark_all_as_read"""
    return ZulipClient().request("POST", "/mark_all_as_read")


def mark_stream_as_read(stream_id: int) -> Dict[str, Any]:
    """POST /mark_stream_as_read"""
    return ZulipClient().request("POST", "/mark_stream_as_read", data={"stream_id": stream_id})


def mark_topic_as_read(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """POST /mark_topic_as_read"""
    return ZulipClient().request(
        "POST",
        "/mark_topic_as_read",
        data={"stream_id": stream_id, "topic_name": topic_name},
    )
