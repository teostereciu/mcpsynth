from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_add_comment(
    issue_id_or_key: str,
    body: Dict[str, Any],
    visibility: Optional[Dict[str, Any]] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """Add a comment to an issue.

    POST /rest/api/3/issue/{issueIdOrKey}/comment

    Args:
        body: ADF document.
        visibility: Optional visibility object.
    """

    client = JiraClient()
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("POST", f"/issue/{issue_id_or_key}/comment", params=params, json=payload)


@mcp.tool()
def jira_get_comments(
    issue_id_or_key: str,
    start_at: int = 0,
    max_results: int = 50,
    order_by: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """Get comments for an issue.

    GET /rest/api/3/issue/{issueIdOrKey}/comment
    """

    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if order_by:
        params["orderBy"] = order_by
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/comment", params=params)


@mcp.tool()
def jira_get_comment(issue_id_or_key: str, comment_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """Get a single comment.

    GET /rest/api/3/issue/{issueIdOrKey}/comment/{id}
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params)


@mcp.tool()
def jira_update_comment(
    issue_id_or_key: str,
    comment_id: str,
    body: Dict[str, Any],
    visibility: Optional[Dict[str, Any]] = None,
    notify_users: Optional[bool] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a comment.

    PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}
    """

    client = JiraClient()
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if expand:
        params["expand"] = expand
    return client.request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params, json=payload)


@mcp.tool()
def jira_delete_comment(issue_id_or_key: str, comment_id: str) -> Dict[str, Any]:
    """Delete a comment.

    DEL /rest/api/3/issue/{issueIdOrKey}/comment/{id}
    """

    client = JiraClient()
    return client.request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")


@mcp.tool()
def jira_get_comments_by_ids(ids: list[int], expand: Optional[str] = None) -> Dict[str, Any]:
    """Get comments by IDs.

    POST /rest/api/3/comment/list
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("POST", "/comment/list", params=params, json={"ids": ids})
