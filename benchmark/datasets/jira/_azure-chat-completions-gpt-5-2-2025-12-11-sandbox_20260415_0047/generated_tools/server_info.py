from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_server_info() -> Dict[str, Any]:
    """Get Jira instance information.

    GET /rest/api/3/serverInfo
    """

    client = JiraClient()
    return client.request("GET", "/serverInfo")
