from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_user(user_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None, expand: Optional[str] = None):
    """GET /user"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if user_id is not None:
        params["accountId"] = user_id
    if username is not None:
        params["username"] = username
    if key is not None:
        params["key"] = key
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/user", params=params or None)


def bulk_get_users(user_ids: List[str], start_index: int = 0, page_size: int = 100):
    """GET /user/bulk"""
    client = JiraClient()
    params: Dict[str, Any] = {"accountId": user_ids, "startAt": start_index, "maxResults": page_size}
    return client.request("GET", "/user/bulk", params=params)


def search_users(query: str, start_index: int = 0, page_size: int = 50):
    """GET /users/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"query": query, "startAt": start_index, "maxResults": page_size}
    return client.request("GET", "/users/search", params=params)


def get_user_groups(user_id: str):
    """GET /user/groups"""
    client = JiraClient()
    return client.request("GET", "/user/groups", params={"accountId": user_id})
