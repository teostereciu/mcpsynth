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
    """Send a channel message or a direct message.

    Args:
        type: "stream"/"channel" for channel messages, "direct"/"private" for DMs.
        to: For channel messages, channel name or ID. For DMs, list of user IDs or emails.
        content: The message content.
        topic: Topic (required for channel messages).
        read_by_sender: Whether the message should be initially marked read by its sender.
    """
    data: dict = {"type": type, "content": content}
    if isinstance(to, list):
        data["to"] = json.dumps(to)
    else:
        data["to"] = to
    if topic is not None:
        data["topic"] = topic
    if read_by_sender is not None:
        data["read_by_sender"] = json.dumps(read_by_sender)
    return zulip_request("POST", "messages", data=data)


def get_messages(
    anchor: Optional[str] = "newest",
    num_before: int = 100,
    num_after: int = 0,
    narrow: Optional[List[dict]] = None,
    apply_markdown: bool = False,
    include_anchor: bool = True,
) -> dict:
    """Fetch messages from Zulip.

    Args:
        anchor: Message ID or special value: "newest", "oldest", "first_unread".
        num_before: Number of messages before the anchor.
        num_after: Number of messages after the anchor.
        narrow: List of narrow filter objects, e.g. [{"operator": "channel", "operand": "general"}].
        apply_markdown: If True, return HTML-rendered content; otherwise raw Markdown.
        include_anchor: Whether to include the anchor message.
    """
    params: dict = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "apply_markdown": json.dumps(apply_markdown),
        "include_anchor": json.dumps(include_anchor),
    }
    if narrow is not None:
        params["narrow"] = json.dumps(narrow)
    else:
        params["narrow"] = "[]"
    return zulip_request("GET", "messages", params=params)


def get_message(message_id: int, apply_markdown: bool = False) -> dict:
    """Fetch a single message by ID.

    Args:
        message_id: The target message's ID.
        apply_markdown: If True, return HTML-rendered content.
    """
    params = {"apply_markdown": json.dumps(apply_markdown)}
    return zulip_request("GET", f"messages/{message_id}", params=params)


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
        propagate_mode: "change_one", "change_later", or "change_all".
        stream_id: Channel ID to move the message(s) to.
        send_notification_to_old_thread: Notify old topic of move.
        send_notification_to_new_thread: Notify new topic of move.
    """
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


def delete_message(message_id: int) -> dict:
    """Permanently delete a message.

    Args:
        message_id: The target message's ID.
    """
    return zulip_request("DELETE", f"messages/{message_id}")


def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> dict:
    """Add an emoji reaction to a message.

    Args:
        message_id: The target message's ID.
        emoji_name: The emoji's human-readable name (e.g. "octopus").
        emoji_code: Optional unique emoji codepoint identifier.
        reaction_type: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji".
    """
    data: dict = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return zulip_request("POST", f"messages/{message_id}/reactions", data=data)


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
        emoji_code: Optional unique emoji codepoint identifier.
        reaction_type: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji".
    """
    data: dict = {}
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return zulip_request("DELETE", f"messages/{message_id}/reactions", data=data)


def update_message_flags(messages: List[int], op: str, flag: str) -> dict:
    """Add or remove personal message flags (e.g. 'read', 'starred').

    Args:
        messages: List of message IDs to update.
        op: "add" or "remove".
        flag: The flag name: "read", "starred", "collapsed", etc.
    """
    data = {
        "messages": json.dumps(messages),
        "op": op,
        "flag": flag,
    }
    return zulip_request("POST", "messages/flags", data=data)


def get_message_history(message_id: int) -> dict:
    """Get the edit history of a message.

    Args:
        message_id: The target message's ID.
    """
    return zulip_request("GET", f"messages/{message_id}/history")


def mark_all_as_read() -> dict:
    """Mark all messages as read."""
    return zulip_request("POST", "mark_all_as_read")


def mark_stream_as_read(stream_id: int) -> dict:
    """Mark all messages in a channel as read.

    Args:
        stream_id: The ID of the channel.
    """
    return zulip_request("POST", "mark_stream_as_read", data={"stream_id": stream_id})


def mark_topic_as_read(stream_id: int, topic_name: str) -> dict:
    """Mark all messages in a topic as read.

    Args:
        stream_id: The ID of the channel.
        topic_name: The name of the topic.
    """
    return zulip_request(
        "POST",
        "mark_topic_as_read",
        data={"stream_id": stream_id, "topic_name": topic_name},
    )


def render_message(content: str) -> dict:
    """Render a Zulip message to HTML.

    Args:
        content: The Markdown content to render.
    """
    return zulip_request("POST", "messages/render", data={"content": content})


def get_read_receipts(message_id: int) -> dict:
    """Get read receipts for a message.

    Args:
        message_id: The target message's ID.
    """
    return zulip_request("GET", f"messages/{message_id}/read_receipts")


def upload_file(file_path: str) -> dict:
    """Upload a file to Zulip.

    Args:
        file_path: Local path to the file to upload.
    """
    try:
        with open(file_path, "rb") as f:
            return zulip_request("POST", "user_uploads", files={"filename": f})
    except Exception as e:
        return {"error": str(e)}
