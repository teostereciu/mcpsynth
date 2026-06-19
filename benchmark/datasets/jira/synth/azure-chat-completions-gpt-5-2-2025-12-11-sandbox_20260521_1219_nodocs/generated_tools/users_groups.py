from typing import Any, Dict, Optional

from .jira_client import JiraClient


def get_user(account_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /user"""
    client = JiraClient()
    params: Dict[str, Any] = {"accountId": account_id}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/user", params=params)


def find_users(query: str, max_results: int = 50, start_at: int = 0) -> Any:
    """GET /user/search"""
    client = JiraClient()
    params = {"query": query, "maxResults": max_results, "startAt": start_at}
    return client.request("GET", "/user/search", params=params)


def get_group_members(groupname: str, start_at: int = 0, max_results: int = 50) -> Dict[str, Any]:
    """GET /group/member"""
    client = JiraClient()
    params = {"groupname": groupname, "startAt": start_at, "maxResults": max_results}
    return client.request("GET", "/group/member", params=params)
