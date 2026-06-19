"""
eBay Sell Inventory API tools.
Covers: inventory items, offers, inventory item groups, bulk operations, locations.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-inventory")

# ---------------------------------------------------------------------------
# Inventory Items
# ---------------------------------------------------------------------------

@mcp.tool()
def get_inventory_item(sku: str) -> dict:
    """
    Retrieve a single inventory item by SKU.

    Args:
        sku: The seller-defined Stock Keeping Unit (SKU) of the inventory item.
    """
    return ebay_request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def create_or_replace_inventory_item(sku: str, item: dict) -> dict:
    """
    Create or fully replace an inventory item for the given SKU.

    Args:
        sku: The seller-defined SKU for the inventory item.
        item: Full inventory item object (condition, product, availability, etc.).
              Example: {
                "condition": "NEW",
                "product": {
                  "title": "My Product",
                  "description": "Description here",
                  "aspects": {"Brand": ["Acme"]},
                  "imageUrls": ["https://example.com/img.jpg"]
                },
                "availability": {
                  "shipToLocationAvailability": {"quantity": 10}
                }
              }
    """
    return ebay_request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json=item)


@mcp.tool()
def delete_inventory_item(sku: str) -> dict:
    """
    Delete an inventory item by SKU.

    Args:
        sku: The seller-defined SKU of the inventory item to delete.
    """
    return ebay_request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def get_inventory_items(limit: int = 25, offset: int = 0) -> dict:
    """
    Retrieve a paginated list of all inventory items for the seller.

    Args:
        limit: Number of items to return (1–200, default 25).
        offset: Number of items to skip for pagination (default 0).
    """
    return ebay_request(
        "GET",
        "/sell/inventory/v1/inventory_item",
        params={"limit": limit, "offset": offset},
    )


@mcp.tool()
def bulk_create_or_replace_inventory_items(requests_list: list) -> dict:
    """
    Create or replace up to 25 inventory items in a single call.

    Args:
        requests_list: List of inventory item request objects, each containing
                       'sku' and the inventory item fields.
    """
    return ebay_request(
        "POST",
        "/sell/inventory/v1/bulk_create_or_replace_inventory_item",
        json={"requests": requests_list},
    )


@mcp.tool()
def bulk_get_inventory_items(skus: list) -> dict:
    """
    Retrieve up to 25 inventory items by SKU in a single call.

    Args:
        skus: List of SKU strings to retrieve.
    """
    return ebay_request(
        "POST",
        "/sell/inventory/v1/bulk_get_inventory_item",
        json={"requests": [{"sku": s} for s in skus]},
    )


@mcp.tool()
def bulk_update_price_quantity(requests_list: list) -> dict:
    """
    Update price and/or quantity for up to 25 inventory items in one call.

    Args:
        requests_list: List of objects with 'sku', optional 'price', and
                       optional 'shipToLocationAvailability' fields.
    """
    return ebay_request(
        "POST",
        "/sell/inventory/v1/bulk_update_price_quantity",
        json={"requests": requests_list},
    )


# ---------------------------------------------------------------------------
# Inventory Item Groups (multi-variation listings)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_inventory_item_group(inventory_item_group_key: str) -> dict:
    """
    Retrieve an inventory item group (multi-variation parent) by its key.

    Args:
        inventory_item_group_key: The unique key of the inventory item group.
    """
    return ebay_request(
        "GET",
        f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}",
    )


@mcp.tool()
def create_or_replace_inventory_item_group(
    inventory_item_group_key: str, group: dict
) -> dict:
    """
    Create or replace an inventory item group for multi-variation listings.

    Args:
        inventory_item_group_key: Unique key for the group.
        group: Group object containing title, description, aspects, imageUrls,
               variantSKUs, and variesBy fields.
    """
    return ebay_request(
        "PUT",
        f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}",
        json=group,
    )


@mcp.tool()
def delete_inventory_item_group(inventory_item_group_key: str) -> dict:
    """
    Delete an inventory item group by its key.

    Args:
        inventory_item_group_key: The unique key of the inventory item group.
    """
    return ebay_request(
        "DELETE",
        f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}",
    )


# ---------------------------------------------------------------------------
# Offers
# ---------------------------------------------------------------------------

@mcp.tool()
def get_offers(
    sku: str | None = None,
    marketplace_id: str | None = None,
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """
    Retrieve offers, optionally filtered by SKU and/or marketplace.

    Args:
        sku: Filter by seller SKU (optional).
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US' (optional).
        limit: Number of offers to return (default 25).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    return ebay_request("GET", "/sell/inventory/v1/offer", params=params)


@mcp.tool()
def get_offer(offer_id: str) -> dict:
    """
    Retrieve a single offer by its offer ID.

    Args:
        offer_id: The unique identifier of the offer.
    """
    return ebay_request("GET", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def create_offer(offer: dict) -> dict:
    """
    Create a new offer for an inventory item.

    Args:
        offer: Offer object. Required fields: sku, marketplaceId, format,
               listingDescription, pricingSummary, categoryId, merchantLocationKey.
               Example: {
                 "sku": "MY-SKU-001",
                 "marketplaceId": "EBAY_US",
                 "format": "FIXED_PRICE",
                 "availableQuantity": 5,
                 "categoryId": "9355",
                 "listingDescription": "Great product",
                 "listingPolicies": {
                   "fulfillmentPolicyId": "...",
                   "paymentPolicyId": "...",
                   "returnPolicyId": "..."
                 },
                 "pricingSummary": {"price": {"value": "29.99", "currency": "USD"}},
                 "merchantLocationKey": "WH1"
               }
    """
    return ebay_request("POST", "/sell/inventory/v1/offer", json=offer)


@mcp.tool()
def update_offer(offer_id: str, offer: dict) -> dict:
    """
    Update an existing offer.

    Args:
        offer_id: The unique identifier of the offer to update.
        offer: Updated offer object (same structure as create_offer).
    """
    return ebay_request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json=offer)


@mcp.tool()
def delete_offer(offer_id: str) -> dict:
    """
    Delete an offer by its offer ID.

    Args:
        offer_id: The unique identifier of the offer to delete.
    """
    return ebay_request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def publish_offer(offer_id: str) -> dict:
    """
    Publish an offer to create or update a live eBay listing.

    Args:
        offer_id: The unique identifier of the offer to publish.
    """
    return ebay_request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


@mcp.tool()
def withdraw_offer(offer_id: str) -> dict:
    """
    Withdraw (end) a published offer/listing.

    Args:
        offer_id: The unique identifier of the offer to withdraw.
    """
    return ebay_request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


@mcp.tool()
def publish_offer_by_inventory_item_group(
    inventory_item_group_key: str, marketplace_id: str
) -> dict:
    """
    Publish all offers associated with an inventory item group as a
    multi-variation listing.

    Args:
        inventory_item_group_key: The key of the inventory item group.
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "POST",
        "/sell/inventory/v1/offer/publish_by_inventory_item_group",
        json={
            "inventoryItemGroupKey": inventory_item_group_key,
            "marketplaceId": marketplace_id,
        },
    )


@mcp.tool()
def withdraw_offer_by_inventory_item_group(
    inventory_item_group_key: str, marketplace_id: str
) -> dict:
    """
    Withdraw all offers associated with an inventory item group.

    Args:
        inventory_item_group_key: The key of the inventory item group.
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "POST",
        "/sell/inventory/v1/offer/withdraw_by_inventory_item_group",
        json={
            "inventoryItemGroupKey": inventory_item_group_key,
            "marketplaceId": marketplace_id,
        },
    )


@mcp.tool()
def bulk_create_offer(offers: list) -> dict:
    """
    Create up to 25 offers in a single bulk call.

    Args:
        offers: List of offer objects (same structure as create_offer).
    """
    return ebay_request(
        "POST",
        "/sell/inventory/v1/bulk_create_offer",
        json={"requests": offers},
    )


@mcp.tool()
def bulk_publish_offer(offer_ids: list) -> dict:
    """
    Publish up to 25 offers in a single bulk call.

    Args:
        offer_ids: List of offer ID strings to publish.
    """
    return ebay_request(
        "POST",
        "/sell/inventory/v1/bulk_publish_offer",
        json={"requests": [{"offerId": oid} for oid in offer_ids]},
    )


@mcp.tool()
def get_listing_fees(offer_ids: list) -> dict:
    """
    Retrieve estimated listing fees for one or more offers before publishing.

    Args:
        offer_ids: List of offer ID strings.
    """
    return ebay_request(
        "POST",
        "/sell/inventory/v1/offer/get_listing_fees",
        json={"offers": [{"offerId": oid} for oid in offer_ids]},
    )


# ---------------------------------------------------------------------------
# Inventory Locations
# ---------------------------------------------------------------------------

@mcp.tool()
def get_inventory_location(merchant_location_key: str) -> dict:
    """
    Retrieve a specific inventory location by its merchant location key.

    Args:
        merchant_location_key: The seller-defined key for the location.
    """
    return ebay_request(
        "GET",
        f"/sell/inventory/v1/location/{merchant_location_key}",
    )


@mcp.tool()
def get_inventory_locations(limit: int = 25, offset: int = 0) -> dict:
    """
    Retrieve all inventory locations for the seller.

    Args:
        limit: Number of locations to return (default 25).
        offset: Pagination offset (default 0).
    """
    return ebay_request(
        "GET",
        "/sell/inventory/v1/location",
        params={"limit": limit, "offset": offset},
    )


@mcp.tool()
def create_inventory_location(merchant_location_key: str, location: dict) -> dict:
    """
    Create a new inventory location.

    Args:
        merchant_location_key: Seller-defined unique key for the location.
        location: Location object with name, merchantLocationStatus, location
                  (address), and operatingHours fields.
    """
    return ebay_request(
        "POST",
        f"/sell/inventory/v1/location/{merchant_location_key}",
        json=location,
    )


@mcp.tool()
def update_inventory_location(merchant_location_key: str, location: dict) -> dict:
    """
    Update an existing inventory location's details.

    Args:
        merchant_location_key: The key of the location to update.
        location: Partial or full location object with fields to update.
    """
    return ebay_request(
        "POST",
        f"/sell/inventory/v1/location/{merchant_location_key}/update_location_details",
        json=location,
    )


@mcp.tool()
def delete_inventory_location(merchant_location_key: str) -> dict:
    """
    Delete an inventory location.

    Args:
        merchant_location_key: The key of the location to delete.
    """
    return ebay_request(
        "DELETE",
        f"/sell/inventory/v1/location/{merchant_location_key}",
    )


@mcp.tool()
def enable_inventory_location(merchant_location_key: str) -> dict:
    """
    Enable (activate) a disabled inventory location.

    Args:
        merchant_location_key: The key of the location to enable.
    """
    return ebay_request(
        "POST",
        f"/sell/inventory/v1/location/{merchant_location_key}/enable",
    )


@mcp.tool()
def disable_inventory_location(merchant_location_key: str) -> dict:
    """
    Disable an inventory location so it cannot be used for new offers.

    Args:
        merchant_location_key: The key of the location to disable.
    """
    return ebay_request(
        "POST",
        f"/sell/inventory/v1/location/{merchant_location_key}/disable",
    )
