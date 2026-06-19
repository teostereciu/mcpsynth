"""Issue property tools: get, set, delete issue properties."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, Any
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    s = requests.Session()
    s.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return s, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_issue_property_keys(issue_id_or_key: str) -> dict:
        """Get all property keys for an issue."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/properties")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_property(issue_id_or_key: str, property_key: str) -> dict:
        """Get the value of a specific issue property."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/properties/{property_key}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def set_issue_property(issue_id_or_key: str, property_key: str, value: Any) -> dict:
        """Set the value of an issue property. Value must be JSON-serializable."""
        s, base = _client()
        try:
            r = s.put(f"{base}/issue/{issue_id_or_key}/properties/{property_key}", json=value)
            if r.status_code in (200, 201):
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_issue_property(issue_id_or_key: str, property_key: str) -> dict:
        """Delete an issue property."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issue/{issue_id_or_key}/properties/{property_key}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
