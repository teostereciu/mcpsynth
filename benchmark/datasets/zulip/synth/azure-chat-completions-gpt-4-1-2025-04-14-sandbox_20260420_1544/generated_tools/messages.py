import os
import requests
from typing import Any, Dict, List, Optional, Union

def zulip_auth() -> Dict[str, str]:
    return {
        "email": os.environ["ZULIP_EMAIL"],
        "api_key": os.environ["ZULIP_API_KEY"],
        "site": os.environ["ZULIP_SITE"].rstrip("/"),
    }

def send_message(type: str, to: Union[str, int, List[Union[str, int]]], content: str, topic: Optional[str] = None, queue_id: Optional[str] = None, local_id: Optional[str] = None, read_by_sender: Optional[bool] = None) -> Dict[str, Any]:
    """
    Send a channel or direct message.
    type: "stream"/"channel" or "direct"/"private"
    to: channel name/ID or list of user IDs/emails
    content: message text
    topic: topic for channel messages
    queue_id, local_id: for local echo
    read_by_sender: mark as read by sender
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/messages"
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
    resp = requests.post(url, auth=(auth["email"], auth["api_key"]), json=data)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def get_messages(anchor: Union[int, str] = "newest", num_before: int = 0, num_after: int = 100, narrow: Optional[List[Dict[str, Any]]] = None, include_anchor: Optional[bool] = None, anchor_date: Optional[str] = None, client_gravatar: Optional[bool] = None, apply_markdown: Optional[bool] = None, message_ids: Optional[List[int]] = None, allow_empty_topic_name: Optional[bool] = None) -> Dict[str, Any]:
    """
    Fetch messages using Zulip's /messages endpoint.
    anchor: message ID or "newest"/"oldest"/"first_unread"/"date"
    num_before, num_after: number of messages before/after anchor
    narrow: list of narrow filters
    message_ids: fetch specific messages
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/messages"
    params = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
    }
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
    # Convert narrow to JSON string if present
    if "narrow" in params and isinstance(params["narrow"], list):
        import json
        params["narrow"] = json.dumps(params["narrow"])
    resp = requests.get(url, auth=(auth["email"], auth["api_key"]), params=params)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def edit_message(message_id: int, topic: str = None, content: str = None, propagate_mode: str = None, send_notification_to_old_thread: bool = None, send_notification_to_new_thread: bool = None, prev_content_sha256: str = None, stream_id: int = None) -> Dict[str, Any]:
    """
    Edit a message's content, topic, or move it to another channel.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/messages/{message_id}"
    data = {}
    if topic is not None:
        data["topic"] = topic
    if content is not None:
        data["content"] = content
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
    resp = requests.patch(url, auth=(auth["email"], auth["api_key"]), data=data)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def delete_message(message_id: int) -> Dict[str, Any]:
    """
    Permanently delete a message by ID.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/messages/{message_id}"
    resp = requests.delete(url, auth=(auth["email"], auth["api_key"]))
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def get_message(message_id: int, apply_markdown: bool = True, allow_empty_topic_name: bool = False) -> Dict[str, Any]:
    """
    Fetch a single message by ID.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/messages/{message_id}"
    params = {"apply_markdown": apply_markdown, "allow_empty_topic_name": allow_empty_topic_name}
    resp = requests.get(url, auth=(auth["email"], auth["api_key"]), params=params)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def add_reaction(message_id: int, emoji_name: str, emoji_code: str = None, reaction_type: str = None) -> Dict[str, Any]:
    """
    Add an emoji reaction to a message.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/messages/{message_id}/reactions"
    data = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    resp = requests.post(url, auth=(auth["email"], auth["api_key"]), data=data)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def remove_reaction(message_id: int, emoji_name: str = None, emoji_code: str = None, reaction_type: str = None) -> Dict[str, Any]:
    """
    Remove an emoji reaction from a message.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/messages/{message_id}/reactions"
    params = {}
    if emoji_name is not None:
        params["emoji_name"] = emoji_name
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    resp = requests.delete(url, auth=(auth["email"], auth["api_key"]), params=params)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}
