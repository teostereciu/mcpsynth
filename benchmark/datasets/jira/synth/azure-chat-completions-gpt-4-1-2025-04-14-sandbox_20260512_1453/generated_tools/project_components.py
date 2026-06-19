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

@tool("list_project_components", description="List all components in a project (paginated)")
def list_project_components(project_id_or_key: str, start_at: int = 0, max_results: int = 50, order_by: Optional[str] = None, query: Optional[str] = None):
    """List all components in a project (paginated)."""
    url = f"{API_ROOT}/project/{project_id_or_key}/component"
    params = {"startAt": start_at, "maxResults": max_results}
    if order_by:
        params["orderBy"] = order_by
    if query:
        params["query"] = query
    resp = requests.get(url, headers=_auth_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("get_project_components", description="Get all components in a project (not paginated)")
def get_project_components(project_id_or_key: str):
    """Get all components in a project (not paginated)."""
    url = f"{API_ROOT}/project/{project_id_or_key}/components"
    resp = requests.get(url, headers=_auth_headers())
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("get_component", description="Get a single component by ID")
def get_component(component_id: str):
    """Get a single component by ID."""
    url = f"{API_ROOT}/component/{component_id}"
    resp = requests.get(url, headers=_auth_headers())
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("create_component", description="Create a new component in a project")
def create_component(name: str, project: str, description: Optional[str] = None, lead_account_id: Optional[str] = None, assignee_type: Optional[str] = None):
    """Create a new component in a project."""
    url = f"{API_ROOT}/component"
    data = {"name": name, "project": project}
    if description:
        data["description"] = description
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    if assignee_type:
        data["assigneeType"] = assignee_type
    resp = requests.post(url, headers={**_auth_headers(), "Content-Type": "application/json"}, json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("update_component", description="Update a component by ID")
def update_component(component_id: str, name: Optional[str] = None, description: Optional[str] = None, lead_account_id: Optional[str] = None, assignee_type: Optional[str] = None):
    """Update a component by ID."""
    url = f"{API_ROOT}/component/{component_id}"
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if lead_account_id is not None:
        data["leadAccountId"] = lead_account_id
    if assignee_type:
        data["assigneeType"] = assignee_type
    resp = requests.put(url, headers={**_auth_headers(), "Content-Type": "application/json"}, json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("delete_component", description="Delete a component by ID")
def delete_component(component_id: str, move_issues_to: Optional[str] = None):
    """Delete a component by ID. Optionally move issues to another component."""
    url = f"{API_ROOT}/component/{component_id}"
    params = {}
    if move_issues_to:
        params["moveIssuesTo"] = move_issues_to
    resp = requests.delete(url, headers=_auth_headers(), params=params)
    if resp.status_code == 204:
        return {"result": "deleted"}
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}

@tool("get_component_issue_counts", description="Get counts of issues assigned to a component")
def get_component_issue_counts(component_id: str):
    """Get counts of issues assigned to a component."""
    url = f"{API_ROOT}/component/{component_id}/relatedIssueCounts"
    resp = requests.get(url, headers=_auth_headers())
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text}
