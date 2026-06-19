from typing import Any, Dict, Optional

from .notion_client import NotionClient


def comments_create(
    *,
    parent: Optional[Dict[str, Any]] = None,
    discussion_id: Optional[str] = None,
    rich_text: Optional[list] = None,
    notion_version: str = "2022-06-28",
) -> Any:
    client = NotionClient(notion_version=notion_version)
    body: Dict[str, Any] = {}
    if parent is not None:
        body["parent"] = parent
    if discussion_id is not None:
        body["discussion_id"] = discussion_id
    if rich_text is not None:
        body["rich_text"] = rich_text
    return client.request("POST", "/comments", json=body)


def comments_list(
    *,
    block_id: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str = "2022-06-28",
) -> Any:
    client = NotionClient(notion_version=notion_version)
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/comments", params=params)
