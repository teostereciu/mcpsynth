"""
Confluence Cloud v2 API — Versions tools.
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


def get_page_versions(
    page_id: str,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
) -> dict:
    """
    Get all versions of a page (v2).
    """
    params: dict = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if body_format:
        params["body-format"] = body_format
    resp = requests.get(_v2(f"/pages/{page_id}/versions"), params=params, auth=_auth())
    return _handle(resp)


def get_page_version_details(page_id: str, version_number: int) -> dict:
    """
    Get details for a specific version of a page (v2).
    """
    resp = requests.get(
        _v2(f"/pages/{page_id}/versions/{version_number}"), auth=_auth()
    )
    return _handle(resp)


def get_blog_post_versions(
    blog_post_id: str,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
) -> dict:
    """
    Get all versions of a blog post (v2).
    """
    params: dict = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if body_format:
        params["body-format"] = body_format
    resp = requests.get(_v2(f"/blogposts/{blog_post_id}/versions"), params=params, auth=_auth())
    return _handle(resp)


def get_blog_post_version_details(blog_post_id: str, version_number: int) -> dict:
    """
    Get details for a specific version of a blog post (v2).
    """
    resp = requests.get(
        _v2(f"/blogposts/{blog_post_id}/versions/{version_number}"), auth=_auth()
    )
    return _handle(resp)


def get_attachment_versions(
    attachment_id: str,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get all versions of an attachment (v2).
    """
    params: dict = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/attachments/{attachment_id}/versions"), params=params, auth=_auth())
    return _handle(resp)


def get_attachment_version_details(attachment_id: str, version_number: int) -> dict:
    """
    Get details for a specific version of an attachment (v2).
    """
    resp = requests.get(
        _v2(f"/attachments/{attachment_id}/versions/{version_number}"), auth=_auth()
    )
    return _handle(resp)


def restore_content_version(
    content_id: str,
    version_number: int,
    message: Optional[str] = None,
    restore_title: bool = True,
) -> dict:
    """
    Restore a historical version of content to be the latest version (v1).
    A new version is created with the content of the historical version.
    content_id: The ID of the page or blog post.
    version_number: The version number to restore.
    """
    payload: dict = {
        "operationKey": "restore",
        "params": {
            "versionNumber": version_number,
            "restoreTitle": restore_title,
        },
    }
    if message:
        payload["params"]["message"] = message
    resp = requests.post(
        _v1(f"/content/{content_id}/version"),
        json=payload,
        auth=_auth(),
    )
    return _handle(resp)
