from typing import Any, Dict, Optional

from ._client import JiraClient


def get_project_versions_paginated(
    client: JiraClient,
    project_id_or_key: str,
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    order_by: Optional[str] = None,
    query: Optional[str] = None,
    status: Optional[str] = None,
    expand: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if order_by is not None:
        params["orderBy"] = order_by
    if query is not None:
        params["query"] = query
    if status is not None:
        params["status"] = status
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/project/{project_id_or_key}/version", params=params or None)


def get_project_versions(client: JiraClient, project_id_or_key: str, *, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/project/{project_id_or_key}/versions", params=params or None)


def create_version(client: JiraClient, version: Dict[str, Any]) -> Any:
    return client.request("POST", "/version", json=version)


def get_version(client: JiraClient, version_id: str, *, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/version/{version_id}", params=params or None)


def update_version(client: JiraClient, version_id: str, version: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/version/{version_id}", json=version)


def delete_version(
    client: JiraClient,
    version_id: str,
    *,
    move_fix_issues_to: Optional[str] = None,
    move_affected_issues_to: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if move_fix_issues_to is not None:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to is not None:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    return client.request("DELETE", f"/version/{version_id}", params=params or None)


def merge_version(client: JiraClient, version_id: str, move_issues_to: str) -> Any:
    return client.request("PUT", f"/version/{version_id}/mergeto/{move_issues_to}")


def move_version(client: JiraClient, version_id: str, *, after: Optional[str] = None, position: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {}
    if after is not None:
        body["after"] = after
    if position is not None:
        body["position"] = position
    return client.request("POST", f"/version/{version_id}/move", json=body)


def get_version_related_issue_counts(client: JiraClient, version_id: str) -> Any:
    return client.request("GET", f"/version/{version_id}/relatedIssueCounts")


def get_version_unresolved_issue_count(client: JiraClient, version_id: str) -> Any:
    return client.request("GET", f"/version/{version_id}/unresolvedIssueCount")
