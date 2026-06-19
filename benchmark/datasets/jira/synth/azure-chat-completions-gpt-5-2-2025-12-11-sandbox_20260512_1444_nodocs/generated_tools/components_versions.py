from typing import Any, Dict, Optional

from jira_client import JiraClient


def create_component(client: JiraClient, project_id: str, name: str, description: Optional[str] = None, lead_account_id: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"projectId": project_id, "name": name}
    if description is not None:
        payload["description"] = description
    if lead_account_id is not None:
        payload["leadAccountId"] = lead_account_id
    return client.request("POST", "/component", json=payload)


def get_component(client: JiraClient, component_id: str) -> Any:
    return client.request("GET", f"/component/{component_id}")


def update_component(client: JiraClient, component_id: str, updates: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/component/{component_id}", json=updates)


def delete_component(client: JiraClient, component_id: str) -> Any:
    return client.request("DELETE", f"/component/{component_id}")


def create_version(client: JiraClient, project_id: str, name: str, description: Optional[str] = None, released: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"projectId": project_id, "name": name}
    if description is not None:
        payload["description"] = description
    if released is not None:
        payload["released"] = released
    return client.request("POST", "/version", json=payload)


def get_version(client: JiraClient, version_id: str) -> Any:
    return client.request("GET", f"/version/{version_id}")


def update_version(client: JiraClient, version_id: str, updates: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/version/{version_id}", json=updates)


def delete_version(client: JiraClient, version_id: str, move_fix_issues_to: Optional[str] = None, move_affected_issues_to: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if move_fix_issues_to is not None:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to is not None:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    return client.request("DELETE", f"/version/{version_id}", params=params)
