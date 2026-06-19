"""Issue comment tools: get, add, update, delete."""
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
    def get_issue_comments(
        issue_id_or_key: str,
        start_at: int = 0,
        max_results: int = 50,
        order_by: Optional[str] = None,
    ) -> dict:
        """Get all comments for an issue."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if order_by:
            params["orderBy"] = order_by
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/comment", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_comment(issue_id_or_key: str, comment_id: str) -> dict:
        """Get a specific comment on an issue."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/comment/{comment_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def add_issue_comment(
        issue_id_or_key: str,
        body_text: str,
        visibility_type: Optional[str] = None,
        visibility_value: Optional[str] = None,
    ) -> dict:
        """Add a comment to an issue. visibility_type can be 'role' or 'group'."""
        s, base = _client()
        body: dict = {
            "body": {
                "type": "doc", "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": body_text}]}]
            }
        }
        if visibility_type and visibility_value:
            body["visibility"] = {"type": visibility_type, "value": visibility_value}
        try:
            r = s.post(f"{base}/issue/{issue_id_or_key}/comment", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_issue_comment(
        issue_id_or_key: str,
        comment_id: str,
        body_text: str,
        visibility_type: Optional[str] = None,
        visibility_value: Optional[str] = None,
    ) -> dict:
        """Update an existing comment on an issue."""
        s, base = _client()
        body: dict = {
            "body": {
                "type": "doc", "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": body_text}]}]
            }
        }
        if visibility_type and visibility_value:
            body["visibility"] = {"type": visibility_type, "value": visibility_value}
        try:
            r = s.put(f"{base}/issue/{issue_id_or_key}/comment/{comment_id}", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_issue_comment(issue_id_or_key: str, comment_id: str) -> dict:
        """Delete a comment from an issue."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issue/{issue_id_or_key}/comment/{comment_id}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_comments_by_ids(comment_ids: List[int], expand: Optional[str] = None) -> dict:
        """Get multiple comments by their IDs."""
        s, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        try:
            r = s.post(f"{base}/comment/list", json={"ids": comment_ids}, params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
