from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def list_projects(*, expand: Optional[str] = None, recent: Optional[int] = None, properties: Optional[List[str]] = None) -> Any:
    """GET /rest/api/3/project (deprecated in docs but useful)"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if recent is not None:
        params["recent"] = recent
    if properties is not None:
        params["properties"] = properties
    return client.request("GET", "/project", params=params or None)


def search_projects(
    *,
    startAt: int = 0,
    maxResults: int = 50,
    orderBy: Optional[str] = None,
    ids: Optional[List[int]] = None,
    keys: Optional[List[str]] = None,
    query: Optional[str] = None,
    typeKey: Optional[str] = None,
    categoryId: Optional[int] = None,
    action: Optional[str] = None,
    expand: Optional[str] = None,
) -> Any:
    """GET /rest/api/3/project/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": startAt, "maxResults": maxResults}
    if orderBy is not None:
        params["orderBy"] = orderBy
    if ids is not None:
        params["id"] = ids
    if keys is not None:
        params["keys"] = keys
    if query is not None:
        params["query"] = query
    if typeKey is not None:
        params["typeKey"] = typeKey
    if categoryId is not None:
        params["categoryId"] = categoryId
    if action is not None:
        params["action"] = action
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/project/search", params=params)


def get_project(projectIdOrKey: str, *, expand: Optional[str] = None, properties: Optional[List[str]] = None) -> Any:
    """GET /rest/api/3/project/{projectIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = properties
    return client.request("GET", f"/project/{projectIdOrKey}", params=params or None)


def create_project(project: Dict[str, Any]) -> Any:
    """POST /rest/api/3/project

    Provide request body as per Jira create project.
    """
    client = JiraClient()
    return client.request("POST", "/project", json_body=project)


def update_project(projectIdOrKey: str, project: Dict[str, Any]) -> Any:
    """PUT /rest/api/3/project/{projectIdOrKey}"""
    client = JiraClient()
    return client.request("PUT", f"/project/{projectIdOrKey}", json_body=project)


def delete_project(projectIdOrKey: str, *, enableUndo: Optional[bool] = None) -> Any:
    """DEL /rest/api/3/project/{projectIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if enableUndo is not None:
        params["enableUndo"] = str(enableUndo).lower()
    return client.request("DELETE", f"/project/{projectIdOrKey}", params=params or None)
