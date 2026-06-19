import os
import requests
from typing import Any, Dict, List, Optional, Union
from fastmcp import FastMCP

mcp = FastMCP("jira-server")

class JiraClient:
    def __init__(self):
        self.base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        self.email = os.environ.get("JIRA_EMAIL")
        self.api_token = os.environ.get("JIRA_API_TOKEN")
        
        if not self.base_url or not self.email or not self.api_token:
            raise ValueError("Missing required environment variables: JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN")
            
        self.api_base = f"{self.base_url}/rest/api/3"
        self.session = requests.Session()
        self.session.auth = (self.email, self.api_token)
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def request(self, method: str, path: str, **kwargs) -> Any:
        url = f"{self.api_base}{path}"
        try:
            response = self.session.request(method, url, **kwargs)
            if response.status_code == 204:
                return {"success": True}
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                try:
                    return {"error": e.response.json()}
                except ValueError:
                    return {"error": e.response.text}
            return {"error": str(e)}

client = JiraClient()

@mcp.tool()
def search_issues(jql: str, start_at: int = 0, max_results: int = 50, fields: Optional[List[str]] = None) -> Dict[str, Any]:
    """Search for issues using JQL (Jira Query Language)."""
    payload = {
        "jql": jql,
        "startAt": start_at,
        "maxResults": max_results
    }
    if fields:
        payload["fields"] = fields
    return client.request("POST", "/search", json=payload)

@mcp.tool()
def get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get a single issue by ID or key."""
    params = {}
    if fields:
        params["fields"] = ",".join(fields)
    return client.request("GET", f"/issue/{issue_id_or_key}", params=params)

@mcp.tool()
def create_issue(project_key: str, summary: str, issue_type: str, description: Optional[str] = None, assignee_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a new issue."""
    fields = {
        "project": {"key": project_key},
        "summary": summary,
        "issuetype": {"name": issue_type}
    }
    
    if description:
        fields["description"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": description
                        }
                    ]
                }
            ]
        }
        
    if assignee_id:
        fields["assignee"] = {"id": assignee_id}
        
    return client.request("POST", "/issue", json={"fields": fields})

@mcp.tool()
def update_issue(issue_id_or_key: str, summary: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing issue."""
    fields = {}
    if summary:
        fields["summary"] = summary
    if description:
        fields["description"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": description
                        }
                    ]
                }
            ]
        }
        
    if not fields:
        return {"error": "No fields to update provided."}
        
    return client.request("PUT", f"/issue/{issue_id_or_key}", json={"fields": fields})

@mcp.tool()
def delete_issue(issue_id_or_key: str) -> Dict[str, Any]:
    """Delete an issue."""
    return client.request("DELETE", f"/issue/{issue_id_or_key}")

@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: Optional[str]) -> Dict[str, Any]:
    """Assign an issue to a user. Pass None or empty string to unassign."""
    payload = {"accountId": account_id} if account_id else {"accountId": None}
    return client.request("PUT", f"/issue/{issue_id_or_key}/assignee", json=payload)

@mcp.tool()
def get_transitions(issue_id_or_key: str) -> Dict[str, Any]:
    """Get a list of transitions possible for this issue by the current user."""
    return client.request("GET", f"/issue/{issue_id_or_key}/transitions")

@mcp.tool()
def transition_issue(issue_id_or_key: str, transition_id: str) -> Dict[str, Any]:
    """Perform a transition on an issue."""
    return client.request("POST", f"/issue/{issue_id_or_key}/transitions", json={"transition": {"id": transition_id}})

@mcp.tool()
def add_comment(issue_id_or_key: str, comment_text: str) -> Dict[str, Any]:
    """Add a comment to an issue."""
    payload = {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": comment_text
                        }
                    ]
                }
            ]
        }
    }
    return client.request("POST", f"/issue/{issue_id_or_key}/comment", json=payload)

@mcp.tool()
def get_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> Dict[str, Any]:
    """Get comments for an issue."""
    params = {"startAt": start_at, "maxResults": max_results}
    return client.request("GET", f"/issue/{issue_id_or_key}/comment", params=params)

@mcp.tool()
def add_worklog(issue_id_or_key: str, time_spent: str, comment: Optional[str] = None) -> Dict[str, Any]:
    """Add a worklog to an issue. time_spent format: '1d 2h 30m'."""
    payload = {"timeSpent": time_spent}
    if comment:
        payload["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": comment
                        }
                    ]
                }
            ]
        }
    return client.request("POST", f"/issue/{issue_id_or_key}/worklog", json=payload)

@mcp.tool()
def get_issue_worklogs(issue_id_or_key: str) -> Dict[str, Any]:
    """Get worklogs for an issue."""
    return client.request("GET", f"/issue/{issue_id_or_key}/worklog")

@mcp.tool()
def add_watcher(issue_id_or_key: str, account_id: str) -> Dict[str, Any]:
    """Add a watcher to an issue."""
    return client.request("POST", f"/issue/{issue_id_or_key}/watchers", json=account_id)

@mcp.tool()
def get_watchers(issue_id_or_key: str) -> Dict[str, Any]:
    """Get watchers for an issue."""
    return client.request("GET", f"/issue/{issue_id_or_key}/watchers")

@mcp.tool()
def link_issues(type_name: str, inward_issue_key: str, outward_issue_key: str) -> Dict[str, Any]:
    """Create a link between two issues. type_name is the name of the issue link type (e.g., 'Blocks', 'Relates')."""
    payload = {
        "type": {"name": type_name},
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key}
    }
    return client.request("POST", "/issueLink", json=payload)

@mcp.tool()
def add_attachment(issue_id_or_key: str, file_path: str) -> Dict[str, Any]:
    """Add an attachment to an issue."""
    url = f"{client.api_base}/issue/{issue_id_or_key}/attachments"
    headers = {"X-Atlassian-Token": "no-check"}
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = client.session.post(url, headers=headers, files=files)
            response.raise_for_status()
            return {"attachments": response.json()}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_projects() -> Dict[str, Any]:
    """Get all projects visible to the user."""
    return client.request("GET", "/project")

@mcp.tool()
def get_project(project_id_or_key: str) -> Dict[str, Any]:
    """Get details of a specific project."""
    return client.request("GET", f"/project/{project_id_or_key}")

@mcp.tool()
def get_components(project_id_or_key: str) -> Dict[str, Any]:
    """Get components for a project."""
    return client.request("GET", f"/project/{project_id_or_key}/components")

@mcp.tool()
def get_versions(project_id_or_key: str) -> Dict[str, Any]:
    """Get versions for a project."""
    return client.request("GET", f"/project/{project_id_or_key}/versions")

@mcp.tool()
def get_users(query: str = "", start_at: int = 0, max_results: int = 50) -> Dict[str, Any]:
    """Search for users by name or email."""
    params = {"query": query, "startAt": start_at, "maxResults": max_results}
    return client.request("GET", "/user/search", params=params)

@mcp.tool()
def get_groups(query: str = "", start_at: int = 0, max_results: int = 50) -> Dict[str, Any]:
    """Search for groups."""
    params = {"query": query, "startAt": start_at, "maxResults": max_results}
    return client.request("GET", "/group/bulk", params=params)

@mcp.tool()
def get_filters(query: str = "", start_at: int = 0, max_results: int = 50) -> Dict[str, Any]:
    """Search for filters."""
    params = {"filterName": query, "startAt": start_at, "maxResults": max_results}
    return client.request("GET", "/filter/search", params=params)

@mcp.tool()
def get_issue_types() -> Dict[str, Any]:
    """Get all issue types."""
    return client.request("GET", "/issuetype")

@mcp.tool()
def get_priorities() -> Dict[str, Any]:
    """Get all priorities."""
    return client.request("GET", "/priority")

@mcp.tool()
def get_statuses() -> Dict[str, Any]:
    """Get all statuses."""
    return client.request("GET", "/status")

if __name__ == "__main__":
    mcp.run()
