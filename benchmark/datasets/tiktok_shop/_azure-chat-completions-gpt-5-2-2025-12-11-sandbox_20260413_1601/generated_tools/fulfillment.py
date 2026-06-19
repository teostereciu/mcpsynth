"""Fulfillment/Logistics domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import TikTokRequestOptions, tiktok_request


def get_warehouse_list(*, shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """Get seller warehouse list.

    API: GET /fulfillment/202309/warehouses
    """

    return tiktok_request(
        "GET",
        "/fulfillment/202309/warehouses",
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def search_packages(
    *,
    package_status: Optional[str] = None,
    page_size: int = 20,
    page_token: Optional[str] = None,
    sort_field: str = "create_time",
    sort_order: str = "DESC",
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Search packages.

    API: POST /fulfillment/202309/packages/search
    """

    params: Dict[str, Any] = {
        "page_size": page_size,
        "sort_field": sort_field,
        "sort_order": sort_order,
    }
    if page_token is not None:
        params["page_token"] = page_token

    body: Dict[str, Any] = {}
    if package_status is not None:
        body["package_status"] = package_status

    return tiktok_request(
        "POST",
        "/fulfillment/202309/packages/search",
        params=params,
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def ship_package(
    *,
    package_id: str,
    handover_method: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Ship a package.

    API: POST /fulfillment/202309/packages/{package_id}/ship
    """

    body = {"handover_method": handover_method}
    return tiktok_request(
        "POST",
        f"/fulfillment/202309/packages/{package_id}/ship",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def get_package_shipping_document(
    *,
    package_id: str,
    document_type: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get package shipping document (e.g., shipping label).

    API: GET /fulfillment/202309/packages/{package_id}/shipping_document
    """

    return tiktok_request(
        "GET",
        f"/fulfillment/202309/packages/{package_id}/shipping_document",
        params={"document_type": document_type},
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )
