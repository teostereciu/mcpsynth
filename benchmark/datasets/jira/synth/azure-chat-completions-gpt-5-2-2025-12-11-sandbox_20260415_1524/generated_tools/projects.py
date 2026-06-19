from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def projects_get_all(expand: Optional[str] = None, recent: Optional[int] = None, properties: Optional[List[str]] = None) -> Any:
    """GET /project - Get all projects (deprecated by Jira, still useful)."""
    client = JiraClient()
    params = clean_params({"expand": expand, "recent": recent, "properties": ",".join(properties) if properties else None})
    return client.request("GET", "/project", params=params)


def projects_search(
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    order_by: Optional[str] = None,
    ids: Optional[List[int]] = None,
    keys: Optional[List[str]] = None,
    query: Optional[str] = None,
    type_key: Optional[str] = None,
    category_id: Optional[int] = None,
    action: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /project/search - Get projects paginated."""
    client = JiraClient()
    params = clean_params(
        {
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "id": ids,
            "keys": keys,
            "query": query,
            "typeKey": type_key,
            "categoryId": category_id,
            "action": action,
            "expand": expand,
        }
    )
    return client.request("GET", "/project/search", params=params)  # type: ignore[return-value]


def project_get(project_id_or_key: str, expand: Optional[str] = None, properties: Optional[List[str]] = None) -> Dict[str, Any]:
    """GET /project/{projectIdOrKey} - Get project."""
    client = JiraClient()
    params = clean_params({"expand": expand, "properties": ",".join(properties) if properties else None})
    return client.request("GET", f"/project/{project_id_or_key}", params=params)  # type: ignore[return-value]


def project_create(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /project - Create project.

    payload: full project create body.
    """
    client = JiraClient()
    return client.request("POST", "/project", json_body=payload)  # type: ignore[return-value]


def project_update(project_id_or_key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /project/{projectIdOrKey} - Update project."""
    client = JiraClient()
    return client.request("PUT", f"/project/{project_id_or_key}", json_body=payload)  # type: ignore[return-value]


def project_delete(project_id_or_key: str, enable_undo: Optional[bool] = None) -> Dict[str, Any]:
    """DELETE /project/{projectIdOrKey} - Delete project."""
    client = JiraClient()
    params = clean_params({"enableUndo": enable_undo})
    return client.request("DELETE", f"/project/{project_id_or_key}", params=params)  # type: ignore[return-value]


def project_statuses_get(project_id_or_key: str) -> Any:
    """GET /project/{projectIdOrKey}/statuses - Get statuses available to a project."""
    client = JiraClient()
    return client.request("GET", f"/project/{project_id_or_key}/statuses")
