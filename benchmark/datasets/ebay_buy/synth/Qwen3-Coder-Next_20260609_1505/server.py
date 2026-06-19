#!/usr/bin/env python3
"""
eBay Buy API MCP Server
An MCP server for interacting with the eBay Buy API
"""

import os
import base64
import requests
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(name="ebay-buy-api")

# Environment variables
EBAY_APP_ID = os.getenv("EBAY_APP_ID")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com"
}

EBAY_BASE_URL = BASE_URLS.get(EBAY_ENVIRONMENT, BASE_URLS["SANDBOX"])

# OAuth token endpoint
OAUTH_TOKEN_URL = "https://api.sandbox.ebay.com/oauth2/token"

# Scopes
SCOPES = {
    "browse": ["https://api.ebay.com/oauth/api_scope"],
    "deal": ["https://api.ebay.com/oauth/api_scope/buy.deal"],
    "feed": ["https://api.ebay.com/oauth/api_scope/buy.item.feed"],
    "marketing": ["https://api.ebay.com/oauth/api_scope/buy.marketing"],
    "offer": ["https://api.ebay.com/oauth/api_scope/buy.offer"],
    "order": ["https://api.ebay.com/oauth/api_scope/buy.guest.order"]
}


def get_access_token():
    """Get OAuth access token using client credentials grant"""
    try:
        response = requests.post(
            OAUTH_TOKEN_URL,
            auth=(EBAY_APP_ID, EBAY_CERT_ID),
            data={
                "grant_type": "client_credentials",
                "scope": " ".join(SCOPES["browse"] + SCOPES["deal"] + 
                                 SCOPES["feed"] + SCOPES["marketing"] + 
                                 SCOPES["offer"] + SCOPES["order"])
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.raise_for_status()
        return response.json()["access_token"]
    except Exception as e:
        return {"error": f"Failed to get access token: {str(e)}"}


def make_request(method, path, params=None, headers=None, data=None):
    """Make a request to the eBay API"""
    access_token = get_access_token()
    if isinstance(access_token, dict) and "error" in access_token:
        return access_token
    
    url = f"{EBAY_BASE_URL}{path}"
    
    default_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    if headers:
        default_headers.update(headers)
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            headers=default_headers,
            json=data
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        else:
            return {
                "error": f"API request failed with status code {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


# Browse API - Get Item
@mcp.tool()
def get_item(item_id: str, field_groups: str = None) -> dict:
    """
    Get detailed information about a specific eBay item.
    
    Args:
        item_id: The eBay-assigned unique identifier of the item (RESTful format)
        field_groups: Optional field groups to include (COMPACT, PRODUCT, ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS)
    
    Returns:
        Item details including description, price, category, shipping options, etc.
    """
    params = {}
    if field_groups:
        params["fieldgroups"] = field_groups
    
    path = f"/buy/browse/v1/item/{item_id}"
    return make_request("GET", path, params=params)


# Browse API - Get Items by Item Group
@mcp.tool()
def get_items_by_item_group(item_group_id: str, field_groups: str = None) -> dict:
    """
    Get items from a specific item group.
    
    Args:
        item_group_id: The unique identifier of the item group
        field_groups: Optional field groups to include
    
    Returns:
        List of items in the specified item group
    """
    params = {}
    if field_groups:
        params["fieldgroups"] = field_groups
    
    path = f"/buy/browse/v1/item/{item_group_id}/items_by_item_group"
    return make_request("GET", path, params=params)


# Browse API - Get Item By Legacy ID
@mcp.tool()
def get_item_by_legacy_id(legacy_item_id: str) -> dict:
    """
    Get item details using the legacy eBay item ID.
    
    Args:
        legacy_item_id: The traditional eBay item ID (numeric)
    
    Returns:
        Item details
    """
    path = f"/buy/browse/v1/item/get_item_by_legacy_id?legacy_item_id={legacy_item_id}"
    return make_request("GET", path)


# Browse API - Search Items
@mcp.tool()
def search_items(
    q: str = None,
    category_ids: str = None,
    limit: int = 10,
    offset: int = 0,
    sort: str = "best_match",
    field_groups: str = None,
    filter: str = None,
    aspect_filter: str = None,
    compatibility_filter: str = None,
    charity_ids: str = None
) -> dict:
    """
    Search for eBay items by various query parameters.
    
    Args:
        q: Search keywords
        category_ids: Comma-separated category IDs to search in
        limit: Maximum number of items to return (default: 10, max: 100)
        offset: Number of items to skip for pagination
        sort: Sort order (best_match, price_plus_shipping_lowest, price_plus_shipping_highest, newly_listed)
        field_groups: Field groups to include (ASPECT_REFINEMENTS, EXTENDED)
        filter: Filter expressions
        aspect_filter: Aspect-based filters
        compatibility_filter: Product compatibility filters
        charity_ids: Charity IDs to filter by
    
    Returns:
        Search results with item summaries
    """
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if sort:
        params["sort"] = sort
    if field_groups:
        params["fieldgroups"] = field_groups
    if filter:
        params["filter"] = filter
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if compatibility_filter:
        params["compatibility_filter"] = compatibility_filter
    if charity_ids:
        params["charity_ids"] = charity_ids
    
    path = "/buy/browse/v1/item_summary/search"
    return make_request("GET", path, params=params)


# Browse API - Search by Image
@mcp.tool()
def search_items_by_image(
    image_base64: str,
    limit: int = 10,
    offset: int = 0,
    category_ids: str = None,
    filter: str = None,
    aspect_filter: str = None
) -> dict:
    """
    Search for eBay items using an image.
    
    Args:
        image_base64: Base64-encoded image to search with
        limit: Maximum number of items to return (default: 10, max: 100)
        offset: Number of items to skip for pagination
        category_ids: Comma-separated category IDs to search in
        filter: Filter expressions
        aspect_filter: Aspect-based filters
    
    Returns:
        Search results with item summaries
    """
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    
    data = {"image": image_base64}
    
    path = "/buy/browse/v1/item_summary/search_by_image"
    return make_request("POST", path, params=params, data=data)


# Browse API - Check Compatibility
@mcp.tool()
def check_compatibility(item_id: str, product_id: str = None, product_id_type: str = None) -> dict:
    """
    Check if an item is compatible with a specific product.
    
    Args:
        item_id: The eBay item ID
        product_id: The product ID (EPID, ePID, or GTIN)
        product_id_type: Type of product ID (EPID, ePID, or GTIN)
    
    Returns:
        Compatibility information
    """
    params = {}
    if product_id:
        params["product_id"] = product_id
    if product_id_type:
        params["product_id_type"] = product_id_type
    
    path = f"/buy/browse/v1/item/{item_id}/check_compatibility"
    return make_request("GET", path, params=params)


# Deal API - Get Events
@mcp.tool()
def get_events(
    limit: int = 20,
    offset: int = 0
) -> dict:
    """
    Retrieve a list of active eBay events.
    
    Args:
        limit: Maximum number of events to return (default: 20, max: 100)
        offset: Number of events to skip for pagination
    
    Returns:
        List of events with details
    """
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    
    path = "/buy/deal/v1/event"
    return make_request("GET", path, params=params)


# Deal API - Get Event
@mcp.tool()
def get_event(event_id: str) -> dict:
    """
    Get details of a specific eBay event.
    
    Args:
        event_id: The unique identifier of the event
    
    Returns:
        Event details
    """
    path = f"/buy/deal/v1/event/{event_id}"
    return make_request("GET", path)


# Deal API - Get Deal Items
@mcp.tool()
def get_deal_items(
    category_ids: str = None,
    commissionable: str = None,
    delivery_country: str = None,
    limit: int = 20,
    offset: int = 0
) -> dict:
    """
    Retrieve a list of deal items.
    
    Args:
        category_ids: Comma-separated category IDs to filter by
        commissionable: Filter by commissionable items (true/false)
        delivery_country: Filter by delivery country (2-letter ISO code)
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
    
    Returns:
        List of deal items
    """
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    
    if category_ids:
        params["category_ids"] = category_ids
    if commissionable:
        params["commissionable"] = commissionable
    if delivery_country:
        params["delivery_country"] = delivery_country
    
    path = "/buy/deal/v1/deal_item"
    return make_request("GET", path, params=params)


# Deal API - Get Event Items
@mcp.tool()
def get_event_items(
    event_id: str,
    limit: int = 20,
    offset: int = 0
) -> dict:
    """
    Get items associated with a specific event.
    
    Args:
        event_id: The unique identifier of the event
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
    
    Returns:
        List of items in the event
    """
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    
    path = f"/buy/deal/v1/event/{event_id}/event_item"
    return make_request("GET", path, params=params)


# Feed API - Get Item Feed
@mcp.tool()
def get_item_feed(
    feed_scope: str,
    category_id: str = None,
    start_date: str = None
) -> dict:
    """
    Download an item feed file (TSV_GZIP format).
    
    Args:
        feed_scope: Feed scope (NEWLY_LISTED or ALL_ACTIVE)
        category_id: Category ID to filter by
        start_date: Start date for the feed (YYYY-MM-DD)
    
    Returns:
        Feed file download information
    """
    params = {"feed_scope": feed_scope}
    
    if category_id:
        params["category_id"] = category_id
    if start_date:
        params["start_date"] = start_date
    
    path = "/buy/feed/v1/item/feed"
    return make_request("GET", path, params=params)


# Feed API - Get Item Group Feed
@mcp.tool()
def get_item_group_feed(
    feed_scope: str,
    category_id: str = None,
    start_date: str = None
) -> dict:
    """
    Download an item group feed file (TSV_GZIP format).
    
    Args:
        feed_scope: Feed scope (NEWLY_LISTED or ALL_ACTIVE)
        category_id: Category ID to filter by
        start_date: Start date for the feed (YYYY-MM-DD)
    
    Returns:
        Feed file download information
    """
    params = {"feed_scope": feed_scope}
    
    if category_id:
        params["category_id"] = category_id
    if start_date:
        params["start_date"] = start_date
    
    path = "/buy/feed/v1/item_group/feed"
    return make_request("GET", path, params=params)


# Feed API - Get Item Priority Feed
@mcp.tool()
def get_item_priority_feed(
    feed_scope: str,
    start_date: str = None
) -> dict:
    """
    Download an item priority feed file (TSV_GZIP format).
    
    Args:
        feed_scope: Feed scope (NEWLY_LISTED or ALL_ACTIVE)
        start_date: Start date for the feed (YYYY-MM-DD)
    
    Returns:
        Feed file download information
    """
    params = {"feed_scope": feed_scope}
    
    if start_date:
        params["start_date"] = start_date
    
    path = "/buy/feed/v1/item_priority/feed"
    return make_request("GET", path, params=params)


# Feed API - Get Item Snapshot Feed
@mcp.tool()
def get_item_snapshot_feed(
    feed_scope: str,
    category_id: str = None,
    start_date: str = None
) -> dict:
    """
    Download an item snapshot feed file (TSV_GZIP format).
    
    Args:
        feed_scope: Feed scope (NEWLY_LISTED or ALL_ACTIVE)
        category_id: Category ID to filter by
        start_date: Start date for the feed (YYYY-MM-DD)
    
    Returns:
        Feed file download information
    """
    params = {"feed_scope": feed_scope}
    
    if category_id:
        params["category_id"] = category_id
    if start_date:
        params["start_date"] = start_date
    
    path = "/buy/feed/v1/item_snapshot/feed"
    return make_request("GET", path, params=params)


# Marketing API - Get Merchandised Products
@mcp.tool()
def get_merchandised_products(
    metric_name: str,
    category_id: str,
    limit: int = 8,
    aspect_filter: str = None
) -> dict:
    """
    Retrieve merchandised products based on metrics.
    
    Args:
        metric_name: Metric to filter by (e.g., BEST_SELLING)
        category_id: eBay category ID
        limit: Maximum number of products to return (default: 8, max: 100)
        aspect_filter: Aspect filter (e.g., Brand:Canon)
    
    Returns:
        List of merchandised products with details
    """
    params = {
        "metric_name": metric_name,
        "category_id": category_id,
        "limit": str(limit)
    }
    
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    
    path = "/buy/marketing/v1_beta/merchandised_product"
    return make_request("GET", path, params=params)


# Offer API - Get Bidding Information
@mcp.tool()
def get_bidding(item_id: str) -> dict:
    """
    Get bidding information for an auction item.
    
    Args:
        item_id: The eBay item ID
    
    Returns:
        Bidding information
    """
    path = f"/buy/offer/v1_beta/item/{item_id}/bidding"
    return make_request("GET", path)


# Offer API - Place Proxy Bid
@mcp.tool()
def place_proxy_bid(
    item_id: str,
    bid_amount: dict,
    quantity: int = 1
) -> dict:
    """
    Place a proxy bid on an auction item.
    
    Args:
        item_id: The eBay item ID
        bid_amount: Bid amount with value and currency
        quantity: Number of items to bid on
    
    Returns:
        Bid placement result
    """
    data = {
        "bid": bid_amount,
        "quantity": quantity
    }
    
    path = f"/buy/offer/v1_beta/item/{item_id}/place_proxy_bid"
    return make_request("POST", path, data=data)


# Order API - Initiate Guest Checkout Session
@mcp.tool()
def initiate_guest_checkout_session(
    contact_email: str,
    line_item_inputs: list,
    shipping_address: dict,
    contact_phone: str,
    contact_name: dict,
    marketplace_id: str = None
) -> dict:
    """
    Create a guest checkout session.
    
    Args:
        contact_email: Buyer's email address
        line_item_inputs: List of line items with itemId and quantity
        shipping_address: Shipping address object
        contact_phone: Contact phone number
        contact_name: Contact name object with first and last name
        marketplace_id: eBay marketplace ID (optional)
    
    Returns:
        Checkout session information
    """
    data = {
        "contactEmail": contact_email,
        "lineItemInputs": line_item_inputs,
        "shippingAddress": shipping_address,
        "contactPhone": contact_phone,
        "contactName": contact_name
    }
    
    headers = {"Content-Type": "application/json"}
    
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    path = "/buy/order/v2/guest_checkout_session/initiate"
    return make_request("POST", path, data=data, headers=headers)


# Order API - Get Guest Checkout Session
@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str) -> dict:
    """
    Get details of a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
    
    Returns:
        Checkout session details
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}"
    return make_request("GET", path)


# Order API - Update Guest Shipping Option
@mcp.tool()
def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str
) -> dict:
    """
    Update the shipping option for a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        line_item_id: The line item ID
        shipping_option_id: The shipping option ID
    
    Returns:
        Updated checkout session information
    """
    data = {
        "shippingOptionId": shipping_option_id
    }
    
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/line_item/{line_item_id}/shipping_option"
    return make_request("PUT", path, data=data)


# Order API - Update Guest Quantity
@mcp.tool()
def update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int
) -> dict:
    """
    Update the quantity of a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        line_item_id: The line item ID
        quantity: New quantity
    
    Returns:
        Updated checkout session information
    """
    data = {
        "quantity": quantity
    }
    
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/line_item/{line_item_id}"
    return make_request("PUT", path, data=data)


# Order API - Update Guest Shipping Address
@mcp.tool()
def update_guest_shipping_address(
    checkout_session_id: str,
    shipping_address: dict
) -> dict:
    """
    Update the shipping address in a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        shipping_address: New shipping address object
    
    Returns:
        Updated checkout session information
    """
    data = {
        "shippingAddress": shipping_address
    }
    
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/shipping_address"
    return make_request("PUT", path, data=data)


# Order API - Apply Guest Coupon
@mcp.tool()
def apply_guest_coupon(
    checkout_session_id: str,
    redemption_code: str
) -> dict:
    """
    Apply a coupon to a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        redemption_code: Coupon redemption code
    
    Returns:
        Updated checkout session information
    """
    data = {
        "redemptionCode": redemption_code
    }
    
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/coupon"
    return make_request("POST", path, data=data)


# Order API - Remove Guest Coupon
@mcp.tool()
def remove_guest_coupon(
    checkout_session_id: str,
    redemption_code: str
) -> dict:
    """
    Remove a coupon from a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        redemption_code: Coupon redemption code
    
    Returns:
        Updated checkout session information
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/coupon/{redemption_code}"
    return make_request("DELETE", path)


# Order API - Get Guest Purchase Order
@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str) -> dict:
    """
    Get details of a guest purchase order.
    
    Args:
        purchase_order_id: The purchase order ID
    
    Returns:
        Purchase order details
    """
    path = f"/buy/order/v2/guest_purchase_order/{purchase_order_id}"
    return make_request("GET", path)


# Additional Browse API - Get Items
@mcp.tool()
def get_items(
    item_ids: str,
    field_groups: str = None
) -> dict:
    """
    Get multiple items by their IDs.
    
    Args:
        item_ids: Comma-separated list of item IDs
        field_groups: Optional field groups to include
    
    Returns:
        List of item details
    """
    params = {}
    if field_groups:
        params["fieldgroups"] = field_groups
    
    path = f"/buy/browse/v1/item/get_items?ids={item_ids}"
    return make_request("GET", path, params=params)


if __name__ == "__main__":
    mcp.run()
