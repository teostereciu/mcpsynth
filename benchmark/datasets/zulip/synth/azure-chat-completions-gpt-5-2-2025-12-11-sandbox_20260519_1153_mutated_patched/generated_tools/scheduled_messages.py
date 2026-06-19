from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient, _maybe_json_dumps


def get_scheduled_messages() -> Dict[str, Any]:
    """GET /scheduled_messages"""
    client = ZulipClient()
    return client.request("GET", "/scheduled_messages")


def create_scheduled_message(
    *,
    type: str,
    to: Union[int, List[int]],
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /scheduled_messages"""
    client = ZulipClient()
    data: Dict[str, Any] = {
        "type": type,
        "to": _maybe_json_dumps(to),
        "content": content,
        "scheduled_delivery_timestamp": str(scheduled_delivery_timestamp),
    }
    if topic is not None:
        data["topic"] = topic
    if read_by_sender is not None:
        data["read_by_sender"] = "true" if read_by_sender else "false"
    return client.request("POST", "/scheduled_messages", data=data)


def update_scheduled_message(
    *,
    scheduled_message_id: int,
    type: Optional[str] = None,
    to: Optional[Union[int, List[int]]] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    """PATCH /scheduled_messages/{scheduled_message_id}"""
    client = ZulipClient()
    data: Dict[str, Any] = {}
    if type is not None:
        data["type"] = type
    if to is not None:
        data["to"] = _maybe_json_dumps(to)
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = str(scheduled_delivery_timestamp)
    return client.request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


def delete_scheduled_message(*, scheduled_message_id: int) -> Dict[str, Any]:
    """DELETE /scheduled_messages/{scheduled_message_id}"""
    client = ZulipClient()
    return client.request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
