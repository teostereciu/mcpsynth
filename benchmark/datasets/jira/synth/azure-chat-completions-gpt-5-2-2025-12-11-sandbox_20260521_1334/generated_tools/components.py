from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def find_components_for_projects(project_ids_or_keys: Optional[List[str]] = None, start_at: int = 0,
                                 max_results: int = 50, order_by: Optional[str] = None,
                                 query: Optional[str] = None) -> Any:
    """GET /component"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if project_ids_or_keys is not None:
        params["projectIdsOrKeys"] = project_ids_or_keys
    if order_by is not None:
        params["orderBy"] = order_by
    if query is not None:
        params["query"] = query
    return JiraClient().request("GET", "/component", params=params)


def create_component(payload: Dict[str, Any]) -> Any:
    """POST /component"""
    return JiraClient().request("POST", "/component", json_body=payload)


def get_component(component_id: str) -> Any:
    """GET /component/{id}"""
    return JiraClient().request("GET", f"/component/{component_id}")


def update_component(component_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /component/{id}"""
    return JiraClient().request("PUT", f"/component/{component_id}", json_body=payload)


def delete_component(component_id: str, move_issues_to: Optional[str] = None) -> Any:
    """DELETE /component/{id}"""
    params: Dict[str, Any] = {}
    if move_issues_to is not None:
        params["moveIssuesTo"] = move_issues_to
    return JiraClient().request("DELETE", f"/component/{component_id}", params=params or None)


def get_component_related_issue_counts(component_id: str) -> Any:
    """GET /component/{id}/relatedIssueCounts"""
    return JiraClient().request("GET", f"/component/{component_id}/relatedIssueCounts")


def get_project_components(project_id_or_key: str) -> Any:
    """GET /project/{projectIdOrKey}/components"""
    return JiraClient().request("GET", f"/project/{project_id_or_key}/components")
