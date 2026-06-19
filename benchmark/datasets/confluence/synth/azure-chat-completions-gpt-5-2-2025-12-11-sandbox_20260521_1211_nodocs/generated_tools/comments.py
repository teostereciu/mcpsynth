from typing import Any, Dict, Optional

from .client import ConfluenceClient


def v1_list_page_comments(page_id: str, *, limit: int = 25, start: int = 0, expand: str = "") -> Any:
    """GET /rest/api/content/{id}/child/comment"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"limit": limit, "start": start}
    if expand:
        params["expand"] = expand
    return c.request("GET", f"/rest/api/content/{page_id}/child/comment", params=params)


def v1_create_page_comment(
    page_id: str,
    *,
    body: str,
    body_format: str = "storage",
    parent_comment_id: Optional[str] = None,
) -> Any:
    """POST /rest/api/content"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {
        "type": "comment",
        "container": {"type": "page", "id": str(page_id)},
        "body": {body_format: {"value": body, "representation": body_format}},
    }
    if parent_comment_id:
        payload["ancestors"] = [{"id": str(parent_comment_id)}]
    return c.request("POST", "/rest/api/content", json=payload, expected=(200, 201))
