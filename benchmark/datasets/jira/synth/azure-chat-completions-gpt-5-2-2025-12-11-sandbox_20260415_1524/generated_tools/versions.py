from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def project_versions_paginated(project_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, query: Optional[str] = None, status: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /project/{projectIdOrKey}/version - Get project versions paginated."""
    client = JiraClient()
    params = clean_params({"startAt": start_at, "maxResults": max_results, "orderBy": order_by, "query": query, "status": status, "expand": expand})
    return client.request("GET", f"/project/{project_id_or_key}/version", params=params)  # type: ignore[return-value]


def project_versions(project_id_or_key: str, expand: Optional[str] = None) -> Any:
    """GET /project/{projectIdOrKey}/versions - Get all versions (not paginated)."""
    client = JiraClient()
    params = clean_params({"expand": expand})
    return client.request("GET", f"/project/{project_id_or_key}/versions", params=params)


def version_create(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /version - Create version."""
    client = JiraClient()
    return client.request("POST", "/version", json_body=payload)  # type: ignore[return-value]


def version_get(version_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /version/{id} - Get version."""
    client = JiraClient()
    params = clean_params({"expand": expand})
    return client.request("GET", f"/version/{version_id}", params=params)  # type: ignore[return-value]


def version_update(version_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /version/{id} - Update version."""
    client = JiraClient()
    return client.request("PUT", f"/version/{version_id}", json_body=payload)  # type: ignore[return-value]


def version_delete(version_id: str, move_fix_issues_to: Optional[str] = None, move_affected_issues_to: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /version/{id} - Delete version (deprecated by Jira)."""
    client = JiraClient()
    params = clean_params({"moveFixIssuesTo": move_fix_issues_to, "moveAffectedIssuesTo": move_affected_issues_to})
    return client.request("DELETE", f"/version/{version_id}", params=params)  # type: ignore[return-value]


def version_merge(version_id: str, move_issues_to: str) -> Dict[str, Any]:
    """PUT /version/{id}/mergeto/{moveIssuesTo} - Merge versions."""
    client = JiraClient()
    return client.request("PUT", f"/version/{version_id}/mergeto/{move_issues_to}")  # type: ignore[return-value]


def version_move(version_id: str, after: Optional[str] = None, position: Optional[str] = None) -> Dict[str, Any]:
    """POST /version/{id}/move - Move version within project."""
    client = JiraClient()
    body: Dict[str, Any] = {}
    if after is not None:
        body["after"] = after
    if position is not None:
        body["position"] = position
    return client.request("POST", f"/version/{version_id}/move", json_body=body)  # type: ignore[return-value]


def version_related_issue_counts(version_id: str) -> Dict[str, Any]:
    """GET /version/{id}/relatedIssueCounts - Get issue counts."""
    client = JiraClient()
    return client.request("GET", f"/version/{version_id}/relatedIssueCounts")  # type: ignore[return-value]
