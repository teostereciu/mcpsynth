from typing import Any, Dict, Optional

from .notion_client import NotionClient


def search(
    *,
    query: Optional[str] = None,
    sort: Optional[Dict[str, Any]] = None,
    filter: Optional[Dict[str, Any]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    payload: Dict[str, Any] = {}
    if query is not None:
        payload["query"] = query
    if sort is not None:
        payload["sort"] = sort
    if filter is not None:
        payload["filter"] = filter
    if start_cursor is not None:
        payload["start_cursor"] = start_cursor
    if page_size is not None:
        payload["page_size"] = page_size
    data, err = client.request("POST", "/search", json=payload)
    return err or data  # type: ignore[return-value]
