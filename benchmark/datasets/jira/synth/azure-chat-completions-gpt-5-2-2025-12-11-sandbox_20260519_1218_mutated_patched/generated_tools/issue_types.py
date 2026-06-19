from typing import Any, Dict, Optional

from ._client import JiraClient


def list_issue_types(client: JiraClient) -> Any:
    return client.request("GET", "/issuetype")


def get_issue_type(client: JiraClient, issue_type_id: str) -> Any:
    return client.request("GET", f"/issuetype/{issue_type_id}")


def create_issue_type(client: JiraClient, issue_type: Dict[str, Any]) -> Any:
    return client.request("POST", "/issuetype", json=issue_type)


def update_issue_type(client: JiraClient, issue_type_id: str, issue_type: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/issuetype/{issue_type_id}", json=issue_type)


def delete_issue_type(client: JiraClient, issue_type_id: str, *, alternative_issue_type_id: Optional[str] = None) -> Any:
    params = {}
    if alternative_issue_type_id is not None:
        params["alternativeIssueTypeId"] = alternative_issue_type_id
    return client.request("DELETE", f"/issuetype/{issue_type_id}", params=params or None)


def get_issue_type_alternatives(client: JiraClient, issue_type_id: str) -> Any:
    return client.request("GET", f"/issuetype/{issue_type_id}/alternatives")


def get_issue_types_for_project(client: JiraClient, project_id: int, *, level: Optional[int] = None) -> Any:
    params = {"projectId": project_id}
    if level is not None:
        params["level"] = level
    return client.request("GET", "/issuetype/project", params=params)
