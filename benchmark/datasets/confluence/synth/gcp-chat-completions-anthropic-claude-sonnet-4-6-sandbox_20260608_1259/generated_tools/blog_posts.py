"""
Confluence Cloud v2 API — Blog Posts tools.
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


def get_blog_posts(
    space_id: Optional[str] = None,
    title: Optional[str] = None,
    status: Optional[str] = None,
    body_format: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get blog posts (v2). Optionally filter by space_id, title, status.
    """
    params: dict = {"limit": limit}
    if space_id:
        params["space-id"] = space_id
    if title:
        params["title"] = title
    if status:
        params["status"] = status
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2("/blogposts"), params=params, auth=_auth())
    return _handle(resp)


def get_blog_post_by_id(
    blog_post_id: str,
    body_format: Optional[str] = "storage",
    version: Optional[int] = None,
    include_labels: bool = False,
    include_properties: bool = False,
) -> dict:
    """
    Get a specific blog post by ID (v2).
    body_format: 'storage' | 'atlas_doc_format' | 'view'.
    """
    params: dict = {}
    if body_format:
        params["body-format"] = body_format
    if version is not None:
        params["version"] = version
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    resp = requests.get(_v2(f"/blogposts/{blog_post_id}"), params=params, auth=_auth())
    return _handle(resp)


def create_blog_post(
    space_id: str,
    title: str,
    body_value: str,
    body_representation: str = "storage",
    status: str = "current",
) -> dict:
    """
    Create a new blog post in a space (v2).
    body_representation: 'storage' | 'atlas_doc_format'.
    status: 'current' (published) | 'draft'.
    """
    payload = {
        "spaceId": space_id,
        "title": title,
        "status": status,
        "body": {
            "representation": body_representation,
            "value": body_value,
        },
    }
    resp = requests.post(_v2("/blogposts"), json=payload, auth=_auth())
    return _handle(resp)


def update_blog_post(
    blog_post_id: str,
    title: str,
    body_value: str,
    version_number: int,
    body_representation: str = "storage",
    status: str = "current",
    space_id: Optional[str] = None,
    version_message: Optional[str] = None,
) -> dict:
    """
    Update a blog post by ID (v2). version_number must be current version + 1.
    """
    payload: dict = {
        "id": str(blog_post_id),
        "status": status,
        "title": title,
        "body": {
            "representation": body_representation,
            "value": body_value,
        },
        "version": {"number": version_number},
    }
    if space_id:
        payload["spaceId"] = space_id
    if version_message:
        payload["version"]["message"] = version_message
    resp = requests.put(_v2(f"/blogposts/{blog_post_id}"), json=payload, auth=_auth())
    return _handle(resp)


def delete_blog_post(blog_post_id: str, purge: bool = False) -> dict:
    """
    Delete a blog post by ID (v2). Set purge=True to permanently delete a trashed post.
    """
    params: dict = {}
    if purge:
        params["purge"] = "true"
    resp = requests.delete(_v2(f"/blogposts/{blog_post_id}"), params=params, auth=_auth())
    return _handle(resp)


def get_blog_posts_in_space(
    space_id: str,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
) -> dict:
    """
    Get all blog posts in a specific space (v2).
    """
    params: dict = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if body_format:
        params["body-format"] = body_format
    resp = requests.get(_v2(f"/spaces/{space_id}/blogposts"), params=params, auth=_auth())
    return _handle(resp)
