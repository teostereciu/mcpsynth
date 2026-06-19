from __future__ import annotations

from typing import Any, Dict, Optional

from .http import safe_call


def search_packages(
    package_status: Optional[str] = None,
    page_size: int = 20,
    page_token: Optional[str] = None,
    sort_field: str = "create_time",
    sort_order: str = "DESC",
    create_time_ge: Optional[int] = None,
    create_time_lt: Optional[int] = None,
    update_time_ge: Optional[int] = None,
    update_time_lt: Optional[int] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /fulfillment/202309/packages/search"""
    params: Dict[str, Any] = {
        "page_size": page_size,
        "page_token": page_token,
        "sort_field": sort_field,
        "sort_order": sort_order,
    }
    if shop_cipher:
        params["shop_cipher"] = shop_cipher

    body: Dict[str, Any] = {
        "package_status": package_status,
        "create_time_ge": create_time_ge,
        "create_time_lt": create_time_lt,
        "update_time_ge": update_time_ge,
        "update_time_lt": update_time_lt,
    }
    return safe_call("POST", "/fulfillment/202309/packages/search", params=params, body=body)


def ship_package(
    package_id: str,
    handover_method: str = "DROP_OFF",
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /fulfillment/202309/packages/{package_id}/ship"""
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    body = {"handover_method": handover_method}
    return safe_call("POST", f"/fulfillment/202309/packages/{package_id}/ship", params=params, body=body)


def get_package_shipping_document(
    package_id: str,
    document_type: str = "SHIPPING_LABEL",
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /fulfillment/202309/packages/{package_id}/shipping_document"""
    params: Dict[str, Any] = {"document_type": document_type}
    if shop_cipher:
        params["shop_cipher"] = shop_cipher
    return safe_call("GET", f"/fulfillment/202309/packages/{package_id}/shipping_document", params=params)


def get_warehouse_list(shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """GET /fulfillment/202309/warehouses"""
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("GET", "/fulfillment/202309/warehouses", params=params)
