from typing import Any, Dict, Optional

from ._client import get_client


def hc_list_categories(sort_by: Optional[str] = None, sort_order: Optional[str] = None, locale: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v2/help_center/categories (or locale variant)"""
    client = get_client()
    params: Dict[str, Any] = {}
    if sort_by is not None:
        params["sort_by"] = sort_by
    if sort_order is not None:
        params["sort_order"] = sort_order
    if locale:
        url = f"{client.base_help_center}/{locale}/categories"
    else:
        url = f"{client.base_help_center}/categories"
    return client.request("GET", url, params=params)  # type: ignore


def hc_show_category(category_id: int, locale: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v2/help_center/categories/{category_id} (or locale variant)"""
    client = get_client()
    if locale:
        url = f"{client.base_help_center}/{locale}/categories/{category_id}"
    else:
        url = f"{client.base_help_center}/categories/{category_id}"
    return client.request("GET", url)  # type: ignore


def hc_create_category(category: Dict[str, Any], locale: Optional[str] = None) -> Dict[str, Any]:
    """POST /api/v2/help_center/categories (or locale variant)

    Body: {"category": {...}}
    """
    client = get_client()
    if locale:
        url = f"{client.base_help_center}/{locale}/categories"
    else:
        url = f"{client.base_help_center}/categories"
    return client.request("POST", url, json={"category": category})  # type: ignore


def hc_update_category(category_id: int, category: Dict[str, Any], locale: Optional[str] = None) -> Dict[str, Any]:
    """PUT /api/v2/help_center/categories/{category_id} (or locale variant)

    Body: {"category": {...}}
    """
    client = get_client()
    if locale:
        url = f"{client.base_help_center}/{locale}/categories/{category_id}"
    else:
        url = f"{client.base_help_center}/categories/{category_id}"
    return client.request("PUT", url, json={"category": category})  # type: ignore


def hc_delete_category(category_id: int, locale: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /api/v2/help_center/categories/{category_id} (or locale variant)"""
    client = get_client()
    if locale:
        url = f"{client.base_help_center}/{locale}/categories/{category_id}"
    else:
        url = f"{client.base_help_center}/categories/{category_id}"
    return client.request("DELETE", url)  # type: ignore
