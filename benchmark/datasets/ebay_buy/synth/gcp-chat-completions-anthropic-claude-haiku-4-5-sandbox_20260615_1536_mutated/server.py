#!/usr/bin/env python3
"""eBay Buy API MCP Server - Comprehensive coverage of eBay Buy API endpoints."""

import os
import time
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-buy-api")

# Configuration
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID", "")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

BASE_URL = "https://api.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://api.ebay.com"
APIX_URL = "https://apix.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://apix.ebay.com"

_token_cache = {"token": None, "expires_at": 0}


def get_oauth_token() -> str:
    """Get OAuth 2.0 access token using Client Credentials flow."""
    if _token_cache["token"] and time.time() < _token_cache["expires_at"]:
        return _token_cache["token"]
    
    try:
        response = requests.post(
            f"{BASE_URL}/identity/v1/oauth2/token",
            auth=(EBAY_APP_ID, EBAY_CERT_ID),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"},
            timeout=10,
        )
        response.raise_for_status()
        token_data = response.json()
        _token_cache["token"] = token_data["access_token"]
        _token_cache["expires_at"] = time.time() + token_data.get("expires_in", 3600) - 60
        return _token_cache["token"]
    except Exception as e:
        return {"error": f"Failed to get OAuth token: {str(e)}"}


def make_request(method: str, path: str, params: Optional[dict] = None, json_body: Optional[dict] = None, use_apix: bool = False) -> dict:
    """Make an authenticated request to eBay API."""
    try:
        token = get_oauth_token()
        if isinstance(token, dict) and "error" in token:
            return token
        
        url = f"{'https://apix.sandbox.ebay.com' if use_apix and EBAY_ENVIRONMENT == 'SANDBOX' else 'https://apix.ebay.com' if use_apix else BASE_URL}{path}"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.request(method=method, url=url, params=params, json=json_body, headers=headers, timeout=30)
        
        try:
            return response.json()
        except:
            return {"status": response.status_code, "body": response.text}
    except Exception as e:
        return {"error": str(e)}


# BROWSE API - Item Methods
@mcp.tool()
def browse_get_item(item_id: str, fieldgroups: Optional[str] = None) -> dict:
    """Get details of a specific item."""
    params = {"fieldgroups": fieldgroups} if fieldgroups else {}
    return make_request("GET", f"/buy/browse/v1/item/{item_id}", params=params)


@mcp.tool()
def browse_get_items(item_ids: Optional[str] = None, item_group_ids: Optional[str] = None) -> dict:
    """Get details for multiple items."""
    params = {}
    if item_ids:
        params["item_ids"] = item_ids
    if item_group_ids:
        params["item_group_ids"] = item_group_ids
    return make_request("GET", "/buy/browse/v1/item", params=params)


@mcp.tool()
def browse_get_item_by_legacy_id(legacy_item_id: str, legacy_variation_sku: Optional[str] = None, fieldgroups: Optional[str] = None) -> dict:
    """Get item details using legacy eBay item ID."""
    params = {"legacy_item_id": legacy_item_id}
    if legacy_variation_sku:
        params["legacy_variation_sku"] = legacy_variation_sku
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    return make_request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params=params)


@mcp.tool()
def browse_get_items_by_item_group(item_group_id: str) -> dict:
    """Get details for all items in an item group."""
    return make_request("GET", "/buy/browse/v1/item/get_items_by_item_group", params={"item_group_id": item_group_id})


@mcp.tool()
def browse_check_compatibility(item_id: str, compatibility_properties: dict) -> dict:
    """Check if a product is compatible with specified attributes."""
    return make_request("POST", f"/buy/browse/v1/item/{item_id}/check_compatibility", json_body={"compatibilityProperties": compatibility_properties})


# BROWSE API - Search
@mcp.tool()
def browse_search_items(q: Optional[str] = None, category_ids: Optional[str] = None, limit: int = 50, offset: int = 0, sort: Optional[str] = None, filter: Optional[str] = None, fieldgroups: Optional[str] = None, aspect_filter: Optional[str] = None) -> dict:
    """Search for items by keyword, category, or other criteria."""
    params = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if sort:
        params["sort"] = sort
    if filter:
        params["filter"] = filter
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    return make_request("GET", "/buy/browse/v1/item_summary/search", params=params)


@mcp.tool()
def browse_search_by_image(image: str, category_ids: Optional[str] = None, limit: int = 50, offset: int = 0) -> dict:
    """Search for items by image."""
    params = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    return make_request("POST", "/buy/browse/v1/item_summary/search_by_image", params=params, json_body={"image": image})


# DEAL API
@mcp.tool()
def deal_get_deal_items(category_ids: Optional[str] = None, max_results: int = 20, offset: int = 0) -> dict:
    """Get current deals and promotions."""
    params = {"max_results": max_results, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    return make_request("GET", "/buy/deal/v1/deal_item", params=params)


@mcp.tool()
def deal_get_events() -> dict:
    """Get all available deal events."""
    return make_request("GET", "/buy/deal/v1/event")


@mcp.tool()
def deal_get_event(event_id: str) -> dict:
    """Get details of a specific deal event."""
    return make_request("GET", f"/buy/deal/v1/event/{event_id}")


@mcp.tool()
def deal_get_event_items(event_ids: str, max_results: int = 20, offset: int = 0) -> dict:
    """Get items for specific deal events."""
    params = {"event_ids": event_ids, "max_results": max_results, "offset": offset}
    return make_request("GET", "/buy/deal/v1/event_item", params=params)


# FEED API
@mcp.tool()
def feed_get_item_feed(feed_scope: str, category_id: str, date: str, limit: int = 100, offset: int = 0) -> dict:
    """Get item feed for a category."""
    params = {"feed_scope": feed_scope, "category_id": category_id, "date": date, "limit": limit, "offset": offset}
    return make_request("GET", "/buy/feed/v1_beta/item", params=params)


@mcp.tool()
def feed_get_item_group_feed(feed_scope: str, category_id: str, date: str, limit: int = 100, offset: int = 0) -> dict:
    """Get item group feed for a category."""
    params = {"feed_scope": feed_scope, "category_id": category_id, "date": date, "limit": limit, "offset": offset}
    return make_request("GET", "/buy/feed/v1_beta/item_group", params=params)


@mcp.tool()
def feed_get_item_snapshot_feed(category_id: str, snapshot_date: str, limit: int = 100, offset: int = 0) -> dict:
    """Get item snapshot feed showing changes to items."""
    params = {"category_id": category_id, "snapshot_date": snapshot_date, "limit": limit, "offset": offset}
    return make_request("GET", "/buy/feed/v1_beta/item_snapshot", params=params)


@mcp.tool()
def feed_get_item_priority_feed(category_id: str, date: str, limit: int = 100, offset: int = 0) -> dict:
    """Get priority item feed for a category."""
    params = {"category_id": category_id, "date": date, "limit": limit, "offset": offset}
    return make_request("GET", "/buy/feed/v1_beta/item_priority", params=params)


# MARKETING API
@mcp.tool()
def marketing_get_merchandised_products(category_id: str, metric_name: str, limit: int = 100, offset: int = 0) -> dict:
    """Get merchandised products for a category."""
    params = {"category_id": category_id, "metric_name": metric_name, "limit": limit, "offset": offset}
    return make_request("GET", "/buy/marketing/v1_beta/merchandised_product", params=params)


# OFFER API
@mcp.tool()
def offer_get_bidding(item_id: str) -> dict:
    """Get bidding information for an auction item."""
    return make_request("GET", f"/buy/offer/v1_beta/bidding/{item_id}")


@mcp.tool()
def offer_place_proxy_bid(item_id: str, max_bid_amount: float) -> dict:
    """Place a proxy bid on an auction item."""
    return make_request("POST", f"/buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid", json_body={"maxBidAmount": str(max_bid_amount)})


# ORDER API - Guest Checkout
@mcp.tool()
def order_initiate_guest_checkout(contact_email: str, line_items: list, shipping_address: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Initiate a guest checkout session."""
    try:
        token = get_oauth_token()
        if isinstance(token, dict) and "error" in token:
            return token
        
        url = f"{APIX_URL}/buy/order/v2/guest_checkout_session/initiate"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
        body = {"contactEmail": contact_email, "lineItemInputs": line_items, "shippingAddress": shipping_address}
        response = requests.post(url, json=body, headers=headers, timeout=30)
        
        try:
            return response.json()
        except:
            return {"status": response.status_code, "body": response.text}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def order_get_guest_checkout_session(checkout_session_id: str) -> dict:
    """Get details of a guest checkout session."""
    return make_request("GET", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}", use_apix=True)


@mcp.tool()
def order_update_guest_quantity(checkout_session_id: str, line_item_id: str, quantity: int) -> dict:
    """Update item quantity in a guest checkout session."""
    return make_request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity", json_body={"lineItemId": line_item_id, "quantity": quantity}, use_apix=True)


@mcp.tool()
def order_update_guest_shipping_address(checkout_session_id: str, shipping_address: dict) -> dict:
    """Update shipping address in a guest checkout session."""
    return make_request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address", json_body={"shippingAddress": shipping_address}, use_apix=True)


@mcp.tool()
def order_update_guest_shipping_option(checkout_session_id: str, line_item_id: str, shipping_option_id: str) -> dict:
    """Update shipping option for a line item in guest checkout."""
    return make_request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option", json_body={"lineItemId": line_item_id, "shippingOptionId": shipping_option_id}, use_apix=True)


@mcp.tool()
def order_apply_guest_coupon(checkout_session_id: str, coupon_code: str) -> dict:
    """Apply a coupon code to a guest checkout session."""
    return make_request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon", json_body={"couponCode": coupon_code}, use_apix=True)


@mcp.tool()
def order_remove_guest_coupon(checkout_session_id: str, coupon_code: str) -> dict:
    """Remove a coupon from a guest checkout session."""
    return make_request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon", json_body={"couponCode": coupon_code}, use_apix=True)


@mcp.tool()
def order_get_guest_purchase_order(purchase_order_id: str) -> dict:
    """Get details of a guest purchase order."""
    return make_request("GET", f"/buy/order/v2/guest_purchase_order/{purchase_order_id}", use_apix=True)


if __name__ == "__main__":
    mcp.run()
