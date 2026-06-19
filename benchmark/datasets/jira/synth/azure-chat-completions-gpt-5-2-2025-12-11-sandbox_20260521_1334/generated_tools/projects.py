from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def search_projects(start_at: int = 0, max_results: int = 50, order_by: Optional[str] = None,
                    ids: Optional[List[int]] = None, keys: Optional[List[str]] = None,
                    query: Optional[str] = None, type_key: Optional[str] = None,
                    category_id: Optional[int] = None, action: Optional[str] = None,
                    expand: Optional[str] = None) -> Any:
    """GET /project/search"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
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
    return JiraClient().request("GET", "/project/search", params=params)


def get_project(project_id_or_key: str, expand: Optional[str] = None, properties: Optional[List[str]] = None) -> Any:
    """GET /project/{projectIdOrKey}"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = properties
    return JiraClient().request("GET", f"/project/{project_id_or_key}", params=params or None)


def create_project(payload: Dict[str, Any]) -> Any:
    """POST /project"""
    return JiraClient().request("POST", "/project", json_body=payload)


def update_project(project_id_or_key: str, payload: Dict[str, Any]) -> Any:
    """PUT /project/{projectIdOrKey}"""
    return JiraClient().request("PUT", f"/project/{project_id_or_key}", json_body=payload)


def delete_project(project_id_or_key: str) -> Any:
    """DELETE /project/{projectIdOrKey}"""
    return JiraClient().request("DELETE", f"/project/{project_id_or_key}")


def get_recent_projects(expand: Optional[str] = None, properties: Optional[List[str]] = None) -> Any:
    """GET /project/recent"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = properties
    return JiraClient().request("GET", "/project/recent", params=params or None)
