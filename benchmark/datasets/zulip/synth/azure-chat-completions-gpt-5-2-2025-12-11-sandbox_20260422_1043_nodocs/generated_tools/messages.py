import json as _json
from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient


def send_message(
    type: str,
    to: Union[int, str, List[int], List[str]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """Send a message.

    type: "stream" or "private".
    to: stream id/name for stream messages; user ids/emails for private.
    """
    c = ZulipClient()
    data: Dict[str, Any] = {"type": type, "to": _json.dumps(to), "content": content}
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = "true" if read_by_sender else "false"
    return c.request("POST", "/messages", data=data)


def get_messages(
    anchor: Union[int, str] = "newest",
    num_before: int = 30,
    num_after: int = 0,
    narrow: Optional[List[Dict[str, Any]]] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    use_first_unread_anchor: Optional[bool] = None,
) -> Dict[str, Any]:
    """Fetch message history."""
    c = ZulipClient()
    params: Dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
    }
    if narrow is not None:
        params["narrow"] = _json.dumps(narrow)
    if client_gravatar is not None:
        params["client_gravatar"] = "true" if client_gravatar else "false"
    if apply_markdown is not None:
        params["apply_markdown"] = "true" if apply_markdown else "false"
    if use_first_unread_anchor is not None:
        params["use_first_unread_anchor"] = "true" if use_first_unread_anchor else "false"
    return c.request("GET", "/messages", params=params)


def get_message(message_id: int) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("GET", f"/messages/{message_id}")


def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
) -> Dict[str, Any]:
    c = ZulipClient()
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = "true" if send_notification_to_old_thread else "false"
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = "true" if send_notification_to_new_thread else "false"
    return c.request("PATCH", f"/messages/{message_id}", data=data)


def delete_message(message_id: int) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("DELETE", f"/messages/{message_id}")


def add_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: str = "unicode_emoji") -> Dict[str, Any]:
    c = ZulipClient()
    data: Dict[str, Any] = {"emoji_name": emoji_name, "reaction_type": reaction_type}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    return c.request("POST", f"/messages/{message_id}/reactions", data=data)


def remove_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: str = "unicode_emoji") -> Dict[str, Any]:
    c = ZulipClient()
    params: Dict[str, Any] = {"emoji_name": emoji_name, "reaction_type": reaction_type}
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    return c.request("DELETE", f"/messages/{message_id}/reactions", params=params)


def update_message_flags(messages: List[int], op: str, flag: str) -> Dict[str, Any]:
    c = ZulipClient()
    data = {"messages": _json.dumps(messages), "op": op, "flag": flag}
    return c.request("POST", "/messages/flags", data=data)


def render_message(content: str) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("POST", "/messages/render", data={"content": content})
