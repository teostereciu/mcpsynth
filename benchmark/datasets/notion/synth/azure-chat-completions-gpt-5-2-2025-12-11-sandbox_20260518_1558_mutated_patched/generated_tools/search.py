from typing import Any, Dict, Optional

from .http_client import request_json


def search(*, query: Optional[str] = None, query_filter: Optional[Dict[str, Any]] = None, sort: Optional[Dict[str, Any]] = None,
           start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """POST /search"""
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if query_filter is not None:
        body["filter"] = query_filter
    if sort is not None:
        body["sort"] = sort
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return request_json("POST", "/search", json_body=body)
