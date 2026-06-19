import os
import requests
from typing import Any, Dict, List, Optional, Union

def zulip_auth() -> Dict[str, str]:
    return {
        "email": os.environ["ZULIP_EMAIL"],
        "api_key": os.environ["ZULIP_API_KEY"],
        "site": os.environ["ZULIP_SITE"].rstrip("/"),
    }

def create_scheduled_message(type: str, to: Union[int, List[int]], content: str, scheduled_delivery_timestamp: int, topic: Optional[str] = None, read_by_sender: Optional[bool] = None) -> Dict[str, Any]:
    """
    Schedule a message to be sent in the future.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/scheduled_messages"
    data = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        data["topic"] = topic
    if read_by_sender is not None:
        data["read_by_sender"] = read_by_sender
    resp = requests.post(url, auth=(auth["email"], auth["api_key"]), data=data)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def get_scheduled_messages() -> Dict[str, Any]:
    """
    Fetch all scheduled messages for the current user.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/scheduled_messages"
    resp = requests.get(url, auth=(auth["email"], auth["api_key"]))
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def update_scheduled_message(scheduled_message_id: int, type: Optional[str] = None, to: Optional[Union[int, List[int]]] = None, content: Optional[str] = None, topic: Optional[str] = None, scheduled_delivery_timestamp: Optional[int] = None) -> Dict[str, Any]:
    """
    Edit a scheduled message by ID.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/scheduled_messages/{scheduled_message_id}"
    data = {}
    if type is not None:
        data["type"] = type
    if to is not None:
        data["to"] = to
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    resp = requests.patch(url, auth=(auth["email"], auth["api_key"]), data=data)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """
    Delete a scheduled message by ID.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/scheduled_messages/{scheduled_message_id}"
    resp = requests.delete(url, auth=(auth["email"], auth["api_key"]))
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}
