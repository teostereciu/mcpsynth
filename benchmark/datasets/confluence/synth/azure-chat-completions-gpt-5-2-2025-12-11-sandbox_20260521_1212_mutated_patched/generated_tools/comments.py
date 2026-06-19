from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_page_footer_comments(
    page_id: int,
    cursor: Optional[str] = None,
    max_results: int = 25,
    body_format: Optional[str] = None,
    content_status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}/footer-comments"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if cursor is not None:
        params["cursor"] = cursor
    if body_format is not None:
        params["body-format"] = body_format
    if content_status is not None:
        params["status"] = content_status
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/footer-comments", params=params)


def list_page_inline_comments(
    page_id: int,
    cursor: Optional[str] = None,
    max_results: int = 25,
    body_format: Optional[str] = None,
    content_status: Optional[list[str]] = None,
    resolution_status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}/inline-comments"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if cursor is not None:
        params["cursor"] = cursor
    if body_format is not None:
        params["body-format"] = body_format
    if content_status is not None:
        params["status"] = content_status
    if resolution_status is not None:
        params["resolution-status"] = resolution_status
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/inline-comments", params=params)


def create_footer_comment(
    body_representation: str,
    body_value: str,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    attachment_id: Optional[str] = None,
    custom_content_id: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /api/v2/footer-comments"""
    client = ConfluenceClient()
    payload: Dict[str, Any] = {
        "body": {"representation": body_representation, "value": body_value}
    }
    if page_id is not None:
        payload["pageId"] = page_id
    if blog_post_id is not None:
        payload["blogPostId"] = blog_post_id
    if parent_comment_id is not None:
        payload["parentCommentId"] = parent_comment_id
    if attachment_id is not None:
        payload["attachmentId"] = attachment_id
    if custom_content_id is not None:
        payload["customContentId"] = custom_content_id
    return client.request("POST", "/api/v2/footer-comments", json=payload)


def create_inline_comment(
    body_representation: str,
    body_value: str,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    inline_marker_ref: Optional[str] = None,
    inline_original_selection: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /api/v2/inline-comments"""
    client = ConfluenceClient()
    payload: Dict[str, Any] = {
        "body": {"representation": body_representation, "value": body_value}
    }
    if page_id is not None:
        payload["pageId"] = page_id
    if blog_post_id is not None:
        payload["blogPostId"] = blog_post_id
    if parent_comment_id is not None:
        payload["parentCommentId"] = parent_comment_id
    if inline_marker_ref is not None or inline_original_selection is not None:
        payload["properties"] = {}
        if inline_marker_ref is not None:
            payload["properties"]["inlineMarkerRef"] = inline_marker_ref
        if inline_original_selection is not None:
            payload["properties"]["inlineOriginalSelection"] = inline_original_selection
    return client.request("POST", "/api/v2/inline-comments", json=payload)
