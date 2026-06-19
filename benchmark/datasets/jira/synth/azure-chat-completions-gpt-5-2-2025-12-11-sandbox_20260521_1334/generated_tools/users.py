from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_user(account_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None,
             expand: Optional[str] = None) -> Any:
    """GET /user"""
    params: Dict[str, Any] = {}
    if account_id is not None:
        params["accountId"] = account_id
    if username is not None:
        params["username"] = username
    if key is not None:
        params["key"] = key
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", "/user", params=params or None)


def bulk_get_users(account_ids: List[str], start_at: int = 0, max_results: int = 100) -> Any:
    """GET /user/bulk"""
    params: Dict[str, Any] = {"accountId": account_ids, "startAt": start_at, "maxResults": max_results}
    return JiraClient().request("GET", "/user/bulk", params=params)


def get_account_ids_for_users(usernames: Optional[List[str]] = None, keys: Optional[List[str]] = None,
                              start_at: int = 0, max_results: int = 100) -> Any:
    """GET /user/bulk/migration"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if usernames is not None:
        params["username"] = usernames
    if keys is not None:
        params["key"] = keys
    return JiraClient().request("GET", "/user/bulk/migration", params=params)


def get_user_groups(account_id: str) -> Any:
    """GET /user/groups"""
    return JiraClient().request("GET", "/user/groups", params={"accountId": account_id})


def search_users(query: Optional[str] = None, start_at: int = 0, max_results: int = 50) -> Any:
    """GET /users/search"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if query is not None:
        params["query"] = query
    return JiraClient().request("GET", "/users/search", params=params)
