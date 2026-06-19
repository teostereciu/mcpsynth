"""Dashboard tools: get, create, update, delete dashboards."""
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
    def get_all_dashboards(
        filter: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> dict:
        """Get all dashboards. filter: 'favourite' or 'my'."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if filter:
            params["filter"] = filter
        try:
            r = s.get(f"{base}/dashboard", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def search_dashboards(
        dashboard_name: Optional[str] = None,
        account_id: Optional[str] = None,
        project_id: Optional[int] = None,
        order_by: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> dict:
        """Search for dashboards with filtering."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if dashboard_name:
            params["dashboardName"] = dashboard_name
        if account_id:
            params["accountId"] = account_id
        if project_id is not None:
            params["projectId"] = project_id
        if order_by:
            params["orderBy"] = order_by
        try:
            r = s.get(f"{base}/dashboard/search", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_dashboard(dashboard_id: str) -> dict:
        """Get a specific dashboard by ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/dashboard/{dashboard_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_dashboard(
        name: str,
        share_permissions: List[dict],
        edit_permissions: Optional[List[dict]] = None,
        description: Optional[str] = None,
    ) -> dict:
        """Create a new dashboard. share_permissions: list of permission objects e.g. [{'type': 'global'}]."""
        s, base = _client()
        body: dict = {
            "name": name,
            "sharePermissions": share_permissions,
            "editPermissions": edit_permissions or [],
        }
        if description:
            body["description"] = description
        try:
            r = s.post(f"{base}/dashboard", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_dashboard(
        dashboard_id: str,
        name: str,
        share_permissions: List[dict],
        edit_permissions: Optional[List[dict]] = None,
        description: Optional[str] = None,
    ) -> dict:
        """Update an existing dashboard."""
        s, base = _client()
        body: dict = {
            "name": name,
            "sharePermissions": share_permissions,
            "editPermissions": edit_permissions or [],
        }
        if description is not None:
            body["description"] = description
        try:
            r = s.put(f"{base}/dashboard/{dashboard_id}", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_dashboard(dashboard_id: str) -> dict:
        """Delete a dashboard."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/dashboard/{dashboard_id}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def copy_dashboard(dashboard_id: str, name: str, description: Optional[str] = None) -> dict:
        """Copy a dashboard."""
        s, base = _client()
        body: dict = {"name": name, "sharePermissions": [], "editPermissions": []}
        if description:
            body["description"] = description
        try:
            r = s.post(f"{base}/dashboard/{dashboard_id}/copy", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_dashboard_gadgets(dashboard_id: int) -> dict:
        """Get gadgets on a dashboard."""
        s, base = _client()
        try:
            r = s.get(f"{base}/dashboard/{dashboard_id}/gadget")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_available_gadgets() -> dict:
        """Get all available gadgets that can be added to dashboards."""
        s, base = _client()
        try:
            r = s.get(f"{base}/dashboard/gadgets")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
