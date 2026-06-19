from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def get_user(account_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /user"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if account_id is not None:
        params["accountId"] = account_id
    if username is not None:
        params["username"] = username
    if key is not None:
        params["key"] = key
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/user", params=params or None)


def create_user(user: Dict[str, Any]) -> Union[Dict[str, Any], list, str]:
    """POST /user"""
    client = JiraClient()
    return client.request("POST", "/user", json=user)


def delete_user(account_id: str, username: Optional[str] = None, key: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """DELETE /user"""
    client = JiraClient()
    params: Dict[str, Any] = {"accountId": account_id}
    if username is not None:
        params["username"] = username
    if key is not None:
        params["key"] = key
    return client.request("DELETE", "/user", params=params)


def bulk_get_users(account_ids: List[str], start_at: Optional[int] = None, max_results: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /user/bulk"""
    client = JiraClient()
    params: Dict[str, Any] = {"accountId": account_ids}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", "/user/bulk", params=params)


def get_user_groups(account_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /user/groups"""
    client = JiraClient()
    return client.request("GET", "/user/groups", params={"accountId": account_id})


def users_search(query: str, max_results: Optional[int] = None, start_at: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /users/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"query": query}
    if max_results is not None:
        params["maxResults"] = max_results
    if start_at is not None:
        params["startAt"] = start_at
    return client.request("GET", "/users/search", params=params)
