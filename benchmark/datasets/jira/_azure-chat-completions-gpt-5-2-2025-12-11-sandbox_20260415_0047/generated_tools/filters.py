from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_create_filter(name: str, jql: str, description: Optional[str] = None, favourite: Optional[bool] = None) -> Dict[str, Any]:
    """Create a saved filter.

    POST /rest/api/3/filter
    """

    client = JiraClient()
    payload: Dict[str, Any] = {"name": name, "jql": jql}
    if description is not None:
        payload["description"] = description
    if favourite is not None:
        payload["favourite"] = favourite
    return client.request("POST", "/filter", json=payload)


@mcp.tool()
def jira_get_filter(filter_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """Get a filter by ID.

    GET /rest/api/3/filter/{id}
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/filter/{filter_id}", params=params)


@mcp.tool()
def jira_update_filter(filter_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Update a filter.

    PUT /rest/api/3/filter/{id}
    """

    client = JiraClient()
    return client.request("PUT", f"/filter/{filter_id}", json=payload)


@mcp.tool()
def jira_delete_filter(filter_id: str) -> Dict[str, Any]:
    """Delete a filter.

    DEL /rest/api/3/filter/{id}
    """

    client = JiraClient()
    return client.request("DELETE", f"/filter/{filter_id}")


@mcp.tool()
def jira_search_filters(
    filter_name: Optional[str] = None,
    account_id: Optional[str] = None,
    group_id: Optional[str] = None,
    group_name: Optional[str] = None,
    project_id: Optional[int] = None,
    ids: Optional[list[int]] = None,
    order_by: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """Search filters.

    GET /rest/api/3/filter/search
    """

    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if filter_name is not None:
        params["filterName"] = filter_name
    if account_id is not None:
        params["accountId"] = account_id
    if group_id is not None:
        params["groupId"] = group_id
    if group_name is not None:
        params["groupname"] = group_name
    if project_id is not None:
        params["projectId"] = project_id
    if ids is not None:
        params["id"] = ids
    if order_by is not None:
        params["orderBy"] = order_by
    return client.request("GET", "/filter/search", params=params)


@mcp.tool()
def jira_get_my_filters(include_favourites: bool = False, expand: Optional[str] = None) -> Dict[str, Any]:
    """Get filters owned by the current user.

    GET /rest/api/3/filter/my
    """

    client = JiraClient()
    params: Dict[str, Any] = {"includeFavourites": str(include_favourites).lower()}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/filter/my", params=params)


@mcp.tool()
def jira_get_favourite_filters(expand: Optional[str] = None) -> Dict[str, Any]:
    """Get favourite filters.

    GET /rest/api/3/filter/favourite
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/filter/favourite", params=params)
