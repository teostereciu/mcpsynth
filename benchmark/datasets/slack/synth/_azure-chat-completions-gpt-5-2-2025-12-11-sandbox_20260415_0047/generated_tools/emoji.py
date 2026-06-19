from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="emoji_list")
def emoji_list() -> Dict[str, Any]:
    """Lists custom emoji for a team (emoji.list)."""

    try:
        return slack_api_call("emoji.list", http_method="GET", params={})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
