from typing import Any, Dict, Optional

from .jira_client import JiraClient


def list_issue_types():
    """GET /issuetype"""
    client = JiraClient()
    return client.request("GET", "/issuetype")


def get_issue_type(id: str):
    """GET /issuetype/{id}"""
    client = JiraClient()
    return client.request("GET", f"/issuetype/{id}")


def get_issue_types_for_project(projectId: int, level: Optional[int] = None):
    """GET /issuetype/project"""
    client = JiraClient()
    params: Dict[str, Any] = {"projectId": projectId}
    if level is not None:
        params["level"] = level
    return client.request("GET", "/issuetype/project", params=params)


def get_alternative_issue_types(id: str):
    """GET /issuetype/{id}/alternatives"""
    client = JiraClient()
    return client.request("GET", f"/issuetype/{id}/alternatives")
