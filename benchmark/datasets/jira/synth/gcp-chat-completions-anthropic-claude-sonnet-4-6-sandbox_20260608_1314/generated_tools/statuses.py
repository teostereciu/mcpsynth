"""Status management tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, List
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_statuses_by_ids(status_ids: List[str]) -> dict:
        """Get Jira statuses by their IDs."""
        session, base = _client()
        r = session.get(f"{base}/statuses", params={"id": status_ids})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_statuses_by_names(names: List[str], project_id: Optional[str] = None) -> dict:
        """Get Jira statuses by their names."""
        session, base = _client()
        params: dict = {"name": names}
        if project_id:
            params["projectId"] = project_id
        r = session.get(f"{base}/statuses/byNames", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def search_statuses(project_id: Optional[str] = None, search_string: Optional[str] = None,
                         status_category: Optional[str] = None,
                         start_at: int = 0, max_results: int = 200) -> dict:
        """Search for Jira statuses with optional filters.
        status_category: 'TODO', 'IN_PROGRESS', 'DONE'"""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if project_id:
            params["projectId"] = project_id
        if search_string:
            params["searchString"] = search_string
        if status_category:
            params["statusCategory"] = status_category
        r = session.get(f"{base}/statuses/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_statuses(scope_type: str, statuses: List[dict],
                         project_id: Optional[str] = None) -> dict:
        """Create new Jira statuses for a project or global scope.
        scope_type: 'PROJECT' or 'GLOBAL'
        statuses: list of dicts with 'name', 'statusCategory' ('TODO'|'IN_PROGRESS'|'DONE'), and optional 'description'
        project_id: required when scope_type='PROJECT'"""
        session, base = _client()
        scope: dict = {"type": scope_type}
        if project_id:
            scope["project"] = {"id": project_id}
        body = {"scope": scope, "statuses": statuses}
        r = session.post(f"{base}/statuses", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_statuses(statuses: List[dict]) -> dict:
        """Update Jira statuses by ID. Each dict must have 'id', 'name', 'statusCategory'."""
        session, base = _client()
        r = session.put(f"{base}/statuses", json={"statuses": statuses})
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_statuses(status_ids: List[str]) -> dict:
        """Delete Jira statuses by their IDs."""
        session, base = _client()
        r = session.delete(f"{base}/statuses", params={"id": status_ids})
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}
