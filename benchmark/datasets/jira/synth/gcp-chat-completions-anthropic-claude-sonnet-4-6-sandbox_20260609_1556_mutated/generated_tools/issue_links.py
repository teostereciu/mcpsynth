"""Issue link tools: create, get, delete links between issues."""
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
    def create_issue_link(
        link_type_name: str,
        inward_issue_key: str,
        outward_issue_key: str,
        comment_text: Optional[str] = None,
    ) -> dict:
        """Create a link between two issues. link_type_name e.g. 'Duplicate', 'Blocks', 'Relates'."""
        s, base = _client()
        body: dict = {
            "type": {"name": link_type_name},
            "inwardIssue": {"key": inward_issue_key},
            "outwardIssue": {"key": outward_issue_key},
        }
        if comment_text:
            body["comment"] = {
                "body": {
                    "type": "doc", "version": 1,
                    "content": [{"type": "paragraph", "content": [{"type": "text", "text": comment_text}]}]
                }
            }
        try:
            r = s.post(f"{base}/issueLink", json=body)
            if r.status_code == 201:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_link(link_id: str) -> dict:
        """Get details of an issue link by its ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issueLink/{link_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_issue_link(link_id: str) -> dict:
        """Delete an issue link by its ID."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issueLink/{link_id}")
            if r.status_code in (200, 204):
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_link_types() -> dict:
        """Get all available issue link types."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issueLinkType")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_issue_link_type(
        name: str,
        inward: str,
        outward: str,
    ) -> dict:
        """Create a new issue link type."""
        s, base = _client()
        try:
            r = s.post(f"{base}/issueLinkType", json={"name": name, "inward": inward, "outward": outward})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_link_type(link_type_id: str) -> dict:
        """Get a specific issue link type by ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issueLinkType/{link_type_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_issue_link_type(
        link_type_id: str,
        name: str,
        inward: str,
        outward: str,
    ) -> dict:
        """Update an issue link type."""
        s, base = _client()
        try:
            r = s.put(f"{base}/issueLinkType/{link_type_id}",
                      json={"name": name, "inward": inward, "outward": outward})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_issue_link_type(link_type_id: str) -> dict:
        """Delete an issue link type."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issueLinkType/{link_type_id}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
