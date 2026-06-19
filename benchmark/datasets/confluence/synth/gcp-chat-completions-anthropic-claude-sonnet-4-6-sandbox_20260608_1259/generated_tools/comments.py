"""
Confluence Cloud v2 API — Comments tools (footer and inline).
"""
import os
import requests
from typing import Optional

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

def _auth():
    return (EMAIL, API_TOKEN)

def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"

def _handle(resp: requests.Response):
    if resp.status_code in (200, 201):
        try:
            return resp.json()
        except Exception:
            return {"status": resp.status_code}
    if resp.status_code == 204:
        return {"status": "deleted"}
    try:
        return {"error": resp.json()}
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}


# ── Footer Comments ──────────────────────────────────────────────────────────

def get_footer_comments(
    body_format: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get all footer comments (v2).
    body_format: 'storage' | 'atlas_doc_format' | 'view'.
    """
    params: dict = {"limit": limit}
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2("/footer-comments"), params=params, auth=_auth())
    return _handle(resp)


def get_page_footer_comments(
    page_id: str,
    body_format: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get footer comments for a specific page (v2).
    """
    params: dict = {"limit": limit}
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/footer-comments"), params=params, auth=_auth())
    return _handle(resp)


def get_page_inline_comments(
    page_id: str,
    body_format: Optional[str] = None,
    resolution_status: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get inline comments for a specific page (v2).
    resolution_status: 'open' | 'resolved'.
    """
    params: dict = {"limit": limit}
    if body_format:
        params["body-format"] = body_format
    if resolution_status:
        params["resolution-status"] = resolution_status
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/inline-comments"), params=params, auth=_auth())
    return _handle(resp)


def get_blog_post_footer_comments(
    blog_post_id: str,
    body_format: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get footer comments for a specific blog post (v2).
    """
    params: dict = {"limit": limit}
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/blogposts/{blog_post_id}/footer-comments"), params=params, auth=_auth())
    return _handle(resp)


def get_blog_post_inline_comments(
    blog_post_id: str,
    body_format: Optional[str] = None,
    resolution_status: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get inline comments for a specific blog post (v2).
    resolution_status: 'open' | 'resolved'.
    """
    params: dict = {"limit": limit}
    if body_format:
        params["body-format"] = body_format
    if resolution_status:
        params["resolution-status"] = resolution_status
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/blogposts/{blog_post_id}/inline-comments"), params=params, auth=_auth())
    return _handle(resp)


def create_footer_comment(
    body_value: str,
    body_representation: str = "storage",
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    attachment_id: Optional[str] = None,
) -> dict:
    """
    Create a footer comment (v2).
    Specify one of: page_id, blog_post_id, parent_comment_id, or attachment_id.
    body_representation: 'storage' | 'atlas_doc_format'.
    """
    payload: dict = {
        "body": {
            "representation": body_representation,
            "value": body_value,
        }
    }
    if page_id:
        payload["pageId"] = page_id
    if blog_post_id:
        payload["blogPostId"] = blog_post_id
    if parent_comment_id:
        payload["parentCommentId"] = parent_comment_id
    if attachment_id:
        payload["attachmentId"] = attachment_id
    resp = requests.post(_v2("/footer-comments"), json=payload, auth=_auth())
    return _handle(resp)


def get_footer_comment_by_id(
    comment_id: str,
    body_format: Optional[str] = "storage",
    version: Optional[int] = None,
) -> dict:
    """
    Get a specific footer comment by ID (v2).
    """
    params: dict = {}
    if body_format:
        params["body-format"] = body_format
    if version is not None:
        params["version"] = version
    resp = requests.get(_v2(f"/footer-comments/{comment_id}"), params=params, auth=_auth())
    return _handle(resp)


def update_footer_comment(
    comment_id: str,
    body_value: str,
    version_number: int,
    body_representation: str = "storage",
    version_message: Optional[str] = None,
) -> dict:
    """
    Update a footer comment by ID (v2). version_number must be current + 1.
    """
    payload: dict = {
        "version": {"number": version_number},
        "body": {
            "representation": body_representation,
            "value": body_value,
        },
    }
    if version_message:
        payload["version"]["message"] = version_message
    resp = requests.put(_v2(f"/footer-comments/{comment_id}"), json=payload, auth=_auth())
    return _handle(resp)


def delete_footer_comment(comment_id: str) -> dict:
    """
    Delete a footer comment by ID (v2).
    """
    resp = requests.delete(_v2(f"/footer-comments/{comment_id}"), auth=_auth())
    return _handle(resp)


# ── Inline Comments ──────────────────────────────────────────────────────────

def get_inline_comments(
    body_format: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get all inline comments (v2).
    """
    params: dict = {"limit": limit}
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2("/inline-comments"), params=params, auth=_auth())
    return _handle(resp)


def create_inline_comment(
    body_value: str,
    body_representation: str = "storage",
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    inline_marker_ref: Optional[str] = None,
    inline_original_selection: Optional[str] = None,
) -> dict:
    """
    Create an inline comment (v2).
    Specify page_id or blog_post_id. Optionally provide inline marker details.
    """
    payload: dict = {
        "body": {
            "representation": body_representation,
            "value": body_value,
        }
    }
    if page_id:
        payload["pageId"] = page_id
    if blog_post_id:
        payload["blogPostId"] = blog_post_id
    if parent_comment_id:
        payload["parentCommentId"] = parent_comment_id
    if inline_marker_ref or inline_original_selection:
        payload["inlineCommentProperties"] = {}
        if inline_marker_ref:
            payload["inlineCommentProperties"]["inlineMarkerRef"] = inline_marker_ref
        if inline_original_selection:
            payload["inlineCommentProperties"]["inlineOriginalSelection"] = inline_original_selection
    resp = requests.post(_v2("/inline-comments"), json=payload, auth=_auth())
    return _handle(resp)


def get_inline_comment_by_id(
    comment_id: str,
    body_format: Optional[str] = "storage",
    version: Optional[int] = None,
) -> dict:
    """
    Get a specific inline comment by ID (v2).
    """
    params: dict = {}
    if body_format:
        params["body-format"] = body_format
    if version is not None:
        params["version"] = version
    resp = requests.get(_v2(f"/inline-comments/{comment_id}"), params=params, auth=_auth())
    return _handle(resp)


def update_inline_comment(
    comment_id: str,
    body_value: str,
    version_number: int,
    body_representation: str = "storage",
    resolution_status: Optional[str] = None,
) -> dict:
    """
    Update an inline comment by ID (v2). version_number must be current + 1.
    resolution_status: 'open' | 'resolved'.
    """
    payload: dict = {
        "version": {"number": version_number},
        "body": {
            "representation": body_representation,
            "value": body_value,
        },
    }
    if resolution_status:
        payload["resolutionStatus"] = resolution_status
    resp = requests.put(_v2(f"/inline-comments/{comment_id}"), json=payload, auth=_auth())
    return _handle(resp)


def delete_inline_comment(comment_id: str) -> dict:
    """
    Delete an inline comment by ID (v2).
    """
    resp = requests.delete(_v2(f"/inline-comments/{comment_id}"), auth=_auth())
    return _handle(resp)
