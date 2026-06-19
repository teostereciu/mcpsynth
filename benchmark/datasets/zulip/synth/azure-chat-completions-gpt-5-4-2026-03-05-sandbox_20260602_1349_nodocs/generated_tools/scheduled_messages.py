from typing import Any, Dict, List, Optional

from generated_tools.common import client, json_dumps


def get_scheduled_messages() -> Dict[str, Any]:
    return client.request("GET", "/scheduled_messages")


def create_scheduled_message(type: str, to: List[str], content: str, scheduled_delivery_timestamp: int, topic: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "type": type,
        "to": json_dumps(to),
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        params["topic"] = topic
    return client.request("POST", "/scheduled_messages", params=params)


def update_scheduled_message(message_id: int, type: Optional[str] = None, to: Optional[List[str]] = None, content: Optional[str] = None, scheduled_delivery_timestamp: Optional[int] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if type is not None:
        params["type"] = type
    if to is not None:
        params["to"] = json_dumps(to)
    if content is not None:
        params["content"] = content
    if scheduled_delivery_timestamp is not None:
        params["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    if topic is not None:
        params["topic"] = topic
    return client.request("PATCH", f"/scheduled_messages/{message_id}", params=params)


def delete_scheduled_message(message_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/scheduled_messages/{message_id}")
