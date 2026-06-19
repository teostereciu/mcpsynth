"""
MCP tools for Jira Users.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-users")


@mcp.tool()
def get_current_user(expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get the details of the currently authenticated user.

    Args:
        expand: Comma-separated list of entities to expand (e.g. 'groups,applicationRoles').
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get("/myself", params=params)


@mcp.tool()
def get_user(
    account_id: Optional[str] = None,
    username: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get details of a specific user.

    Args:
        account_id: The user's account ID (preferred).
        username: The user's username (deprecated, use account_id).
        expand: Comma-separated list of entities to expand (e.g. 'groups,applicationRoles').
    """
    params: Dict[str, Any] = {}
    if account_id:
        params["accountId"] = account_id
    if username:
        params["username"] = username
    if expand:
        params["expand"] = expand
    return jira_get("/user", params=params)


@mcp.tool()
def find_users(
    query: Optional[str] = None,
    account_id: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
    include_active: bool = True,
    include_inactive: bool = False,
) -> Dict[str, Any]:
    """
    Find users by query string (name, email, display name).

    Args:
        query: Search string to match against user name, display name, or email.
        account_id: Filter by account ID.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        include_active: Include active users.
        include_inactive: Include inactive users.
    """
    params: Dict[str, Any] = {
        "startAt": start_at,
        "maxResults": max_results,
        "includeActive": include_active,
        "includeInactive": include_inactive,
    }
    if query:
        params["query"] = query
    if account_id:
        params["accountId"] = account_id
    return jira_get("/user/search", params=params)


@mcp.tool()
def find_users_for_picker(
    query: str,
    max_results: int = 50,
    show_avatar: bool = False,
    exclude: Optional[str] = None,
    exclude_account_ids: Optional[str] = None,
    project_id: Optional[str] = None,
    issue_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Find users suitable for a user picker (e.g. for assigning issues).

    Args:
        query: Search string.
        max_results: Maximum number of results.
        show_avatar: Include avatar URLs in results.
        exclude: Comma-separated usernames to exclude.
        exclude_account_ids: Comma-separated account IDs to exclude.
        project_id: Project ID to scope the search.
        issue_id: Issue ID to scope the search.
    """
    params: Dict[str, Any] = {
        "query": query,
        "maxResults": max_results,
        "showAvatar": show_avatar,
    }
    if exclude:
        params["exclude"] = exclude
    if exclude_account_ids:
        params["excludeAccountIds"] = exclude_account_ids
    if project_id:
        params["projectId"] = project_id
    if issue_id:
        params["issueId"] = issue_id
    return jira_get("/user/picker", params=params)


@mcp.tool()
def find_assignable_users(
    project: Optional[str] = None,
    issue_key: Optional[str] = None,
    query: Optional[str] = None,
    username: Optional[str] = None,
    account_id: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Find users who can be assigned to issues in a project or specific issue.

    Args:
        project: Project key to find assignable users for.
        issue_key: Issue key to find assignable users for.
        query: Search string to filter users.
        username: Filter by username (deprecated).
        account_id: Filter by account ID.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if project:
        params["project"] = project
    if issue_key:
        params["issueKey"] = issue_key
    if query:
        params["query"] = query
    if username:
        params["username"] = username
    if account_id:
        params["accountId"] = account_id
    return jira_get("/user/assignable/search", params=params)


@mcp.tool()
def find_users_with_permissions(
    permissions: str,
    query: Optional[str] = None,
    account_id: Optional[str] = None,
    issue_key: Optional[str] = None,
    project_key: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Find users who have specific permissions in a project or issue.

    Args:
        permissions: Comma-separated list of permissions (e.g. 'BROWSE,CREATE_ISSUES').
        query: Search string to filter users.
        account_id: Filter by account ID.
        issue_key: Issue key to scope the permission check.
        project_key: Project key to scope the permission check.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
    """
    params: Dict[str, Any] = {
        "permissions": permissions,
        "startAt": start_at,
        "maxResults": max_results,
    }
    if query:
        params["query"] = query
    if account_id:
        params["accountId"] = account_id
    if issue_key:
        params["issueKey"] = issue_key
    if project_key:
        params["projectKey"] = project_key
    return jira_get("/user/permission/search", params=params)


@mcp.tool()
def get_user_groups(account_id: str) -> Dict[str, Any]:
    """
    Get the groups a user belongs to.

    Args:
        account_id: The user's account ID.
    """
    return jira_get("/user/groups", params={"accountId": account_id})


@mcp.tool()
def get_account_ids_for_users(
    username: Optional[str] = None,
    key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get account IDs for users by username or user key (for migration purposes).

    Args:
        username: The username to look up.
        key: The user key to look up.
    """
    params: Dict[str, Any] = {}
    if username:
        params["username"] = username
    if key:
        params["key"] = key
    return jira_get("/user/bulk/migration", params=params)


@mcp.tool()
def get_all_users(
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Get all users (requires admin permissions).

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
    """
    return jira_get("/users/search", params={"startAt": start_at, "maxResults": max_results})
