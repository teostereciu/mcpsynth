
import json

def get_messages(
    num_before: int,
    num_after: int,
    anchor: Optional[Union[int, str]] = None,
    narrow: Optional[List[dict]] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    use_first_unread_anchor: Optional[bool] = None,
) -> dict:
    """Get messages from a stream or private message conversation.

    Args:
        num_before: The number of messages to fetch before the anchor.
        num_after: The number of messages to fetch after the anchor.
        anchor: The anchor message ID. Can be an integer message ID or the string 'newest'.
        narrow: A list of objects specifying the narrow.
        client_gravatar: Whether to include gravatar URLs for the senders.
        apply_markdown: Whether to apply Markdown to the message content.
        use_first_unread_anchor: Whether to use the first unread message as the anchor.
    """
    params = {
        "num_before": num_before,
        "num_after": num_after,
    }
    if anchor is not None:
        params["anchor"] = anchor
    if narrow:
        params["narrow"] = json.dumps(narrow)
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if apply_markdown is not None:
        params["apply_markdown"] = apply_markdown
    if use_first_unread_anchor is not None:
        params["use_first_unread_anchor"] = use_first_unread_anchor

    return make_request("GET", "messages", params=params)


def update_message(
    message_id: int,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = True,
    send_notification_to_new_thread: Optional[bool] = True,
    content: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> dict:
    """Edit a message.

    Args:
        message_id: The ID of the message to edit.
        topic: The new topic for the message.
        propagate_mode: The propagation mode for the topic edit. Defaults to 'change_one'.
        send_notification_to_old_thread: Whether to send notifications to the old thread. Defaults to True.
        send_notification_to_new_thread: Whether to send notifications to the new thread. Defaults to True.
        content: The new content of the message.
        stream_id: The ID of the stream to move the message to.
    """
    data = {
        "message_id": message_id,
    }
    if topic:
        data["topic"] = topic
    if propagate_mode:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = send_notification_to_old_thread
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = send_notification_to_new_thread
    if content:
        data["content"] = content
    if stream_id:
        data["stream_id"] = stream_id

    return make_request("PATCH", f"messages/{message_id}", data=data)


def delete_message(message_id: int) -> dict:
    """Delete a message.

    Args:
        message_id: The ID of the message to delete.
    """
    return make_request("DELETE", f"messages/{message_id}")
from .zulip_client import make_request
from typing import List, Optional, Union

def send_message(
    message_type: str,
    to: Union[List[int], str],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> dict:
    """Send a message to a user, multiple users, or a stream.

    Args:
        message_type: The type of message to send. 'private' for a private message, 'stream' for a stream message.
        to: The recipient of the message. For 'private' messages, a list of user IDs. For 'stream' messages, the name of the stream.
        content: The content of the message.
        topic: The topic of the message (only for 'stream' messages).
        queue_id: A unique ID for the message to be returned in the response.
        local_id: A unique ID for the message to be returned in the response.
        read_by_sender: Whether the message should be marked as read by the sender.
    """
    data = {
        "type": message_type,
        "to": to,
        "content": content,
    }
    if topic:
        data["topic"] = topic
    if queue_id:
        data["queue_id"] = queue_id
    if local_id:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = read_by_sender

    return make_request("POST", "messages", data=data)
