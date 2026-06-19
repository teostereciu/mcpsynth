from typing import Any, Dict, Optional

from .client import notion_request


def create_comment(
    parent: Dict[str, Any],
    rich_text: list,
    *,
    attachments: Optional[list] = None,
    display_name: Optional[str] = None,
    show_child_attributes: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /v1/comments"""
    body: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    if attachments is not None:
        body["attachments"] = attachments
    if display_name is not None:
        body["display_name"] = display_name

    params: Dict[str, Any] = {}
    if show_child_attributes is not None:
        params["show_child_attributes"] = str(show_child_attributes).lower()

    return notion_request("POST", "/comments", params=params or None, json_body=body)


def retrieve_comment(comment_id: str) -> Dict[str, Any]:
    """GET /v1/comments/{comment_id}"""
    return notion_request("GET", f"/comments/{comment_id}")


def list_comments(
    *,
    block_id: Optional[str] = None,
    page_id: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/comments

    Provide either block_id or page_id.
    """
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_id is not None:
        params["page_id"] = page_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", "/comments", params=params or None)
