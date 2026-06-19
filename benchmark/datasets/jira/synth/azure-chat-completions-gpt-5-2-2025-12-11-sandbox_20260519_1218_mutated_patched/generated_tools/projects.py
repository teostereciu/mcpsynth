from typing import Any, Dict, List, Optional, Union

from ._client import JiraClient


def list_projects(
    client: JiraClient,
    *,
    expand: Optional[str] = None,
    recent: Optional[int] = None,
    properties: Optional[List[str]] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if recent is not None:
        params["recent"] = recent
    if properties is not None:
        params["properties"] = properties
    return client.request("GET", "/project", params=params or None)


def search_projects(
    client: JiraClient,
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    order_by: Optional[str] = None,
    ids: Optional[List[int]] = None,
    keys: Optional[List[str]] = None,
    query: Optional[str] = None,
    type_key: Optional[str] = None,
    category_id: Optional[int] = None,
    action: Optional[str] = None,
    expand: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if order_by is not None:
        params["orderBy"] = order_by
    if ids is not None:
        params["id"] = ids
    if keys is not None:
        params["keys"] = keys
    if query is not None:
        params["query"] = query
    if type_key is not None:
        params["typeKey"] = type_key
    if category_id is not None:
        params["categoryId"] = category_id
    if action is not None:
        params["action"] = action
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/project/search", params=params or None)


def get_project(
    client: JiraClient,
    project_id_or_key: str,
    *,
    expand: Optional[str] = None,
    properties: Optional[List[str]] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = properties
    return client.request("GET", f"/project/{project_id_or_key}", params=params or None)


def create_project(client: JiraClient, project: Dict[str, Any]) -> Any:
    return client.request("POST", "/project", json=project)


def update_project(client: JiraClient, project_id_or_key: str, project: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/project/{project_id_or_key}", json=project)


def delete_project(client: JiraClient, project_id_or_key: str, *, enable_undo: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if enable_undo is not None:
        params["enableUndo"] = str(enable_undo).lower()
    return client.request("DELETE", f"/project/{project_id_or_key}", params=params or None)


def get_project_statuses(client: JiraClient, project_id_or_key: str) -> Any:
    return client.request("GET", f"/project/{project_id_or_key}/statuses")


def get_recent_projects(client: JiraClient, *, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/project/recent", params=params or None)
