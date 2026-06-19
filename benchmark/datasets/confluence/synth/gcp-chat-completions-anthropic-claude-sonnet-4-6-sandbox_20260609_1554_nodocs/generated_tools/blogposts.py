"""
Confluence Cloud REST API — Blog Posts (v2 preferred)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "")
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


def _resolve_space_id(space_key: str) -> tuple:
    """Return (space_id, error_dict_or_None)."""
    resp = requests.get(_v1(f"/space/{space_key}"), auth=_auth())
    if not resp.ok:
        return None, _handle(resp)
    return resp.json().get("id"), None


def list_blogposts(
    space_key: str = "",
    limit: int = 25,
    cursor: str = "",
    status: str = "current",
    body_format: str = "storage",
) -> dict:
    """List blog posts in a space (v2).

    Args:
        space_key: Space key (defaults to CONFLUENCE_SPACE_KEY env var).
        limit: Maximum number of results.
        cursor: Pagination cursor.
        status: Blog post status ('current', 'draft').
        body_format: Body representation format.
    """
    key = space_key or SPACE_KEY
    space_id, err = _resolve_space_id(key)
    if err:
        return err

    params: dict = {
        "space-id": space_id,
        "limit": limit,
        "status": status,
        "body-format": body_format,
    }
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2("/blogposts"), params=params, auth=_auth())
    return _handle(resp)


def get_blogpost_by_id(blogpost_id: str, body_format: str = "storage") -> dict:
    """Get a blog post by ID (v2).

    Args:
        blogpost_id: The blog post ID.
        body_format: Body representation format.
    """
    params = {"body-format": body_format}
    resp = requests.get(_v2(f"/blogposts/{blogpost_id}"), params=params, auth=_auth())
    return _handle(resp)


def create_blogpost(
    title: str,
    body: str,
    space_key: str = "",
    body_format: str = "storage",
    status: str = "current",
) -> dict:
    """Create a new blog post (v2).

    Args:
        title: Blog post title.
        body: Blog post body content.
        space_key: Space key (defaults to CONFLUENCE_SPACE_KEY env var).
        body_format: Body representation format ('storage', 'wiki', 'atlas_doc_format').
        status: 'current' (published) or 'draft'.
    """
    key = space_key or SPACE_KEY
    space_id, err = _resolve_space_id(key)
    if err:
        return err

    payload = {
        "spaceId": str(space_id),
        "status": status,
        "title": title,
        "body": {
            "representation": body_format,
            "value": body,
        },
    }
    resp = requests.post(_v2("/blogposts"), json=payload, auth=_auth())
    return _handle(resp)


def update_blogpost(
    blogpost_id: str,
    title: str,
    body: str,
    version_number: int,
    body_format: str = "storage",
    status: str = "current",
) -> dict:
    """Update an existing blog post (v2).

    Args:
        blogpost_id: The blog post ID.
        title: New title.
        body: New body content.
        version_number: Next version number (current version + 1).
        body_format: Body representation format.
        status: 'current' or 'draft'.
    """
    payload = {
        "id": blogpost_id,
        "status": status,
        "title": title,
        "body": {
            "representation": body_format,
            "value": body,
        },
        "version": {"number": version_number},
    }
    resp = requests.put(_v2(f"/blogposts/{blogpost_id}"), json=payload, auth=_auth())
    return _handle(resp)


def delete_blogpost(blogpost_id: str) -> dict:
    """Delete a blog post by ID (v2).

    Args:
        blogpost_id: The blog post ID to delete.
    """
    resp = requests.delete(_v2(f"/blogposts/{blogpost_id}"), auth=_auth())
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)
