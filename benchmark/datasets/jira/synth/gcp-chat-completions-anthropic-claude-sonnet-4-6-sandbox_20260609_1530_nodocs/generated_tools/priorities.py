"""
MCP tools for Jira Priorities and Statuses.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-priorities-statuses")


# ── Priorities ──────────────────────────────────────────────────────────────

@mcp.tool()
def get_priorities() -> Dict[str, Any]:
    """
    Get all issue priorities (e.g. Highest, High, Medium, Low, Lowest).
    Returns a list of priorities with their IDs, names, and icon URLs.
    """
    return jira_get("/priority")


@mcp.tool()
def get_priority(priority_id: str) -> Dict[str, Any]:
    """
    Get details of a specific priority.

    Args:
        priority_id: The priority ID.
    """
    return jira_get(f"/priority/{priority_id}")


@mcp.tool()
def search_priorities(
    start_at: int = 0,
    max_results: int = 50,
    id_: Optional[str] = None,
    project_id: Optional[str] = None,
    priority_name: Optional[str] = None,
    only_default: bool = False,
) -> Dict[str, Any]:
    """
    Search for priorities with filtering.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        id_: Comma-separated priority IDs to filter by.
        project_id: Filter by project ID.
        priority_name: Filter by priority name (partial match).
        only_default: Return only the default priority.
    """
    params: Dict[str, Any] = {
        "startAt": start_at,
        "maxResults": max_results,
        "onlyDefault": only_default,
    }
    if id_:
        params["id"] = id_
    if project_id:
        params["projectId"] = project_id
    if priority_name:
        params["priorityName"] = priority_name
    return jira_get("/priority/search", params=params)


@mcp.tool()
def create_priority(
    name: str,
    description: Optional[str] = None,
    icon_url: Optional[str] = None,
    status_color: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new issue priority.

    Args:
        name: Priority name.
        description: Priority description.
        icon_url: URL of the priority icon.
        status_color: Hex color code for the priority (e.g. '#FF0000').
    """
    body: Dict[str, Any] = {"name": name}
    if description:
        body["description"] = description
    if icon_url:
        body["iconUrl"] = icon_url
    if status_color:
        body["statusColor"] = status_color
    return jira_post("/priority", json=body)


@mcp.tool()
def update_priority(
    priority_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    icon_url: Optional[str] = None,
    status_color: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update an existing priority.

    Args:
        priority_id: The priority ID.
        name: New priority name.
        description: New priority description.
        icon_url: New icon URL.
        status_color: New hex color code.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if icon_url is not None:
        body["iconUrl"] = icon_url
    if status_color is not None:
        body["statusColor"] = status_color
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/priority/{priority_id}", json=body)


@mcp.tool()
def delete_priority(priority_id: str, replace_with: str) -> Dict[str, Any]:
    """
    Delete a priority and replace it with another.

    Args:
        priority_id: The priority ID to delete.
        replace_with: The priority ID to replace deleted priority with.
    """
    return jira_delete(f"/priority/{priority_id}", params={"replaceWith": replace_with})


@mcp.tool()
def set_default_priority(priority_id: str) -> Dict[str, Any]:
    """
    Set a priority as the default priority.

    Args:
        priority_id: The priority ID to set as default.
    """
    return jira_put("/priority/default", json={"id": priority_id})


@mcp.tool()
def move_priorities(order: List[str]) -> Dict[str, Any]:
    """
    Reorder priorities.

    Args:
        order: List of priority IDs in the desired order.
    """
    return jira_put("/priority/move", json={"ids": order})


# ── Statuses ─────────────────────────────────────────────────────────────────

@mcp.tool()
def get_statuses() -> Dict[str, Any]:
    """
    Get all issue statuses.
    Returns a list of statuses with their IDs, names, and categories.
    """
    return jira_get("/status")


@mcp.tool()
def get_status(id_or_name: str) -> Dict[str, Any]:
    """
    Get details of a specific status by ID or name.

    Args:
        id_or_name: The status ID or name.
    """
    return jira_get(f"/status/{id_or_name}")


@mcp.tool()
def get_status_categories() -> Dict[str, Any]:
    """
    Get all status categories (e.g. To Do, In Progress, Done).
    """
    return jira_get("/statuscategory")


@mcp.tool()
def get_status_category(id_or_key: str) -> Dict[str, Any]:
    """
    Get a specific status category.

    Args:
        id_or_key: The status category ID or key.
    """
    return jira_get(f"/statuscategory/{id_or_key}")


@mcp.tool()
def search_statuses(
    start_at: int = 0,
    max_results: int = 200,
    project_id: Optional[str] = None,
    issue_type_id: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search for statuses with filtering.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        project_id: Filter by project ID.
        issue_type_id: Filter by issue type ID.
        expand: Expand options.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if project_id:
        params["projectId"] = project_id
    if issue_type_id:
        params["issueTypeId"] = issue_type_id
    if expand:
        params["expand"] = expand
    return jira_get("/statuses/search", params=params)
