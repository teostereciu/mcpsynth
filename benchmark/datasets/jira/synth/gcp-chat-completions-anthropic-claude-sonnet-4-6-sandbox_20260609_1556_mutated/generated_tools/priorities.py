"""Issue priority tools."""
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
    def get_priorities() -> dict:
        """Get all issue priorities."""
        s, base = _client()
        try:
            r = s.get(f"{base}/priority")
            r.raise_for_status()
            return {"priorities": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def search_priorities(
        start_at: int = 0,
        max_results: int = 50,
        priority_name: Optional[str] = None,
        only_default: bool = False,
        project_ids: Optional[List[str]] = None,
    ) -> dict:
        """Search for priorities with filtering."""
        s, base = _client()
        params: dict = {"startAt": str(start_at), "maxResults": str(max_results), "onlyDefault": only_default}
        if priority_name:
            params["priorityName"] = priority_name
        try:
            if project_ids:
                r = s.get(f"{base}/priority/search",
                          params=[("startAt", str(start_at)), ("maxResults", str(max_results))] +
                          [("projectId", pid) for pid in project_ids])
            else:
                r = s.get(f"{base}/priority/search", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_priority(priority_id: str) -> dict:
        """Get a specific priority by ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/priority/{priority_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_priority(
        name: str,
        status_color: str,
        description: Optional[str] = None,
        icon_url: Optional[str] = None,
    ) -> dict:
        """Create a new issue priority."""
        s, base = _client()
        body: dict = {"name": name, "statusColor": status_color}
        if description:
            body["description"] = description
        if icon_url:
            body["iconUrl"] = icon_url
        try:
            r = s.post(f"{base}/priority", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_priority(
        priority_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status_color: Optional[str] = None,
        icon_url: Optional[str] = None,
    ) -> dict:
        """Update an existing priority."""
        s, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if status_color:
            body["statusColor"] = status_color
        if icon_url:
            body["iconUrl"] = icon_url
        try:
            r = s.put(f"{base}/priority/{priority_id}", json=body)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_priority(priority_id: str) -> dict:
        """Delete a priority (async operation)."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/priority/{priority_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def set_default_priority(priority_id: str) -> dict:
        """Set the default issue priority."""
        s, base = _client()
        try:
            r = s.put(f"{base}/priority/default", json={"id": priority_id})
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def move_priorities(priority_ids: List[str], after: Optional[str] = None, position: Optional[str] = None) -> dict:
        """Change the order of priorities. position: 'First', 'Last'."""
        s, base = _client()
        body: dict = {"ids": priority_ids}
        if after:
            body["after"] = after
        if position:
            body["position"] = position
        try:
            r = s.put(f"{base}/priority/move", json=body)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
