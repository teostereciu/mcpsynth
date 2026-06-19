from typing import Any, Dict, List, Optional

from ._client import JiraClient


def list_priorities(client: JiraClient) -> Any:
    return client.request("GET", "/priority")


def get_priority(client: JiraClient, priority_id: str) -> Any:
    return client.request("GET", f"/priority/{priority_id}")


def search_priorities(
    client: JiraClient,
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    ids: Optional[List[str]] = None,
    project_ids: Optional[List[str]] = None,
    priority_name: Optional[str] = None,
    only_default: Optional[bool] = None,
    expand: Optional[str] = None,
) -> Any:
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


def create_priority(client: JiraClient, priority: Dict[str, Any]) -> Any:
    return client.request("POST", "/priority", json=priority)


def update_priority(client: JiraClient, priority_id: str, priority: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/priority/{priority_id}", json=priority)


def delete_priority(client: JiraClient, priority_id: str) -> Any:
    return client.request("DELETE", f"/priority/{priority_id}")


def set_default_priority(client: JiraClient, priority_id: str) -> Any:
    return client.request("PUT", "/priority/default", json={"id": priority_id})


def move_priorities(client: JiraClient, ids: List[str], *, after: Optional[str] = None, position: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"ids": ids}
    if after is not None:
        body["after"] = after
    if position is not None:
        body["position"] = position
    return client.request("PUT", "/priority/move", json=body)
