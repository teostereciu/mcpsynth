from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="usergroups_list")
def usergroups_list(include_users: Optional[bool] = None, include_disabled: Optional[bool] = None) -> Dict[str, Any]:
    """Lists user groups for a team (usergroups.list)."""

    params: Dict[str, Any] = {}
    if include_users is not None:
        params["include_users"] = include_users
    if include_disabled is not None:
        params["include_disabled"] = include_disabled

    try:
        return slack_api_call("usergroups.list", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
