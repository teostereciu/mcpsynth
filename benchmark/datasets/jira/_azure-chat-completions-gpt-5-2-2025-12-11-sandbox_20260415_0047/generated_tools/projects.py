from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_list_projects(max_results: int = 50) -> Dict[str, Any]:
    """List projects visible to the current user.

    Uses GET /rest/api/3/project/search for pagination.
    """

    client = JiraClient()
    return client.request(
        "GET",
        "/project/search",
        params={"startAt": 0, "maxResults": max_results},
    )


@mcp.tool()
def jira_get_project(project_id_or_key: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """Get a project by ID or key.

    GET /rest/api/3/project/{projectIdOrKey}
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/project/{project_id_or_key}", params=params)


@mcp.tool()
def jira_search_projects(
    query: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
    order_by: Optional[str] = None,
    keys: Optional[list[str]] = None,
    type_key: Optional[str] = None,
) -> Dict[str, Any]:
    """Search projects with pagination.

    GET /rest/api/3/project/search
    """

    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if query:
        params["query"] = query
    if order_by:
        params["orderBy"] = order_by
    if keys:
        params["keys"] = keys
    if type_key:
        params["typeKey"] = type_key
    return client.request("GET", "/project/search", params=params)


@mcp.tool()
def jira_create_project(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create a project.

    POST /rest/api/3/project

    Provide the request body as `payload`.
    """

    client = JiraClient()
    return client.request("POST", "/project", json=payload)
