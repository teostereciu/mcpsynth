"""Zulip Message Reminders API tools."""
from typing import Optional
from .client import zulip_request


def get_reminders() -> dict:
    """Get all message reminders for the current user."""
    try:
        return zulip_request("GET", "reminders")
    except Exception as e:
        return {"error": str(e)}


def create_message_reminder(
    message_id: Optional[int] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
    note: Optional[str] = None,
) -> dict:
    """Create a message reminder to be sent to the current user at a specified time.

    Args:
        message_id: The ID of the message to reference in the reminder.
        scheduled_delivery_timestamp: UNIX timestamp (UTC seconds) for when to send the reminder.
        note: A note to include with the reminder.
    """
    try:
        data: dict = {}
        if message_id is not None:
            data["message_id"] = message_id
        if scheduled_delivery_timestamp is not None:
            data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
        if note is not None:
            data["note"] = note
        return zulip_request("POST", "reminders", data=data)
    except Exception as e:
        return {"error": str(e)}


def delete_reminder(reminder_id: int) -> dict:
    """Delete a message reminder.

    Args:
        reminder_id: The ID of the reminder to delete.
    """
    try:
        return zulip_request("DELETE", f"reminders/{reminder_id}")
    except Exception as e:
        return {"error": str(e)}
