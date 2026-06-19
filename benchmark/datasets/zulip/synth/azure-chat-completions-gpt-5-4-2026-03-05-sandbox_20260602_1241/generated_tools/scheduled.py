from typing import Any, Dict, List, Optional, Union

from generated_tools.common import client


def get_scheduled_messages() -> Dict[str, Any]:
    return client.request("GET", "/scheduled_messages")


def create_scheduled_message(
    message_type: str,
    to: Union[int, List[int]],
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
            "topic": topic,
            "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
            "read_by_sender": read_by_sender,
        },
    )


def update_scheduled_message(
    scheduled_message_id: int,
    message_type: Optional[str] = None,
    to: Optional[Union[int, List[int]]] = None,
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


def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
