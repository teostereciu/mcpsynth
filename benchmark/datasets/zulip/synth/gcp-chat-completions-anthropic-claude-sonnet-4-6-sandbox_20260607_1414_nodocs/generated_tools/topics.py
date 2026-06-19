"""
Zulip MCP Tools — Topics domain
Covers: list, rename, resolve/unresolve, delete
"""

from typing import Optional
from .client import zulip_get, zulip_post, zulip_patch, zulip_delete


def get_topics(stream_id: int) -> dict:
    """Get the list of topics in a stream.

    Args:
        stream_id: The ID of the stream whose topics to list.
    """
    return zulip_get(f"/users/me/{stream_id}/topics")


def delete_topic(stream_id: int, topic_name: str) -> dict:
    """Delete all messages in a topic. Requires admin privileges.

    Args:
        stream_id: The ID of the stream containing the topic.
        topic_name: The name of the topic to delete.
    """
    return zulip_post(
        f"/streams/{stream_id}/delete_topic", {"topic_name": topic_name}
    )


def rename_topic(
    stream_id: int,
    current_topic: str,
    new_topic: str,
    propagate_mode: str = "change_all",
    send_notification_to_old_thread: bool = True,
    send_notification_to_new_thread: bool = True,
) -> dict:
    """Rename a topic by moving all its messages to a new topic name.

    Args:
        stream_id: The ID of the stream containing the topic.
        current_topic: The current name of the topic.
        new_topic: The new name for the topic.
        propagate_mode: "change_one", "change_later", or "change_all".
        send_notification_to_old_thread: Notify the old thread of the rename.
        send_notification_to_new_thread: Notify the new thread of the rename.
    """
    # Fetch the oldest message in the topic to use as anchor
    narrow = f'[{{"operator":"stream","operand":{stream_id}}},{{"operator":"topic","operand":"{current_topic}"}}]'
    msgs = zulip_get(
        "/messages",
        {
            "anchor": "oldest",
            "num_before": 0,
            "num_after": 1,
            "narrow": narrow,
            "apply_markdown": False,
        },
    )
    messages = msgs.get("messages", [])
    if not messages:
        return {"result": "error", "msg": "No messages found in topic"}
    message_id = messages[0]["id"]
    return zulip_patch(
        f"/messages/{message_id}",
        {
            "topic": new_topic,
            "propagate_mode": propagate_mode,
            "send_notification_to_old_thread": send_notification_to_old_thread,
            "send_notification_to_new_thread": send_notification_to_new_thread,
        },
    )


def resolve_topic(stream_id: int, topic_name: str) -> dict:
    """Mark a topic as resolved by prepending '✔ ' to its name.

    Args:
        stream_id: The ID of the stream containing the topic.
        topic_name: The current name of the topic (without the resolved prefix).
    """
    resolved_name = f"✔ {topic_name}"
    return rename_topic(stream_id, topic_name, resolved_name)


def unresolve_topic(stream_id: int, topic_name: str) -> dict:
    """Mark a topic as unresolved by removing the '✔ ' prefix from its name.

    Args:
        stream_id: The ID of the stream containing the topic.
        topic_name: The current name of the topic (with the resolved prefix).
    """
    unresolved_name = topic_name.removeprefix("✔ ")
    return rename_topic(stream_id, topic_name, unresolved_name)


def move_topic_to_stream(
    source_stream_id: int,
    destination_stream_id: int,
    topic_name: str,
    new_topic_name: Optional[str] = None,
    propagate_mode: str = "change_all",
    send_notification_to_old_thread: bool = True,
    send_notification_to_new_thread: bool = True,
) -> dict:
    """Move an entire topic from one stream to another.

    Args:
        source_stream_id: The ID of the source stream.
        destination_stream_id: The ID of the destination stream.
        topic_name: The name of the topic to move.
        new_topic_name: Optional new name for the topic in the destination stream.
        propagate_mode: "change_one", "change_later", or "change_all".
        send_notification_to_old_thread: Notify the old thread.
        send_notification_to_new_thread: Notify the new thread.
    """
    narrow = f'[{{"operator":"stream","operand":{source_stream_id}}},{{"operator":"topic","operand":"{topic_name}"}}]'
    msgs = zulip_get(
        "/messages",
        {
            "anchor": "oldest",
            "num_before": 0,
            "num_after": 1,
            "narrow": narrow,
            "apply_markdown": False,
        },
    )
    messages = msgs.get("messages", [])
    if not messages:
        return {"result": "error", "msg": "No messages found in topic"}
    message_id = messages[0]["id"]
    params: dict = {
        "stream_id": destination_stream_id,
        "topic": new_topic_name if new_topic_name else topic_name,
        "propagate_mode": propagate_mode,
        "send_notification_to_old_thread": send_notification_to_old_thread,
        "send_notification_to_new_thread": send_notification_to_new_thread,
    }
    return zulip_patch(f"/messages/{message_id}", params)
