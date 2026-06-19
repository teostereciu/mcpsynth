from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_user(account_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """Get a user by accountId.

    GET /rest/api/3/user
    """

    client = JiraClient()
    params: Dict[str, Any] = {"accountId": account_id}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/user", params=params)


@mcp.tool()
def jira_search_users(
    query: str,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """Search users.

    GET /rest/api/3/users/search

    Note: Jira's user search API uses `query`.
    """

    client = JiraClient()
    return client.request(
        "GET",
        "/users/search",
        params={"query": query, "startAt": start_at, "maxResults": max_results},
    )


@mcp.tool()
def jira_get_users_bulk(account_ids: list[str], start_at: int = 0, max_results: int = 100) -> Dict[str, Any]:
    """Bulk get users by accountId.

    GET /rest/api/3/user/bulk
    """

    client = JiraClient()
    return client.request(
        "GET",
        "/user/bulk",
        params={"accountId": account_ids, "startAt": start_at, "maxResults": max_results},
    )
