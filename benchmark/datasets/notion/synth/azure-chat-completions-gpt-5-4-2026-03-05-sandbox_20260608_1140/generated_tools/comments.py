from typing import Any, Dict, List, Optional

from generated_tools.common import notion_request


def create_comment(parent: Dict[str, Any], rich_text: List[Dict[str, Any]], attachments: Optional[List[Dict[str, Any]]] = None, display_name: Optional[str] = None, discussion_id: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent, "rich_text": rich_text}
    if attachments is not None:
        body["attachments"] = attachments
    if display_name is not None:
        body["display_name"] = display_name
    if discussion_id is not None:
        body["discussion_id"] = discussion_id
    return notion_request("POST", "/comments", json_body=body)


def retrieve_comment(comment_id: str) -> Any:
    return notion_request("GET", f"/comments/{comment_id}")


def list_comments(block_id: Optional[str] = None, page_id: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_id is not None:
        params["page_id"] = page_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", "/comments", params=params or None)
