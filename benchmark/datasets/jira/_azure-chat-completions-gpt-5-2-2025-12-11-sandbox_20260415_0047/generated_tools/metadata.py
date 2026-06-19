from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_list_issue_types() -> Dict[str, Any]:
    """List issue types visible to the user.

    GET /rest/api/3/issuetype
    """

    client = JiraClient()
    return client.request("GET", "/issuetype")


@mcp.tool()
def jira_get_issue_type(issue_type_id: str) -> Dict[str, Any]:
    """Get an issue type.

    GET /rest/api/3/issuetype/{id}
    """

    client = JiraClient()
    return client.request("GET", f"/issuetype/{issue_type_id}")


@mcp.tool()
def jira_list_priorities() -> Dict[str, Any]:
    """List issue priorities.

    GET /rest/api/3/priority
    """

    client = JiraClient()
    return client.request("GET", "/priority")


@mcp.tool()
def jira_get_priority(priority_id: str) -> Dict[str, Any]:
    """Get an issue priority.

    GET /rest/api/3/priority/{id}
    """

    client = JiraClient()
    return client.request("GET", f"/priority/{priority_id}")
