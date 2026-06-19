import json
from typing import Any, Dict, List, Optional
from generated_tools.client import client

def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create one or more drafts.
    
    Args:
        drafts: A list of draft dictionaries. Each draft should contain:
            - 'type': "stream" or "private"
            - 'to': list of user IDs (for private) or stream name/ID (for stream)
            - 'topic': topic name (required for stream)
            - 'content': content of the draft
            - 'timestamp': optional UNIX epoch timestamp
    """
    data = {
        "drafts": json.dumps(drafts),
    }
    return client.request("POST", "drafts", data=data)

def get_drafts() -> Dict[str, Any]:
    """
    Get all drafts for the current user.
    """
    return client.request("GET", "drafts")

def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    """
    Edit an existing draft.
    
    Args:
        draft_id: The ID of the draft to edit.
        draft: The updated draft dictionary containing:
            - 'type': "stream" or "private"
            - 'to': list of user IDs or stream name/ID
            - 'topic': topic name
            - 'content': content of the draft
            - 'timestamp': optional UNIX epoch timestamp
    """
    data = {
        "draft": json.dumps(draft),
    }
    return client.request("PATCH", f"drafts/{draft_id}", data=data)

def delete_draft(draft_id: int) -> Dict[str, Any]:
    """
    Delete a draft.
    
    Args:
        draft_id: The ID of the draft to delete.
    """
    return client.request("DELETE", f"drafts/{draft_id}")
