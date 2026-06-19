from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_user(*, accountId: Optional[str] = None, expand: Optional[str] = None) -> Any:
    """GET /rest/api/3/user"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if accountId is not None:
        params["accountId"] = accountId
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/user", params=params or None)


def bulk_get_users(accountIds: List[str], *, startAt: int = 0, maxResults: int = 100) -> Any:
    """GET /rest/api/3/user/bulk"""
    client = JiraClient()
    params: Dict[str, Any] = {"accountId": accountIds, "startAt": startAt, "maxResults": maxResults}
    return client.request("GET", "/user/bulk", params=params)


def get_user_groups(accountId: str) -> Any:
    """GET /rest/api/3/user/groups"""
    client = JiraClient()
    return client.request("GET", "/user/groups", params={"accountId": accountId})


def search_users(query: str, *, maxResults: int = 50, startAt: int = 0) -> Any:
    """GET /rest/api/3/users/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"query": query, "maxResults": maxResults, "startAt": startAt}
    return client.request("GET", "/users/search", params=params)
