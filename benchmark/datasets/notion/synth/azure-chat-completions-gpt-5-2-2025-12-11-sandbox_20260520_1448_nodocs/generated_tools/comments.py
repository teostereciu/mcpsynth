from typing import Any, Dict, Optional

from notion_client import NotionClient


def comments_create(parent: Dict[str, Any], rich_text: list) -> Any:
    """POST /comments"""
    client = NotionClient()
    body = {"parent": parent, "rich_text": rich_text}
    return client.request("POST", "/comments", json=body)


def comments_list(*, block_id: Optional[str] = None, page_id: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """GET /comments"""
    client = NotionClient()
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_id is not None:
        params["page_id"] = page_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/comments", params=params or None)
