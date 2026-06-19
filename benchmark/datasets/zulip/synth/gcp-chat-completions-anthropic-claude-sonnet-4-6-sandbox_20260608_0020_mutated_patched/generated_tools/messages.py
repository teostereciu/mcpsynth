"""Zulip Messages API tools."""
import json
from typing import Optional, List, Any
from .client import zulip_request


def send_message(
    type: str,
    to: Any,
    content: str,
    topic: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> dict:
    """Send a channel message or direct message.

    Args:
        type: Message type - 'channel' or 'direct' (or 'stream'/'private').
        to: For channel messages: channel name or ID. For direct messages: list of user IDs or emails.
        content: The message content.
        topic: Topic for channel messages (required for channel messages).
        read_by_sender: Whether message should be initially marked read by sender.
    """
    try:
        data: dict = {"type": type, "to": to if isinstance(to, str) else json.dumps(to), "content": content}
        if topic is not None:
            data["topic"] = topic
        if read_by_sender is not None:
            data["read_by_sender"] = json.dumps(read_by_sender)
        return zulip_request("POST", "messages", data=data)
    except Exception as e:
        return {"error": str(e)}


def get_messages(
    num_before: int,
    num_after: int,
    anchor: Optional[str] = "newest",
    narrow: Optional[List[dict]] = None,
    apply_markdown: bool = True,
    include_anchor: bool = True,
) -> dict:
    """Fetch messages from Zulip.

    Args:
        num_before: Number of messages before the anchor.
        num_after: Number of messages after the anchor.
        anchor: Message ID or 'newest'/'oldest'/'first_unread' to anchor the fetch.
        narrow: List of narrow filter objects e.g. [{"operator": "channel", "operand": "general"}].
        apply_markdown: If True, return content as rendered HTML.
        include_anchor: Whether to include the anchor message.
    """
    try:
        params: dict = {
            "num_before": num_before,
            "num_after": num_after,
            "anchor": anchor,
            "apply_markdown": json.dumps(apply_markdown),
            "include_anchor": json.dumps(include_anchor),
        }
        if narrow is not None:
            params["narrow"] = json.dumps(narrow)
        return zulip_request("GET", "messages", params=params)
    except Exception as e:
        return {"error": str(e)}


def get_message(message_id: int, apply_markdown: bool = True) -> dict:
    """Fetch a single message by ID.

    Args:
        message_id: The ID of the message to fetch.
        apply_markdown: If True, return content as rendered HTML.
    """
    try:
        params = {"apply_markdown": json.dumps(apply_markdown)}
        return zulip_request("GET", f"messages/{message_id}", params=params)
    except Exception as e:
        return {"error": str(e)}


def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    stream_id: Optional[int] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
) -> dict:
    """Edit a message's content, topic, or channel.

    Args:
        message_id: The target message's ID.
        content: New content for the message.
        topic: New topic to move the message(s) to.
        propagate_mode: Which messages to edit: 'change_one', 'change_later', or 'change_all'.
        stream_id: Channel ID to move the message(s) to.
        send_notification_to_old_thread: Whether to notify old thread of move.
        send_notification_to_new_thread: Whether to notify new thread of move.
    """
    try:
        data: dict = {}
        if content is not None:
            data["content"] = content
        if topic is not None:
            data["topic"] = topic
        if propagate_mode is not None:
            data["propagate_mode"] = propagate_mode
        if stream_id is not None:
            data["stream_id"] = stream_id
        if send_notification_to_old_thread is not None:
            data["send_notification_to_old_thread"] = json.dumps(send_notification_to_old_thread)
        if send_notification_to_new_thread is not None:
            data["send_notification_to_new_thread"] = json.dumps(send_notification_to_new_thread)
        return zulip_request("PATCH", f"messages/{message_id}", data=data)
    except Exception as e:
        return {"error": str(e)}


def delete_message(message_id: int) -> dict:
    """Permanently delete a message.

    Args:
        message_id: The target message's ID.
    """
    try:
        return zulip_request("DELETE", f"messages/{message_id}")
    except Exception as e:
        return {"error": str(e)}


def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> dict:
    """Add an emoji reaction to a message.

    Args:
        message_id: The target message's ID.
        emoji_name: The emoji's human-readable name (e.g. 'octopus').
        emoji_code: Optional unique identifier for the emoji codepoint.
        reaction_type: Type of emoji: 'unicode_emoji', 'realm_emoji', or 'zulip_extra_emoji'.
    """
    try:
        data: dict = {"emoji_name": emoji_name}
        if emoji_code is not None:
            data["emoji_code"] = emoji_code
        if reaction_type is not None:
            data["reaction_type"] = reaction_type
        return zulip_request("POST", f"messages/{message_id}/reactions", data=data)
    except Exception as e:
        return {"error": str(e)}


def remove_reaction(
    message_id: int,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> dict:
    """Remove an emoji reaction from a message.

    Args:
        message_id: The target message's ID.
        emoji_name: The emoji's human-readable name.
        emoji_code: Optional unique identifier for the emoji codepoint.
        reaction_type: Type of emoji: 'unicode_emoji', 'realm_emoji', or 'zulip_extra_emoji'.
    """
    try:
        data: dict = {}
        if emoji_name is not None:
            data["emoji_name"] = emoji_name
        if emoji_code is not None:
            data["emoji_code"] = emoji_code
        if reaction_type is not None:
            data["reaction_type"] = reaction_type
        return zulip_request("DELETE", f"messages/{message_id}/reactions", data=data)
    except Exception as e:
        return {"error": str(e)}


def update_message_flags(messages: List[int], op: str, flag: str) -> dict:
    """Add or remove personal message flags (read, starred, etc.) on messages.

    Args:
        messages: List of message IDs to update.
        op: Operation - 'add' or 'remove'.
        flag: The flag to add/remove: 'read', 'starred', 'collapsed', etc.
    """
    try:
        data = {
            "messages": json.dumps(messages),
            "op": op,
            "flag": flag,
        }
        return zulip_request("POST", "messages/flags", data=data)
    except Exception as e:
        return {"error": str(e)}


def get_message_history(message_id: int) -> dict:
    """Get the edit history of a message.

    Args:
        message_id: The target message's ID.
    """
    try:
        return zulip_request("GET", f"messages/{message_id}/history")
    except Exception as e:
        return {"error": str(e)}


def render_message(content: str) -> dict:
    """Render a message's Markdown content to HTML.

    Args:
        content: The Markdown content to render.
    """
    try:
        return zulip_request("POST", "messages/render", data={"content": content})
    except Exception as e:
        return {"error": str(e)}


def mark_all_as_read() -> dict:
    """Mark all messages as read for the current user."""
    try:
        return zulip_request("POST", "mark_all_as_read")
    except Exception as e:
        return {"error": str(e)}


def mark_stream_as_read(stream_id: int) -> dict:
    """Mark all messages in a channel as read.

    Args:
        stream_id: The ID of the channel to mark as read.
    """
    try:
        return zulip_request("POST", "mark_stream_as_read", data={"stream_id": stream_id})
    except Exception as e:
        return {"error": str(e)}


def mark_topic_as_read(stream_id: int, topic_name: str) -> dict:
    """Mark all messages in a topic as read.

    Args:
        stream_id: The ID of the channel containing the topic.
        topic_name: The name of the topic to mark as read.
    """
    try:
        return zulip_request(
            "POST",
            "mark_topic_as_read",
            data={"stream_id": stream_id, "topic_name": topic_name},
        )
    except Exception as e:
        return {"error": str(e)}


def get_read_receipts(message_id: int) -> dict:
    """Get read receipts for a message.

    Args:
        message_id: The target message's ID.
    """
    try:
        return zulip_request("GET", f"messages/{message_id}/read_receipts")
    except Exception as e:
        return {"error": str(e)}


def upload_file(filename: str, file_content: bytes) -> dict:
    """Upload a file to Zulip.

    Args:
        filename: The name of the file to upload.
        file_content: The binary content of the file.
    """
    try:
        import io
        files = {"filename": (filename, io.BytesIO(file_content))}
        return zulip_request("POST", "user_uploads", files=files)
    except Exception as e:
        return {"error": str(e)}


def check_messages_match_narrow(msg_ids: List[int], narrow: List[dict]) -> dict:
    """Check if messages match a narrow filter.

    Args:
        msg_ids: List of message IDs to check.
        narrow: The narrow filter to check against.
    """
    try:
        params = {
            "msg_ids": json.dumps(msg_ids),
            "narrow": json.dumps(narrow),
        }
        return zulip_request("GET", "messages/matches_narrow", params=params)
    except Exception as e:
        return {"error": str(e)}


def update_message_flags_for_narrow(
    anchor: str,
    num_before: int,
    num_after: int,
    narrow: List[dict],
    op: str,
    flag: str,
) -> dict:
    """Update message flags for messages matching a narrow filter.

    Args:
        anchor: Message ID or 'newest'/'oldest'/'first_unread'.
        num_before: Number of messages before anchor.
        num_after: Number of messages after anchor.
        narrow: Narrow filter to select messages.
        op: Operation - 'add' or 'remove'.
        flag: The flag to add/remove.
    """
    try:
        data = {
            "anchor": anchor,
            "num_before": num_before,
            "num_after": num_after,
            "narrow": json.dumps(narrow),
            "op": op,
            "flag": flag,
        }
        return zulip_request("POST", "messages/flags/narrow", data=data)
    except Exception as e:
        return {"error": str(e)}
