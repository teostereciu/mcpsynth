from typing import Any, Dict, Optional

from .notion_client import NotionClient


def comments_list(*, block_id: Optional[str] = None, page_id: Optional[str] = None,
                  start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                  notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """GET /comments

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
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("GET", "/comments", params=params)


def comments_create(parent: Dict[str, Any], rich_text: list, *, notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """POST /comments"""
    body = {"parent": parent, "rich_text": rich_text}
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("POST", "/comments", json_body=body)
