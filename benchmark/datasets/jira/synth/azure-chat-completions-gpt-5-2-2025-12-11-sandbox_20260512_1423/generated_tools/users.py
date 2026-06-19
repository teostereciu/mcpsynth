from typing import Any, Dict, List, Optional

from ._client import get_client


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
    return get_client().request("GET", "/user", params=params or None)


def user_search(query: str, start_at: int = 0, max_results: int = 50, include_active: Optional[bool] = None,
                include_inactive: Optional[bool] = None) -> Any:
    """GET /users/search"""
    params: Dict[str, Any] = {"query": query, "startAt": start_at, "maxResults": max_results}
    if include_active is not None:
        params["includeActive"] = str(bool(include_active)).lower()
    if include_inactive is not None:
        params["includeInactive"] = str(bool(include_inactive)).lower()
    return get_client().request("GET", "/users/search", params=params)


def bulk_get_users(account_ids: List[str], start_at: int = 0, max_results: int = 100) -> Any:
    """GET /user/bulk"""
    params: Dict[str, Any] = {"accountId": account_ids, "startAt": start_at, "maxResults": max_results}
    return get_client().request("GET", "/user/bulk", params=params)


def get_user_groups(account_id: str) -> Any:
    """GET /user/groups"""
    return get_client().request("GET", "/user/groups", params={"accountId": account_id})
