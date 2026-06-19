"""
Confluence Cloud REST API — Pages (v2 preferred)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "")
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


# ---------------------------------------------------------------------------
# Pages – CRUD
# ---------------------------------------------------------------------------

def get_page_by_id(page_id: str, body_format: str = "storage") -> dict:
    """Get a page by its ID (v2).

    Args:
        page_id: The ID of the page.
        body_format: Representation format for the body ('storage', 'atlas_doc_format', 'wiki').
    """
    params = {"body-format": body_format}
    resp = requests.get(_v2(f"/pages/{page_id}"), params=params, auth=_auth())
    return _handle(resp)


def get_pages_in_space(
    space_key: str = "",
    limit: int = 25,
    cursor: str = "",
    status: str = "current",
    body_format: str = "storage",
) -> dict:
    """List pages in a space (v2).

    Args:
        space_key: Space key to filter by (defaults to CONFLUENCE_SPACE_KEY env var).
        limit: Maximum number of results (1-250).
        cursor: Pagination cursor from a previous response.
        status: Page status filter ('current', 'archived', 'deleted').
        body_format: Body representation format.
    """
    key = space_key or SPACE_KEY
    params: dict = {"limit": limit, "status": status, "body-format": body_format}
    if cursor:
        params["cursor"] = cursor
    # Resolve space id from key first via v1
    space_resp = requests.get(
        _v1(f"/space/{key}"), auth=_auth()
    )
    if not space_resp.ok:
        return _handle(space_resp)
    space_id = space_resp.json().get("id")
    params["space-id"] = space_id
    resp = requests.get(_v2("/pages"), params=params, auth=_auth())
    return _handle(resp)


def create_page(
    title: str,
    body: str,
    space_key: str = "",
    parent_id: str = "",
    body_format: str = "storage",
    status: str = "current",
) -> dict:
    """Create a new page (v2).

    Args:
        title: Page title.
        body: Page body content.
        space_key: Space key (defaults to CONFLUENCE_SPACE_KEY env var).
        parent_id: Optional parent page ID.
        body_format: Body representation format ('storage', 'wiki', 'atlas_doc_format').
        status: 'current' (published) or 'draft'.
    """
    key = space_key or SPACE_KEY
    # Resolve space id
    space_resp = requests.get(_v1(f"/space/{key}"), auth=_auth())
    if not space_resp.ok:
        return _handle(space_resp)
    space_id = space_resp.json().get("id")

    payload: dict = {
        "spaceId": str(space_id),
        "status": status,
        "title": title,
        "body": {
            "representation": body_format,
            "value": body,
        },
    }
    if parent_id:
        payload["parentId"] = parent_id

    resp = requests.post(_v2("/pages"), json=payload, auth=_auth())
    return _handle(resp)


def update_page(
    page_id: str,
    title: str,
    body: str,
    version_number: int,
    body_format: str = "storage",
    status: str = "current",
) -> dict:
    """Update an existing page (v2).

    Args:
        page_id: The ID of the page to update.
        title: New page title.
        body: New page body content.
        version_number: The next version number (current version + 1).
        body_format: Body representation format.
        status: 'current' or 'draft'.
    """
    payload = {
        "id": page_id,
        "status": status,
        "title": title,
        "body": {
            "representation": body_format,
            "value": body,
        },
        "version": {"number": version_number},
    }
    resp = requests.put(_v2(f"/pages/{page_id}"), json=payload, auth=_auth())
    return _handle(resp)


def delete_page(page_id: str) -> dict:
    """Delete a page by ID (v2).

    Args:
        page_id: The ID of the page to delete.
    """
    resp = requests.delete(_v2(f"/pages/{page_id}"), auth=_auth())
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)


def get_page_children(page_id: str, limit: int = 25, cursor: str = "") -> dict:
    """Get child pages of a page (v2).

    Args:
        page_id: The parent page ID.
        limit: Maximum number of results.
        cursor: Pagination cursor.
    """
    params: dict = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/children"), params=params, auth=_auth())
    return _handle(resp)


def get_page_ancestors(page_id: str) -> dict:
    """Get ancestor pages of a page (v2).

    Args:
        page_id: The page ID.
    """
    resp = requests.get(_v2(f"/pages/{page_id}/ancestors"), auth=_auth())
    return _handle(resp)


def move_page(page_id: str, target_page_id: str, position: str = "append") -> dict:
    """Move a page to a new location (v1).

    Args:
        page_id: The ID of the page to move.
        target_page_id: The ID of the target page.
        position: Position relative to target ('before', 'after', 'append').
    """
    resp = requests.put(
        _v1(f"/content/{page_id}/move/{position}/{target_page_id}"),
        auth=_auth(),
    )
    return _handle(resp)


def get_page_by_title(title: str, space_key: str = "") -> dict:
    """Find a page by title within a space (v1).

    Args:
        title: Exact page title to search for.
        space_key: Space key (defaults to CONFLUENCE_SPACE_KEY env var).
    """
    key = space_key or SPACE_KEY
    params = {
        "spaceKey": key,
        "title": title,
        "expand": "body.storage,version",
    }
    resp = requests.get(_v1("/content"), params=params, auth=_auth())
    return _handle(resp)
