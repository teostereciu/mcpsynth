from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_current_user(expand: Optional[str] = None) -> Dict[str, Any]:
    """Get details for the current user.

    Maps to GET /rest/api/3/myself
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/myself", params=params)
