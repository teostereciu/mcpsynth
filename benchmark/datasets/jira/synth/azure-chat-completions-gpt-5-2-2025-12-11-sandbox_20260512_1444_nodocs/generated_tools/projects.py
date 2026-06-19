from typing import Any, Dict, Optional

from jira_client import JiraClient


def list_projects(client: JiraClient, expand: Optional[str] = None, recent: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    if recent is not None:
        params["recent"] = recent
    return client.request("GET", "/project", params=params)


def get_project(client: JiraClient, project_id_or_key: str, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/project/{project_id_or_key}", params=params)


def create_project(client: JiraClient, key: str, name: str, project_type_key: str, project_template_key: str, lead_account_id: Optional[str] = None, description: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {
        "key": key,
        "name": name,
        "projectTypeKey": project_type_key,
        "projectTemplateKey": project_template_key,
    }
    if lead_account_id:
        payload["leadAccountId"] = lead_account_id
    if description:
        payload["description"] = description
    return client.request("POST", "/project", json=payload)


def update_project(client: JiraClient, project_id_or_key: str, updates: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/project/{project_id_or_key}", json=updates)


def delete_project(client: JiraClient, project_id_or_key: str) -> Any:
    return client.request("DELETE", f"/project/{project_id_or_key}")
