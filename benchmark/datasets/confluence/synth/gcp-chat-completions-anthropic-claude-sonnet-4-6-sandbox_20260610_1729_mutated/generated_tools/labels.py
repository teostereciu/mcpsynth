"""
Confluence Cloud labels tools.
v2: GET /api/v2/labels, GET /api/v2/pages/{id}/labels, GET /api/v2/blogposts/{id}/labels,
    GET /api/v2/spaces/{id}/labels
v1: POST /wiki/rest/api/content/{id}/label (add labels),
    DEL /wiki/rest/api/content/{id}/label (remove label by query param),
    DEL /wiki/rest/api/content/{id}/label/{label} (remove label by path)
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


def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"


def get_labels(
    prefix: list[str] | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return all labels in the Confluence site."""
    params: dict = {"max_results": max_results}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2("/labels"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_page_labels(
    page_id: str,
    prefix: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return labels for a specific page."""
    params: dict = {"max_results": max_results}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/pages/{page_id}/labels"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blogpost_labels(
    blog_post_id: str,
    prefix: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return labels for a specific blog post."""
    params: dict = {"max_results": max_results}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/blogposts/{blog_post_id}/labels"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_space_labels(
    space_id: str,
    prefix: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return labels for a specific space."""
    params: dict = {"max_results": max_results}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/spaces/{space_id}/labels"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def add_labels_to_content(content_id: str, labels: list[str], prefix: str = "global") -> dict:
    """
    Add labels to a piece of content (page, blog post, etc.) using v1 API.
    labels: list of label name strings.
    prefix: label prefix, typically 'global'.
    """
    payload = [{"prefix": prefix, "name": name} for name in labels]
    try:
        r = requests.post(
            _v1(f"/content/{content_id}/label"),
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


def remove_label_from_content(content_id: str, label_name: str) -> dict:
    """
    Remove a label from a piece of content using v1 API.
    Uses query parameter form (supports labels with '/' characters).
    """
    try:
        r = requests.delete(
            _v1(f"/content/{content_id}/label"),
            params={"name": label_name},
            auth=_auth(),
            timeout=30,
        )
        if r.status_code == 204:
            return {"success": True, "message": f"Label '{label_name}' removed from content {content_id}."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
