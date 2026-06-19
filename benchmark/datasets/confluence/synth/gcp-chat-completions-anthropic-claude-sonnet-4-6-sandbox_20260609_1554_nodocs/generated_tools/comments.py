"""
Confluence Cloud REST API — Comments (v2 preferred)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, API_TOKEN)


def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"


def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"


def _handle(resp: requests.Response) -> dict:
    try:
        data = resp.json()
    except Exception:
        data = {"raw": resp.text}
    if not resp.ok:
        return {"error": data, "status_code": resp.status_code}
    return data


# ---------------------------------------------------------------------------
# Footer (page-level) comments
# ---------------------------------------------------------------------------

def list_page_footer_comments(
    page_id: str,
    limit: int = 25,
    cursor: str = "",
    body_format: str = "storage",
) -> dict:
    """List footer comments on a page (v2).

    Args:
        page_id: The page ID.
        limit: Maximum number of results.
        cursor: Pagination cursor.
        body_format: Body representation format ('storage', 'atlas_doc_format').
    """
    params: dict = {"limit": limit, "body-format": body_format}
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/footer-comments"), params=params, auth=_auth())
    return _handle(resp)


def create_page_footer_comment(
    page_id: str,
    body: str,
    body_format: str = "storage",
    parent_comment_id: str = "",
) -> dict:
    """Create a footer comment on a page (v2).

    Args:
        page_id: The page ID to comment on.
        body: Comment body content.
        body_format: Body representation format ('storage', 'atlas_doc_format', 'wiki').
        parent_comment_id: Optional parent comment ID for threaded replies.
    """
    payload: dict = {
        "pageId": page_id,
        "body": {
            "representation": body_format,
            "value": body,
        },
    }
    if parent_comment_id:
        payload["parentCommentId"] = parent_comment_id
    resp = requests.post(_v2("/footer-comments"), json=payload, auth=_auth())
    return _handle(resp)


def get_footer_comment_by_id(comment_id: str, body_format: str = "storage") -> dict:
    """Get a footer comment by ID (v2).

    Args:
        comment_id: The comment ID.
        body_format: Body representation format.
    """
    params = {"body-format": body_format}
    resp = requests.get(_v2(f"/footer-comments/{comment_id}"), params=params, auth=_auth())
    return _handle(resp)


def update_footer_comment(
    comment_id: str,
    body: str,
    version_number: int,
    body_format: str = "storage",
) -> dict:
    """Update a footer comment (v2).

    Args:
        comment_id: The comment ID.
        body: New comment body content.
        version_number: Next version number (current + 1).
        body_format: Body representation format.
    """
    payload = {
        "version": {"number": version_number},
        "body": {
            "representation": body_format,
            "value": body,
        },
    }
    resp = requests.put(_v2(f"/footer-comments/{comment_id}"), json=payload, auth=_auth())
    return _handle(resp)


def delete_footer_comment(comment_id: str) -> dict:
    """Delete a footer comment by ID (v2).

    Args:
        comment_id: The comment ID to delete.
    """
    resp = requests.delete(_v2(f"/footer-comments/{comment_id}"), auth=_auth())
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)


# ---------------------------------------------------------------------------
# Inline comments
# ---------------------------------------------------------------------------

def list_page_inline_comments(
    page_id: str,
    limit: int = 25,
    cursor: str = "",
    body_format: str = "storage",
    resolution_status: str = "",
) -> dict:
    """List inline comments on a page (v2).

    Args:
        page_id: The page ID.
        limit: Maximum number of results.
        cursor: Pagination cursor.
        body_format: Body representation format.
        resolution_status: Filter by resolution status ('open', 'resolved').
    """
    params: dict = {"limit": limit, "body-format": body_format}
    if cursor:
        params["cursor"] = cursor
    if resolution_status:
        params["resolution-status"] = resolution_status
    resp = requests.get(_v2(f"/pages/{page_id}/inline-comments"), params=params, auth=_auth())
    return _handle(resp)


def create_page_inline_comment(
    page_id: str,
    body: str,
    inline_marker_ref: str,
    body_format: str = "storage",
    parent_comment_id: str = "",
) -> dict:
    """Create an inline comment on a page (v2).

    Args:
        page_id: The page ID.
        body: Comment body content.
        inline_marker_ref: The inline marker reference (text selection identifier).
        body_format: Body representation format.
        parent_comment_id: Optional parent comment ID for replies.
    """
    payload: dict = {
        "pageId": page_id,
        "body": {
            "representation": body_format,
            "value": body,
        },
        "inlineCommentProperties": {
            "textSelection": inline_marker_ref,
        },
    }
    if parent_comment_id:
        payload["parentCommentId"] = parent_comment_id
    resp = requests.post(_v2("/inline-comments"), json=payload, auth=_auth())
    return _handle(resp)


def get_inline_comment_by_id(comment_id: str, body_format: str = "storage") -> dict:
    """Get an inline comment by ID (v2).

    Args:
        comment_id: The comment ID.
        body_format: Body representation format.
    """
    params = {"body-format": body_format}
    resp = requests.get(_v2(f"/inline-comments/{comment_id}"), params=params, auth=_auth())
    return _handle(resp)


def delete_inline_comment(comment_id: str) -> dict:
    """Delete an inline comment by ID (v2).

    Args:
        comment_id: The comment ID to delete.
    """
    resp = requests.delete(_v2(f"/inline-comments/{comment_id}"), auth=_auth())
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)
