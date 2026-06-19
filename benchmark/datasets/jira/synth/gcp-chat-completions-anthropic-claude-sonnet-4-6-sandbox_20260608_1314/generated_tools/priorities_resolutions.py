"""Issue priority and resolution tools."""
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

    # --- Priorities ---

    @mcp.tool()
    def get_priorities() -> dict:
        """Get all Jira issue priorities."""
        session, base = _client()
        r = session.get(f"{base}/priority")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_priority(priority_id: str) -> dict:
        """Get a specific Jira issue priority by ID."""
        session, base = _client()
        r = session.get(f"{base}/priority/{priority_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def search_priorities(priority_name: Optional[str] = None,
                           project_ids: Optional[List[str]] = None,
                           start_at: str = "0", max_results: str = "50") -> dict:
        """Search for Jira issue priorities with optional filters."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if priority_name:
            params["priorityName"] = priority_name
        if project_ids:
            params["projectId"] = project_ids
        r = session.get(f"{base}/priority/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_priority(name: str, status_color: str, description: Optional[str] = None,
                         icon_url: Optional[str] = None) -> dict:
        """Create a new Jira issue priority.
        status_color: hex color e.g. '#FF0000'"""
        session, base = _client()
        body: dict = {"name": name, "statusColor": status_color}
        if description:
            body["description"] = description
        if icon_url:
            body["iconUrl"] = icon_url
        r = session.post(f"{base}/priority", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_priority(priority_id: str, name: Optional[str] = None,
                         status_color: Optional[str] = None,
                         description: Optional[str] = None) -> dict:
        """Update a Jira issue priority."""
        session, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if status_color:
            body["statusColor"] = status_color
        if description is not None:
            body["description"] = description
        r = session.put(f"{base}/priority/{priority_id}", json=body)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def set_default_priority(priority_id: str) -> dict:
        """Set the default Jira issue priority."""
        session, base = _client()
        r = session.put(f"{base}/priority/default", json={"id": priority_id})
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    # --- Resolutions ---

    @mcp.tool()
    def get_resolutions() -> dict:
        """Get all Jira issue resolutions."""
        session, base = _client()
        r = session.get(f"{base}/resolution")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_resolution(resolution_id: str) -> dict:
        """Get a specific Jira issue resolution by ID."""
        session, base = _client()
        r = session.get(f"{base}/resolution/{resolution_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def search_resolutions(resolution_ids: Optional[List[str]] = None,
                            only_default: bool = False,
                            start_at: str = "0", max_results: str = "50") -> dict:
        """Search for Jira issue resolutions."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results, "onlyDefault": only_default}
        if resolution_ids:
            params["id"] = resolution_ids
        r = session.get(f"{base}/resolution/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_resolution(name: str, description: Optional[str] = None) -> dict:
        """Create a new Jira issue resolution."""
        session, base = _client()
        body: dict = {"name": name}
        if description:
            body["description"] = description
        r = session.post(f"{base}/resolution", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_resolution(resolution_id: str, name: str, description: Optional[str] = None) -> dict:
        """Update a Jira issue resolution."""
        session, base = _client()
        body: dict = {"name": name}
        if description is not None:
            body["description"] = description
        r = session.put(f"{base}/resolution/{resolution_id}", json=body)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def set_default_resolution(resolution_id: str) -> dict:
        """Set the default Jira issue resolution."""
        session, base = _client()
        r = session.put(f"{base}/resolution/default", json={"id": resolution_id})
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}
