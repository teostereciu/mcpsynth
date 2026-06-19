from typing import Any, Dict
from .notion_client import NotionClient

client = NotionClient()


def create_comment(parent: Dict[str, Any], rich_text: Any) -> Dict[str, Any]:
    return client.request("POST", "/comments", json={"parent": parent, "rich_text": rich_text})


def list_comments(block_id: str = None, page_id: str = None, start_cursor: Any = None, page_size: Any = None) -> Dict[str, Any]:
    params = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_id is not None:
        params["page_id"] = page_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/comments", params=params or None)


def retrieve_comment(comment_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/comments/{comment_id}")
