"""
Confluence Cloud v2 API — Spaces tools.
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


def get_spaces(
    keys: Optional[List[str]] = None,
    space_type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get all spaces (v2). Optionally filter by keys, type ('global'|'personal'), status.
    """
    params = {"limit": limit}
    if keys:
        params["keys"] = ",".join(keys)
    if space_type:
        params["type"] = space_type
    if status:
        params["status"] = status
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2("/spaces"), params=params, auth=_auth())
    return _handle(resp)


def get_space_by_id(
    space_id: str,
    include_labels: bool = False,
    include_properties: bool = False,
    include_permissions: bool = False,
) -> dict:
    """
    Get a specific space by numeric ID (v2).
    """
    params = {}
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    if include_permissions:
        params["include-permissions"] = "true"
    resp = requests.get(_v2(f"/spaces/{space_id}"), params=params, auth=_auth())
    return _handle(resp)


def create_space(
    name: str,
    key: Optional[str] = None,
    description: Optional[str] = None,
    is_private: bool = False,
) -> dict:
    """
    Create a new space (v2).
    name: Display name of the space.
    key: Space key (short identifier). Optional.
    description: Plain text description.
    is_private: If True, creates a private space.
    """
    payload: dict = {"name": name, "createPrivateSpace": is_private}
    if key:
        payload["key"] = key
    if description:
        payload["description"] = {
            "value": description,
            "representation": "plain",
        }
    resp = requests.post(_v2("/spaces"), json=payload, auth=_auth())
    return _handle(resp)


def delete_space(space_key: str) -> dict:
    """
    Delete a space by space key (v1). This is an async operation.
    Returns a long-running task reference.
    """
    resp = requests.delete(_v1(f"/space/{space_key}"), auth=_auth())
    return _handle(resp)
