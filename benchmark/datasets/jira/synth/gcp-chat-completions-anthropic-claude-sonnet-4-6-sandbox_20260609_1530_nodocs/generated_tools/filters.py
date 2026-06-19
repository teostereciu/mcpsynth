"""
MCP tools for Jira Filters (saved JQL searches).
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-filters")


@mcp.tool()
def get_filter(filter_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a specific saved filter by ID.

    Args:
        filter_id: The filter ID.
        expand: Comma-separated list of entities to expand (e.g. 'sharedUsers,subscriptions').
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/filter/{filter_id}", params=params)


@mcp.tool()
def create_filter(
    name: str,
    jql: str,
    description: Optional[str] = None,
    favourite: bool = False,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new saved filter.

    Args:
        name: Filter name.
        jql: JQL query string.
        description: Filter description.
        favourite: Whether to mark this filter as a favourite.
        expand: Comma-separated list of entities to expand in the response.
    """
    body: Dict[str, Any] = {"name": name, "jql": jql, "favourite": favourite}
    if description:
        body["description"] = description
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_post("/filter", json=body, params=params)


@mcp.tool()
def update_filter(
    filter_id: str,
    name: Optional[str] = None,
    jql: Optional[str] = None,
    description: Optional[str] = None,
    favourite: Optional[bool] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update an existing saved filter.

    Args:
        filter_id: The filter ID.
        name: New filter name.
        jql: New JQL query string.
        description: New filter description.
        favourite: Whether to mark as favourite.
        expand: Comma-separated list of entities to expand in the response.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if jql is not None:
        body["jql"] = jql
    if description is not None:
        body["description"] = description
    if favourite is not None:
        body["favourite"] = favourite
    if not body:
        return {"error": "No fields provided to update."}
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_put(f"/filter/{filter_id}", json=body, params=params)


@mcp.tool()
def delete_filter(filter_id: str) -> Dict[str, Any]:
    """
    Delete a saved filter.

    Args:
        filter_id: The filter ID.
    """
    return jira_delete(f"/filter/{filter_id}")


@mcp.tool()
def get_my_filters(
    expand: Optional[str] = None,
    include_favourites: bool = False,
) -> Dict[str, Any]:
    """
    Get filters owned by the current user.

    Args:
        expand: Comma-separated list of entities to expand.
        include_favourites: Include favourite filters.
    """
    params: Dict[str, Any] = {"includeFavourites": include_favourites}
    if expand:
        params["expand"] = expand
    return jira_get("/filter/my", params=params)


@mcp.tool()
def get_favourite_filters(expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get the current user's favourite filters.

    Args:
        expand: Comma-separated list of entities to expand.
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get("/filter/favourite", params=params)


@mcp.tool()
def search_filters(
    filter_name: Optional[str] = None,
    account_id: Optional[str] = None,
    group_name: Optional[str] = None,
    project_id: Optional[int] = None,
    order_by: str = "name",
    start_at: int = 0,
    max_results: int = 50,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search for filters with various criteria.

    Args:
        filter_name: Filter name to search for (partial match).
        account_id: Filter by owner account ID.
        group_name: Filter by shared group name.
        project_id: Filter by shared project ID.
        order_by: Field to sort by (e.g. 'name', 'id', 'description').
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        expand: Comma-separated list of entities to expand.
    """
    params: Dict[str, Any] = {
        "orderBy": order_by,
        "startAt": start_at,
        "maxResults": max_results,
    }
    if filter_name:
        params["filterName"] = filter_name
    if account_id:
        params["accountId"] = account_id
    if group_name:
        params["groupname"] = group_name
    if project_id is not None:
        params["projectId"] = project_id
    if expand:
        params["expand"] = expand
    return jira_get("/filter/search", params=params)


@mcp.tool()
def get_filter_columns(filter_id: str) -> Dict[str, Any]:
    """
    Get the column configuration for a filter (columns shown in issue navigator).

    Args:
        filter_id: The filter ID.
    """
    return jira_get(f"/filter/{filter_id}/columns")


@mcp.tool()
def set_filter_columns(filter_id: str, columns: List[str]) -> Dict[str, Any]:
    """
    Set the column configuration for a filter.

    Args:
        filter_id: The filter ID.
        columns: List of column field IDs (e.g. ['summary', 'status', 'assignee']).
    """
    return jira_put(
        f"/filter/{filter_id}/columns",
        json=[{"value": col} for col in columns],
    )


@mcp.tool()
def reset_filter_columns(filter_id: str) -> Dict[str, Any]:
    """
    Reset the column configuration for a filter to the default.

    Args:
        filter_id: The filter ID.
    """
    return jira_delete(f"/filter/{filter_id}/columns")


@mcp.tool()
def get_filter_sharing(filter_id: str) -> Dict[str, Any]:
    """
    Get the sharing permissions for a filter.

    Args:
        filter_id: The filter ID.
    """
    return jira_get(f"/filter/{filter_id}/permission")


@mcp.tool()
def add_filter_sharing(
    filter_id: str,
    share_type: str,
    project_id: Optional[str] = None,
    project_role_id: Optional[str] = None,
    group_name: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add a sharing permission to a filter.

    Args:
        filter_id: The filter ID.
        share_type: Type of sharing: 'global', 'authenticated', 'project', 'group', 'user'.
        project_id: Project ID (required when share_type='project').
        project_role_id: Project role ID (optional when share_type='project').
        group_name: Group name (required when share_type='group').
    """
    body: Dict[str, Any] = {"type": share_type}
    if project_id:
        body["projectId"] = project_id
    if project_role_id:
        body["projectRoleId"] = project_role_id
    if group_name:
        body["groupname"] = group_name
    return jira_post(f"/filter/{filter_id}/permission", json=body)


@mcp.tool()
def delete_filter_sharing(filter_id: str, permission_id: str) -> Dict[str, Any]:
    """
    Delete a sharing permission from a filter.

    Args:
        filter_id: The filter ID.
        permission_id: The permission ID to delete.
    """
    return jira_delete(f"/filter/{filter_id}/permission/{permission_id}")
