from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def create_group(name: str) -> Any:
    """POST /group"""
    return JiraClient().request("POST", "/group", json_body={"name": name})


def delete_group(group_id: Optional[str] = None, groupname: Optional[str] = None,
                 swap_group_id: Optional[str] = None, swap_group: Optional[str] = None) -> Any:
    """DELETE /group"""
    params: Dict[str, Any] = {}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    if swap_group_id is not None:
        params["swapGroupId"] = swap_group_id
    if swap_group is not None:
        params["swapGroup"] = swap_group
    return JiraClient().request("DELETE", "/group", params=params or None)


def bulk_get_groups(start_at: int = 0, max_results: int = 50, group_ids: Optional[List[str]] = None,
                    group_names: Optional[List[str]] = None, access_type: Optional[str] = None,
                    application_key: Optional[str] = None) -> Any:
    """GET /group/bulk"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if group_ids is not None:
        params["groupId"] = group_ids
    if group_names is not None:
        params["groupName"] = group_names
    if access_type is not None:
        params["accessType"] = access_type
    if application_key is not None:
        params["applicationKey"] = application_key
    return JiraClient().request("GET", "/group/bulk", params=params)


def get_users_from_group(group_id: Optional[str] = None, groupname: Optional[str] = None,
                         include_inactive_users: Optional[bool] = None,
                         start_at: int = 0, max_results: int = 50) -> Any:
    """GET /group/member"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    if include_inactive_users is not None:
        params["includeInactiveUsers"] = str(include_inactive_users).lower()
    return JiraClient().request("GET", "/group/member", params=params)


def add_user_to_group(group_id: Optional[str], account_id: str, groupname: Optional[str] = None) -> Any:
    """POST /group/user"""
    params: Dict[str, Any] = {}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    return JiraClient().request("POST", "/group/user", params=params or None, json_body={"accountId": account_id})


def remove_user_from_group(group_id: Optional[str], account_id: str, groupname: Optional[str] = None) -> Any:
    """DELETE /group/user"""
    params: Dict[str, Any] = {"accountId": account_id}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    return JiraClient().request("DELETE", "/group/user", params=params)


def find_groups(query: Optional[str] = None, exclude: Optional[List[str]] = None,
                exclude_id: Optional[List[str]] = None, max_results: int = 50,
                case_insensitive: Optional[bool] = None) -> Any:
    """GET /groups/picker"""
    params: Dict[str, Any] = {"maxResults": max_results}
    if query is not None:
        params["query"] = query
    if exclude is not None:
        params["exclude"] = exclude
    if exclude_id is not None:
        params["excludeId"] = exclude_id
    if case_insensitive is not None:
        params["caseInsensitive"] = str(case_insensitive).lower()
    return JiraClient().request("GET", "/groups/picker", params=params)
