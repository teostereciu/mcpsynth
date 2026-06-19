from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_list_dashboards(start_at: int = 0, max_results: int = 50, filter: Optional[str] = None) -> Dict[str, Any]:
    """List dashboards.

    GET /rest/api/3/dashboard
    """

    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", "/dashboard", params=params)


@mcp.tool()
def jira_get_dashboard(dashboard_id: str) -> Dict[str, Any]:
    """Get a dashboard.

    GET /rest/api/3/dashboard/{id}
    """

    client = JiraClient()
    return client.request("GET", f"/dashboard/{dashboard_id}")


@mcp.tool()
def jira_search_dashboards(
    dashboard_name: Optional[str] = None,
    account_id: Optional[str] = None,
    group_id: Optional[str] = None,
    group_name: Optional[str] = None,
    project_id: Optional[int] = None,
    order_by: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """Search dashboards.

    GET /rest/api/3/dashboard/search
    """

    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if dashboard_name is not None:
        params["dashboardName"] = dashboard_name
    if account_id is not None:
        params["accountId"] = account_id
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    if project_id is not None:
        params["projectId"] = project_id
    if order_by is not None:
        params["orderBy"] = order_by
    if status is not None:
        params["status"] = status
    return client.request("GET", "/dashboard/search", params=params)


@mcp.tool()
def jira_create_dashboard(payload: Dict[str, Any], extend_admin_permissions: Optional[bool] = None) -> Dict[str, Any]:
    """Create a dashboard.

    POST /rest/api/3/dashboard
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if extend_admin_permissions is not None:
        params["extendAdminPermissions"] = str(extend_admin_permissions).lower()
    return client.request("POST", "/dashboard", params=params, json=payload)


@mcp.tool()
def jira_get_dashboard_gadgets(dashboard_id: int) -> Dict[str, Any]:
    """Get gadgets on a dashboard.

    GET /rest/api/3/dashboard/{dashboardId}/gadget
    """

    client = JiraClient()
    return client.request("GET", f"/dashboard/{dashboard_id}/gadget")


@mcp.tool()
def jira_get_available_gadgets() -> Dict[str, Any]:
    """Get available gadgets.

    GET /rest/api/3/dashboard/gadgets
    """

    client = JiraClient()
    return client.request("GET", "/dashboard/gadgets")
