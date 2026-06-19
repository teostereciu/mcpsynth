from typing import Any, Dict, Optional

from generated_tools.jira_client import jira_client


def create_component(project_id_or_key: str, name: str, description: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"project": project_id_or_key, "name": name}
    if description is not None:
        payload["description"] = description
    return jira_client.request("POST", "/component", json_body=payload)


def get_component(component_id: str) -> Any:
    return jira_client.request("GET", f"/component/{component_id}")


def update_component(component_id: str, updates: Dict[str, Any]) -> Any:
    return jira_client.request("PUT", f"/component/{component_id}", json_body=updates)


def delete_component(component_id: str) -> Any:
    return jira_client.request("DELETE", f"/component/{component_id}")


def create_version(project_id: str, name: str, description: Optional[str] = None, released: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"projectId": project_id, "name": name}
    if description is not None:
        payload["description"] = description
    if released is not None:
        payload["released"] = released
    return jira_client.request("POST", "/version", json_body=payload)


def get_version(version_id: str) -> Any:
    return jira_client.request("GET", f"/version/{version_id}")


def update_version(version_id: str, updates: Dict[str, Any]) -> Any:
    return jira_client.request("PUT", f"/version/{version_id}", json_body=updates)


def delete_version(version_id: str) -> Any:
    return jira_client.request("DELETE", f"/version/{version_id}")
