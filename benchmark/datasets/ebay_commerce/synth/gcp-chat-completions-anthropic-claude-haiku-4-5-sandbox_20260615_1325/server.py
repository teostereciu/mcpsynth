#!/usr/bin/env python3
"""
eBay Commerce API MCP Server

This server implements tools for interacting with the eBay Commerce API,
including Catalog, Charity, Identity, Media, Notification, Taxonomy, and Translation APIs.
"""

import os
import json
import base64
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("ebay-commerce")

# Configuration
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID", "")
EBAY_REFRESH_TOKEN = os.getenv("EBAY_REFRESH_TOKEN", "")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URL = "https://api.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://api.ebay.com"
MEDIA_BASE_URL = "https://apim.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://apim.ebay.com"
IDENTITY_BASE_URL = "https://apiz.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://apiz.ebay.com"

# Token cache
_app_token_cache = None
_user_token_cache = None


def get_app_token() -> str:
    """Get an app token using client credentials grant."""
    global _app_token_cache
    
    if _app_token_cache:
        return _app_token_cache
    
    auth_string = base64.b64encode(f"{EBAY_APP_ID}:{EBAY_CERT_ID}".encode()).decode()
    
    response = requests.post(
        f"{BASE_URL}/identity/v1/oauth2/token",
        headers={
            "Authorization": f"Basic {auth_string}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope"
        }
    )
    
    if response.status_code != 200:
        return {"error": f"Failed to get app token: {response.text}"}
    
    token = response.json().get("access_token")
    _app_token_cache = token
    return token


def get_user_token() -> str:
    """Get a user token using refresh token grant."""
    global _user_token_cache
    
    if _user_token_cache:
        return _user_token_cache
    
    auth_string = base64.b64encode(f"{EBAY_APP_ID}:{EBAY_CERT_ID}".encode()).decode()
    
    response = requests.post(
        f"{BASE_URL}/identity/v1/oauth2/token",
        headers={
            "Authorization": f"Basic {auth_string}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": EBAY_REFRESH_TOKEN
        }
    )
    
    if response.status_code != 200:
        return {"error": f"Failed to get user token: {response.text}"}
    
    token = response.json().get("access_token")
    _user_token_cache = token
    return token


def make_request(method: str, url: str, token_type: str = "app", **kwargs) -> Dict[str, Any]:
    """Make an HTTP request to the eBay API."""
    try:
        if token_type == "app":
            token = get_app_token()
        else:
            token = get_user_token()
        
        if isinstance(token, dict) and "error" in token:
            return token
        
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {token}"
        
        response = requests.request(method, url, headers=headers, **kwargs)
        
        if response.status_code >= 400:
            return {"error": f"API error {response.status_code}: {response.text}"}
        
        if response.status_code == 204:
            return {"success": True}
        
        if response.text:
            return response.json()
        
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# CATALOG API TOOLS
# ============================================================================

@mcp.tool()
def search_products(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """Search for products in the eBay catalog."""
    params = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if gtin:
        params["gtin"] = gtin
    if mpn:
        params["mpn"] = mpn
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    url = f"{BASE_URL}/commerce/catalog/v1_beta/product_summary/search"
    return make_request("GET", url, token_type="app", params=params, headers=headers)


@mcp.tool()
def get_product(epid: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get detailed information about a product by ePID."""
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    url = f"{BASE_URL}/commerce/catalog/v1_beta/product/{epid}"
    return make_request("GET", url, token_type="app", headers=headers)


# ============================================================================
# CHARITY API TOOLS
# ============================================================================

@mcp.tool()
def get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get details about a charitable organization."""
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    url = f"{BASE_URL}/commerce/charity/v1/charity_org/{charity_org_id}"
    return make_request("GET", url, token_type="app", headers=headers)


@mcp.tool()
def search_charity_orgs(
    q: Optional[str] = None,
    registration_id: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """Search for charitable organizations."""
    params = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if registration_id:
        params["registration_id"] = registration_id
    
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    url = f"{BASE_URL}/commerce/charity/v1/charity_org"
    return make_request("GET", url, token_type="app", params=params, headers=headers)


# ============================================================================
# IDENTITY API TOOLS
# ============================================================================

@mcp.tool()
def get_user() -> Dict[str, Any]:
    """Get the authenticated user's account information."""
    url = f"{IDENTITY_BASE_URL}/commerce/identity/v1/user/"
    return make_request("GET", url, token_type="user")


# ============================================================================
# MEDIA API TOOLS
# ============================================================================

@mcp.tool()
def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """Upload an image to eBay Picture Services from a URL."""
    url = f"{MEDIA_BASE_URL}/commerce/media/v1_beta/image/create_image_from_url"
    payload = {"imageUrl": image_url}
    headers = {"Content-Type": "application/json"}
    return make_request("POST", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def get_image(image_id: str) -> Dict[str, Any]:
    """Get details about an image."""
    url = f"{MEDIA_BASE_URL}/commerce/media/v1_beta/image/{image_id}"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def create_video(video_url: str) -> Dict[str, Any]:
    """Upload a video to eBay from a URL."""
    url = f"{MEDIA_BASE_URL}/commerce/media/v1_beta/video/create_video"
    payload = {"videoUrl": video_url}
    headers = {"Content-Type": "application/json"}
    return make_request("POST", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def get_video(video_id: str) -> Dict[str, Any]:
    """Get details about a video."""
    url = f"{MEDIA_BASE_URL}/commerce/media/v1_beta/video/{video_id}"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def create_document_from_url(document_url: str) -> Dict[str, Any]:
    """Upload a document to eBay from a URL."""
    url = f"{MEDIA_BASE_URL}/commerce/media/v1_beta/document/create_document_from_url"
    payload = {"documentUrl": document_url}
    headers = {"Content-Type": "application/json"}
    return make_request("POST", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def get_document(document_id: str) -> Dict[str, Any]:
    """Get details about a document."""
    url = f"{MEDIA_BASE_URL}/commerce/media/v1_beta/document/{document_id}"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def upload_video(video_id: str, file_path: str) -> Dict[str, Any]:
    """Upload a video file to eBay."""
    url = f"{MEDIA_BASE_URL}/commerce/media/v1_beta/video/{video_id}/upload"
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
        headers = {"Content-Type": "application/octet-stream", "Content-Length": str(len(file_content))}
        return make_request("POST", url, token_type="user", data=file_content, headers=headers)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def upload_document(document_id: str, file_path: str) -> Dict[str, Any]:
    """Upload a document file to eBay."""
    url = f"{MEDIA_BASE_URL}/commerce/media/v1_beta/document/{document_id}/upload"
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            token = get_user_token()
            if isinstance(token, dict) and "error" in token:
                return token
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.post(url, files=files, headers=headers)
            if response.status_code >= 400:
                return {"error": f"API error {response.status_code}: {response.text}"}
            if response.text:
                return response.json()
            return {"success": True}
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# NOTIFICATION API TOOLS
# ============================================================================

@mcp.tool()
def get_notification_config() -> Dict[str, Any]:
    """Get the notification configuration."""
    url = f"{BASE_URL}/commerce/notification/v1/config"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def update_notification_config(delivery_url: str, verification_token: Optional[str] = None) -> Dict[str, Any]:
    """Update the notification configuration."""
    url = f"{BASE_URL}/commerce/notification/v1/config"
    payload = {"deliveryUrl": delivery_url}
    if verification_token:
        payload["verificationToken"] = verification_token
    headers = {"Content-Type": "application/json"}
    return make_request("PUT", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def create_destination(destination_url: str, name: str) -> Dict[str, Any]:
    """Create a notification destination."""
    url = f"{BASE_URL}/commerce/notification/v1/destination"
    payload = {"url": destination_url, "name": name}
    headers = {"Content-Type": "application/json"}
    return make_request("POST", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def get_destinations() -> Dict[str, Any]:
    """Get all notification destinations."""
    url = f"{BASE_URL}/commerce/notification/v1/destination"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def get_destination(destination_id: str) -> Dict[str, Any]:
    """Get a specific notification destination."""
    url = f"{BASE_URL}/commerce/notification/v1/destination/{destination_id}"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def update_destination(destination_id: str, destination_url: str, name: str) -> Dict[str, Any]:
    """Update a notification destination."""
    url = f"{BASE_URL}/commerce/notification/v1/destination/{destination_id}"
    payload = {"url": destination_url, "name": name}
    headers = {"Content-Type": "application/json"}
    return make_request("PUT", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def delete_destination(destination_id: str) -> Dict[str, Any]:
    """Delete a notification destination."""
    url = f"{BASE_URL}/commerce/notification/v1/destination/{destination_id}"
    return make_request("DELETE", url, token_type="user")


@mcp.tool()
def get_topics() -> Dict[str, Any]:
    """Get all available notification topics."""
    url = f"{BASE_URL}/commerce/notification/v1/topic"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def get_topic(topic_id: str) -> Dict[str, Any]:
    """Get details about a specific notification topic."""
    url = f"{BASE_URL}/commerce/notification/v1/topic/{topic_id}"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def create_subscription(topic_id: str, destination_id: str, status: str, schema_version: str,
                       delivery_protocol: str = "HTTPS", format_type: str = "JSON") -> Dict[str, Any]:
    """Create a notification subscription."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription"
    payload = {
        "topicId": topic_id,
        "destinationId": destination_id,
        "status": status,
        "payload": {"deliveryProtocol": delivery_protocol, "format": format_type, "schemaVersion": schema_version}
    }
    headers = {"Content-Type": "application/json"}
    return make_request("POST", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def get_subscriptions() -> Dict[str, Any]:
    """Get all subscriptions."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Get details about a specific subscription."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def update_subscription(subscription_id: str, status: str) -> Dict[str, Any]:
    """Update a subscription."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}"
    payload = {"status": status}
    headers = {"Content-Type": "application/json"}
    return make_request("PUT", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """Delete a subscription."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}"
    return make_request("DELETE", url, token_type="user")


@mcp.tool()
def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Enable a subscription."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}/enable"
    return make_request("POST", url, token_type="user")


@mcp.tool()
def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Disable a subscription."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}/disable"
    return make_request("POST", url, token_type="user")


@mcp.tool()
def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """Send a test notification for a subscription."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}/test"
    return make_request("POST", url, token_type="user")


@mcp.tool()
def get_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    """Get a subscription filter."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}"
    return make_request("GET", url, token_type="user")


@mcp.tool()
def create_subscription_filter(subscription_id: str, filter_type: str, filter_value: str) -> Dict[str, Any]:
    """Create a subscription filter."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}/filter"
    payload = {"filterType": filter_type, "filterValue": filter_value}
    headers = {"Content-Type": "application/json"}
    return make_request("POST", url, token_type="user", json=payload, headers=headers)


@mcp.tool()
def delete_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    """Delete a subscription filter."""
    url = f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}"
    return make_request("DELETE", url, token_type="user")


@mcp.tool()
def get_public_key(public_key_id: str) -> Dict[str, Any]:
    """Get the public key for verifying notification signatures."""
    url = f"{BASE_URL}/commerce/notification/v1/public_key/{public_key_id}"
    return make_request("GET", url, token_type="app")


# ============================================================================
# TAXONOMY API TOOLS
# ============================================================================

@mcp.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace."""
    params = {"marketplace_id": marketplace_id}
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/get_default_category_tree_id"
    return make_request("GET", url, token_type="app", params=params)


@mcp.tool()
def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """Get the complete category tree."""
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}"
    headers = {"Accept-Encoding": "gzip"}
    return make_request("GET", url, token_type="app", headers=headers)


@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a subtree of the category tree."""
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree"
    params = {"category_id": category_id}
    return make_request("GET", url, token_type="app", params=params)


@mcp.tool()
def get_category_suggestions(q: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get category suggestions based on keywords."""
    params = {"q": q, "marketplace_id": marketplace_id}
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/get_category_suggestions"
    return make_request("GET", url, token_type="app", params=params)


@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get item aspects for a category."""
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category"
    params = {"category_id": category_id}
    return make_request("GET", url, token_type="app", params=params)


@mcp.tool()
def fetch_item_aspects(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Fetch item aspects for a category."""
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects"
    params = {"category_id": category_id}
    return make_request("GET", url, token_type="app", params=params)


@mcp.tool()
def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get compatibility properties for a category."""
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties"
    params = {"category_id": category_id}
    return make_request("GET", url, token_type="app", params=params)


@mcp.tool()
def get_compatibility_property_values(category_tree_id: str, category_id: str, property_name: str) -> Dict[str, Any]:
    """Get compatibility property values for a category."""
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values"
    params = {"category_id": category_id, "property_name": property_name}
    return make_request("GET", url, token_type="app", params=params)


@mcp.tool()
def get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    """Get expired categories."""
    url = f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories"
    return make_request("GET", url, token_type="app")


# ============================================================================
# TRANSLATION API TOOLS
# ============================================================================

@mcp.tool()
def translate_text(text: str, from_language: str, to_language: str, translation_context: str = "ITEM_TITLE") -> Dict[str, Any]:
    """Translate text from one language to another."""
    url = f"{BASE_URL}/commerce/translation/v1_beta/translate"
    payload = {"text": [text], "from": from_language, "to": to_language, "translationContext": translation_context}
    headers = {"Content-Type": "application/json"}
    return make_request("POST", url, token_type="app", json=payload, headers=headers)


if __name__ == "__main__":
    mcp.run()
