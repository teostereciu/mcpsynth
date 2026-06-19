from typing import Any, Dict, Optional

from jira_client import JiraClient


def find_groups(client: JiraClient, query: str, max_results: int = 50) -> Any:
    params = {"query": query, "maxResults": max_results}
    return client.request("GET", "/groups/picker", params=params)


def get_group_members(client: JiraClient, group_id: Optional[str] = None, group_name: Optional[str] = None, include_inactive_users: bool = False, start_at: int = 0, max_results: int = 50) -> Any:
    params: Dict[str, Any] = {"includeInactiveUsers": str(include_inactive_users).lower(), "startAt": start_at, "maxResults": max_results}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    return client.request("GET", "/group/member", params=params)
