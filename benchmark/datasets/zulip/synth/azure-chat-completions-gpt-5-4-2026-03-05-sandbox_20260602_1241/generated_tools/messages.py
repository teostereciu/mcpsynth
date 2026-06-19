from typing import Any, Dict, List, Optional, Union

from generated_tools.common import client


def send_message(
    message_type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/messages",
        data={
            "type": message_type,
            "to": to,
            "content": content,
            "topic": topic,
            "queue_id": queue_id,
            "local_id": local_id,
            "read_by_sender": read_by_sender,
        },
    )


def get_messages(
    anchor: Optional[Union[str, int]] = "newest",
    num_before: Optional[int] = 100,
    num_after: Optional[int] = 0,
    narrow: Optional[List[Dict[str, Any]]] = None,
    include_anchor: Optional[bool] = None,
    anchor_date: Optional[str] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    message_ids: Optional[List[int]] = None,
    allow_empty_topic_name: Optional[bool] = None,
    use_first_unread_anchor: Optional[bool] = None,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/messages",
        params={
            "anchor": anchor,
            "num_before": num_before,
            "num_after": num_after,
            "narrow": narrow or [],
            "include_anchor": include_anchor,
            "anchor_date": anchor_date,
            "client_gravatar": client_gravatar,
            "apply_markdown": apply_markdown,
            "message_ids": message_ids,
            "allow_empty_topic_name": allow_empty_topic_name,
            "use_first_unread_anchor": use_first_unread_anchor,
        },
    )


def get_message(message_id: int, apply_markdown: Optional[bool] = None, allow_empty_topic_name: Optional[bool] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/messages/{message_id}",
        params={
            "apply_markdown": apply_markdown,
            "allow_empty_topic_name": allow_empty_topic_name,
        },
    )


def update_message(
    message_id: int,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    content: Optional[str] = None,
    prev_content_sha256: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> Dict[str, Any]:
    return client.request(
        "PATCH",
        f"/messages/{message_id}",
        data={
            "topic": topic,
            "propagate_mode": propagate_mode,
            "send_notification_to_old_thread": send_notification_to_old_thread,
            "send_notification_to_new_thread": send_notification_to_new_thread,
            "content": content,
            "prev_content_sha256": prev_content_sha256,
            "stream_id": stream_id,
        },
    )


def delete_message(message_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/messages/{message_id}")


def get_message_history(message_id: int, allow_empty_topic_name: Optional[bool] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/messages/{message_id}/history",
        params={"allow_empty_topic_name": allow_empty_topic_name},
    )


def add_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/messages/{message_id}/reactions",
        data={"emoji_name": emoji_name, "emoji_code": emoji_code, "reaction_type": reaction_type},
    )


def remove_reaction(message_id: int, emoji_name: Optional[str] = None, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    return client.request(
        "DELETE",
        f"/messages/{message_id}/reactions",
        data={"emoji_name": emoji_name, "emoji_code": emoji_code, "reaction_type": reaction_type},
    )


def render_message(content: str) -> Dict[str, Any]:
    return client.request("POST", "/messages/render", data={"content": content})


def check_messages_match_narrow(msg_ids: List[int], narrow: List[Dict[str, Any]]) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/messages/matches_narrow",
        params={"msg_ids": msg_ids, "narrow": narrow},
    )
