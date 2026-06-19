from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def get_all_issue_types() -> Union[Dict[str, Any], list, str]:
    """GET /issuetype"""
    client = JiraClient()
    return client.request("GET", "/issuetype")


def create_issue_type(name: str, issue_type: str = "standard", description: Optional[str] = None, hierarchy_level: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """POST /issuetype"""
    client = JiraClient()
    body: Dict[str, Any] = {"name": name, "type": issue_type}
    if description is not None:
        body["description"] = description
    if hierarchy_level is not None:
        body["hierarchyLevel"] = hierarchy_level
    return client.request("POST", "/issuetype", json=body)


def get_issue_types_for_project(project_id: int, level: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /issuetype/project"""
    client = JiraClient()
    params: Dict[str, Any] = {"projectId": project_id}
    if level is not None:
        params["level"] = level
    return client.request("GET", "/issuetype/project", params=params)


def get_issue_type(issue_type_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /issuetype/{id}"""
    client = JiraClient()
    return client.request("GET", f"/issuetype/{issue_type_id}")


def update_issue_type(issue_type_id: str, name: Optional[str] = None, description: Optional[str] = None, avatar_id: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """PUT /issuetype/{id}"""
    client = JiraClient()
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if avatar_id is not None:
        body["avatarId"] = avatar_id
    return client.request("PUT", f"/issuetype/{issue_type_id}", json=body)


def delete_issue_type(issue_type_id: str, alternative_issue_type_id: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """DELETE /issuetype/{id}"""
    client = JiraClient()
    params = {"alternativeIssueTypeId": alternative_issue_type_id} if alternative_issue_type_id is not None else None
    return client.request("DELETE", f"/issuetype/{issue_type_id}", params=params)


def get_alternative_issue_types(issue_type_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /issuetype/{id}/alternatives"""
    client = JiraClient()
    return client.request("GET", f"/issuetype/{issue_type_id}/alternatives")
