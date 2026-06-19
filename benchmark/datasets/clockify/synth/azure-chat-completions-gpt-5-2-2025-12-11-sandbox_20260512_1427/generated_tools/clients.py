from typing import Any, Dict, Optional

from .http import request_json


def list_clients(
    workspaceId: str,
    name: Optional[str] = None,
    sort_column: str = "NAME",
    sort_order: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    archived: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"sort-column": sort_column}
    if name is not None:
        params["name"] = name
    if sort_order is not None:
        params["sort-order"] = sort_order
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    if archived is not None:
        params["archived"] = archived
    return request_json("GET", f"/workspaces/{workspaceId}/clients", params=params)


def create_client(workspaceId: str, name: Optional[str] = None, address: Optional[str] = None, email: Optional[str] = None, note: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {}
    if address is not None:
        body["address"] = address
    if email is not None:
        body["email"] = email
    if name is not None:
        body["name"] = name
    if note is not None:
        body["note"] = note
    return request_json("POST", f"/workspaces/{workspaceId}/clients", json=body)


def delete_client(workspaceId: str, id: str) -> Any:
    return request_json("DELETE", f"/workspaces/{workspaceId}/clients/{id}")


def get_client(workspaceId: str, id: str) -> Any:
    return request_json("GET", f"/workspaces/{workspaceId}/clients/{id}")


def update_client(
    workspaceId: str,
    id: str,
    archive_projects: Optional[bool] = None,
    mark_tasks_as_done: Optional[bool] = None,
    **fields: Any,
) -> Any:
    params: Dict[str, Any] = {}
    if archive_projects is not None:
        params["archive-projects"] = str(archive_projects).lower()
    if mark_tasks_as_done is not None:
        params["mark-tasks-as-done"] = str(mark_tasks_as_done).lower()
    return request_json("PUT", f"/workspaces/{workspaceId}/clients/{id}", params=params or None, json=fields)
