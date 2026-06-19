from typing import Any, Dict, List, Optional

from .common import client


def send_message(
    message_type: str,
    to: Any,
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
    anchor: Optional[str] = None,
    include_anchor: Optional[bool] = None,
    anchor_date: Optional[str] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    filter_spec: Optional[List[Dict[str, Any]]] = None,
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
            "include_anchor": include_anchor,
            "anchor_date": anchor_date,
            "num_before": num_before,
            "num_after": num_after,
            "filter_spec": filter_spec,
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


def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/messages/{message_id}/reactions",
        data={
            "emoji_name": emoji_name,
            "emoji_code": emoji_code,
            "reaction_type": reaction_type,
        },
    )


def remove_reaction(
    message_id: int,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "DELETE",
        f"/messages/{message_id}/reactions",
        data={
            "emoji_name": emoji_name,
            "emoji_code": emoji_code,
            "reaction_type": reaction_type,
        },
    )


def create_scheduled_message(
    message_type: str,
    to: Any,
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/scheduled_messages",
        data={
            "type": message_type,
            "to": to,
            "content": content,
            "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
            "topic": topic,
            "read_by_sender": read_by_sender,
        },
    )


def get_scheduled_messages() -> Dict[str, Any]:
    return client.request("GET", "/scheduled_messages")


def update_scheduled_message(
    scheduled_message_id: int,
    message_type: Optional[str] = None,
    to: Optional[Any] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    return client.request(
        "PATCH",
        f"/scheduled_messages/{scheduled_message_id}",
        data={
            "type": message_type,
            "to": to,
            "content": content,
            "topic": topic,
            "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
        },
    )
