"""Issue watchers and votes tools."""
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
    def get_issue_watchers(issue_id_or_key: str) -> dict:
        """Get the list of watchers for an issue."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/watchers")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def add_issue_watcher(issue_id_or_key: str, account_id: str) -> dict:
        """Add a user as a watcher of an issue."""
        s, base = _client()
        try:
            r = s.post(f"{base}/issue/{issue_id_or_key}/watchers", json=account_id)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def remove_issue_watcher(issue_id_or_key: str, account_id: str) -> dict:
        """Remove a user as a watcher of an issue."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issue/{issue_id_or_key}/watchers",
                         params={"accountId": account_id})
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_watching_bulk(issue_ids: List[str]) -> dict:
        """Check watching status for multiple issues at once."""
        s, base = _client()
        try:
            r = s.post(f"{base}/issue/watching", json={"issueIds": issue_ids})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_votes(issue_id_or_key: str) -> dict:
        """Get vote details for an issue."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/votes")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def add_issue_vote(issue_id_or_key: str) -> dict:
        """Add the current user's vote to an issue."""
        s, base = _client()
        try:
            r = s.post(f"{base}/issue/{issue_id_or_key}/votes")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def remove_issue_vote(issue_id_or_key: str) -> dict:
        """Remove the current user's vote from an issue."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issue/{issue_id_or_key}/votes")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
