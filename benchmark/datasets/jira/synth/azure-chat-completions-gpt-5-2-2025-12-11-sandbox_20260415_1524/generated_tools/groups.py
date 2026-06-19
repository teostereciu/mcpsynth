from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def group_get(group_id: Optional[str] = None, groupname: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /group - Get group (deprecated by Jira)."""
    client = JiraClient()
    params = clean_params({"groupId": group_id, "groupname": groupname, "expand": expand})
    return client.request("GET", "/group", params=params)  # type: ignore[return-value]


def group_create(name: str) -> Dict[str, Any]:
    """POST /group - Create group."""
    client = JiraClient()
    return client.request("POST", "/group", json_body={"name": name})  # type: ignore[return-value]


def group_delete(group_id: Optional[str] = None, groupname: Optional[str] = None, swap_group_id: Optional[str] = None, swap_group: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /group - Delete group."""
    client = JiraClient()
    params = clean_params({"groupId": group_id, "groupname": groupname, "swapGroupId": swap_group_id, "swapGroup": swap_group})
    return client.request("DELETE", "/group", params=params)  # type: ignore[return-value]


def groups_bulk(start_at: Optional[int] = None, max_results: Optional[int] = None, group_ids: Optional[List[str]] = None, group_names: Optional[List[str]] = None, access_type: Optional[str] = None, application_key: Optional[str] = None) -> Dict[str, Any]:
    """GET /group/bulk - Bulk get groups."""
    client = JiraClient()
    params = clean_params({"startAt": start_at, "maxResults": max_results, "groupId": group_ids, "groupName": group_names, "accessType": access_type, "applicationKey": application_key})
    return client.request("GET", "/group/bulk", params=params)  # type: ignore[return-value]


def group_members(group_id: Optional[str] = None, groupname: Optional[str] = None, include_inactive_users: Optional[bool] = None, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Dict[str, Any]:
    """GET /group/member - Get users from group."""
    client = JiraClient()
    params = clean_params({"groupId": group_id, "groupname": groupname, "includeInactiveUsers": include_inactive_users, "startAt": start_at, "maxResults": max_results})
    return client.request("GET", "/group/member", params=params)  # type: ignore[return-value]


def group_add_user(account_id: str, group_id: Optional[str] = None, groupname: Optional[str] = None) -> Dict[str, Any]:
    """POST /group/user - Add user to group."""
    client = JiraClient()
    params = clean_params({"groupId": group_id, "groupname": groupname})
    return client.request("POST", "/group/user", params=params, json_body={"accountId": account_id})  # type: ignore[return-value]


def group_remove_user(account_id: str, group_id: Optional[str] = None, groupname: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /group/user - Remove user from group."""
    client = JiraClient()
    params = clean_params({"groupId": group_id, "groupname": groupname, "accountId": account_id})
    return client.request("DELETE", "/group/user", params=params)  # type: ignore[return-value]


def groups_picker(query: Optional[str] = None, exclude: Optional[List[str]] = None, exclude_id: Optional[List[str]] = None, max_results: Optional[int] = None, case_insensitive: Optional[bool] = None) -> Dict[str, Any]:
    """GET /groups/picker - Find groups."""
    client = JiraClient()
    params = clean_params({"query": query, "exclude": exclude, "excludeId": exclude_id, "maxResults": max_results, "caseInsensitive": case_insensitive})
    return client.request("GET", "/groups/picker", params=params)  # type: ignore[return-value]
