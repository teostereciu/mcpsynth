from typing import Any, Dict, Optional

from .client import notion_request


def search(
    *,
    query: Optional[str] = None,
    filter: Optional[Dict[str, Any]] = None,
    sort: Optional[Dict[str, Any]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    show_child_attributes: Optional[bool] = None,
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

    params: Dict[str, Any] = {}
    if show_child_attributes is not None:
        params["show_child_attributes"] = str(show_child_attributes).lower()

    return notion_request("POST", "/search", params=params or None, json_body=body)
