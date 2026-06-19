from typing import Any, Dict, List, Optional

from .notion_client import NotionClient, omit_none


def comments_create(
    *,
    parent: Dict[str, Any],
    rich_text: List[Dict[str, Any]],
    attachments: Optional[List[Dict[str, Any]]] = None,
    display_name: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /comments

    Source: docs/create-a-comment.md
    """
    body = omit_none(
        {
            "parent": parent,
            "rich_text": rich_text,
            "attachments": attachments,
            "display_name": display_name,
        }
    )
    return NotionClient().request("POST", "/comments", json=body)


def comments_list(
    *,
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /comments

    Source: docs/list-comments.md
    """
    params = omit_none(
        {"block_id": block_id, "start_cursor": start_cursor, "page_size": page_size}
    )
    return NotionClient().request("GET", "/comments", params=params)


def comments_retrieve(*, comment_id: str) -> Dict[str, Any]:
    """GET /comments/{comment_id}

    Source: docs/retrieve-comment.md
    """
    return NotionClient().request("GET", f"/comments/{comment_id}")
