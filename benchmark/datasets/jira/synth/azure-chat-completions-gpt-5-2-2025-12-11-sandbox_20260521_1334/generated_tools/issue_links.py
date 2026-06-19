from typing import Any, Dict, Optional

from .jira_client import JiraClient


def create_issue_link(type_name: str, inward_issue_key: str, outward_issue_key: str,
                      comment: Optional[Dict[str, Any]] = None) -> Any:
    """POST /issueLink"""
    body: Dict[str, Any] = {
        "type": {"name": type_name},
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key},
    }
    if comment is not None:
        body["comment"] = comment
    return JiraClient().request("POST", "/issueLink", json_body=body)


def get_issue_link(link_id: str) -> Any:
    """GET /issueLink/{linkId}"""
    return JiraClient().request("GET", f"/issueLink/{link_id}")


def delete_issue_link(link_id: str) -> Any:
    """DELETE /issueLink/{linkId}"""
    return JiraClient().request("DELETE", f"/issueLink/{link_id}")
