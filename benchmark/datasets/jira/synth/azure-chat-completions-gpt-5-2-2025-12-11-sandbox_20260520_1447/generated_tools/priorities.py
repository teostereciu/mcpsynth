from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def get_priorities() -> Union[Dict[str, Any], list, str]:
    """GET /priority"""
    client = JiraClient()
    return client.request("GET", "/priority")


def get_priority(priority_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /priority/{id}"""
    client = JiraClient()
    return client.request("GET", f"/priority/{priority_id}")


def search_priorities(start_at: Optional[int] = None, max_results: Optional[int] = None, ids: Optional[List[str]] = None, project_ids: Optional[List[str]] = None, priority_name: Optional[str] = None, only_default: Optional[bool] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /priority/search"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
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
    return client.request("GET", "/priority/search", params=params or None)


def create_priority(name: str, status_color: str, description: Optional[str] = None, avatar_id: Optional[int] = None, icon_url: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """POST /priority"""
    client = JiraClient()
    body: Dict[str, Any] = {"name": name, "statusColor": status_color}
    if description is not None:
        body["description"] = description
    if avatar_id is not None:
        body["avatarId"] = avatar_id
    if icon_url is not None:
        body["iconUrl"] = icon_url
    return client.request("POST", "/priority", json=body)


def update_priority(priority_id: str, name: Optional[str] = None, status_color: Optional[str] = None, description: Optional[str] = None, avatar_id: Optional[int] = None, icon_url: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """PUT /priority/{id}"""
    client = JiraClient()
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if status_color is not None:
        body["statusColor"] = status_color
    if description is not None:
        body["description"] = description
    if avatar_id is not None:
        body["avatarId"] = avatar_id
    if icon_url is not None:
        body["iconUrl"] = icon_url
    return client.request("PUT", f"/priority/{priority_id}", json=body)


def set_default_priority(priority_id: str) -> Union[Dict[str, Any], list, str]:
    """PUT /priority/default"""
    client = JiraClient()
    return client.request("PUT", "/priority/default", json={"id": priority_id})


def move_priorities(ids: List[str], position: Optional[str] = None, after: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """PUT /priority/move"""
    client = JiraClient()
    body: Dict[str, Any] = {"ids": ids}
    if position is not None:
        body["position"] = position
    if after is not None:
        body["after"] = after
    return client.request("PUT", "/priority/move", json=body)


def delete_priority(priority_id: str) -> Union[Dict[str, Any], list, str]:
    """DELETE /priority/{id} (async; Jira returns 303 with task)"""
    client = JiraClient()
    return client.request("DELETE", f"/priority/{priority_id}")
