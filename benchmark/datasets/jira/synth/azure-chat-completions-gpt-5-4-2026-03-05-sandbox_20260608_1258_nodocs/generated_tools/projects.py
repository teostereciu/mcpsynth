from typing import Any, Dict, Optional

from generated_tools.jira_client import jira_client


def list_projects() -> Any:
    return jira_client.request("GET", "/project/search")


def get_project(project_id_or_key: str, expand: Optional[str] = None) -> Any:
    return jira_client.request("GET", f"/project/{project_id_or_key}", params={"expand": expand})


def create_project(
    key: str,
    name: str,
    project_type_key: str,
    project_template_key: str,
    lead_account_id: str,
    description: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "key": key,
        "name": name,
        "projectTypeKey": project_type_key,
        "projectTemplateKey": project_template_key,
        "leadAccountId": lead_account_id,
    }
    if description is not None:
        payload["description"] = description
    return jira_client.request("POST", "/project", json_body=payload)


def update_project(project_id_or_key: str, updates: Dict[str, Any]) -> Any:
    return jira_client.request("PUT", f"/project/{project_id_or_key}", json_body=updates)


def delete_project(project_id_or_key: str) -> Any:
    return jira_client.request("DELETE", f"/project/{project_id_or_key}")


def list_project_components(project_id_or_key: str) -> Any:
    return jira_client.request("GET", f"/project/{project_id_or_key}/components")


def list_project_versions(project_id_or_key: str) -> Any:
    return jira_client.request("GET", f"/project/{project_id_or_key}/versions")


def list_project_issue_types(project_id_or_key: str) -> Any:
    return jira_client.request("GET", f"/project/{project_id_or_key}/statuses")
