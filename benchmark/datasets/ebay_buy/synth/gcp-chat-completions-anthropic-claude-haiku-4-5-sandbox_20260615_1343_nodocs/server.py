#!/usr/bin/env python3
"""
MCP Server for eBay Buy API

Provides tools for searching items, getting item details, managing shopping carts,
creating orders, and accessing deals and feeds.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("ebay-buy-api")

# Configuration from environment
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
OAUTH_URL = f"{BASE_URL}/identity/v1/oauth2/token"

# Cache for access token
_access_token = None
_token_expiry = 0


def get_access_token() -> str:
    """Get OAuth 2.0 access token using Client Credentials flow."""
    global _access_token, _token_expiry
    import time

    # Return cached token if still valid
    if _access_token and time.time() < _token_expiry:
        return _access_token

    try:
        response = requests.post(
            OAUTH_URL,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            auth=(EBAY_APP_ID, EBAY_CERT_ID),
            data={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"},
        )
        response.raise_for_status()
        data = response.json()
        _access_token = data["access_token"]
        _token_expiry = time.time() + data.get("expires_in", 3600) - 60
        return _access_token
    except Exception as e:
        return f"error:failed_to_get_token:{str(e)}"


def api_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    json_body: Optional[dict] = None,
) -> dict:
    """Make an authenticated request to the eBay Buy API."""
    try:
        token = get_access_token()
        if token.startswith("error:"):
            return {"error": token}

        url = f"{BASE_URL}{endpoint}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_body,
            timeout=30,
        )

        # Handle different status codes
        if response.status_code == 204:
            return {"success": True}
        elif response.status_code >= 400:
            try:
                error_data = response.json()
                return {"error": error_data}
            except:
                return {"error": f"HTTP {response.status_code}: {response.text}"}

        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# ============================================================================
# BROWSE API - Search and Item Details
# ============================================================================


@server.tool()
def search_items(
    q: str,
    limit: int = 50,
    offset: int = 0,
    sort: Optional[str] = None,
    category_ids: Optional[str] = None,
    condition: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
) -> dict:
    """
    Search for items on eBay.

    Args:
        q: Search query string
        limit: Maximum number of results (1-200, default 50)
        offset: Number of results to skip for pagination
        sort: Sort order (e.g., "price", "newlyListed", "endingSoonest")
        category_ids: Comma-separated category IDs to filter by
        condition: Item condition filter (e.g., "New", "Used", "Refurbished")
        price_min: Minimum price filter
        price_max: Maximum price filter

    Returns:
        Search results with items and pagination info
    """
    params = {
        "q": q,
        "limit": min(limit, 200),
        "offset": offset,
    }

    if sort:
        params["sort"] = sort
    if category_ids:
        params["category_ids"] = category_ids
    if condition:
        params["filter"] = f"conditions:{condition}"
    if price_min is not None or price_max is not None:
        price_filter = "price:"
        if price_min is not None:
            price_filter += f"[{price_min}.."
        if price_max is not None:
            price_filter += f"..{price_max}]"
        else:
            price_filter += "..]"
        params["filter"] = price_filter

    return api_request("GET", "/buy/browse/v1/item_summary/search", params=params)


@server.tool()
def get_item(item_id: str) -> dict:
    """
    Get detailed information about a specific item.

    Args:
        item_id: The eBay item ID

    Returns:
        Complete item details including price, condition, shipping, etc.
    """
    return api_request("GET", f"/buy/browse/v1/item/{item_id}")


@server.tool()
def get_item_by_legacy_id(legacy_item_id: str, legacy_variation_id: Optional[str] = None) -> dict:
    """
    Get item details using legacy eBay item ID format.

    Args:
        legacy_item_id: The legacy format item ID
        legacy_variation_id: Optional legacy variation ID for multi-variation items

    Returns:
        Item details
    """
    params = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id:
        params["legacy_variation_id"] = legacy_variation_id

    return api_request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params=params)


@server.tool()
def get_items_by_ids(item_ids: str) -> dict:
    """
    Get details for multiple items at once.

    Args:
        item_ids: Comma-separated list of item IDs (max 20)

    Returns:
        List of item details
    """
    params = {"item_ids": item_ids}
    return api_request("GET", "/buy/browse/v1/item", params=params)


@server.tool()
def get_item_variations(item_id: str) -> dict:
    """
    Get all variations (colors, sizes, etc.) for a multi-variation item.

    Args:
        item_id: The eBay item ID

    Returns:
        List of variations with their details and availability
    """
    return api_request("GET", f"/buy/browse/v1/item/{item_id}/get_variations")


@server.tool()
def get_item_groups(item_id: str) -> dict:
    """
    Get item groups (related items) for a specific item.

    Args:
        item_id: The eBay item ID

    Returns:
        Related items grouped by type
    """
    return api_request("GET", f"/buy/browse/v1/item_group/{item_id}")


@server.tool()
def get_shopping_cart() -> dict:
    """
    Get the current shopping cart contents.

    Returns:
        Cart items, quantities, and pricing
    """
    return api_request("GET", "/buy/browse/v1/shopping_cart")


@server.tool()
def add_item_to_cart(item_id: str, quantity: int = 1) -> dict:
    """
    Add an item to the shopping cart.

    Args:
        item_id: The eBay item ID
        quantity: Number of items to add (default 1)

    Returns:
        Updated cart information
    """
    body = {
        "items": [
            {
                "item_id": item_id,
                "quantity": quantity,
            }
        ]
    }
    return api_request("POST", "/buy/browse/v1/shopping_cart/add_item", json_body=body)


@server.tool()
def remove_item_from_cart(cart_item_id: str) -> dict:
    """
    Remove an item from the shopping cart.

    Args:
        cart_item_id: The cart item ID (from get_shopping_cart)

    Returns:
        Updated cart information
    """
    return api_request("DELETE", f"/buy/browse/v1/shopping_cart/remove_item/{cart_item_id}")


@server.tool()
def update_cart_item_quantity(cart_item_id: str, quantity: int) -> dict:
    """
    Update the quantity of an item in the cart.

    Args:
        cart_item_id: The cart item ID
        quantity: New quantity

    Returns:
        Updated cart information
    """
    body = {"quantity": quantity}
    return api_request(
        "PUT",
        f"/buy/browse/v1/shopping_cart/update_quantity/{cart_item_id}",
        json_body=body,
    )


# ============================================================================
# DEAL API - Deals and Events
# ============================================================================


@server.tool()
def get_deals(
    limit: int = 20,
    offset: int = 0,
    category_ids: Optional[str] = None,
) -> dict:
    """
    Get current eBay deals.

    Args:
        limit: Maximum number of deals to return (1-100, default 20)
        offset: Number of deals to skip for pagination
        category_ids: Comma-separated category IDs to filter deals

    Returns:
        List of active deals with details
    """
    params = {
        "limit": min(limit, 100),
        "offset": offset,
    }
    if category_ids:
        params["category_ids"] = category_ids

    return api_request("GET", "/buy/deal/v1/deal", params=params)


@server.tool()
def get_deal_by_id(deal_id: str) -> dict:
    """
    Get details for a specific deal.

    Args:
        deal_id: The deal ID

    Returns:
        Deal details including items, discount, and expiration
    """
    return api_request("GET", f"/buy/deal/v1/deal/{deal_id}")


@server.tool()
def get_deal_events(
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Get upcoming eBay deal events.

    Args:
        limit: Maximum number of events (1-100, default 20)
        offset: Number of events to skip

    Returns:
        List of upcoming deal events
    """
    params = {
        "limit": min(limit, 100),
        "offset": offset,
    }
    return api_request("GET", "/buy/deal/v1/event", params=params)


@server.tool()
def get_event_by_id(event_id: str) -> dict:
    """
    Get details for a specific deal event.

    Args:
        event_id: The event ID

    Returns:
        Event details including start time, end time, and deals
    """
    return api_request("GET", f"/buy/deal/v1/event/{event_id}")


# ============================================================================
# FEED API - Item Feeds and Snapshots
# ============================================================================


@server.tool()
def get_item_feed(
    feed_scope: str = "ALL_ACTIVE",
    category_id: Optional[str] = None,
    limit: int = 100,
    continuation_token: Optional[str] = None,
) -> dict:
    """
    Get a feed of items (for bulk operations or monitoring).

    Args:
        feed_scope: Scope of items (e.g., "ALL_ACTIVE", "NEWLY_LISTED")
        category_id: Optional category ID to filter items
        limit: Maximum items per request (1-100, default 100)
        continuation_token: Token for continuing a previous request

    Returns:
        List of items and continuation token for pagination
    """
    params = {
        "feed_scope": feed_scope,
        "limit": min(limit, 100),
    }
    if category_id:
        params["category_id"] = category_id
    if continuation_token:
        params["continuation_token"] = continuation_token

    return api_request("GET", "/buy/feed/v1/item", params=params)


@server.tool()
def get_item_snapshot_feed(
    snapshot_date: str,
    category_id: str,
    continuation_token: Optional[str] = None,
) -> dict:
    """
    Get a snapshot feed of items for a specific date and category.

    Args:
        snapshot_date: Date in YYYYMMDD format
        category_id: Category ID for the snapshot
        continuation_token: Token for continuing a previous request

    Returns:
        Snapshot items and continuation token
    """
    params = {
        "snapshot_date": snapshot_date,
        "category_id": category_id,
    }
    if continuation_token:
        params["continuation_token"] = continuation_token

    return api_request("GET", "/buy/feed/v1/item_snapshot", params=params)


# ============================================================================
# ORDER API - Guest Checkout and Order Management
# ============================================================================


@server.tool()
def create_guest_checkout(
    line_items: list,
    shipping_address: dict,
    shipping_method: Optional[str] = None,
    payment_method: Optional[dict] = None,
) -> dict:
    """
    Create a guest checkout (order) without requiring an eBay account.

    Args:
        line_items: List of items with format [{"item_id": "...", "quantity": 1}, ...]
        shipping_address: Address dict with keys: street, city, state, postal_code, country
        shipping_method: Preferred shipping method (optional)
        payment_method: Payment details (optional)

    Returns:
        Order confirmation with order ID and details
    """
    body = {
        "line_items": line_items,
        "shipping_address": shipping_address,
    }
    if shipping_method:
        body["shipping_method"] = shipping_method
    if payment_method:
        body["payment_method"] = payment_method

    return api_request("POST", "/buy/order/v1/guest_checkout", json_body=body)


@server.tool()
def get_guest_order(order_id: str) -> dict:
    """
    Get details for a guest checkout order.

    Args:
        order_id: The order ID from create_guest_checkout

    Returns:
        Order details including items, shipping, and status
    """
    return api_request("GET", f"/buy/order/v1/guest_order/{order_id}")


@server.tool()
def estimate_shipping(
    line_items: list,
    shipping_address: dict,
) -> dict:
    """
    Estimate shipping costs for items to a specific address.

    Args:
        line_items: List of items with format [{"item_id": "...", "quantity": 1}, ...]
        shipping_address: Address dict with keys: street, city, state, postal_code, country

    Returns:
        Estimated shipping costs and available methods
    """
    body = {
        "line_items": line_items,
        "shipping_address": shipping_address,
    }
    return api_request("POST", "/buy/order/v1/estimate_shipping", json_body=body)


# ============================================================================
# MARKETPLACE INSIGHTS API - Market Data
# ============================================================================


@server.tool()
def get_item_market_insights(item_id: str) -> dict:
    """
    Get market insights for an item (pricing trends, demand, etc.).

    Args:
        item_id: The eBay item ID

    Returns:
        Market data including price trends and demand metrics
    """
    return api_request("GET", f"/buy/marketplace_insights/v1/item_market_insights/{item_id}")


@server.tool()
def search_item_market_insights(
    q: str,
    limit: int = 10,
    category_ids: Optional[str] = None,
) -> dict:
    """
    Search for market insights across multiple items.

    Args:
        q: Search query
        limit: Maximum results (1-100, default 10)
        category_ids: Optional category IDs to filter

    Returns:
        Market insights for matching items
    """
    params = {
        "q": q,
        "limit": min(limit, 100),
    }
    if category_ids:
        params["category_ids"] = category_ids

    return api_request("GET", "/buy/marketplace_insights/v1/item_market_insights/search", params=params)


# ============================================================================
# RECOMMENDATION API - Personalized Recommendations
# ============================================================================


@server.tool()
def get_item_recommendations(item_id: str, limit: int = 10) -> dict:
    """
    Get recommended items based on a specific item.

    Args:
        item_id: The eBay item ID to base recommendations on
        limit: Maximum recommendations (1-20, default 10)

    Returns:
        List of recommended items
    """
    params = {
        "item_id": item_id,
        "limit": min(limit, 20),
    }
    return api_request("GET", "/buy/recommendation/v1/item_recommendation", params=params)


# ============================================================================
# COMMERCE CATALOG API - Category and Aspect Data
# ============================================================================


@server.tool()
def get_category_tree(category_tree_id: str) -> dict:
    """
    Get the category tree for a marketplace.

    Args:
        category_tree_id: The category tree ID (e.g., "0" for US)

    Returns:
        Complete category hierarchy
    """
    return api_request("GET", f"/commerce/catalog/v1/category_tree/{category_tree_id}")


@server.tool()
def get_category_suggestions(
    q: str,
    category_tree_id: str = "0",
) -> dict:
    """
    Get category suggestions for a search query.

    Args:
        q: Search query
        category_tree_id: Category tree ID (default "0" for US)

    Returns:
        Suggested categories
    """
    params = {
        "q": q,
        "category_tree_id": category_tree_id,
    }
    return api_request("GET", "/commerce/catalog/v1/category_tree/get_category_suggestions", params=params)


@server.tool()
def get_item_aspects(
    category_id: str,
    category_tree_id: str = "0",
) -> dict:
    """
    Get item aspects (attributes) for a category.

    Args:
        category_id: The category ID
        category_tree_id: Category tree ID (default "0" for US)

    Returns:
        List of aspects/attributes for the category
    """
    params = {
        "category_id": category_id,
        "category_tree_id": category_tree_id,
    }
    return api_request("GET", "/commerce/catalog/v1/item_aspects", params=params)


# ============================================================================
# TAXONOMY API - Category and Aspect Metadata
# ============================================================================


@server.tool()
def get_default_category_and_aspects(
    q: str,
    category_tree_id: str = "0",
) -> dict:
    """
    Get the default category and aspects for a search query.

    Args:
        q: Search query
        category_tree_id: Category tree ID (default "0" for US)

    Returns:
        Default category and applicable aspects
    """
    params = {
        "q": q,
        "category_tree_id": category_tree_id,
    }
    return api_request("GET", "/commerce/taxonomy/v1/get_default_category_and_aspects", params=params)


@server.tool()
def get_category_aspects(
    category_id: str,
    category_tree_id: str = "0",
) -> dict:
    """
    Get aspects for a specific category.

    Args:
        category_id: The category ID
        category_tree_id: Category tree ID (default "0" for US)

    Returns:
        List of aspects for the category
    """
    params = {
        "category_id": category_id,
        "category_tree_id": category_tree_id,
    }
    return api_request("GET", "/commerce/taxonomy/v1/category_aspects", params=params)


# ============================================================================
# TRANSLATION API - Multi-language Support
# ============================================================================


@server.tool()
def translate_text(
    text: str,
    from_language_code: str,
    to_language_code: str,
) -> dict:
    """
    Translate text between languages.

    Args:
        text: Text to translate
        from_language_code: Source language code (e.g., "en")
        to_language_code: Target language code (e.g., "es")

    Returns:
        Translated text
    """
    body = {
        "text": text,
        "from_language_code": from_language_code,
        "to_language_code": to_language_code,
    }
    return api_request("POST", "/commerce/translation/v1/translate", json_body=body)


# ============================================================================
# MEDIA API - Image and Video Management
# ============================================================================


@server.tool()
def get_item_images(item_id: str) -> dict:
    """
    Get all images for an item.

    Args:
        item_id: The eBay item ID

    Returns:
        List of image URLs and metadata
    """
    return api_request("GET", f"/buy/media/v1/item/{item_id}/image")


# ============================================================================
# NOTIFICATION API - Subscription Management
# ============================================================================


@server.tool()
def get_subscriptions() -> dict:
    """
    Get all active notification subscriptions.

    Returns:
        List of subscriptions with topics and endpoints
    """
    return api_request("GET", "/commerce/notification/v1/subscription")


@server.tool()
def create_subscription(
    topic: str,
    destination: str,
    verification_token: Optional[str] = None,
) -> dict:
    """
    Create a new notification subscription.

    Args:
        topic: Notification topic (e.g., "ITEM_SOLD", "ITEM_UNSOLD")
        destination: Webhook URL to receive notifications
        verification_token: Optional token for webhook verification

    Returns:
        Subscription details with ID
    """
    body = {
        "topic": topic,
        "destination": destination,
    }
    if verification_token:
        body["verification_token"] = verification_token

    return api_request("POST", "/commerce/notification/v1/subscription", json_body=body)


@server.tool()
def delete_subscription(subscription_id: str) -> dict:
    """
    Delete a notification subscription.

    Args:
        subscription_id: The subscription ID

    Returns:
        Confirmation of deletion
    """
    return api_request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}")


if __name__ == "__main__":
    server.run()
