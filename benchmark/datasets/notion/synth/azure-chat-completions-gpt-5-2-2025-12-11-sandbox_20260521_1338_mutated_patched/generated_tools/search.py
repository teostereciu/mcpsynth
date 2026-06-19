from typing import Any, Dict, Optional

from .notion_client import request_json


def search(query: Optional[str] = None, *, query_filter: Optional[Dict[str, Any]] = None,
           sort: Optional[Dict[str, Any]] = None, page_cursor: Optional[str] = None,
           results_per_page: Optional[int] = None) -> Dict[str, Any]:
    """POST /v1/search

    Doc: docs/post-search.md
    """
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if query_filter is not None:
        body["filter"] = query_filter
    if sort is not None:
        body["sort"] = sort
    if page_cursor is not None:
        body["start_cursor"] = page_cursor
    if results_per_page is not None:
        body["page_size"] = results_per_page
    return request_json("POST", "/search", json=body)
