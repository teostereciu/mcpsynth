"""Issue field tools: get, create, update, delete fields."""
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
    def get_fields() -> dict:
        """Get all issue fields (system and custom)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/field")
            r.raise_for_status()
            return {"fields": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def search_fields(
        query: Optional[str] = None,
        field_type: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 50,
        order_by: Optional[str] = None,
    ) -> dict:
        """Search for fields with filtering. field_type: 'custom' or 'system'."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if field_type:
            params["type"] = field_type
        if order_by:
            params["orderBy"] = order_by
        try:
            r = s.get(f"{base}/field/search", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_custom_field(
        name: str,
        field_type: str,
        description: Optional[str] = None,
        searcher_key: Optional[str] = None,
    ) -> dict:
        """Create a new custom field. field_type e.g. 'com.atlassian.jira.plugin.system.customfieldtypes:textfield'."""
        s, base = _client()
        body: dict = {"name": name, "type": field_type}
        if description:
            body["description"] = description
        if searcher_key:
            body["searcherKey"] = searcher_key
        try:
            r = s.post(f"{base}/field", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_custom_field(
        field_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        searcher_key: Optional[str] = None,
    ) -> dict:
        """Update a custom field's name, description, or searcher."""
        s, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if searcher_key:
            body["searcherKey"] = searcher_key
        try:
            r = s.put(f"{base}/field/{field_id}", json=body)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_custom_field(field_id: str) -> dict:
        """Delete a custom field (async operation)."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/field/{field_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def trash_custom_field(field_id: str) -> dict:
        """Move a custom field to trash."""
        s, base = _client()
        try:
            r = s.post(f"{base}/field/{field_id}/trash")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def restore_custom_field(field_id: str) -> dict:
        """Restore a custom field from trash."""
        s, base = _client()
        try:
            r = s.post(f"{base}/field/{field_id}/restore")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_server_info() -> dict:
        """Get information about the Jira instance (version, build, etc.)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/serverInfo")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
