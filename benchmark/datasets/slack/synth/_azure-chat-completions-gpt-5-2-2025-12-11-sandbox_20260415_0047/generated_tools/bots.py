from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="bots_info")
def bots_info(bot: str) -> Dict[str, Any]:
    """Gets information about a bot user (bots.info)."""

    try:
        return slack_api_call("bots.info", http_method="GET", params={"bot": bot})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
