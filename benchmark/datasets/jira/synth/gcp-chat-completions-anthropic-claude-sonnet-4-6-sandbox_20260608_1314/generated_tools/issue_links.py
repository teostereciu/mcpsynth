"""Issue links and link types tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def create_issue_link(link_type_name: str, inward_issue_key: str, outward_issue_key: str,
                           comment_text: Optional[str] = None) -> dict:
        """Create a link between two Jira issues.
        link_type_name: e.g. 'Duplicate', 'Blocks', 'Relates to'
        inward_issue_key: the inward (e.g. 'is blocked by') issue key
        outward_issue_key: the outward (e.g. 'blocks') issue key"""
        session, base = _client()
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
        r = session.post(f"{base}/issueLink", json=body)
        if r.status_code in (200, 201):
            return r.json() if r.text else {"success": True}
        if r.status_code == 201:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_link(link_id: str) -> dict:
        """Get details of a specific issue link by its ID."""
        session, base = _client()
        r = session.get(f"{base}/issueLink/{link_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_issue_link(link_id: str) -> dict:
        """Delete an issue link by its ID."""
        session, base = _client()
        r = session.delete(f"{base}/issueLink/{link_id}")
        if r.status_code in (200, 204):
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_link_types() -> dict:
        """Get all available issue link types (e.g. Duplicate, Blocks, Relates to)."""
        session, base = _client()
        r = session.get(f"{base}/issueLinkType")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_link_type(issue_link_type_id: str) -> dict:
        """Get a specific issue link type by ID."""
        session, base = _client()
        r = session.get(f"{base}/issueLinkType/{issue_link_type_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_issue_link_type(name: str, inward: str, outward: str) -> dict:
        """Create a new issue link type.
        name: e.g. 'Duplicate'
        inward: description for inward direction e.g. 'is duplicated by'
        outward: description for outward direction e.g. 'duplicates'"""
        session, base = _client()
        body = {"name": name, "inward": inward, "outward": outward}
        r = session.post(f"{base}/issueLinkType", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_issue_link_type(issue_link_type_id: str, name: str, inward: str, outward: str) -> dict:
        """Update an existing issue link type."""
        session, base = _client()
        body = {"name": name, "inward": inward, "outward": outward}
        r = session.put(f"{base}/issueLinkType/{issue_link_type_id}", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_issue_link_type(issue_link_type_id: str) -> dict:
        """Delete an issue link type by ID."""
        session, base = _client()
        r = session.delete(f"{base}/issueLinkType/{issue_link_type_id}")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_remote_issue_links(issue_id_or_key: str, global_id: Optional[str] = None) -> dict:
        """Get remote issue links for a Jira issue (links to external systems)."""
        session, base = _client()
        params = {}
        if global_id:
            params["globalId"] = global_id
        r = session.get(f"{base}/issue/{issue_id_or_key}/remotelink", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_remote_issue_link(issue_id_or_key: str, url: str, title: str,
                                  relationship: Optional[str] = None,
                                  global_id: Optional[str] = None,
                                  summary: Optional[str] = None) -> dict:
        """Create or update a remote issue link (link to an external system/URL) on a Jira issue."""
        session, base = _client()
        body: dict = {
            "object": {"url": url, "title": title}
        }
        if summary:
            body["object"]["summary"] = summary
        if relationship:
            body["relationship"] = relationship
        if global_id:
            body["globalId"] = global_id
        r = session.post(f"{base}/issue/{issue_id_or_key}/remotelink", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_remote_issue_link_by_id(issue_id_or_key: str, link_id: str) -> dict:
        """Delete a remote issue link from a Jira issue by link ID."""
        session, base = _client()
        r = session.delete(f"{base}/issue/{issue_id_or_key}/remotelink/{link_id}")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}
