"""Issue CRUD, transitions, assignments, changelogs, and search tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, List, Any
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    email = os.environ["JIRA_EMAIL"]
    token = os.environ["JIRA_API_TOKEN"]
    s = requests.Session()
    s.auth = (email, token)
    s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return s, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def create_issue(
        project_id: str,
        summary: str,
        issue_type_id: str,
        description: Optional[str] = None,
        assignee_id: Optional[str] = None,
        priority_id: Optional[str] = None,
        labels: Optional[List[str]] = None,
        parent_key: Optional[str] = None,
        additional_fields: Optional[dict] = None,
    ) -> dict:
        """Create a new Jira issue (or subtask if parent_key is provided)."""
        s, base = _client()
        fields: dict = {
            "project": {"id": project_id},
            "summary": summary,
            "issuetype": {"id": issue_type_id},
        }
        if description:
            fields["description"] = {
                "type": "doc", "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": description}]}]
            }
        if assignee_id:
            fields["assignee"] = {"id": assignee_id}
        if priority_id:
            fields["priority"] = {"id": priority_id}
        if labels:
            fields["labels"] = labels
        if parent_key:
            fields["parent"] = {"key": parent_key}
        if additional_fields:
            fields.update(additional_fields)
        try:
            r = s.post(f"{base}/issue", json={"fields": fields})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue(
        issue_id_or_key: str,
        fields: Optional[str] = None,
        expand: Optional[str] = None,
    ) -> dict:
        """Get details of a Jira issue by ID or key."""
        s, base = _client()
        params = {}
        if fields:
            params["fields"] = fields
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_issue(
        issue_id_or_key: str,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        assignee_id: Optional[str] = None,
        priority_id: Optional[str] = None,
        labels: Optional[List[str]] = None,
        additional_fields: Optional[dict] = None,
    ) -> dict:
        """Update fields on an existing Jira issue."""
        s, base = _client()
        fields: dict = {}
        if summary:
            fields["summary"] = summary
        if description:
            fields["description"] = {
                "type": "doc", "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": description}]}]
            }
        if assignee_id is not None:
            fields["assignee"] = {"id": assignee_id} if assignee_id else None
        if priority_id:
            fields["priority"] = {"id": priority_id}
        if labels is not None:
            fields["labels"] = labels
        if additional_fields:
            fields.update(additional_fields)
        try:
            r = s.put(f"{base}/issue/{issue_id_or_key}", json={"fields": fields})
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_issue(issue_id_or_key: str, delete_subtasks: bool = False) -> dict:
        """Delete a Jira issue."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/issue/{issue_id_or_key}", params={"deleteSubtasks": str(delete_subtasks).lower()})
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> dict:
        """Assign an issue to a user (pass None account_id to unassign)."""
        s, base = _client()
        body = {"accountId": account_id}
        try:
            r = s.put(f"{base}/issue/{issue_id_or_key}/assignee", json=body)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_transitions(issue_id_or_key: str) -> dict:
        """Get available workflow transitions for an issue."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/transitions")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def transition_issue(
        issue_id_or_key: str,
        transition_id: str,
        comment: Optional[str] = None,
        fields: Optional[dict] = None,
    ) -> dict:
        """Transition an issue to a new workflow status."""
        s, base = _client()
        body: dict = {"transition": {"id": transition_id}}
        if comment:
            body["update"] = {
                "comment": [{"add": {"body": {
                    "type": "doc", "version": 1,
                    "content": [{"type": "paragraph", "content": [{"type": "text", "text": comment}]}]
                }}}]
            }
        if fields:
            body["fields"] = fields
        try:
            r = s.post(f"{base}/issue/{issue_id_or_key}/transitions", json=body)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_changelog(
        issue_id_or_key: str,
        start_at: int = 0,
        max_results: int = 50,
    ) -> dict:
        """Get the changelog for an issue."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/changelog",
                      params={"startAt": start_at, "maxResults": max_results})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_create_issue_metadata(
        project_ids: Optional[str] = None,
        project_keys: Optional[str] = None,
        issue_type_ids: Optional[str] = None,
    ) -> dict:
        """Get metadata for creating issues (available fields, issue types, etc.)."""
        s, base = _client()
        params = {}
        if project_ids:
            params["projectIds"] = project_ids
        if project_keys:
            params["projectKeys"] = project_keys
        if issue_type_ids:
            params["issuetypeIds"] = issue_type_ids
        try:
            r = s.get(f"{base}/issue/createmeta", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def bulk_create_issues(issues: List[dict]) -> dict:
        """Create multiple issues in a single request. Each item in issues should have fields dict."""
        s, base = _client()
        try:
            r = s.post(f"{base}/issue/bulk", json={"issueUpdates": issues})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_edit_metadata(issue_id_or_key: str) -> dict:
        """Get metadata for editing an issue (available fields)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/issue/{issue_id_or_key}/editmeta")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def notify_issue(
        issue_id_or_key: str,
        subject: Optional[str] = None,
        text_body: Optional[str] = None,
        html_body: Optional[str] = None,
        to_reporter: bool = False,
        to_assignee: bool = False,
        to_watchers: bool = False,
    ) -> dict:
        """Send a notification about an issue."""
        s, base = _client()
        body: dict = {}
        if subject:
            body["subject"] = subject
        if text_body:
            body["textBody"] = text_body
        if html_body:
            body["htmlBody"] = html_body
        to: dict = {}
        if to_reporter:
            to["reporter"] = True
        if to_assignee:
            to["assignee"] = True
        if to_watchers:
            to["watchers"] = True
        if to:
            body["to"] = to
        try:
            r = s.post(f"{base}/issue/{issue_id_or_key}/notify", json=body)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def search_issues_jql(
        jql: str,
        start_at: int = 0,
        max_results: int = 50,
        fields: Optional[List[str]] = None,
        expand: Optional[str] = None,
    ) -> dict:
        """Search for issues using JQL (Jira Query Language)."""
        s, base = _client()
        body: dict = {
            "jql": jql,
            "startAt": start_at,
            "maxResults": max_results,
        }
        if fields:
            body["fields"] = fields
        if expand:
            body["expand"] = [expand] if isinstance(expand, str) else expand
        try:
            r = s.post(f"{base}/search", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_issue_picker_suggestions(
        query: str,
        current_jql: Optional[str] = None,
        current_issue_key: Optional[str] = None,
        show_sub_tasks: bool = True,
    ) -> dict:
        """Get issue picker suggestions for auto-complete."""
        s, base = _client()
        params: dict = {"query": query, "showSubTasks": show_sub_tasks}
        if current_jql:
            params["currentJQL"] = current_jql
        if current_issue_key:
            params["currentIssueKey"] = current_issue_key
        try:
            r = s.get(f"{base}/issue/picker", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def bulk_fetch_changelogs(
        issue_ids_or_keys: List[str],
        field_ids: Optional[List[str]] = None,
        page_size: int = 100,
        next_page_token: Optional[str] = None,
    ) -> dict:
        """Bulk fetch changelogs for multiple issues."""
        s, base = _client()
        body: dict = {"issueIdsOrKeys": issue_ids_or_keys, "page_size": page_size}
        if field_ids:
            body["fieldIds"] = field_ids
        if next_page_token:
            body["nextPageToken"] = next_page_token
        try:
            r = s.post(f"{base}/changelog/bulkfetch", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
