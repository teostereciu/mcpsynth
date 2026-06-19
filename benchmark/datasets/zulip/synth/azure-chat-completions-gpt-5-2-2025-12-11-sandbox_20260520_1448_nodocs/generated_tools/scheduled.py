from __future__ import annotations

from typing import Any, Optional

from zulip_client import ZulipClient


def create_scheduled_message(
    client: ZulipClient,
    *,
    type: str,
    to: Any,
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
) -> dict:
    data: dict[str, Any] = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        data["topic"] = topic
    return client.request("POST", "/scheduled_messages", data=data)


def get_scheduled_messages(client: ZulipClient) -> dict:
    return client.request("GET", "/scheduled_messages")


def delete_scheduled_message(client: ZulipClient, *, scheduled_message_id: int) -> dict:
    return client.request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
