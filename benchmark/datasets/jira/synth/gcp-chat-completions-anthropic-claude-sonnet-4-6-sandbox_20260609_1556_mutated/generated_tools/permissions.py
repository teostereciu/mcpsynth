"""Permission tools: check and get permissions."""
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
    def get_my_permissions(
        project_key: Optional[str] = None,
        project_id: Optional[str] = None,
        issue_key: Optional[str] = None,
        issue_id: Optional[str] = None,
        permissions: Optional[str] = None,
    ) -> dict:
        """Get the current user's permissions. permissions: comma-separated list e.g. 'BROWSE_PROJECTS,EDIT_ISSUES'."""
        s, base = _client()
        params: dict = {}
        if project_key:
            params["projectKey"] = project_key
        if project_id:
            params["projectId"] = project_id
        if issue_key:
            params["issueKey"] = issue_key
        if issue_id:
            params["issueId"] = issue_id
        if permissions:
            params["permissions"] = permissions
        try:
            r = s.get(f"{base}/mypermissions", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_all_permissions() -> dict:
        """Get all permissions available in Jira."""
        s, base = _client()
        try:
            r = s.get(f"{base}/permissions")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def check_permissions(
        global_permissions: Optional[List[str]] = None,
        project_permissions: Optional[List[dict]] = None,
        account_id: Optional[str] = None,
    ) -> dict:
        """Check bulk permissions for a user. project_permissions: [{permissions:[...], projects:[...], issues:[...]}]."""
        s, base = _client()
        body: dict = {}
        if account_id:
            body["accountId"] = account_id
        if global_permissions:
            body["globalPermissions"] = global_permissions
        if project_permissions:
            body["projectPermissions"] = project_permissions
        try:
            r = s.post(f"{base}/permissions/check", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_permitted_projects(permissions: List[str]) -> dict:
        """Get all projects where the user has the specified permissions."""
        s, base = _client()
        try:
            r = s.post(f"{base}/permissions/project", json={"permissions": permissions})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
