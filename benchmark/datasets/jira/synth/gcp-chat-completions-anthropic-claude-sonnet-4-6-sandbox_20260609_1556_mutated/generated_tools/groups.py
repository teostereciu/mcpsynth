"""Group management tools."""
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
    def create_group(name: str) -> dict:
        """Create a new group."""
        s, base = _client()
        try:
            r = s.post(f"{base}/group", json={"name": name})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_group(group_id: Optional[str] = None, group_name: Optional[str] = None) -> dict:
        """Delete a group by ID or name."""
        s, base = _client()
        params = {}
        if group_id:
            params["groupId"] = group_id
        if group_name:
            params["groupname"] = group_name
        try:
            r = s.delete(f"{base}/group", params=params)
            if r.status_code == 200:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_group_members(
        group_id: Optional[str] = None,
        group_name: Optional[str] = None,
        include_inactive_users: bool = False,
        start_at: int = 0,
        max_results: int = 50,
    ) -> dict:
        """Get members of a group."""
        s, base = _client()
        params: dict = {"includeInactiveUsers": include_inactive_users,
                        "startAt": start_at, "maxResults": max_results}
        if group_id:
            params["groupId"] = group_id
        if group_name:
            params["groupname"] = group_name
        try:
            r = s.get(f"{base}/group/member", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def add_user_to_group(account_id: str, group_id: Optional[str] = None, group_name: Optional[str] = None) -> dict:
        """Add a user to a group."""
        s, base = _client()
        params = {}
        if group_id:
            params["groupId"] = group_id
        if group_name:
            params["groupname"] = group_name
        try:
            r = s.post(f"{base}/group/user", json={"accountId": account_id}, params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def remove_user_from_group(
        account_id: str,
        group_id: Optional[str] = None,
        group_name: Optional[str] = None,
    ) -> dict:
        """Remove a user from a group."""
        s, base = _client()
        params: dict = {"accountId": account_id}
        if group_id:
            params["groupId"] = group_id
        if group_name:
            params["groupname"] = group_name
        try:
            r = s.delete(f"{base}/group/user", params=params)
            if r.status_code == 200:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def find_groups(
        query: Optional[str] = None,
        max_results: int = 20,
        exclude_ids: Optional[List[str]] = None,
    ) -> dict:
        """Find groups by name query."""
        s, base = _client()
        params: dict = {"maxResults": max_results}
        if query:
            params["query"] = query
        try:
            if exclude_ids:
                r = s.get(f"{base}/groups/picker",
                          params=[("maxResults", max_results)] +
                          ([("query", query)] if query else []) +
                          [("excludeId", eid) for eid in exclude_ids])
            else:
                r = s.get(f"{base}/groups/picker", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def bulk_get_groups(
        group_ids: Optional[List[str]] = None,
        group_names: Optional[List[str]] = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> dict:
        """Get multiple groups by IDs or names."""
        s, base = _client()
        params_list = [("startAt", start_at), ("maxResults", max_results)]
        if group_ids:
            params_list += [("groupId", gid) for gid in group_ids]
        if group_names:
            params_list += [("groupName", gn) for gn in group_names]
        try:
            r = s.get(f"{base}/group/bulk", params=params_list)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
