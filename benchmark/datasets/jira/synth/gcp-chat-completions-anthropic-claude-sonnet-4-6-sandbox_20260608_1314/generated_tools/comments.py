"""Issue comment tools: get, add, update, delete comments."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, List
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def _text_to_adf(text: str) -> dict:
    """Convert plain text to Atlassian Document Format."""
    return {
        "type": "doc",
        "version": 1,
        "content": [{"type": "paragraph", "content": [{"type": "text", "text": text}]}]
    }

def register(mcp: FastMCP):

    @mcp.tool()
    def get_issue_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50,
                            order_by: Optional[str] = None) -> dict:
        """Get all comments for a Jira issue."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if order_by:
            params["orderBy"] = order_by
        r = session.get(f"{base}/issue/{issue_id_or_key}/comment", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_comment(issue_id_or_key: str, comment_id: str) -> dict:
        """Get a specific comment from a Jira issue by comment ID."""
        session, base = _client()
        r = session.get(f"{base}/issue/{issue_id_or_key}/comment/{comment_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def add_issue_comment(issue_id_or_key: str, body_text: str,
                           visibility_type: Optional[str] = None,
                           visibility_value: Optional[str] = None) -> dict:
        """Add a comment to a Jira issue. body_text is plain text that will be converted to ADF.
        Optionally restrict visibility by role or group (visibility_type='role'|'group', visibility_value='name')."""
        session, base = _client()
        payload: dict = {"body": _text_to_adf(body_text)}
        if visibility_type and visibility_value:
            payload["visibility"] = {"type": visibility_type, "value": visibility_value}
        r = session.post(f"{base}/issue/{issue_id_or_key}/comment", json=payload)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_issue_comment(issue_id_or_key: str, comment_id: str, body_text: str,
                              visibility_type: Optional[str] = None,
                              visibility_value: Optional[str] = None) -> dict:
        """Update an existing comment on a Jira issue."""
        session, base = _client()
        payload: dict = {"body": _text_to_adf(body_text)}
        if visibility_type and visibility_value:
            payload["visibility"] = {"type": visibility_type, "value": visibility_value}
        r = session.put(f"{base}/issue/{issue_id_or_key}/comment/{comment_id}", json=payload)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_issue_comment(issue_id_or_key: str, comment_id: str) -> dict:
        """Delete a comment from a Jira issue."""
        session, base = _client()
        r = session.delete(f"{base}/issue/{issue_id_or_key}/comment/{comment_id}")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_comments_by_ids(comment_ids: List[int]) -> dict:
        """Get multiple comments by their IDs in a single request."""
        session, base = _client()
        r = session.post(f"{base}/comment/list", json={"ids": comment_ids})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
