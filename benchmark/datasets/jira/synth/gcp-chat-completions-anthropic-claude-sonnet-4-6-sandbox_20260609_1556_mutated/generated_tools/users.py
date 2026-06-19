"""User management and search tools."""
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
    def get_user(account_id: str) -> dict:
        """Get a user by account ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/user", params={"accountId": account_id})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_current_user() -> dict:
        """Get the currently authenticated user."""
        s, base = _client()
        try:
            r = s.get(f"{base}/myself")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_user(
        email_address: str,
        products: List[str],
        display_name: Optional[str] = None,
    ) -> dict:
        """Create a new Jira user."""
        s, base = _client()
        body: dict = {"emailAddress": email_address, "products": products}
        if display_name:
            body["displayName"] = display_name
        try:
            r = s.post(f"{base}/user", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_user(account_id: str) -> dict:
        """Delete a user from Jira."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/user", params={"accountId": account_id})
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def bulk_get_users(account_ids: List[str], start_at: int = 0, max_results: int = 10) -> dict:
        """Get multiple users by their account IDs."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        for aid in account_ids:
            params.setdefault("accountId", []).append(aid)
        # requests handles list params
        try:
            r = s.get(f"{base}/user/bulk", params=[("startAt", start_at), ("maxResults", max_results)] +
                      [("accountId", aid) for aid in account_ids])
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def find_users(
        query: Optional[str] = None,
        account_id: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> dict:
        """Search for users by query string."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if account_id:
            params["accountId"] = account_id
        try:
            r = s.get(f"{base}/user/search", params=params)
            r.raise_for_status()
            return {"users": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def find_users_for_picker(
        query: str,
        max_results: int = 50,
        exclude_account_ids: Optional[List[str]] = None,
    ) -> dict:
        """Find users for a picker/autocomplete UI."""
        s, base = _client()
        params: dict = {"query": query, "maxResults": max_results}
        try:
            if exclude_account_ids:
                r = s.get(f"{base}/user/picker",
                          params=[("query", query), ("maxResults", max_results)] +
                          [("excludeAccountIds", aid) for aid in exclude_account_ids])
            else:
                r = s.get(f"{base}/user/picker", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def find_users_assignable_to_issue(
        query: Optional[str] = None,
        project: Optional[str] = None,
        issue_key: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> dict:
        """Find users that can be assigned to an issue."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if project:
            params["project"] = project
        if issue_key:
            params["issueKey"] = issue_key
        try:
            r = s.get(f"{base}/user/assignable/search", params=params)
            r.raise_for_status()
            return {"users": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def find_users_assignable_to_projects(
        project_keys: str,
        query: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> dict:
        """Find users assignable to issues in one or more projects."""
        s, base = _client()
        params: dict = {"projectKeys": project_keys, "startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        try:
            r = s.get(f"{base}/user/assignable/multiProjectSearch", params=params)
            r.raise_for_status()
            return {"users": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_all_users(start_at: int = 0, max_results: int = 50) -> dict:
        """Get all users in the Jira instance."""
        s, base = _client()
        try:
            r = s.get(f"{base}/users/search", params={"startAt": start_at, "maxResults": max_results})
            r.raise_for_status()
            return {"users": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_user_groups(account_id: str) -> dict:
        """Get the groups a user belongs to."""
        s, base = _client()
        try:
            r = s.get(f"{base}/user/groups", params={"accountId": account_id})
            r.raise_for_status()
            return {"groups": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
