from typing import Any, Dict, List, Optional

from .http_client import request_json


def comments_create(*, parent: Dict[str, Any], rich_text: List[Dict[str, Any]], attachments: Optional[List[Dict[str, Any]]] = None,
                    display_name: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /comments"""
    body: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    if attachments is not None:
        body["attachments"] = attachments
    if display_name is not None:
        body["display_name"] = display_name
    return request_json("POST", "/comments", json_body=body)


def comments_retrieve(comment_id: str) -> Dict[str, Any]:
    """GET /comments/{comment_id}"""
    return request_json("GET", f"/comments/{comment_id}")


def comments_list(*, block_id: Optional[str] = None, page_id: Optional[str] = None,
                  start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /comments

    Notion supports listing comments by block_id (and sometimes page_id depending on API version).
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
    return request_json("GET", "/comments", params=params or None)
