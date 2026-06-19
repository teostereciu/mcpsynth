from typing import Any, Dict, List, Optional, Union

from .http_client import ZulipClient, dumps_if_needed


def get_scheduled_messages() -> Dict[str, Any]:
    """GET /scheduled_messages

    Doc: docs/api_get-scheduled-messages.md
    """
    client = ZulipClient()
    return client.request("GET", "/scheduled_messages")


def create_scheduled_message(*, type: str, to: Union[str, int, List[Union[str, int]]], content: str, scheduled_delivery_timestamp: int, topic: Optional[str] = None) -> Dict[str, Any]:
    """POST /scheduled_messages

    Doc: docs/api_create-scheduled-message.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {
        "type": type,
        "to": dumps_if_needed(to),
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        data["topic"] = topic
    return client.request("POST", "/scheduled_messages", data=data)


def update_scheduled_message(*, scheduled_message_id: int, type: Optional[str] = None, to: Optional[Union[str, int, List[Union[str, int]]]] = None, content: Optional[str] = None, scheduled_delivery_timestamp: Optional[int] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """PATCH /scheduled_messages/{scheduled_message_id}

    Doc: docs/api_update-scheduled-message.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {}
    if type is not None:
        data["type"] = type
    if to is not None:
        data["to"] = dumps_if_needed(to)
    if content is not None:
        data["content"] = content
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    if topic is not None:
        data["topic"] = topic
    return client.request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


def delete_scheduled_message(*, scheduled_message_id: int) -> Dict[str, Any]:
    """DELETE /scheduled_messages/{scheduled_message_id}

    Doc: docs/api_delete-scheduled-message.md
    """
    client = ZulipClient()
    return client.request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
