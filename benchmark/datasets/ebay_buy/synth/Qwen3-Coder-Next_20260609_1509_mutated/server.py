#!/usr/bin/env python3
"""
eBay Buy API MCP Server

This MCP server provides tools for interacting with the eBay Buy API,
covering Browse, Deal, Feed, Marketing, Offer, and Order namespaces.
"""

import os
import json
import requests
from typing import Any, Dict, Optional
from fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("ebay-buy")

# Get eBay API configuration from environment
EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

# Base URLs for eBay API
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com"
}
BASE_URL = BASE_URLS.get(EBAY_ENVIRONMENT, BASE_URLS["SANDBOX"])

# OAuth token URL
OAUTH_TOKEN_URL = "https://api.sandbox.ebay.com/oauth/api_scope"

# Auth scopes for different API namespaces
SCOPES = {
    "browse": "https://api.ebay.com/oauth/api_scope",
    "browse_bulk": "https://api.ebay.com/oauth/api_scope/buy.item.bulk",
    "deal": "https://api.ebay.com/oauth/api_scope/buy.deal",
    "feed": "https://api.ebay.com/oauth/api_scope/buy.item.feed",
    "marketing": "https://api.ebay.com/oauth/api_scope/buy.marketing",
    "offer": "https://api.ebay.com/oauth/api_scope/buy.offer",
    "order": "https://api.ebay.com/oauth/api_scope/buy.guest.order"
}


def get_oauth_token() -> Optional[str]:
    """Get OAuth 2.0 access token using client credentials flow."""
    if not EBAY_APP_ID or not EBAY_CERT_ID:
        return None
    
    try:
        response = requests.post(
            "https://api.sandbox.ebay.com/oauth2/token",
            auth=(EBAY_APP_ID, EBAY_CERT_ID),
            data={
                "grant_type": "client_credentials",
                "scope": SCOPES["browse"]
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.raise_for_status()
        return response.json().get("access_token")
    except Exception:
        return None


def make_api_call(method: str, path: str, params: Optional[Dict] = None, 
                  headers: Optional[Dict] = None, json_body: Optional[Dict] = None) -> Dict[str, Any]:
    """Make an API call to eBay and return the response."""
    try:
        token = get_oauth_token()
        if not token:
            return {"error": "Authentication failed. EBAY_APP_ID and EBAY_CERT_ID must be set."}
        
        url = f"{BASE_URL}{path}"
        
        # Default headers
        default_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # Merge headers
        if headers:
            default_headers.update(headers)
        
        # Make request
        if method.upper() == "GET":
            response = requests.get(url, params=params, headers=default_headers)
        elif method.upper() == "POST":
            response = requests.post(url, params=params, headers=default_headers, json=json_body)
        elif method.upper() == "PUT":
            response = requests.put(url, params=params, headers=default_headers, json=json_body)
        elif method.upper() == "DELETE":
            response = requests.delete(url, params=params, headers=default_headers)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        # Handle response
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except:
                return {"data": response.text}
        else:
            try:
                error_data = response.json()
                return {"error": error_data}
            except:
                return {"error": f"API error {response.status_code}: {response.text}"}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# Browse API - Get Item
@mcp.tool()
def get_item(listing_id: str, fieldgroups: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieves the details of a specific item from eBay.
    
    Args:
        listing_id: The unique identifier of the item (RESTful format)
        fieldgroups: Optional field groups to include (COMPACT, PRODUCT, ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS)
    
    Returns:
        Item details including price, condition, seller info, shipping options, etc.
    """
    path = f"/buy/browse/v1/item/{listing_id}"
    params = {}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    return make_api_call("GET", path, params=params)


# Browse API - Get Items (Batch)
@mcp.tool()
def get_items(item_ids: Optional[str] = None, item_group_ids: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieves details for multiple items in a single request.
    
    Args:
        item_ids: Comma-separated list of item IDs (RESTful format)
        item_group_ids: Comma-separated list of item group IDs
    
    Returns:
        List of item details
    """
    path = "/buy/browse/v1/item"
    params = {}
    if item_ids:
        params["item_ids"] = item_ids
    if item_group_ids:
        params["item_group_ids"] = item_group_ids
    return make_api_call("GET", path, params=params)


# Browse API - Search Items
@mcp.tool()
def search_items(q: Optional[str] = None, category_ids: Optional[str] = None, 
                 max_results: Optional[int] = None, skip: Optional[int] = None,
                 filter: Optional[str] = None, fieldgroups: Optional[str] = None,
                 aspect_filter: Optional[str] = None, compatibility_filter: Optional[str] = None,
                 order_by: Optional[str] = None) -> Dict[str, Any]:
    """
    Search for eBay items by various criteria.
    
    Args:
        q: Search query string (keywords, ePID, GTIN, etc.)
        category_ids: Category ID(s) to search in
        max_results: Maximum number of results to return (default: 20, max: 100)
        skip: Number of results to skip for pagination
        filter: Filter expression for result fields
        fieldgroups: Field groups to include in response
        aspect_filter: Filter results by item aspects
        compatibility_filter: Filter for items compatible with specific products
        order_by: Sort order (e.g., "-price", "price", "newlyListed")
    
    Returns:
        Search results with item summaries
    """
    path = "/buy/browse/v1/item_summary/search"
    params = {}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if max_results:
        params["max_results"] = str(max_results)
    if skip:
        params["skip"] = str(skip)
    if filter:
        params["filter"] = filter
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if compatibility_filter:
        params["compatibility_filter"] = compatibility_filter
    if order_by:
        params["order_by"] = order_by
    return make_api_call("GET", path, params=params)


# Browse API - Search by Image
@mcp.tool()
def search_items_by_image(image: str, max_results: Optional[int] = None,
                          order_by: Optional[str] = None) -> Dict[str, Any]:
    """
    Search for items using an image URL or base64-encoded image.
    
    Args:
        image: Image URL or base64-encoded image data
        max_results: Maximum number of results to return
        order_by: Sort order for results
    
    Returns:
        Search results matching the uploaded image
    """
    path = "/buy/browse/v1/item_summary/search_by_image"
    params = {"image": image}
    if max_results:
        params["max_results"] = str(max_results)
    if order_by:
        params["order_by"] = order_by
    return make_api_call("POST", path, params=params)


# Browse API - Get Items by Legacy ID
@mcp.tool()
def get_item_by_legacy_id(legacy_item_id: str) -> Dict[str, Any]:
    """
    Retrieves item details using the legacy eBay item ID.
    
    Args:
        legacy_item_id: The traditional eBay item ID
    
    Returns:
        Item details
    """
    path = "/buy/browse/v1/item/get_item_by_legacy_id"
    params = {"legacy_item_id": legacy_item_id}
    return make_api_call("GET", path, params=params)


# Browse API - Get Items by Item Group
@mcp.tool()
def get_items_by_item_group(item_group_id: str, fieldgroups: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieves details for all items in an item group (seller-defined variations).
    
    Args:
        item_group_id: The ID of the item group
        fieldgroups: Optional field groups to include
    
    Returns:
        List of items in the group
    """
    path = "/buy/browse/v1/item/get_items_by_item_group"
    params = {"item_group_id": item_group_id}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    return make_api_call("GET", path, params=params)


# Browse API - Check Compatibility
@mcp.tool()
def check_compatibility(listing_id: str, product_attributes: list) -> Dict[str, Any]:
    """
    Check if an item is compatible with specific product attributes.
    
    Args:
        listing_id: The item ID to check
        product_attributes: List of product attributes to check compatibility with
    
    Returns:
        Compatibility information
    """
    path = f"/buy/browse/v1/item/{listing_id}/check_compatibility"
    
    # Format product attributes for the request
    if isinstance(product_attributes, list):
        # Convert list to proper format if needed
        attributes_list = []
        for attr in product_attributes:
            if isinstance(attr, dict):
                attributes_list.append(attr)
            else:
                attributes_list.append({"name": str(attr), "value": ""})
        body = {"product_attributes": attributes_list}
    else:
        body = {"product_attributes": product_attributes}
    
    return make_api_call("POST", path, json_body=body)


# Deal API - Get Deals
@mcp.tool()
def get_deal_items(category_ids: Optional[str] = None, max_results: Optional[int] = None,
                   skip: Optional[int] = None, commissionable: Optional[bool] = None,
                   delivery_country: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieve deal items from eBay.
    
    Args:
        category_ids: Category IDs to filter deals
        max_results: Maximum number of results
        skip: Number of results to skip
        commissionable: Filter for commissionable items
        delivery_country: Filter by delivery country (2-letter ISO code)
    
    Returns:
        List of deal items
    """
    path = "/buy/deal/v1/deal_item"
    params = {}
    if category_ids:
        params["category_ids"] = category_ids
    if max_results:
        params["max_results"] = str(max_results)
    if skip:
        params["skip"] = str(skip)
    if commissionable is not None:
        params["commissionable"] = "true" if commissionable else "false"
    if delivery_country:
        params["delivery_country"] = delivery_country
    return make_api_call("GET", path, params=params)


# Deal API - Get Event
@mcp.tool()
def get_event(event_id: str) -> Dict[str, Any]:
    """
    Get details of a specific deal event.
    
    Args:
        event_id: The event ID
    
    Returns:
        Event details
    """
    path = f"/buy/deal/v1/event/{event_id}"
    return make_api_call("GET", path)


# Deal API - Get Events
@mcp.tool()
def get_events(category_ids: Optional[str] = None, max_results: Optional[int] = None,
               skip: Optional[int] = None) -> Dict[str, Any]:
    """
    Retrieve active deal events.
    
    Args:
        category_ids: Filter by category IDs
        max_results: Maximum number of results
        skip: Number of results to skip
    
    Returns:
        List of active events
    """
    path = "/buy/deal/v1/event"
    params = {}
    if category_ids:
        params["category_ids"] = category_ids
    if max_results:
        params["max_results"] = str(max_results)
    if skip:
        params["skip"] = str(skip)
    return make_api_call("GET", path, params=params)


# Deal API - Get Event Items
@mcp.tool()
def get_event_items(event_ids: str, category_ids: Optional[str] = None, 
                    max_results: Optional[int] = None, skip: Optional[int] = None) -> Dict[str, Any]:
    """
    Retrieve items associated with specific deal events.
    
    Args:
        event_ids: Event IDs (comma-separated)
        category_ids: Filter by category IDs
        max_results: Maximum number of results
        skip: Number of results to skip
    
    Returns:
        List of items in the events
    """
    path = "/buy/deal/v1/event_item"
    params = {"event_ids": event_ids}
    if category_ids:
        params["category_ids"] = category_ids
    if max_results:
        params["max_results"] = str(max_results)
    if skip:
        params["skip"] = str(skip)
    return make_api_call("GET", path, params=params)


# Feed API - Get Item Feed
@mcp.tool()
def get_item_feed(feed_scope: str, category_id: Optional[str] = None, 
                  date: Optional[str] = None) -> Dict[str, Any]:
    """
    Download a feed file containing item data.
    
    Args:
        feed_scope: Type of feed (NEWLY_LISTED or ALL_ACTIVE)
        category_id: Category ID to filter feed
        date: Date for the feed (format: YYYYMMDD for daily, YYYY-MM-DD for bootstrap)
    
    Returns:
        Feed file URL (TSV_GZIP format)
    """
    path = "/buy/feed/v1_beta/item"
    params = {"feed_scope": feed_scope}
    if category_id:
        params["category_id"] = category_id
    if date:
        params["date"] = date
    return make_api_call("GET", path, params=params)


# Feed API - Get Item Group Feed
@mcp.tool()
def get_item_group_feed(feed_scope: str, category_id: Optional[str] = None,
                        date: Optional[str] = None) -> Dict[str, Any]:
    """
    Download a feed file containing item group data.
    
    Args:
        feed_scope: Type of feed (NEWLY_LISTED or ALL_ACTIVE)
        category_id: Category ID to filter feed
        date: Date for the feed
    
    Returns:
        Feed file URL
    """
    path = "/buy/feed/v1_beta/item_group"
    params = {"feed_scope": feed_scope}
    if category_id:
        params["category_id"] = category_id
    if date:
        params["date"] = date
    return make_api_call("GET", path, params=params)


# Feed API - Get Item Priority Feed
@mcp.tool()
def get_item_priority_feed(category_id: str, date: str) -> Dict[str, Any]:
    """
    Download a feed file containing priority item data.
    
    Args:
        category_id: Category ID
        date: Date for the feed (format: YYYYMMDD)
    
    Returns:
        Feed file URL
    """
    path = "/buy/feed/v1_beta/item_priority"
    params = {"category_id": category_id, "date": date}
    return make_api_call("GET", path, params=params)


# Feed API - Get Item Snapshot Feed
@mcp.tool()
def get_item_snapshot_feed(category_id: str, snapshot_date: str) -> Dict[str, Any]:
    """
    Download a snapshot feed file.
    
    Args:
        category_id: Category ID
        snapshot_date: Snapshot date (format: YYYY-MM-DDTHH:MM:SS.000Z)
    
    Returns:
        Feed file URL
    """
    path = "/buy/feed/v1_beta/item_snapshot"
    params = {"category_id": category_id, "snapshot_date": snapshot_date}
    return make_api_call("GET", path, params=params)


# Marketing API - Get Merchandised Products
@mcp.tool()
def get_merchandised_products(category_id: str, metric_name: Optional[str] = None,
                              item_id: Optional[str] = None, max_results: Optional[int] = None) -> Dict[str, Any]:
    """
    Retrieve merchandised products recommendations.
    
    Args:
        category_id: Category ID
        metric_name: Metric to use for recommendations (BEST_SELLING, MOST_VIEWED, etc.)
        item_id: Item ID for 'VIEWED' or 'BOUGHT' recommendations
        max_results: Maximum number of results
    
    Returns:
        List of recommended products
    """
    path = "/buy/marketing/v1_beta/merchandised_product"
    params = {"category_id": category_id}
    if metric_name:
        params["metric_name"] = metric_name
    if item_id:
        params["item_id"] = item_id
    if max_results:
        params["max_results"] = str(max_results)
    return make_api_call("GET", path, params=params)


# Offer API - Get Bidding
@mcp.tool()
def get_bidding(listing_id: str) -> Dict[str, Any]:
    """
    Get current bidding information for an auction item.
    
    Args:
        listing_id: The item ID
    
    Returns:
        Bidding information including current bid and bid count
    """
    path = f"/buy/offer/v1_beta/bidding/{listing_id}"
    return make_api_call("GET", path)


# Offer API - Place Proxy Bid
@mcp.tool()
def place_proxy_bid(listing_id: str, bid_amount: float, currency: str = "USD") -> Dict[str, Any]:
    """
    Place a proxy bid on an auction item.
    
    Args:
        listing_id: The item ID
        bid_amount: The maximum bid amount
        currency: Currency code (default: USD)
    
    Returns:
        Bidding confirmation
    """
    path = f"/buy/offer/v1_beta/bidding/{listing_id}/place_proxy_bid"
    
    body = {
        "bid": {
            "amount": str(bid_amount),
            "currency": currency.upper()
        }
    }
    
    return make_api_call("POST", path, json_body=body)


# Order API - Initiate Guest Checkout Session
@mcp.tool()
def initiate_guest_checkout_session(contact_email: str, line_items: list, 
                                    shipping_address: dict, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a guest checkout session.
    
    Args:
        contact_email: Buyer's email address
        line_items: List of line items with itemId and quantity
        shipping_address: Shipping address information
        marketplace_id: eBay marketplace ID
    
    Returns:
        Checkout session with session ID and line items
    """
    path = "/buy/order/v2/guest_checkout_session/initiate"
    
    body = {
        "contactEmail": contact_email,
        "lineItemInputs": line_items,
        "shippingAddress": shipping_address
    }
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    headers["Content-Type"] = "application/json"
    
    return make_api_call("POST", path, json_body=body, headers=headers)


# Order API - Get Guest Checkout Session
@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Get details of a guest checkout session.
    
    Args:
        checkout_session_id: The session ID
        marketplace_id: eBay marketplace ID
    
    Returns:
        Checkout session details
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}"
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_api_call("GET", path, headers=headers)


# Order API - Apply Coupon to Guest Checkout
@mcp.tool()
def apply_guest_coupon(checkout_session_id: str, coupon_code: str, 
                       marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Apply a coupon to a guest checkout session.
    
    Args:
        checkout_session_id: The session ID
        coupon_code: The coupon code to apply
        marketplace_id: eBay marketplace ID
    
    Returns:
        Updated checkout session with applied coupon
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon"
    
    body = {"coupon_code": coupon_code}
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_api_call("POST", path, json_body=body, headers=headers)


# Order API - Remove Coupon from Guest Checkout
@mcp.tool()
def remove_guest_coupon(checkout_session_id: str, coupon_code: str,
                        marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Remove a coupon from a guest checkout session.
    
    Args:
        checkout_session_id: The session ID
        coupon_code: The coupon code to remove
        marketplace_id: eBay marketplace ID
    
    Returns:
        Updated checkout session
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon"
    
    body = {"coupon_code": coupon_code}
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_api_call("POST", path, json_body=body, headers=headers)


# Order API - Update Guest Checkout Quantity
@mcp.tool()
def update_guest_quantity(checkout_session_id: str, line_item_id: str, quantity: int,
                          marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Update the quantity of a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The session ID
        line_item_id: The line item ID
        quantity: New quantity
        marketplace_id: eBay marketplace ID
    
    Returns:
        Updated checkout session
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity"
    
    body = {
        "lineItemInputs": [
            {"lineItem": {"lineItemId": line_item_id}, "quantity": quantity}
        ]
    }
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_api_call("POST", path, json_body=body, headers=headers)


# Order API - Update Guest Shipping Address
@mcp.tool()
def update_guest_shipping_address(checkout_session_id: str, shipping_address: dict,
                                  marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Update the shipping address in a guest checkout session.
    
    Args:
        checkout_session_id: The session ID
        shipping_address: New shipping address
        marketplace_id: eBay marketplace ID
    
    Returns:
        Updated checkout session
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address"
    
    body = {"shippingAddress": shipping_address}
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_api_call("POST", path, json_body=body, headers=headers)


# Order API - Update Guest Shipping Option
@mcp.tool()
def update_guest_shipping_option(checkout_session_id: str, line_item_id: str, shipping_option_id: str,
                                 marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Update the shipping option for a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The session ID
        line_item_id: The line item ID
        shipping_option_id: The shipping option ID to select
        marketplace_id: eBay marketplace ID
    
    Returns:
        Updated checkout session
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option"
    
    body = {
        "lineItemInputs": [
            {
                "lineItem": {"lineItemId": line_item_id},
                "shippingOption": {"shippingOptionId": shipping_option_id}
            }
        ]
    }
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_api_call("POST", path, json_body=body, headers=headers)


# Order API - Get Guest Purchase Order
@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Get details of a guest purchase order.
    
    Args:
        purchase_order_id: The purchase order ID
        marketplace_id: eBay marketplace ID
    
    Returns:
        Purchase order details
    """
    path = f"/buy/order/v2/guest_purchase_order/{purchase_order_id}"
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_api_call("GET", path, headers=headers)


if __name__ == "__main__":
    mcp.run()
