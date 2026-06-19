"""
Confluence Cloud v2 Pages tools.
Endpoints: GET/POST/PUT/DELETE /api/v2/pages, GET /api/v2/spaces/{id}/pages
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
TOKEN = os.environ.get("JIRA_API_TOKEN", "")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, TOKEN)


def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"


def get_pages(
    space_id: str | None = None,
    title: str | None = None,
    status: str | None = None,
    body_format: str = "storage",
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return a list of pages, optionally filtered by space, title, or status."""
    params: dict = {"body-format": body_format, "max_results": max_results}
    if space_id:
        params["space-id"] = space_id
    if title:
        params["title"] = title
    if status:
        params["content_status"] = status
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2("/pages"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_page_by_id(
    page_id: str,
    body_format: str = "storage",
    include_labels: bool = False,
    include_properties: bool = False,
    include_versions: bool = False,
    version: int | None = None,
) -> dict:
    """Return a specific page by its ID."""
    params: dict = {"body-format": body_format}
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    if include_versions:
        params["include-versions"] = "true"
    if version is not None:
        params["version"] = version
    try:
        r = requests.get(_v2(f"/pages/{page_id}"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def create_page(
    space_id: str,
    title: str,
    body_value: str,
    body_representation: str = "storage",
    parent_id: str | None = None,
    status: str = "current",
) -> dict:
    """Create a new page in the given space."""
    payload: dict = {
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
    try:
        r = requests.post(_v2("/pages"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def update_page(
    page_id: str,
    title: str,
    body_value: str,
    version_number: int,
    body_representation: str = "storage",
    status: str = "current",
    parent_id: str | None = None,
    version_message: str = "",
) -> dict:
    """Update an existing page by ID. version_number must be current version + 1."""
    payload: dict = {
        "id": str(page_id),
        "title": title,
        "status": status,
        "body": {
            "representation": body_representation,
            "value": body_value,
        },
        "version": {
            "number": version_number,
            "message": version_message,
        },
    }
    if parent_id:
        payload["parentId"] = parent_id
    try:
        r = requests.put(_v2(f"/pages/{page_id}"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def delete_page(page_id: str, purge: bool = False) -> dict:
    """Delete a page by ID. Set purge=True to permanently delete a trashed page."""
    params = {}
    if purge:
        params["purge"] = "true"
    try:
        r = requests.delete(_v2(f"/pages/{page_id}"), params=params, auth=_auth(), timeout=30)
        if r.status_code == 204:
            return {"success": True, "message": f"Page {page_id} deleted."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_pages_in_space(
    space_id: str,
    cursor: str | None = None,
    max_results: int = 25,
    body_format: str = "storage",
) -> dict:
    """Return all pages in a specific space."""
    params: dict = {"body-format": body_format, "max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/spaces/{space_id}/pages"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_page_ancestors(page_id: str) -> dict:
    """Return the ancestor pages of a specific page using v1 API."""
    v1_url = f"{BASE_URL}/rest/api/content/{page_id}?expand=ancestors"
    try:
        r = requests.get(v1_url, auth=_auth(), timeout=30)
        r.raise_for_status()
        data = r.json()
        return {"ancestors": data.get("ancestors", []), "id": data.get("id"), "title": data.get("title")}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_page_children(page_id: str, child_type: str = "page") -> dict:
    """Return the children of a specific page (type: page, comment, attachment)."""
    v1_url = f"{BASE_URL}/rest/api/content/{page_id}/child/{child_type}"
    try:
        r = requests.get(v1_url, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def move_page(page_id: str, target_parent_id: str, version_number: int, title: str, space_id: str) -> dict:
    """Move a page to a new parent by updating its parentId."""
    payload: dict = {
        "id": str(page_id),
        "title": title,
        "status": "current",
        "parentId": target_parent_id,
        "body": {"representation": "storage", "value": ""},
        "version": {"number": version_number},
    }
    # We need to fetch current body first
    current = get_page_by_id(page_id, body_format="storage")
    if "error" in current:
        return current
    body_val = ""
    try:
        body_val = current["body"]["storage"]["value"]
    except (KeyError, TypeError):
        pass
    payload["body"]["value"] = body_val
    try:
        r = requests.put(_v2(f"/pages/{page_id}"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
