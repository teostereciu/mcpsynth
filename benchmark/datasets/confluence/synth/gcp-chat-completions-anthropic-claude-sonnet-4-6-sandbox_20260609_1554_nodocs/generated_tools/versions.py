"""
Confluence Cloud REST API — Page Versions (v1)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, API_TOKEN)


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


def list_page_versions(
    page_id: str,
    limit: int = 25,
    start: int = 0,
    expand: str = "content",
) -> dict:
    """List all versions of a page (v1).

    Args:
        page_id: The page ID.
        limit: Maximum number of results.
        start: Offset for pagination.
        expand: Comma-separated properties to expand (e.g. 'content').
    """
    params = {"limit": limit, "start": start, "expand": expand}
    resp = requests.get(_v1(f"/content/{page_id}/version"), params=params, auth=_auth())
    return _handle(resp)


def get_page_version(page_id: str, version_number: int, expand: str = "content") -> dict:
    """Get a specific version of a page (v1).

    Args:
        page_id: The page ID.
        version_number: The version number to retrieve.
        expand: Comma-separated properties to expand.
    """
    params = {"expand": expand}
    resp = requests.get(
        _v1(f"/content/{page_id}/version/{version_number}"),
        params=params,
        auth=_auth(),
    )
    return _handle(resp)


def restore_page_version(
    page_id: str,
    version_number: int,
    message: str = "",
) -> dict:
    """Restore a page to a previous version (v1).

    Args:
        page_id: The page ID.
        version_number: The version number to restore.
        message: Optional message describing the restore operation.
    """
    payload: dict = {
        "operationKey": "restore",
        "params": {"versionNumber": version_number},
    }
    if message:
        payload["params"]["message"] = message
    resp = requests.post(
        _v1(f"/content/{page_id}/version"),
        json=payload,
        auth=_auth(),
    )
    return _handle(resp)


def delete_page_version(page_id: str, version_number: int) -> dict:
    """Delete a specific version of a page (v1).

    Args:
        page_id: The page ID.
        version_number: The version number to delete.
    """
    resp = requests.delete(
        _v1(f"/content/{page_id}/version/{version_number}"),
        auth=_auth(),
    )
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)
