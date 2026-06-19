

def get_messages(
    num_before: int,
    num_after: int,
    anchor: Optional[Union[int, str]] = None,
    narrow: Optional[List[dict]] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    use_first_unread_anchor: Optional[bool] = None,
) -> dict:
    """
    Fetch messages.
    """
    if ZULIP_EMAIL is None or ZULIP_API_KEY is None or ZULIP_SITE is None:
        return {"error": "ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set."}

    base_url = f"{ZULIP_SITE}/api/v1"

    params = {
        "num_before": num_before,
        "num_after": num_after,
    }
    if anchor is not None:
        params["anchor"] = anchor
    if narrow is not None:
        params["narrow"] = narrow
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if apply_markdown is not None:
        params["apply_markdown"] = apply_markdown
    if use_first_unread_anchor is not None:
        params["use_first_unread_anchor"] = use_first_unread_anchor

    response = requests.get(
        f"{base_url}/messages",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        params=params,
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}


def get_message(message_id: int, apply_markdown: Optional[bool] = None) -> dict:
    """
    Fetch a single message.
    """
    if ZULIP_EMAIL is None or ZULIP_API_KEY is None or ZULIP_SITE is None:
        return {"error": "ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set."}

    base_url = f"{ZULIP_SITE}/api/v1"

    params = {}
    if apply_markdown is not None:
        params["apply_markdown"] = apply_markdown

    response = requests.get(
        f"{base_url}/messages/{message_id}",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        params=params,
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}


def update_message(
    message_id: int,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    content: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> dict:
    """
    Edit a message.
    """
    if ZULIP_EMAIL is None or ZULIP_API_KEY is None or ZULIP_SITE is None:
        return {"error": "ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set."}

    base_url = f"{ZULIP_SITE}/api/v1"

    data = {}
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = send_notification_to_old_thread
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = send_notification_to_new_thread
    if content is not None:
        data["content"] = content
    if stream_id is not None:
        data["stream_id"] = stream_id

    response = requests.patch(
        f"{base_url}/messages/{message_id}",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        json=data,
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}


def delete_message(message_id: int) -> dict:
    """
    Permanently delete a message.
    """
    if ZULIP_EMAIL is None or ZULIP_API_KEY is None or ZULIP_SITE is None:
        return {"error": "ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set."}

    base_url = f"{ZULIP_SITE}/api/v1"

    response = requests.delete(
        f"{base_url}/messages/{message_id}",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

import os
import requests
from typing import Union, List, Optional

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

def send_message(
    type: str,
    to: Union[str, List[int]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> dict:
    """
    Send a message to a stream or a private message to a user.
    """
    
    if ZULIP_EMAIL is None or ZULIP_API_KEY is None or ZULIP_SITE is None:
        return {"error": "ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set."}

    base_url = f"{ZULIP_SITE}/api/v1"
    
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

    response = requests.post(
        f"{base_url}/messages",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        json=data,
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
