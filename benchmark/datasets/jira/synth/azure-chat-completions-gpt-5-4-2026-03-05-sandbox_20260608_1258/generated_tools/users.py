from typing import Any, Dict, Optional

from generated_tools.issues import _request


def get_user(account_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None, expand: Optional[str] = None) -> Any:
    params = {}
    if account_id is not None:
        params["accountId"] = account_id
    if username is not None:
        params["username"] = username
    if key is not None:
        params["key"] = key
    if expand is not None:
        params["expand"] = expand
    return _request("GET", "/user", params=params or None)


def bulk_get_users(account_ids: list[str], start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {"accountId": account_ids}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return _request("GET", "/user/bulk", params=params)


def get_user_groups(account_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None) -> Any:
    params = {}
    if account_id is not None:
        params["accountId"] = account_id
    if username is not None:
        params["username"] = username
    if key is not None:
        params["key"] = key
    return _request("GET", "/user/groups", params=params or None)


def create_group(name: str) -> Any:
    return _request("POST", "/group", json_body={"name": name})


def list_groups(start_at: Optional[int] = None, max_results: Optional[int] = None, group_ids: Optional[list[str]] = None, group_names: Optional[list[str]] = None, access_type: Optional[str] = None, application_key: Optional[str] = None) -> Any:
    params = {}
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
    return _request("GET", "/group/bulk", params=params or None)


def get_group_members(group_id: Optional[str] = None, group_name: Optional[str] = None, include_inactive_users: Optional[bool] = None, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    params = {}
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    if include_inactive_users is not None:
        params["includeInactiveUsers"] = str(include_inactive_users).lower()
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return _request("GET", "/group/member", params=params or None)


def add_user_to_group(account_id: str, group_id: Optional[str] = None, group_name: Optional[str] = None) -> Any:
    params = {}
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    return _request("POST", "/group/user", params=params or None, json_body={"accountId": account_id})


def remove_user_from_group(account_id: str, group_id: Optional[str] = None, group_name: Optional[str] = None, username: Optional[str] = None) -> Any:
    params = {"accountId": account_id}
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    if username is not None:
        params["username"] = username
    return _request("DELETE", "/group/user", params=params)


def find_groups(query: Optional[str] = None, account_id: Optional[str] = None, exclude: Optional[list[str]] = None, exclude_id: Optional[list[str]] = None, max_results: Optional[int] = None, case_insensitive: Optional[bool] = None, user_name: Optional[str] = None) -> Any:
    params = {}
    if query is not None:
        params["query"] = query
    if account_id is not None:
        params["accountId"] = account_id
    if exclude is not None:
        params["exclude"] = exclude
    if exclude_id is not None:
        params["excludeId"] = exclude_id
    if max_results is not None:
        params["maxResults"] = max_results
    if case_insensitive is not None:
        params["caseInsensitive"] = str(case_insensitive).lower()
    if user_name is not None:
        params["userName"] = user_name
    return _request("GET", "/groups/picker", params=params or None)
