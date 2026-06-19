import os
import requests
from typing import Any, Dict

ZULIP_SITE = os.environ.get("ZULIP_SITE")
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
BASE_URL = f"{ZULIP_SITE}/api/v1"

def create_scheduled_message(type: str, to, content: str, scheduled_delivery_timestamp: int, topic: str = None, read_by_sender: bool = None) -> Dict[str, Any]:
    """
    Create a scheduled message (channel or direct).
    Args:
        type: 'stream', 'channel', 'direct', or 'private'
        to: channel id for channel messages, list of user ids for direct messages
        content: message body
        scheduled_delivery_timestamp: UNIX timestamp (UTC seconds)
        topic: topic for channel messages
        read_by_sender: whether sender marks as read
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/scheduled_messages"
    data = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp
    }
    if topic is not None:
        data["topic"] = topic
    if read_by_sender is not None:
        data["read_by_sender"] = read_by_sender
    try:
        resp = requests.post(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), data=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_scheduled_messages() -> Dict[str, Any]:
    """
    Fetch all scheduled messages for the current user.
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/scheduled_messages"
    try:
        resp = requests.get(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """
    Delete (cancel) a scheduled message by ID.
    Args:
        scheduled_message_id: ID of the scheduled message
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/scheduled_messages/{scheduled_message_id}"
    try:
        resp = requests.delete(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def update_scheduled_message(scheduled_message_id: int, type: str = None, to=None, content: str = None, scheduled_delivery_timestamp: int = None, topic: str = None) -> Dict[str, Any]:
    """
    Edit an existing scheduled message.
    Args:
        scheduled_message_id: ID of the scheduled message
        type: message type
        to: channel id or list of user ids
        content: new content
        scheduled_delivery_timestamp: new UNIX timestamp
        topic: new topic
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/scheduled_messages/{scheduled_message_id}"
    data = {}
    if type is not None:
        data["type"] = type
    if to is not None:
        data["to"] = to
    if content is not None:
        data["content"] = content
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    if topic is not None:
        data["topic"] = topic
    try:
        resp = requests.patch(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), data=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
