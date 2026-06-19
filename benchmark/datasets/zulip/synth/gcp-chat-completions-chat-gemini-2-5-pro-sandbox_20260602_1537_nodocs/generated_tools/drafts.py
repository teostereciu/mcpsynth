"""Tools for interacting with drafts in Zulip."""

import os
import requests
from typing import Optional, List

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

def create_draft(type: str, to: List[int], topic: str, content: str) -> dict:
    """Creates a draft."""
    data = {
        "type": type,
        "to": to,
        "topic": topic,
        "content": content,
    }
    response = requests.post(
        f"{ZULIP_SITE}/api/v1/drafts",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data=data,
    )
    return response.json()

def delete_draft(draft_id: int) -> dict:
    """Deletes a draft."""
    response = requests.delete(f"{ZULIP_SITE}/api/v1/drafts/{draft_id}", auth=(ZULIP_EMAIL, ZULIP_API_KEY))
    return response.json()

def edit_draft(draft_id: int, type: str, to: List[int], topic: str, content: str) -> dict:
    """Edits a draft."""
    data = {
        "type": type,
        "to": to,
        "topic": topic,
        "content": content,
    }
    response = requests.patch(
        f"{ZULIP_SITE}/api/v1/drafts/{draft_id}",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data=data,
    )
    return response.json()

def get_drafts() -> dict:
    """Gets all drafts."""
    response = requests.get(f"{ZULIP_SITE}/api/v1/drafts", auth=(ZULIP_EMAIL, ZULIP_API_KEY))
    return response.json()
