"""
Confluence Cloud v2 Spaces tools.
Endpoints: GET/POST /api/v2/spaces, GET /api/v2/spaces/{id}
Also v1 DELETE /wiki/rest/api/space/{spaceKey}
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


def get_spaces(
    keys: list[str] | None = None,
    space_type: str | None = None,
    status: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return all spaces, optionally filtered by keys, type, or status."""
    params: dict = {"max_results": max_results}
    if keys:
        params["keys"] = keys
    if space_type:
        params["type"] = space_type
    if status:
        params["content_status"] = status
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2("/spaces"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_space_by_id(
    space_id: str,
    include_icon: bool = False,
    include_labels: bool = False,
    include_properties: bool = False,
) -> dict:
    """Return a specific space by its numeric ID."""
    params: dict = {}
    if include_icon:
        params["include-icon"] = "true"
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    try:
        r = requests.get(_v2(f"/spaces/{space_id}"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def create_space(
    name: str,
    key: str | None = None,
    description: str | None = None,
    is_private: bool = False,
) -> dict:
    """Create a new Confluence space."""
    payload: dict = {"name": name}
    if key:
        payload["key"] = key
    if description:
        payload["description"] = {"value": description, "representation": "plain"}
    if is_private:
        payload["createPrivateSpace"] = True
    try:
        r = requests.post(_v2("/spaces"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def delete_space(space_key: str) -> dict:
    """Delete a space by its key (v1 API). Returns a long-running task."""
    try:
        r = requests.delete(_v1(f"/space/{space_key}"), auth=_auth(), timeout=30)
        if r.status_code in (200, 202, 204):
            try:
                return r.json()
            except Exception:
                return {"success": True, "message": f"Space {space_key} deletion initiated."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
