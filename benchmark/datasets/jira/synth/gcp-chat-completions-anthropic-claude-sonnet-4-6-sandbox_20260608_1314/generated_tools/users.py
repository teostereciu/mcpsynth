"""User management and search tools."""
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
    def get_current_user() -> dict:
        """Get details of the currently authenticated Jira user."""
        session, base = _client()
        r = session.get(f"{base}/myself")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_user(account_id: str) -> dict:
        """Get a Jira user by their account ID."""
        session, base = _client()
        r = session.get(f"{base}/user", params={"accountId": account_id})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def find_users(query: Optional[str] = None, account_id: Optional[str] = None,
                    start_at: int = 0, max_results: int = 50) -> dict:
        """Search for Jira users by display name, email, or account ID."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if account_id:
            params["accountId"] = account_id
        r = session.get(f"{base}/user/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def find_users_for_picker(query: str, max_results: int = 50,
                               exclude_account_ids: Optional[List[str]] = None) -> dict:
        """Find users for a picker/autocomplete field by query string."""
        session, base = _client()
        params: dict = {"query": query, "maxResults": max_results}
        if exclude_account_ids:
            params["excludeAccountIds"] = exclude_account_ids
        r = session.get(f"{base}/user/picker", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def find_users_assignable_to_issue(project_key: Optional[str] = None,
                                        issue_key: Optional[str] = None,
                                        query: Optional[str] = None,
                                        start_at: int = 0, max_results: int = 50) -> dict:
        """Find users who can be assigned to a Jira issue. Provide either project_key or issue_key."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if project_key:
            params["project"] = project_key
        if issue_key:
            params["issueKey"] = issue_key
        if query:
            params["query"] = query
        r = session.get(f"{base}/user/assignable/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def find_users_assignable_to_projects(project_keys: str, query: Optional[str] = None,
                                           start_at: int = 0, max_results: int = 50) -> dict:
        """Find users assignable to issues in one or more projects (comma-separated project keys)."""
        session, base = _client()
        params: dict = {"projectKeys": project_keys, "startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        r = session.get(f"{base}/user/assignable/multiProjectSearch", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_all_users(start_at: int = 0, max_results: int = 50) -> dict:
        """Get all Jira users (paginated)."""
        session, base = _client()
        params = {"startAt": start_at, "maxResults": max_results}
        r = session.get(f"{base}/users/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_user_groups(account_id: str) -> dict:
        """Get the groups that a Jira user belongs to."""
        session, base = _client()
        r = session.get(f"{base}/user/groups", params={"accountId": account_id})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def bulk_get_users(account_ids: List[str], start_at: int = 0, max_results: int = 100) -> dict:
        """Get multiple Jira users by their account IDs in a single request."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        # requests handles list params
        r = session.get(f"{base}/user/bulk", params={**params, "accountId": account_ids})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def find_users_with_permissions(permissions: str, project_key: Optional[str] = None,
                                     issue_key: Optional[str] = None,
                                     query: Optional[str] = None,
                                     start_at: int = 0, max_results: int = 50) -> dict:
        """Find users who have specific permissions for a project or issue.
        permissions: comma-separated permission names e.g. 'BROWSE_PROJECTS,CREATE_ISSUES'"""
        session, base = _client()
        params: dict = {"permissions": permissions, "startAt": start_at, "maxResults": max_results}
        if project_key:
            params["projectKey"] = project_key
        if issue_key:
            params["issueKey"] = issue_key
        if query:
            params["query"] = query
        r = session.get(f"{base}/user/permission/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
