from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def get_group(group_id: Optional[str] = None, groupname: Optional[str] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /group (Deprecated in docs)"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/group", params=params or None)


def create_group(name: str) -> Union[Dict[str, Any], list, str]:
    """POST /group"""
    client = JiraClient()
    return client.request("POST", "/group", json={"name": name})


def delete_group(group_id: Optional[str] = None, groupname: Optional[str] = None, swap_group: Optional[str] = None, swap_group_id: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """DELETE /group"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    if swap_group is not None:
        params["swapGroup"] = swap_group
    if swap_group_id is not None:
        params["swapGroupId"] = swap_group_id
    return client.request("DELETE", "/group", params=params or None)


def bulk_get_groups(start_at: Optional[int] = None, max_results: Optional[int] = None, group_ids: Optional[List[str]] = None, group_names: Optional[List[str]] = None, access_type: Optional[str] = None, application_key: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /group/bulk"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if group_ids is not None:
        params["groupId"] = group_ids
    if group_names is not None:
        params["groupName"] = group_names
    if access_type is not None:
        params["accessType"] = access_type
    if application_key is not None:
        params["applicationKey"] = application_key
    return client.request("GET", "/group/bulk", params=params or None)


def get_group_members(group_id: Optional[str] = None, groupname: Optional[str] = None, include_inactive_users: Optional[bool] = None, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /group/member"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    if include_inactive_users is not None:
        params["includeInactiveUsers"] = str(include_inactive_users).lower()
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", "/group/member", params=params or None)


def add_user_to_group(account_id: str, group_id: Optional[str] = None, groupname: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """POST /group/user"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    return client.request("POST", "/group/user", params=params or None, json={"accountId": account_id})


def remove_user_from_group(account_id: str, group_id: Optional[str] = None, groupname: Optional[str] = None, username: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """DELETE /group/user"""
    client = JiraClient()
    params: Dict[str, Any] = {"accountId": account_id}
    if group_id is not None:
        params["groupId"] = group_id
    if groupname is not None:
        params["groupname"] = groupname
    if username is not None:
        params["username"] = username
    return client.request("DELETE", "/group/user", params=params)


def groups_picker(query: Optional[str] = None, exclude: Optional[List[str]] = None, exclude_id: Optional[List[str]] = None, max_results: Optional[int] = None, case_insensitive: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """GET /groups/picker"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if exclude is not None:
        params["exclude"] = exclude
    if exclude_id is not None:
        params["excludeId"] = exclude_id
    if max_results is not None:
        params["maxResults"] = max_results
    if case_insensitive is not None:
        params["caseInsensitive"] = str(case_insensitive).lower()
    return client.request("GET", "/groups/picker", params=params or None)
