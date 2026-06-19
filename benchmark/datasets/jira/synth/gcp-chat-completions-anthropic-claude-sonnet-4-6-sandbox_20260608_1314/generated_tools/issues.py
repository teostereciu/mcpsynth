"""Issue CRUD, transitions, assignments, changelogs, and search tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, List, Any
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    email = os.environ["JIRA_EMAIL"]
    token = os.environ["JIRA_API_TOKEN"]
    session = requests.Session()
    session.auth = (email, token)
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_issue(issue_id_or_key: str, fields: Optional[str] = None, expand: Optional[str] = None) -> dict:
        """Get a Jira issue by ID or key. Optionally specify comma-separated fields or expand options."""
        session, base = _client()
        params = {}
        if fields:
            params["fields"] = fields
        if expand:
            params["expand"] = expand
        r = session.get(f"{base}/issue/{issue_id_or_key}", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_issue(fields: dict, update: Optional[dict] = None, transition: Optional[dict] = None) -> dict:
        """Create a new Jira issue. 'fields' must include at minimum 'project' (id or key), 'issuetype', and 'summary'.
        Example fields: {'project': {'key': 'PROJ'}, 'issuetype': {'name': 'Bug'}, 'summary': 'My bug'}"""
        session, base = _client()
        body: dict = {"fields": fields}
        if update:
            body["update"] = update
        if transition:
            body["transition"] = transition
        r = session.post(f"{base}/issue", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_issue(issue_id_or_key: str, fields: Optional[dict] = None, update: Optional[dict] = None) -> dict:
        """Update a Jira issue. Provide fields and/or update dicts with the changes to apply."""
        session, base = _client()
        body: dict = {}
        if fields:
            body["fields"] = fields
        if update:
            body["update"] = update
        r = session.put(f"{base}/issue/{issue_id_or_key}", json=body)
        if r.status_code == 204:
            return {"success": True}
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_issue(issue_id_or_key: str, delete_subtasks: bool = False) -> dict:
        """Delete a Jira issue by ID or key. Set delete_subtasks=True to also delete subtasks."""
        session, base = _client()
        params = {"deleteSubtasks": str(delete_subtasks).lower()}
        r = session.delete(f"{base}/issue/{issue_id_or_key}", params=params)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> dict:
        """Assign a Jira issue to a user by account ID. Pass account_id=None to unassign."""
        session, base = _client()
        body = {"accountId": account_id}
        r = session.put(f"{base}/issue/{issue_id_or_key}/assignee", json=body)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_transitions(issue_id_or_key: str) -> dict:
        """Get available workflow transitions for a Jira issue."""
        session, base = _client()
        r = session.get(f"{base}/issue/{issue_id_or_key}/transitions")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def transition_issue(issue_id_or_key: str, transition_id: str, fields: Optional[dict] = None, comment: Optional[str] = None) -> dict:
        """Transition a Jira issue to a new workflow state using a transition ID.
        Use get_issue_transitions to find valid transition IDs."""
        session, base = _client()
        body: dict = {"transition": {"id": transition_id}}
        if fields:
            body["fields"] = fields
        if comment:
            body["update"] = {"comment": [{"add": {"body": {"type": "doc", "version": 1, "content": [{"type": "paragraph", "content": [{"type": "text", "text": comment}]}]}}}]}
        r = session.post(f"{base}/issue/{issue_id_or_key}/transitions", json=body)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_changelog(issue_id_or_key: str, start_at: int = 0, max_results: int = 100) -> dict:
        """Get the changelog for a Jira issue (history of field changes)."""
        session, base = _client()
        params = {"startAt": start_at, "maxResults": max_results}
        r = session.get(f"{base}/issue/{issue_id_or_key}/changelog", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_create_issue_metadata(project_ids: Optional[str] = None, project_keys: Optional[str] = None,
                                   issue_type_ids: Optional[str] = None, issue_type_names: Optional[str] = None) -> dict:
        """Get metadata for creating issues, including available fields and their schemas."""
        session, base = _client()
        params = {}
        if project_ids:
            params["projectIds"] = project_ids
        if project_keys:
            params["projectKeys"] = project_keys
        if issue_type_ids:
            params["issuetypeIds"] = issue_type_ids
        if issue_type_names:
            params["issuetypeNames"] = issue_type_names
        r = session.get(f"{base}/issue/createmeta", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def bulk_create_issues(issue_updates: List[dict]) -> dict:
        """Create multiple Jira issues in a single request. Each item in issue_updates should have a 'fields' key."""
        session, base = _client()
        body = {"issueUpdates": issue_updates}
        r = session.post(f"{base}/issue/bulk", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def search_issues_jql(jql: str, start_at: int = 0, max_results: int = 50,
                           fields: Optional[List[str]] = None, expand: Optional[str] = None) -> dict:
        """Search for Jira issues using JQL (Jira Query Language). Returns matching issues with their fields."""
        session, base = _client()
        body: dict = {"jql": jql, "startAt": start_at, "maxResults": max_results}
        if fields:
            body["fields"] = fields
        if expand:
            body["expand"] = [expand] if isinstance(expand, str) else expand
        r = session.post(f"{base}/search/jql", json=body)
        if r.ok:
            return r.json()
        # fallback to /search
        r2 = session.post(f"{base}/search", json=body)
        if r2.ok:
            return r2.json()
        return {"error": r2.text, "status_code": r2.status_code}

    @mcp.tool()
    def get_issue_picker_suggestions(query: str, current_jql: Optional[str] = None) -> dict:
        """Get issue picker suggestions matching a query string (for autocomplete)."""
        session, base = _client()
        params: dict = {"query": query}
        if current_jql:
            params["currentJQL"] = current_jql
        r = session.get(f"{base}/issue/picker", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_issue_edit_metadata(issue_id_or_key: str) -> dict:
        """Get metadata for editing a Jira issue, including editable fields."""
        session, base = _client()
        r = session.get(f"{base}/issue/{issue_id_or_key}/editmeta")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def notify_issue(issue_id_or_key: str, subject: str, text_body: str,
                     html_body: Optional[str] = None, to_reporter: bool = False,
                     to_assignee: bool = False, to_watchers: bool = False) -> dict:
        """Send a notification email about a Jira issue."""
        session, base = _client()
        body: dict = {
            "subject": subject,
            "textBody": text_body,
            "to": {
                "reporter": to_reporter,
                "assignee": to_assignee,
                "watchers": to_watchers,
            }
        }
        if html_body:
            body["htmlBody"] = html_body
        r = session.post(f"{base}/issue/{issue_id_or_key}/notify", json=body)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}
