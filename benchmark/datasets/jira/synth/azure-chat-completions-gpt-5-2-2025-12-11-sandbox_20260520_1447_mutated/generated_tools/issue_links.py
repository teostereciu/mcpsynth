from typing import Any, Dict, Optional

from .jira_client import JiraClient


def create_issue_link(inwardIssueKey: str, outwardIssueKey: str, linkTypeName: str, comment: Optional[Dict[str, Any]] = None):
    """POST /issueLink"""
    client = JiraClient()
    payload: Dict[str, Any] = {
        "inwardIssue": {"key": inwardIssueKey},
        "outwardIssue": {"key": outwardIssueKey},
        "type": {"name": linkTypeName},
    }
    if comment is not None:
        payload["comment"] = comment
    return client.request("POST", "/issueLink", json=payload)


def get_issue_link(linkId: str):
    """GET /issueLink/{linkId}"""
    client = JiraClient()
    return client.request("GET", f"/issueLink/{linkId}")


def delete_issue_link(linkId: str):
    """DELETE /issueLink/{linkId}"""
    client = JiraClient()
    return client.request("DELETE", f"/issueLink/{linkId}")
