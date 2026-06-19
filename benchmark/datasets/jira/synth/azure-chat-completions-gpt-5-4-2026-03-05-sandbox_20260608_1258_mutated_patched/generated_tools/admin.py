from typing import Any, Optional

from .common import JiraClient, compact_dict


def get_user(account_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/user", params=compact_dict({"accountId": account_id, "accountId": account_id, "username": username, "key": key, "expand": expand}))


def create_user(body: dict) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/user", json_body=body)


def delete_user(account_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", "/rest/api/3/user", params=compact_dict({"accountId": account_id, "accountId": account_id, "username": username, "key": key}))


def bulk_get_users(account_ids: list[str], start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/user/bulk", params=compact_dict({"accountId": account_ids, "startAt": start_at, "maxResults": max_results}))


def get_user_default_columns(account_id: Optional[str] = None, username: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/user/columns", params=compact_dict({"accountId": account_id, "accountId": account_id, "username": username}))


def set_user_default_columns(columns: list[str], account_id: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("PUT", "/rest/api/3/user/columns", params=compact_dict({"accountId": account_id, "accountId": account_id}), data=[("columns", c) for c in columns])


def reset_user_default_columns(account_id: Optional[str] = None, username: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", "/rest/api/3/user/columns", params=compact_dict({"accountId": account_id, "accountId": account_id, "username": username}))


def get_group(group_id: Optional[str] = None, groupname: Optional[str] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/group", params=compact_dict({"groupId": group_id, "groupname": groupname, "expand": expand}))


def create_group(name: str) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/group", json_body={"name": name})


def remove_group(group_id: Optional[str] = None, groupname: Optional[str] = None, swap_group: Optional[str] = None, swap_group_id: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", "/rest/api/3/group", params=compact_dict({"groupId": group_id, "groupname": groupname, "swapGroup": swap_group, "swapGroupId": swap_group_id}))


def bulk_get_groups(start_at: Optional[int] = None, max_results: Optional[int] = None, group_id: Optional[list[str]] = None, group_name: Optional[list[str]] = None, access_type: Optional[str] = None, application_key: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/group/bulk", params=compact_dict({"startAt": start_at, "maxResults": max_results, "groupId": group_id, "groupName": group_name, "accessType": access_type, "applicationKey": application_key}))


def get_group_members(group_id: Optional[str] = None, groupname: Optional[str] = None, include_inactive_users: Optional[bool] = None, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/group/member", params=compact_dict({"groupId": group_id, "groupname": groupname, "includeInactiveUsers": include_inactive_users, "startAt": start_at, "maxResults": max_results}))


def add_user_to_group(account_id: str, group_id: Optional[str] = None, groupname: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/group/user", params=compact_dict({"groupId": group_id, "groupname": groupname}), json_body={"accountId": account_id, "accountId": account_id})


def remove_user_from_group(account_id: str, group_id: Optional[str] = None, groupname: Optional[str] = None, username: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", "/rest/api/3/group/user", params=compact_dict({"groupId": group_id, "groupname": groupname, "username": username, "accountId": account_id, "accountId": account_id}))


def find_groups(query: Optional[str] = None, exclude: Optional[list[str]] = None, exclude_id: Optional[list[str]] = None, max_results: Optional[int] = None, case_insensitive: Optional[bool] = None, account_id: Optional[str] = None, username: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/groups/picker", params=compact_dict({"query": query, "exclude": exclude, "excludeId": exclude_id, "maxResults": max_results, "maxResults": max_results, "caseInsensitive": case_insensitive, "accountId": account_id, "accountId": account_id, "userName": username}))
