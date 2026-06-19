"""eBay Sell Inventory API tools."""
from typing import Optional
from .client import get_client


def create_or_replace_inventory_item(seller_sku: str, body: dict, content_language: str = "en-US") -> dict:
    """Create or replace an inventory item record for a given SKU."""
    client = get_client()
    headers = {"Content-Language": content_language}
    return client.request("PUT", f"/sell/inventory/v1/inventory_item/{seller_sku}", json=body, extra_headers=headers)


def get_inventory_item(seller_sku: str) -> dict:
    """Retrieve the inventory item record for a given SKU."""
    client = get_client()
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{seller_sku}")


def get_inventory_items(limit: Optional[str] = None, offset: Optional[str] = None) -> dict:
    """Retrieve all inventory item records for the seller's account."""
    client = get_client()
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/inventory/v1/inventory_item", params=params)


def delete_inventory_item(seller_sku: str) -> dict:
    """Delete an inventory item record for a given SKU."""
    client = get_client()
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{seller_sku}")


def bulk_create_or_replace_inventory_item(body: dict, content_language: str = "en-US") -> dict:
    """Create or replace up to 25 inventory item records in one call."""
    client = get_client()
    headers = {"Content-Language": content_language}
    return client.request("POST", "/sell/inventory/v1/bulk_create_or_replace_inventory_item", json=body, extra_headers=headers)


def bulk_get_inventory_item(body: dict) -> dict:
    """Retrieve up to 25 inventory item records by SKU values."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_get_inventory_item", json=body)


def bulk_update_price_quantity(body: dict) -> dict:
    """Update price and/or quantity for up to 25 offers associated with one inventory item."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_update_price_quantity", json=body)


def create_offer(body: dict, content_language: str = "en-US") -> dict:
    """Create an offer for a specific inventory item on a specific eBay marketplace."""
    client = get_client()
    headers = {"Content-Language": content_language}
    return client.request("POST", "/sell/inventory/v1/offer", json=body, extra_headers=headers)


def get_offer(offer_id: str) -> dict:
    """Retrieve a specific published or unpublished offer by offer ID."""
    client = get_client()
    return client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


def get_offers(seller_sku: Optional[str] = None, marketplace_id: Optional[str] = None,
               format: Optional[str] = None, limit: Optional[str] = None,
               offset: Optional[str] = None) -> dict:
    """Retrieve all existing offers for a specified SKU value."""
    client = get_client()
    params = {}
    if seller_sku:
        params["seller_sku"] = seller_sku
    if marketplace_id:
        params["market_id"] = marketplace_id
    if format:
        params["format"] = format
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/inventory/v1/offer", params=params)


def update_offer(offer_id: str, body: dict, content_language: str = "en-US") -> dict:
    """Update an existing offer (published or unpublished)."""
    client = get_client()
    headers = {"Content-Language": content_language}
    return client.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json=body, extra_headers=headers)


def delete_offer(offer_id: str) -> dict:
    """Delete an unpublished offer or end a published eBay listing."""
    client = get_client()
    return client.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


def publish_offer(offer_id: str) -> dict:
    """Convert an unpublished offer into a live eBay listing."""
    client = get_client()
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


def withdraw_offer(offer_id: str) -> dict:
    """End a single-variation listing associated with the specified offer."""
    client = get_client()
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


def bulk_create_offer(body: dict) -> dict:
    """Create up to 25 offers in one call."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_create_offer", json=body)


def bulk_publish_offer(body: dict) -> dict:
    """Convert up to 25 unpublished offers into live eBay listings."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_publish_offer", json=body)


def get_listing_fees(body: dict) -> dict:
    """Retrieve expected listing fees for up to 250 unpublished offers."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/offer/get_listing_fees", json=body)


def publish_offer_by_inventory_item_group(body: dict) -> dict:
    """Convert all unpublished offers in an inventory item group into a multiple-variation listing."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/offer/publish_by_inventory_item_group", json=body)


def withdraw_offer_by_inventory_item_group(body: dict) -> dict:
    """End a multiple-variation listing associated with an inventory item group."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/offer/withdraw_by_inventory_item_group", json=body)


def create_inventory_location(merchant_location_key: str, body: dict) -> dict:
    """Create a new inventory location."""
    client = get_client()
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}", json=body)


def get_inventory_location(merchant_location_key: str) -> dict:
    """Retrieve details for a specific inventory location."""
    client = get_client()
    return client.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


def get_inventory_locations(limit: Optional[str] = None, offset: Optional[str] = None) -> dict:
    """Retrieve all inventory locations for the seller's account."""
    client = get_client()
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/inventory/v1/location", params=params)


def delete_inventory_location(merchant_location_key: str) -> dict:
    """Delete an inventory location."""
    client = get_client()
    return client.request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")


def disable_inventory_location(merchant_location_key: str) -> dict:
    """Disable an inventory location."""
    client = get_client()
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/disable")


def enable_inventory_location(merchant_location_key: str) -> dict:
    """Enable a previously disabled inventory location."""
    client = get_client()
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/enable")


def update_inventory_location(merchant_location_key: str, body: dict) -> dict:
    """Update details for an existing inventory location."""
    client = get_client()
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/update_location_details", json=body)


def create_or_replace_inventory_item_group(inventory_item_group_key: str, body: dict) -> dict:
    """Create or replace an inventory item group (for multi-variation listings)."""
    client = get_client()
    return client.request("PUT", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}", json=body)


def get_inventory_item_group(inventory_item_group_key: str) -> dict:
    """Retrieve an inventory item group by its key."""
    client = get_client()
    return client.request("GET", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


def delete_inventory_item_group(inventory_item_group_key: str) -> dict:
    """Delete an inventory item group."""
    client = get_client()
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


def bulk_migrate_listing(body: dict) -> dict:
    """Convert existing eBay listings (1-5) to Inventory API objects."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_migrate_listing", json=body)


def create_or_replace_product_compatibility(seller_sku: str, body: dict) -> dict:
    """Create or replace product compatibility for an inventory item."""
    client = get_client()
    return client.request("PUT", f"/sell/inventory/v1/inventory_item/{seller_sku}/product_compatibility", json=body)


def get_product_compatibility(seller_sku: str) -> dict:
    """Retrieve product compatibility for an inventory item."""
    client = get_client()
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{seller_sku}/product_compatibility")


def delete_product_compatibility(seller_sku: str) -> dict:
    """Delete product compatibility for an inventory item."""
    client = get_client()
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{seller_sku}/product_compatibility")
