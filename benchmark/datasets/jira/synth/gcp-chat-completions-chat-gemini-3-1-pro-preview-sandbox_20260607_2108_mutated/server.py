import os
import json
import requests
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira")

def get_base_url() -> str:
    base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
    if not base_url:
        raise ValueError("JIRA_BASE_URL environment variable is required")
    return f"{base_url}/rest/api/3"

def get_auth() -> tuple[str, str]:
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    if not email or not token:
        raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN environment variables are required")
    return (email, token)

def make_request(method: str, endpoint: str, **kwargs) -> Any:
    url = f"{get_base_url()}{endpoint}"
    auth = get_auth()
    
    headers = kwargs.pop("headers", {})
    headers.setdefault("Accept", "application/json")
    if method in ["POST", "PUT", "PATCH"]:
        headers.setdefault("Content-Type", "application/json")
        
    try:
        response = requests.request(method, url, auth=auth, headers=headers, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except requests.exceptions.HTTPError as e:
        try:
            error_data = e.response.json()
            return {"error": str(e), "details": error_data}
        except Exception:
            return {"error": str(e), "content": e.response.text}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_issue(issue_id_or_key: str) -> Any:
    """Get an issue by ID or key."""
    return make_request("GET", f"/issue/{issue_id_or_key}")

@mcp.tool()
def create_issue(fields: Dict[str, Any]) -> Any:
    """Create an issue."""
    return make_request("POST", "/issue", json={"fields": fields})

@mcp.tool()
def edit_issue(issue_id_or_key: str, fields: Dict[str, Any]) -> Any:
    """Edit an issue."""
    return make_request("PUT", f"/issue/{issue_id_or_key}", json={"fields": fields})

@mcp.tool()
def delete_issue(issue_id_or_key: str) -> Any:
    """Delete an issue."""
    return make_request("DELETE", f"/issue/{issue_id_or_key}")

@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: str) -> Any:
    """Assign an issue to a user."""
    return make_request("PUT", f"/issue/{issue_id_or_key}/assignee", json={"accountId": account_id})

@mcp.tool()
def get_transitions(issue_id_or_key: str) -> Any:
    """Get available transitions for an issue."""
    return make_request("GET", f"/issue/{issue_id_or_key}/transitions")

@mcp.tool()
def transition_issue(issue_id_or_key: str, transition_id: str) -> Any:
    """Transition an issue."""
    return make_request("POST", f"/issue/{issue_id_or_key}/transitions", json={"transition": {"id": transition_id}})

@mcp.tool()
def add_comment(issue_id_or_key: str, body: Dict[str, Any]) -> Any:
    """Add a comment to an issue. Body must be in Atlassian Document Format."""
    return make_request("POST", f"/issue/{issue_id_or_key}/comment", json={"body": body})

@mcp.tool()
def get_comments(issue_id_or_key: str) -> Any:
    """Get comments for an issue."""
    return make_request("GET", f"/issue/{issue_id_or_key}/comment")

@mcp.tool()
def add_worklog(issue_id_or_key: str, time_spent: str) -> Any:
    """Add a worklog to an issue."""
    return make_request("POST", f"/issue/{issue_id_or_key}/worklog", json={"timeSpent": time_spent})

@mcp.tool()
def get_worklogs(issue_id_or_key: str) -> Any:
    """Get worklogs for an issue."""
    return make_request("GET", f"/issue/{issue_id_or_key}/worklog")

@mcp.tool()
def search_issues(jql: str, max_results: int = 50) -> Any:
    """Search for issues using JQL."""
    return make_request("GET", "/search", params={"jql": jql, "maxResults": max_results})

@mcp.tool()
def get_project(project_id_or_key: str) -> Any:
    """Get a project by ID or key."""
    return make_request("GET", f"/project/{project_id_or_key}")

@mcp.tool()
def get_projects() -> Any:
    """Get all projects."""
    return make_request("GET", "/project")

@mcp.tool()
def get_components(project_id_or_key: str) -> Any:
    """Get components for a project."""
    return make_request("GET", f"/project/{project_id_or_key}/components")

@mcp.tool()
def get_versions(project_id_or_key: str) -> Any:
    """Get versions for a project."""
    return make_request("GET", f"/project/{project_id_or_key}/versions")

@mcp.tool()
def get_users(query: str) -> Any:
    """Search for users."""
    return make_request("GET", "/user/search", params={"query": query})

@mcp.tool()
def get_groups() -> Any:
    """Get groups."""
    return make_request("GET", "/group/bulk")

@mcp.tool()
def get_filters() -> Any:
    """Get filters."""
    return make_request("GET", "/filter")

@mcp.tool()
def get_issue_types() -> Any:
    """Get issue types."""
    return make_request("GET", "/issuetype")

@mcp.tool()
def get_priorities() -> Any:
    """Get priorities."""
    return make_request("GET", "/priority")

@mcp.tool()
def get_statuses() -> Any:
    """Get statuses."""
    return make_request("GET", "/status")

if __name__ == "__main__":
    mcp.run()
