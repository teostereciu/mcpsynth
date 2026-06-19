import os
import requests
from fastmcp import FastMCP
from typing import Any, Dict, List, Optional

mcp = FastMCP("jira")

JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

def get_auth():
    return (JIRA_EMAIL, JIRA_API_TOKEN)

def make_request(method: str, endpoint: str, **kwargs) -> Any:
    url = f"{JIRA_BASE_URL}/rest/api/3/{endpoint.lstrip('/')}"
    try:
        response = requests.request(method, url, auth=get_auth(), **kwargs)
        response.raise_for_status()
        if response.status_code == 204:
            return {"success": True}
        if not response.text:
            return {"success": True}
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}

@mcp.tool()
def get_issue(issue_id_or_key: str) -> Dict[str, Any]:
    """Get an issue by ID or key."""
    return make_request("GET", f"issue/{issue_id_or_key}")

@mcp.tool()
def create_issue(fields: Dict[str, Any]) -> Dict[str, Any]:
    """Create an issue. Provide fields like project, summary, description, issuetype."""
    return make_request("POST", "issue", json={"fields": fields})

@mcp.tool()
def update_issue(issue_id_or_key: str, fields: Dict[str, Any]) -> Dict[str, Any]:
    """Update an issue. Provide fields to update."""
    return make_request("PUT", f"issue/{issue_id_or_key}", json={"fields": fields})

@mcp.tool()
def delete_issue(issue_id_or_key: str) -> Dict[str, Any]:
    """Delete an issue."""
    return make_request("DELETE", f"issue/{issue_id_or_key}")

@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Dict[str, Any]:
    """Assign an issue to a user. Pass account_id, or None to unassign."""
    return make_request("PUT", f"issue/{issue_id_or_key}/assignee", json={"accountId": account_id})

@mcp.tool()
def get_transitions(issue_id_or_key: str) -> Dict[str, Any]:
    """Get available transitions for an issue."""
    return make_request("GET", f"issue/{issue_id_or_key}/transitions")

@mcp.tool()
def transition_issue(issue_id_or_key: str, transition_id: str) -> Dict[str, Any]:
    """Perform a transition on an issue."""
    return make_request("POST", f"issue/{issue_id_or_key}/transitions", json={"transition": {"id": transition_id}})

@mcp.tool()
def get_comments(issue_id_or_key: str) -> Dict[str, Any]:
    """Get comments for an issue."""
    return make_request("GET", f"issue/{issue_id_or_key}/comment")

@mcp.tool()
def add_comment(issue_id_or_key: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """Add a comment to an issue. Body must be an Atlassian Document Format object."""
    return make_request("POST", f"issue/{issue_id_or_key}/comment", json={"body": body})

@mcp.tool()
def get_worklogs(issue_id_or_key: str) -> Dict[str, Any]:
    """Get worklogs for an issue."""
    return make_request("GET", f"issue/{issue_id_or_key}/worklog")

@mcp.tool()
def add_worklog(issue_id_or_key: str, time_spent: str) -> Dict[str, Any]:
    """Add a worklog to an issue. time_spent e.g. '1d 2h 30m'."""
    return make_request("POST", f"issue/{issue_id_or_key}/worklog", json={"timeSpent": time_spent})

@mcp.tool()
def get_watchers(issue_id_or_key: str) -> Dict[str, Any]:
    """Get watchers for an issue."""
    return make_request("GET", f"issue/{issue_id_or_key}/watchers")

@mcp.tool()
def add_watcher(issue_id_or_key: str, account_id: str) -> Dict[str, Any]:
    """Add a watcher to an issue."""
    return make_request("POST", f"issue/{issue_id_or_key}/watchers", json=account_id)

@mcp.tool()
def remove_watcher(issue_id_or_key: str, account_id: str) -> Dict[str, Any]:
    """Remove a watcher from an issue."""
    return make_request("DELETE", f"issue/{issue_id_or_key}/watchers", params={"accountId": account_id})

@mcp.tool()
def add_attachment(issue_id_or_key: str, file_path: str) -> Dict[str, Any]:
    """Add an attachment to an issue. Provide the local file path."""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_id_or_key}/attachments"
    headers = {"X-Atlassian-Token": "no-check"}
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, auth=get_auth(), headers=headers, files=files)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def link_issues(type_name: str, inward_issue_key: str, outward_issue_key: str) -> Dict[str, Any]:
    """Create a link between two issues."""
    return make_request("POST", "issueLink", json={
        "type": {"name": type_name},
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key}
    })

@mcp.tool()
def search_issues(jql: str, max_results: int = 50) -> Dict[str, Any]:
    """Search for issues using JQL."""
    return make_request("POST", "search", json={"jql": jql, "maxResults": max_results})

@mcp.tool()
def get_project(project_id_or_key: str) -> Dict[str, Any]:
    """Get a project by ID or key."""
    return make_request("GET", f"project/{project_id_or_key}")

@mcp.tool()
def get_projects() -> Dict[str, Any]:
    """Get all projects."""
    return make_request("GET", "project/search")

@mcp.tool()
def get_components(project_id_or_key: str) -> Dict[str, Any]:
    """Get components for a project."""
    return make_request("GET", f"project/{project_id_or_key}/components")

@mcp.tool()
def create_component(name: str, project: str, description: Optional[str] = None) -> Dict[str, Any]:
    """Create a component."""
    data = {"name": name, "project": project}
    if description:
        data["description"] = description
    return make_request("POST", "component", json=data)

@mcp.tool()
def get_versions(project_id_or_key: str) -> Dict[str, Any]:
    """Get versions for a project."""
    return make_request("GET", f"project/{project_id_or_key}/versions")

@mcp.tool()
def create_version(name: str, project: str, description: Optional[str] = None) -> Dict[str, Any]:
    """Create a version."""
    data = {"name": name, "project": project}
    if description:
        data["description"] = description
    return make_request("POST", "version", json=data)

@mcp.tool()
def get_user(account_id: str) -> Dict[str, Any]:
    """Get a user by account ID."""
    return make_request("GET", "user", params={"accountId": account_id})

@mcp.tool()
def find_users(query: str) -> Dict[str, Any]:
    """Find users by query."""
    return make_request("GET", "user/search", params={"query": query})

@mcp.tool()
def get_group(groupname: str) -> Dict[str, Any]:
    """Get a group by name."""
    return make_request("GET", "group", params={"groupname": groupname})

@mcp.tool()
def get_filter(filter_id: str) -> Dict[str, Any]:
    """Get a filter by ID."""
    return make_request("GET", f"filter/{filter_id}")

@mcp.tool()
def get_issue_types() -> List[Dict[str, Any]]:
    """Get all issue types."""
    return make_request("GET", "issuetype")

@mcp.tool()
def get_priorities() -> List[Dict[str, Any]]:
    """Get all priorities."""
    return make_request("GET", "priority")

@mcp.tool()
def get_statuses() -> List[Dict[str, Any]]:
    """Get all statuses."""
    return make_request("GET", "status")

if __name__ == "__main__":
    mcp.run()
