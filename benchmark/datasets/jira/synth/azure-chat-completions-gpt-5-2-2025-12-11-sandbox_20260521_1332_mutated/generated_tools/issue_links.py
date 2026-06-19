from typing import Any, Dict

from .jira_client import JiraClient


def create_issue_link(link: Dict[str, Any]) -> Any:
    """POST /rest/api/3/issueLink

    Provide body with inwardIssue/outwardIssue/type and optional comment.
    """
    client = JiraClient()
    return client.request("POST", "/issueLink", json_body=link)


def get_issue_link(linkId: str) -> Any:
    """GET /rest/api/3/issueLink/{linkId}"""
    client = JiraClient()
    return client.request("GET", f"/issueLink/{linkId}")


def delete_issue_link(linkId: str) -> Any:
    """DEL /rest/api/3/issueLink/{linkId}"""
    client = JiraClient()
    return client.request("DELETE", f"/issueLink/{linkId}")
