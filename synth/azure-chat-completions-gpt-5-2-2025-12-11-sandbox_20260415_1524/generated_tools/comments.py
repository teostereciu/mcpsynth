from typing import Any, Dict, Optional

from ._client import request_json


def comments_create(parent: Dict[str, Any], rich_text: list, *, discussion_id: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    if discussion_id is not None:
        body["discussion_id"] = discussion_id
    return request_json("POST", "/comments", json=body)


def comments_retrieve(comment_id: str) -> Any:
    return request_json("GET", f"/comments/{comment_id}")


def comments_list(
    *,
    block_id: Optional[str] = None,
    page_id: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_id is not None:
        params["page_id"] = page_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/comments", params=params or None)
