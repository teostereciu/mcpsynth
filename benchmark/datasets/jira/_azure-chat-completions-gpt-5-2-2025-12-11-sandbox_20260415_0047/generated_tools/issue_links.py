from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_create_issue_link(
    inward_issue_key: str,
    outward_issue_key: str,
    link_type_name: str,
    comment: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create an issue link.

    POST /rest/api/3/issueLink

    Args:
        inward_issue_key: The inward issue key.
        outward_issue_key: The outward issue key.
        link_type_name: Link type name (e.g. "Blocks", "Duplicate").
        comment: Optional comment object (with body/visibility).
    """

    client = JiraClient()
    payload: Dict[str, Any] = {
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key},
        "type": {"name": link_type_name},
    }
    if comment is not None:
        payload["comment"] = comment
    return client.request("POST", "/issueLink", json=payload)


@mcp.tool()
def jira_get_issue_link(link_id: str) -> Dict[str, Any]:
    """Get an issue link.

    GET /rest/api/3/issueLink/{linkId}
    """

    client = JiraClient()
    return client.request("GET", f"/issueLink/{link_id}")


@mcp.tool()
def jira_delete_issue_link(link_id: str) -> Dict[str, Any]:
    """Delete an issue link.

    DEL /rest/api/3/issueLink/{linkId}
    """

    client = JiraClient()
    return client.request("DELETE", f"/issueLink/{link_id}")
