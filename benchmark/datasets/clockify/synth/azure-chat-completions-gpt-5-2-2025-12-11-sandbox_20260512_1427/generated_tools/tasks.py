from typing import Any, Dict, Optional

from .http import request_json


def list_tasks(
    workspaceId: str,
    projectId: str,
    name: Optional[str] = None,
    strict_name_search: Optional[bool] = None,
    is_active: Optional[bool] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    sort_column: Optional[str] = None,
    sort_order: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if strict_name_search is not None:
        params["strict-name-search"] = str(strict_name_search).lower()
    if is_active is not None:
        params["is-active"] = str(is_active).lower()
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    if sort_column is not None:
        params["sort-column"] = sort_column
    if sort_order is not None:
        params["sort-order"] = sort_order
    return request_json("GET", f"/workspaces/{workspaceId}/projects/{projectId}/tasks", params=params or None)


def create_task(workspaceId: str, projectId: str, name: str, contains_assignee: bool = True, **fields: Any) -> Any:
    params = {"contains-assignee": str(contains_assignee).lower()}
    body: Dict[str, Any] = {"name": name}
    body.update(fields)
    return request_json("POST", f"/workspaces/{workspaceId}/projects/{projectId}/tasks", params=params, json=body)


def update_task_cost_rate(workspaceId: str, projectId: str, id: str, amount: int, since: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"amount": amount}
    if since is not None:
        body["since"] = since
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/tasks/{id}/cost-rate", json=body)


def update_task_billable_rate(workspaceId: str, projectId: str, id: str, amount: int, since: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"amount": amount}
    if since is not None:
        body["since"] = since
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/tasks/{id}/billable-rate", json=body)


def delete_task(workspaceId: str, projectId: str, taskId: str) -> Any:
    return request_json("DELETE", f"/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}")


def get_task(workspaceId: str, projectId: str, taskId: str) -> Any:
    return request_json("GET", f"/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}")


def update_task(
    workspaceId: str,
    projectId: str,
    taskId: str,
    contains_assignee: bool = True,
    membership_status: Optional[str] = None,
    **fields: Any,
) -> Any:
    params: Dict[str, Any] = {"contains-assignee": str(contains_assignee).lower()}
    if membership_status is not None:
        params["membership-status"] = membership_status
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}", params=params, json=fields)
