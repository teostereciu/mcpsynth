"""
Confluence Cloud — Labels tools (v1 for add/remove, v2 for listing).
"""
import os
import requests
from typing import Optional, List

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

def _auth():
    return (EMAIL, API_TOKEN)

def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"

def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"

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


def get_labels(
    prefix: Optional[str] = None,
    limit: int = 50,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get all labels (v2). Optionally filter by prefix ('global'|'my'|'team').
    """
    params: dict = {"limit": limit}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2("/labels"), params=params, auth=_auth())
    return _handle(resp)


def get_page_labels(
    page_id: str,
    prefix: Optional[str] = None,
    limit: int = 50,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get labels for a specific page (v2).
    """
    params: dict = {"limit": limit}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/labels"), params=params, auth=_auth())
    return _handle(resp)


def get_blog_post_labels(
    blog_post_id: str,
    prefix: Optional[str] = None,
    limit: int = 50,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get labels for a specific blog post (v2).
    """
    params: dict = {"limit": limit}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/blogposts/{blog_post_id}/labels"), params=params, auth=_auth())
    return _handle(resp)


def get_space_labels(
    space_id: str,
    prefix: Optional[str] = None,
    limit: int = 50,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get labels for a specific space (v2).
    """
    params: dict = {"limit": limit}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/spaces/{space_id}/labels"), params=params, auth=_auth())
    return _handle(resp)


def get_attachment_labels(
    attachment_id: str,
    prefix: Optional[str] = None,
    limit: int = 50,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get labels for a specific attachment (v2).
    """
    params: dict = {"limit": limit}
    if prefix:
        params["prefix"] = prefix
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/attachments/{attachment_id}/labels"), params=params, auth=_auth())
    return _handle(resp)


def add_content_labels(
    content_id: str,
    labels: List[str],
    prefix: str = "global",
) -> dict:
    """
    Add labels to a piece of content (v1). Does not remove existing labels.
    labels: list of label name strings.
    prefix: 'global' | 'my' | 'team'.
    """
    body = [{"prefix": prefix, "name": name} for name in labels]
    resp = requests.post(
        _v1(f"/content/{content_id}/label"),
        json=body,
        auth=_auth(),
    )
    return _handle(resp)


def remove_content_label(
    content_id: str,
    label_name: str,
) -> dict:
    """
    Remove a label from a piece of content (v1).
    Uses query parameter form to support labels with special characters.
    """
    params = {"name": label_name}
    resp = requests.delete(
        _v1(f"/content/{content_id}/label"),
        params=params,
        auth=_auth(),
    )
    return _handle(resp)
