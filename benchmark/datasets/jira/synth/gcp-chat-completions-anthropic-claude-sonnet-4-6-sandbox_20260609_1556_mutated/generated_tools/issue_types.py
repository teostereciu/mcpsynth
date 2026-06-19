"""Issue type tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    s = requests.Session()
    s.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return s, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_all_issue_types() -> dict:
        """Get all issue types available to the user."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issuetype")
            r.raise_for_status()
            return {"issueTypes": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_types_for_project(project_id: int, level: Optional[int] = None) -> dict:
        """Get issue types available for a specific project."""
        s, base = _client()
        params: dict = {"projectId": project_id}
        if level is not None:
            params["level"] = level
        try:
            r = s.get(f"{base}/issuetype/project", params=params)
            r.raise_for_status()
            return {"issueTypes": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_type(issue_type_id: str) -> dict:
        """Get a specific issue type by ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issuetype/{issue_type_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_issue_type(
        name: str,
        type: str = "standard",
        description: Optional[str] = None,
        hierarchy_level: Optional[int] = None,
    ) -> dict:
        """Create a new issue type. type: 'standard' or 'subtask'."""
        s, base = _client()
        body: dict = {"name": name, "type": type}
        if description:
            body["description"] = description
        if hierarchy_level is not None:
            body["hierarchyLevel"] = hierarchy_level
        try:
            r = s.post(f"{base}/issuetype", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_issue_type(
        issue_type_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        avatar_id: Optional[int] = None,
    ) -> dict:
        """Update an issue type."""
        s, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if avatar_id is not None:
            body["avatarId"] = avatar_id
        try:
            r = s.put(f"{base}/issuetype/{issue_type_id}", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_issue_type(issue_type_id: str, alternative_issue_type_id: Optional[str] = None) -> dict:
        """Delete an issue type."""
        s, base = _client()
        params = {}
        if alternative_issue_type_id:
            params["alternativeIssueTypeId"] = alternative_issue_type_id
        try:
            r = s.delete(f"{base}/issuetype/{issue_type_id}", params=params)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_alternative_issue_types(issue_type_id: str) -> dict:
        """Get alternative issue types for a given issue type."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issuetype/{issue_type_id}/alternatives")
            r.raise_for_status()
            return {"issueTypes": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
