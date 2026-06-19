from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def list_page_footer_comments(
    page_id: int,
    *,
    cursor: Optional[str] = None,
    max_results: int = 25,
    body_format: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}/footer-comments"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    if body_format:
        params["body-format"] = body_format
    status, body, headers = c.request("GET", f"/api/v2/pages/{page_id}/footer-comments", params=params)
    return ok_or_error(status, body, headers)


def list_page_inline_comments(
    page_id: int,
    *,
    cursor: Optional[str] = None,
    max_results: int = 25,
    body_format: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}/inline-comments"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    if body_format:
        params["body-format"] = body_format
    status, body, headers = c.request("GET", f"/api/v2/pages/{page_id}/inline-comments", params=params)
    return ok_or_error(status, body, headers)


def create_footer_comment(
    *,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    attachment_id: Optional[str] = None,
    custom_content_id: Optional[str] = None,
    body_storage_value: str,
    content_status: str = "current",
) -> Dict[str, Any]:
    """POST /api/v2/footer-comments"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {
        "content_status": content_status,
        "body": {"representation": "storage", "value": body_storage_value},
    }
    if page_id:
        payload["pageId"] = page_id
    if blog_post_id:
        payload["blogPostId"] = blog_post_id
    if parent_comment_id:
        payload["parentCommentId"] = parent_comment_id
    if attachment_id:
        payload["attachmentId"] = attachment_id
    if custom_content_id:
        payload["customContentId"] = custom_content_id

    status, body, headers = c.request("POST", "/api/v2/footer-comments", json_body=payload)
    return ok_or_error(status, body, headers)
