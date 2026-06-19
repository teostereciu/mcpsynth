"""
Zulip MCP Tools — Scheduled Messages domain
Covers: create, list, edit, delete scheduled messages
"""

from typing import Optional
from .client import zulip_get, zulip_post, zulip_patch, zulip_delete


def get_scheduled_messages() -> dict:
    """Get all scheduled messages for the current user."""
    return zulip_get("/scheduled_messages")


def create_scheduled_message(
    type: str,
    to: str,
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
) -> dict:
    """Schedule a message to be sent at a future time.

    Args:
        type: "stream" for stream messages, "direct" for direct messages.
        to: For stream messages, the stream name or ID.
            For direct messages, a JSON-encoded list of recipient user IDs or emails.
        content: The Markdown content of the message.
        scheduled_delivery_timestamp: Unix timestamp (seconds) for when to send.
        topic: Required for stream messages. The topic name.
    """
    params: dict = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        params["topic"] = topic
    return zulip_post("/scheduled_messages", params)


def edit_scheduled_message(
    scheduled_message_id: int,
    type: Optional[str] = None,
    to: Optional[str] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> dict:
    """Edit an existing scheduled message.

    Args:
        scheduled_message_id: The ID of the scheduled message to edit.
        type: New type: "stream" or "direct".
        to: New recipient (stream name/ID or JSON-encoded list of user IDs/emails).
        content: New Markdown content.
        topic: New topic (for stream messages).
        scheduled_delivery_timestamp: New Unix timestamp for delivery.
    """
    params: dict = {}
    if type is not None:
        params["type"] = type
    if to is not None:
        params["to"] = to
    if content is not None:
        params["content"] = content
    if topic is not None:
        params["topic"] = topic
    if scheduled_delivery_timestamp is not None:
        params["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    return zulip_patch(f"/scheduled_messages/{scheduled_message_id}", params)


def delete_scheduled_message(scheduled_message_id: int) -> dict:
    """Delete a scheduled message.

    Args:
        scheduled_message_id: The ID of the scheduled message to delete.
    """
    return zulip_delete(f"/scheduled_messages/{scheduled_message_id}")
