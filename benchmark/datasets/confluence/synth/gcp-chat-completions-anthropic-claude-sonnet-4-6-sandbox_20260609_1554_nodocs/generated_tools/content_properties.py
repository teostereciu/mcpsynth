"""
Confluence Cloud REST API — Content Properties (v2 preferred)
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


def list_page_properties(page_id: str, limit: int = 25, cursor: str = "") -> dict:
    """List all content properties on a page (v2).

    Args:
        page_id: The page ID.
        limit: Maximum number of results.
        cursor: Pagination cursor.
    """
    params: dict = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/properties"), params=params, auth=_auth())
    return _handle(resp)


def get_page_property(page_id: str, property_key: str) -> dict:
    """Get a specific content property on a page (v2).

    Args:
        page_id: The page ID.
        property_key: The property key.
    """
    resp = requests.get(_v2(f"/pages/{page_id}/properties/{property_key}"), auth=_auth())
    return _handle(resp)


def create_page_property(page_id: str, property_key: str, value: dict) -> dict:
    """Create a content property on a page (v2).

    Args:
        page_id: The page ID.
        property_key: The property key (alphanumeric and hyphens).
        value: The property value as a JSON-serializable dict.
    """
    payload = {"key": property_key, "value": value}
    resp = requests.post(_v2(f"/pages/{page_id}/properties"), json=payload, auth=_auth())
    return _handle(resp)


def update_page_property(
    page_id: str,
    property_key: str,
    value: dict,
    version_number: int,
) -> dict:
    """Update a content property on a page (v2).

    Args:
        page_id: The page ID.
        property_key: The property key.
        value: The new property value as a JSON-serializable dict.
        version_number: Next version number (current version + 1).
    """
    payload = {
        "key": property_key,
        "value": value,
        "version": {"number": version_number},
    }
    resp = requests.put(
        _v2(f"/pages/{page_id}/properties/{property_key}"),
        json=payload,
        auth=_auth(),
    )
    return _handle(resp)


def delete_page_property(page_id: str, property_key: str) -> dict:
    """Delete a content property from a page (v2).

    Args:
        page_id: The page ID.
        property_key: The property key to delete.
    """
    resp = requests.delete(
        _v2(f"/pages/{page_id}/properties/{property_key}"),
        auth=_auth(),
    )
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)


# ---------------------------------------------------------------------------
# Generic content properties (v1) — works for any content type
# ---------------------------------------------------------------------------

def list_content_properties(content_id: str, limit: int = 25, start: int = 0) -> dict:
    """List all content properties for any content type (v1).

    Args:
        content_id: The content ID (page, blogpost, etc.).
        limit: Maximum number of results.
        start: Offset for pagination.
    """
    params = {"limit": limit, "start": start}
    resp = requests.get(_v1(f"/content/{content_id}/property"), params=params, auth=_auth())
    return _handle(resp)


def get_content_property(content_id: str, property_key: str) -> dict:
    """Get a specific content property for any content type (v1).

    Args:
        content_id: The content ID.
        property_key: The property key.
    """
    resp = requests.get(_v1(f"/content/{content_id}/property/{property_key}"), auth=_auth())
    return _handle(resp)


def set_content_property(content_id: str, property_key: str, value: dict) -> dict:
    """Create or update a content property for any content type (v1).

    Args:
        content_id: The content ID.
        property_key: The property key.
        value: The property value as a JSON-serializable dict.
    """
    payload = {"key": property_key, "value": value}
    resp = requests.put(
        _v1(f"/content/{content_id}/property/{property_key}"),
        json=payload,
        auth=_auth(),
    )
    return _handle(resp)


def delete_content_property(content_id: str, property_key: str) -> dict:
    """Delete a content property for any content type (v1).

    Args:
        content_id: The content ID.
        property_key: The property key to delete.
    """
    resp = requests.delete(
        _v1(f"/content/{content_id}/property/{property_key}"),
        auth=_auth(),
    )
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)
