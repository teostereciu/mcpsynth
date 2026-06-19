#!/usr/bin/env python3
"""
eBay Buy API MCP Server

An MCP server with comprehensive coverage of the eBay Buy API,
suitable for use by an autonomous agent completing real-world tasks.
"""

import os
import requests
from fastmcp.server import FastMCP

# Initialize FastMCP server
mcp = FastMCP("ebay-buy-api")

# Configuration from environment variables
EBAY_APP_ID = os.getenv("EBAY_APP_ID")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com"
}

BASE_URL = BASE_URLS.get(EBAY_ENVIRONMENT, BASE_URLS["SANDBOX"])


def get_access_token():
    """Get OAuth 2.0 access token using Client Credentials flow."""
    token_url = f"{BASE_URL}/identity/v1/oauth2/token"
    
    response = requests.post(
        token_url,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {EBAY_APP_ID}:{EBAY_CERT_ID}"
        },
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope"
        },
        auth=(EBAY_APP_ID, EBAY_CERT_ID)
    )
    
    if response.status_code != 200:
        return {"error": f"Failed to get access token: {response.status_code} - {response.text}"}
    
    return response.json()


def make_ebay_request(method, path, params=None, data=None):
    """Make a request to the eBay API."""
    token = get_access_token()
    
    if isinstance(token, dict) and "error" in token:
        return token
    
    access_token = token.get("access_token")
    
    url = f"{BASE_URL}{path}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 400:
            return {"error": f"API request failed: {response.status_code} - {response.text}"}
        
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# Browse API Tools

@mcp.tool()
def search_items(query=None, category_ids=None, filter=None, limit=10, offset=0):
    """Search for items on eBay.
    
    Args:
        query: Search keywords
        category_ids: List of category IDs to filter by
        filter: Additional filters (e.g., "price:[10 TO 100]")
        limit: Maximum number of items to return
        offset: Offset for pagination
        
    Returns:
        Search results with item summaries
    """
    params = {
        "limit": limit,
        "offset": offset
    }
    
    if query:
        params["q"] = query
        
    if category_ids:
        if isinstance(category_ids, list):
            params["category_ids"] = ",".join(category_ids)
        else:
            params["category_ids"] = category_ids
            
    if filter:
        params["filter"] = filter
    
    return make_ebay_request("GET", "/buy/browse/v1/item_summary/search", params)


@mcp.tool()
def get_item(item_id):
    """Get detailed information about a specific item.
    
    Args:
        item_id: The eBay item ID
        
    Returns:
        Item details including title, price, condition, etc.
    """
    return make_ebay_request("GET", f"/buy/browse/v1/item/{item_id}")


@mcp.tool()
def get_item_variations(item_id):
    """Get variations for a specific item.
    
    Args:
        item_id: The eBay item ID
        
    Returns:
        Item variations including size, color, etc.
    """
    return make_ebay_request("GET", f"/buy/browse/v1/item/{item_id}/variations")


@mcp.tool()
def get_categories(root_category_id=None):
    """Get category tree information.
    
    Args:
        root_category_id: Optional root category ID to start from
        
    Returns:
        Category tree structure
    """
    params = {}
    if root_category_id:
        params["root_category_id"] = root_category_id
    
    return make_ebay_request("GET", "/buy/browse/v1/category_tree", params)


@mcp.tool()
def get_category_tree(category_id):
    """Get detailed information about a specific category.
    
    Args:
        category_id: The category ID
        
    Returns:
        Category details including children categories
    """
    return make_ebay_request("GET", f"/buy/browse/v1/category_tree/{category_id}")


@mcp.tool()
def get_item_summaries_by_category(
    category_id,
    query=None,
    limit=10,
    offset=0
):
    """Get item summaries from a specific category.
    
    Args:
        category_id: The category ID to search in
        query: Optional search query
        limit: Maximum number of items to return
        offset: Offset for pagination
        
    Returns:
        Item summaries from the specified category
    """
    params = {
        "limit": limit,
        "offset": offset
    }
    
    if query:
        params["q"] = query
    
    return make_ebay_request("GET", "/buy/browse/v1/item_summary/search", params)


# Deal API Tools

@mcp.tool()
def get_deals(status=None, limit=10, offset=0):
    """Get active deals on eBay.
    
    Args:
        status: Filter by status (ACTIVE, UPCOMING, ENDED)
        limit: Maximum number of deals to return
        offset: Offset for pagination
        
    Returns:
        List of deals with details
    """
    params = {
        "limit": limit,
        "offset": offset
    }
    
    if status:
        params["status"] = status
    
    return make_ebay_request("GET", "/buy/deal/v1beta/deals", params)


@mcp.tool()
def get_deal(deal_id):
    """Get details about a specific deal.
    
    Args:
        deal_id: The deal ID
        
    Returns:
        Deal details including items, pricing, etc.
    """
    return make_ebay_request("GET", f"/buy/deal/v1beta/deals/{deal_id}")


@mcp.tool()
def get_events(status=None, limit=10, offset=0):
    """Get events on eBay.
    
    Args:
        status: Filter by status (ACTIVE, UPCOMING, ENDED)
        limit: Maximum number of events to return
        offset: Offset for pagination
        
    Returns:
        List of events with details
    """
    params = {
        "limit": limit,
        "offset": offset
    }
    
    if status:
        params["status"] = status
    
    return make_ebay_request("GET", "/buy/deal/v1beta/events", params)


@mcp.tool()
def get_event(event_id):
    """Get details about a specific event.
    
    Args:
        event_id: The event ID
        
    Returns:
        Event details including items, pricing, etc.
    """
    return make_ebay_request("GET", f"/buy/deal/v1beta/events/{event_id}")


@mcp.tool()
def get_deal_items(deal_id, limit=10, offset=0):
    """Get items in a specific deal.
    
    Args:
        deal_id: The deal ID
        limit: Maximum number of items to return
        offset: Offset for pagination
        
    Returns:
        List of items in the deal
    """
    params = {
        "limit": limit,
        "offset": offset
    }
    
    return make_ebay_request("GET", f"/buy/deal/v1beta/deals/{deal_id}/items", params)


@mcp.tool()
def get_event_items(event_id, limit=10, offset=0):
    """Get items in a specific event.
    
    Args:
        event_id: The event ID
        limit: Maximum number of items to return
        offset: Offset for pagination
        
    Returns:
        List of items in the event
    """
    params = {
        "limit": limit,
        "offset": offset
    }
    
    return make_ebay_request("GET", f"/buy/deal/v1beta/events/{event_id}/items", params)


# Feed API Tools

@mcp.tool()
def get_item_feed(feed_type="ALL", limit=10, offset=0):
    """Get item feed for monitoring changes.
    
    Args:
        feed_type: Type of items to include (ALL, ACTIVE, INACTIVE, OBSOLETE)
        limit: Maximum number of items to return
        offset: Offset for pagination
        
    Returns:
        Item feed with change information
    """
    params = {
        "limit": limit,
        "offset": offset
    }
    
    if feed_type:
        params["feed_type"] = feed_type
    
    return make_ebay_request("GET", "/buy/feed/v1beta/item", params)


@mcp.tool()
def get_item_snapshot(item_id):
    """Get a snapshot of a specific item.
    
    Args:
        item_id: The eBay item ID
        
    Returns:
        Item snapshot with all current details
    """
    return make_ebay_request("GET", f"/buy/feed/v1beta/item/{item_id}/snapshot")


# Order API Tools - Guest Checkout Flow

@mcp.tool()
def get_guest_checkout_session(session_id):
    """Get details about a guest checkout session.
    
    Args:
        session_id: The session ID
        
    Returns:
        Session details including cart items, shipping, etc.
    """
    return make_ebay_request("GET", f"/buy/order/v1/guest_checkout/sessions/{session_id}")


@mcp.tool()
def create_guest_checkout_session(cart_items, shipping_address=None, billing_address=None):
    """Create a new guest checkout session.
    
    Args:
        cart_items: List of items in the cart with quantity
        shipping_address: Optional shipping address
        billing_address: Optional billing address
        
    Returns:
        Session details including session ID
    """
    data = {
        "cartItems": cart_items
    }
    
    if shipping_address:
        data["shippingAddress"] = shipping_address
        
    if billing_address:
        data["billingAddress"] = billing_address
    
    return make_ebay_request("POST", "/buy/order/v1/guest_checkout/sessions", data=data)


@mcp.tool()
def update_guest_checkout_session(session_id, cart_items=None, shipping_address=None, billing_address=None):
    """Update an existing guest checkout session.
    
    Args:
        session_id: The session ID
        cart_items: Updated list of cart items
        shipping_address: Updated shipping address
        billing_address: Updated billing address
        
    Returns:
        Updated session details
    """
    data = {}
    
    if cart_items:
        data["cartItems"] = cart_items
        
    if shipping_address:
        data["shippingAddress"] = shipping_address
        
    if billing_address:
        data["billingAddress"] = billing_address
    
    return make_ebay_request("PUT", f"/buy/order/v1/guest_checkout/sessions/{session_id}", data=data)


@mcp.tool()
def cancel_guest_checkout_session(session_id):
    """Cancel a guest checkout session.
    
    Args:
        session_id: The session ID
        
    Returns:
        Confirmation of cancellation
    """
    return make_ebay_request("DELETE", f"/buy/order/v1/guest_checkout/sessions/{session_id}")


@mcp.tool()
def get_order_items(order_id=None, limit=10, offset=0):
    """Get order items.
    
    Args:
        order_id: Optional specific order ID
        limit: Maximum number of items to return
        offset: Offset for pagination
        
    Returns:
        List of order items
    """
    params = {
        "limit": limit,
        "offset": offset
    }
    
    path = "/buy/order/v1/order_item"
    if order_id:
        path = f"/buy/order/v1/order/{order_id}/item"
    
    return make_ebay_request("GET", path, params)


@mcp.tool()
def get_order(order_id):
    """Get details about a specific order.
    
    Args:
        order_id: The order ID
        
    Returns:
        Order details including items, shipping, payment, etc.
    """
    return make_ebay_request("GET", f"/buy/order/v1/order/{order_id}")


@mcp.tool()
def get_order_transactions(order_id):
    """Get transactions for a specific order.
    
    Args:
        order_id: The order ID
        
    Returns:
        List of transactions for the order
    """
    return make_ebay_request("GET", f"/buy/order/v1/order/{order_id}/transaction")


if __name__ == "__main__":
    mcp.run()
