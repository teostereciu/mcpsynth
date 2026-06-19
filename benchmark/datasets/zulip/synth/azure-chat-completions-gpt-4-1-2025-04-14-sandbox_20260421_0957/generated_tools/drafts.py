import os
import requests
from typing import Any, Dict, List

ZULIP_SITE = os.environ.get("ZULIP_SITE")
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
BASE_URL = f"{ZULIP_SITE}/api/v1"

def get_drafts() -> Dict[str, Any]:
    """
    Fetch all drafts for the current user.
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/drafts"
    try:
        resp = requests.get(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    """
    Edit a draft on the server.
    Args:
        draft_id: ID of the draft to edit
        draft: dict representing the draft (type, to, topic, content, timestamp)
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/drafts/{draft_id}"
    data = {"draft": draft}
    try:
        resp = requests.patch(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def delete_draft(draft_id: int) -> Dict[str, Any]:
    """
    Delete a single draft from the server.
    Args:
        draft_id: ID of the draft to delete
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/drafts/{draft_id}"
    try:
        resp = requests.delete(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create one or more drafts on the server.
    Args:
        drafts: list of draft dicts (type, to, topic, content, timestamp)
    Returns:
        JSON response from Zulip API
    """
    url = f"{BASE_URL}/drafts"
    data = {"drafts": drafts}
    try:
        resp = requests.post(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
