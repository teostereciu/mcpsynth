from __future__ import annotations

from typing import Any, Optional

from zulip_client import ZulipClient


def send_message(
    client: ZulipClient,
    *,
    type: str,
    content: str,
    to: Any,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
) -> dict:
    data: dict[str, Any] = {"type": type, "content": content, "to": to}
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    return client.request("POST", "/messages", data=data)


def get_messages(
    client: ZulipClient,
    *,
    anchor: Any = "newest",
    num_before: int = 30,
    num_after: int = 0,
    narrow: Optional[Any] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    use_first_unread_anchor: Optional[bool] = None,
) -> dict:
    params: dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
    }
    if narrow is not None:
        params["narrow"] = narrow
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if apply_markdown is not None:
        params["apply_markdown"] = apply_markdown
    if use_first_unread_anchor is not None:
        params["use_first_unread_anchor"] = use_first_unread_anchor
    return client.request("GET", "/messages", params=params)


def update_message(
    client: ZulipClient,
    *,
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
) -> dict:
    data: dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = send_notification_to_old_thread
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = send_notification_to_new_thread
    return client.request("PATCH", f"/messages/{message_id}", data=data)


def delete_message(client: ZulipClient, *, message_id: int) -> dict:
    return client.request("DELETE", f"/messages/{message_id}")


def add_reaction(
    client: ZulipClient,
    *,
    message_id: int,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> dict:
    data: dict[str, Any] = {}
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return client.request("POST", f"/messages/{message_id}/reactions", data=data)


def remove_reaction(
    client: ZulipClient,
    *,
    message_id: int,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> dict:
    params: dict[str, Any] = {}
    if emoji_name is not None:
        params["emoji_name"] = emoji_name
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    return client.request("DELETE", f"/messages/{message_id}/reactions", params=params)


def update_message_flags(
    client: ZulipClient,
    *,
    messages: list[int],
    op: str,
    flag: str,
) -> dict:
    data = {"messages": messages, "op": op, "flag": flag}
    return client.request("POST", "/messages/flags", data=data)
