from typing import Any, Dict, Optional

from jira_client import JiraClient


def find_groups(query: str, max_results: int = 50) -> Any:
    """GET /groups/picker"""
    client = JiraClient()
    params: Dict[str, Any] = {"query": query, "maxResults": max_results}
    return client.request("GET", "/groups/picker", params=params)


def get_group_members(groupname: Optional[str] = None, group_id: Optional[str] = None, start_at: int = 0, max_results: int = 50) -> Any:
    """GET /group/member"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if groupname:
        params["groupname"] = groupname
    if group_id:
        params["groupId"] = group_id
    return client.request("GET", "/group/member", params=params)
