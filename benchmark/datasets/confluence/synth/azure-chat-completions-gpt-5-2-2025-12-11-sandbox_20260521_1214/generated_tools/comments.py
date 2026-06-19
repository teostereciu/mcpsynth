from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_page_footer_comments(
    *,
    page_id: int,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
    status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}/footer-comments"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if body_format:
        params["body-format"] = body_format
    if status:
        params["status"] = status
    if sort:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/footer-comments", params=params)


def list_page_inline_comments(
    *,
    page_id: int,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
    status: Optional[list[str]] = None,
    resolution_status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}/inline-comments"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if body_format:
        params["body-format"] = body_format
    if status:
        params["status"] = status
    if resolution_status:
        params["resolution-status"] = resolution_status
    if sort:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/inline-comments", params=params)


def create_footer_comment(
    *,
    body_value: str,
    body_representation: str = "storage",
    page_id: Optional[int] = None,
    blog_post_id: Optional[int] = None,
    parent_comment_id: Optional[str] = None,
    attachment_id: Optional[str] = None,
    custom_content_id: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /wiki/api/v2/footer-comments"""
    client = ConfluenceClient.from_env()
    body: Dict[str, Any] = {
        "body": {"representation": body_representation, "value": body_value}
    }
    if page_id is not None:
        body["pageId"] = str(page_id)
    if blog_post_id is not None:
        body["blogPostId"] = str(blog_post_id)
    if parent_comment_id is not None:
        body["parentCommentId"] = str(parent_comment_id)
    if attachment_id is not None:
        body["attachmentId"] = str(attachment_id)
    if custom_content_id is not None:
        body["customContentId"] = str(custom_content_id)

    return client.request(
        "POST",
        "/api/v2/footer-comments",
        json_body=body,
        content_type="application/json",
    )
