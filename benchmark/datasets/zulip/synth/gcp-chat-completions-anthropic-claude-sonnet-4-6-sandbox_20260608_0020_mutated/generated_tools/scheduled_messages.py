"""Zulip Scheduled Messages API tools."""
import json
from typing import Optional, Any
from .client import zulip_request


def get_scheduled_messages() -> dict:
    """Get all scheduled messages for the current user."""
    try:
        return zulip_request("GET", "scheduled_messages")
    except Exception as e:
        return {"error": str(e)}


def create_scheduled_message(
    type: str,
    to: Any,
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
) -> dict:
    """Create a new scheduled message.

    Args:
        type: Message type - 'channel', 'channel_name', or 'direct'.
        to: For channel messages: channel ID (int). For direct messages: list of user IDs.
        content: The content of the message.
        scheduled_delivery_timestamp: UNIX timestamp (UTC seconds) for when to send.
        topic: Topic for channel messages (required for channel type).
    """
    try:
        data: dict = {
            "type": type,
            "to": to if isinstance(to, int) else json.dumps(to),
            "content": content,
            "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
        }
        if topic is not None:
            data["topic"] = topic
        return zulip_request("POST", "scheduled_messages", data=data)
    except Exception as e:
        return {"error": str(e)}


def update_scheduled_message(
    scheduled_message_id: int,
    type: Optional[str] = None,
    to: Optional[Any] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> dict:
    """Edit an existing scheduled message.

    Args:
        scheduled_message_id: The ID of the scheduled message to update.
        type: New message type - 'channel', 'channel_name', or 'direct'.
        to: New target audience (channel ID or list of user IDs).
        content: New content for the message.
        topic: New topic for channel messages.
        scheduled_delivery_timestamp: New UNIX timestamp for when to send.
    """
    try:
        data: dict = {}
        if type is not None:
            data["type"] = type
        if to is not None:
            data["to"] = to if isinstance(to, int) else json.dumps(to)
        if content is not None:
            data["content"] = content
        if topic is not None:
            data["topic"] = topic
        if scheduled_delivery_timestamp is not None:
            data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
        return zulip_request("PATCH", f"scheduled_messages/{scheduled_message_id}", data=data)
    except Exception as e:
        return {"error": str(e)}


def delete_scheduled_message(scheduled_message_id: int) -> dict:
    """Delete a scheduled message.

    Args:
        scheduled_message_id: The ID of the scheduled message to delete.
    """
    try:
        return zulip_request("DELETE", f"scheduled_messages/{scheduled_message_id}")
    except Exception as e:
        return {"error": str(e)}
