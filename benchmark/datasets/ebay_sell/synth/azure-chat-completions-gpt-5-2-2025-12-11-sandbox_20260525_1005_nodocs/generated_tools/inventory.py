from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def inventory_get_inventory_item(sku: str) -> Dict[str, Any]:
    """GET /sell/inventory/v1/inventory_item/{sku}"""
    c = EbayClient()
    return c.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


def inventory_create_or_replace_inventory_item(sku: str, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/inventory/v1/inventory_item/{sku}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json=inventory_item)


def inventory_delete_inventory_item(sku: str) -> Dict[str, Any]:
    """DELETE /sell/inventory/v1/inventory_item/{sku}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


def inventory_bulk_create_or_replace_inventory_item(request_body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/inventory/v1/bulk_create_or_replace_inventory_item"""
    c = EbayClient()
    return c.request("POST", "/sell/inventory/v1/bulk_create_or_replace_inventory_item", json=request_body)


def inventory_get_offers(
    sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /sell/inventory/v1/offer"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if sku is not None:
        params["sku"] = sku
    if marketplace_id is not None:
        params["marketplace_id"] = marketplace_id
    if format is not None:
        params["format"] = format
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return c.request("GET", "/sell/inventory/v1/offer", params=params)


def inventory_get_offer(offer_id: str) -> Dict[str, Any]:
    """GET /sell/inventory/v1/offer/{offerId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


def inventory_create_offer(offer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/inventory/v1/offer"""
    c = EbayClient()
    return c.request("POST", "/sell/inventory/v1/offer", json=offer)


def inventory_update_offer(offer_id: str, offer_patch: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/inventory/v1/offer/{offerId}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json=offer_patch)


def inventory_delete_offer(offer_id: str) -> Dict[str, Any]:
    """DELETE /sell/inventory/v1/offer/{offerId}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


def inventory_publish_offer(offer_id: str) -> Dict[str, Any]:
    """POST /sell/inventory/v1/offer/{offerId}/publish"""
    c = EbayClient()
    return c.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


def inventory_withdraw_offer(offer_id: str) -> Dict[str, Any]:
    """POST /sell/inventory/v1/offer/{offerId}/withdraw"""
    c = EbayClient()
    return c.request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


def inventory_get_locations(limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /sell/inventory/v1/location"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return c.request("GET", "/sell/inventory/v1/location", params=params)


def inventory_get_location(merchant_location_key: str) -> Dict[str, Any]:
    """GET /sell/inventory/v1/location/{merchantLocationKey}"""
    c = EbayClient()
    return c.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


def inventory_create_or_replace_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/inventory/v1/location/{merchantLocationKey}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/inventory/v1/location/{merchant_location_key}", json=location)


def inventory_delete_location(merchant_location_key: str) -> Dict[str, Any]:
    """DELETE /sell/inventory/v1/location/{merchantLocationKey}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")
