from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def priorities_get_all() -> Any:
    """GET /priority - Get priorities."""
    client = JiraClient()
    return client.request("GET", "/priority")


def priority_get(priority_id: str) -> Dict[str, Any]:
    """GET /priority/{id} - Get priority."""
    client = JiraClient()
    return client.request("GET", f"/priority/{priority_id}")  # type: ignore[return-value]


def priority_search(start_at: Optional[int] = None, max_results: Optional[int] = None, ids: Optional[List[str]] = None, project_ids: Optional[List[str]] = None, priority_name: Optional[str] = None, only_default: Optional[bool] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /priority/search - Search priorities."""
    client = JiraClient()
    params = clean_params({"startAt": start_at, "maxResults": max_results, "id": ids, "projectId": project_ids, "priorityName": priority_name, "onlyDefault": only_default, "expand": expand})
    return client.request("GET", "/priority/search", params=params)  # type: ignore[return-value]


def priority_create(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /priority - Create priority."""
    client = JiraClient()
    return client.request("POST", "/priority", json_body=payload)  # type: ignore[return-value]


def priority_update(priority_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /priority/{id} - Update priority."""
    client = JiraClient()
    return client.request("PUT", f"/priority/{priority_id}", json_body=payload)  # type: ignore[return-value]


def priority_set_default(priority_id: str) -> Dict[str, Any]:
    """PUT /priority/default - Set default priority."""
    client = JiraClient()
    return client.request("PUT", "/priority/default", json_body={"id": priority_id})  # type: ignore[return-value]


def priority_move(ids: List[str], after: Optional[str] = None, position: Optional[str] = None) -> Dict[str, Any]:
    """PUT /priority/move - Move priorities."""
    client = JiraClient()
    body: Dict[str, Any] = {"ids": ids}
    if after is not None:
        body["after"] = after
    if position is not None:
        body["position"] = position
    return client.request("PUT", "/priority/move", json_body=body)  # type: ignore[return-value]


def priority_delete(priority_id: str) -> Dict[str, Any]:
    """DELETE /priority/{id} - Delete priority (async, returns task)."""
    client = JiraClient()
    return client.request("DELETE", f"/priority/{priority_id}")  # type: ignore[return-value]
