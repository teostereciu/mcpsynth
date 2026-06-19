from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create an issue.

    POST /rest/api/3/issue

    Args:
        fields: Issue fields payload (must include project, issuetype, summary, etc.).
        update: Optional update section.
    """

    client = JiraClient()
    payload: Dict[str, Any] = {"fields": fields}
    if update is not None:
        payload["update"] = update
    return client.request("POST", "/issue", json=payload)


@mcp.tool()
def jira_get_issue(
    issue_id_or_key: str,
    fields: Optional[list[str]] = None,
    expand: Optional[str] = None,
    properties: Optional[list[str]] = None,
) -> Dict[str, Any]:
    """Get an issue by ID or key.

    GET /rest/api/3/issue/{issueIdOrKey}
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = ",".join(fields)
    if expand:
        params["expand"] = expand
    if properties:
        params["properties"] = ",".join(properties)
    return client.request("GET", f"/issue/{issue_id_or_key}", params=params)


@mcp.tool()
def jira_update_issue(
    issue_id_or_key: str,
    fields: Optional[Dict[str, Any]] = None,
    update: Optional[Dict[str, Any]] = None,
    notify_users: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update an issue.

    PUT /rest/api/3/issue/{issueIdOrKey}

    Returns {"ok": true} on success.
    """

    client = JiraClient()
    payload: Dict[str, Any] = {}
    if fields is not None:
        payload["fields"] = fields
    if update is not None:
        payload["update"] = update
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    return client.request("PUT", f"/issue/{issue_id_or_key}", params=params, json=payload)


@mcp.tool()
def jira_delete_issue(issue_id_or_key: str, delete_subtasks: bool = False) -> Dict[str, Any]:
    """Delete an issue.

    DEL /rest/api/3/issue/{issueIdOrKey}
    """

    client = JiraClient()
    return client.request(
        "DELETE",
        f"/issue/{issue_id_or_key}",
        params={"deleteSubtasks": str(delete_subtasks).lower()},
    )


@mcp.tool()
def jira_assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Dict[str, Any]:
    """Assign an issue to a user.

    PUT /rest/api/3/issue/{issueIdOrKey}/assignee

    Args:
        account_id: Atlassian accountId. If None, unassigns.
    """

    client = JiraClient()
    payload: Dict[str, Any] = {"accountId": account_id}
    return client.request("PUT", f"/issue/{issue_id_or_key}/assignee", json=payload)
