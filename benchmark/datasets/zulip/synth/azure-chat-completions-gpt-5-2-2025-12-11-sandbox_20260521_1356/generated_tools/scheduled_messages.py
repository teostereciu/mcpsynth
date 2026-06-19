from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient, _maybe_json_dumps


def get_scheduled_messages(client: ZulipClient) -> Dict[str, Any]:
    return client.request("GET", "/scheduled_messages")


def create_scheduled_message(
    client: ZulipClient,
    type: str,
    to: Union[int, List[int]],
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "type": type,
        "to": _maybe_json_dumps(to),
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        params["topic"] = topic
    if read_by_sender is not None:
        params["read_by_sender"] = "true" if read_by_sender else "false"
    return client.request("POST", "/scheduled_messages", params)


def update_scheduled_message(
    client: ZulipClient,
    scheduled_message_id: int,
    type: Optional[str] = None,
    to: Optional[Union[int, List[int]]] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if type is not None:
        params["type"] = type
    if to is not None:
        params["to"] = _maybe_json_dumps(to)
    if content is not None:
        params["content"] = content
    if topic is not None:
        params["topic"] = topic
    if scheduled_delivery_timestamp is not None:
        params["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    return client.request("PATCH", f"/scheduled_messages/{scheduled_message_id}", params)


def delete_scheduled_message(client: ZulipClient, scheduled_message_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
