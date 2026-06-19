import json as _json
from typing import Any, Dict, List, Optional

from .client import ZulipClient


def get_drafts() -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("GET", "/drafts")


def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    c = ZulipClient()
    data = {"drafts": _json.dumps(drafts)}
    return c.request("POST", "/drafts", data=data)


def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    c = ZulipClient()
    data = {"draft": _json.dumps(draft)}
    return c.request("PATCH", f"/drafts/{draft_id}", data=data)


def delete_draft(draft_id: int) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("DELETE", f"/drafts/{draft_id}")
