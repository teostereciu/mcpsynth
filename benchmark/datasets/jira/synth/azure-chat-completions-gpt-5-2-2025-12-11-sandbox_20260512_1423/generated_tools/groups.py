from typing import Any, Dict, List, Optional

from ._client import get_client


def groups_picker(query: Optional[str] = None, max_results: Optional[int] = None, exclude: Optional[List[str]] = None,
                  exclude_id: Optional[List[str]] = None, case_insensitive: Optional[bool] = None) -> Any:
    """GET /groups/picker"""
    params: Dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if max_results is not None:
        params["maxResults"] = max_results
    if exclude:
        params["exclude"] = exclude
    if exclude_id:
        params["excludeId"] = exclude_id
    if case_insensitive is not None:
        params["caseInsensitive"] = str(bool(case_insensitive)).lower()
    return get_client().request("GET", "/groups/picker", params=params or None)


def group_members(group_id: Optional[str] = None, group_name: Optional[str] = None, include_inactive_users: bool = False,
                  start_at: int = 0, max_results: int = 50) -> Any:
    """GET /group/member"""
    params: Dict[str, Any] = {
        "includeInactiveUsers": str(bool(include_inactive_users)).lower(),
        "startAt": start_at,
        "maxResults": max_results,
    }
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    return get_client().request("GET", "/group/member", params=params)


def create_group(name: str) -> Any:
    """POST /group"""
    return get_client().request("POST", "/group", json_body={"name": name})


def delete_group(group_id: Optional[str] = None, group_name: Optional[str] = None,
                 swap_group_id: Optional[str] = None, swap_group: Optional[str] = None) -> Any:
    """DELETE /group"""
    params: Dict[str, Any] = {}
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    if swap_group_id is not None:
        params["swapGroupId"] = swap_group_id
    if swap_group is not None:
        params["swapGroup"] = swap_group
    return get_client().request("DELETE", "/group", params=params or None)


def add_user_to_group(account_id: str, group_id: Optional[str] = None, group_name: Optional[str] = None) -> Any:
    """POST /group/user"""
    params: Dict[str, Any] = {}
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    return get_client().request("POST", "/group/user", params=params or None, json_body={"accountId": account_id})


def remove_user_from_group(account_id: str, group_id: Optional[str] = None, group_name: Optional[str] = None) -> Any:
    """DELETE /group/user"""
    params: Dict[str, Any] = {"accountId": account_id}
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    return get_client().request("DELETE", "/group/user", params=params)
