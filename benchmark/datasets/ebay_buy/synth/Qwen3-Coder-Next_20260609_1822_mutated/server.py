#!/usr/bin/env python3
"""MCP Server for eBay Buy API"""

import os
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(name="ebay-buy-api")

# OAuth 2.0 Client Credentials grant endpoint
TOKEN_ENDPOINT = {
    "SANDBOX": "https://api.sandbox.ebay.com/identity/v1/oauth2/token",
    "PRODUCTION": "https://api.ebay.com/identity/v1/oauth2/token",
}

# Base URLs for API endpoints
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def get_environment() -> str:
    """Get eBay environment from environment variable or default to SANDBOX."""
    return os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()


def get_access_token() -> str:
    """Get OAuth 2.0 access token using client credentials grant."""
    env = get_environment()
    token_url = TOKEN_ENDPOINT[env]
    
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    
    if not app_id or not cert_id:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID environment variables must be set")
    
    payload = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    
    response = requests.post(
        token_url,
        auth=(app_id, cert_id),
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    response.raise_for_status()
    
    return response.json()["access_token"]


def make_ebay_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Make a request to the eBay Buy API."""
    env = get_environment()
    base_url = BASE_URLS[env]
    url = f"{base_url}{path}"
    
    # Get access token
    token = get_access_token()
    
    # Default headers
    default_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    # Merge headers
    if headers:
        default_headers.update(headers)
    
    # Make request
    response = requests.request(
        method=method,
        url=url,
        params=params,
        headers=default_headers,
    )
    
    # Handle errors gracefully
    try:
        data = response.json()
    except ValueError:
        data = {"error": f"Invalid JSON response: {response.text}"}
    
    if not response.ok:
        return {"error": f"HTTP {response.status_code}: {data.get('error', 'Unknown error')}"}
    
    return data


# Browse API - Item methods


@mcp.tool()
def get_item(listing_id: str) -> Dict[str, Any]:
    """Retrieve details of a specific item.
    
    Args:
        listing_id: The unique identifier of the item
        
    Returns:
        Item details including description, price, category, condition, etc.
    """
    path = f"/buy/v1/item/{listing_id}"
    return make_ebay_request("GET", path)


@mcp.tool()
def get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
) -> Dict[str, Any]:
    """Retrieve item details using a legacy item ID.
    
    Args:
        legacy_item_id: The legacy eBay item ID
        legacy_variation_id: Optional legacy variation ID for item groups
        fieldgroups: Comma-separated list of field groups (PRODUCT, ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS)
        
    Returns:
        Item details including RESTful item_id and legacy item details
    """
    path = "/buy/v1/item/get_item_by_legacy_id"
    params = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    
    return make_ebay_request("GET", path, params=params)


@mcp.tool()
def get_items(item_ids: str) -> Dict[str, Any]:
    """Retrieve details for multiple items using their item IDs.
    
    Args:
        item_ids: Comma-separated list of item IDs (up to 20 IDs)
        
    Returns:
        Dictionary containing items array with item details
    """
    path = "/buy/v1/item"
    params = {"item_ids": item_ids}
    return make_ebay_request("GET", path, params=params)


@mcp.tool()
def get_items_by_item_group(
    item_group_id: str,
    fieldgroups: Optional[str] = None,
) -> Dict[str, Any]:
    """Retrieve details about individual items in an item group.
    
    Args:
        item_group_id: The unique identifier of the item group
        fieldgroups: Comma-separated list of field groups (ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS)
        
    Returns:
        Item group details including items array and commonDescriptions
    """
    path = "/buy/v1/item/get_items_by_item_group"
    params = {"item_group_id": item_group_id}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    
    return make_ebay_request("GET", path, params=params)


@mcp.tool()
def search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    charity_ids: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
    order_by: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    delivery_country: Optional[str] = None,
    location: Optional[str] = None,
    max_distance: Optional[str] = None,
    pickup: Optional[str] = None,
    postal_code: Optional[str] = None,
    shipping_address: Optional[str] = None,
    shipping_option: Optional[str] = None,
    shipping_type: Optional[str] = None,
) -> Dict[str, Any]:
    """Search for eBay items by various query parameters.
    
    Args:
        q: Keyword search query
        category_ids: Comma-separated list of category IDs to search
        epid: eBay product ID
        gtin: Global Trade Item Number (UPC, EAN, ISBN)
        charity_ids: Comma-separated list of charity IDs
        fieldgroups: Comma-separated list of field groups
        limit: Maximum number of items to return (default: 20, max: 100)
        offset: Number of items to skip for pagination
        order_by: Sort order for results
        filter: Filter by field values
        aspect_filter: Filter by item aspects
        compatibility_filter: Filter by vehicle compatibility
        delivery_country: Filter by delivery country (2-digit ISO code)
        location: Filter by item location
        max_distance: Maximum distance for local pickup searches
        pickup: Local pickup options (SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, etc.)
        postal_code: Postal code for distance calculations
        shipping_address: Shipping address for delivery calculations
        shipping_option: Filter by shipping options
        shipping_type: Filter by shipping types
        
    Returns:
        Search results with item summaries
    """
    path = "/buy/v1/item_summary/search"
    params = {
        "limit": limit,
        "skip": offset,
    }
    
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if epid:
        params["epid"] = epid
    if gtin:
        params["gtin"] = gtin
    if charity_ids:
        params["charity_ids"] = charity_ids
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    if order_by:
        params["order_by"] = order_by
    if filter:
        params["filter"] = filter
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if compatibility_filter:
        params["compatibility_filter"] = compatibility_filter
    if delivery_country:
        params["delivery_country"] = delivery_country
    if location:
        params["location"] = location
    if max_distance:
        params["max_distance"] = max_distance
    if pickup:
        params["pickup"] = pickup
    if postal_code:
        params["postal_code"] = postal_code
    if shipping_address:
        params["shipping_address"] = shipping_address
    if shipping_option:
        params["shipping_option"] = shipping_option
    if shipping_type:
        params["shipping_type"] = shipping_type
    
    return make_ebay_request("GET", path, params=params)


@mcp.tool()
def search_items_by_image(
    image: str,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
    fieldgroups: Optional[str] = None,
) -> Dict[str, Any]:
    """Search for items using an image.
    
    Args:
        image: Base64-encoded image or URL to image
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
        fieldgroups: Comma-separated list of field groups
        
    Returns:
        Search results with item summaries
    """
    path = "/buy/v1/item_summary/search_by_image"
    params = {
        "image": image,
        "limit": limit,
        "skip": offset,
    }
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    
    return make_ebay_request("GET", path, params=params)


# Browse API - Compatibility check


@mcp.tool()
def check_compatibility(
    item_id: str,
    compatibility_properties: list,
) -> Dict[str, Any]:
    """Check if an item is compatible with specified properties.
    
    Args:
        item_id: The unique identifier of the item
        compatibility_properties: List of property name/value pairs to check compatibility
        
    Returns:
        Compatibility information for the item
    """
    path = f"/buy/v1/item/{item_id}/check_compatibility"
    payload = {"compatibilityProperties": compatibility_properties}
    
    return make_ebay_request("POST", path, json=payload)


# Deal API


@mcp.tool()
def get_events(
    marketplace_id: str,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
) -> Dict[str, Any]:
    """Retrieve paginated eBay events for a marketplace.
    
    Args:
        marketplace_id: The eBay marketplace ID
        limit: Maximum number of events to return (default: 20, max: 100)
        offset: Number of events to skip for pagination
        
    Returns:
        Event details including coupons, dates, and terms
    """
    path = "/buy/deal/v1/event"
    params = {
        "max_results": limit,
        "skip": offset,
    }
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, params=params, headers=headers)


@mcp.tool()
def get_event(event_id: str, marketplace_id: str) -> Dict[str, Any]:
    """Retrieve details for a specific eBay event.
    
    Args:
        event_id: The unique identifier of the event
        marketplace_id: The eBay marketplace ID
        
    Returns:
        Event details including applicable coupons, dates, and terms
    """
    path = f"/buy/deal/v1/event/{event_id}"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, headers=headers)


@mcp.tool()
def get_deal_items(
    marketplace_id: str,
    category_ids: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
) -> Dict[str, Any]:
    """Retrieve paginated deal items for a marketplace.
    
    Args:
        marketplace_id: The eBay marketplace ID
        category_ids: Comma-separated list of category IDs to filter
        commissionable: Filter by commissionable items (true/false)
        delivery_country: Filter by delivery country (2-digit ISO code)
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
        
    Returns:
        Deal items with pricing, shipping, and deal information
    """
    path = "/buy/deal/v1/deal_item"
    params = {
        "max_results": limit,
        "skip": offset,
    }
    if category_ids:
        params["category_ids"] = category_ids
    if commissionable is not None:
        params["commissionable"] = str(commissionable).lower()
    if delivery_country:
        params["delivery_country"] = delivery_country
    
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, params=params, headers=headers)


@mcp.tool()
def get_event_items(
    event_id: str,
    marketplace_id: str,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
) -> Dict[str, Any]:
    """Retrieve items for a specific event.
    
    Args:
        event_id: The unique identifier of the event
        marketplace_id: The eBay marketplace ID
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
        
    Returns:
        Event items with details
    """
    path = f"/buy/deal/v1/event/{event_id}/event_item"
    params = {
        "max_results": limit,
        "skip": offset,
    }
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, params=params, headers=headers)


# Feed API


@mcp.tool()
def get_item_feed(
    marketplace_id: str,
    feed_type: str = "SNAPSHOT",
    limit: Optional[int] = 100,
) -> Dict[str, Any]:
    """Retrieve a feed of item data.
    
    Args:
        marketplace_id: The eBay marketplace ID
        feed_type: Type of feed (SNAPSHOT or PRIORITY)
        limit: Maximum number of items per feed
        
    Returns:
        Item feed data
    """
    path = "/buy/feed/v1/item"
    params = {
        "feed_type": feed_type,
        "max_results": limit,
    }
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, params=params, headers=headers)


@mcp.tool()
def get_item_group_feed(
    marketplace_id: str,
    feed_type: str = "SNAPSHOT",
    limit: Optional[int] = 100,
) -> Dict[str, Any]:
    """Retrieve a feed of item group data.
    
    Args:
        marketplace_id: The eBay marketplace ID
        feed_type: Type of feed (SNAPSHOT or PRIORITY)
        limit: Maximum number of items per feed
        
    Returns:
        Item group feed data
    """
    path = "/buy/feed/v1/item_group"
    params = {
        "feed_type": feed_type,
        "max_results": limit,
    }
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, params=params, headers=headers)


@mcp.tool()
def get_item_priority_feed(
    marketplace_id: str,
    limit: Optional[int] = 100,
) -> Dict[str, Any]:
    """Retrieve a priority feed of item data.
    
    Args:
        marketplace_id: The eBay marketplace ID
        limit: Maximum number of items per feed
        
    Returns:
        Priority feed data
    """
    path = "/buy/feed/v1/item_priority"
    params = {
        "max_results": limit,
    }
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, params=params, headers=headers)


@mcp.tool()
def get_item_snapshot_feed(
    marketplace_id: str,
    limit: Optional[int] = 100,
) -> Dict[str, Any]:
    """Retrieve a snapshot feed of item data.
    
    Args:
        marketplace_id: The eBay marketplace ID
        limit: Maximum number of items per feed
        
    Returns:
        Snapshot feed data
    """
    path = "/buy/feed/v1/item_snapshot"
    params = {
        "max_results": limit,
    }
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, params=params, headers=headers)


# Marketing API


@mcp.tool()
def get_merchandised_products(
    marketplace_id: str,
    item_id: str,
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
) -> Dict[str, Any]:
    """Retrieve merchandised products related to an item.
    
    Args:
        marketplace_id: The eBay marketplace ID
        item_id: The item ID to get related products for
        limit: Maximum number of products to return (default: 10)
        offset: Number of products to skip for pagination
        
    Returns:
        Related products information
    """
    path = f"/buy/marketing/v1/item/{item_id}/merchandised_products"
    params = {
        "max_results": limit,
        "skip": offset,
    }
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, params=params, headers=headers)


# Offer API


@mcp.tool()
def get_bidding(item_id: str, marketplace_id: str) -> Dict[str, Any]:
    """Retrieve bidding information for an item.
    
    Args:
        item_id: The unique identifier of the item
        marketplace_id: The eBay marketplace ID
        
    Returns:
        Bidding information including bid count and current bid price
    """
    path = f"/buy/offer/v1/item/{item_id}/bidding"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, headers=headers)


@mcp.tool()
def place_proxy_bid(
    item_id: str,
    marketplace_id: str,
    bid_amount: Dict[str, Any],
) -> Dict[str, Any]:
    """Place a proxy bid on an item.
    
    Args:
        item_id: The unique identifier of the item
        marketplace_id: The eBay marketplace ID
        bid_amount: Object containing value and currency for the bid amount
        
    Returns:
        Bid placement confirmation
    """
    path = f"/buy/offer/v1/item/{item_id}/bidding/place_proxy_bid"
    payload = {"bidAmount": bid_amount}
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    
    return make_ebay_request("POST", path, json=payload, headers=headers)


# Order API - Guest Checkout


@mcp.tool()
def initiate_guest_checkout_session(
    marketplace_id: str,
    guest_checkout_session: Dict[str, Any],
) -> Dict[str, Any]:
    """Initiate a guest checkout session.
    
    Args:
        marketplace_id: The eBay marketplace ID
        guest_checkout_session: Session details including lineItems and shippingAddress
        
    Returns:
        Guest checkout session details
    """
    path = "/buy/order/v1/guest_checkout_session"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("POST", path, json=guest_checkout_session, headers=headers)


@mcp.tool()
def get_guest_checkout_session(session_id: str, marketplace_id: str) -> Dict[str, Any]:
    """Retrieve details of a guest checkout session.
    
    Args:
        session_id: The unique identifier of the guest checkout session
        marketplace_id: The eBay marketplace ID
        
    Returns:
        Guest checkout session details
    """
    path = f"/buy/order/v1/guest_checkout_session/{session_id}"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, headers=headers)


@mcp.tool()
def update_guest_shipping_address(
    session_id: str,
    marketplace_id: str,
    shipping_address: Dict[str, Any],
) -> Dict[str, Any]:
    """Update the shipping address for a guest checkout session.
    
    Args:
        session_id: The unique identifier of the guest checkout session
        marketplace_id: The eBay marketplace ID
        shipping_address: New shipping address details
        
    Returns:
        Updated guest checkout session
    """
    path = f"/buy/order/v1/guest_checkout_session/{session_id}/shipping_address"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("PUT", path, json=shipping_address, headers=headers)


@mcp.tool()
def update_guest_shipping_option(
    session_id: str,
    marketplace_id: str,
    shipping_option: Dict[str, Any],
) -> Dict[str, Any]:
    """Update the shipping option for a guest checkout session.
    
    Args:
        session_id: The unique identifier of the guest checkout session
        marketplace_id: The eBay marketplace ID
        shipping_option: New shipping option details
        
    Returns:
        Updated guest checkout session
    """
    path = f"/buy/order/v1/guest_checkout_session/{session_id}/shipping_option"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("PUT", path, json=shipping_option, headers=headers)


@mcp.tool()
def update_guest_quantity(
    session_id: str,
    marketplace_id: str,
    quantity: Dict[str, Any],
) -> Dict[str, Any]:
    """Update the quantity of an item in a guest checkout session.
    
    Args:
        session_id: The unique identifier of the guest checkout session
        marketplace_id: The eBay marketplace ID
        quantity: Object containing lineItemId and quantity
        
    Returns:
        Updated guest checkout session
    """
    path = f"/buy/order/v1/guest_checkout_session/{session_id}/quantity"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("PUT", path, json=quantity, headers=headers)


@mcp.tool()
def apply_guest_coupon(
    session_id: str,
    marketplace_id: str,
    coupon: Dict[str, Any],
) -> Dict[str, Any]:
    """Apply a coupon to a guest checkout session.
    
    Args:
        session_id: The unique identifier of the guest checkout session
        marketplace_id: The eBay marketplace ID
        coupon: Object containing coupon code
        
    Returns:
        Updated guest checkout session
    """
    path = f"/buy/order/v1/guest_checkout_session/{session_id}/coupon"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("POST", path, json=coupon, headers=headers)


@mcp.tool()
def remove_guest_coupon(
    session_id: str,
    marketplace_id: str,
    coupon_code: str,
) -> Dict[str, Any]:
    """Remove a coupon from a guest checkout session.
    
    Args:
        session_id: The unique identifier of the guest checkout session
        marketplace_id: The eBay marketplace ID
        coupon_code: The coupon code to remove
        
    Returns:
        Updated guest checkout session
    """
    path = f"/buy/order/v1/guest_checkout_session/{session_id}/coupon/{coupon_code}"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("DELETE", path, headers=headers)


@mcp.tool()
def get_guest_purchase_order(
    guest_purchase_order_id: str,
    marketplace_id: str,
) -> Dict[str, Any]:
    """Retrieve details of a guest purchase order.
    
    Args:
        guest_purchase_order_id: The unique identifier of the guest purchase order
        marketplace_id: The eBay marketplace ID
        
    Returns:
        Guest purchase order details
    """
    path = f"/buy/order/v1/guest_purchase_order/{guest_purchase_order_id}"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    
    return make_ebay_request("GET", path, headers=headers)


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
