"""Project CRUD and related operations."""
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
    def get_project(project_id_or_key: str, expand: Optional[str] = None) -> dict:
        """Get details of a Jira project by ID or key."""
        session, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        r = session.get(f"{base}/project/{project_id_or_key}", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def search_projects(query: Optional[str] = None, type_key: Optional[str] = None,
                         category_id: Optional[int] = None, start_at: int = 0,
                         max_results: int = 50, order_by: Optional[str] = None,
                         action: Optional[str] = None) -> dict:
        """Search for Jira projects with optional filters. Returns paginated results.
        type_key: 'software', 'service_desk', 'business'
        action: 'view', 'browse', 'edit'"""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if type_key:
            params["typeKey"] = type_key
        if category_id:
            params["categoryId"] = category_id
        if order_by:
            params["orderBy"] = order_by
        if action:
            params["action"] = action
        r = session.get(f"{base}/project/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_all_projects(expand: Optional[str] = None, recent: Optional[int] = None) -> dict:
        """Get all Jira projects visible to the current user."""
        session, base = _client()
        params: dict = {}
        if expand:
            params["expand"] = expand
        if recent is not None:
            params["recent"] = recent
        r = session.get(f"{base}/project", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_recent_projects() -> dict:
        """Get the list of recently viewed Jira projects (up to 20)."""
        session, base = _client()
        r = session.get(f"{base}/project/recent")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_project(key: str, name: str, project_type_key: str,
                        project_template_key: str, description: Optional[str] = None,
                        lead_account_id: Optional[str] = None,
                        assignee_type: Optional[str] = None,
                        avatar_id: Optional[int] = None,
                        category_id: Optional[int] = None) -> dict:
        """Create a new Jira project.
        project_type_key: 'software', 'service_desk', 'business'
        project_template_key: e.g. 'com.pyxis.greenhopper.jira:gh-simplified-agility-scrum'
        assignee_type: 'PROJECT_LEAD' or 'UNASSIGNED'"""
        session, base = _client()
        body: dict = {
            "key": key,
            "name": name,
            "projectTypeKey": project_type_key,
            "projectTemplateKey": project_template_key,
        }
        if description:
            body["description"] = description
        if lead_account_id:
            body["leadAccountId"] = lead_account_id
        if assignee_type:
            body["assigneeType"] = assignee_type
        if avatar_id:
            body["avatarId"] = avatar_id
        if category_id:
            body["categoryId"] = category_id
        r = session.post(f"{base}/project", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_project(project_id_or_key: str, name: Optional[str] = None,
                        description: Optional[str] = None,
                        lead_account_id: Optional[str] = None,
                        assignee_type: Optional[str] = None,
                        avatar_id: Optional[int] = None,
                        category_id: Optional[int] = None) -> dict:
        """Update a Jira project's details."""
        session, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if lead_account_id:
            body["leadAccountId"] = lead_account_id
        if assignee_type:
            body["assigneeType"] = assignee_type
        if avatar_id:
            body["avatarId"] = avatar_id
        if category_id is not None:
            body["categoryId"] = category_id
        r = session.put(f"{base}/project/{project_id_or_key}", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_project(project_id_or_key: str) -> dict:
        """Delete a Jira project by ID or key."""
        session, base = _client()
        r = session.delete(f"{base}/project/{project_id_or_key}")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def archive_project(project_id_or_key: str) -> dict:
        """Archive a Jira project."""
        session, base = _client()
        r = session.post(f"{base}/project/{project_id_or_key}/archive")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def restore_project(project_id_or_key: str) -> dict:
        """Restore an archived Jira project."""
        session, base = _client()
        r = session.post(f"{base}/project/{project_id_or_key}/restore")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_project_statuses(project_id_or_key: str) -> dict:
        """Get all issue statuses available in a Jira project."""
        session, base = _client()
        r = session.get(f"{base}/project/{project_id_or_key}/statuses")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_project_notification_scheme(project_key_or_id: str) -> dict:
        """Get the notification scheme associated with a Jira project."""
        session, base = _client()
        r = session.get(f"{base}/project/{project_key_or_id}/notificationscheme")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
