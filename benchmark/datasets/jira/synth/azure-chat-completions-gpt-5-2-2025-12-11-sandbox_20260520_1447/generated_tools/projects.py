from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def get_all_projects(expand: Optional[str] = None, recent: Optional[int] = None, properties: Optional[List[str]] = None) -> Union[Dict[str, Any], list, str]:
    """GET /project (Deprecated in docs; still useful)"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if recent is not None:
        params["recent"] = recent
    if properties is not None:
        params["properties"] = ",".join(properties)
    return client.request("GET", "/project", params=params or None)


def create_project(project: Dict[str, Any]) -> Union[Dict[str, Any], list, str]:
    """POST /project"""
    client = JiraClient()
    return client.request("POST", "/project", json=project)


def get_recent_projects(expand: Optional[str] = None, properties: Optional[List[str]] = None) -> Union[Dict[str, Any], list, str]:
    """GET /project/recent"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = properties
    return client.request("GET", "/project/recent", params=params or None)


def search_projects(start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, ids: Optional[List[int]] = None, keys: Optional[List[str]] = None, query: Optional[str] = None, type_key: Optional[str] = None, category_id: Optional[int] = None, action: Optional[str] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /project/search"""
    client = JiraClient()
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


def get_project(project_id_or_key: str, expand: Optional[str] = None, properties: Optional[List[str]] = None) -> Union[Dict[str, Any], list, str]:
    """GET /project/{projectIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = ",".join(properties)
    return client.request("GET", f"/project/{project_id_or_key}", params=params or None)


def update_project(project_id_or_key: str, project: Dict[str, Any]) -> Union[Dict[str, Any], list, str]:
    """PUT /project/{projectIdOrKey}"""
    client = JiraClient()
    return client.request("PUT", f"/project/{project_id_or_key}", json=project)


def delete_project(project_id_or_key: str, enable_undo: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """DELETE /project/{projectIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if enable_undo is not None:
        params["enableUndo"] = str(enable_undo).lower()
    return client.request("DELETE", f"/project/{project_id_or_key}", params=params or None)


def get_project_statuses(project_id_or_key: str) -> Union[Dict[str, Any], list, str]:
    """GET /project/{projectIdOrKey}/statuses"""
    client = JiraClient()
    return client.request("GET", f"/project/{project_id_or_key}/statuses")
