from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def create_or_replace_inventory_item(
    sku: str,
    inventory_item: Dict[str, Any],
    *,
    content_language: str = "en-US",
) -> Dict[str, Any]:
    """PUT /inventory_item/{sku}

    Creates a new inventory item record or replaces an existing one.
    """
    client = EbayClient()
    return client.request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{sku}",
        json=inventory_item,
        headers={"Content-Language": content_language},
        content_type="application/json",
    )


def get_inventory_item(sku: str) -> Dict[str, Any]:
    """GET /inventory_item/{sku}"""
    client = EbayClient()
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


def delete_inventory_item(sku: str) -> Dict[str, Any]:
    """DELETE /inventory_item/{sku}"""
    client = EbayClient()
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


def get_inventory_items(
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /inventory_item

    Retrieves a paginated list of inventory items.
    """
    client = EbayClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/inventory/v1/inventory_item", params=params or None)


def create_inventory_location(
    merchant_location_key: str,
    location: Dict[str, Any],
) -> Dict[str, Any]:
    """POST /location/{merchantLocationKey}"""
    client = EbayClient()
    return client.request(
        "POST",
        f"/sell/inventory/v1/location/{merchant_location_key}",
        json=location,
        content_type="application/json",
    )


def get_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """GET /location/{merchantLocationKey}"""
    client = EbayClient()
    return client.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


def get_inventory_locations(
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /location"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/inventory/v1/location", params=params or None)


def update_inventory_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /location/{merchantLocationKey}"""
    client = EbayClient()
    return client.request(
        "PUT",
        f"/sell/inventory/v1/location/{merchant_location_key}",
        json=location,
        content_type="application/json",
    )


def disable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """POST /location/{merchantLocationKey}/disable"""
    client = EbayClient()
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/disable")


def enable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """POST /location/{merchantLocationKey}/enable"""
    client = EbayClient()
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/enable")


def create_offer(offer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /offer"""
    client = EbayClient()
    return client.request("POST", "/sell/inventory/v1/offer", json=offer, content_type="application/json")


def get_offer(offer_id: str) -> Dict[str, Any]:
    """GET /offer/{offerId}"""
    client = EbayClient()
    return client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


def update_offer(offer_id: str, offer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /offer/{offerId}"""
    client = EbayClient()
    return client.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json=offer, content_type="application/json")


def delete_offer(offer_id: str) -> Dict[str, Any]:
    """DELETE /offer/{offerId}"""
    client = EbayClient()
    return client.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


def get_offers(
    *,
    sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /offer

    Query offers by sku/marketplace/format.
    """
    client = EbayClient()
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
    return client.request("GET", "/sell/inventory/v1/offer", params=params or None)


def publish_offer(offer_id: str) -> Dict[str, Any]:
    """POST /offer/{offerId}/publish"""
    client = EbayClient()
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


def withdraw_offer(offer_id: str) -> Dict[str, Any]:
    """POST /offer/{offerId}/withdraw"""
    client = EbayClient()
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


def bulk_update_price_quantity(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /bulk_update_price_quantity"""
    client = EbayClient()
    return client.request(
        "POST",
        "/sell/inventory/v1/bulk_update_price_quantity",
        json=payload,
        content_type="application/json",
    )
