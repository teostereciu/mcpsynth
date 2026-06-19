#!/usr/bin/env python3
"""
eBay Buy API MCP Server

An MCP server with comprehensive coverage of the eBay Buy API,
suitable for use by an autonomous agent completing real-world tasks.
"""

import os
import requests
from typing import Any

from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("ebay-buy-api")

# Configuration
EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

# Global token cache
_access_token = None
_token_expiry = None


def get_base_url() -> str:
    """Get the base URL based on environment."""
    return BASE_URLS.get(EBAY_ENVIRONMENT, BASE_URLS["SANDBOX"])


def get_access_token() -> str:
    """Get OAuth 2.0 access token using Client Credentials grant."""
    global _access_token, _token_expiry
    
    # Check if we have a valid cached token
    if _access_token and _token_expiry and _token_expiry > __import__('time').time():
        return _access_token
    
    # Get new token
    token_url = "https://api.ebay.com/oauth/api_token"
    auth = (EBAY_APP_ID, EBAY_CERT_ID)
    
    response = requests.post(
        token_url,
        auth=auth,
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope"
        }
    )
    
    if response.status_code != 200:
        raise Exception(f"Failed to get access token: {response.status_code} - {response.text}")
    
    data = response.json()
    _access_token = data.get("access_token")
    # Cache token for 4 minutes (tokens expire in 2 hours, but we refresh early)
    _token_expiry = __import__('time').time() + 240
    
    return _access_token


def make_request(method: str, path: str, params: dict = None, 
                 body: dict = None) -> dict:
    """Make a request to the eBay API."""
    url = f"{get_base_url()}{path}"
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json",
    }
    
    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        params=params,
        json=body
    )
    
    if response.status_code >= 200 and response.status_code < 300:
        if response.content:
            return response.json()
        return {}
    
    # Handle errors gracefully
    error_msg = f"API request failed with status {response.status_code}"
    if response.content:
        try:
            error_data = response.json()
            error_msg = f"{error_msg}: {error_data}"
        except:
            error_msg = f"{error_msg}: {response.text}"
    return {"error": error_msg}


# Browse API - Item Methods


@mcp.tool()
def check_compatibility(
    item_id: str,
    compatibility_properties: list
) -> dict:
    """
    Checks if a product (such as a car, truck, or motorcycle) is compatible 
    with a specific item listed on eBay.
    
    Args:
        item_id: The eBay RESTful identifier of the item (the part being checked)
        compatibility_properties: List of attribute name/value pairs defining 
                                 the product (e.g., [{"name": "Year", "value": "2019"}, 
                                 {"name": "Make", "value": "BMW"}])
    
    Returns:
        Compatibility status (COMPATIBLE, NOT_COMPATIBLE, or UNDETERMINED) 
        or error dict
    """
    path = f"/buy/browse/v1/item/{item_id}/check_compatibility"
    body = {"compatibilityProperties": compatibility_properties}
    return make_request("POST", path, body=body)


@mcp.tool()
def get_item(item_id: str) -> dict:
    """
    Retrieves the details of a specific item, such as description, price, 
    category, all item aspects, condition, return policies, seller feedback 
    and score, shipping options, shipping costs, estimated delivery, and 
    other information the buyer needs to make a purchasing decision.
    
    Args:
        item_id: The eBay RESTful identifier of the item (ePID format or legacy ID)
    
    Returns:
        Detailed item information or error dict
    """
    path = f"/buy/browse/v1/item/{item_id}"
    return make_request("GET", path)


@mcp.tool()
def get_items(item_ids: list) -> dict:
    """
    Retrieves the details about specific items that buyers need to make a 
    purchasing decision. This is a Limited Release method available only to 
    select Partners.
    
    Args:
        item_ids: List of eBay item identifiers (RESTful or legacy IDs)
    
    Returns:
        Item details for the requested items or error dict
    """
    params = {"item_ids": ",".join(item_ids)}
    path = "/buy/browse/v1/item"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_item_by_legacy_id(legacy_item_id: str) -> dict:
    """
    Retrieves the details of a specific item using the traditional/legacy 
    eBay item ID.
    
    Args:
        legacy_item_id: The traditional eBay item ID
    
    Returns:
        Item details or error dict
    """
    params = {"legacy_item_id": legacy_item_id}
    path = "/buy/browse/v1/item/get_item_by_legacy_id"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_items_by_item_group(item_group_id: str) -> dict:
    """
    Retrieves all items in an item group (items with variations like color, 
    size, etc.).
    
    Args:
        item_group_id: The unique identifier of an item group
    
    Returns:
        List of items in the group or error dict
    """
    params = {"item_group_id": item_group_id}
    path = "/buy/browse/v1/item/get_items_by_item_group"
    return make_request("GET", path, params=params)


@mcp.tool()
def search_items(
    q: str = None,
    limit: int = 10,
    offset: int = 0,
    category_ids: list = None,
    gtin: str = None,
    epid: str = None,
    charity_ids: list = None,
    auto_correct: str = None,
    filter: list = None,
    aspect_filter: dict = None,
    sort: str = None
) -> dict:
    """
    Searches for eBay items by various query parameters and retrieves summaries 
    of the items. Supports keyword search, category search, product search by 
    ePID or GTIN, and more.
    
    Args:
        q: Keyword search query (max 100 characters)
        limit: Maximum number of items to return (max 100)
        offset: Number of items to skip for pagination
        category_ids: List of category IDs to filter results
        gtin: Global Trade Item Number (UPC, EAN, ISBN)
        epid: eBay Product ID from the eBay product catalog
        charity_ids: List of charity IDs to filter results
        auto_correct: Set to 'KEYWORD' for auto-correction
        filter: List of field filters (e.g., 'price:[10..50]')
        aspect_filter: Dictionary of aspect filters (e.g., {'Color': 'Red'})
        sort: Sort order (e.g., 'price', '-price', 'newlyListed')
    
    Returns:
        Search results with item summaries or error dict
    """
    params = {
        "limit": str(limit),
        "offset": str(offset),
    }
    
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = ",".join(category_ids)
    if gtin:
        params["gtin"] = gtin
    if epid:
        params["epid"] = epid
    if charity_ids:
        params["charity_ids"] = ",".join(charity_ids)
    if auto_correct:
        params["auto_correct"] = auto_correct
    if filter:
        params["filter"] = ",".join(filter)
    if aspect_filter:
        # Convert dict to comma-separated key:value pairs
        aspect_pairs = [f"{k}:{{{v}}}" if isinstance(v, str) else f"{k}:{{{','.join(v)}}}" 
                       for k, v in aspect_filter.items()]
        params["aspect_filter"] = ",".join(aspect_pairs)
    if sort:
        params["sort"] = sort
    
    path = "/buy/browse/v1/item_summary/search"
    return make_request("GET", path, params=params)


@mcp.tool()
def search_items_by_image(
    image: str,
    limit: int = 10,
    offset: int = 0,
    category_ids: list = None,
    filter: list = None,
    aspect_filter: dict = None
) -> dict:
    """
    Searches for items using an image as the search query.
    
    Args:
        image: Base64-encoded image or image URL
        limit: Maximum number of items to return (max 100)
        offset: Number of items to skip for pagination
        category_ids: List of category IDs to filter results
        filter: List of field filters
        aspect_filter: Dictionary of aspect filters
    
    Returns:
        Search results with item summaries or error dict
    """
    params = {
        "limit": str(limit),
        "offset": str(offset),
    }
    
    if category_ids:
        params["category_ids"] = ",".join(category_ids)
    if filter:
        params["filter"] = ",".join(filter)
    if aspect_filter:
        aspect_pairs = [f"{k}:{{{v}}}" if isinstance(v, str) else f"{k}:{{{','.join(v)}}}" 
                       for k, v in aspect_filter.items()]
        params["aspect_filter"] = ",".join(aspect_pairs)
    
    path = "/buy/browse/v1/item_summary/search_by_image"
    return make_request("POST", path, params=params, body={"image": image})


# Deal API


@mcp.tool()
def get_events(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves all active deals events.
    
    Args:
        limit: Maximum number of events to return (max 100)
        offset: Number of events to skip for pagination
    
    Returns:
        List of deals events or error dict
    """
    params = {
        "limit": str(limit),
        "offset": str(offset),
    }
    path = "/buy/deal/v1/event"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_event(event_id: str) -> dict:
    """
    Retrieves details of a specific deals event.
    
    Args:
        event_id: The unique identifier of the event
    
    Returns:
        Event details or error dict
    """
    path = f"/buy/deal/v1/event/{event_id}"
    return make_request("GET", path)


@mcp.tool()
def get_event_items(
    event_ids: list,
    limit: int = 10,
    offset: int = 0
) -> dict:
    """
    Retrieves all items in one or more specific deals events.
    
    Args:
        event_ids: List of event IDs
        limit: Maximum number of items to return (max 100)
        offset: Number of items to skip for pagination
    
    Returns:
        List of items in the events or error dict
    """
    params = {
        "event_ids": ",".join(event_ids),
        "limit": str(limit),
        "offset": str(offset),
    }
    path = "/buy/deal/v1/event_item"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_deal_items(
    category_ids: list = None,
    limit: int = 10,
    offset: int = 0
) -> dict:
    """
    Retrieves all items in active deals.
    
    Args:
        category_ids: List of category IDs to filter results
        limit: Maximum number of items to return (max 100)
        offset: Number of items to skip for pagination
    
    Returns:
        List of deal items or error dict
    """
    params = {
        "limit": str(limit),
        "offset": str(offset),
    }
    
    if category_ids:
        params["category_ids"] = ",".join(category_ids)
    
    path = "/buy/deal/v1/deal_item"
    return make_request("GET", path, params=params)


# Feed API


@mcp.tool()
def get_item_feed(
    feed_scope: str,
    category_id: str = None,
    date: str = None,
    limit: int = 10,
    offset: int = 0
) -> dict:
    """
    Retrieves a feed of items based on the specified feed scope.
    
    Args:
        feed_scope: The type of feed (NEWLY_LISTED, PRICE_CHANGED, etc.)
        category_id: Category ID to filter the feed
        date: Date in YYYYMMDD format for the feed
        limit: Maximum number of items to return (max 100)
        offset: Number of items to skip for pagination
    
    Returns:
        Feed data or error dict
    """
    params = {
        "feed_scope": feed_scope,
        "limit": str(limit),
        "offset": str(offset),
    }
    
    if category_id:
        params["category_id"] = category_id
    if date:
        params["date"] = date
    
    path = "/buy/feed/v1_beta/item"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_item_group_feed(
    feed_scope: str,
    category_id: str = None,
    date: str = None,
    limit: int = 10,
    offset: int = 0
) -> dict:
    """
    Retrieves a feed of item groups based on the specified feed scope.
    
    Args:
        feed_scope: The type of feed
        category_id: Category ID to filter the feed
        date: Date in YYYYMMDD format for the feed
        limit: Maximum number of items to return (max 100)
        offset: Number of items to skip for pagination
    
    Returns:
        Feed data or error dict
    """
    params = {
        "feed_scope": feed_scope,
        "limit": str(limit),
        "offset": str(offset),
    }
    
    if category_id:
        params["category_id"] = category_id
    if date:
        params["date"] = date
    
    path = "/buy/feed/v1_beta/item_group"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_item_priority_feed(
    category_id: str,
    date: str = None,
    limit: int = 10,
    offset: int = 0
) -> dict:
    """
    Retrieves a feed of items that should have priority.
    
    Args:
        category_id: Category ID to filter the feed
        date: Date in YYYYMMDD format for the feed
        limit: Maximum number of items to return (max 100)
        offset: Number of items to skip for pagination
    
    Returns:
        Feed data or error dict
    """
    params = {
        "category_id": category_id,
        "limit": str(limit),
        "offset": str(offset),
    }
    
    if date:
        params["date"] = date
    
    path = "/buy/feed/v1_beta/item_priority"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    limit: int = 10,
    offset: int = 0
) -> dict:
    """
    Retrieves a feed of item snapshots for a specific date.
    
    Args:
        category_id: Category ID to filter the feed
        snapshot_date: Date in YYYY-MM-DD format for the snapshot
        limit: Maximum number of items to return (max 100)
        offset: Number of items to skip for pagination
    
    Returns:
        Feed data or error dict
    """
    params = {
        "category_id": category_id,
        "snapshot_date": snapshot_date,
        "limit": str(limit),
        "offset": str(offset),
    }
    
    path = "/buy/feed/v1_beta/item_snapshot"
    return make_request("GET", path, params=params)


# Marketing API


@mcp.tool()
def get_merchandised_products(
    category_id: str,
    metric_name: str = "BEST_SELLING",
    aspect_filter: dict = None,
    limit: int = 10,
    offset: int = 0
) -> dict:
    """
    Retrieves products that are being merchandised on eBay based on the 
    specified metric.
    
    Args:
        category_id: Category ID to filter products
        metric_name: Metric to use (BEST_SELLING, BEST_MATCH, etc.)
        aspect_filter: Dictionary of aspect filters
        limit: Maximum number of products to return (max 100)
        offset: Number of products to skip for pagination
    
    Returns:
        Merchandised products or error dict
    """
    params = {
        "category_id": category_id,
        "metric_name": metric_name,
        "limit": str(limit),
        "offset": str(offset),
    }
    
    if aspect_filter:
        aspect_pairs = [f"{k}:{{{v}}}" if isinstance(v, str) else f"{k}:{{{','.join(v)}}}" 
                       for k, v in aspect_filter.items()]
        params["aspect_filter"] = ",".join(aspect_pairs)
    
    path = "/buy/marketing/v1_beta/merchandised_product"
    return make_request("GET", path, params=params)


# Offer API - Bidding


@mcp.tool()
def get_bidding(item_id: str) -> dict:
    """
    Retrieves bidding information for an auction item.
    
    Args:
        item_id: The eBay item ID
    
    Returns:
        Bidding information or error dict
    """
    path = f"/buy/offer/v1_beta/bidding/{item_id}"
    return make_request("GET", path)


@mcp.tool()
def place_proxy_bid(item_id: str, max_amount: float, currency: str = "USD") -> dict:
    """
    Places a proxy bid on behalf of a buyer for an auction item.
    
    Args:
        item_id: The eBay item ID
        max_amount: Maximum bid amount
        currency: Currency code (default: USD)
    
    Returns:
        Bid placement result or error dict
    """
    path = f"/buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid"
    body = {
        "maxAmount": {
            "currency": currency,
            "value": str(max_amount)
        }
    }
    return make_request("POST", path, body=body)


# Order API - Guest Checkout


@mcp.tool()
def initiate_guest_checkout_session(
    email: str,
    items: list,
    shipping_address: dict = None,
    shipping_option: dict = None,
    coupon_codes: list = None
) -> dict:
    """
    Initiates a guest checkout session.
    
    Args:
        email: Guest buyer's email address
        items: List of items to purchase with quantity and item_id
        shipping_address: Shipping address details
        shipping_option: Shipping option selection
        coupon_codes: List of coupon codes
    
    Returns:
        Guest checkout session details or error dict
    """
    body = {
        "email": email,
        "items": items,
    }
    
    if shipping_address:
        body["shippingAddress"] = shipping_address
    if shipping_option:
        body["shippingOption"] = shipping_option
    if coupon_codes:
        body["couponCodes"] = coupon_codes
    
    path = "/buy/order/v2/guest_checkout_session/initiate"
    return make_request("POST", path, body=body)


@mcp.tool()
def get_guest_checkout_session(session_id: str) -> dict:
    """
    Retrieves details of a guest checkout session.
    
    Args:
        session_id: The guest checkout session ID
    
    Returns:
        Session details or error dict
    """
    path = f"/buy/order/v2/guest_checkout_session/{session_id}"
    return make_request("GET", path)


@mcp.tool()
def update_guest_shipping_address(
    session_id: str,
    shipping_address: dict
) -> dict:
    """
    Updates the shipping address for a guest checkout session.
    
    Args:
        session_id: The guest checkout session ID
        shipping_address: New shipping address details
    
    Returns:
        Updated session details or error dict
    """
    path = f"/buy/order/v2/guest_checkout_session/{session_id}/update_shipping_address"
    return make_request("POST", path, body={"shippingAddress": shipping_address})


@mcp.tool()
def update_guest_shipping_option(
    session_id: str,
    shipping_option: dict
) -> dict:
    """
    Updates the shipping option for a guest checkout session.
    
    Args:
        session_id: The guest checkout session ID
        shipping_option: New shipping option details
    
    Returns:
        Updated session details or error dict
    """
    path = f"/buy/order/v2/guest_checkout_session/{session_id}/update_shipping_option"
    return make_request("POST", path, body={"shippingOption": shipping_option})


@mcp.tool()
def update_guest_quantity(
    session_id: str,
    items: list
) -> dict:
    """
    Updates item quantities in a guest checkout session.
    
    Args:
        session_id: The guest checkout session ID
        items: List of items with updated quantities
    
    Returns:
        Updated session details or error dict
    """
    path = f"/buy/order/v2/guest_checkout_session/{session_id}/update_quantity"
    return make_request("POST", path, body={"items": items})


@mcp.tool()
def apply_guest_coupon(
    session_id: str,
    coupon_code: str
) -> dict:
    """
    Applies a coupon to a guest checkout session.
    
    Args:
        session_id: The guest checkout session ID
        coupon_code: Coupon code to apply
    
    Returns:
        Updated session details or error dict
    """
    path = f"/buy/order/v2/guest_checkout_session/{session_id}/apply_coupon"
    return make_request("POST", path, body={"couponCode": coupon_code})


@mcp.tool()
def remove_guest_coupon(
    session_id: str,
    coupon_code: str
) -> dict:
    """
    Removes a coupon from a guest checkout session.
    
    Args:
        session_id: The guest checkout session ID
        coupon_code: Coupon code to remove
    
    Returns:
        Updated session details or error dict
    """
    path = f"/buy/order/v2/guest_checkout_session/{session_id}/remove_coupon"
    return make_request("POST", path, body={"couponCode": coupon_code})


@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str) -> dict:
    """
    Retrieves details of a guest purchase order.
    
    Args:
        purchase_order_id: The guest purchase order ID
    
    Returns:
        Purchase order details or error dict
    """
    path = f"/buy/order/v2/guest_purchase_order/{purchase_order_id}"
    return make_request("GET", path)


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
