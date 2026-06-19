from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_priorities() -> Any:
    """GET /priority"""
    return JiraClient().request("GET", "/priority")


def get_priority(priority_id: str) -> Any:
    """GET /priority/{id}"""
    return JiraClient().request("GET", f"/priority/{priority_id}")


def search_priorities(start_at: int = 0, max_results: int = 50, ids: Optional[List[str]] = None,
                      project_ids: Optional[List[str]] = None, priority_name: Optional[str] = None,
                      only_default: Optional[bool] = None, expand: Optional[str] = None) -> Any:
    """GET /priority/search"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if ids is not None:
        params["id"] = ids
    if project_ids is not None:
        params["projectId"] = project_ids
    if priority_name is not None:
        params["priorityName"] = priority_name
    if only_default is not None:
        params["onlyDefault"] = str(only_default).lower()
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", "/priority/search", params=params)


def create_priority(payload: Dict[str, Any]) -> Any:
    """POST /priority"""
    return JiraClient().request("POST", "/priority", json_body=payload)


def update_priority(priority_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /priority/{id}"""
    return JiraClient().request("PUT", f"/priority/{priority_id}", json_body=payload)


def delete_priority(priority_id: str) -> Any:
    """DELETE /priority/{id} (async; returns task)"""
    return JiraClient().request("DELETE", f"/priority/{priority_id}")


def set_default_priority(priority_id: str) -> Any:
    """PUT /priority/default"""
    return JiraClient().request("PUT", "/priority/default", json_body={"id": priority_id})


def move_priorities(ids: List[str], after: Optional[str] = None, position: Optional[str] = None) -> Any:
    """PUT /priority/move"""
    body: Dict[str, Any] = {"ids": ids}
    if after is not None:
        body["after"] = after
    if position is not None:
        body["position"] = position
    return JiraClient().request("PUT", "/priority/move", json_body=body)
