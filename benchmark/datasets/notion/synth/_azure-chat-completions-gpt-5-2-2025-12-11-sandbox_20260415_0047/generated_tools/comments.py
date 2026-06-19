"""Tools for Notion Comments API."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import notion_request


def create_comment(
    *,
    parent: Dict[str, Any],
    rich_text: List[Dict[str, Any]],
    attachments: Optional[List[Dict[str, Any]]] = None,
    display_name: Optional[Dict[str, Any]] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """POST /v1/comments"""
    body: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    if attachments is not None:
        body["attachments"] = attachments
    if display_name is not None:
        body["display_name"] = display_name
    return notion_request("POST", "/comments", json=body, notion_version=notion_version)


def retrieve_comment(*, comment_id: str, notion_version: str | None = None) -> Dict[str, Any]:
    """GET /v1/comments/{comment_id}"""
    return notion_request("GET", f"/comments/{comment_id}", notion_version=notion_version)


def list_comments(
    *,
    block_id: Optional[str] = None,
    page_id: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """GET /v1/comments

    Notion supports listing comments by block_id or page_id.
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
    return notion_request("GET", "/comments", params=params or None, notion_version=notion_version)
