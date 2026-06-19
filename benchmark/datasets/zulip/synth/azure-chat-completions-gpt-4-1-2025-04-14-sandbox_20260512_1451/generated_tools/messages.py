import os
import requests
from mcp.server.fastmcp import FastMCP

ZULIP_SITE = os.environ.get("ZULIP_SITE")
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
BASE_URL = f"{ZULIP_SITE}/api/v1"


def send_message(type, to, content, topic=None, queue_id=None, local_id=None, read_by_sender=None):
    """
    Send a channel or direct message.
    Args:
        type (str): 'stream', 'channel', 'direct', or 'private'
        to (str/int/list): Channel name/ID or user ID/email(s)
        content (str): Message content
        topic (str, optional): Topic for channel messages
        queue_id (str, optional): Event queue ID for local echo
        local_id (str, optional): Local echo message ID
        read_by_sender (bool, optional): Mark as read by sender
    Returns:
        dict: JSON response from Zulip
    """
    url = f"{BASE_URL}/messages"
    data = {
        "type": type,
        "to": to,
        "content": content,
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
        resp = requests.post(url, data=data, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_messages(anchor="newest", num_before=100, num_after=0, narrow=None, client_gravatar=True, apply_markdown=True, message_ids=None, allow_empty_topic_name=False, include_anchor=True, anchor_date=None):
    """
    Fetch messages using Zulip's narrow/filter system.
    Args:
        anchor (str/int): Message ID or special string ('newest', 'oldest', etc.)
        num_before (int): Number of messages before anchor
        num_after (int): Number of messages after anchor
        narrow (list, optional): Narrow/filter (list of dicts)
        client_gravatar (bool, optional): Compute gravatar URLs
        apply_markdown (bool, optional): Return HTML or markdown
        message_ids (list, optional): Specific message IDs to fetch
        allow_empty_topic_name (bool, optional): Allow empty topic names
        include_anchor (bool, optional): Include anchor message
        anchor_date (str, optional): Date for anchor='date'
    Returns:
        dict: JSON response from Zulip
    """
    url = f"{BASE_URL}/messages"
    params = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "client_gravatar": client_gravatar,
        "apply_markdown": apply_markdown,
        "allow_empty_topic_name": allow_empty_topic_name,
        "include_anchor": include_anchor,
    }
    if narrow is not None:
        params["narrow"] = narrow
    if message_ids is not None:
        params["message_ids"] = message_ids
    if anchor_date is not None:
        params["anchor_date"] = anchor_date
    try:
        resp = requests.get(url, params=params, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def delete_message(message_id):
    """
    Permanently delete a message by ID.
    Args:
        message_id (int): The ID of the message to delete.
    Returns:
        dict: JSON response from Zulip
    """
    url = f"{BASE_URL}/messages/{message_id}"
    try:
        resp = requests.delete(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def update_message(message_id, content=None, topic=None, propagate_mode=None, send_notification_to_old_thread=None, send_notification_to_new_thread=None, prev_content_sha256=None, stream_id=None):
    """
    Edit a message's content, topic, or channel.
    Args:
        message_id (int): ID of the message to edit
        content (str, optional): New content
        topic (str, optional): New topic
        propagate_mode (str, optional): 'change_one', 'change_later', 'change_all'
        send_notification_to_old_thread (bool, optional): Notify old topic
        send_notification_to_new_thread (bool, optional): Notify new topic
        prev_content_sha256 (str, optional): SHA256 of previous content
        stream_id (int, optional): Move to channel ID
    Returns:
        dict: JSON response from Zulip
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
        resp = requests.patch(url, data=data, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def update_message_flags(messages, op, flag):
    """
    Add or remove personal message flags (e.g. read, starred) on message IDs.
    Args:
        messages (list): List of message IDs
        op (str): 'add' or 'remove'
        flag (str): Flag to add/remove
    Returns:
        dict: JSON response from Zulip
    """
    url = f"{BASE_URL}/messages/flags"
    data = {
        "messages": messages,
        "op": op,
        "flag": flag,
    }
    try:
        resp = requests.post(url, data=data, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def update_message_flags_for_narrow(anchor, num_before, num_after, narrow, op, flag, include_anchor=True):
    """
    Add or remove personal message flags (e.g. read, starred) on a range of messages within a narrow.
    Args:
        anchor (str/int): Anchor message ID or special string
        num_before (int): Number of messages before anchor
        num_after (int): Number of messages after anchor
        narrow (list): Narrow/filter (list of dicts)
        op (str): 'add' or 'remove'
        flag (str): Flag to add/remove
        include_anchor (bool, optional): Include anchor message
    Returns:
        dict: JSON response from Zulip
    """
    url = f"{BASE_URL}/messages/flags/narrow"
    data = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "narrow": narrow,
        "op": op,
        "flag": flag,
        "include_anchor": include_anchor,
    }
    try:
        resp = requests.post(url, data=data, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_message_history(message_id, allow_empty_topic_name=False):
    """
    Fetch the edit history of a message.
    Args:
        message_id (int): Message ID
        allow_empty_topic_name (bool, optional): Allow empty topic names
    Returns:
        dict: JSON response from Zulip
    """
    url = f"{BASE_URL}/messages/{message_id}/history"
    params = {"allow_empty_topic_name": allow_empty_topic_name}
    try:
        resp = requests.get(url, params=params, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_message(message_id, apply_markdown=True, allow_empty_topic_name=False):
    """
    Fetch a single message by ID.
    Args:
        message_id (int): Message ID
        apply_markdown (bool, optional): Return HTML or markdown
        allow_empty_topic_name (bool, optional): Allow empty topic names
    Returns:
        dict: JSON response from Zulip
    """
    url = f"{BASE_URL}/messages/{message_id}"
    params = {
        "apply_markdown": apply_markdown,
        "allow_empty_topic_name": allow_empty_topic_name,
    }
    try:
        resp = requests.get(url, params=params, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
