"""
Confluence Cloud v2 Content Properties tools.
Endpoints for pages: GET/POST /api/v2/pages/{page-id}/properties,
                     GET/PUT/DEL /api/v2/pages/{page-id}/properties/{property-id}
Endpoints for blog posts: GET/POST /api/v2/blogposts/{blogpost-id}/properties,
                          GET/PUT/DEL /api/v2/blogposts/{blogpost-id}/properties/{property-id}
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


# ─── Page Properties ────────────────────────────────────────────────────────

def get_page_properties(
    page_id: str,
    key: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return all content properties for a specific page."""
    params: dict = {"max_results": max_results}
    if key:
        params["key"] = key
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/pages/{page_id}/properties"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def create_page_property(page_id: str, key: str, value: object) -> dict:
    """Create a new content property on a page."""
    payload = {"key": key, "value": value}
    try:
        r = requests.post(_v2(f"/pages/{page_id}/properties"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_page_property_by_id(page_id: str, property_id: str) -> dict:
    """Return a specific content property of a page by property ID."""
    try:
        r = requests.get(_v2(f"/pages/{page_id}/properties/{property_id}"), auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def update_page_property(
    page_id: str,
    property_id: str,
    key: str,
    value: object,
    version_number: int,
    version_message: str = "",
) -> dict:
    """Update a content property on a page by property ID."""
    payload = {
        "key": key,
        "value": value,
        "version": {"number": version_number, "message": version_message},
    }
    try:
        r = requests.put(
            _v2(f"/pages/{page_id}/properties/{property_id}"),
            json=payload,
            auth=_auth(),
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def delete_page_property(page_id: str, property_id: str) -> dict:
    """Delete a content property from a page by property ID."""
    try:
        r = requests.delete(
            _v2(f"/pages/{page_id}/properties/{property_id}"),
            auth=_auth(),
            timeout=30,
        )
        if r.status_code == 204:
            return {"success": True, "message": f"Property {property_id} deleted from page {page_id}."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


# ─── Blog Post Properties ────────────────────────────────────────────────────

def get_blogpost_properties(
    blog_post_id: str,
    key: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return all content properties for a specific blog post."""
    params: dict = {"max_results": max_results}
    if key:
        params["key"] = key
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/blogposts/{blog_post_id}/properties"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def create_blogpost_property(blog_post_id: str, key: str, value: object) -> dict:
    """Create a new content property on a blog post."""
    payload = {"key": key, "value": value}
    try:
        r = requests.post(_v2(f"/blogposts/{blog_post_id}/properties"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blogpost_property_by_id(blog_post_id: str, property_id: str) -> dict:
    """Return a specific content property of a blog post by property ID."""
    try:
        r = requests.get(_v2(f"/blogposts/{blog_post_id}/properties/{property_id}"), auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def update_blogpost_property(
    blog_post_id: str,
    property_id: str,
    key: str,
    value: object,
    version_number: int,
    version_message: str = "",
) -> dict:
    """Update a content property on a blog post by property ID."""
    payload = {
        "key": key,
        "value": value,
        "version": {"number": version_number, "message": version_message},
    }
    try:
        r = requests.put(
            _v2(f"/blogposts/{blog_post_id}/properties/{property_id}"),
            json=payload,
            auth=_auth(),
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def delete_blogpost_property(blog_post_id: str, property_id: str) -> dict:
    """Delete a content property from a blog post by property ID."""
    try:
        r = requests.delete(
            _v2(f"/blogposts/{blog_post_id}/properties/{property_id}"),
            auth=_auth(),
            timeout=30,
        )
        if r.status_code == 204:
            return {"success": True, "message": f"Property {property_id} deleted from blog post {blog_post_id}."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
