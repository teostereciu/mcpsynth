from typing import Any, Dict, Optional

from .notion_client import NotionClient


def list_comments(
    *,
    block_id: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    data, err = client.request("GET", "/comments", params=params)
    return err or data  # type: ignore[return-value]


def create_comment(
    parent: Dict[str, Any],
    rich_text: list,
    *,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    payload: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    data, err = client.request("POST", "/comments", json=payload)
    return err or data  # type: ignore[return-value]
