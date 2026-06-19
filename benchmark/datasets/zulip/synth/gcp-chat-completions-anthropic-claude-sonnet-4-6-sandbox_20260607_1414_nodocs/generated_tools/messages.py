"""
Zulip MCP Tools — Messages domain
Covers: send, fetch, edit, delete, move, history, flags
"""

import requests
from typing import Optional
from .client import zulip_get, zulip_post, zulip_patch, zulip_delete


def send_message(
    type: str,
    content: str,
    to: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
) -> dict:
    """Send a message to a stream or direct message.

    Args:
        type: "stream" for stream messages, "direct" (or "private") for DMs.
        content: The Markdown-formatted content of the message.
        to: For stream messages, the name or ID of the stream.
            For DMs, a comma-separated list of user email addresses or IDs.
        topic: Required for stream messages. The topic name (max 60 chars).
        queue_id: Optional. The ID of an event queue registered for this client.
        local_id: Optional. A local ID for the message (for deduplication).
    """
    params: dict = {"type": type, "content": content, "to": to}
    if topic is not None:
        params["topic"] = topic
    if queue_id is not None:
        params["queue_id"] = queue_id
    if local_id is not None:
        params["local_id"] = local_id
    return zulip_post("/messages", params)


def get_messages(
    anchor: str,
    num_before: int,
    num_after: int,
    narrow: Optional[str] = None,
    client_gravatar: bool = False,
    apply_markdown: bool = True,
    include_anchor: bool = True,
) -> dict:
    """Fetch a range of messages from a Zulip server.

    Args:
        anchor: Integer message ID or special values "newest", "oldest",
                "first_unread" to anchor the fetch window.
        num_before: Number of messages to fetch before the anchor.
        num_after: Number of messages to fetch after the anchor.
        narrow: JSON-encoded list of narrow filter objects, e.g.
                '[{"operator":"stream","operand":"general"}]'.
        client_gravatar: If True, the server will not compute Gravatar URLs.
        apply_markdown: If True, message content is rendered as HTML.
        include_anchor: If False, the anchor message itself is excluded.
    """
    params: dict = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "client_gravatar": client_gravatar,
        "apply_markdown": apply_markdown,
        "include_anchor": include_anchor,
    }
    if narrow is not None:
        params["narrow"] = narrow
    return zulip_get("/messages", params)


def get_message(message_id: int, apply_markdown: bool = True) -> dict:
    """Fetch a single message by its ID.

    Args:
        message_id: The unique ID of the message.
        apply_markdown: If True, message content is rendered as HTML.
    """
    return zulip_get(f"/messages/{message_id}", {"apply_markdown": apply_markdown})


def edit_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: bool = True,
    send_notification_to_new_thread: bool = True,
) -> dict:
    """Edit the content and/or topic of a message.

    Args:
        message_id: The ID of the message to edit.
        content: New Markdown content for the message.
        topic: New topic for the message (stream messages only).
        propagate_mode: One of "change_one", "change_later", "change_all".
                        Controls which messages are affected when changing topic.
        send_notification_to_old_thread: Whether to send a notification to the
                                         old thread when moving messages.
        send_notification_to_new_thread: Whether to send a notification to the
                                         new thread when moving messages.
    """
    params: dict = {}
    if content is not None:
        params["content"] = content
    if topic is not None:
        params["topic"] = topic
    if propagate_mode is not None:
        params["propagate_mode"] = propagate_mode
    params["send_notification_to_old_thread"] = send_notification_to_old_thread
    params["send_notification_to_new_thread"] = send_notification_to_new_thread
    return zulip_patch(f"/messages/{message_id}", params)


def delete_message(message_id: int) -> dict:
    """Permanently delete a message.

    Args:
        message_id: The ID of the message to delete.
    """
    return zulip_delete(f"/messages/{message_id}")


def move_message(
    message_id: int,
    stream_id: Optional[int] = None,
    topic: Optional[str] = None,
    propagate_mode: str = "change_one",
    send_notification_to_old_thread: bool = True,
    send_notification_to_new_thread: bool = True,
) -> dict:
    """Move a message (and optionally subsequent messages) to a different
    stream and/or topic.

    Args:
        message_id: The ID of the message to move.
        stream_id: The ID of the destination stream (optional).
        topic: The destination topic name (optional).
        propagate_mode: "change_one", "change_later", or "change_all".
        send_notification_to_old_thread: Notify the old thread of the move.
        send_notification_to_new_thread: Notify the new thread of the move.
    """
    params: dict = {
        "propagate_mode": propagate_mode,
        "send_notification_to_old_thread": send_notification_to_old_thread,
        "send_notification_to_new_thread": send_notification_to_new_thread,
    }
    if stream_id is not None:
        params["stream_id"] = stream_id
    if topic is not None:
        params["topic"] = topic
    return zulip_patch(f"/messages/{message_id}", params)


def get_message_history(message_id: int) -> dict:
    """Retrieve the edit history of a message.

    Args:
        message_id: The ID of the message whose history to retrieve.
    """
    return zulip_get(f"/messages/{message_id}/history")


def add_message_flag(messages: str, flag: str) -> dict:
    """Add a flag (e.g. "read", "starred") to one or more messages.

    Args:
        messages: JSON-encoded list of message IDs, e.g. "[1, 2, 3]".
        flag: The flag to add. Common values: "read", "starred".
    """
    return zulip_post("/messages/flags", {"messages": messages, "flag": flag, "op": "add"})


def remove_message_flag(messages: str, flag: str) -> dict:
    """Remove a flag (e.g. "read", "starred") from one or more messages.

    Args:
        messages: JSON-encoded list of message IDs, e.g. "[1, 2, 3]".
        flag: The flag to remove. Common values: "read", "starred".
    """
    return zulip_post("/messages/flags", {"messages": messages, "flag": flag, "op": "remove"})


def mark_all_as_read() -> dict:
    """Mark all messages in the current user's account as read."""
    return zulip_post("/mark_all_as_read", {})


def mark_stream_as_read(stream_id: int) -> dict:
    """Mark all messages in a stream as read.

    Args:
        stream_id: The ID of the stream to mark as read.
    """
    return zulip_post("/mark_stream_as_read", {"stream_id": stream_id})


def mark_topic_as_read(stream_id: int, topic_name: str) -> dict:
    """Mark all messages in a topic as read.

    Args:
        stream_id: The ID of the stream containing the topic.
        topic_name: The name of the topic to mark as read.
    """
    return zulip_post(
        "/mark_topic_as_read", {"stream_id": stream_id, "topic_name": topic_name}
    )


def get_raw_message(message_id: int) -> dict:
    """Retrieve the raw (un-rendered) Markdown content of a message.

    Args:
        message_id: The ID of the message.
    """
    return zulip_get(f"/messages/{message_id}", {"apply_markdown": False})


def check_messages_match_narrow(msg_ids: str, narrow: str) -> dict:
    """Check whether messages match a given narrow filter.

    Args:
        msg_ids: JSON-encoded list of message IDs to check.
        narrow: JSON-encoded list of narrow filter objects.
    """
    return zulip_get("/messages/matches_narrow", {"msg_ids": msg_ids, "narrow": narrow})


def update_message_flags_for_narrow(
    anchor: str,
    num_before: int,
    num_after: int,
    narrow: str,
    op: str,
    flag: str,
    include_anchor: bool = True,
) -> dict:
    """Add or remove a flag on messages matching a narrow filter.

    Args:
        anchor: Integer message ID or "newest"/"oldest"/"first_unread".
        num_before: Number of messages before anchor to consider.
        num_after: Number of messages after anchor to consider.
        narrow: JSON-encoded list of narrow filter objects.
        op: "add" or "remove".
        flag: The flag to update, e.g. "read" or "starred".
        include_anchor: Whether to include the anchor message.
    """
    return zulip_post(
        "/messages/flags/narrow",
        {
            "anchor": anchor,
            "num_before": num_before,
            "num_after": num_after,
            "narrow": narrow,
            "op": op,
            "flag": flag,
            "include_anchor": include_anchor,
        },
    )
