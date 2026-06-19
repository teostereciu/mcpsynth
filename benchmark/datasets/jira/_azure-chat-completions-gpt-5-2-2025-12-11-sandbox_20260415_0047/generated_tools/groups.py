from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_group(group_id: Optional[str] = None, group_name: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    """Get group details.

    GET /rest/api/3/group
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    if expand:
        params["expand"] = expand
    return client.request("GET", "/group", params=params)


@mcp.tool()
def jira_get_group_members(
    group_id: Optional[str] = None,
    group_name: Optional[str] = None,
    include_inactive_users: bool = False,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """Get users from a group.

    GET /rest/api/3/group/member
    """

    client = JiraClient()
    params: Dict[str, Any] = {
        "includeInactiveUsers": str(include_inactive_users).lower(),
        "startAt": start_at,
        "maxResults": max_results,
    }
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    return client.request("GET", "/group/member", params=params)


@mcp.tool()
def jira_groups_picker(query: Optional[str] = None, max_results: int = 50) -> Dict[str, Any]:
    """Find groups for picker.

    GET /rest/api/3/groups/picker
    """

    client = JiraClient()
    params: Dict[str, Any] = {"maxResults": max_results}
    if query is not None:
        params["query"] = query
    return client.request("GET", "/groups/picker", params=params)


@mcp.tool()
def jira_create_group(name: str) -> Dict[str, Any]:
    """Create a group.

    POST /rest/api/3/group
    """

    client = JiraClient()
    return client.request("POST", "/group", json={"name": name})


@mcp.tool()
def jira_delete_group(group_id: Optional[str] = None, group_name: Optional[str] = None) -> Dict[str, Any]:
    """Delete a group.

    DEL /rest/api/3/group
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    return client.request("DELETE", "/group", params=params)


@mcp.tool()
def jira_add_user_to_group(account_id: str, group_id: Optional[str] = None, group_name: Optional[str] = None) -> Dict[str, Any]:
    """Add a user to a group.

    POST /rest/api/3/group/user
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    return client.request("POST", "/group/user", params=params, json={"accountId": account_id})


@mcp.tool()
def jira_remove_user_from_group(account_id: str, group_id: Optional[str] = None, group_name: Optional[str] = None) -> Dict[str, Any]:
    """Remove a user from a group.

    DEL /rest/api/3/group/user
    """

    client = JiraClient()
    params: Dict[str, Any] = {"accountId": account_id}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    return client.request("DELETE", "/group/user", params=params)
