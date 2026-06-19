from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="team_info")
def team_info(team: Optional[str] = None) -> Dict[str, Any]:
    """Gets information about the current team (team.info)."""

    params: Dict[str, Any] = {}
    if team is not None:
        params["team"] = team

    try:
        return slack_api_call("team.info", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="team_access_logs")
def team_access_logs(
    count: Optional[int] = None,
    page: Optional[int] = None,
    before: Optional[int] = None,
) -> Dict[str, Any]:
    """Gets the access logs for the current team (team.accessLogs)."""

    params: Dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    if page is not None:
        params["page"] = page
    if before is not None:
        params["before"] = before

    try:
        return slack_api_call("team.accessLogs", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
