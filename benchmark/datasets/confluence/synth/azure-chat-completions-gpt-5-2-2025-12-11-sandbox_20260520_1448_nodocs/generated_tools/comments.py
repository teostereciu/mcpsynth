from typing import Any, Dict, Optional

from .http import confluence_request


def list_comments(page_id: int, limit: int = 25, start: int = 0, expand: str = "body.storage") -> Dict[str, Any]:
    params = {"limit": limit, "start": start, "expand": expand}
    return confluence_request("GET", f"/rest/api/content/{page_id}/child/comment", params=params)


def create_footer_comment(page_id: int, body: str, representation: str = "storage") -> Dict[str, Any]:
    payload = {
        "type": "comment",
        "container": {"type": "page", "id": str(page_id)},
        "body": {representation: {"value": body, "representation": representation}},
    }
    return confluence_request("POST", "/rest/api/content", json=payload)


def create_inline_comment(page_id: int, body: str, inline_original_selection: str, representation: str = "storage") -> Dict[str, Any]:
    # Inline comments require additional metadata; implement minimal v1 payload.
    payload = {
        "type": "comment",
        "container": {"type": "page", "id": str(page_id)},
        "body": {representation: {"value": body, "representation": representation}},
        "metadata": {"properties": {"inlineOriginalSelection": inline_original_selection}},
    }
    return confluence_request("POST", "/rest/api/content", json=payload)
