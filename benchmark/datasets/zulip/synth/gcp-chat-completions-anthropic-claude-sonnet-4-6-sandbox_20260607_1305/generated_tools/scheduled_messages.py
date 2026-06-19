"""Zulip Scheduled Messages, Drafts, and Saved Snippets API tools."""
import json
from typing import Optional, List, Any
from .client import zulip_request


# ── Scheduled Messages ──────────────────────────────────────────────────────

def get_scheduled_messages() -> dict:
    """Get all scheduled messages for the current user."""
    return zulip_request("GET", "scheduled_messages")


def create_scheduled_message(
    type: str,
    to: Any,
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
) -> dict:
    """Create a new scheduled message.

    Args:
        type: "stream"/"channel" for channel messages, "direct"/"private" for DMs.
        to: For channel messages, the integer channel ID. For DMs, list of user IDs.
        content: The message content.
        scheduled_delivery_timestamp: UNIX timestamp (UTC seconds) for when to send.
        topic: Topic (required for channel messages).
    """
    data: dict = {
        "type": type,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if isinstance(to, list):
        data["to"] = json.dumps(to)
    else:
        data["to"] = to
    if topic is not None:
        data["topic"] = topic
    return zulip_request("POST", "scheduled_messages", data=data)


def update_scheduled_message(
    scheduled_message_id: int,
    type: Optional[str] = None,
    to: Optional[Any] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> dict:
    """Edit a scheduled message.

    Args:
        scheduled_message_id: The ID of the scheduled message to update.
        type: New message type.
        to: New recipient (channel ID or list of user IDs).
        content: New message content.
        topic: New topic (for channel messages).
        scheduled_delivery_timestamp: New delivery timestamp.
    """
    data: dict = {}
    if type is not None:
        data["type"] = type
    if to is not None:
        data["to"] = json.dumps(to) if isinstance(to, list) else to
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    return zulip_request("PATCH", f"scheduled_messages/{scheduled_message_id}", data=data)


def delete_scheduled_message(scheduled_message_id: int) -> dict:
    """Delete a scheduled message.

    Args:
        scheduled_message_id: The ID of the scheduled message to delete.
    """
    return zulip_request("DELETE", f"scheduled_messages/{scheduled_message_id}")


# ── Message Reminders ────────────────────────────────────────────────────────

def get_reminders() -> dict:
    """Get all message reminders for the current user."""
    return zulip_request("GET", "reminders")


def create_message_reminder(
    message_id: int,
    scheduled_delivery_timestamp: int,
) -> dict:
    """Create a reminder for a message.

    Args:
        message_id: The ID of the message to set a reminder for.
        scheduled_delivery_timestamp: UNIX timestamp (UTC seconds) for the reminder.
    """
    data = {
        "message_id": message_id,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    return zulip_request("POST", "reminders", data=data)


def delete_reminder(reminder_id: int) -> dict:
    """Delete a message reminder.

    Args:
        reminder_id: The ID of the reminder to delete.
    """
    return zulip_request("DELETE", f"reminders/{reminder_id}")


# ── Drafts ───────────────────────────────────────────────────────────────────

def get_drafts() -> dict:
    """Get all drafts for the current user."""
    return zulip_request("GET", "drafts")


def create_drafts(drafts: List[dict]) -> dict:
    """Create one or more drafts.

    Args:
        drafts: List of draft objects. Each draft must have:
                - type: "" (unaddressed), "stream", or "private"
                - to: list of channel/user IDs
                - topic: topic name (for stream drafts)
                - content: draft body
                Optional: timestamp (UNIX seconds)
    """
    return zulip_request("POST", "drafts", data={"drafts": json.dumps(drafts)})


def edit_draft(draft_id: int, draft: dict) -> dict:
    """Edit an existing draft.

    Args:
        draft_id: The ID of the draft to edit.
        draft: Updated draft object with fields: type, to, topic, content, timestamp.
    """
    return zulip_request("PATCH", f"drafts/{draft_id}", data={"draft": json.dumps(draft)})


def delete_draft(draft_id: int) -> dict:
    """Delete a draft.

    Args:
        draft_id: The ID of the draft to delete.
    """
    return zulip_request("DELETE", f"drafts/{draft_id}")


# ── Saved Snippets ───────────────────────────────────────────────────────────

def get_saved_snippets() -> dict:
    """Get all saved snippets for the current user."""
    return zulip_request("GET", "saved_snippets")


def create_saved_snippet(title: str, content: str) -> dict:
    """Create a new saved snippet.

    Args:
        title: The title of the saved snippet.
        content: The Markdown content of the saved snippet.
    """
    return zulip_request("POST", "saved_snippets", data={"title": title, "content": content})


def edit_saved_snippet(saved_snippet_id: int, title: Optional[str] = None, content: Optional[str] = None) -> dict:
    """Edit a saved snippet.

    Args:
        saved_snippet_id: The ID of the saved snippet to edit.
        title: New title for the snippet.
        content: New content for the snippet.
    """
    data: dict = {}
    if title is not None:
        data["title"] = title
    if content is not None:
        data["content"] = content
    return zulip_request("PATCH", f"saved_snippets/{saved_snippet_id}", data=data)


def delete_saved_snippet(saved_snippet_id: int) -> dict:
    """Delete a saved snippet.

    Args:
        saved_snippet_id: The ID of the saved snippet to delete.
    """
    return zulip_request("DELETE", f"saved_snippets/{saved_snippet_id}")
