from typing import Any, Dict, Optional, List

from .http_client import ConfluenceClient


def list_page_footer_comments(
    *,
    page_id: int,
    body_format: Optional[str] = None,
    status: Optional[List[str]] = None,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = 25,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}/footer-comments"""
    params: Dict[str, Any] = {}
    if body_format is not None:
        params["body-format"] = body_format
    if status:
        params["status"] = status
    if sort is not None:
        params["sort"] = sort
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    return ConfluenceClient().request("GET", f"/api/v2/pages/{page_id}/footer-comments", params=params)  # type: ignore[return-value]


def list_page_inline_comments(
    *,
    page_id: int,
    body_format: Optional[str] = None,
    status: Optional[List[str]] = None,
    resolution_status: Optional[List[str]] = None,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = 25,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}/inline-comments"""
    params: Dict[str, Any] = {}
    if body_format is not None:
        params["body-format"] = body_format
    if status:
        params["status"] = status
    if resolution_status:
        params["resolution-status"] = resolution_status
    if sort is not None:
        params["sort"] = sort
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    return ConfluenceClient().request("GET", f"/api/v2/pages/{page_id}/inline-comments", params=params)  # type: ignore[return-value]


def create_footer_comment(
    *,
    body_representation: str,
    body_value: str,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    attachment_id: Optional[str] = None,
    custom_content_id: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /wiki/api/v2/footer-comments"""
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

    return ConfluenceClient().request("POST", "/api/v2/footer-comments", json=payload)  # type: ignore[return-value]


def create_inline_comment(
    *,
    body_representation: str,
    body_value: str,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    inline_marker_ref: Optional[str] = None,
    inline_original_selection: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /wiki/api/v2/inline-comments"""
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

    return ConfluenceClient().request("POST", "/api/v2/inline-comments", json=payload)  # type: ignore[return-value]
