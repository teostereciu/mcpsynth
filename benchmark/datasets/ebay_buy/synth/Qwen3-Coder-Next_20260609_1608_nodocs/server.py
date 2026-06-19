#!/usr/bin/env python3
"""
eBay Buy API MCP Server

An MCP server for the eBay Buy API enabling autonomous agents to interact
with eBay's shopping, deals, feeds, and order management capabilities.
"""

import os
import time
from typing import Any

import requests
from fastmcp import FastMCP

# Configuration
APP_ID = os.environ.get("EBAY_APP_ID")
CERT_ID = os.environ.get("EBAY_CERT_ID")
ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

BASE_URL = "https://api.sandbox.ebay.com" if ENVIRONMENT == "SANDBOX" else "https://api.ebay.com"

# Token cache
_token_cache: dict[str, Any] = {}
_TOKEN_EXPIRY: dict[str, float] = {}


def get_oauth_token() -> str:
    """Get OAuth 2.0 access token using Client Credentials flow."""
    cache_key = f"{APP_ID}_{ENVIRONMENT}"
    current_time = time.time()
    
    if cache_key in _TOKEN_EXPIRY and current_time < _TOKEN_EXPIRY[cache_key]:
        return _token_cache[cache_key]
    
    token_url = f"{BASE_URL}/identity/v1/oauth2/token"
    
    response = requests.post(
        token_url,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {os.environ.get('EBAY_AUTH_HEADER', '')}",
        },
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope"
        },
        auth=(APP_ID, CERT_ID)
    )
    
    if response.status_code != 200:
        return {"error": f"Failed to get OAuth token: {response.status_code} - {response.text}"}
    
    token_data = response.json()
    access_token = token_data.get("access_token")
    expires_in = token_data.get("expires_in", 3600)
    
    _token_cache[cache_key] = access_token
    _TOKEN_EXPIRY[cache_key] = current_time + expires_in - 60  # Refresh 1 minute before expiry
    
    return access_token


def make_request(
    method: str,
    path: str,
    params: dict[str, Any] | None = None,
    json: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Make authenticated request to eBay API."""
    token = get_oauth_token()
    if isinstance(token, dict) and "error" in token:
        return token
    
    url = f"{BASE_URL}{path}"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json,
            headers=headers,
            timeout=30,
        )
        
        if response.status_code >= 400:
            error_msg = f"API error ({response.status_code}): {response.text}"
            return {"error": error_msg}
        
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# Initialize FastMCP server
mcp = FastMCP("ebay-buy-api")


# ==================== Browse API ====================

@mcp.tool()
def get_item(item_id: str) -> dict[str, Any]:
    """Get detailed information about a specific eBay item.
    
    Args:
        item_id: The eBay item ID (e.g., 'v1|1234567890|0')
        
    Returns:
        Item details including title, price, condition, seller info, etc.
    """
    return make_request("GET", f"/buy/browse/v1/item/{item_id}")


@mcp.tool()
def search_items(
    q: str | None = None,
    category_ids: str | None = None,
    filters: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict[str, Any]:
    """Search for items on eBay.
    
    Args:
        q: Search query string
        category_ids: Comma-separated category IDs to filter by
        filters: Additional filter expressions
        limit: Maximum number of results (default 10, max 50)
        offset: Result offset for pagination
        
    Returns:
        Search results with matching items
    """
    params = {
        "limit": limit,
        "offset": offset,
    }
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if filters:
        params["filter"] = filters
        
    return make_request("GET", "/buy/browse/v1/item_summary/search", params=params)


@mcp.tool()
def get_item_summary(item_id: str) -> dict[str, Any]:
    """Get a summary of item details including pricing and availability.
    
    Args:
        item_id: The eBay item ID
        
    Returns:
        Item summary with price, condition, and availability info
    """
    return make_request("GET", f"/buy/browse/v1/item/{item_id}/summary")


@mcp.tool()
def get_item_relationships(item_id: str) -> dict[str, Any]:
    """Get relationships for an item (e.g., similar items, variants).
    
    Args:
        item_id: The eBay item ID
        
    Returns:
        Item relationships data
    """
    return make_request("GET", f"/buy/browse/v1/item/{item_id}/relationships")


@mcp.tool()
def get_item_seller_info(item_id: str) -> dict[str, Any]:
    """Get seller information for a specific item.
    
    Args:
        item_id: The eBay item ID
        
    Returns:
        Seller information including feedback score and store info
    """
    return make_request("GET", f"/buy/browse/v1/item/{item_id}/seller_info")


@mcp.tool()
def get_item_variations(item_id: str) -> dict[str, Any]:
    """Get variations for a multiple-variation listing.
    
    Args:
        item_id: The eBay item ID
        
    Returns:
        List of variations with their details
    """
    return make_request("GET", f"/buy/browse/v1/item/{item_id}/variations")


@mcp.tool()
def search_item_groups(
    q: str | None = None,
    filters: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict[str, Any]:
    """Search for item groups (e.g., collections, bundles).
    
    Args:
        q: Search query string
        filters: Additional filter expressions
        limit: Maximum number of results
        offset: Result offset for pagination
        
    Returns:
        Matching item groups
    """
    params = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if filters:
        params["filter"] = filters
        
    return make_request("GET", "/buy/browse/v1/item_group/search", params=params)


@mcp.tool()
def get_item_group(item_group_id: str) -> dict[str, Any]:
    """Get details of a specific item group.
    
    Args:
        item_group_id: The item group ID
        
    Returns:
        Item group details
    """
    return make_request("GET", f"/buy/browse/v1/item_group/{item_group_id}")


@mcp.tool()
def get_item_group_items(item_group_id: str) -> dict[str, Any]:
    """Get items in a specific item group.
    
    Args:
        item_group_id: The item group ID
        
    Returns:
        List of items in the group
    """
    return make_request("GET", f"/buy/browse/v1/item_group/{item_group_id}/item")


@mcp.tool()
def get_categories() -> dict[str, Any]:
    """Get list of eBay categories.
    
    Returns:
        List of top-level categories
    """
    return make_request("GET", "/buy/browse/v1/category")


@mcp.tool()
def get_category_tree(category_id: str | None = None) -> dict[str, Any]:
    """Get category tree structure.
    
    Args:
        category_id: Parent category ID. If omitted, returns root categories.
        
    Returns:
        Category tree structure with nested subcategories
    """
    path = f"/buy/browse/v1/category_tree/{category_id}" if category_id else "/buy/browse/v1/category_tree"
    return make_request("GET", path)


@mcp.tool()
def get_user_reviews(user_id: str, limit: int = 10, offset: int = 0) -> dict[str, Any]:
    """Get reviews for a seller.
    
    Args:
        user_id: The seller's eBay user ID
        limit: Maximum number of reviews to return
        offset: Review offset for pagination
        
    Returns:
        Seller reviews and ratings
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", f"/buy/browse/v1/user/{user_id}/review", params=params)


@mcp.tool()
def get_item_reviews(item_id: str, limit: int = 10, offset: int = 0) -> dict[str, Any]:
    """Get reviews for an item.
    
    Args:
        item_id: The eBay item ID
        limit: Maximum number of reviews to return
        offset: Review offset for pagination
        
    Returns:
        Item reviews and ratings
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", f"/buy/browse/v1/item/{item_id}/review", params=params)


@mcp.tool()
def get_inventory_items(
    sku: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict[str, Any]:
    """Get inventory items (items available for purchase).
    
    Args:
        sku: Filter by SKU
        limit: Maximum number of items to return
        offset: Item offset for pagination
        
    Returns:
        List of inventory items
    """
    params = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    return make_request("GET", "/buy/inventory/v1/inventory_item", params=params)


# ==================== Deal API ====================

@mcp.tool()
def get_deals(
    deal_type: str | None = None,
    status: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict[str, Any]:
    """Get active deals on eBay.
    
    Args:
        deal_type: Filter by deal type (e.g., SALE, BULK_DEAL)
        status: Filter by deal status
        limit: Maximum number of deals to return
        offset: Deal offset for pagination
        
    Returns:
        List of active deals
    """
    params = {"limit": limit, "offset": offset}
    if deal_type:
        params["deal_type"] = deal_type
    if status:
        params["status"] = status
        
    return make_request("GET", "/buy/deal/v1/deal", params=params)


@mcp.tool()
def get_deal_items(deal_id: str, limit: int = 10, offset: int = 0) -> dict[str, Any]:
    """Get items in a specific deal.
    
    Args:
        deal_id: The deal ID
        limit: Maximum number of items to return
        offset: Item offset for pagination
        
    Returns:
        List of items in the deal
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", f"/buy/deal/v1/deal/{deal_id}/item", params=params)


@mcp.tool()
def get_events(
    event_type: str | None = None,
    status: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict[str, Any]:
    """Get events (e.g., eBay live sales, special promotions).
    
    Args:
        event_type: Filter by event type
        status: Filter by event status
        limit: Maximum number of events to return
        offset: Event offset for pagination
        
    Returns:
        List of events
    """
    params = {"limit": limit, "offset": offset}
    if event_type:
        params["event_type"] = event_type
    if status:
        params["status"] = status
        
    return make_request("GET", "/buy/deal/v1/event", params=params)


@mcp.tool()
def get_event_items(event_id: str, limit: int = 10, offset: int = 0) -> dict[str, Any]:
    """Get items in a specific event.
    
    Args:
        event_id: The event ID
        limit: Maximum number of items to return
        offset: Item offset for pagination
        
    Returns:
        List of items in the event
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", f"/buy/deal/v1/event/{event_id}/item", params=params)


# ==================== Feed API ====================

@mcp.tool()
def get_feed_list(
    feed_type: str | None = None,
    status: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict[str, Any]:
    """Get list of feeds (item data exports).
    
    Args:
        feed_type: Filter by feed type
        status: Filter by feed status
        limit: Maximum number of feeds to return
        offset: Feed offset for pagination
        
    Returns:
        List of feeds
    """
    params = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if status:
        params["status"] = status
        
    return make_request("GET", "/sell/feed/v1/feed", params=params)


@mcp.tool()
def get_feed_status(feed_id: str) -> dict[str, Any]:
    """Get status of a specific feed.
    
    Args:
        feed_id: The feed ID
        
    Returns:
        Feed status and processing info
    """
    return make_request("GET", f"/sell/feed/v1/feed/{feed_id}")


@mcp.tool()
def get_feed_result(feed_id: str) -> dict[str, Any]:
    """Get results from a processed feed.
    
    Args:
        feed_id: The feed ID
        
    Returns:
        Feed results data
    """
    return make_request("GET", f"/sell/feed/v1/feed/{feed_id}/result")


@mcp.tool()
def get_snapshot_list(
    snapshot_type: str | None = None,
    status: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict[str, Any]:
    """Get list of snapshots (item data snapshots).
    
    Args:
        snapshot_type: Filter by snapshot type
        status: Filter by snapshot status
        limit: Maximum number of snapshots to return
        offset: Snapshot offset for pagination
        
    Returns:
        List of snapshots
    """
    params = {"limit": limit, "offset": offset}
    if snapshot_type:
        params["snapshot_type"] = snapshot_type
    if status:
        params["status"] = status
        
    return make_request("GET", "/sell/feed/v1/snapshot", params=params)


@mcp.tool()
def get_snapshot_status(snapshot_id: str) -> dict[str, Any]:
    """Get status of a specific snapshot.
    
    Args:
        snapshot_id: The snapshot ID
        
    Returns:
        Snapshot status and processing info
    """
    return make_request("GET", f"/sell/feed/v1/snapshot/{snapshot_id}")


@mcp.tool()
def get_snapshot_result(snapshot_id: str) -> dict[str, Any]:
    """Get results from a processed snapshot.
    
    Args:
        snapshot_id: The snapshot ID
        
    Returns:
        Snapshot results data
    """
    return make_request("GET", f"/sell/feed/v1/snapshot/{snapshot_id}/result")


# ==================== Order API ====================

@mcp.tool()
def create_order(order: dict[str, Any]) -> dict[str, Any]:
    """Create a new order.
    
    Args:
        order: Order details including line items, shipping address, etc.
        
    Returns:
        Created order with order ID
    """
    return make_request("POST", "/buy/order/v1/order", json=order)


@mcp.tool()
def get_order(order_id: str) -> dict[str, Any]:
    """Get details of a specific order.
    
    Args:
        order_id: The order ID
        
    Returns:
        Order details including status, line items, shipping, payments
    """
    return make_request("GET", f"/buy/order/v1/order/{order_id}")


@mcp.tool()
def update_order(order_id: str, update_mask: str, order: dict[str, Any]) -> dict[str, Any]:
    """Update an existing order.
    
    Args:
        order_id: The order ID
        update_mask: Comma-separated list of fields to update
        order: Updated order data
        
    Returns:
        Updated order
    """
    params = {"update_mask": update_mask}
    return make_request("PUT", f"/buy/order/v1/order/{order_id}", params=params, json=order)


@mcp.tool()
def cancel_order(order_id: str, reason: str = "Buyer request") -> dict[str, Any]:
    """Cancel an order.
    
    Args:
        order_id: The order ID
        reason: Reason for cancellation
        
    Returns:
        Cancellation result
    """
    payload = {"reason": reason}
    return make_request("POST", f"/buy/order/v1/order/{order_id}/cancel", json=payload)


@mcp.tool()
def get_order_list(
    states: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict[str, Any]:
    """Get list of orders.
    
    Args:
        states: Filter by order states (comma-separated)
        date_from: Filter orders from this date (ISO 8601 format)
        date_to: Filter orders until this date (ISO 8601 format)
        limit: Maximum number of orders to return
        offset: Order offset for pagination
        
    Returns:
        List of orders matching criteria
    """
    params = {"limit": limit, "offset": offset}
    if states:
        params["states"] = states
    if date_from:
        params["date_from"] = date_from
    if date_to:
        params["date_to"] = date_to
        
    return make_request("GET", "/buy/order/v1/order", params=params)


@mcp.tool()
def create_guest_checkout_session(session: dict[str, Any]) -> dict[str, Any]:
    """Create a guest checkout session.
    
    Args:
        session: Checkout session details including items, shipping info, etc.
        
    Returns:
        Created checkout session with session ID
    """
    return make_request("POST", "/buy/order/v1/guest_checkout_session", json=session)


@mcp.tool()
def get_guest_checkout_session(session_id: str) -> dict[str, Any]:
    """Get details of a guest checkout session.
    
    Args:
        session_id: The checkout session ID
        
    Returns:
        Checkout session details
    """
    return make_request("GET", f"/buy/order/v1/guest_checkout_session/{session_id}")


# ==================== Utility ====================

@mcp.tool()
def get_version() -> dict[str, str]:
    """Get server version information."""
    return {"version": "1.0.0", "api_base": BASE_URL, "environment": ENVIRONMENT}


if __name__ == "__main__":
    mcp.run()
