from typing import Any, Dict, List, Optional

from ._client import get_client


def list_views(
    page: Optional[int] = None,
    per_page: Optional[int] = None,
    access: Optional[str] = None,
    active: Optional[bool] = None,
    group_id: Optional[int] = None,
    sort: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/views"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    if access is not None:
        params["access"] = access
    if active is not None:
        params["active"] = str(active).lower()
    if group_id is not None:
        params["group_id"] = group_id
    if sort is not None:
        params["sort"] = sort
    if sort_by is not None:
        params["sort_by"] = sort_by
    if sort_order is not None:
        params["sort_order"] = sort_order
    return client.request("GET", f"{client.base_support}/views", params=params)  # type: ignore


def list_active_views() -> Dict[str, Any]:
    """GET /api/v2/views/active"""
    client = get_client()
    return client.request("GET", f"{client.base_support}/views/active")  # type: ignore


def show_view(view_id: int) -> Dict[str, Any]:
    """GET /api/v2/views/{view_id}"""
    client = get_client()
    return client.request("GET", f"{client.base_support}/views/{view_id}")  # type: ignore


def show_many_views(ids: List[int], active: Optional[bool] = None) -> Dict[str, Any]:
    """GET /api/v2/views/show_many?ids=..."""
    client = get_client()
    params: Dict[str, Any] = {"ids": ",".join(str(i) for i in ids)}
    if active is not None:
        params["active"] = str(active).lower()
    return client.request("GET", f"{client.base_support}/views/show_many", params=params)  # type: ignore


def execute_view(view_id: int, page: Optional[int] = None, per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v2/views/{view_id}/execute"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request("GET", f"{client.base_support}/views/{view_id}/execute", params=params)  # type: ignore


def list_tickets_from_view(view_id: int, page: Optional[int] = None, per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v2/views/{view_id}/tickets"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request("GET", f"{client.base_support}/views/{view_id}/tickets", params=params)  # type: ignore
