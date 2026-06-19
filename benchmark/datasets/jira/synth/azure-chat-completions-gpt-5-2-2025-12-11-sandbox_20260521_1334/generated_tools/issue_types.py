from typing import Any, Dict, Optional

from .jira_client import JiraClient


def get_issue_types() -> Any:
    """GET /issuetype"""
    return JiraClient().request("GET", "/issuetype")


def get_issue_type(issue_type_id: str) -> Any:
    """GET /issuetype/{id}"""
    return JiraClient().request("GET", f"/issuetype/{issue_type_id}")


def create_issue_type(payload: Dict[str, Any]) -> Any:
    """POST /issuetype"""
    return JiraClient().request("POST", "/issuetype", json_body=payload)


def update_issue_type(issue_type_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /issuetype/{id}"""
    return JiraClient().request("PUT", f"/issuetype/{issue_type_id}", json_body=payload)


def delete_issue_type(issue_type_id: str, alternative_issue_type_id: Optional[str] = None) -> Any:
    """DELETE /issuetype/{id}"""
    params = {}
    if alternative_issue_type_id is not None:
        params["alternativeIssueTypeId"] = alternative_issue_type_id
    return JiraClient().request("DELETE", f"/issuetype/{issue_type_id}", params=params or None)


def get_issue_type_alternatives(issue_type_id: str) -> Any:
    """GET /issuetype/{id}/alternatives"""
    return JiraClient().request("GET", f"/issuetype/{issue_type_id}/alternatives")


def get_issue_types_for_project(project_id: int, level: Optional[int] = None) -> Any:
    """GET /issuetype/project"""
    params = {"projectId": project_id}
    if level is not None:
        params["level"] = level
    return JiraClient().request("GET", "/issuetype/project", params=params)
