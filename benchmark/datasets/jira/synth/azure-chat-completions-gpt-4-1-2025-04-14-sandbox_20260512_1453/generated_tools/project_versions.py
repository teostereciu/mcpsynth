import os
import requests
from mcp.tools import tool
from typing import Optional

JIRA_BASE_URL = os.environ["JIRA_BASE_URL"]
JIRA_EMAIL = os.environ["JIRA_EMAIL"]
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
API_ROOT = f"{JIRA_BASE_URL}/rest/api/3"

def _auth_headers():
    from base64 import b64encode
    token = b64encode(f"{JIRA_EMAIL}:{JIRA_API_TOKEN}".encode()).decode()
    return {
        "Authorization": f"Basic {token}",
        "Accept": "application/json"
    }

@tool("list_project_versions", description="List all versions in a project (paginated)")
def list_project_versions(project_id_or_key: str, start_at: int = 0, max_results: int = 50, order_by: Optional[str] = None, query: Optional[str] = None, status: Optional[str] = None, expand: Optional[str] = None):
    """List all versions in a project (paginated)."""
    url = f"{API_ROOT}/project/{project_id_or_key}/version"
    params = {"startAt": start_at, "maxResults": max_results}
    if order_by:
        params["orderBy"] = order_by
    if query:
        params["query"] = query
    if status:
        params["status"] = status
    if expand:
        params["expand"] = expand
    resp = requests.get(url, headers=_auth_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("get_project_versions", description="Get all versions in a project (not paginated)")
def get_project_versions(project_id_or_key: str, expand: Optional[str] = None):
    """Get all versions in a project (not paginated)."""
    url = f"{API_ROOT}/project/{project_id_or_key}/versions"
    params = {}
    if expand:
        params["expand"] = expand
    resp = requests.get(url, headers=_auth_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("get_version", description="Get a single version by ID")
def get_version(version_id: str, expand: Optional[str] = None):
    """Get a single version by ID."""
    url = f"{API_ROOT}/version/{version_id}"
    params = {}
    if expand:
        params["expand"] = expand
    resp = requests.get(url, headers=_auth_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("create_version", description="Create a new version in a project")
def create_version(name: str, project_id: int, description: Optional[str] = None, released: Optional[bool] = None, release_date: Optional[str] = None, archived: Optional[bool] = None):
    """Create a new version in a project."""
    url = f"{API_ROOT}/version"
    data = {"name": name, "projectId": project_id}
    if description:
        data["description"] = description
    if released is not None:
        data["released"] = released
    if release_date:
        data["releaseDate"] = release_date
    if archived is not None:
        data["archived"] = archived
    resp = requests.post(url, headers={**_auth_headers(), "Content-Type": "application/json"}, json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("update_version", description="Update a version by ID")
def update_version(version_id: str, name: Optional[str] = None, description: Optional[str] = None, released: Optional[bool] = None, release_date: Optional[str] = None, archived: Optional[bool] = None):
    """Update a version by ID."""
    url = f"{API_ROOT}/version/{version_id}"
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if released is not None:
        data["released"] = released
    if release_date:
        data["releaseDate"] = release_date
    if archived is not None:
        data["archived"] = archived
    resp = requests.put(url, headers={**_auth_headers(), "Content-Type": "application/json"}, json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("delete_version", description="Delete a version by ID")
def delete_version(version_id: str, move_fix_issues_to: Optional[str] = None, move_affected_issues_to: Optional[str] = None):
    """Delete a version by ID. Optionally move issues to other versions."""
    url = f"{API_ROOT}/version/{version_id}"
    params = {}
    if move_fix_issues_to:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    resp = requests.delete(url, headers=_auth_headers(), params=params)
    if resp.status_code == 204:
        return {"result": "deleted"}
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("merge_versions", description="Merge two versions (delete one and move issues to another)")
def merge_versions(version_id: str, move_issues_to: str):
    """Merge two versions. Deletes version_id and moves issues to move_issues_to."""
    url = f"{API_ROOT}/version/{version_id}/mergeto/{move_issues_to}"
    resp = requests.put(url, headers=_auth_headers())
    if resp.status_code == 204:
        return {"result": "merged and deleted"}
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}
