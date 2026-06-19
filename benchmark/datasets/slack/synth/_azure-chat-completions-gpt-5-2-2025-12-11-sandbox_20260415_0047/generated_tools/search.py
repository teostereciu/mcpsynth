from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="search_messages")
def search_messages(
    query: str,
    count: Optional[int] = None,
    page: Optional[int] = None,
    highlight: Optional[bool] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    cursor: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Searches for messages matching a query (search.messages).

    Note: Slack's legacy search.* endpoints typically require a user token with search:read.
    If the bot token lacks scope, Slack returns ok:false with error=missing_scope.
    """

    params: Dict[str, Any] = {"query": query}
    if count is not None:
        params["count"] = count
    if page is not None:
        params["page"] = page
    if highlight is not None:
        params["highlight"] = highlight
    if sort is not None:
        params["sort"] = sort
    if sort_dir is not None:
        params["sort_dir"] = sort_dir
    if cursor is not None:
        params["cursor"] = cursor
    if team_id is not None:
        params["team_id"] = team_id

    try:
        return slack_api_call("search.messages", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="search_all")
def search_all(
    query: str,
    count: Optional[int] = None,
    page: Optional[int] = None,
    highlight: Optional[bool] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Searches for messages and files matching a query (search.all)."""

    params: Dict[str, Any] = {"query": query}
    if count is not None:
        params["count"] = count
    if page is not None:
        params["page"] = page
    if highlight is not None:
        params["highlight"] = highlight
    if sort is not None:
        params["sort"] = sort
    if sort_dir is not None:
        params["sort_dir"] = sort_dir
    if team_id is not None:
        params["team_id"] = team_id

    try:
        return slack_api_call("search.all", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="search_files")
def search_files(
    query: str,
    count: Optional[int] = None,
    page: Optional[int] = None,
    highlight: Optional[bool] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Searches for files matching a query (search.files)."""

    params: Dict[str, Any] = {"query": query}
    if count is not None:
        params["count"] = count
    if page is not None:
        params["page"] = page
    if highlight is not None:
        params["highlight"] = highlight
    if sort is not None:
        params["sort"] = sort
    if sort_dir is not None:
        params["sort_dir"] = sort_dir
    if team_id is not None:
        params["team_id"] = team_id

    try:
        return slack_api_call("search.files", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
