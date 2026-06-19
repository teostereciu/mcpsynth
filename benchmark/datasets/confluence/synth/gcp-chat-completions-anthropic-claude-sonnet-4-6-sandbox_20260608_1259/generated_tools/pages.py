"""
Confluence Cloud v2 API — Pages tools.
"""
import os
import requests
from typing import Optional

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "")

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


def get_pages(
    space_id: Optional[str] = None,
    title: Optional[str] = None,
    status: Optional[str] = None,
    body_format: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get pages (v2). Optionally filter by space_id, title, status.
    body_format: 'storage' | 'atlas_doc_format' | 'view' (default none).
    """
    params = {"limit": limit}
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
    resp = requests.get(_v2("/pages"), params=params, auth=_auth())
    return _handle(resp)


def get_page_by_id(
    page_id: str,
    body_format: Optional[str] = "storage",
    version: Optional[int] = None,
    include_labels: bool = False,
    include_properties: bool = False,
    include_versions: bool = False,
) -> dict:
    """
    Get a specific page by ID (v2).
    body_format: 'storage' | 'atlas_doc_format' | 'view'.
    """
    params = {}
    if body_format:
        params["body-format"] = body_format
    if version is not None:
        params["version"] = version
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    if include_versions:
        params["include-versions"] = "true"
    resp = requests.get(_v2(f"/pages/{page_id}"), params=params, auth=_auth())
    return _handle(resp)


def create_page(
    space_id: str,
    title: str,
    body_value: str,
    body_representation: str = "storage",
    parent_id: Optional[str] = None,
    status: str = "current",
) -> dict:
    """
    Create a page in a space (v2).
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
    if parent_id:
        payload["parentId"] = parent_id
    resp = requests.post(_v2("/pages"), json=payload, auth=_auth())
    return _handle(resp)


def update_page(
    page_id: str,
    title: str,
    body_value: str,
    version_number: int,
    body_representation: str = "storage",
    status: str = "current",
    parent_id: Optional[str] = None,
    version_message: Optional[str] = None,
) -> dict:
    """
    Update a page by ID (v2). version_number must be current version + 1.
    """
    payload = {
        "id": str(page_id),
        "status": status,
        "title": title,
        "body": {
            "representation": body_representation,
            "value": body_value,
        },
        "version": {"number": version_number},
    }
    if parent_id:
        payload["parentId"] = parent_id
    if version_message:
        payload["version"]["message"] = version_message
    resp = requests.put(_v2(f"/pages/{page_id}"), json=payload, auth=_auth())
    return _handle(resp)


def delete_page(page_id: str, purge: bool = False) -> dict:
    """
    Delete a page by ID (v2). Set purge=True to permanently delete a trashed page.
    """
    params = {}
    if purge:
        params["purge"] = "true"
    resp = requests.delete(_v2(f"/pages/{page_id}"), params=params, auth=_auth())
    return _handle(resp)


def get_pages_in_space(
    space_id: str,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
) -> dict:
    """
    Get all pages in a specific space (v2).
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if body_format:
        params["body-format"] = body_format
    resp = requests.get(_v2(f"/spaces/{space_id}/pages"), params=params, auth=_auth())
    return _handle(resp)


def get_child_pages(
    page_id: str,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get child pages of a page (v2 via pages filtered by parentId using CQL search,
    or v1 children endpoint).
    Uses v1 children endpoint for direct child listing.
    """
    params = {
        "expand": "version",
        "limit": limit,
    }
    if cursor:
        params["start"] = cursor
    resp = requests.get(
        _v1(f"/content/{page_id}/child/page"), params=params, auth=_auth()
    )
    return _handle(resp)


def get_page_ancestors(page_id: str) -> dict:
    """
    Get ancestors of a page (v1 expand=ancestors).
    """
    params = {"expand": "ancestors"}
    resp = requests.get(_v1(f"/content/{page_id}"), params=params, auth=_auth())
    return _handle(resp)


def move_page(
    page_id: str,
    target_parent_id: str,
    position: str = "append",
) -> dict:
    """
    Move a page by updating its parentId (v2 update).
    position is ignored (v2 uses parentId only).
    First fetches current page to get version number.
    """
    current = get_page_by_id(page_id, body_format="storage")
    if "error" in current:
        return current
    version_number = current.get("version", {}).get("number", 1) + 1
    title = current.get("title", "")
    body = current.get("body", {}).get("storage", {}).get("value", "")
    return update_page(
        page_id=page_id,
        title=title,
        body_value=body,
        version_number=version_number,
        parent_id=target_parent_id,
    )


def get_pages_for_label(
    label_id: str,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get pages associated with a label (v2).
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/labels/{label_id}/pages"), params=params, auth=_auth())
    return _handle(resp)
