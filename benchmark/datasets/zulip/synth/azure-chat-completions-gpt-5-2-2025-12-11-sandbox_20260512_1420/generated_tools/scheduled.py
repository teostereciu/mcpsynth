import json
from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient


def get_scheduled_messages() -> Dict[str, Any]:
    """GET /scheduled_messages"""
    return ZulipClient().request("GET", "/scheduled_messages")


def create_scheduled_message(
    type: str,
    to: Union[int, List[int]],
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /scheduled_messages"""
    data: Dict[str, Any] = {
        "type": type,
        "to": json.dumps(to) if isinstance(to, list) else to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        data["topic"] = topic
    if read_by_sender is not None:
        data["read_by_sender"] = json.dumps(read_by_sender)
    return ZulipClient().request("POST", "/scheduled_messages", data=data)


def update_scheduled_message(
    scheduled_message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    """PATCH /scheduled_messages/{scheduled_message_id}"""
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    return ZulipClient().request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """DELETE /scheduled_messages/{scheduled_message_id}"""
    return ZulipClient().request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
