#!/usr/bin/env python3
"""
eBay Buy API MCP Server
An MCP server with comprehensive coverage of the eBay Buy API,
suitable for use by an autonomous agent completing real-world tasks.
"""

import os
import sys
import base64
import json
import requests
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("ebay-buy-api")

# Environment variables
EBAY_APP_ID = os.getenv("EBAY_APP_ID")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com"
}

BASE_URL = BASE_URLS.get(EBAY_ENVIRONMENT, BASE_URLS["SANDBOX"])


def get_access_token() -> Optional[str]:
    """Get OAuth 2.0 access token using client credentials grant."""
    auth_string = f"{EBAY_APP_ID}:{EBAY_CERT_ID}"
    auth_header = base64.b64encode(auth_string.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    scopes = [
        "https://api.ebay.com/oauth/api_scope",
        "https://api.ebay.com/oauth/api_scope/buy.guest.order",
        "https://api.ebay.com/oauth/api_scope/buy.deal",
        "https://api.ebay.com/oauth/api_scope/buy.feed",
        "https://api.ebay.com/oauth/api_scope/buy.offer",
        "https://api.ebay.com/oauth/api_scope/buy.marketing",
        "https://api.ebay.com/oauth/api_scope/buy.item.bulk"
    ]
    
    data = {
        "grant_type": "client_credentials",
        "scope": " ".join(scopes)
    }
    
    try:
        response = requests.post(
            "https://api.ebay.com/oauth/api_scope",
            headers=headers,
            data=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("access_token")
    except Exception as e:
        return {"error": f"Failed to get access token: {str(e)}"}


def make_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Make authenticated request to eBay API."""
    token = get_access_token()
    
    if isinstance(token, dict) and "error" in token:
        return token
    
    if headers is None:
        headers = {}
    
    headers["Authorization"] = f"Bearer {token}"
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    
    if "X-EBAY-C-MARKETPLACE-ID" not in headers:
        headers["X-EBAY-C-MARKETPLACE-ID"] = "EBAY_US"
    
    url = f"{BASE_URL}{path}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            json=json_data,
            timeout=60
        )
        
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
                return {"error": f"HTTP {response.status_code}: {response.text}"}
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection error"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_item(item_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a specific item, such as description, price, 
    category, all item aspects, condition, return policies, seller feedback 
    and score, shipping options, shipping costs, estimated delivery, and 
    other information the buyer needs to make a purchasing decision.
    
    Args:
        item_id: The unique RESTful identifier of the item
    Returns:
        Item details including price, condition, shipping options, etc.
    """
    path = f"/buy/browse/v1/item/{item_id}"
    return make_request("GET", path)


@mcp.tool()
def get_items(item_ids: List[str]) -> Dict[str, Any]:
    """
    Retrieves details about specific items that buyers need to make a 
    purchasing decision. This is a limited release available only to select Partners.
    
    Args:
        item_ids: List of unique RESTful item identifiers
    Returns:
        Details for the specified items
    """
    params = {"item_id": ",".join(item_ids)}
    path = "/buy/browse/v1/item"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_items_by_item_group(item_group_id: str) -> Dict[str, Any]:
    """
    Retrieves details about individual items in an item group. An item group 
    is an item that has various aspect differences, such as color, size, 
    storage capacity, etc.
    
    Args:
        item_group_id: The unique RESTful identifier of the item group
    Returns:
        Item details for all items in the group, including common descriptions
    """
    params = {"item_group_id": item_group_id}
    path = "/buy/browse/v1/item/get_items_by_item_group"
    return make_request("GET", path, params=params)


@mcp.tool()
def search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
    sort: Optional[str] = None,
    field_groups: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    charity_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    pickup_postal_code: Optional[str] = None
) -> Dict[str, Any]:
    """
    Searches for eBay items by various query parameters and retrieves summaries.
    You can search by keyword, category, eBay product ID (ePID), or GTIN.
    
    Args:
        q: Keyword search query
        category_ids: Category ID(s) to search in
        limit: Maximum number of items to return (default: 10, max: 100)
        offset: Number of items to skip for pagination
        sort: Sort order (e.g., 'best_match', 'ending_soonest', 'newly_listed')
        field_groups: Field groups to include (e.g., 'COMPACT', 'PRODUCT')
        filter: Filter by field values
        aspect_filter: Filter by item aspects
        compatibility_filter: Filter by product compatibility
        charity_ids: Charity ID(s) to filter by
        delivery_country: Filter by delivery country (2-letter ISO code)
        pickup_postal_code: Filter by pickup postal code
    Returns:
        Search results with item summaries
    """
    params = {"limit": str(limit), "offset": str(offset)}
    
    if q: params["q"] = q
    if category_ids: params["category_ids"] = category_ids
    if sort: params["sort"] = sort
    if field_groups: params["field_groups"] = field_groups
    if filter: params["filter"] = filter
    if aspect_filter: params["aspect_filter"] = aspect_filter
    if compatibility_filter: params["compatibility_filter"] = compatibility_filter
    if charity_ids: params["charity_ids"] = charity_ids
    if delivery_country: params["delivery_country"] = delivery_country
    if pickup_postal_code: params["pickup_postal_code"] = pickup_postal_code
    
    path = "/buy/browse/v1/item_summary/search"
    return make_request("GET", path, params=params)


@mcp.tool()
def search_items_by_image(
    base64_image: str,
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None
) -> Dict[str, Any]:
    """
    Searches for eBay items based on an image and retrieves summaries.
    Pass in a Base64 image in the request payload.
    
    Args:
        base64_image: Base64-encoded image string
        limit: Maximum number of items to return (default: 10)
        offset: Number of items to skip for pagination
        filter: Filter by field values
        aspect_filter: Filter by item aspects
        category_ids: Category ID(s) to search in
        delivery_country: Filter by delivery country (2-letter ISO code)
    Returns:
        Search results with item summaries
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if filter: params["filter"] = filter
    if aspect_filter: params["aspect_filter"] = aspect_filter
    if category_ids: params["category_ids"] = category_ids
    if delivery_country: params["delivery_country"] = delivery_country
    
    payload = {"image": base64_image}
    path = "/buy/browse/v1/item_summary/search_by_image"
    return make_request("POST", path, params=params, json_data=payload)


@mcp.tool()
def check_compatibility(
    item_id: str,
    compatibility_properties: List[Dict[str, str]]
) -> Dict[str, Any]:
    """
    Checks if a product is compatible with the specified item. You can use this 
    method to check the compatibility of cars, trucks, and motorcycles with a 
    specific part listed on eBay.
    
    Args:
        item_id: The unique RESTful identifier of the item (part)
        compatibility_properties: List of attribute name/value pairs to define 
                                a specific product (e.g., [{"name": "Year", "value": "2019"}])
    Returns:
        Compatibility status (COMPATIBLE, NOT_COMPATIBLE, or UNDETERMINED)
    """
    path = f"/buy/browse/v1/item/{item_id}/check_compatibility"
    payload = {"compatibilityProperties": compatibility_properties}
    return make_request("POST", path, json_data=payload)


@mcp.tool()
def get_item_by_legacy_id(legacy_id: str) -> Dict[str, Any]:
    """
    Retrieves item details using the legacy eBay item ID.
    
    Args:
        legacy_id: The traditional/legacy eBay item ID
    Returns:
        Item details
    """
    params = {"legacy_id": legacy_id}
    path = "/buy/browse/v1/item"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_events(
    marketplace_id: str = "EBAY_US",
    limit: int = 20,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Returns paginated results containing all eBay events for the specified marketplace.
    
    Args:
        marketplace_id: eBay marketplace ID (default: EBAY_US)
        limit: Maximum number of events to return (default: 20, max: 100)
        offset: Number of events to skip for pagination
    Returns:
        Paginated list of events with their details
    """
    params = {"limit": str(limit), "offset": str(offset)}
    path = "/buy/deal/v1/event"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_event(event_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """
    Returns details for a specific event.
    
    Args:
        event_id: The unique identifier for the event
        marketplace_id: eBay marketplace ID (default: EBAY_US)
    Returns:
        Event details including title, description, dates, and terms
    """
    path = f"/buy/deal/v1/event/{event_id}"
    return make_request("GET", path)


@mcp.tool()
def get_event_items(
    event_ids: str,
    marketplace_id: str = "EBAY_US",
    category_ids: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
    delivery_country: Optional[str] = None
) -> Dict[str, Any]:
    """
    Returns a paginated set of event items associated with the specified search 
    criteria and marketplace ID.
    
    Args:
        event_ids: Comma-separated list of event IDs (maximum: 1)
        marketplace_id: eBay marketplace ID (default: EBAY_US)
        category_ids: Category ID(s) to filter by
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
        delivery_country: Filter by delivery country (2-letter ISO code)
    Returns:
        Paginated list of event items with pricing and shipping info
    """
    params = {"event_ids": event_ids, "limit": str(limit), "offset": str(offset)}
    if category_ids: params["category_ids"] = category_ids
    if delivery_country: params["delivery_country"] = delivery_country
    path = "/buy/deal/v1/event_item"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_deal_items(
    deal_ids: str,
    marketplace_id: str = "EBAY_US",
    limit: int = 20,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Returns a paginated set of deal items associated with the specified deal IDs 
    and marketplace ID.
    
    Args:
        deal_ids: Comma-separated list of deal IDs
        marketplace_id: eBay marketplace ID (default: EBAY_US)
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
    Returns:
        Paginated list of deal items
    """
    params = {"deal_ids": deal_ids, "limit": str(limit), "offset": str(offset)}
    path = "/buy/deal/v1/deal_item"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_item_feed(
    limit: int = 20,
    offset: int = 0,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    item_ids: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieves a feed of item data that matches the specified filters.
    
    Args:
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
        start_time: Start time for the feed (ISO 8601 format)
        end_time: End time for the feed (ISO 8601 format)
        item_ids: Comma-separated list of item IDs to include
    Returns:
        Feed of item data with timestamps
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if start_time: params["start_time"] = start_time
    if end_time: params["end_time"] = end_time
    if item_ids: params["item_ids"] = item_ids
    path = "/buy/feed/v1beta/item"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_item_group_feed(
    limit: int = 20,
    offset: int = 0,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    item_group_ids: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieves a feed of item group data that matches the specified filters.
    
    Args:
        limit: Maximum number of item groups to return (default: 20)
        offset: Number of item groups to skip for pagination
        start_time: Start time for the feed (ISO 8601 format)
        end_time: End time for the feed (ISO 8601 format)
        item_group_ids: Comma-separated list of item group IDs to include
    Returns:
        Feed of item group data with timestamps
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if start_time: params["start_time"] = start_time
    if end_time: params["end_time"] = end_time
    if item_group_ids: params["item_group_ids"] = item_group_ids
    path = "/buy/feed/v1beta/item_group"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_item_priority_feed(
    limit: int = 20,
    offset: int = 0,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieves a feed of item priority data that matches the specified filters.
    
    Args:
        limit: Maximum number of items to return (default: 20)
        offset: Number of items to skip for pagination
        start_time: Start time for the feed (ISO 8601 format)
        end_time: End time for the feed (ISO 8601 format)
    Returns:
        Feed of item priority data
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if start_time: params["start_time"] = start_time
    if end_time: params["end_time"] = end_time
    path = "/buy/feed/v1beta/item_priority"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_item_snapshot_feed(
    limit: int = 20,
    offset: int = 0,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieves a feed of item snapshot data that matches the specified filters.
    
    Args:
        limit: Maximum number of snapshots to return (default: 20)
        offset: Number of snapshots to skip for pagination
        start_time: Start time for the feed (ISO 8601 format)
        end_time: End time for the feed (ISO 8601 format)
    Returns:
        Feed of item snapshot data
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if start_time: params["start_time"] = start_time
    if end_time: params["end_time"] = end_time
    path = "/buy/feed/v1beta/item_snapshot"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_merchandised_products(
    item_id: str,
    limit: int = 10,
    offset: int = 0,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieves products that are merchandised with the specified item. These are 
    typically related products that complement the item.
    
    Args:
        item_id: The unique RESTful identifier of the item
        limit: Maximum number of products to return (default: 10)
        offset: Number of products to skip for pagination
        marketplace_id: eBay marketplace ID (default: EBAY_US)
    Returns:
        List of merchandised products with details
    """
    params = {"limit": str(limit), "offset": str(offset)}
    path = f"/buy/marketing/v1/merchandised_product/{item_id}"
    return make_request("GET", path, params=params)


@mcp.tool()
def get_bidding(item_id: str) -> Dict[str, Any]:
    """
    Retrieves the current bidding information for an auction item.
    
    Args:
        item_id: The unique RESTful identifier of the auction item
    Returns:
        Bidding information including current bid and bid count
    """
    path = f"/buy/offer/v1beta/bidding/{item_id}"
    return make_request("GET", path)


@mcp.tool()
def place_proxy_bid(
    item_id: str,
    bid_amount: float,
    currency: str = "USD"
) -> Dict[str, Any]:
    """
    Places a proxy bid on an auction item. This sets a maximum bid that eBay 
    will bid on your behalf up to that amount.
    
    Args:
        item_id: The unique RESTful identifier of the auction item
        bid_amount: The maximum bid amount you're willing to pay
        currency: The currency code (default: USD)
    Returns:
        Bid confirmation with bid ID and status
    """
    path = f"/buy/offer/v1beta/bidding/{item_id}"
    payload = {"bid": {"amount": str(bid_amount), "currency": currency}}
    return make_request("POST", path, json_data=payload)


@mcp.tool()
def initiate_guest_checkout_session(
    contact_email: str,
    line_item_inputs: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Creates an eBay guest checkout session, which is the first step in performing 
    a checkout. The method returns a checkoutSessionId that you use as a URI 
    parameter in subsequent guest checkout methods.
    
    Args:
        contact_email: The buyer's email address
        line_item_inputs: List of line items with itemId and quantity
        shipping_address: Shipping address details
        marketplace_id: eBay marketplace ID (default: EBAY_US)
    Returns:
        Checkout session with session ID and line item details
    """
    payload = {
        "contactEmail": contact_email,
        "lineItemInputs": line_item_inputs,
        "shippingAddress": shipping_address
    }
    path = "/buy/order/v2/guest_checkout_session/initiate"
    return make_request("POST", path, json_data=payload)


@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a guest checkout session.
    
    Args:
        checkout_session_id: The unique identifier for the checkout session
    Returns:
        Checkout session details including line items, shipping, and pricing
    """
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}"
    return make_request("GET", path)


@mcp.tool()
def apply_guest_coupon(
    checkout_session_id: str,
    coupon_code: str
) -> Dict[str, Any]:
    """
    Applies a coupon to a guest checkout session.
    
    Args:
        checkout_session_id: The unique identifier for the checkout session
        coupon_code: The coupon code to apply
    Returns:
        Updated checkout session with coupon applied
    """
    payload = {"couponCode": coupon_code}
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon"
    return make_request("POST", path, json_data=payload)


@mcp.tool()
def remove_guest_coupon(
    checkout_session_id: str,
    coupon_code: str
) -> Dict[str, Any]:
    """
    Removes a coupon from a guest checkout session.
    
    Args:
        checkout_session_id: The unique identifier for the checkout session
        coupon_code: The coupon code to remove
    Returns:
        Updated checkout session with coupon removed
    """
    payload = {"couponCode": coupon_code}
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon"
    return make_request("POST", path, json_data=payload)


@mcp.tool()
def update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int
) -> Dict[str, Any]:
    """
    Updates the quantity of a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The unique identifier for the checkout session
        line_item_id: The unique identifier for the line item
        quantity: The new quantity for the line item
    Returns:
        Updated checkout session with updated line item quantity
    """
    payload = {"lineItemInputs": [{"lineItemId": line_item_id, "quantity": quantity}]}
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity"
    return make_request("POST", path, json_data=payload)


@mcp.tool()
def update_guest_shipping_address(
    checkout_session_id: str,
    shipping_address: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates the shipping address for a guest checkout session.
    
    Args:
        checkout_session_id: The unique identifier for the checkout session
        shipping_address: New shipping address details
    Returns:
        Updated checkout session with updated shipping address
    """
    payload = {"shippingAddress": shipping_address}
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address"
    return make_request("POST", path, json_data=payload)


@mcp.tool()
def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str
) -> Dict[str, Any]:
    """
    Updates the shipping option for a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The unique identifier for the checkout session
        line_item_id: The unique identifier for the line item
        shipping_option_id: The new shipping option ID
    Returns:
        Updated checkout session with updated shipping option
    """
    payload = {"lineItemInputs": [{"lineItemId": line_item_id, "shippingOptionId": shipping_option_id}]}
    path = f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option"
    return make_request("POST", path, json_data=payload)


@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a guest purchase order.
    
    Args:
        purchase_order_id: The unique identifier for the purchase order
    Returns:
        Purchase order details including status, pricing, and shipping info
    """
    path = f"/buy/order/v2/guest_purchase_order/{purchase_order_id}"
    return make_request("GET", path)


if __name__ == "__main__":
    mcp.run()
