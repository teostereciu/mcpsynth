from typing import Any, Dict, Optional

from jira_client import JiraClient


def get_project(project_id_or_key: str, expand: Optional[str] = None) -> Any:
    """GET /project/{projectIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/project/{project_id_or_key}", params=params)


def list_projects(expand: Optional[str] = None, recent: Optional[int] = None) -> Any:
    """GET /project"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    if recent is not None:
        params["recent"] = recent
    return client.request("GET", "/project", params=params)


def create_project(payload: Dict[str, Any]) -> Any:
    """POST /project"""
    client = JiraClient()
    return client.request("POST", "/project", json=payload)


def update_project(project_id_or_key: str, payload: Dict[str, Any]) -> Any:
    """PUT /project/{projectIdOrKey}"""
    client = JiraClient()
    return client.request("PUT", f"/project/{project_id_or_key}", json=payload)


def delete_project(project_id_or_key: str) -> Any:
    """DELETE /project/{projectIdOrKey}"""
    client = JiraClient()
    return client.request("DELETE", f"/project/{project_id_or_key}")
