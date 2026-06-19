from typing import Any, Dict, Optional

from .jira_client import JiraClient


def get_project_versions_paginated(project_id_or_key: str, start_at: int = 0, max_results: int = 50,
                                   order_by: Optional[str] = None, query: Optional[str] = None,
                                   status: Optional[str] = None, expand: Optional[str] = None) -> Any:
    """GET /project/{projectIdOrKey}/version"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if order_by is not None:
        params["orderBy"] = order_by
    if query is not None:
        params["query"] = query
    if status is not None:
        params["status"] = status
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", f"/project/{project_id_or_key}/version", params=params)


def get_project_versions(project_id_or_key: str, expand: Optional[str] = None) -> Any:
    """GET /project/{projectIdOrKey}/versions"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", f"/project/{project_id_or_key}/versions", params=params or None)


def create_version(payload: Dict[str, Any]) -> Any:
    """POST /version"""
    return JiraClient().request("POST", "/version", json_body=payload)


def get_version(version_id: str, expand: Optional[str] = None) -> Any:
    """GET /version/{id}"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", f"/version/{version_id}", params=params or None)


def update_version(version_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /version/{id}"""
    return JiraClient().request("PUT", f"/version/{version_id}", json_body=payload)


def delete_version(version_id: str, move_fix_issues_to: Optional[str] = None,
                   move_affected_issues_to: Optional[str] = None) -> Any:
    """DELETE /version/{id} (Deprecated in docs but still useful)"""
    params: Dict[str, Any] = {}
    if move_fix_issues_to is not None:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to is not None:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    return JiraClient().request("DELETE", f"/version/{version_id}", params=params or None)


def merge_versions(version_id: str, move_issues_to: str) -> Any:
    """PUT /version/{id}/mergeto/{moveIssuesTo}"""
    return JiraClient().request("PUT", f"/version/{version_id}/mergeto/{move_issues_to}")


def move_version(version_id: str, after: Optional[str] = None, position: Optional[str] = None) -> Any:
    """POST /version/{id}/move"""
    body: Dict[str, Any] = {}
    if after is not None:
        body["after"] = after
    if position is not None:
        body["position"] = position
    return JiraClient().request("POST", f"/version/{version_id}/move", json_body=body)
