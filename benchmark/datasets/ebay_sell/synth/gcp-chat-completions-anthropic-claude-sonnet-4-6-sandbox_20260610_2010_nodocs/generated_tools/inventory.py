"""
eBay Sell Inventory API tools.
Covers: inventory items, offers, inventory item groups, bulk operations, locations.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post, api_put, api_delete, api_patch

mcp = FastMCP("ebay-inventory")


# ── Inventory Items ──────────────────────────────────────────────────────────

@mcp.tool()
def get_inventory_item(sku: str) -> dict:
    """Retrieve a single inventory item by SKU."""
    return api_get(f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def get_inventory_items(limit: int = 25, offset: int = 0) -> dict:
    """Retrieve a paginated list of all inventory items for the seller."""
    return api_get("/sell/inventory/v1/inventory_item", params={"limit": limit, "offset": offset})


@mcp.tool()
def create_or_replace_inventory_item(sku: str, product: dict, condition: str,
                                     availability: dict, package_weight_and_size: dict | None = None) -> dict:
    """
    Create or replace an inventory item identified by SKU.

    Args:
        sku: Seller-defined SKU for the item.
        product: Dict with title, description, aspects, imageUrls, etc.
        condition: Item condition (e.g. NEW, LIKE_NEW, GOOD).
        availability: Dict with shipToLocationAvailability (quantity).
        package_weight_and_size: Optional shipping package details.
    """
    body: dict = {"product": product, "condition": condition, "availability": availability}
    if package_weight_and_size:
        body["packageWeightAndSize"] = package_weight_and_size
    from .auth import auth_headers, get_base_url
    import requests
    url = get_base_url() + f"/sell/inventory/v1/inventory_item/{sku}"
    try:
        r = requests.put(url, headers=auth_headers(), json=body, timeout=30)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json() if r.text else {"status": "ok"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def delete_inventory_item(sku: str) -> dict:
    """Delete an inventory item by SKU."""
    return api_delete(f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def bulk_create_or_replace_inventory_item(requests_list: list[dict]) -> dict:
    """
    Bulk create or replace up to 25 inventory items in one call.

    Args:
        requests_list: List of inventory item request objects, each containing
                       sku, product, condition, availability.
    """
    return api_post("/sell/inventory/v1/bulk_create_or_replace_inventory_item",
                    body={"requests": requests_list})


@mcp.tool()
def bulk_get_inventory_item(skus: list[str]) -> dict:
    """
    Bulk retrieve up to 25 inventory items by SKU list.

    Args:
        skus: List of SKU strings to retrieve.
    """
    return api_post("/sell/inventory/v1/bulk_get_inventory_item",
                    body={"requests": [{"sku": s} for s in skus]})


@mcp.tool()
def bulk_update_price_quantity(requests_list: list[dict]) -> dict:
    """
    Bulk update price and/or quantity for up to 25 offers/inventory items.

    Args:
        requests_list: List of objects with sku, shipToLocationAvailability,
                       and/or offers (list with offerId, price).
    """
    return api_post("/sell/inventory/v1/bulk_update_price_quantity",
                    body={"requests": requests_list})


# ── Inventory Item Groups ────────────────────────────────────────────────────

@mcp.tool()
def get_inventory_item_group(inventory_item_group_key: str) -> dict:
    """Retrieve an inventory item group (multi-variation listing group) by key."""
    return api_get(f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


@mcp.tool()
def create_or_replace_inventory_item_group(inventory_item_group_key: str,
                                           title: str,
                                           description: str,
                                           aspects: dict,
                                           image_urls: list[str],
                                           variant_skus: list[str],
                                           subtitle: str | None = None) -> dict:
    """
    Create or replace an inventory item group for multi-variation listings.

    Args:
        inventory_item_group_key: Unique key for the group.
        title: Title for the group listing.
        description: Description for the group listing.
        aspects: Shared aspects dict (e.g. {"Brand": ["Nike"]}).
        image_urls: List of image URLs for the group.
        variant_skus: List of SKUs that belong to this group.
        subtitle: Optional subtitle.
    """
    body: dict = {
        "title": title,
        "description": description,
        "aspects": aspects,
        "imageUrls": image_urls,
        "variantSKUs": variant_skus,
    }
    if subtitle:
        body["subtitle"] = subtitle
    from .auth import auth_headers, get_base_url
    import requests
    url = get_base_url() + f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}"
    try:
        r = requests.put(url, headers=auth_headers(), json=body, timeout=30)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json() if r.text else {"status": "ok"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def delete_inventory_item_group(inventory_item_group_key: str) -> dict:
    """Delete an inventory item group by key."""
    return api_delete(f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


# ── Offers ───────────────────────────────────────────────────────────────────

@mcp.tool()
def get_offers(sku: str | None = None, marketplace_id: str | None = None,
               limit: int = 25, offset: int = 0) -> dict:
    """
    Retrieve offers, optionally filtered by SKU and/or marketplace.

    Args:
        sku: Filter by seller SKU.
        marketplace_id: eBay marketplace ID (e.g. EBAY_US).
        limit: Number of results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    return api_get("/sell/inventory/v1/offer", params=params)


@mcp.tool()
def get_offer(offer_id: str) -> dict:
    """Retrieve a single offer by offer ID."""
    return api_get(f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def create_offer(sku: str, marketplace_id: str, format: str,
                 listing_description: str, pricing_summary: dict,
                 category_id: str | None = None,
                 listing_policies: dict | None = None,
                 merchant_location_key: str | None = None,
                 tax: dict | None = None,
                 listing_duration: str | None = None) -> dict:
    """
    Create a new offer for an inventory item.

    Args:
        sku: SKU of the inventory item.
        marketplace_id: eBay marketplace (e.g. EBAY_US).
        format: Listing format (FIXED_PRICE or AUCTION).
        listing_description: HTML description for the listing.
        pricing_summary: Dict with price (value, currency).
        category_id: eBay category ID.
        listing_policies: Dict with fulfillmentPolicyId, paymentPolicyId, returnPolicyId.
        merchant_location_key: Key of the merchant location.
        tax: Tax information dict.
        listing_duration: Duration (e.g. GTC for Good Till Cancelled).
    """
    body: dict = {
        "sku": sku,
        "marketplaceId": marketplace_id,
        "format": format,
        "listingDescription": listing_description,
        "pricingSummary": pricing_summary,
    }
    if category_id:
        body["categoryId"] = category_id
    if listing_policies:
        body["listingPolicies"] = listing_policies
    if merchant_location_key:
        body["merchantLocationKey"] = merchant_location_key
    if tax:
        body["tax"] = tax
    if listing_duration:
        body["listingDuration"] = listing_duration
    return api_post("/sell/inventory/v1/offer", body=body)


@mcp.tool()
def update_offer(offer_id: str, listing_description: str | None = None,
                 pricing_summary: dict | None = None,
                 category_id: str | None = None,
                 listing_policies: dict | None = None,
                 merchant_location_key: str | None = None,
                 tax: dict | None = None) -> dict:
    """
    Update an existing offer.

    Args:
        offer_id: The offer ID to update.
        listing_description: New HTML description.
        pricing_summary: New pricing dict.
        category_id: New category ID.
        listing_policies: New listing policies dict.
        merchant_location_key: New merchant location key.
        tax: New tax information.
    """
    body: dict = {}
    if listing_description is not None:
        body["listingDescription"] = listing_description
    if pricing_summary is not None:
        body["pricingSummary"] = pricing_summary
    if category_id is not None:
        body["categoryId"] = category_id
    if listing_policies is not None:
        body["listingPolicies"] = listing_policies
    if merchant_location_key is not None:
        body["merchantLocationKey"] = merchant_location_key
    if tax is not None:
        body["tax"] = tax
    return api_put(f"/sell/inventory/v1/offer/{offer_id}", body=body)


@mcp.tool()
def delete_offer(offer_id: str) -> dict:
    """Delete an offer by offer ID."""
    return api_delete(f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def publish_offer(offer_id: str) -> dict:
    """Publish an offer to create or relist the corresponding eBay listing."""
    return api_post(f"/sell/inventory/v1/offer/{offer_id}/publish")


@mcp.tool()
def publish_offer_by_inventory_item_group(inventory_item_group_key: str,
                                          marketplace_id: str) -> dict:
    """
    Publish all offers associated with an inventory item group (multi-variation listing).

    Args:
        inventory_item_group_key: The group key.
        marketplace_id: eBay marketplace ID.
    """
    return api_post("/sell/inventory/v1/offer/publish_by_inventory_item_group",
                    body={"inventoryItemGroupKey": inventory_item_group_key,
                          "marketplaceId": marketplace_id})


@mcp.tool()
def withdraw_offer(offer_id: str) -> dict:
    """Withdraw (end) a published offer/listing."""
    return api_post(f"/sell/inventory/v1/offer/{offer_id}/withdraw")


@mcp.tool()
def bulk_create_offer(requests_list: list[dict]) -> dict:
    """
    Bulk create up to 25 offers in one call.

    Args:
        requests_list: List of offer creation request objects.
    """
    return api_post("/sell/inventory/v1/bulk_create_offer",
                    body={"requests": requests_list})


@mcp.tool()
def bulk_publish_offer(requests_list: list[dict]) -> dict:
    """
    Bulk publish up to 25 offers in one call.

    Args:
        requests_list: List of objects each containing offerId.
    """
    return api_post("/sell/inventory/v1/bulk_publish_offer",
                    body={"requests": requests_list})


@mcp.tool()
def get_listing_fees(offers: list[dict]) -> dict:
    """
    Retrieve estimated listing fees for one or more offers before publishing.

    Args:
        offers: List of objects each containing offerId.
    """
    return api_post("/sell/inventory/v1/offer/get_listing_fees",
                    body={"offers": offers})


# ── Inventory Locations ──────────────────────────────────────────────────────

@mcp.tool()
def get_inventory_location(merchant_location_key: str) -> dict:
    """Retrieve a merchant inventory location by key."""
    return api_get(f"/sell/inventory/v1/location/{merchant_location_key}")


@mcp.tool()
def get_inventory_locations(limit: int = 25, offset: int = 0) -> dict:
    """Retrieve all merchant inventory locations."""
    return api_get("/sell/inventory/v1/location",
                   params={"limit": limit, "offset": offset})


@mcp.tool()
def create_inventory_location(merchant_location_key: str, location: dict,
                               location_types: list[str],
                               name: str | None = None,
                               merchant_location_status: str | None = None) -> dict:
    """
    Create a new merchant inventory location.

    Args:
        merchant_location_key: Unique key for the location.
        location: Dict with address fields.
        location_types: List of location types (e.g. ['WAREHOUSE']).
        name: Human-readable name.
        merchant_location_status: ENABLED or DISABLED.
    """
    body: dict = {"location": location, "locationTypes": location_types}
    if name:
        body["name"] = name
    if merchant_location_status:
        body["merchantLocationStatus"] = merchant_location_status
    from .auth import auth_headers, get_base_url
    import requests
    url = get_base_url() + f"/sell/inventory/v1/location/{merchant_location_key}"
    try:
        r = requests.post(url, headers=auth_headers(), json=body, timeout=30)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json() if r.text else {"status": "ok"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def update_inventory_location(merchant_location_key: str,
                               name: str | None = None,
                               location: dict | None = None) -> dict:
    """
    Update details of an existing inventory location.

    Args:
        merchant_location_key: Key of the location to update.
        name: New name.
        location: New location address dict.
    """
    body: dict = {}
    if name:
        body["name"] = name
    if location:
        body["location"] = location
    return api_post(f"/sell/inventory/v1/location/{merchant_location_key}/update_location_details",
                    body=body)


@mcp.tool()
def delete_inventory_location(merchant_location_key: str) -> dict:
    """Delete a merchant inventory location."""
    return api_delete(f"/sell/inventory/v1/location/{merchant_location_key}")


@mcp.tool()
def enable_inventory_location(merchant_location_key: str) -> dict:
    """Enable a previously disabled inventory location."""
    return api_post(f"/sell/inventory/v1/location/{merchant_location_key}/enable")


@mcp.tool()
def disable_inventory_location(merchant_location_key: str) -> dict:
    """Disable an inventory location."""
    return api_post(f"/sell/inventory/v1/location/{merchant_location_key}/disable")
