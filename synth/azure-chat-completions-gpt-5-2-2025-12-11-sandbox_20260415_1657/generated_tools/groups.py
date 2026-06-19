from typing import Any, Dict, Optional

from ._client import get_client


def list_groups(
    page: Optional[int] = None,
    per_page: Optional[int] = None,
    sort: Optional[str] = None,
    include: Optional[str] = None,
    exclude_deleted: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /api/v2/groups"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    if sort is not None:
        params["sort"] = sort
    if include is not None:
        params["include"] = include
    if exclude_deleted is not None:
        params["exclude_deleted"] = str(exclude_deleted).lower()
    return client.request("GET", f"{client.base_support}/groups", params=params)  # type: ignore


def list_assignable_groups(page: Optional[int] = None, per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v2/groups/assignable"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request("GET", f"{client.base_support}/groups/assignable", params=params)  # type: ignore


def show_group(group_id: int, include: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v2/groups/{group_id}"""
    client = get_client()
    params: Dict[str, Any] = {}
    if include is not None:
        params["include"] = include
    return client.request("GET", f"{client.base_support}/groups/{group_id}", params=params)  # type: ignore


def create_group(group: Dict[str, Any]) -> Dict[str, Any]:
    """POST /api/v2/groups

    Body: {"group": {...}}
    """
    client = get_client()
    return client.request("POST", f"{client.base_support}/groups", json={"group": group})  # type: ignore


def update_group(group_id: int, group: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /api/v2/groups/{group_id}

    Body: {"group": {...}}
    """
    client = get_client()
    return client.request(
        "PUT", f"{client.base_support}/groups/{group_id}", json={"group": group}
    )  # type: ignore


def delete_group(group_id: int) -> Dict[str, Any]:
    """DELETE /api/v2/groups/{group_id}"""
    client = get_client()
    return client.request("DELETE", f"{client.base_support}/groups/{group_id}")  # type: ignore


def list_user_groups(user_id: int, page: Optional[int] = None, per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v2/users/{user_id}/groups"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request("GET", f"{client.base_support}/users/{user_id}/groups", params=params)  # type: ignore
