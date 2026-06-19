"""Issue worklog tools: get, add, update, delete."""
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
    def get_issue_worklogs(
        issue_id_or_key: str,
        start_at: int = 0,
        max_results: int = 50,
        started_after: Optional[int] = None,
        started_before: Optional[int] = None,
    ) -> dict:
        """Get worklogs for an issue."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if started_after:
            params["startedAfter"] = started_after
        if started_before:
            params["startedBefore"] = started_before
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/worklog", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_worklog(issue_id_or_key: str, worklog_id: str) -> dict:
        """Get a specific worklog entry."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/worklog/{worklog_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def add_worklog(
        issue_id_or_key: str,
        time_spent: Optional[str] = None,
        time_spent_seconds: Optional[int] = None,
        started: Optional[str] = None,
        comment_text: Optional[str] = None,
        adjust_estimate: Optional[str] = None,
        new_estimate: Optional[str] = None,
    ) -> dict:
        """Add a worklog to an issue. time_spent e.g. '3h 20m', started e.g. '2021-01-17T12:34:00.000+0000'."""
        s, base = _client()
        body: dict = {}
        if time_spent:
            body["timeSpent"] = time_spent
        if time_spent_seconds is not None:
            body["timeSpentSeconds"] = time_spent_seconds
        if started:
            body["started"] = started
        if comment_text:
            body["comment"] = {
                "type": "doc", "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": comment_text}]}]
            }
        params: dict = {}
        if adjust_estimate:
            params["adjustEstimate"] = adjust_estimate
        if new_estimate:
            params["newEstimate"] = new_estimate
        try:
            r = s.post(f"{base}/issue/{issue_id_or_key}/worklog", json=body, params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_worklog(
        issue_id_or_key: str,
        worklog_id: str,
        time_spent: Optional[str] = None,
        time_spent_seconds: Optional[int] = None,
        started: Optional[str] = None,
        comment_text: Optional[str] = None,
        adjust_estimate: Optional[str] = None,
        new_estimate: Optional[str] = None,
    ) -> dict:
        """Update an existing worklog entry."""
        s, base = _client()
        body: dict = {}
        if time_spent:
            body["timeSpent"] = time_spent
        if time_spent_seconds is not None:
            body["timeSpentSeconds"] = time_spent_seconds
        if started:
            body["started"] = started
        if comment_text:
            body["comment"] = {
                "type": "doc", "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": comment_text}]}]
            }
        params: dict = {}
        if adjust_estimate:
            params["adjustEstimate"] = adjust_estimate
        if new_estimate:
            params["newEstimate"] = new_estimate
        try:
            r = s.put(f"{base}/issue/{issue_id_or_key}/worklog/{worklog_id}", json=body, params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_worklog(
        issue_id_or_key: str,
        worklog_id: str,
        adjust_estimate: Optional[str] = None,
        new_estimate: Optional[str] = None,
    ) -> dict:
        """Delete a worklog entry from an issue."""
        s, base = _client()
        params: dict = {}
        if adjust_estimate:
            params["adjustEstimate"] = adjust_estimate
        if new_estimate:
            params["newEstimate"] = new_estimate
        try:
            r = s.delete(f"{base}/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_worklogs_by_ids(worklog_ids: List[int]) -> dict:
        """Get multiple worklogs by their IDs."""
        s, base = _client()
        try:
            r = s.post(f"{base}/worklog/list", json={"ids": worklog_ids})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_deleted_worklogs(since: Optional[int] = None) -> dict:
        """Get IDs of worklogs deleted since a given timestamp (epoch ms)."""
        s, base = _client()
        params = {}
        if since is not None:
            params["since"] = since
        try:
            r = s.get(f"{base}/worklog/deleted", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_updated_worklogs(since: Optional[int] = None) -> dict:
        """Get IDs of worklogs updated since a given timestamp (epoch ms)."""
        s, base = _client()
        params = {}
        if since is not None:
            params["since"] = since
        try:
            r = s.get(f"{base}/worklog/updated", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
