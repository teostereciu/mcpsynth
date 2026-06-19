from typing import Any, Dict, Optional

from ._client import get_client


def list_macros(
    page: Optional[int] = None,
    per_page: Optional[int] = None,
    access: Optional[str] = None,
    active: Optional[bool] = None,
    category: Optional[int] = None,
    group_id: Optional[int] = None,
    include: Optional[str] = None,
    only_viewable: Optional[bool] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/macros"""
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
    if category is not None:
        params["category"] = category
    if group_id is not None:
        params["group_id"] = group_id
    if include is not None:
        params["include"] = include
    if only_viewable is not None:
        params["only_viewable"] = str(only_viewable).lower()
    if sort_by is not None:
        params["sort_by"] = sort_by
    if sort_order is not None:
        params["sort_order"] = sort_order
    return client.request("GET", f"{client.base_support}/macros", params=params)  # type: ignore


def list_active_macros(
    access: Optional[str] = None,
    category: Optional[int] = None,
    group_id: Optional[int] = None,
    include: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/macros/active"""
    client = get_client()
    params: Dict[str, Any] = {}
    if access is not None:
        params["access"] = access
    if category is not None:
        params["category"] = category
    if group_id is not None:
        params["group_id"] = group_id
    if include is not None:
        params["include"] = include
    if sort_by is not None:
        params["sort_by"] = sort_by
    if sort_order is not None:
        params["sort_order"] = sort_order
    return client.request("GET", f"{client.base_support}/macros/active", params=params)  # type: ignore


def show_macro(macro_id: int) -> Dict[str, Any]:
    """GET /api/v2/macros/{macro_id}"""
    client = get_client()
    return client.request("GET", f"{client.base_support}/macros/{macro_id}")  # type: ignore


def create_macro(macro: Dict[str, Any]) -> Dict[str, Any]:
    """POST /api/v2/macros

    Body: {"macro": {...}}
    """
    client = get_client()
    return client.request("POST", f"{client.base_support}/macros", json={"macro": macro})  # type: ignore


def update_macro(macro_id: int, macro: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /api/v2/macros/{macro_id}

    Body: {"macro": {...}}
    """
    client = get_client()
    return client.request(
        "PUT", f"{client.base_support}/macros/{macro_id}", json={"macro": macro}
    )  # type: ignore


def delete_macro(macro_id: int) -> Dict[str, Any]:
    """DELETE /api/v2/macros/{macro_id}"""
    client = get_client()
    return client.request("DELETE", f"{client.base_support}/macros/{macro_id}")  # type: ignore
