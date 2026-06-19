"""
MCP tools for Jira Issue Comments.
"""

from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-comments")


def _adf_body(text: str) -> Dict[str, Any]:
    """Convert plain text to Atlassian Document Format."""
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [{"type": "text", "text": text}],
            }
        ],
    }


@mcp.tool()
def get_issue_comments(
    issue_id_or_key: str,
    start_at: int = 0,
    max_results: int = 50,
    order_by: str = "created",
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get comments for a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        start_at: Index of the first comment to return.
        max_results: Maximum number of comments to return.
        order_by: Field to sort by ('created' or '-created' for descending).
        expand: Expand options (e.g. 'renderedBody').
    """
    params: Dict[str, Any] = {
        "startAt": start_at,
        "maxResults": max_results,
        "orderBy": order_by,
    }
    if expand:
        params["expand"] = expand
    return jira_get(f"/issue/{issue_id_or_key}/comment", params=params)


@mcp.tool()
def get_comment(issue_id_or_key: str, comment_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a single comment from an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        comment_id: The comment ID.
        expand: Expand options (e.g. 'renderedBody').
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params)


@mcp.tool()
def add_comment(
    issue_id_or_key: str,
    body: str,
    visibility_type: Optional[str] = None,
    visibility_value: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add a comment to a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        body: The comment text (plain text, converted to ADF internally).
        visibility_type: Restrict visibility by 'role' or 'group'.
        visibility_value: The role or group name for visibility restriction.
    """
    payload: Dict[str, Any] = {"body": _adf_body(body)}
    if visibility_type and visibility_value:
        payload["visibility"] = {"type": visibility_type, "value": visibility_value}
    return jira_post(f"/issue/{issue_id_or_key}/comment", json=payload)


@mcp.tool()
def update_comment(
    issue_id_or_key: str,
    comment_id: str,
    body: str,
    visibility_type: Optional[str] = None,
    visibility_value: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update an existing comment on a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        comment_id: The comment ID.
        body: The new comment text (plain text).
        visibility_type: Restrict visibility by 'role' or 'group'.
        visibility_value: The role or group name for visibility restriction.
    """
    payload: Dict[str, Any] = {"body": _adf_body(body)}
    if visibility_type and visibility_value:
        payload["visibility"] = {"type": visibility_type, "value": visibility_value}
    return jira_put(f"/issue/{issue_id_or_key}/comment/{comment_id}", json=payload)


@mcp.tool()
def delete_comment(issue_id_or_key: str, comment_id: str) -> Dict[str, Any]:
    """
    Delete a comment from a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        comment_id: The comment ID.
    """
    return jira_delete(f"/issue/{issue_id_or_key}/comment/{comment_id}")
