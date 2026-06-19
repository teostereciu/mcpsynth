from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="dnd_info")
def dnd_info(user: Optional[str] = None) -> Dict[str, Any]:
    """Retrieves a user's current Do Not Disturb status (dnd.info)."""

    params: Dict[str, Any] = {}
    if user is not None:
        params["user"] = user

    try:
        return slack_api_call("dnd.info", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="dnd_team_info")
def dnd_team_info(users: Optional[str] = None) -> Dict[str, Any]:
    """Retrieves DND status for up to 50 users (dnd.teamInfo)."""

    params: Dict[str, Any] = {}
    if users is not None:
        params["users"] = users

    try:
        return slack_api_call("dnd.teamInfo", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
