from typing import Any, Dict, Optional

from generated_tools.notion_client import client


def create_comment(rich_text: list, parent: Optional[Dict[str, Any]] = None, discussion_id: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"rich_text": rich_text}
    if parent is not None:
        body["parent"] = parent
    if discussion_id is not None:
        body["discussion_id"] = discussion_id
    return client.request("POST", "/comments", json_body=body)


def list_comments(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {"block_id": block_id}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/comments", params=params)
