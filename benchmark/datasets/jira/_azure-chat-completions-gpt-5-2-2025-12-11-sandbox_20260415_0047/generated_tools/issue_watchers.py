from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_watchers(issue_id_or_key: str) -> Dict[str, Any]:
    """Get watchers for an issue.

    GET /rest/api/3/issue/{issueIdOrKey}/watchers
    """

    client = JiraClient()
    return client.request("GET", f"/issue/{issue_id_or_key}/watchers")


@mcp.tool()
def jira_add_watcher(issue_id_or_key: str, account_id: Optional[str] = None) -> Dict[str, Any]:
    """Add a watcher to an issue.

    POST /rest/api/3/issue/{issueIdOrKey}/watchers

    Jira expects the request body to be a JSON string containing the accountId.
    If account_id is None, Jira adds the calling user.
    """

    client = JiraClient()
    body = account_id if account_id is not None else ""
    return client.request(
        "POST",
        f"/issue/{issue_id_or_key}/watchers",
        headers={"Content-Type": "application/json"},
        data=f"\"{body}\"" if body else "\"\"",
    )


@mcp.tool()
def jira_remove_watcher(issue_id_or_key: str, account_id: str) -> Dict[str, Any]:
    """Remove a watcher from an issue.

    DEL /rest/api/3/issue/{issueIdOrKey}/watchers?accountId=...
    """

    client = JiraClient()
    return client.request(
        "DELETE",
        f"/issue/{issue_id_or_key}/watchers",
        params={"accountId": account_id},
    )


@mcp.tool()
def jira_is_watching_bulk(issue_ids: list[str]) -> Dict[str, Any]:
    """Get watched status for a list of issue IDs.

    POST /rest/api/3/issue/watching
    """

    client = JiraClient()
    return client.request("POST", "/issue/watching", json={"issueIds": issue_ids})
