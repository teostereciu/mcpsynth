"""
eBay Sell Inventory API tools.
Covers: inventory items, offers, inventory item groups, bulk operations, locations.
"""

from typing import Optional
from auth import api_get, api_post, api_put, api_delete


# ---------------------------------------------------------------------------
# Inventory Items
# ---------------------------------------------------------------------------

def get_inventory_item(sku: str) -> dict:
    """Get a single inventory item by SKU."""
    return api_get(f"/sell/inventory/v1/inventory_item/{sku}")


def get_inventory_items(limit: int = 25, offset: int = 0) -> dict:
    """Get all inventory items for the seller (paginated)."""
    return api_get("/sell/inventory/v1/inventory_item", params={"limit": limit, "offset": offset})


def create_or_replace_inventory_item(sku: str, body: dict) -> dict:
    """
    Create or replace an inventory item for the given SKU.

    body fields (key ones):
      availability: dict with shipToLocationAvailability
      condition: e.g. "NEW", "USED_EXCELLENT"
      conditionDescription: str
      product: dict with title, description, aspects, imageUrls, mpn, brand
    """
    return api_put(f"/sell/inventory/v1/inventory_item/{sku}", body=body)


def delete_inventory_item(sku: str) -> dict:
    """Delete an inventory item by SKU."""
    return api_delete(f"/sell/inventory/v1/inventory_item/{sku}")


def bulk_create_or_replace_inventory_item(requests_list: list) -> dict:
    """
    Bulk create or replace up to 25 inventory items.
    requests_list: list of dicts each with 'sku' and inventory item fields.
    """
    return api_post("/sell/inventory/v1/bulk_create_or_replace_inventory_item",
                    body={"requests": requests_list})


def bulk_get_inventory_item(skus: list) -> dict:
    """Bulk get inventory items by list of SKUs (up to 25)."""
    return api_post("/sell/inventory/v1/bulk_get_inventory_item",
                    body={"requests": [{"sku": s} for s in skus]})


def bulk_update_price_quantity(requests_list: list) -> dict:
    """
    Bulk update price and/or quantity for up to 25 offers.
    requests_list: list of dicts with offerId, availableQuantity, price fields.
    """
    return api_post("/sell/inventory/v1/bulk_update_price_quantity",
                    body={"requests": requests_list})


# ---------------------------------------------------------------------------
# Inventory Item Groups
# ---------------------------------------------------------------------------

def get_inventory_item_group(inventory_item_group_key: str) -> dict:
    """Get an inventory item group (multi-variation listing group)."""
    return api_get(f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


def create_or_replace_inventory_item_group(inventory_item_group_key: str, body: dict) -> dict:
    """
    Create or replace an inventory item group.

    body fields:
      aspects: dict of shared aspects
      description: str
      imageUrls: list of str
      inventoryItems: list of dicts with sku and availability
      subtitle: str
      title: str
      variantSKUs: list of str
    """
    return api_put(f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}", body=body)


def delete_inventory_item_group(inventory_item_group_key: str) -> dict:
    """Delete an inventory item group."""
    return api_delete(f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


# ---------------------------------------------------------------------------
# Offers
# ---------------------------------------------------------------------------

def get_offers(sku: Optional[str] = None, marketplace_id: Optional[str] = None,
               format: Optional[str] = None, limit: int = 25, offset: int = 0) -> dict:
    """Get all offers, optionally filtered by SKU, marketplace, or format."""
    params: dict = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    if format:
        params["format"] = format
    return api_get("/sell/inventory/v1/offer", params=params)


def get_offer(offer_id: str) -> dict:
    """Get a single offer by offer ID."""
    return api_get(f"/sell/inventory/v1/offer/{offer_id}")


def create_offer(body: dict) -> dict:
    """
    Create a new offer.

    body fields:
      sku: str (required)
      marketplaceId: str (required, e.g. "EBAY_US")
      format: str (e.g. "FIXED_PRICE")
      availableQuantity: int
      categoryId: str
      listingDescription: str
      listingPolicies: dict (fulfillmentPolicyId, paymentPolicyId, returnPolicyId)
      merchantLocationKey: str
      pricingSummary: dict with price (value, currency)
      tax: dict
      storeCategoryNames: list of str
    """
    return api_post("/sell/inventory/v1/offer", body=body)


def update_offer(offer_id: str, body: dict) -> dict:
    """Update an existing offer by offer ID."""
    return api_put(f"/sell/inventory/v1/offer/{offer_id}", body=body)


def delete_offer(offer_id: str) -> dict:
    """Delete an offer by offer ID."""
    return api_delete(f"/sell/inventory/v1/offer/{offer_id}")


def publish_offer(offer_id: str) -> dict:
    """Publish an offer to create/update the corresponding eBay listing."""
    return api_post(f"/sell/inventory/v1/offer/{offer_id}/publish")


def publish_offer_by_inventory_item_group(inventory_item_group_key: str,
                                          marketplace_id: str) -> dict:
    """Publish all offers associated with an inventory item group."""
    return api_post("/sell/inventory/v1/offer/publish_by_inventory_item_group",
                    body={"inventoryItemGroupKey": inventory_item_group_key,
                          "marketplaceId": marketplace_id})


def withdraw_offer(offer_id: str) -> dict:
    """Withdraw (unpublish) an offer, ending the associated listing."""
    return api_post(f"/sell/inventory/v1/offer/{offer_id}/withdraw")


def withdraw_offer_by_inventory_item_group(inventory_item_group_key: str,
                                           marketplace_id: str) -> dict:
    """Withdraw all offers associated with an inventory item group."""
    return api_post("/sell/inventory/v1/offer/withdraw_by_inventory_item_group",
                    body={"inventoryItemGroupKey": inventory_item_group_key,
                          "marketplaceId": marketplace_id})


def bulk_create_offer(requests_list: list) -> dict:
    """Bulk create up to 25 offers."""
    return api_post("/sell/inventory/v1/bulk_create_offer",
                    body={"requests": requests_list})


def bulk_publish_offer(requests_list: list) -> dict:
    """Bulk publish up to 25 offers. requests_list: list of dicts with offerId."""
    return api_post("/sell/inventory/v1/bulk_publish_offer",
                    body={"requests": requests_list})


def get_listing_fees(offer_ids: list) -> dict:
    """Get listing fees for a list of offer IDs before publishing."""
    return api_post("/sell/inventory/v1/offer/get_listing_fees",
                    body={"offers": [{"offerId": oid} for oid in offer_ids]})


# ---------------------------------------------------------------------------
# Inventory Locations
# ---------------------------------------------------------------------------

def get_inventory_location(merchant_location_key: str) -> dict:
    """Get a specific inventory location."""
    return api_get(f"/sell/inventory/v1/location/{merchant_location_key}")


def get_inventory_locations(limit: int = 25, offset: int = 0) -> dict:
    """Get all inventory locations for the seller."""
    return api_get("/sell/inventory/v1/location", params={"limit": limit, "offset": offset})


def create_inventory_location(merchant_location_key: str, body: dict) -> dict:
    """
    Create an inventory location.

    body fields:
      location: dict with address fields
      locationInstructions: str
      locationTypes: list of str (e.g. ["WAREHOUSE"])
      locationWebUrl: str
      merchantLocationStatus: str ("ENABLED" or "DISABLED")
      name: str
      operatingHours: list
      phone: str
      specialHours: list
    """
    return api_post(f"/sell/inventory/v1/location/{merchant_location_key}", body=body)


def update_inventory_location(merchant_location_key: str, body: dict) -> dict:
    """Update an existing inventory location."""
    return api_post(f"/sell/inventory/v1/location/{merchant_location_key}/update_location_details",
                    body=body)


def delete_inventory_location(merchant_location_key: str) -> dict:
    """Delete an inventory location."""
    return api_delete(f"/sell/inventory/v1/location/{merchant_location_key}")


def enable_inventory_location(merchant_location_key: str) -> dict:
    """Enable an inventory location."""
    return api_post(f"/sell/inventory/v1/location/{merchant_location_key}/enable")


def disable_inventory_location(merchant_location_key: str) -> dict:
    """Disable an inventory location."""
    return api_post(f"/sell/inventory/v1/location/{merchant_location_key}/disable")
