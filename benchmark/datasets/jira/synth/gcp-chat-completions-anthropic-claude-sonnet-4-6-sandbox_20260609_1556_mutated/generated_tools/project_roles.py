"""Project role tools."""
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
    def get_all_project_roles() -> dict:
        """Get all project roles defined in Jira."""
        s, base = _client()
        try:
            r = s.get(f"{base}/role")
            r.raise_for_status()
            return {"roles": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project_role_by_id(role_id: int) -> dict:
        """Get a project role by its ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/role/{role_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_project_role(name: str, description: Optional[str] = None) -> dict:
        """Create a new project role."""
        s, base = _client()
        body: dict = {"name": name}
        if description:
            body["description"] = description
        try:
            r = s.post(f"{base}/role", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_project_role(role_id: int, name: str, description: str) -> dict:
        """Update a project role's name and description."""
        s, base = _client()
        try:
            r = s.put(f"{base}/role/{role_id}", json={"name": name, "description": description})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_project_role(role_id: int, swap_with: Optional[int] = None) -> dict:
        """Delete a project role."""
        s, base = _client()
        params = {}
        if swap_with is not None:
            params["swap"] = swap_with
        try:
            r = s.delete(f"{base}/role/{role_id}", params=params)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project_roles_for_project(project_id_or_key: str) -> dict:
        """Get all roles for a specific project."""
        s, base = _client()
        try:
            r = s.get(f"{base}/project/{project_id_or_key}/role")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project_role_for_project(project_id_or_key: str, role_id: int) -> dict:
        """Get a specific role and its actors for a project."""
        s, base = _client()
        try:
            r = s.get(f"{base}/project/{project_id_or_key}/role/{role_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project_role_details(project_id_or_key: str) -> dict:
        """Get all role details for a project."""
        s, base = _client()
        try:
            r = s.get(f"{base}/project/{project_id_or_key}/roledetails")
            r.raise_for_status()
            return {"roleDetails": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
