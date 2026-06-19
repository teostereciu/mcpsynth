"""
Confluence Cloud REST API — Labels (v1 + v2)
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


def get_page_labels(page_id: str, prefix: str = "", limit: int = 25, cursor: str = "") -> dict:
    """Get labels on a page (v2).

    Args:
        page_id: The page ID.
        prefix: Filter by label prefix ('global', 'my', 'team').
        limit: Maximum number of results.
        cursor: Pagination cursor.
    """
    params: dict = {"limit": limit}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/labels"), params=params, auth=_auth())
    return _handle(resp)


def add_labels_to_page(page_id: str, labels: list) -> dict:
    """Add one or more labels to a page (v1).

    Args:
        page_id: The page ID.
        labels: List of label name strings, e.g. ['important', 'reviewed'].
    """
    payload = [{"prefix": "global", "name": lbl} for lbl in labels]
    resp = requests.post(
        _v1(f"/content/{page_id}/label"),
        json=payload,
        auth=_auth(),
    )
    return _handle(resp)


def remove_label_from_page(page_id: str, label: str) -> dict:
    """Remove a label from a page (v1).

    Args:
        page_id: The page ID.
        label: The label name to remove.
    """
    resp = requests.delete(
        _v1(f"/content/{page_id}/label/{label}"),
        auth=_auth(),
    )
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)


def get_blogpost_labels(blogpost_id: str, limit: int = 25, cursor: str = "") -> dict:
    """Get labels on a blog post (v2).

    Args:
        blogpost_id: The blog post ID.
        limit: Maximum number of results.
        cursor: Pagination cursor.
    """
    params: dict = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/blogposts/{blogpost_id}/labels"), params=params, auth=_auth())
    return _handle(resp)


def add_labels_to_blogpost(blogpost_id: str, labels: list) -> dict:
    """Add one or more labels to a blog post (v1).

    Args:
        blogpost_id: The blog post ID.
        labels: List of label name strings.
    """
    payload = [{"prefix": "global", "name": lbl} for lbl in labels]
    resp = requests.post(
        _v1(f"/content/{blogpost_id}/label"),
        json=payload,
        auth=_auth(),
    )
    return _handle(resp)


def remove_label_from_blogpost(blogpost_id: str, label: str) -> dict:
    """Remove a label from a blog post (v1).

    Args:
        blogpost_id: The blog post ID.
        label: The label name to remove.
    """
    resp = requests.delete(
        _v1(f"/content/{blogpost_id}/label/{label}"),
        auth=_auth(),
    )
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)
