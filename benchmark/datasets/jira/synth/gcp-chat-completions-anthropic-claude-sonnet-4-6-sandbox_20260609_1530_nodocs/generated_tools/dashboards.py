"""
MCP tools for Jira Dashboards.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-dashboards")


@mcp.tool()
def get_dashboards(
    filter_: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Get all dashboards accessible to the current user.

    Args:
        filter_: Filter by ownership: 'my' (owned by me), 'favourite' (my favourites).
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if filter_:
        params["filter"] = filter_
    return jira_get("/dashboard", params=params)


@mcp.tool()
def search_dashboards(
    dashboard_name: Optional[str] = None,
    account_id: Optional[str] = None,
    group_permission: Optional[str] = None,
    project_permission_id: Optional[str] = None,
    order_by: str = "name",
    start_at: int = 0,
    max_results: int = 50,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search for dashboards with filtering.

    Args:
        dashboard_name: Filter by dashboard name (partial match).
        account_id: Filter by owner account ID.
        group_permission: Filter by group permission name.
        project_permission_id: Filter by project permission ID.
        order_by: Field to sort by (e.g. 'name', 'id', 'description').
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        expand: Expand options.
    """
    params: Dict[str, Any] = {
        "orderBy": order_by,
        "startAt": start_at,
        "maxResults": max_results,
    }
    if dashboard_name:
        params["dashboardName"] = dashboard_name
    if account_id:
        params["accountId"] = account_id
    if group_permission:
        params["groupPermission"] = group_permission
    if project_permission_id:
        params["projectPermissionId"] = project_permission_id
    if expand:
        params["expand"] = expand
    return jira_get("/dashboard/search", params=params)


@mcp.tool()
def get_dashboard(dashboard_id: str) -> Dict[str, Any]:
    """
    Get details of a specific dashboard.

    Args:
        dashboard_id: The dashboard ID.
    """
    return jira_get(f"/dashboard/{dashboard_id}")


@mcp.tool()
def create_dashboard(
    name: str,
    description: Optional[str] = None,
    share_permissions: Optional[List[Dict[str, Any]]] = None,
    edit_permissions: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Create a new dashboard.

    Args:
        name: Dashboard name.
        description: Dashboard description.
        share_permissions: List of share permission dicts.
                           Example: [{"type": "global"}] or [{"type": "group", "group": {"name": "jira-users"}}]
        edit_permissions: List of edit permission dicts (same format as share_permissions).
    """
    body: Dict[str, Any] = {
        "name": name,
        "sharePermissions": share_permissions or [],
        "editPermissions": edit_permissions or [],
    }
    if description:
        body["description"] = description
    return jira_post("/dashboard", json=body)


@mcp.tool()
def update_dashboard(
    dashboard_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    share_permissions: Optional[List[Dict[str, Any]]] = None,
    edit_permissions: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Update an existing dashboard.

    Args:
        dashboard_id: The dashboard ID.
        name: New dashboard name.
        description: New dashboard description.
        share_permissions: New share permissions list.
        edit_permissions: New edit permissions list.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if share_permissions is not None:
        body["sharePermissions"] = share_permissions
    if edit_permissions is not None:
        body["editPermissions"] = edit_permissions
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/dashboard/{dashboard_id}", json=body)


@mcp.tool()
def delete_dashboard(dashboard_id: str) -> Dict[str, Any]:
    """
    Delete a dashboard.

    Args:
        dashboard_id: The dashboard ID.
    """
    return jira_delete(f"/dashboard/{dashboard_id}")


@mcp.tool()
def copy_dashboard(
    dashboard_id: str,
    name: str,
    description: Optional[str] = None,
    share_permissions: Optional[List[Dict[str, Any]]] = None,
    edit_permissions: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Copy an existing dashboard.

    Args:
        dashboard_id: The source dashboard ID to copy.
        name: Name for the new dashboard.
        description: Description for the new dashboard.
        share_permissions: Share permissions for the new dashboard.
        edit_permissions: Edit permissions for the new dashboard.
    """
    body: Dict[str, Any] = {
        "name": name,
        "sharePermissions": share_permissions or [],
        "editPermissions": edit_permissions or [],
    }
    if description:
        body["description"] = description
    return jira_post(f"/dashboard/{dashboard_id}/copy", json=body)


@mcp.tool()
def get_dashboard_gadgets(dashboard_id: str) -> Dict[str, Any]:
    """
    Get all gadgets on a dashboard.

    Args:
        dashboard_id: The dashboard ID.
    """
    return jira_get(f"/dashboard/{dashboard_id}/gadget")


@mcp.tool()
def add_dashboard_gadget(
    dashboard_id: str,
    module_key: Optional[str] = None,
    uri: Optional[str] = None,
    color: str = "blue",
    position: Optional[Dict[str, int]] = None,
    title: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add a gadget to a dashboard.

    Args:
        dashboard_id: The dashboard ID.
        module_key: The gadget module key (e.g. 'com.atlassian.jira.gadgets:assigned-to-me-gadget').
        uri: The gadget URI (alternative to module_key).
        color: Gadget color: 'blue', 'red', 'yellow', 'green', 'cyan', 'purple', 'gray', 'white'.
        position: Position dict with 'column' and 'row' (e.g. {"column": 0, "row": 0}).
        title: Gadget title.
    """
    body: Dict[str, Any] = {"color": color}
    if module_key:
        body["moduleKey"] = module_key
    if uri:
        body["uri"] = uri
    if position:
        body["position"] = position
    if title:
        body["title"] = title
    return jira_post(f"/dashboard/{dashboard_id}/gadget", json=body)


@mcp.tool()
def update_dashboard_gadget(
    dashboard_id: str,
    gadget_id: int,
    color: Optional[str] = None,
    position: Optional[Dict[str, int]] = None,
    title: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a gadget on a dashboard.

    Args:
        dashboard_id: The dashboard ID.
        gadget_id: The gadget ID.
        color: New gadget color.
        position: New position dict with 'column' and 'row'.
        title: New gadget title.
    """
    body: Dict[str, Any] = {}
    if color is not None:
        body["color"] = color
    if position is not None:
        body["position"] = position
    if title is not None:
        body["title"] = title
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/dashboard/{dashboard_id}/gadget/{gadget_id}", json=body)


@mcp.tool()
def remove_dashboard_gadget(dashboard_id: str, gadget_id: int) -> Dict[str, Any]:
    """
    Remove a gadget from a dashboard.

    Args:
        dashboard_id: The dashboard ID.
        gadget_id: The gadget ID.
    """
    return jira_delete(f"/dashboard/{dashboard_id}/gadget/{gadget_id}")


@mcp.tool()
def get_dashboard_item_property(
    dashboard_id: str, item_id: str, property_key: str
) -> Dict[str, Any]:
    """
    Get a property of a dashboard item (gadget).

    Args:
        dashboard_id: The dashboard ID.
        item_id: The dashboard item (gadget) ID.
        property_key: The property key.
    """
    return jira_get(f"/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}")


@mcp.tool()
def set_dashboard_item_property(
    dashboard_id: str, item_id: str, property_key: str, value: Any
) -> Dict[str, Any]:
    """
    Set a property on a dashboard item (gadget).

    Args:
        dashboard_id: The dashboard ID.
        item_id: The dashboard item (gadget) ID.
        property_key: The property key.
        value: The property value (any JSON-serializable value).
    """
    return jira_put(
        f"/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}",
        json=value,
    )
