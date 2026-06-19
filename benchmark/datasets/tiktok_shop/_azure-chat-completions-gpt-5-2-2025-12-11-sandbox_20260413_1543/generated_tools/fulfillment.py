"""Fulfillment/logistics domain tools (warehouses, packages, shipping docs)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .client import TikTokShopClient


def search_packages(
    *,
    page_size: int = 20,
    page_token: Optional[str] = None,
    sort_field: Optional[str] = None,
    sort_order: Optional[str] = None,
    create_time_ge: Optional[int] = None,
    create_time_lt: Optional[int] = None,
    update_time_ge: Optional[int] = None,
    update_time_lt: Optional[int] = None,
    package_status: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /fulfillment/202309/packages/search"""

    client = TikTokShopClient.from_env()
    params: Dict[str, Any] = {
        "page_size": page_size,
        "page_token": page_token,
        "sort_field": sort_field,
        "sort_order": sort_order,
        "shop_cipher": shop_cipher,
    }
    body: Dict[str, Any] = {
        "create_time_ge": create_time_ge,
        "create_time_lt": create_time_lt,
        "update_time_ge": update_time_ge,
        "update_time_lt": update_time_lt,
        "package_status": package_status,
    }
    body = {k: v for k, v in body.items() if v is not None}

    return client.request(
        "POST",
        "/fulfillment/202309/packages/search",
        params=params,
        body=body,
        use_shop_cipher=True,
    )


def get_package_shipping_document(
    *,
    package_id: str,
    document_type: str,
    document_size: Optional[str] = None,
    document_format: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /fulfillment/202309/packages/{package_id}/shipping_documents"""

    client = TikTokShopClient.from_env()
    params: Dict[str, Any] = {
        "document_type": document_type,
        "document_size": document_size,
        "document_format": document_format,
        "shop_cipher": shop_cipher,
    }
    return client.request(
        "GET",
        f"/fulfillment/202309/packages/{package_id}/shipping_documents",
        params=params,
        use_shop_cipher=True,
    )


def ship_package(
    *,
    package_id: str,
    handover_method: Optional[str] = None,
    pickup_slot: Optional[Dict[str, Any]] = None,
    self_shipment: Optional[Dict[str, Any]] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /fulfillment/202309/packages/{package_id}/ship"""

    client = TikTokShopClient.from_env()
    body: Dict[str, Any] = {}
    if handover_method is not None:
        body["handover_method"] = handover_method
    if pickup_slot is not None:
        body["pickup_slot"] = pickup_slot
    if self_shipment is not None:
        body["self_shipment"] = self_shipment

    return client.request(
        "POST",
        f"/fulfillment/202309/packages/{package_id}/ship",
        params={"shop_cipher": shop_cipher},
        body=body,
        use_shop_cipher=True,
    )


def get_warehouse_list(*, shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """GET /logistics/202309/warehouses"""

    client = TikTokShopClient.from_env()
    return client.request(
        "GET",
        "/logistics/202309/warehouses",
        params={"shop_cipher": shop_cipher},
        use_shop_cipher=True,
    )
