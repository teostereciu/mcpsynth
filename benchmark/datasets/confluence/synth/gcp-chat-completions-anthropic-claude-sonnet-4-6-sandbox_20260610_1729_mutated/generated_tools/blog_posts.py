"""
Confluence Cloud v2 Blog Post tools.
Endpoints: GET/POST /api/v2/blogposts, GET/PUT/DELETE /api/v2/blogposts/{id},
           GET /api/v2/spaces/{id}/blogposts
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


def get_blog_posts(
    space_id: str | None = None,
    title: str | None = None,
    status: str | None = None,
    body_format: str = "storage",
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return a list of blog posts, optionally filtered by space, title, or status."""
    params: dict = {"body-format": body_format, "max_results": max_results}
    if space_id:
        params["space-id"] = space_id
    if title:
        params["title"] = title
    if status:
        params["content_status"] = status
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2("/blogposts"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blog_post_by_id(
    blog_post_id: str,
    body_format: str = "storage",
    include_labels: bool = False,
    include_properties: bool = False,
    include_versions: bool = False,
) -> dict:
    """Return a specific blog post by its ID."""
    params: dict = {"body-format": body_format}
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    if include_versions:
        params["include-versions"] = "true"
    try:
        r = requests.get(_v2(f"/blogposts/{blog_post_id}"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def create_blog_post(
    space_id: str,
    title: str,
    body_value: str,
    body_representation: str = "storage",
    status: str = "current",
) -> dict:
    """Create a new blog post in the given space."""
    payload: dict = {
        "spaceId": space_id,
        "title": title,
        "status": status,
        "body": {
            "representation": body_representation,
            "value": body_value,
        },
    }
    try:
        r = requests.post(_v2("/blogposts"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def update_blog_post(
    blog_post_id: str,
    title: str,
    body_value: str,
    version_number: int,
    space_id: str,
    body_representation: str = "storage",
    status: str = "current",
    version_message: str = "",
) -> dict:
    """Update an existing blog post by ID. version_number must be current version + 1."""
    payload: dict = {
        "id": str(blog_post_id),
        "title": title,
        "status": status,
        "spaceId": space_id,
        "body": {
            "representation": body_representation,
            "value": body_value,
        },
        "version": {
            "number": version_number,
            "message": version_message,
        },
    }
    try:
        r = requests.put(_v2(f"/blogposts/{blog_post_id}"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def delete_blog_post(blog_post_id: str, purge: bool = False) -> dict:
    """Delete a blog post by ID. Set purge=True to permanently delete a trashed post."""
    params = {}
    if purge:
        params["purge"] = "true"
    try:
        r = requests.delete(_v2(f"/blogposts/{blog_post_id}"), params=params, auth=_auth(), timeout=30)
        if r.status_code == 204:
            return {"success": True, "message": f"Blog post {blog_post_id} deleted."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blog_posts_in_space(
    space_id: str,
    cursor: str | None = None,
    max_results: int = 25,
    body_format: str = "storage",
) -> dict:
    """Return all blog posts in a specific space."""
    params: dict = {"body-format": body_format, "max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/spaces/{space_id}/blogposts"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
