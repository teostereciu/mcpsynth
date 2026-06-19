"""Zulip Drafts API tools."""
import json
from typing import Optional, List
from .client import zulip_request


def get_drafts() -> dict:
    """Get all drafts for the current user."""
    try:
        return zulip_request("GET", "drafts")
    except Exception as e:
        return {"error": str(e)}


def create_drafts(drafts: List[dict]) -> dict:
    """Create one or more drafts.

    Args:
        drafts: List of draft objects. Each draft should have:
            - type: '' (unaddressed), 'channel_name', or 'private'
            - to: List of channel IDs (for channel) or user IDs (for DM)
            - topic: Topic name (for channel messages)
            - content: The draft message content
            - timestamp: (optional) UNIX timestamp of last edit
    """
    try:
        return zulip_request("POST", "drafts", data={"drafts": json.dumps(drafts)})
    except Exception as e:
        return {"error": str(e)}


def edit_draft(draft_id: int, draft: dict) -> dict:
    """Edit an existing draft.

    Args:
        draft_id: The ID of the draft to edit.
        draft: Updated draft object with fields: type, to, topic, content, timestamp.
    """
    try:
        return zulip_request("PATCH", f"drafts/{draft_id}", data={"draft": json.dumps(draft)})
    except Exception as e:
        return {"error": str(e)}


def delete_draft(draft_id: int) -> dict:
    """Delete a draft.

    Args:
        draft_id: The ID of the draft to delete.
    """
    try:
        return zulip_request("DELETE", f"drafts/{draft_id}")
    except Exception as e:
        return {"error": str(e)}


def get_saved_snippets() -> dict:
    """Get all saved snippets for the current user."""
    try:
        return zulip_request("GET", "saved_snippets")
    except Exception as e:
        return {"error": str(e)}


def create_saved_snippet(title: str, content: str) -> dict:
    """Create a new saved snippet.

    Args:
        title: The title of the saved snippet.
        content: The content of the saved snippet.
    """
    try:
        return zulip_request("POST", "saved_snippets", data={"title": title, "content": content})
    except Exception as e:
        return {"error": str(e)}


def edit_saved_snippet(saved_snippet_id: int, title: Optional[str] = None, content: Optional[str] = None) -> dict:
    """Edit an existing saved snippet.

    Args:
        saved_snippet_id: The ID of the saved snippet to edit.
        title: New title for the snippet.
        content: New content for the snippet.
    """
    try:
        data: dict = {}
        if title is not None:
            data["title"] = title
        if content is not None:
            data["content"] = content
        return zulip_request("PATCH", f"saved_snippets/{saved_snippet_id}", data=data)
    except Exception as e:
        return {"error": str(e)}


def delete_saved_snippet(saved_snippet_id: int) -> dict:
    """Delete a saved snippet.

    Args:
        saved_snippet_id: The ID of the saved snippet to delete.
    """
    try:
        return zulip_request("DELETE", f"saved_snippets/{saved_snippet_id}")
    except Exception as e:
        return {"error": str(e)}
