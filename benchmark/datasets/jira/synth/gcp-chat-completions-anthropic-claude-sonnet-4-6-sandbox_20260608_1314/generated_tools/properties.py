"""Issue property tools and server info."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, Any
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_server_info() -> dict:
        """Get information about the Jira instance (version, build number, server time, etc.)."""
        session, base = _client()
        r = session.get(f"{base}/serverInfo")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_property_keys(issue_id_or_key: str) -> dict:
        """Get all property keys for a Jira issue."""
        session, base = _client()
        r = session.get(f"{base}/issue/{issue_id_or_key}/properties")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_property(issue_id_or_key: str, property_key: str) -> dict:
        """Get the value of a specific property on a Jira issue."""
        session, base = _client()
        r = session.get(f"{base}/issue/{issue_id_or_key}/properties/{property_key}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def set_issue_property(issue_id_or_key: str, property_key: str, value: Any) -> dict:
        """Set a property value on a Jira issue. Value must be a JSON-serializable object."""
        session, base = _client()
        r = session.put(f"{base}/issue/{issue_id_or_key}/properties/{property_key}", json=value)
        if r.ok:
            return r.json() if r.text else {"success": True}
        if r.status_code in (200, 201, 204):
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_issue_property(issue_id_or_key: str, property_key: str) -> dict:
        """Delete a property from a Jira issue."""
        session, base = _client()
        r = session.delete(f"{base}/issue/{issue_id_or_key}/properties/{property_key}")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_my_preferences(key: str) -> dict:
        """Get the value of a preference for the current Jira user."""
        session, base = _client()
        r = session.get(f"{base}/mypreferences", params={"key": key})
        if r.ok:
            return {"key": key, "value": r.json()}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_my_locale() -> dict:
        """Get the locale setting for the current Jira user."""
        session, base = _client()
        r = session.get(f"{base}/mypreferences/locale")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
