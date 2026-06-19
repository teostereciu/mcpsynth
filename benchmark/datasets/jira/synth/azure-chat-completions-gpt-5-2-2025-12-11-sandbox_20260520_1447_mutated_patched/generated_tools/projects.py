from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def list_projects(expand: Optional[str] = None, recent: Optional[int] = None, properties: Optional[List[str]] = None):
    """GET /project (deprecated in docs but useful)"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if recent is not None:
        params["recent"] = recent
    if properties is not None:
        params["properties"] = properties
    return client.request("GET", "/project", params=params or None)


def search_projects(start_index: int = 0, page_size: int = 50, orderBy: Optional[str] = None, query: Optional[str] = None, keys: Optional[List[str]] = None, id: Optional[List[int]] = None, typeKey: Optional[str] = None, categoryId: Optional[int] = None, action: Optional[str] = None, expand: Optional[str] = None):
    """GET /project/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_index, "maxResults": page_size}
    if orderBy is not None:
        params["orderBy"] = orderBy
    if query is not None:
        params["query"] = query
    if keys is not None:
        params["keys"] = keys
    if id is not None:
        params["id"] = id
    if typeKey is not None:
        params["typeKey"] = typeKey
    if categoryId is not None:
        params["categoryId"] = categoryId
    if action is not None:
        params["action"] = action
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/project/search", params=params)


def get_project(projectIdOrKey: str, expand: Optional[str] = None, properties: Optional[List[str]] = None):
    """GET /project/{projectIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = properties
    return client.request("GET", f"/project/{projectIdOrKey}", params=params or None)


def create_project(payload: Dict[str, Any]):
    """POST /project"""
    client = JiraClient()
    return client.request("POST", "/project", json=payload)


def update_project(projectIdOrKey: str, payload: Dict[str, Any]):
    """PUT /project/{projectIdOrKey}"""
    client = JiraClient()
    return client.request("PUT", f"/project/{projectIdOrKey}", json=payload)


def delete_project(projectIdOrKey: str, enableUndo: Optional[bool] = None):
    """DELETE /project/{projectIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if enableUndo is not None:
        params["enableUndo"] = str(enableUndo).lower()
    return client.request("DELETE", f"/project/{projectIdOrKey}", params=params or None)
