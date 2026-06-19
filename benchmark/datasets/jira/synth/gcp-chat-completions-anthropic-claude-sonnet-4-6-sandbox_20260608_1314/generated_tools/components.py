"""Project component tools: get, create, update, delete components."""
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
    def get_component(component_id: str) -> dict:
        """Get a Jira project component by ID."""
        session, base = _client()
        r = session.get(f"{base}/component/{component_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_component(project_key: str, name: str,
                          description: Optional[str] = None,
                          lead_account_id: Optional[str] = None,
                          assignee_type: Optional[str] = None) -> dict:
        """Create a new component in a Jira project.
        assignee_type: 'PROJECT_DEFAULT', 'COMPONENT_LEAD', 'PROJECT_LEAD', 'UNASSIGNED'"""
        session, base = _client()
        body: dict = {"project": project_key, "name": name}
        if description:
            body["description"] = description
        if lead_account_id:
            body["leadAccountId"] = lead_account_id
        if assignee_type:
            body["assigneeType"] = assignee_type
        r = session.post(f"{base}/component", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_component(component_id: str, name: Optional[str] = None,
                          description: Optional[str] = None,
                          lead_account_id: Optional[str] = None,
                          assignee_type: Optional[str] = None) -> dict:
        """Update a Jira project component."""
        session, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if lead_account_id is not None:
            body["leadAccountId"] = lead_account_id
        if assignee_type:
            body["assigneeType"] = assignee_type
        r = session.put(f"{base}/component/{component_id}", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_component(component_id: str, move_issues_to: Optional[str] = None) -> dict:
        """Delete a Jira project component. Optionally move its issues to another component."""
        session, base = _client()
        params = {}
        if move_issues_to:
            params["moveIssuesTo"] = move_issues_to
        r = session.delete(f"{base}/component/{component_id}", params=params)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_component_issue_counts(component_id: str) -> dict:
        """Get the count of issues for a Jira project component."""
        session, base = _client()
        r = session.get(f"{base}/component/{component_id}/relatedIssueCounts")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_project_components(project_id_or_key: str, start_at: int = 0,
                                max_results: int = 50, query: Optional[str] = None) -> dict:
        """Get a paginated list of components for a Jira project."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        r = session.get(f"{base}/project/{project_id_or_key}/component", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_project_components_all(project_id_or_key: str) -> dict:
        """Get all components for a Jira project (non-paginated)."""
        session, base = _client()
        r = session.get(f"{base}/project/{project_id_or_key}/components")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
