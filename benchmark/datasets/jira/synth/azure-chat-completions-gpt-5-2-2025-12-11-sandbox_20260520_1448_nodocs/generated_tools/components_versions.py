from typing import Any, Dict, Optional

from jira_client import JiraClient


def create_component(payload: Dict[str, Any]) -> Any:
    """POST /component"""
    client = JiraClient()
    return client.request("POST", "/component", json=payload)


def get_component(component_id: str) -> Any:
    """GET /component/{id}"""
    client = JiraClient()
    return client.request("GET", f"/component/{component_id}")


def update_component(component_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /component/{id}"""
    client = JiraClient()
    return client.request("PUT", f"/component/{component_id}", json=payload)


def delete_component(component_id: str) -> Any:
    """DELETE /component/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/component/{component_id}")


def create_version(payload: Dict[str, Any]) -> Any:
    """POST /version"""
    client = JiraClient()
    return client.request("POST", "/version", json=payload)


def get_version(version_id: str, expand: Optional[str] = None) -> Any:
    """GET /version/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/version/{version_id}", params=params)


def update_version(version_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /version/{id}"""
    client = JiraClient()
    return client.request("PUT", f"/version/{version_id}", json=payload)


def delete_version(version_id: str, move_fix_issues_to: Optional[str] = None, move_affected_issues_to: Optional[str] = None) -> Any:
    """DELETE /version/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if move_fix_issues_to:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    return client.request("DELETE", f"/version/{version_id}", params=params)
