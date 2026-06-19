from typing import Any, Dict, List, Optional

from ._client import JiraClient


def list_resolutions(client: JiraClient) -> Any:
    return client.request("GET", "/resolution")


def get_resolution(client: JiraClient, resolution_id: str) -> Any:
    return client.request("GET", f"/resolution/{resolution_id}")


def search_resolutions(
    client: JiraClient,
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    ids: Optional[List[str]] = None,
    only_default: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if ids is not None:
        params["id"] = ids
    if only_default is not None:
        params["onlyDefault"] = str(only_default).lower()
    return client.request("GET", "/resolution/search", params=params or None)


def create_resolution(client: JiraClient, resolution: Dict[str, Any]) -> Any:
    return client.request("POST", "/resolution", json=resolution)


def update_resolution(client: JiraClient, resolution_id: str, resolution: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/resolution/{resolution_id}", json=resolution)


def delete_resolution(client: JiraClient, resolution_id: str, *, replace_with: str) -> Any:
    return client.request("DELETE", f"/resolution/{resolution_id}", params={"replaceWith": replace_with})


def set_default_resolution(client: JiraClient, resolution_id: str) -> Any:
    return client.request("PUT", "/resolution/default", json={"id": resolution_id})


def move_resolutions(client: JiraClient, ids: List[str], *, after: Optional[str] = None, position: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"ids": ids}
    if after is not None:
        body["after"] = after
    if position is not None:
        body["position"] = position
    return client.request("PUT", "/resolution/move", json=body)
