from typing import Any, Dict, Optional

from .http import request_json


def list_tags(
    workspaceId: str,
    name: Optional[str] = None,
    strict_name_search: Optional[bool] = None,
    excluded_ids: Optional[str] = None,
    sort_column: Optional[str] = None,
    sort_order: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    archived: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if strict_name_search is not None:
        params["strict-name-search"] = str(strict_name_search).lower()
    if excluded_ids is not None:
        parts = [x.strip() for x in excluded_ids.split(",") if x.strip()]
        params["excluded-ids"] = parts if len(parts) > 1 else excluded_ids
    if sort_column is not None:
        params["sort-column"] = sort_column
    if sort_order is not None:
        params["sort-order"] = sort_order
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    if archived is not None:
        params["archived"] = str(archived).lower()
    return request_json("GET", f"/workspaces/{workspaceId}/tags", params=params or None)


def create_tag(workspaceId: str, name: str) -> Any:
    return request_json("POST", f"/workspaces/{workspaceId}/tags", json={"name": name})


def delete_tag(workspaceId: str, id: str) -> Any:
    return request_json("DELETE", f"/workspaces/{workspaceId}/tags/{id}")


def get_tag(workspaceId: str, id: str) -> Any:
    return request_json("GET", f"/workspaces/{workspaceId}/tags/{id}")


def update_tag(workspaceId: str, id: str, name: Optional[str] = None, archived: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if archived is not None:
        body["archived"] = archived
    return request_json("PUT", f"/workspaces/{workspaceId}/tags/{id}", json=body)
