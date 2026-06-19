import os
import requests
from typing import Any, Dict

ZULIP_SITE = os.environ.get("ZULIP_SITE")
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
BASE_URL = f"{ZULIP_SITE}/api/v1"

def add_reaction(message_id: int, emoji_name: str, emoji_code: str = None, reaction_type: str = None) -> Dict[str, Any]:
    """
    Add an emoji reaction to a message.
    Args:
        message_id: ID of the message
        emoji_name: human-readable emoji name
        emoji_code: unique identifier for emoji (optional)
        reaction_type: type of emoji (optional)
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/messages/{message_id}/reactions"
    data = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    try:
        resp = requests.post(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), data=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def remove_reaction(message_id: int, emoji_name: str = None, emoji_code: str = None, reaction_type: str = None) -> Dict[str, Any]:
    """
    Remove an emoji reaction from a message.
    Args:
        message_id: ID of the message
        emoji_name: human-readable emoji name (optional)
        emoji_code: unique identifier for emoji (optional)
        reaction_type: type of emoji (optional)
    Returns:
        JSON response from Zulip API
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
        resp = requests.delete(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
