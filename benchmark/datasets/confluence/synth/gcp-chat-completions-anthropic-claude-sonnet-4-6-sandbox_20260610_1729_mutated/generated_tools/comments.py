"""
Confluence Cloud v2 Comments tools (footer and inline).
Endpoints: GET/POST /api/v2/footer-comments, GET/PUT/DELETE /api/v2/footer-comments/{id},
           GET/POST /api/v2/inline-comments, GET/PUT/DELETE /api/v2/inline-comments/{id},
           GET /api/v2/pages/{id}/footer-comments, GET /api/v2/pages/{id}/inline-comments,
           GET /api/v2/blogposts/{id}/footer-comments, GET /api/v2/blogposts/{id}/inline-comments
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, TOKEN)


def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"


def get_page_footer_comments(
    page_id: str,
    body_format: str = "storage",
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return root footer comments for a specific page."""
    params: dict = {"body-format": body_format, "max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/pages/{page_id}/footer-comments"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_page_inline_comments(
    page_id: str,
    body_format: str = "storage",
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return root inline comments for a specific page."""
    params: dict = {"body-format": body_format, "max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/pages/{page_id}/inline-comments"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blogpost_footer_comments(
    blog_post_id: str,
    body_format: str = "storage",
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return root footer comments for a specific blog post."""
    params: dict = {"body-format": body_format, "max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/blogposts/{blog_post_id}/footer-comments"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blogpost_inline_comments(
    blog_post_id: str,
    body_format: str = "storage",
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return root inline comments for a specific blog post."""
    params: dict = {"body-format": body_format, "max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/blogposts/{blog_post_id}/inline-comments"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def create_footer_comment(
    body_value: str,
    body_representation: str = "storage",
    page_id: str | None = None,
    blog_post_id: str | None = None,
    parent_comment_id: str | None = None,
) -> dict:
    """
    Create a footer comment on a page, blog post, or as a reply to another comment.
    Provide exactly one of: page_id, blog_post_id, or parent_comment_id.
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
    try:
        r = requests.post(_v2("/footer-comments"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_footer_comment_by_id(comment_id: str, body_format: str = "storage") -> dict:
    """Return a specific footer comment by its ID."""
    params: dict = {"body-format": body_format}
    try:
        r = requests.get(_v2(f"/footer-comments/{comment_id}"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def update_footer_comment(
    comment_id: str,
    body_value: str,
    version_number: int,
    body_representation: str = "storage",
    version_message: str = "",
) -> dict:
    """Update a footer comment by ID."""
    payload: dict = {
        "version": {"number": version_number, "message": version_message},
        "body": {"representation": body_representation, "value": body_value},
    }
    try:
        r = requests.put(_v2(f"/footer-comments/{comment_id}"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def delete_footer_comment(comment_id: str) -> dict:
    """Delete a footer comment by ID."""
    try:
        r = requests.delete(_v2(f"/footer-comments/{comment_id}"), auth=_auth(), timeout=30)
        if r.status_code == 204:
            return {"success": True, "message": f"Footer comment {comment_id} deleted."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def create_inline_comment(
    body_value: str,
    body_representation: str = "storage",
    page_id: str | None = None,
    blog_post_id: str | None = None,
    inline_marker_ref: str | None = None,
    inline_original_selection: str | None = None,
) -> dict:
    """
    Create an inline comment on a page or blog post.
    Optionally provide inline marker reference and original selection text.
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
    if inline_marker_ref or inline_original_selection:
        payload["inlineCommentProperties"] = {}
        if inline_marker_ref:
            payload["inlineCommentProperties"]["inlineMarkerRef"] = inline_marker_ref
        if inline_original_selection:
            payload["inlineCommentProperties"]["inlineOriginalSelection"] = inline_original_selection
    try:
        r = requests.post(_v2("/inline-comments"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_inline_comment_by_id(comment_id: str, body_format: str = "storage") -> dict:
    """Return a specific inline comment by its ID."""
    params: dict = {"body-format": body_format}
    try:
        r = requests.get(_v2(f"/inline-comments/{comment_id}"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def update_inline_comment(
    comment_id: str,
    body_value: str,
    version_number: int,
    body_representation: str = "storage",
    resolution_status: str | None = None,
) -> dict:
    """Update an inline comment by ID. Optionally resolve/reopen with resolution_status."""
    payload: dict = {
        "version": {"number": version_number},
        "body": {"representation": body_representation, "value": body_value},
    }
    if resolution_status:
        payload["resolutionStatus"] = resolution_status
    try:
        r = requests.put(_v2(f"/inline-comments/{comment_id}"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def delete_inline_comment(comment_id: str) -> dict:
    """Delete an inline comment by ID."""
    try:
        r = requests.delete(_v2(f"/inline-comments/{comment_id}"), auth=_auth(), timeout=30)
        if r.status_code == 204:
            return {"success": True, "message": f"Inline comment {comment_id} deleted."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
