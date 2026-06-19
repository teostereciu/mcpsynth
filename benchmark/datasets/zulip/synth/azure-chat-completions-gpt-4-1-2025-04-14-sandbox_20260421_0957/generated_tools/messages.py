import os
import requests
from typing import Any, Dict

ZULIP_SITE = os.environ.get("ZULIP_SITE")
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
BASE_URL = f"{ZULIP_SITE}/api/v1"

def send_message(type: str, to, content: str, topic: str = None, queue_id: str = None, local_id: str = None, read_by_sender: bool = None) -> Dict[str, Any]:
    """
    Send a channel or direct message.
    Args:
        type: 'stream', 'channel', 'direct', or 'private'
        to: channel name/id for channel messages, list of user ids/emails for direct messages
        content: message body
        topic: topic for channel messages
        queue_id: event queue ID for local echo
        local_id: local echo message ID
        read_by_sender: whether the sender should mark the message as read
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/messages"
    data = {
        "type": type,
        "to": to,
        "content": content
    }
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = read_by_sender
    try:
        resp = requests.post(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), data=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def update_message_flags(messages, op: str, flag: str) -> Dict[str, Any]:
    """
    Add or remove personal message flags (read, starred, etc) on a collection of message IDs.
    Args:
        messages: list of message IDs
        op: 'add' or 'remove'
        flag: flag to add/remove (read, starred, collapsed, etc)
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/messages/flags"
    data = {
        "messages": messages,
        "op": op,
        "flag": flag
    }
    try:
        resp = requests.post(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_message_history(message_id: int, allow_empty_topic_name: bool = False) -> Dict[str, Any]:
    """
    Fetch the edit history of a previously edited message.
    Args:
        message_id: ID of the message
        allow_empty_topic_name: whether empty topic names are supported
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/messages/{message_id}/history"
    params = {"allow_empty_topic_name": allow_empty_topic_name}
    try:
        resp = requests.get(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def edit_message(message_id: int, content: str = None, topic: str = None, propagate_mode: str = None, send_notification_to_old_thread: bool = None, send_notification_to_new_thread: bool = None, prev_content_sha256: str = None, stream_id: int = None) -> Dict[str, Any]:
    """
    Edit a message's content, topic, or channel.
    Args:
        message_id: ID of the message to edit
        content: new content
        topic: new topic
        propagate_mode: 'change_one', 'change_later', 'change_all'
        send_notification_to_old_thread: notify old topic
        send_notification_to_new_thread: notify new topic
        prev_content_sha256: SHA256 of previous content
        stream_id: new channel ID
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/messages/{message_id}"
    data = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = send_notification_to_old_thread
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = send_notification_to_new_thread
    if prev_content_sha256 is not None:
        data["prev_content_sha256"] = prev_content_sha256
    if stream_id is not None:
        data["stream_id"] = stream_id
    try:
        resp = requests.patch(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), data=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def delete_message(message_id: int) -> Dict[str, Any]:
    """
    Permanently delete a message by ID.
    Args:
        message_id: ID of the message to delete
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/messages/{message_id}"
    try:
        resp = requests.delete(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_messages(anchor: str = "newest", num_before: int = 0, num_after: int = 0, narrow=None, include_anchor: bool = True, anchor_date: str = None, client_gravatar: bool = True, apply_markdown: bool = True, message_ids=None, allow_empty_topic_name: bool = False, use_first_unread_anchor: bool = False) -> Dict[str, Any]:
    """
    Fetch messages with optional narrow and anchor.
    Args:
        anchor: message ID or special string (newest, oldest, first_unread, date)
        num_before: number of messages before anchor
        num_after: number of messages after anchor
        narrow: list of narrow filters
        include_anchor: include anchor message
        anchor_date: ISO8601 date for anchor (if anchor='date')
        client_gravatar: whether client computes gravatars
        apply_markdown: return HTML or markdown
        message_ids: list of message IDs to fetch
        allow_empty_topic_name: support empty topic name
        use_first_unread_anchor: legacy, deprecated
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/messages"
    params = {}
    if anchor is not None:
        params["anchor"] = anchor
    if num_before:
        params["num_before"] = num_before
    if num_after:
        params["num_after"] = num_after
    if narrow is not None:
        params["narrow"] = narrow
    if include_anchor is not None:
        params["include_anchor"] = include_anchor
    if anchor_date is not None:
        params["anchor_date"] = anchor_date
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if apply_markdown is not None:
        params["apply_markdown"] = apply_markdown
    if message_ids is not None:
        params["message_ids"] = message_ids
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = allow_empty_topic_name
    if use_first_unread_anchor is not None:
        params["use_first_unread_anchor"] = use_first_unread_anchor
    try:
        resp = requests.get(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
