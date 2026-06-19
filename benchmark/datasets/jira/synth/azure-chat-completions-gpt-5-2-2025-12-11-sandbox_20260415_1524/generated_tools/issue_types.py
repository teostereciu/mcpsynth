from typing import Any, Dict, Optional

from .jira_client import JiraClient, clean_params


def issue_types_get_all() -> Any:
    """GET /issuetype - Get all issue types for user."""
    client = JiraClient()
    return client.request("GET", "/issuetype")


def issue_type_get(issue_type_id: str) -> Dict[str, Any]:
    """GET /issuetype/{id} - Get issue type."""
    client = JiraClient()
    return client.request("GET", f"/issuetype/{issue_type_id}")  # type: ignore[return-value]


def issue_type_create(name: str, type_: str = "standard", description: Optional[str] = None, hierarchy_level: Optional[int] = None) -> Dict[str, Any]:
    """POST /issuetype - Create issue type."""
    client = JiraClient()
    body: Dict[str, Any] = {"name": name, "type": type_}
    if description is not None:
        body["description"] = description
    if hierarchy_level is not None:
        body["hierarchyLevel"] = hierarchy_level
    return client.request("POST", "/issuetype", json_body=body)  # type: ignore[return-value]


def issue_type_update(issue_type_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /issuetype/{id} - Update issue type."""
    client = JiraClient()
    return client.request("PUT", f"/issuetype/{issue_type_id}", json_body=payload)  # type: ignore[return-value]


def issue_type_delete(issue_type_id: str, alternative_issue_type_id: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /issuetype/{id} - Delete issue type."""
    client = JiraClient()
    params = clean_params({"alternativeIssueTypeId": alternative_issue_type_id})
    return client.request("DELETE", f"/issuetype/{issue_type_id}", params=params)  # type: ignore[return-value]


def issue_type_alternatives(issue_type_id: str) -> Any:
    """GET /issuetype/{id}/alternatives - Get alternative issue types."""
    client = JiraClient()
    return client.request("GET", f"/issuetype/{issue_type_id}/alternatives")


def issue_types_for_project(project_id: int, level: Optional[int] = None) -> Any:
    """GET /issuetype/project - Get issue types for project."""
    client = JiraClient()
    params = clean_params({"projectId": project_id, "level": level})
    return client.request("GET", "/issuetype/project", params=params)
