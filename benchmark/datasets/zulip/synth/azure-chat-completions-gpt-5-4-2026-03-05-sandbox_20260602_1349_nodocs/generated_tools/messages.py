from typing import Any, Dict, List, Optional

from generated_tools.common import client, json_dumps


def send_message(
    type: str,
    content: str,
    to: Optional[List[str]] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"type": type, "content": content}
    if to is not None:
        params["to"] = json_dumps(to)
    if topic is not None:
        params["topic"] = topic
    return client.request("POST", "/messages", params=params)


def get_messages(
    anchor: str = "newest",
    num_before: int = 20,
    num_after: int = 0,
    narrow: Optional[List[Dict[str, Any]]] = None,
    client_gravatar: bool = False,
    apply_markdown: bool = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "client_gravatar": str(client_gravatar).lower(),
        "apply_markdown": str(apply_markdown).lower(),
    }
    if narrow is not None:
        params["narrow"] = json_dumps(narrow)
    return client.request("GET", "/messages", params=params)


def get_message(message_id: int) -> Dict[str, Any]:
    return client.request("GET", f"/messages/{message_id}")


def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    stream_id: Optional[int] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if content is not None:
        params["content"] = content
    if topic is not None:
        params["topic"] = topic
    if stream_id is not None:
        params["stream_id"] = stream_id
    if propagate_mode is not None:
        params["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        params["send_notification_to_old_thread"] = str(send_notification_to_old_thread).lower()
    if send_notification_to_new_thread is not None:
        params["send_notification_to_new_thread"] = str(send_notification_to_new_thread).lower()
    return client.request("PATCH", f"/messages/{message_id}", params=params)


def delete_message(message_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/messages/{message_id}")


def mark_stream_topic_as_read(stream_id: int, topic_name: str) -> Dict[str, Any]:
    params = {"stream_id": stream_id, "topic_name": topic_name}
    return client.request("POST", "/mark_topic_as_read", params=params)


def add_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: str = "unicode_emoji") -> Dict[str, Any]:
    params: Dict[str, Any] = {"emoji_name": emoji_name, "reaction_type": reaction_type}
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    return client.request("POST", f"/messages/{message_id}/reactions", params=params)


def remove_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: str = "unicode_emoji") -> Dict[str, Any]:
    params: Dict[str, Any] = {"emoji_name": emoji_name, "reaction_type": reaction_type}
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    return client.request("DELETE", f"/messages/{message_id}/reactions", params=params)


def update_message_flags(messages: List[int], op: str, flag: str) -> Dict[str, Any]:
    params = {"messages": json_dumps(messages), "op": op, "flag": flag}
    return client.request("POST", "/messages/flags", params=params)


def get_message_history(message_id: int) -> Dict[str, Any]:
    return client.request("GET", f"/messages/{message_id}/history")
