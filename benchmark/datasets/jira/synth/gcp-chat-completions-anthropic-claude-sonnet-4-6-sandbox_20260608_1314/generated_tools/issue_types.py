"""Issue type tools: get, create, update, delete issue types."""
from mcp.server.fastmcp import FastMCP
from typing import Optional
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_all_issue_types() -> dict:
        """Get all Jira issue types available to the current user."""
        session, base = _client()
        r = session.get(f"{base}/issuetype")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_type(issue_type_id: str) -> dict:
        """Get a specific Jira issue type by ID."""
        session, base = _client()
        r = session.get(f"{base}/issuetype/{issue_type_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_types_for_project(project_id: int, level: Optional[int] = None) -> dict:
        """Get issue types available for a specific Jira project."""
        session, base = _client()
        params: dict = {"projectId": project_id}
        if level is not None:
            params["level"] = level
        r = session.get(f"{base}/issuetype/project", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_issue_type(name: str, description: Optional[str] = None,
                           type_: str = "standard", hierarchy_level: Optional[int] = None) -> dict:
        """Create a new Jira issue type.
        type_: 'standard' or 'subtask'"""
        session, base = _client()
        body: dict = {"name": name, "type": type_}
        if description:
            body["description"] = description
        if hierarchy_level is not None:
            body["hierarchyLevel"] = hierarchy_level
        r = session.post(f"{base}/issuetype", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_issue_type(issue_type_id: str, name: Optional[str] = None,
                           description: Optional[str] = None,
                           avatar_id: Optional[int] = None) -> dict:
        """Update a Jira issue type."""
        session, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if avatar_id:
            body["avatarId"] = avatar_id
        r = session.put(f"{base}/issuetype/{issue_type_id}", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_issue_type(issue_type_id: str, alternative_issue_type_id: Optional[str] = None) -> dict:
        """Delete a Jira issue type. Optionally provide an alternative type to replace it."""
        session, base = _client()
        params: dict = {}
        if alternative_issue_type_id:
            params["alternativeIssueTypeId"] = alternative_issue_type_id
        r = session.delete(f"{base}/issuetype/{issue_type_id}", params=params)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_alternative_issue_types(issue_type_id: str) -> dict:
        """Get alternative issue types that can replace a given issue type."""
        session, base = _client()
        r = session.get(f"{base}/issuetype/{issue_type_id}/alternatives")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
