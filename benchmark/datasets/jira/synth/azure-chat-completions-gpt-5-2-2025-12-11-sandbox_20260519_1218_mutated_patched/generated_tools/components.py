from typing import Any, Dict, List, Optional

from ._client import JiraClient


def find_components(
    client: JiraClient,
    *,
    project_ids_or_keys: Optional[List[str]] = None,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    order_by: Optional[str] = None,
    query: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if project_ids_or_keys is not None:
        params["projectIdsOrKeys"] = project_ids_or_keys
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if order_by is not None:
        params["orderBy"] = order_by
    if query is not None:
        params["query"] = query
    return client.request("GET", "/component", params=params or None)


def create_component(client: JiraClient, component: Dict[str, Any]) -> Any:
    return client.request("POST", "/component", json=component)


def get_component(client: JiraClient, component_id: str) -> Any:
    return client.request("GET", f"/component/{component_id}")


def update_component(client: JiraClient, component_id: str, component: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/component/{component_id}", json=component)


def delete_component(client: JiraClient, component_id: str, *, move_issues_to: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if move_issues_to is not None:
        params["moveIssuesTo"] = move_issues_to
    return client.request("DELETE", f"/component/{component_id}", params=params or None)


def get_component_related_issue_counts(client: JiraClient, component_id: str) -> Any:
    return client.request("GET", f"/component/{component_id}/relatedIssueCounts")


def get_project_components(client: JiraClient, project_id_or_key: str) -> Any:
    return client.request("GET", f"/project/{project_id_or_key}/component")
