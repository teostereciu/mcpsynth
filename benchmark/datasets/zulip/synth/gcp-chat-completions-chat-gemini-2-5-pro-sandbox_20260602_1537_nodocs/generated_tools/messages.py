"""Tools for interacting with messages in Zulip."""

import os
import requests
from typing import Optional, List

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

def send_public_message(stream: str, topic: str, content: str) -> dict:
    """Sends a public message to a stream."""
    response = requests.post(
        f"{ZULIP_SITE}/api/v1/messages",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data={
            "type": "stream",
            "to": stream,
            "topic": topic,
            "content": content,
        },
    )
    return response.json()

def remove_reaction(message_id: int, emoji_name: str) -> dict:
    """Removes a reaction from a message."""
    response = requests.delete(
        f"{ZULIP_SITE}/api/v1/messages/{message_id}/reactions",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data={"emoji_name": emoji_name},
    )
    return response.json()

def add_reaction(message_id: int, emoji_name: str) -> dict:
    """Adds a reaction to a message."""
    response = requests.post(
        f"{ZULIP_SITE}/api/v1/messages/{message_id}/reactions",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data={"emoji_name": emoji_name},
    )
    return response.json()

def get_messages(num_before: int, num_after: int, anchor: Optional[str] = 'newest') -> dict:
    """Fetches messages from a stream."""
    response = requests.get(
        f"{ZULIP_SITE}/api/v1/messages",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        params={
            "num_before": num_before,
            "num_after": num_after,
            "anchor": anchor,
        },
    )
    return response.json()

def delete_message(message_id: int) -> dict:
    """Deletes a message."""
    response = requests.delete(
        f"{ZULIP_SITE}/api/v1/messages/{message_id}",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
    )
    return response.json()

def edit_message(message_id: int, topic: Optional[str] = None, content: Optional[str] = None) -> dict:
    """Edits a message."""
    data = {}
    if topic:
        data["topic"] = topic
    if content:
        data["content"] = content
    response = requests.patch(
        f"{ZULIP_SITE}/api/v1/messages/{message_id}",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data=data,
    )
    return response.json()

def send_private_message(to: List[str], content: str) -> dict:
    """Sends a private message to one or more users."""
    response = requests.post(
        f"{ZULIP_SITE}/api/v1/messages",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data={
            "type": "private",
            "to": ",".join(to),
            "content": content,
        },
    )
    return response.json()
