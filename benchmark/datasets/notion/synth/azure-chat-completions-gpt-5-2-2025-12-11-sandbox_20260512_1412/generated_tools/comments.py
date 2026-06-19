from typing import Any, Dict, List, Optional

from ._client import request_json


def comments_create(parent: Dict[str, Any], rich_text: List[Dict[str, Any]], *, discussion_id: Optional[str] = None) -> Any:
    """POST /v1/comments"""
    body: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    if discussion_id is not None:
        body["discussion_id"] = discussion_id
    return request_json("POST", "/comments", json_body=body)


def comments_retrieve(comment_id: str) -> Any:
    """GET /v1/comments/{comment_id}"""
    return request_json("GET", f"/comments/{comment_id}")


def comments_list(*, block_id: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """GET /v1/comments"""
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/comments", params=params)
