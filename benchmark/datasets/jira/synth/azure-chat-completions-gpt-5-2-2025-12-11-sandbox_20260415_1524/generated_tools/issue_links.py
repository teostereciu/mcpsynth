from typing import Any, Dict, Optional

from .jira_client import JiraClient


def issue_link_create(
    inward_issue_key_or_id: str,
    outward_issue_key_or_id: str,
    link_type_name: str,
    comment: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /issueLink - Create issue link."""
    client = JiraClient()
    body: Dict[str, Any] = {
        "inwardIssue": {"key": inward_issue_key_or_id},
        "outwardIssue": {"key": outward_issue_key_or_id},
        "type": {"name": link_type_name},
    }
    if comment is not None:
        body["comment"] = comment
    return client.request("POST", "/issueLink", json_body=body)  # type: ignore[return-value]


def issue_link_get(link_id: str) -> Dict[str, Any]:
    """GET /issueLink/{linkId} - Get issue link."""
    client = JiraClient()
    return client.request("GET", f"/issueLink/{link_id}")  # type: ignore[return-value]


def issue_link_delete(link_id: str) -> Dict[str, Any]:
    """DELETE /issueLink/{linkId} - Delete issue link."""
    client = JiraClient()
    return client.request("DELETE", f"/issueLink/{link_id}")  # type: ignore[return-value]
