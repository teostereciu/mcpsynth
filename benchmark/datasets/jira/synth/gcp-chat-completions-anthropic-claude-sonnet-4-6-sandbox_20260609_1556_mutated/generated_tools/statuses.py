"""Status management tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, List
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    s = requests.Session()
    s.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return s, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_statuses_by_ids(status_ids: List[str]) -> dict:
        """Get statuses by their IDs."""
        s, base = _client()
        try:
            r = s.get(f"{base}/statuses", params=[("id", sid) for sid in status_ids])
            r.raise_for_status()
            return {"statuses": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_statuses_by_names(names: List[str], project_id: Optional[str] = None) -> dict:
        """Get statuses by their names."""
        s, base = _client()
        params_list = [("name", n) for n in names]
        if project_id:
            params_list.append(("projectId", project_id))
        try:
            r = s.get(f"{base}/statuses/byNames", params=params_list)
            r.raise_for_status()
            return {"statuses": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def search_statuses(
        project_id: Optional[str] = None,
        search_string: Optional[str] = None,
        status_category: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 200,
    ) -> dict:
        """Search for statuses with filtering."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if project_id:
            params["projectId"] = project_id
        if search_string:
            params["searchString"] = search_string
        if status_category:
            params["statusCategory"] = status_category
        try:
            r = s.get(f"{base}/statuses/search", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_statuses(scope_type: str, statuses: List[dict], project_id: Optional[str] = None) -> dict:
        """Create statuses. scope_type: 'PROJECT' or 'GLOBAL'. Each status: {name, statusCategory, description?}."""
        s, base = _client()
        scope: dict = {"type": scope_type}
        if project_id:
            scope["project"] = {"id": project_id}
        try:
            r = s.post(f"{base}/statuses", json={"scope": scope, "statuses": statuses})
            r.raise_for_status()
            return {"statuses": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_statuses(statuses: List[dict]) -> dict:
        """Update statuses by ID. Each status: {id, name, statusCategory, description?}."""
        s, base = _client()
        try:
            r = s.put(f"{base}/statuses", json={"statuses": statuses})
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_statuses(status_ids: List[str]) -> dict:
        """Delete statuses by their IDs."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/statuses", params=[("id", sid) for sid in status_ids])
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_workflow_statuses() -> dict:
        """Get all workflow statuses (legacy endpoint)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/status")
            r.raise_for_status()
            return {"statuses": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_workflow_status(id_or_name: str) -> dict:
        """Get a specific workflow status by ID or name."""
        s, base = _client()
        try:
            r = s.get(f"{base}/status/{id_or_name}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_status_categories() -> dict:
        """Get all status categories."""
        s, base = _client()
        try:
            r = s.get(f"{base}/statuscategory")
            r.raise_for_status()
            return {"statusCategories": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
