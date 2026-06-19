import json
from typing import Any, Dict, List, Optional

from .client import ZulipClient


def get_drafts() -> Dict[str, Any]:
    """GET /drafts"""
    return ZulipClient().request("GET", "/drafts")


def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """POST /drafts"""
    return ZulipClient().request("POST", "/drafts", data={"drafts": json.dumps(drafts)})


def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /drafts/{draft_id}"""
    return ZulipClient().request("PATCH", f"/drafts/{draft_id}", data={"draft": json.dumps(draft)})


def delete_draft(draft_id: int) -> Dict[str, Any]:
    """DELETE /drafts/{draft_id}"""
    return ZulipClient().request("DELETE", f"/drafts/{draft_id}")
