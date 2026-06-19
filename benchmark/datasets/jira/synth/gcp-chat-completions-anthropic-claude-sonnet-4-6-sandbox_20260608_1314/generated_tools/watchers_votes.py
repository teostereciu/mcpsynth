"""Issue watchers and votes tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, List
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_issue_watchers(issue_id_or_key: str) -> dict:
        """Get the list of watchers for a Jira issue."""
        session, base = _client()
        r = session.get(f"{base}/issue/{issue_id_or_key}/watchers")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def add_issue_watcher(issue_id_or_key: str, account_id: str) -> dict:
        """Add a user as a watcher of a Jira issue by their account ID."""
        session, base = _client()
        r = session.post(f"{base}/issue/{issue_id_or_key}/watchers", json=account_id)
        if r.status_code == 204:
            return {"success": True}
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def remove_issue_watcher(issue_id_or_key: str, account_id: str) -> dict:
        """Remove a user as a watcher from a Jira issue."""
        session, base = _client()
        r = session.delete(f"{base}/issue/{issue_id_or_key}/watchers", params={"accountId": account_id})
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_votes(issue_id_or_key: str) -> dict:
        """Get vote details for a Jira issue (vote count and list of voters)."""
        session, base = _client()
        r = session.get(f"{base}/issue/{issue_id_or_key}/votes")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def add_issue_vote(issue_id_or_key: str) -> dict:
        """Add the current user's vote to a Jira issue."""
        session, base = _client()
        r = session.post(f"{base}/issue/{issue_id_or_key}/votes")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def remove_issue_vote(issue_id_or_key: str) -> dict:
        """Remove the current user's vote from a Jira issue."""
        session, base = _client()
        r = session.delete(f"{base}/issue/{issue_id_or_key}/votes")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_is_watching_issue_bulk(issue_ids: List[str]) -> dict:
        """Check whether the current user is watching a list of issues (by ID)."""
        session, base = _client()
        r = session.post(f"{base}/issue/watching", json={"issueIds": issue_ids})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
