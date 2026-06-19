from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def resolutions_get_all() -> Any:
    """GET /resolution - Get resolutions."""
    client = JiraClient()
    return client.request("GET", "/resolution")


def resolution_get(resolution_id: str) -> Dict[str, Any]:
    """GET /resolution/{id} - Get resolution."""
    client = JiraClient()
    return client.request("GET", f"/resolution/{resolution_id}")  # type: ignore[return-value]


def resolution_search(start_at: Optional[int] = None, max_results: Optional[int] = None, ids: Optional[List[str]] = None, only_default: Optional[bool] = None) -> Dict[str, Any]:
    """GET /resolution/search - Search resolutions."""
    client = JiraClient()
    params = clean_params({"startAt": start_at, "maxResults": max_results, "id": ids, "onlyDefault": only_default})
    return client.request("GET", "/resolution/search", params=params)  # type: ignore[return-value]


def resolution_create(name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """POST /resolution - Create resolution."""
    client = JiraClient()
    body: Dict[str, Any] = {"name": name}
    if description is not None:
        body["description"] = description
    return client.request("POST", "/resolution", json_body=body)  # type: ignore[return-value]


def resolution_update(resolution_id: str, name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """PUT /resolution/{id} - Update resolution."""
    client = JiraClient()
    body: Dict[str, Any] = {"name": name}
    if description is not None:
        body["description"] = description
    return client.request("PUT", f"/resolution/{resolution_id}", json_body=body)  # type: ignore[return-value]


def resolution_set_default(resolution_id: str) -> Dict[str, Any]:
    """PUT /resolution/default - Set default resolution."""
    client = JiraClient()
    return client.request("PUT", "/resolution/default", json_body={"id": resolution_id})  # type: ignore[return-value]


def resolution_move(ids: List[str], after: Optional[str] = None, position: Optional[str] = None) -> Dict[str, Any]:
    """PUT /resolution/move - Move resolutions."""
    client = JiraClient()
    body: Dict[str, Any] = {"ids": ids}
    if after is not None:
        body["after"] = after
    if position is not None:
        body["position"] = position
    return client.request("PUT", "/resolution/move", json_body=body)  # type: ignore[return-value]


def resolution_delete(resolution_id: str, replace_with: str) -> Dict[str, Any]:
    """DELETE /resolution/{id} - Delete resolution (async)."""
    client = JiraClient()
    params = clean_params({"replaceWith": replace_with})
    return client.request("DELETE", f"/resolution/{resolution_id}", params=params)  # type: ignore[return-value]
