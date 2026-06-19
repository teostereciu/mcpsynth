from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def search_components(projectIdsOrKeys: Optional[List[str]] = None, start_index: int = 0, page_size: int = 50, orderBy: Optional[str] = None, query: Optional[str] = None):
    """GET /component"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_index, "maxResults": page_size}
    if projectIdsOrKeys is not None:
        params["projectIdsOrKeys"] = projectIdsOrKeys
    if orderBy is not None:
        params["orderBy"] = orderBy
    if query is not None:
        params["query"] = query
    return client.request("GET", "/component", params=params)


def create_component(payload: Dict[str, Any]):
    """POST /component"""
    client = JiraClient()
    return client.request("POST", "/component", json=payload)


def get_component(id: str):
    """GET /component/{id}"""
    client = JiraClient()
    return client.request("GET", f"/component/{id}")


def update_component(id: str, payload: Dict[str, Any]):
    """PUT /component/{id}"""
    client = JiraClient()
    return client.request("PUT", f"/component/{id}", json=payload)


def delete_component(id: str, moveIssuesTo: Optional[str] = None):
    """DELETE /component/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if moveIssuesTo is not None:
        params["moveIssuesTo"] = moveIssuesTo
    return client.request("DELETE", f"/component/{id}", params=params or None)


def get_project_components(projectIdOrKey: str):
    """GET /project/{projectIdOrKey}/components"""
    client = JiraClient()
    return client.request("GET", f"/project/{projectIdOrKey}/components")
