from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_votes(issue_id_or_key: str) -> Dict[str, Any]:
    """Get votes on an issue.

    GET /rest/api/3/issue/{issueIdOrKey}/votes
    """

    client = JiraClient()
    return client.request("GET", f"/issue/{issue_id_or_key}/votes")


@mcp.tool()
def jira_add_vote(issue_id_or_key: str) -> Dict[str, Any]:
    """Add current user's vote to an issue.

    POST /rest/api/3/issue/{issueIdOrKey}/votes
    """

    client = JiraClient()
    return client.request("POST", f"/issue/{issue_id_or_key}/votes")


@mcp.tool()
def jira_remove_vote(issue_id_or_key: str) -> Dict[str, Any]:
    """Remove current user's vote from an issue.

    DEL /rest/api/3/issue/{issueIdOrKey}/votes
    """

    client = JiraClient()
    return client.request("DELETE", f"/issue/{issue_id_or_key}/votes")
