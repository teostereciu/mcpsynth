"""Issue worklog tools: get, add, update, delete worklogs."""
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
    def get_issue_worklogs(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> dict:
        """Get all worklogs for a Jira issue."""
        session, base = _client()
        params = {"startAt": start_at, "maxResults": max_results}
        r = session.get(f"{base}/issue/{issue_id_or_key}/worklog", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_worklog(issue_id_or_key: str, worklog_id: str) -> dict:
        """Get a specific worklog entry from a Jira issue."""
        session, base = _client()
        r = session.get(f"{base}/issue/{issue_id_or_key}/worklog/{worklog_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def add_issue_worklog(issue_id_or_key: str, time_spent: str, started: str,
                           comment_text: Optional[str] = None,
                           adjust_estimate: Optional[str] = None,
                           new_estimate: Optional[str] = None) -> dict:
        """Add a worklog to a Jira issue.
        time_spent: e.g. '3h 30m', '1d'
        started: ISO 8601 datetime string e.g. '2024-01-15T09:00:00.000+0000'
        adjust_estimate: 'new', 'leave', 'manual', 'auto'
        new_estimate: new remaining estimate (e.g. '2h') when adjust_estimate='new'"""
        session, base = _client()
        payload: dict = {"timeSpent": time_spent, "started": started}
        if comment_text:
            payload["comment"] = {
                "type": "doc", "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": comment_text}]}]
            }
        params: dict = {}
        if adjust_estimate:
            params["adjustEstimate"] = adjust_estimate
        if new_estimate:
            params["newEstimate"] = new_estimate
        r = session.post(f"{base}/issue/{issue_id_or_key}/worklog", json=payload, params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_issue_worklog(issue_id_or_key: str, worklog_id: str,
                              time_spent: Optional[str] = None,
                              started: Optional[str] = None,
                              comment_text: Optional[str] = None,
                              adjust_estimate: Optional[str] = None,
                              new_estimate: Optional[str] = None) -> dict:
        """Update an existing worklog on a Jira issue."""
        session, base = _client()
        payload: dict = {}
        if time_spent:
            payload["timeSpent"] = time_spent
        if started:
            payload["started"] = started
        if comment_text:
            payload["comment"] = {
                "type": "doc", "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": comment_text}]}]
            }
        params: dict = {}
        if adjust_estimate:
            params["adjustEstimate"] = adjust_estimate
        if new_estimate:
            params["newEstimate"] = new_estimate
        r = session.put(f"{base}/issue/{issue_id_or_key}/worklog/{worklog_id}", json=payload, params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_issue_worklog(issue_id_or_key: str, worklog_id: str,
                              adjust_estimate: Optional[str] = None,
                              new_estimate: Optional[str] = None) -> dict:
        """Delete a worklog from a Jira issue."""
        session, base = _client()
        params: dict = {}
        if adjust_estimate:
            params["adjustEstimate"] = adjust_estimate
        if new_estimate:
            params["newEstimate"] = new_estimate
        r = session.delete(f"{base}/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}
