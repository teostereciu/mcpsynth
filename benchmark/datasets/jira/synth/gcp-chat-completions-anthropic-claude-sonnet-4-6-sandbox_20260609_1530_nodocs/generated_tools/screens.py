"""
MCP tools for Jira Screens and Screen Schemes.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-screens")


@mcp.tool()
def get_screens(
    start_at: int = 0,
    max_results: int = 100,
    id_: Optional[str] = None,
    query_string: Optional[str] = None,
    scope: Optional[str] = None,
    order_by: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all screens.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        id_: Comma-separated screen IDs to filter by.
        query_string: Filter by screen name (partial match).
        scope: Filter by scope: 'GLOBAL', 'TEMPLATE', 'PROJECT'.
        order_by: Field to sort by.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if id_:
        params["id"] = id_
    if query_string:
        params["queryString"] = query_string
    if scope:
        params["scope"] = scope
    if order_by:
        params["orderBy"] = order_by
    return jira_get("/screens", params=params)


@mcp.tool()
def get_screen(screen_id: int) -> Dict[str, Any]:
    """
    Get details of a specific screen.

    Args:
        screen_id: The screen ID.
    """
    return jira_get(f"/screens/{screen_id}")


@mcp.tool()
def create_screen(name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new screen.

    Args:
        name: Screen name.
        description: Screen description.
    """
    body: Dict[str, Any] = {"name": name}
    if description:
        body["description"] = description
    return jira_post("/screens", json=body)


@mcp.tool()
def update_screen(
    screen_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a screen.

    Args:
        screen_id: The screen ID.
        name: New screen name.
        description: New screen description.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/screens/{screen_id}", json=body)


@mcp.tool()
def delete_screen(screen_id: int) -> Dict[str, Any]:
    """
    Delete a screen.

    Args:
        screen_id: The screen ID.
    """
    return jira_delete(f"/screens/{screen_id}")


@mcp.tool()
def get_screen_tabs(screen_id: int, project_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Get all tabs for a screen.

    Args:
        screen_id: The screen ID.
        project_key: Project key to scope the request.
    """
    params: Dict[str, Any] = {}
    if project_key:
        params["projectKey"] = project_key
    return jira_get(f"/screens/{screen_id}/tabs", params=params)


@mcp.tool()
def create_screen_tab(screen_id: int, name: str) -> Dict[str, Any]:
    """
    Create a new tab on a screen.

    Args:
        screen_id: The screen ID.
        name: Tab name.
    """
    return jira_post(f"/screens/{screen_id}/tabs", json={"name": name})


@mcp.tool()
def update_screen_tab(screen_id: int, tab_id: int, name: str) -> Dict[str, Any]:
    """
    Update a screen tab.

    Args:
        screen_id: The screen ID.
        tab_id: The tab ID.
        name: New tab name.
    """
    return jira_put(f"/screens/{screen_id}/tabs/{tab_id}", json={"name": name})


@mcp.tool()
def delete_screen_tab(screen_id: int, tab_id: int) -> Dict[str, Any]:
    """
    Delete a screen tab.

    Args:
        screen_id: The screen ID.
        tab_id: The tab ID.
    """
    return jira_delete(f"/screens/{screen_id}/tabs/{tab_id}")


@mcp.tool()
def get_screen_tab_fields(
    screen_id: int,
    tab_id: int,
    project_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get fields on a screen tab.

    Args:
        screen_id: The screen ID.
        tab_id: The tab ID.
        project_key: Project key to scope the request.
    """
    params: Dict[str, Any] = {}
    if project_key:
        params["projectKey"] = project_key
    return jira_get(f"/screens/{screen_id}/tabs/{tab_id}/fields", params=params)


@mcp.tool()
def add_field_to_screen_tab(screen_id: int, tab_id: int, field_id: str) -> Dict[str, Any]:
    """
    Add a field to a screen tab.

    Args:
        screen_id: The screen ID.
        tab_id: The tab ID.
        field_id: The field ID to add (e.g. 'summary', 'customfield_10001').
    """
    return jira_post(
        f"/screens/{screen_id}/tabs/{tab_id}/fields",
        json={"fieldId": field_id},
    )


@mcp.tool()
def remove_field_from_screen_tab(screen_id: int, tab_id: int, field_id: str) -> Dict[str, Any]:
    """
    Remove a field from a screen tab.

    Args:
        screen_id: The screen ID.
        tab_id: The tab ID.
        field_id: The field ID to remove.
    """
    return jira_delete(f"/screens/{screen_id}/tabs/{tab_id}/fields/{field_id}")


@mcp.tool()
def get_available_screen_fields(screen_id: int) -> Dict[str, Any]:
    """
    Get fields that can be added to a screen (not yet on any tab).

    Args:
        screen_id: The screen ID.
    """
    return jira_get(f"/screens/{screen_id}/availableFields")


@mcp.tool()
def get_screen_schemes(
    start_at: int = 0,
    max_results: int = 25,
    id_: Optional[str] = None,
    expand: Optional[str] = None,
    query_string: Optional[str] = None,
    order_by: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all screen schemes.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        id_: Comma-separated screen scheme IDs to filter by.
        expand: Expand options.
        query_string: Filter by name (partial match).
        order_by: Field to sort by.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if id_:
        params["id"] = id_
    if expand:
        params["expand"] = expand
    if query_string:
        params["queryString"] = query_string
    if order_by:
        params["orderBy"] = order_by
    return jira_get("/screenscheme", params=params)
