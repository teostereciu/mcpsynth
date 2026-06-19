"""eBay Sell Inventory API tools."""
from typing import Any, Optional
from .client import get_client


# --- Inventory Items ---

def create_or_replace_inventory_item(seller_sku: str, body: dict) -> dict:
    """Create or replace an inventory item record for a given SKU."""
    client = get_client()
    return client.request("PUT", f"/sell/inventory/v1/inventory_item/{seller_sku}", json=body)


def get_inventory_item(seller_sku: str) -> dict:
    """Retrieve the inventory item record for a given SKU."""
    client = get_client()
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{seller_sku}")


def get_inventory_items(limit: Optional[str] = None, offset: Optional[str] = None) -> dict:
    """Retrieve all inventory item records for the seller's account."""
    client = get_client()
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/inventory/v1/inventory_item", params=params)


def delete_inventory_item(seller_sku: str) -> dict:
    """Delete an inventory item record associated with a specified SKU."""
    client = get_client()
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{seller_sku}")


def bulk_create_or_replace_inventory_item(body: dict) -> dict:
    """Create or update up to 25 inventory item records in one call."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_create_or_replace_inventory_item", json=body)


def bulk_get_inventory_item(body: dict) -> dict:
    """Retrieve up to 25 inventory item records by SKU values."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_get_inventory_item", json=body)


def bulk_update_price_quantity(body: dict) -> dict:
    """Update price and/or quantity for up to 25 offers of one inventory item."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_update_price_quantity", json=body)


# --- Offers ---

def create_offer(body: dict) -> dict:
    """Create an offer for a specific inventory item on an eBay marketplace."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/offer", json=body)


def get_offer(offer_id: str) -> dict:
    """Retrieve a specific published or unpublished offer by offer ID."""
    client = get_client()
    return client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


def get_offers(
    seller_sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve all existing offers for a specified SKU value."""
    client = get_client()
    params = {}
    if seller_sku is not None:
        params["seller_sku"] = seller_sku
    if marketplace_id is not None:
        params["marketplace_id"] = marketplace_id
    if format is not None:
        params["format"] = format
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/inventory/v1/offer", params=params)


def update_offer(offer_id: str, body: dict) -> dict:
    """Update an existing offer (published or unpublished)."""
    client = get_client()
    return client.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json=body)


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
    """Create multiple offers (up to 25) for inventory items in one call."""
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


def bulk_migrate_listing(body: dict) -> dict:
    """Convert existing eBay listings to Inventory API objects (up to 5 at a time)."""
    client = get_client()
    return client.request("POST", "/sell/inventory/v1/bulk_migrate_listing", json=body)


# --- Inventory Locations ---

def create_inventory_location(merchant_location_key: str, body: dict) -> dict:
    """Create a new inventory location."""
    client = get_client()
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}", json=body)


def get_inventory_location(merchant_location_key: str) -> dict:
    """Retrieve all defined details of a specific inventory location."""
    client = get_client()
    return client.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


def get_inventory_locations(limit: Optional[str] = None, offset: Optional[str] = None) -> dict:
    """Retrieve all inventory locations associated with the seller's account."""
    client = get_client()
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/inventory/v1/location", params=params)


def delete_inventory_location(merchant_location_key: str) -> dict:
    """Delete the specified inventory location."""
    client = get_client()
    return client.request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")
