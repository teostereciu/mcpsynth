from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def components_find(project_ids_or_keys: Optional[List[str]] = None, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, query: Optional[str] = None) -> Dict[str, Any]:
    """GET /component - Find components for projects."""
    client = JiraClient()
    params = clean_params(
        {
            "projectIdsOrKeys": project_ids_or_keys,
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "query": query,
        }
    )
    return client.request("GET", "/component", params=params)  # type: ignore[return-value]


def component_create(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /component - Create component."""
    client = JiraClient()
    return client.request("POST", "/component", json_body=payload)  # type: ignore[return-value]


def component_get(component_id: str) -> Dict[str, Any]:
    """GET /component/{id} - Get component."""
    client = JiraClient()
    return client.request("GET", f"/component/{component_id}")  # type: ignore[return-value]


def component_update(component_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /component/{id} - Update component."""
    client = JiraClient()
    return client.request("PUT", f"/component/{component_id}", json_body=payload)  # type: ignore[return-value]


def component_delete(component_id: str, move_issues_to: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /component/{id} - Delete component."""
    client = JiraClient()
    params = clean_params({"moveIssuesTo": move_issues_to})
    return client.request("DELETE", f"/component/{component_id}", params=params)  # type: ignore[return-value]


def component_related_issue_counts(component_id: str) -> Dict[str, Any]:
    """GET /component/{id}/relatedIssueCounts - Get issue counts."""
    client = JiraClient()
    return client.request("GET", f"/component/{component_id}/relatedIssueCounts")  # type: ignore[return-value]


def project_components_get(project_id_or_key: str) -> Any:
    """GET /project/{projectIdOrKey}/components - Get components for a project."""
    client = JiraClient()
    return client.request("GET", f"/project/{project_id_or_key}/components")
