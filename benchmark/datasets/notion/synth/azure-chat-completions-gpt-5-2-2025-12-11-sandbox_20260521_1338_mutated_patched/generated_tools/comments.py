from typing import Any, Dict, List, Optional

from .notion_client import request_json


def comments_create(parent: Dict[str, Any], rich_text: List[Dict[str, Any]], *, attachments: Optional[List[Dict[str, Any]]] = None,
                    display_name: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/comments

    Doc: docs/create-a-comment.md
    """
    body: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    if attachments is not None:
        body["attachments"] = attachments
    if display_name is not None:
        body["display_name"] = display_name
    return request_json("POST", "/comments", json=body)


def comments_retrieve(comment_id: str) -> Dict[str, Any]:
    """GET /v1/comments/{comment_id}

    Doc: docs/retrieve-comment.md
    """
    return request_json("GET", f"/comments/{comment_id}")


def comments_list(*, block_id: Optional[str] = None, page_id: Optional[str] = None,
                  page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /v1/comments

    Doc: docs/list-comments.md

    Provide either block_id or page_id.
    """
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_id is not None:
        params["page_id"] = page_id
    if page_cursor is not None:
        params["start_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return request_json("GET", "/comments", params=params)
