import os
import requests
from mcp.tools import tool

ZULIP_SITE = os.environ["ZULIP_SITE"]
ZULIP_EMAIL = os.environ["ZULIP_EMAIL"]
ZULIP_API_KEY = os.environ["ZULIP_API_KEY"]
BASE_URL = f"{ZULIP_SITE}/api/v1"


def zulip_auth():
    return (ZULIP_EMAIL, ZULIP_API_KEY)

@tool("send_message")
def send_message(type: str, to, content: str, topic: str = None, queue_id: str = None, local_id: str = None, read_by_sender: bool = None):
    """
    Send a message (channel or direct). type: 'stream', 'channel', or 'direct'. 'to' is channel name/ID or list of user IDs/emails. 'content' is the message. 'topic' required for channel messages.
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
        resp = requests.post(url, auth=zulip_auth(), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("delete_draft")
def delete_draft(draft_id: int):
    """
    Delete a draft by ID.
    """
    url = f"{BASE_URL}/drafts/{draft_id}"
    try:
        resp = requests.delete(url, auth=zulip_auth())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("edit_draft")
def edit_draft(draft_id: int, draft: dict):
    """
    Edit a draft by ID. 'draft' is a dict as described in Zulip docs.
    """
    url = f"{BASE_URL}/drafts/{draft_id}"
    data = {"draft": draft}
    try:
        resp = requests.patch(url, auth=zulip_auth(), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("get_drafts")
def get_drafts():
    """
    Get all drafts for the current user.
    """
    url = f"{BASE_URL}/drafts"
    try:
        resp = requests.get(url, auth=zulip_auth())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("create_drafts")
def create_drafts(drafts: list):
    """
    Create one or more drafts. 'drafts' is a list of draft objects as described in Zulip docs.
    """
    url = f"{BASE_URL}/drafts"
    data = {"drafts": drafts}
    try:
        resp = requests.post(url, auth=zulip_auth(), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("delete_scheduled_message")
def delete_scheduled_message(scheduled_message_id: int):
    """
    Delete a scheduled message by ID.
    """
    url = f"{BASE_URL}/scheduled_messages/{scheduled_message_id}"
    try:
        resp = requests.delete(url, auth=zulip_auth())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("edit_scheduled_message")
def edit_scheduled_message(scheduled_message_id: int, type: str = None, to = None, content: str = None, topic: str = None, scheduled_delivery_timestamp: int = None):
    """
    Edit a scheduled message by ID. All fields are optional except scheduled_message_id. See Zulip docs for details.
    """
    url = f"{BASE_URL}/scheduled_messages/{scheduled_message_id}"
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
    try:
        resp = requests.patch(url, auth=zulip_auth(), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("get_scheduled_messages")
def get_scheduled_messages():
    """
    Get all scheduled messages for the current user.
    """
    url = f"{BASE_URL}/scheduled_messages"
    try:
        resp = requests.get(url, auth=zulip_auth())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("create_scheduled_message")
def create_scheduled_message(type: str, to, content: str, scheduled_delivery_timestamp: int, topic: str = None, read_by_sender: bool = None):
    """
    Create a scheduled message. 'type' is 'stream', 'channel', or 'direct'. 'to' is channel ID or list of user IDs. 'content' is message. 'scheduled_delivery_timestamp' is UNIX timestamp. 'topic' required for channel messages.
    """
    url = f"{BASE_URL}/scheduled_messages"
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
    try:
        resp = requests.post(url, auth=zulip_auth(), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("remove_reaction")
def remove_reaction(message_id: int, emoji_name: str = None, emoji_code: str = None, reaction_type: str = None):
    """
    Remove an emoji reaction from a message. emoji_name is optional but recommended. emoji_code and reaction_type are optional.
    """
    url = f"{BASE_URL}/messages/{message_id}/reactions"
    params = {}
    if emoji_name is not None:
        params["emoji_name"] = emoji_name
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    try:
        resp = requests.delete(url, auth=zulip_auth(), params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("add_reaction")
def add_reaction(message_id: int, emoji_name: str, emoji_code: str = None, reaction_type: str = None):
    """
    Add an emoji reaction to a message. emoji_name is required. emoji_code and reaction_type are optional.
    """
    url = f"{BASE_URL}/messages/{message_id}/reactions"
    data = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    try:
        resp = requests.post(url, auth=zulip_auth(), data=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("get_message_history")
def get_message_history(message_id: int, allow_empty_topic_name: bool = None):
    """
    Fetch the edit history of a message by ID.
    """
    url = f"{BASE_URL}/messages/{message_id}/history"
    params = {}
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = allow_empty_topic_name
    try:
        resp = requests.get(url, auth=zulip_auth(), params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("delete_message")
def delete_message(message_id: int):
    """
    Permanently delete a message by ID.
    """
    url = f"{BASE_URL}/messages/{message_id}"
    try:
        resp = requests.delete(url, auth=zulip_auth())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("get_messages")
def get_messages(anchor=None, num_before=None, num_after=None, narrow=None, client_gravatar=None, apply_markdown=None, message_ids=None, allow_empty_topic_name=None, use_first_unread_anchor=None):
    """
    Get messages. anchor: message ID or special string. num_before/num_after: number of messages before/after anchor. narrow: list of narrows. message_ids: list of IDs. See Zulip docs for details.
    """
    url = f"{BASE_URL}/messages"
    params = {}
    if anchor is not None:
        params["anchor"] = anchor
    if num_before is not None:
        params["num_before"] = num_before
    if num_after is not None:
        params["num_after"] = num_after
    if narrow is not None:
        params["narrow"] = narrow
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
        resp = requests.get(url, auth=zulip_auth(), params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool("edit_message")
def edit_message(message_id: int, content: str = None, topic: str = None, propagate_mode: str = None, send_notification_to_old_thread: bool = None, send_notification_to_new_thread: bool = None, prev_content_sha256: str = None, stream_id: int = None):
    """
    Edit a message. You can update content, topic, or channel. See Zulip docs for permissions and propagation modes.
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
        resp = requests.patch(url, auth=zulip_auth(), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
