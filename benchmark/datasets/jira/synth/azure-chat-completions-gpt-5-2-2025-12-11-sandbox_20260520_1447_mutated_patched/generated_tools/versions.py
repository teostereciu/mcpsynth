from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def list_project_versions(projectIdOrKey: str, expand: Optional[str] = None):
    """GET /project/{projectIdOrKey}/versions"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/project/{projectIdOrKey}/versions", params=params or None)


def list_project_versions_paginated(projectIdOrKey: str, start_index: int = 0, page_size: int = 50, orderBy: Optional[str] = None, query: Optional[str] = None, status: Optional[str] = None, expand: Optional[str] = None):
    """GET /project/{projectIdOrKey}/version"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_index, "maxResults": page_size}
    if orderBy is not None:
        params["orderBy"] = orderBy
    if query is not None:
        params["query"] = query
    if status is not None:
        params["status"] = status
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/project/{projectIdOrKey}/version", params=params)


def create_version(payload: Dict[str, Any]):
    """POST /version"""
    client = JiraClient()
    return client.request("POST", "/version", json=payload)


def get_version(id: str, expand: Optional[str] = None):
    """GET /version/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/version/{id}", params=params or None)


def update_version(id: str, payload: Dict[str, Any]):
    """PUT /version/{id}"""
    client = JiraClient()
    return client.request("PUT", f"/version/{id}", json=payload)
