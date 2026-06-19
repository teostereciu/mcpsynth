from typing import Any, Dict, List

from ._client import ZulipClient, dumps_narrow


def get_drafts() -> Dict[str, Any]:
    """GET /drafts"""
    return ZulipClient().request("GET", "/drafts")


def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """POST /drafts"""
    data = {"drafts": dumps_narrow(drafts)}
    return ZulipClient().request("POST", "/drafts", data=data)


def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /drafts/{draft_id}"""
    data = {"draft": dumps_narrow(draft)}
    return ZulipClient().request("PATCH", f"/drafts/{draft_id}", data=data)


def delete_draft(draft_id: int) -> Dict[str, Any]:
    """DELETE /drafts/{draft_id}"""
    return ZulipClient().request("DELETE", f"/drafts/{draft_id}")
