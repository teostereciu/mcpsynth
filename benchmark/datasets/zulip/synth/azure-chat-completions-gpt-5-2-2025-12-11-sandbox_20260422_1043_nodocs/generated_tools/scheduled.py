import json as _json
from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient


def get_scheduled_messages() -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("GET", "/scheduled_messages")


def schedule_message(
    type: str,
    to: Union[int, str, List[int], List[str]],
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    c = ZulipClient()
    data: Dict[str, Any] = {
        "type": type,
        "to": _json.dumps(to),
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        data["topic"] = topic
    return c.request("POST", "/scheduled_messages", data=data)


def update_scheduled_message(scheduled_message_id: int, scheduled_delivery_timestamp: int) -> Dict[str, Any]:
    c = ZulipClient()
    data = {"scheduled_delivery_timestamp": scheduled_delivery_timestamp}
    return c.request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
