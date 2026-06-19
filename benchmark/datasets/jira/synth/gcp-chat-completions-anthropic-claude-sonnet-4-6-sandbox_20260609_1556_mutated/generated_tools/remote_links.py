"""Issue remote link tools."""
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
    def get_remote_issue_links(issue_id_or_key: str, global_id: Optional[str] = None) -> dict:
        """Get remote issue links for an issue."""
        s, base = _client()
        params = {}
        if global_id:
            params["globalId"] = global_id
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/remotelink", params=params)
            r.raise_for_status()
            return r.json() if isinstance(r.json(), dict) else {"remoteLinks": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_or_update_remote_issue_link(
        issue_id_or_key: str,
        url: str,
        title: str,
        summary: Optional[str] = None,
        relationship: Optional[str] = None,
        global_id: Optional[str] = None,
        resolved: bool = False,
    ) -> dict:
        """Create or update a remote issue link (link to external system)."""
        s, base = _client()
        body: dict = {
            "object": {"url": url, "title": title, "status": {"resolved": resolved}}
        }
        if summary:
            body["object"]["summary"] = summary
        if relationship:
            body["relationship"] = relationship
        if global_id:
            body["globalId"] = global_id
        try:
            r = s.post(f"{base}/issue/{issue_id_or_key}/remotelink", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_remote_issue_link_by_id(issue_id_or_key: str, link_id: str) -> dict:
        """Get a specific remote issue link by its ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/remotelink/{link_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_remote_issue_link(
        issue_id_or_key: str,
        link_id: str,
        url: str,
        title: str,
        summary: Optional[str] = None,
        relationship: Optional[str] = None,
        global_id: Optional[str] = None,
        resolved: bool = False,
    ) -> dict:
        """Update a remote issue link by ID."""
        s, base = _client()
        body: dict = {
            "object": {"url": url, "title": title, "status": {"resolved": resolved}}
        }
        if summary:
            body["object"]["summary"] = summary
        if relationship:
            body["relationship"] = relationship
        if global_id:
            body["globalId"] = global_id
        try:
            r = s.put(f"{base}/issue/{issue_id_or_key}/remotelink/{link_id}", json=body)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_remote_issue_link_by_id(issue_id_or_key: str, link_id: str) -> dict:
        """Delete a remote issue link by its ID."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issue/{issue_id_or_key}/remotelink/{link_id}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_remote_issue_link_by_global_id(issue_id_or_key: str, global_id: str) -> dict:
        """Delete a remote issue link by its global ID."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issue/{issue_id_or_key}/remotelink",
                         params={"globalId": global_id})
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
