"""
MCP tools for Jira Issue Worklogs.
"""

from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-worklogs")


@mcp.tool()
def get_issue_worklogs(
    issue_id_or_key: str,
    start_at: int = 0,
    max_results: int = 50,
    started_after: Optional[int] = None,
    started_before: Optional[int] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get worklogs for a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        start_at: Index of the first worklog to return.
        max_results: Maximum number of worklogs to return.
        started_after: Return worklogs started after this epoch millisecond timestamp.
        started_before: Return worklogs started before this epoch millisecond timestamp.
        expand: Expand options (e.g. 'properties').
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if started_after is not None:
        params["startedAfter"] = started_after
    if started_before is not None:
        params["startedBefore"] = started_before
    if expand:
        params["expand"] = expand
    return jira_get(f"/issue/{issue_id_or_key}/worklog", params=params)


@mcp.tool()
def get_worklog(issue_id_or_key: str, worklog_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a single worklog entry from an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        worklog_id: The worklog ID.
        expand: Expand options.
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params)


@mcp.tool()
def add_worklog(
    issue_id_or_key: str,
    time_spent: str,
    comment: Optional[str] = None,
    started: Optional[str] = None,
    adjust_estimate: str = "auto",
    new_estimate: Optional[str] = None,
    reduce_by: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add a worklog entry to a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        time_spent: Time spent in Jira duration format (e.g. '2h 30m', '1d').
        comment: Optional comment for the worklog.
        started: Start date/time in ISO 8601 format (e.g. '2024-01-15T09:00:00.000+0000').
                 Defaults to current time if not provided.
        adjust_estimate: How to adjust the remaining estimate:
                         'auto' (default), 'new', 'leave', 'manual'.
        new_estimate: New remaining estimate (used when adjust_estimate='new').
        reduce_by: Amount to reduce remaining estimate by (used when adjust_estimate='manual').
    """
    body: Dict[str, Any] = {"timeSpent": time_spent}
    if comment:
        body["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment}],
                }
            ],
        }
    if started:
        body["started"] = started
    params: Dict[str, Any] = {"adjustEstimate": adjust_estimate}
    if new_estimate:
        params["newEstimate"] = new_estimate
    if reduce_by:
        params["reduceBy"] = reduce_by
    return jira_post(f"/issue/{issue_id_or_key}/worklog", json=body, params=params)


@mcp.tool()
def update_worklog(
    issue_id_or_key: str,
    worklog_id: str,
    time_spent: Optional[str] = None,
    comment: Optional[str] = None,
    started: Optional[str] = None,
    adjust_estimate: str = "auto",
    new_estimate: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update an existing worklog entry on a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        worklog_id: The worklog ID.
        time_spent: New time spent in Jira duration format (e.g. '3h').
        comment: New comment for the worklog.
        started: New start date/time in ISO 8601 format.
        adjust_estimate: How to adjust the remaining estimate: 'auto', 'new', 'leave'.
        new_estimate: New remaining estimate (used when adjust_estimate='new').
    """
    body: Dict[str, Any] = {}
    if time_spent:
        body["timeSpent"] = time_spent
    if comment:
        body["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment}],
                }
            ],
        }
    if started:
        body["started"] = started
    params: Dict[str, Any] = {"adjustEstimate": adjust_estimate}
    if new_estimate:
        params["newEstimate"] = new_estimate
    return jira_put(
        f"/issue/{issue_id_or_key}/worklog/{worklog_id}", json=body, params=params
    )


@mcp.tool()
def delete_worklog(
    issue_id_or_key: str,
    worklog_id: str,
    adjust_estimate: str = "auto",
    new_estimate: Optional[str] = None,
    increase_by: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Delete a worklog entry from a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        worklog_id: The worklog ID.
        adjust_estimate: How to adjust the remaining estimate: 'auto', 'new', 'leave', 'manual'.
        new_estimate: New remaining estimate (used when adjust_estimate='new').
        increase_by: Amount to increase remaining estimate by (used when adjust_estimate='manual').
    """
    params: Dict[str, Any] = {"adjustEstimate": adjust_estimate}
    if new_estimate:
        params["newEstimate"] = new_estimate
    if increase_by:
        params["increaseBy"] = increase_by
    return jira_delete(
        f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params
    )


@mcp.tool()
def get_updated_worklogs(since: int) -> Dict[str, Any]:
    """
    Get a list of worklog IDs that were updated since a given timestamp.
    Useful for syncing worklogs.

    Args:
        since: Epoch millisecond timestamp. Returns worklogs updated after this time.
    """
    return jira_get("/worklog/updated", params={"since": since})


@mcp.tool()
def get_deleted_worklogs(since: int) -> Dict[str, Any]:
    """
    Get a list of worklog IDs that were deleted since a given timestamp.

    Args:
        since: Epoch millisecond timestamp. Returns worklogs deleted after this time.
    """
    return jira_get("/worklog/deleted", params={"since": since})
