"""
Confluence Cloud v2 API — Content Properties tools.
Focused on page and blog post properties (most common use cases).
"""
import os
import requests
from typing import Optional, Any

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


# ── Page Properties ───────────────────────────────────────────────────────────

def get_page_properties(
    page_id: str,
    key: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get content properties for a page (v2). Optionally filter by key.
    """
    params: dict = {"limit": limit}
    if key:
        params["key"] = key
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/properties"), params=params, auth=_auth())
    return _handle(resp)


def get_page_property_by_id(page_id: str, property_id: str) -> dict:
    """
    Get a specific content property for a page by property ID (v2).
    """
    resp = requests.get(_v2(f"/pages/{page_id}/properties/{property_id}"), auth=_auth())
    return _handle(resp)


def create_page_property(page_id: str, key: str, value: Any) -> dict:
    """
    Create a content property for a page (v2).
    key: Property key string.
    value: Property value (any JSON-serializable type).
    """
    payload = {"key": key, "value": value}
    resp = requests.post(_v2(f"/pages/{page_id}/properties"), json=payload, auth=_auth())
    return _handle(resp)


def update_page_property(
    page_id: str,
    property_id: str,
    key: str,
    value: Any,
    version_number: int,
    version_message: Optional[str] = None,
) -> dict:
    """
    Update a content property for a page by property ID (v2).
    version_number must be current version + 1.
    """
    payload: dict = {
        "key": key,
        "value": value,
        "version": {"number": version_number},
    }
    if version_message:
        payload["version"]["message"] = version_message
    resp = requests.put(
        _v2(f"/pages/{page_id}/properties/{property_id}"), json=payload, auth=_auth()
    )
    return _handle(resp)


def delete_page_property(page_id: str, property_id: str) -> dict:
    """
    Delete a content property for a page by property ID (v2).
    """
    resp = requests.delete(
        _v2(f"/pages/{page_id}/properties/{property_id}"), auth=_auth()
    )
    return _handle(resp)


# ── Blog Post Properties ──────────────────────────────────────────────────────

def get_blog_post_properties(
    blog_post_id: str,
    key: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get content properties for a blog post (v2). Optionally filter by key.
    """
    params: dict = {"limit": limit}
    if key:
        params["key"] = key
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/blogposts/{blog_post_id}/properties"), params=params, auth=_auth())
    return _handle(resp)


def get_blog_post_property_by_id(blog_post_id: str, property_id: str) -> dict:
    """
    Get a specific content property for a blog post by property ID (v2).
    """
    resp = requests.get(
        _v2(f"/blogposts/{blog_post_id}/properties/{property_id}"), auth=_auth()
    )
    return _handle(resp)


def create_blog_post_property(blog_post_id: str, key: str, value: Any) -> dict:
    """
    Create a content property for a blog post (v2).
    """
    payload = {"key": key, "value": value}
    resp = requests.post(
        _v2(f"/blogposts/{blog_post_id}/properties"), json=payload, auth=_auth()
    )
    return _handle(resp)


def update_blog_post_property(
    blog_post_id: str,
    property_id: str,
    key: str,
    value: Any,
    version_number: int,
    version_message: Optional[str] = None,
) -> dict:
    """
    Update a content property for a blog post by property ID (v2).
    version_number must be current version + 1.
    """
    payload: dict = {
        "key": key,
        "value": value,
        "version": {"number": version_number},
    }
    if version_message:
        payload["version"]["message"] = version_message
    resp = requests.put(
        _v2(f"/blogposts/{blog_post_id}/properties/{property_id}"),
        json=payload,
        auth=_auth(),
    )
    return _handle(resp)


def delete_blog_post_property(blog_post_id: str, property_id: str) -> dict:
    """
    Delete a content property for a blog post by property ID (v2).
    """
    resp = requests.delete(
        _v2(f"/blogposts/{blog_post_id}/properties/{property_id}"), auth=_auth()
    )
    return _handle(resp)
