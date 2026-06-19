"""Project CRUD and related operations."""
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
    def get_all_projects(expand: Optional[str] = None) -> dict:
        """Get all projects visible to the user."""
        s, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/project", params=params)
            r.raise_for_status()
            return {"projects": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def search_projects(
        query: Optional[str] = None,
        type_key: Optional[str] = None,
        category_id: Optional[int] = None,
        start_at: int = 0,
        max_results: int = 50,
        order_by: Optional[str] = None,
        expand: Optional[str] = None,
    ) -> dict:
        """Search for projects with pagination and filtering."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if type_key:
            params["typeKey"] = type_key
        if category_id is not None:
            params["categoryId"] = category_id
        if order_by:
            params["orderBy"] = order_by
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/project/search", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project(project_id_or_key: str, expand: Optional[str] = None) -> dict:
        """Get details of a specific project."""
        s, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/project/{project_id_or_key}", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_project(
        key: str,
        name: str,
        project_type_key: str,
        project_template_key: str,
        description: Optional[str] = None,
        lead_account_id: Optional[str] = None,
        assignee_type: Optional[str] = None,
        avatar_id: Optional[int] = None,
        category_id: Optional[int] = None,
        permission_scheme: Optional[int] = None,
        notification_scheme: Optional[int] = None,
    ) -> dict:
        """Create a new project."""
        s, base = _client()
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
        if avatar_id is not None:
            body["avatarId"] = avatar_id
        if category_id is not None:
            body["categoryId"] = category_id
        if permission_scheme is not None:
            body["permissionScheme"] = permission_scheme
        if notification_scheme is not None:
            body["notificationScheme"] = notification_scheme
        try:
            r = s.post(f"{base}/project", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_project(
        project_id_or_key: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        lead_account_id: Optional[str] = None,
        assignee_type: Optional[str] = None,
        avatar_id: Optional[int] = None,
        category_id: Optional[int] = None,
    ) -> dict:
        """Update an existing project."""
        s, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if lead_account_id:
            body["leadAccountId"] = lead_account_id
        if assignee_type:
            body["assigneeType"] = assignee_type
        if avatar_id is not None:
            body["avatarId"] = avatar_id
        if category_id is not None:
            body["categoryId"] = category_id
        try:
            r = s.put(f"{base}/project/{project_id_or_key}", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_project(project_id_or_key: str) -> dict:
        """Delete a project."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/project/{project_id_or_key}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def archive_project(project_id_or_key: str) -> dict:
        """Archive a project."""
        s, base = _client()
        try:
            r = s.post(f"{base}/project/{project_id_or_key}/archive")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def restore_project(project_id_or_key: str) -> dict:
        """Restore an archived project."""
        s, base = _client()
        try:
            r = s.post(f"{base}/project/{project_id_or_key}/restore")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project_statuses(project_id_or_key: str) -> dict:
        """Get all statuses available for a project."""
        s, base = _client()
        try:
            r = s.get(f"{base}/project/{project_id_or_key}/statuses")
            r.raise_for_status()
            return {"statuses": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_recent_projects(expand: Optional[str] = None) -> dict:
        """Get recently viewed projects."""
        s, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/project/recent", params=params)
            r.raise_for_status()
            return {"projects": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project_notification_scheme(project_key_or_id: str) -> dict:
        """Get the notification scheme for a project."""
        s, base = _client()
        try:
            r = s.get(f"{base}/project/{project_key_or_id}/notificationscheme")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
