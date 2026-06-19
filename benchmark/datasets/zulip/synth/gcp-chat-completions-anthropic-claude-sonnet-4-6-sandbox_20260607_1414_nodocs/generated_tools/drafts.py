"""
Zulip MCP Tools — Drafts domain
Covers: create, list, edit, delete drafts
"""

from typing import Optional
from .client import zulip_get, zulip_post, zulip_patch, zulip_delete


def get_drafts() -> dict:
    """Get all drafts saved by the current user."""
    return zulip_get("/drafts")


def create_drafts(drafts: str) -> dict:
    """Create one or more message drafts.

    Args:
        drafts: JSON-encoded list of draft objects. Each draft object must have:
                - "type": "stream" or "private"
                - "to": list of stream IDs (stream) or user IDs (private)
                - "topic": topic string (stream drafts)
                - "content": Markdown content of the draft
                - "timestamp": (optional) Unix timestamp
                Example:
                '[{"type":"stream","to":[1],"topic":"hello","content":"Draft text"}]'
    """
    return zulip_post("/drafts", {"drafts": drafts})


def edit_draft(draft_id: int, draft: str) -> dict:
    """Edit an existing draft.

    Args:
        draft_id: The ID of the draft to edit.
        draft: JSON-encoded draft object with updated fields. Must include:
               - "type": "stream" or "private"
               - "to": list of stream IDs or user IDs
               - "topic": topic string (stream drafts)
               - "content": Markdown content
               Example:
               '{"type":"stream","to":[1],"topic":"updated","content":"New content"}'
    """
    return zulip_patch(f"/drafts/{draft_id}", {"draft": draft})


def delete_draft(draft_id: int) -> dict:
    """Delete a draft.

    Args:
        draft_id: The ID of the draft to delete.
    """
    return zulip_delete(f"/drafts/{draft_id}")
