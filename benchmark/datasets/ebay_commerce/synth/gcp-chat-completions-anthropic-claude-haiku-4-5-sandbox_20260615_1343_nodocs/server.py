#!/usr/bin/env python3
"""
MCP Server for eBay Commerce API
Implements tools for Catalog, Taxonomy, Identity, Media, Notification, and Charity APIs
"""

import os
import json
import base64
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("ebay-commerce")

# Configuration from environment
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID", "")
EBAY_REFRESH_TOKEN = os.getenv("EBAY_REFRESH_TOKEN", "")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URL = "https://api.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://api.ebay.com"
MEDIA_BASE_URL = "https://apim.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://apim.ebay.com"

# Token cache
_app_token_cache = None
_user_token_cache = None


def get_app_token() -> str:
    """Get OAuth app token using client credentials grant"""
    global _app_token_cache
    if _app_token_cache:
        return _app_token_cache
    
    auth_string = base64.b64encode(f"{EBAY_APP_ID}:{EBAY_CERT_ID}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_string}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/identity/v1/oauth2/token", headers=headers, data=data)
        response.raise_for_status()
        _app_token_cache = response.json()["access_token"]
        return _app_token_cache
    except Exception as e:
        return f"Error getting app token: {str(e)}"


def get_user_token() -> str:
    """Get OAuth user token using refresh token grant"""
    global _user_token_cache
    if _user_token_cache:
        return _user_token_cache
    
    auth_string = base64.b64encode(f"{EBAY_APP_ID}:{EBAY_CERT_ID}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_string}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN
    }
    
    try:
        response = requests.post(f"{BASE_URL}/identity/v1/oauth2/token", headers=headers, data=data)
        response.raise_for_status()
        _user_token_cache = response.json()["access_token"]
        return _user_token_cache
    except Exception as e:
        return f"Error getting user token: {str(e)}"


def make_request(method: str, endpoint: str, token_type: str = "app", **kwargs) -> dict:
    """Make authenticated request to eBay API"""
    if token_type == "app":
        token = get_app_token()
        base = BASE_URL
    else:
        token = get_user_token()
        base = BASE_URL
    
    # Special handling for media API
    if "/commerce/media/" in endpoint:
        base = MEDIA_BASE_URL
    
    url = f"{base}{endpoint}"
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Bearer {token}"
    headers["Content-Type"] = "application/json"
    
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        if response.status_code >= 400:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
        return response.json() if response.text else {}
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# CATALOG API TOOLS
# ============================================================================

@server.tool()
def search_catalog_products(q: str, limit: int = 10, offset: int = 0) -> dict:
    """Search for products in the eBay catalog"""
    params = {
        "q": q,
        "limit": limit,
        "offset": offset
    }
    return make_request("GET", "/commerce/catalog/v1/product_summary/search", "app", params=params)


@server.tool()
def get_product_by_id(product_id: str) -> dict:
    """Get detailed product information by product ID"""
    return make_request("GET", f"/commerce/catalog/v1/product/{product_id}", "app")


@server.tool()
def get_product_by_sku(sku: str) -> dict:
    """Get product information by SKU"""
    params = {"sku": sku}
    return make_request("GET", "/commerce/catalog/v1/product_summary/search", "app", params=params)


@server.tool()
def get_product_by_upc(upc: str) -> dict:
    """Get product information by UPC"""
    params = {"upc": upc}
    return make_request("GET", "/commerce/catalog/v1/product_summary/search", "app", params=params)


@server.tool()
def get_product_by_ean(ean: str) -> dict:
    """Get product information by EAN"""
    params = {"ean": ean}
    return make_request("GET", "/commerce/catalog/v1/product_summary/search", "app", params=params)


# ============================================================================
# TAXONOMY API TOOLS
# ============================================================================

@server.tool()
def get_category_tree(category_tree_id: str) -> dict:
    """Get the complete category tree for a marketplace"""
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}", "app")


@server.tool()
def get_category_suggestions(q: str, category_tree_id: str) -> dict:
    """Get category suggestions based on keywords"""
    params = {
        "q": q,
        "category_tree_id": category_tree_id
    }
    return make_request("GET", "/commerce/taxonomy/v1/category_tree/get_category_suggestions", "app", params=params)


@server.tool()
def get_category_aspects(category_id: str, category_tree_id: str) -> dict:
    """Get aspects for a category"""
    params = {"category_tree_id": category_tree_id}
    return make_request("GET", f"/commerce/taxonomy/v1/category/{category_id}/aspects", "app", params=params)


@server.tool()
def get_item_aspects_for_category(category_id: str, category_tree_id: str) -> dict:
    """Get item aspects for a specific category"""
    params = {"category_tree_id": category_tree_id}
    return make_request("GET", f"/commerce/taxonomy/v1/category/{category_id}/item_aspects", "app", params=params)


@server.tool()
def get_compatibility_properties(category_id: str, category_tree_id: str) -> dict:
    """Get compatibility properties for a category"""
    params = {"category_tree_id": category_tree_id}
    return make_request("GET", f"/commerce/taxonomy/v1/category/{category_id}/compatibility_properties", "app", params=params)


@server.tool()
def get_compatibility_property_values(category_id: str, property_name: str, category_tree_id: str) -> dict:
    """Get values for a compatibility property"""
    params = {"category_tree_id": category_tree_id}
    return make_request("GET", f"/commerce/taxonomy/v1/category/{category_id}/compatibility_properties/{property_name}/values", "app", params=params)


# ============================================================================
# IDENTITY API TOOLS
# ============================================================================

@server.tool()
def get_user_profile() -> dict:
    """Get the authenticated user's profile information"""
    return make_request("GET", "/commerce/identity/v1/user", "user")


# ============================================================================
# MEDIA API TOOLS
# ============================================================================

@server.tool()
def upload_image(image_data: str, content_type: str = "image/jpeg") -> dict:
    """Upload an image to eBay Media Service
    
    Args:
        image_data: Base64-encoded image data
        content_type: MIME type (image/jpeg, image/png, etc.)
    """
    headers = {
        "Content-Type": content_type
    }
    # Decode base64 to binary
    try:
        image_bytes = base64.b64decode(image_data)
    except Exception as e:
        return {"error": f"Invalid base64 image data: {str(e)}"}
    
    return make_request("POST", "/commerce/media/v1/image", "user", headers=headers, data=image_bytes)


@server.tool()
def get_image_details(image_id: str) -> dict:
    """Get details about an uploaded image"""
    return make_request("GET", f"/commerce/media/v1/image/{image_id}", "user")


@server.tool()
def delete_image(image_id: str) -> dict:
    """Delete an uploaded image"""
    return make_request("DELETE", f"/commerce/media/v1/image/{image_id}", "user")


@server.tool()
def upload_video(video_data: str, content_type: str = "video/mp4") -> dict:
    """Upload a video to eBay Media Service
    
    Args:
        video_data: Base64-encoded video data
        content_type: MIME type (video/mp4, video/quicktime, etc.)
    """
    headers = {
        "Content-Type": content_type
    }
    try:
        video_bytes = base64.b64decode(video_data)
    except Exception as e:
        return {"error": f"Invalid base64 video data: {str(e)}"}
    
    return make_request("POST", "/commerce/media/v1/video", "user", headers=headers, data=video_bytes)


@server.tool()
def get_video_details(video_id: str) -> dict:
    """Get details about an uploaded video"""
    return make_request("GET", f"/commerce/media/v1/video/{video_id}", "user")


@server.tool()
def delete_video(video_id: str) -> dict:
    """Delete an uploaded video"""
    return make_request("DELETE", f"/commerce/media/v1/video/{video_id}", "user")


# ============================================================================
# NOTIFICATION API TOOLS
# ============================================================================

@server.tool()
def get_subscriptions() -> dict:
    """Get all webhook subscriptions for the user"""
    return make_request("GET", "/commerce/notification/v1/subscription", "user")


@server.tool()
def create_subscription(delivery_url: str, event_types: list) -> dict:
    """Create a new webhook subscription
    
    Args:
        delivery_url: URL where webhooks will be delivered
        event_types: List of event types to subscribe to (e.g., ["ITEM.CREATED", "ITEM.UPDATED"])
    """
    payload = {
        "deliveryUrl": delivery_url,
        "eventTypes": event_types
    }
    return make_request("POST", "/commerce/notification/v1/subscription", "user", json=payload)


@server.tool()
def get_subscription(subscription_id: str) -> dict:
    """Get details about a specific subscription"""
    return make_request("GET", f"/commerce/notification/v1/subscription/{subscription_id}", "user")


@server.tool()
def update_subscription(subscription_id: str, delivery_url: str = None, event_types: list = None) -> dict:
    """Update a webhook subscription"""
    payload = {}
    if delivery_url:
        payload["deliveryUrl"] = delivery_url
    if event_types:
        payload["eventTypes"] = event_types
    
    return make_request("PUT", f"/commerce/notification/v1/subscription/{subscription_id}", "user", json=payload)


@server.tool()
def delete_subscription(subscription_id: str) -> dict:
    """Delete a webhook subscription"""
    return make_request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}", "user")


@server.tool()
def get_subscription_events(subscription_id: str, limit: int = 100) -> dict:
    """Get events for a subscription"""
    params = {"limit": limit}
    return make_request("GET", f"/commerce/notification/v1/subscription/{subscription_id}/event", "user", params=params)


@server.tool()
def get_event_details(subscription_id: str, event_id: str) -> dict:
    """Get details about a specific event"""
    return make_request("GET", f"/commerce/notification/v1/subscription/{subscription_id}/event/{event_id}", "user")


# ============================================================================
# CHARITY API TOOLS
# ============================================================================

@server.tool()
def search_charities(q: str, limit: int = 10) -> dict:
    """Search for charities by name or keyword"""
    params = {
        "q": q,
        "limit": limit
    }
    return make_request("GET", "/commerce/charity/v1/charity_org", "app", params=params)


@server.tool()
def get_charity_by_id(charity_id: str) -> dict:
    """Get details about a specific charity"""
    return make_request("GET", f"/commerce/charity/v1/charity_org/{charity_id}", "app")


# ============================================================================
# TRANSLATION API TOOLS
# ============================================================================

@server.tool()
def translate_text(text: str, from_language: str, to_language: str) -> dict:
    """Translate text between languages
    
    Args:
        text: Text to translate
        from_language: Source language code (e.g., "en")
        to_language: Target language code (e.g., "es")
    """
    payload = {
        "text": text,
        "from": from_language,
        "to": to_language
    }
    return make_request("POST", "/commerce/translation/v1/translate", "app", json=payload)


@server.tool()
def translate_listing(listing_id: str, from_language: str, to_language: str) -> dict:
    """Translate a listing to another language"""
    payload = {
        "listingId": listing_id,
        "from": from_language,
        "to": to_language
    }
    return make_request("POST", "/commerce/translation/v1/translate_listing", "app", json=payload)


if __name__ == "__main__":
    server.run()
