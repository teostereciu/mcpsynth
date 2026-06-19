from typing import Any, Dict, Optional

from .notion_client import NotionClient


def search(
    *,
    query: Optional[str] = None,
    sort: Optional[Dict[str, Any]] = None,
    filter: Optional[Dict[str, Any]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str = "2022-06-28",
) -> Any:
    """POST /search"""
    client = NotionClient(notion_version=notion_version)
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if sort is not None:
        body["sort"] = sort
    if filter is not None:
        body["filter"] = filter
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return client.request("POST", "/search", json=body)
