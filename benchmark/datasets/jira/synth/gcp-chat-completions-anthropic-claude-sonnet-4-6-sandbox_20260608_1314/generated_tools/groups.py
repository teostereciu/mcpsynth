"""Group management tools: create, delete, find groups, add/remove members."""
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
    def find_groups(query: Optional[str] = None, max_results: int = 20,
                     exclude: Optional[List[str]] = None) -> dict:
        """Find Jira groups by name query string."""
        session, base = _client()
        params: dict = {"maxResults": max_results}
        if query:
            params["query"] = query
        if exclude:
            params["exclude"] = exclude
        r = session.get(f"{base}/groups/picker", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_group(name: str) -> dict:
        """Create a new Jira group."""
        session, base = _client()
        r = session.post(f"{base}/group", json={"name": name})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_group(group_id: str, swap_group_id: Optional[str] = None) -> dict:
        """Delete a Jira group by group ID. Optionally specify a group to swap issues to."""
        session, base = _client()
        params: dict = {"groupId": group_id}
        if swap_group_id:
            params["swapGroupId"] = swap_group_id
        r = session.delete(f"{base}/group", params=params)
        if r.ok:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_group_members(group_id: str, include_inactive_users: bool = False,
                           start_at: int = 0, max_results: int = 50) -> dict:
        """Get the members of a Jira group (paginated)."""
        session, base = _client()
        params: dict = {
            "groupId": group_id,
            "includeInactiveUsers": include_inactive_users,
            "startAt": start_at,
            "maxResults": max_results
        }
        r = session.get(f"{base}/group/member", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def add_user_to_group(group_id: str, account_id: str) -> dict:
        """Add a user to a Jira group."""
        session, base = _client()
        r = session.post(f"{base}/group/user", params={"groupId": group_id},
                         json={"accountId": account_id})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def remove_user_from_group(group_id: str, account_id: str) -> dict:
        """Remove a user from a Jira group."""
        session, base = _client()
        r = session.delete(f"{base}/group/user",
                           params={"groupId": group_id, "accountId": account_id})
        if r.ok:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def bulk_get_groups(group_ids: Optional[List[str]] = None,
                         group_names: Optional[List[str]] = None,
                         start_at: int = 0, max_results: int = 50) -> dict:
        """Get multiple Jira groups by IDs or names (paginated)."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if group_ids:
            params["groupId"] = group_ids
        if group_names:
            params["groupName"] = group_names
        r = session.get(f"{base}/group/bulk", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
