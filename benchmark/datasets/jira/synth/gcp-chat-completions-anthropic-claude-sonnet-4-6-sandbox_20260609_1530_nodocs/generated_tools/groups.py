"""
MCP tools for Jira Groups.
"""

from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-groups")


@mcp.tool()
def get_group(group_name: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get details of a group, including its members.

    Args:
        group_name: The group name.
        expand: Expand options (e.g. 'users').
    """
    params: Dict[str, Any] = {"groupname": group_name}
    if expand:
        params["expand"] = expand
    return jira_get("/group", params=params)


@mcp.tool()
def create_group(name: str) -> Dict[str, Any]:
    """
    Create a new group.

    Args:
        name: The group name.
    """
    return jira_post("/group", json={"name": name})


@mcp.tool()
def delete_group(
    group_name: str,
    swap_group: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Delete a group.

    Args:
        group_name: The group name to delete.
        swap_group: Group to transfer restrictions to when deleting.
    """
    params: Dict[str, Any] = {"groupname": group_name}
    if swap_group:
        params["swapGroup"] = swap_group
    return jira_delete("/group", params=params)


@mcp.tool()
def get_group_members(
    group_name: str,
    include_inactive_users: bool = False,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Get members of a group.

    Args:
        group_name: The group name.
        include_inactive_users: Include inactive users in results.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
    """
    params: Dict[str, Any] = {
        "groupname": group_name,
        "includeInactiveUsers": include_inactive_users,
        "startAt": start_at,
        "maxResults": max_results,
    }
    return jira_get("/group/member", params=params)


@mcp.tool()
def add_user_to_group(group_name: str, account_id: str) -> Dict[str, Any]:
    """
    Add a user to a group.

    Args:
        group_name: The group name.
        account_id: The account ID of the user to add.
    """
    return jira_post(
        "/group/user",
        json={"accountId": account_id},
        params={"groupname": group_name},
    )


@mcp.tool()
def remove_user_from_group(group_name: str, account_id: str) -> Dict[str, Any]:
    """
    Remove a user from a group.

    Args:
        group_name: The group name.
        account_id: The account ID of the user to remove.
    """
    return jira_delete(
        "/group/user",
        params={"groupname": group_name, "accountId": account_id},
    )


@mcp.tool()
def find_groups(
    query: Optional[str] = None,
    exclude: Optional[str] = None,
    max_results: int = 20,
    user_account_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Find groups by query string.

    Args:
        query: Search string to match against group names.
        exclude: Comma-separated group names to exclude.
        max_results: Maximum number of results to return.
        user_account_id: Filter to groups the user belongs to.
    """
    params: Dict[str, Any] = {"maxResults": max_results}
    if query:
        params["query"] = query
    if exclude:
        params["exclude"] = exclude
    if user_account_id:
        params["userAccountId"] = user_account_id
    return jira_get("/groups/picker", params=params)


@mcp.tool()
def bulk_get_groups(
    group_id: Optional[str] = None,
    group_name: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Get multiple groups by ID or name.

    Args:
        group_id: Comma-separated group IDs to retrieve.
        group_name: Comma-separated group names to retrieve.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupName"] = group_name
    return jira_get("/group/bulk", params=params)
