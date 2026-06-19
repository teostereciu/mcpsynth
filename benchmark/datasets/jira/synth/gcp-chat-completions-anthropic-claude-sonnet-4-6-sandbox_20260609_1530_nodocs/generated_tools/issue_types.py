"""
MCP tools for Jira Issue Types.
"""

from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-issue-types")


@mcp.tool()
def get_all_issue_types() -> Dict[str, Any]:
    """
    Get all issue types available to the current user.
    Returns a list of issue types with their IDs, names, and descriptions.
    """
    return jira_get("/issuetype")


@mcp.tool()
def get_issue_type(issue_type_id: str) -> Dict[str, Any]:
    """
    Get details of a specific issue type.

    Args:
        issue_type_id: The issue type ID.
    """
    return jira_get(f"/issuetype/{issue_type_id}")


@mcp.tool()
def create_issue_type(
    name: str,
    description: Optional[str] = None,
    type_: str = "standard",
    hierarchy_level: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Create a new issue type.

    Args:
        name: Issue type name.
        description: Issue type description.
        type_: Issue type category: 'standard' or 'subtask'.
        hierarchy_level: Hierarchy level (0 for standard, -1 for subtask).
    """
    body: Dict[str, Any] = {"name": name, "type": type_}
    if description:
        body["description"] = description
    if hierarchy_level is not None:
        body["hierarchyLevel"] = hierarchy_level
    return jira_post("/issuetype", json=body)


@mcp.tool()
def update_issue_type(
    issue_type_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    avatar_id: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Update an existing issue type.

    Args:
        issue_type_id: The issue type ID.
        name: New issue type name.
        description: New issue type description.
        avatar_id: New avatar ID for the issue type.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if avatar_id is not None:
        body["avatarId"] = avatar_id
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/issuetype/{issue_type_id}", json=body)


@mcp.tool()
def delete_issue_type(
    issue_type_id: str,
    alternative_issue_type_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Delete an issue type.

    Args:
        issue_type_id: The issue type ID to delete.
        alternative_issue_type_id: Issue type ID to migrate existing issues to.
    """
    params: Dict[str, Any] = {}
    if alternative_issue_type_id:
        params["alternativeIssueTypeId"] = alternative_issue_type_id
    return jira_delete(f"/issuetype/{issue_type_id}", params=params)


@mcp.tool()
def get_issue_type_alternatives(issue_type_id: str) -> Dict[str, Any]:
    """
    Get a list of issue types that can be used as alternatives to the given issue type.
    Useful when deleting an issue type to find valid migration targets.

    Args:
        issue_type_id: The issue type ID.
    """
    return jira_get(f"/issuetype/{issue_type_id}/alternatives")


@mcp.tool()
def get_issue_types_for_project(
    project_id: int,
    level: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Get issue types available for a specific project.

    Args:
        project_id: The project ID (numeric).
        level: Hierarchy level filter (-1 for subtasks, 0 for standard, 1 for epics).
    """
    params: Dict[str, Any] = {"projectId": project_id}
    if level is not None:
        params["level"] = level
    return jira_get("/issuetype/project", params=params)


@mcp.tool()
def get_issue_type_screen_schemes() -> Dict[str, Any]:
    """
    Get all issue type screen schemes.
    """
    return jira_get("/issuetypescreenscheme")


@mcp.tool()
def get_issue_type_schemes(
    start_at: int = 0,
    max_results: int = 50,
    id_: Optional[str] = None,
    order_by: str = "name",
    expand: Optional[str] = None,
    query_string: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all issue type schemes.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        id_: Comma-separated list of issue type scheme IDs to filter by.
        order_by: Field to sort by.
        expand: Comma-separated list of entities to expand.
        query_string: Filter by name.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results, "orderBy": order_by}
    if id_:
        params["id"] = id_
    if expand:
        params["expand"] = expand
    if query_string:
        params["queryString"] = query_string
    return jira_get("/issuetypescheme", params=params)
