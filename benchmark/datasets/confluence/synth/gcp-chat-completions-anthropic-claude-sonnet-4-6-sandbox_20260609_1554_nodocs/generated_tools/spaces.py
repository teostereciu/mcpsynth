"""
Confluence Cloud REST API — Spaces (v2 preferred)
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


def list_spaces(
    limit: int = 25,
    cursor: str = "",
    type: str = "",
    status: str = "current",
) -> dict:
    """List all spaces (v2).

    Args:
        limit: Maximum number of results (1-250).
        cursor: Pagination cursor from a previous response.
        type: Filter by space type ('global', 'personal').
        status: Filter by status ('current', 'archived').
    """
    params: dict = {"limit": limit, "status": status}
    if cursor:
        params["cursor"] = cursor
    if type:
        params["type"] = type
    resp = requests.get(_v2("/spaces"), params=params, auth=_auth())
    return _handle(resp)


def get_space_by_key(space_key: str) -> dict:
    """Get a space by its key (v1).

    Args:
        space_key: The space key (e.g. 'SYNTH').
    """
    resp = requests.get(_v1(f"/space/{space_key}"), auth=_auth())
    return _handle(resp)


def get_space_by_id(space_id: str) -> dict:
    """Get a space by its ID (v2).

    Args:
        space_id: The numeric space ID.
    """
    resp = requests.get(_v2(f"/spaces/{space_id}"), auth=_auth())
    return _handle(resp)


def create_space(
    key: str,
    name: str,
    description: str = "",
    type: str = "global",
) -> dict:
    """Create a new space (v1).

    Args:
        key: Unique space key (uppercase letters/numbers, e.g. 'MYSPACE').
        name: Display name of the space.
        description: Optional plain-text description.
        type: Space type ('global' or 'personal').
    """
    payload: dict = {
        "key": key,
        "name": name,
        "type": type,
    }
    if description:
        payload["description"] = {
            "plain": {"value": description, "representation": "plain"}
        }
    resp = requests.post(_v1("/space"), json=payload, auth=_auth())
    return _handle(resp)


def delete_space(space_key: str) -> dict:
    """Delete a space by key (v1). This is an asynchronous operation.

    Args:
        space_key: The key of the space to delete.
    """
    resp = requests.delete(_v1(f"/space/{space_key}"), auth=_auth())
    if resp.status_code in (200, 202, 204):
        try:
            return resp.json()
        except Exception:
            return {"success": True}
    return _handle(resp)


def get_space_content(
    space_key: str,
    content_type: str = "page",
    limit: int = 25,
    start: int = 0,
) -> dict:
    """Get content within a space (v1).

    Args:
        space_key: The space key.
        content_type: Type of content ('page', 'blogpost').
        limit: Maximum number of results.
        start: Offset for pagination.
    """
    params = {
        "limit": limit,
        "start": start,
        "expand": "body.storage,version",
    }
    resp = requests.get(
        _v1(f"/space/{space_key}/content/{content_type}"),
        params=params,
        auth=_auth(),
    )
    return _handle(resp)
