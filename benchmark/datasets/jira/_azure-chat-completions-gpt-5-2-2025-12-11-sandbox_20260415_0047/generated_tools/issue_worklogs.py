from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_worklogs(
    issue_id_or_key: str,
    start_at: int = 0,
    max_results: int = 50,
    started_after: Optional[int] = None,
    started_before: Optional[int] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """Get worklogs for an issue.

    GET /rest/api/3/issue/{issueIdOrKey}/worklog
    """

    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if started_after is not None:
        params["startedAfter"] = started_after
    if started_before is not None:
        params["startedBefore"] = started_before
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/worklog", params=params)


@mcp.tool()
def jira_add_worklog(
    issue_id_or_key: str,
    time_spent_seconds: int,
    started: str,
    comment: Optional[Dict[str, Any]] = None,
    visibility: Optional[Dict[str, Any]] = None,
    notify_users: Optional[bool] = None,
    adjust_estimate: Optional[str] = None,
    new_estimate: Optional[str] = None,
    reduce_by: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """Add a worklog to an issue.

    POST /rest/api/3/issue/{issueIdOrKey}/worklog
    """

    client = JiraClient()
    payload: Dict[str, Any] = {"timeSpentSeconds": time_spent_seconds, "started": started}
    if comment is not None:
        payload["comment"] = comment
    if visibility is not None:
        payload["visibility"] = visibility

    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if adjust_estimate is not None:
        params["adjustEstimate"] = adjust_estimate
    if new_estimate is not None:
        params["newEstimate"] = new_estimate
    if reduce_by is not None:
        params["reduceBy"] = reduce_by
    if expand is not None:
        params["expand"] = expand

    return client.request("POST", f"/issue/{issue_id_or_key}/worklog", params=params, json=payload)
