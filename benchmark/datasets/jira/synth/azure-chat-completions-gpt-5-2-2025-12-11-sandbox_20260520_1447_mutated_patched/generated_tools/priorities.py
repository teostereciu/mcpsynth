from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def list_priorities():
    """GET /priority"""
    client = JiraClient()
    return client.request("GET", "/priority")


def get_priority(id: str):
    """GET /priority/{id}"""
    client = JiraClient()
    return client.request("GET", f"/priority/{id}")


def search_priorities(start_index: int = 0, page_size: int = 50, id: Optional[List[str]] = None, projectId: Optional[List[str]] = None, priorityName: Optional[str] = None, onlyDefault: Optional[bool] = None, expand: Optional[str] = None):
    """GET /priority/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_index, "maxResults": page_size}
    if id is not None:
        params["id"] = id
    if projectId is not None:
        params["projectId"] = projectId
    if priorityName is not None:
        params["priorityName"] = priorityName
    if onlyDefault is not None:
        params["onlyDefault"] = str(onlyDefault).lower()
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/priority/search", params=params)
