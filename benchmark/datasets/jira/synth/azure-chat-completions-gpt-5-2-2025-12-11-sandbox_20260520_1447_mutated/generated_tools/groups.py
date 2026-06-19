from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def find_groups(query: Optional[str] = None, exclude: Optional[List[str]] = None, excludeId: Optional[List[str]] = None, page_size: int = 50, caseInsensitive: Optional[bool] = None):
    """GET /groups/picker"""
    client = JiraClient()
    params: Dict[str, Any] = {"page_size": page_size}
    if query is not None:
        params["query"] = query
    if exclude is not None:
        params["exclude"] = exclude
    if excludeId is not None:
        params["excludeId"] = excludeId
    if caseInsensitive is not None:
        params["caseInsensitive"] = str(caseInsensitive).lower()
    return client.request("GET", "/groups/picker", params=params)


def get_group_members(groupId: Optional[str] = None, groupname: Optional[str] = None, includeInactiveUsers: bool = False, start_index: int = 0, page_size: int = 50):
    """GET /group/member"""
    client = JiraClient()
    params: Dict[str, Any] = {
        "includeInactiveUsers": str(includeInactiveUsers).lower(),
        "start_index": start_index,
        "page_size": page_size,
    }
    if groupId is not None:
        params["groupId"] = groupId
    if groupname is not None:
        params["groupname"] = groupname
    return client.request("GET", "/group/member", params=params)


def add_user_to_group(user_id: str, groupId: Optional[str] = None, groupname: Optional[str] = None):
    """POST /group/user"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if groupId is not None:
        params["groupId"] = groupId
    if groupname is not None:
        params["groupname"] = groupname
    return client.request("POST", "/group/user", params=params or None, json={"user_id": user_id})


def remove_user_from_group(user_id: str, groupId: Optional[str] = None, groupname: Optional[str] = None):
    """DELETE /group/user"""
    client = JiraClient()
    params: Dict[str, Any] = {"user_id": user_id}
    if groupId is not None:
        params["groupId"] = groupId
    if groupname is not None:
        params["groupname"] = groupname
    return client.request("DELETE", "/group/user", params=params)
