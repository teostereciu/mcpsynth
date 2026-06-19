from typing import Any, Dict, Optional

from .notion_client import NotionClient


def comments_create(
    parent: Dict[str, Any],
    rich_text: Any,
    *,
    attachments: Optional[Any] = None,
    display_name: Optional[Any] = None,
) -> Dict[str, Any]:
    """POST /v1/comments

    Doc: docs/create-a-comment.md
    """
    body: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    if attachments is not None:
        body["attachments"] = attachments
    if display_name is not None:
        body["display_name"] = display_name
    client = NotionClient()
    return client.request("POST", "/comments", json_body=body)


def comments_retrieve(comment_id: str) -> Dict[str, Any]:
    """GET /v1/comments/{comment_id}

    Doc: docs/retrieve-comment.md
    """
    client = NotionClient()
    return client.request("GET", f"/comments/{comment_id}")


def comments_list(
    *,
    block_id: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/comments

    Doc: docs/list-comments.md
    """
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size

    client = NotionClient()
    return client.request("GET", "/comments", params=params or None)
