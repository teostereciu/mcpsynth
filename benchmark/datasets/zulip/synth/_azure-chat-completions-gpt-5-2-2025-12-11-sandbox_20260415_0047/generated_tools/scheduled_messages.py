"""Scheduled message tools."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Union

from .http import zulip_request


JsonDict = Dict[str, Any]


def create_scheduled_message(
    *,
    type: str,
    to: Union[int, Sequence[int]],
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> JsonDict:
    """POST /scheduled_messages"""
    data: Dict[str, Any] = {
        "type": type,
        "to": to,
        "content": content,
        "topic": topic,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
        "read_by_sender": read_by_sender,
    }
    return zulip_request("POST", "/scheduled_messages", data=data)


def get_scheduled_messages() -> JsonDict:
    """GET /scheduled_messages"""
    return zulip_request("GET", "/scheduled_messages")


def update_scheduled_message(*, scheduled_message_id: int, scheduled_delivery_timestamp: int) -> JsonDict:
    """PATCH /scheduled_messages/{scheduled_message_id}"""
    return zulip_request(
        "PATCH",
        f"/scheduled_messages/{scheduled_message_id}",
        data={"scheduled_delivery_timestamp": scheduled_delivery_timestamp},
    )


def delete_scheduled_message(*, scheduled_message_id: int) -> JsonDict:
    """DELETE /scheduled_messages/{scheduled_message_id}"""
    return zulip_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
