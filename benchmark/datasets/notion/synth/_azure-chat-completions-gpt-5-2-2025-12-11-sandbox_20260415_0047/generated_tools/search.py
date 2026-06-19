"""Tools for Notion Search API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import notion_request


def search(
    *,
    query: Optional[str] = None,
    filter: Optional[Dict[str, Any]] = None,
    sort: Optional[Dict[str, Any]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """POST /v1/search"""
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if filter is not None:
        body["filter"] = filter
    if sort is not None:
        body["sort"] = sort
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return notion_request("POST", "/search", json=body, notion_version=notion_version)
