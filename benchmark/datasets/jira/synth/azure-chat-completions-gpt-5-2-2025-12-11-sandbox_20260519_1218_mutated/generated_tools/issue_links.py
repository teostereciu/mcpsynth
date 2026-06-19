from typing import Any, Dict, Optional

from ._client import JiraClient


def create_issue_link(
    client: JiraClient,
    *,
    inward_issue_key: str,
    outward_issue_key: str,
    link_type_name: str,
    comment: Optional[Dict[str, Any]] = None,
) -> Any:
    body: Dict[str, Any] = {
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key},
        "type": {"name": link_type_name},
    }
    if comment is not None:
        body["comment"] = comment
    return client.request("POST", "/issueLink", json=body)


def get_issue_link(client: JiraClient, link_id: str) -> Any:
    return client.request("GET", f"/issueLink/{link_id}")


def delete_issue_link(client: JiraClient, link_id: str) -> Any:
    return client.request("DELETE", f"/issueLink/{link_id}")
