#!/usr/bin/env python3
"""
eBay Buy API MCP Server

This server provides tools for interacting with the eBay Buy API,
including Browse, Deal, Feed, Marketing, Offer, and Order endpoints.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
server = FastMCP("ebay-buy-api")

# Configuration
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID", "")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URL = (
    "https://api.sandbox.ebay.com"
    if EBAY_ENVIRONMENT == "SANDBOX"
    else "https://api.ebay.com"
)

# OAuth token endpoint
TOKEN_URL = f"{BASE_URL}/identity/v1/oauth2/token"

# Cache for access token
_access_token = None
_token_expiry = 0


def get_access_token() -> str:
    """Get or refresh the OAuth 2.0 access token."""
    global _access_token, _token_expiry
    import time

    current_time = time.time()
    if _access_token and current_time < _token_expiry:
        return _access_token

    try:
        response = requests.post(
            TOKEN_URL,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            },
            auth=(EBAY_APP_ID, EBAY_CERT_ID),
            timeout=10,
        )
        response.raise_for_status()
        token_data = response.json()
        _access_token = token_data["access_token"]
        _token_expiry = current_time + token_data.get("expires_in", 3600) - 60
        return _access_token
    except Exception as e:
        return {"error": f"Failed to get access token: {str(e)}"}


def make_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    json_data: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> dict:
    """Make an authenticated request to the eBay API."""
    try:
        token = get_access_token()
        if isinstance(token, dict) and "error" in token:
            return token

        url = f"{BASE_URL}/buy{endpoint}"
        request_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
        }
        if headers:
            request_headers.update(headers)

        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
            headers=request_headers,
            timeout=30,
        )

        if response.status_code >= 400:
            try:
                error_data = response.json()
                return {"error": error_data}
            except:
                return {"error": f"HTTP {response.status_code}: {response.text}"}

        try:
            return response.json()
        except:
            return {"success": True, "status_code": response.status_code}

    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# BROWSE API TOOLS
# ============================================================================


@server.tool()
def search_items(
    q: str,
    category_ids: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    sort: Optional[str] = None,
    filter: Optional[str] = None,
) -> dict:
    """
    Search for items by keyword or category.

    Args:
        q: The search query (keyword)
        category_ids: Comma-separated category IDs to filter by
        limit: Maximum number of items to return (1-200, default 50)
        offset: Number of items to skip for pagination
        sort: Sort order (e.g., "price", "-price", "newlyListed")
        filter: Additional filters (e.g., "price:[100..500]")

    Returns:
        Search results with matching items
    """
    params = {"q": q, "limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    if sort:
        params["sort"] = sort
    if filter:
        params["filter"] = filter

    return make_request("GET", "/browse/v1/item_summary/search", params=params)


@server.tool()
def search_items_by_image(image_url: str, limit: int = 50) -> dict:
    """
    Search for items using an image URL.

    Args:
        image_url: URL of the image to search with
        limit: Maximum number of items to return

    Returns:
        Search results with matching items
    """
    return make_request(
        "POST",
        "/browse/v1/item_summary/search_by_image",
        json_data={"image_url": image_url},
        params={"limit": limit},
    )


@server.tool()
def get_item(item_id: str, fieldgroups: Optional[str] = None) -> dict:
    """
    Get detailed information about a specific item.

    Args:
        item_id: The eBay item ID
        fieldgroups: Comma-separated field groups (COMPACT, PRODUCT, ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS)

    Returns:
        Detailed item information
    """
    params = {}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups

    return make_request("GET", f"/browse/v1/item/{item_id}", params=params)


@server.tool()
def get_item_by_legacy_id(
    legacy_item_id: str, legacy_variation_id: Optional[str] = None
) -> dict:
    """
    Get item details using a legacy eBay item ID.

    Args:
        legacy_item_id: The legacy eBay item ID
        legacy_variation_id: Optional legacy variation ID for variations

    Returns:
        Item details
    """
    params = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id:
        params["legacy_variation_id"] = legacy_variation_id

    return make_request("GET", "/browse/v1/item/get_item_by_legacy_id", params=params)


@server.tool()
def get_items(item_ids: str) -> dict:
    """
    Get details for multiple items at once.

    Args:
        item_ids: Comma-separated list of item IDs

    Returns:
        Details for all requested items
    """
    params = {"item_ids": item_ids}
    return make_request("GET", "/browse/v1/item", params=params)


@server.tool()
def get_items_by_item_group(item_group_id: str) -> dict:
    """
    Get all items in an item group (variations of the same item).

    Args:
        item_group_id: The item group ID

    Returns:
        All items in the group
    """
    params = {"item_group_id": item_group_id}
    return make_request("GET", "/browse/v1/item/get_items_by_item_group", params=params)


@server.tool()
def check_item_compatibility(item_id: str, compatibility_payload: str) -> dict:
    """
    Check if an item is compatible with specified parts/vehicles.

    Args:
        item_id: The item ID to check
        compatibility_payload: JSON string with compatibility criteria

    Returns:
        Compatibility check results
    """
    try:
        payload = json.loads(compatibility_payload)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON in compatibility_payload"}

    return make_request(
        "POST", f"/browse/v1/item/{item_id}/check_compatibility", json_data=payload
    )


# ============================================================================
# DEAL API TOOLS
# ============================================================================


@server.tool()
def get_deal_items(
    category_ids: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Get current deal items.

    Args:
        category_ids: Comma-separated category IDs to filter deals
        limit: Maximum number of deals to return (1-100, default 20)
        offset: Number of deals to skip for pagination

    Returns:
        List of current deals
    """
    params = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids

    return make_request("GET", "/deal/v1/deal_item", params=params)


@server.tool()
def get_event_items(
    event_ids: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Get items for specific events.

    Args:
        event_ids: Comma-separated event IDs
        limit: Maximum number of items to return (1-100, default 20)
        offset: Number of items to skip for pagination

    Returns:
        Items associated with the events
    """
    params = {"limit": limit, "offset": offset}
    if event_ids:
        params["event_ids"] = event_ids

    return make_request("GET", "/deal/v1/event_item", params=params)


@server.tool()
def get_event(event_id: str) -> dict:
    """
    Get details about a specific event.

    Args:
        event_id: The event ID

    Returns:
        Event details
    """
    return make_request("GET", f"/deal/v1/event/{event_id}")


@server.tool()
def get_events(limit: int = 20, offset: int = 0) -> dict:
    """
    Get all current events.

    Args:
        limit: Maximum number of events to return (1-100, default 20)
        offset: Number of events to skip for pagination

    Returns:
        List of current events
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/deal/v1/event", params=params)


# ============================================================================
# FEED API TOOLS
# ============================================================================


@server.tool()
def get_item_feed(
    category_id: str,
    date: str,
    feed_scope: str = "NEWLY_LISTED",
) -> dict:
    """
    Download an item feed file (TSV_GZIP format).

    Args:
        category_id: The category ID for the feed
        date: The date for the feed (YYYYMMDD format)
        feed_scope: NEWLY_LISTED (daily) or ALL_ACTIVE (weekly bootstrap)

    Returns:
        Feed file download information
    """
    params = {
        "category_id": category_id,
        "date": date,
        "feed_scope": feed_scope,
    }
    return make_request("GET", "/feed/v1/item", params=params)


@server.tool()
def get_item_group_feed(
    category_id: str,
    date: str,
) -> dict:
    """
    Download an item group feed file.

    Args:
        category_id: The category ID for the feed
        date: The date for the feed (YYYYMMDD format)

    Returns:
        Feed file download information
    """
    params = {
        "category_id": category_id,
        "date": date,
    }
    return make_request("GET", "/feed/v1/item_group", params=params)


@server.tool()
def get_item_priority_feed(
    category_id: str,
    date: str,
) -> dict:
    """
    Download an item priority feed file.

    Args:
        category_id: The category ID for the feed
        date: The date for the feed (YYYYMMDD format)

    Returns:
        Feed file download information
    """
    params = {
        "category_id": category_id,
        "date": date,
    }
    return make_request("GET", "/feed/v1/item_priority", params=params)


@server.tool()
def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
) -> dict:
    """
    Download an item snapshot feed file.

    Args:
        category_id: The category ID for the feed
        snapshot_date: The snapshot date (YYYYMMDD format)

    Returns:
        Feed file download information
    """
    params = {
        "category_id": category_id,
        "snapshot_date": snapshot_date,
    }
    return make_request("GET", "/feed/v1/item_snapshot", params=params)


# ============================================================================
# MARKETING API TOOLS
# ============================================================================


@server.tool()
def get_merchandised_products(
    category_id: str,
    limit: int = 30,
) -> dict:
    """
    Get merchandised products for a category.

    Args:
        category_id: The category ID
        limit: Maximum number of products to return (1-100, default 30)

    Returns:
        Merchandised products
    """
    params = {
        "category_id": category_id,
        "limit": limit,
    }
    return make_request("GET", "/marketing/v1/merchandised_product", params=params)


# ============================================================================
# OFFER API TOOLS
# ============================================================================


@server.tool()
def get_bidding(item_id: str) -> dict:
    """
    Get bidding information for an auction item.

    Args:
        item_id: The item ID

    Returns:
        Bidding information
    """
    return make_request("GET", f"/offer/v1/bidding/{item_id}")


@server.tool()
def place_proxy_bid(item_id: str, bid_amount: str) -> dict:
    """
    Place a proxy bid on an auction item.

    Args:
        item_id: The item ID to bid on
        bid_amount: The bid amount (as a string for precision)

    Returns:
        Bid placement result
    """
    return make_request(
        "POST",
        f"/offer/v1/bidding/{item_id}/place_proxy_bid",
        json_data={"max_bid_amount": bid_amount},
    )


# ============================================================================
# ORDER API TOOLS (Guest Checkout)
# ============================================================================


@server.tool()
def initiate_guest_checkout_session(items_payload: str) -> dict:
    """
    Initiate a guest checkout session.

    Args:
        items_payload: JSON string with items to add to cart

    Returns:
        Checkout session details with session ID
    """
    try:
        payload = json.loads(items_payload)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON in items_payload"}

    return make_request(
        "POST",
        "/order/v2/guest_checkout_session/initiate",
        json_data=payload,
    )


@server.tool()
def get_guest_checkout_session(checkout_session_id: str) -> dict:
    """
    Get details of a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID

    Returns:
        Checkout session details
    """
    return make_request(
        "GET",
        f"/order/v2/guest_checkout_session/{checkout_session_id}",
    )


@server.tool()
def apply_guest_coupon(checkout_session_id: str, coupon_code: str) -> dict:
    """
    Apply a coupon code to a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID
        coupon_code: The coupon code to apply

    Returns:
        Updated checkout session
    """
    return make_request(
        "POST",
        f"/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        json_data={"coupon_code": coupon_code},
    )


@server.tool()
def remove_guest_coupon(checkout_session_id: str) -> dict:
    """
    Remove a coupon from a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID

    Returns:
        Updated checkout session
    """
    return make_request(
        "POST",
        f"/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon",
    )


@server.tool()
def update_guest_quantity(
    checkout_session_id: str, line_item_id: str, quantity: int
) -> dict:
    """
    Update the quantity of an item in a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID
        line_item_id: The line item ID to update
        quantity: The new quantity

    Returns:
        Updated checkout session
    """
    return make_request(
        "POST",
        f"/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity",
        json_data={"line_item_id": line_item_id, "quantity": quantity},
    )


@server.tool()
def update_guest_shipping_address(
    checkout_session_id: str, address_payload: str
) -> dict:
    """
    Update the shipping address for a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID
        address_payload: JSON string with address details

    Returns:
        Updated checkout session
    """
    try:
        payload = json.loads(address_payload)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON in address_payload"}

    return make_request(
        "POST",
        f"/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        json_data=payload,
    )


@server.tool()
def update_guest_shipping_option(
    checkout_session_id: str, shipping_option_id: str
) -> dict:
    """
    Update the shipping option for a guest checkout session.

    Args:
        checkout_session_id: The checkout session ID
        shipping_option_id: The shipping option ID to select

    Returns:
        Updated checkout session
    """
    return make_request(
        "POST",
        f"/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        json_data={"shipping_option_id": shipping_option_id},
    )


@server.tool()
def get_guest_purchase_order(purchase_order_id: str) -> dict:
    """
    Get details of a guest purchase order.

    Args:
        purchase_order_id: The purchase order ID

    Returns:
        Purchase order details
    """
    return make_request(
        "GET",
        f"/order/v2/guest_purchase_order/{purchase_order_id}",
    )


if __name__ == "__main__":
    server.run()
