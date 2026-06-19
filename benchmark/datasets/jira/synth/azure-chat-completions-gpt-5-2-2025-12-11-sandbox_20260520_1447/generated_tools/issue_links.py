from typing import Any, Dict, Optional, Union

from .http_client import JiraClient


def create_issue_link(inward_issue: Dict[str, Any], outward_issue: Dict[str, Any], link_type: Dict[str, Any], comment: Optional[Dict[str, Any]] = None) -> Union[Dict[str, Any], list, str]:
    """POST /issueLink"""
    client = JiraClient()
    body: Dict[str, Any] = {"inwardIssue": inward_issue, "outwardIssue": outward_issue, "type": link_type}
    if comment is not None:
        body["comment"] = comment
    return client.request("POST", "/issueLink", json=body)


def get_issue_link(link_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /issueLink/{linkId}"""
    client = JiraClient()
    return client.request("GET", f"/issueLink/{link_id}")


def delete_issue_link(link_id: str) -> Union[Dict[str, Any], list, str]:
    """DELETE /issueLink/{linkId}"""
    client = JiraClient()
    return client.request("DELETE", f"/issueLink/{link_id}")
