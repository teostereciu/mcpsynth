"""Issue resolution tools."""
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
    def get_resolutions() -> dict:
        """Get all issue resolutions."""
        s, base = _client()
        try:
            r = s.get(f"{base}/resolution")
            r.raise_for_status()
            return {"resolutions": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def search_resolutions(
        start_at: int = 0,
        max_results: int = 50,
        resolution_ids: Optional[List[str]] = None,
        only_default: bool = False,
    ) -> dict:
        """Search for resolutions with filtering."""
        s, base = _client()
        params: dict = {"startAt": str(start_at), "maxResults": str(max_results), "onlyDefault": only_default}
        try:
            if resolution_ids:
                r = s.get(f"{base}/resolution/search",
                          params=[("startAt", str(start_at)), ("maxResults", str(max_results))] +
                          [("id", rid) for rid in resolution_ids])
            else:
                r = s.get(f"{base}/resolution/search", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_resolution(resolution_id: str) -> dict:
        """Get a specific resolution by ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/resolution/{resolution_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_resolution(name: str, description: Optional[str] = None) -> dict:
        """Create a new issue resolution."""
        s, base = _client()
        body: dict = {"name": name}
        if description:
            body["description"] = description
        try:
            r = s.post(f"{base}/resolution", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_resolution(resolution_id: str, name: str, description: Optional[str] = None) -> dict:
        """Update an issue resolution."""
        s, base = _client()
        body: dict = {"name": name}
        if description is not None:
            body["description"] = description
        try:
            r = s.put(f"{base}/resolution/{resolution_id}", json=body)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_resolution(resolution_id: str, replace_with: str) -> dict:
        """Delete a resolution (async). replace_with: ID of resolution to use instead."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/resolution/{resolution_id}", params={"replaceWith": replace_with})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def set_default_resolution(resolution_id: str) -> dict:
        """Set the default issue resolution."""
        s, base = _client()
        try:
            r = s.put(f"{base}/resolution/default", json={"id": resolution_id})
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
