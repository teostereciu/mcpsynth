import os
import requests

BASE_URL = os.environ.get("ZULIP_SITE", "") + "/api/v1"
AUTH = (os.environ.get("ZULIP_EMAIL"), os.environ.get("ZULIP_API_KEY"))


def send_message(type: str, to, content: str, topic: str = None, queue_id: str = None, local_id: str = None, read_by_sender: bool = None):
    """Send a channel or direct message."""
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
        data["read_by_sender"] = str(read_by_sender).lower()

    try:
        response = requests.post(url, auth=AUTH, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            return response.json()
        except Exception:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def get_messages(anchor=None, include_anchor=True, anchor_date=None, num_before=None, num_after=None, narrow=None, client_gravatar=True, apply_markdown=True, message_ids=None, allow_empty_topic_name=False, use_first_unread_anchor=False):
    """Fetch messages matching a narrow filter."""
    url = f"{BASE_URL}/messages"
    params = {}
    if anchor is not None:
        params["anchor"] = anchor
    params["include_anchor"] = str(include_anchor).lower()
    if anchor_date is not None:
        params["anchor_date"] = anchor_date
    if num_before is not None:
        params["num_before"] = num_before
    if num_after is not None:
        params["num_after"] = num_after
    if narrow is not None:
        import json
        params["narrow"] = json.dumps(narrow)
    params["client_gravatar"] = str(client_gravatar).lower()
    params["apply_markdown"] = str(apply_markdown).lower()
    if message_ids is not None:
        import json
        params["message_ids"] = json.dumps(message_ids)
    params["allow_empty_topic_name"] = str(allow_empty_topic_name).lower()
    params["use_first_unread_anchor"] = str(use_first_unread_anchor).lower()

    try:
        response = requests.get(url, auth=AUTH, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            return response.json()
        except Exception:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def delete_message(message_id: int):
    """Permanently delete a message by ID."""
    url = f"{BASE_URL}/messages/{message_id}"
    try:
        response = requests.delete(url, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            return response.json()
        except Exception:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def list_tools():
    return ["send_message", "get_messages", "delete_message"]
