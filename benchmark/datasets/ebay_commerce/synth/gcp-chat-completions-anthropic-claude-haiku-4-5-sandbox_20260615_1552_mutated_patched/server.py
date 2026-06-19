#!/usr/bin/env python3
"""
eBay Commerce API MCP Server

Implements tools for interacting with eBay Commerce APIs including:
- Catalog (products)
- Charity (charitable organizations)
- Identity (user information)
- Media (images, videos, documents)
- Notification (webhooks, subscriptions)
- Taxonomy (categories, aspects)
- Translation
"""

import os
import json
import requests
import base64
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("ebay-commerce")

# Configuration
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID", "")
EBAY_REFRESH_TOKEN = os.getenv("EBAY_REFRESH_TOKEN", "")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URL = "https://api.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://api.ebay.com"
MEDIA_BASE_URL = "https://apim.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://apim.ebay.com"
TOKEN_URL = f"{BASE_URL}/identity/v1/oauth2/token"

# Token cache
_app_token_cache = None
_user_token_cache = None


def get_app_token() -> str:
    """Get OAuth app token using client credentials grant."""
    global _app_token_cache
    if _app_token_cache:
        return _app_token_cache
    
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope"
        },
        auth=(EBAY_APP_ID, EBAY_CERT_ID)
    )
    
    if response.status_code != 200:
        return {"error": f"Failed to get app token: {response.text}"}
    
    token = response.json().get("access_token")
    _app_token_cache = token
    return token


def get_user_token() -> str:
    """Get OAuth user token using refresh token grant."""
    global _user_token_cache
    if _user_token_cache:
        return _user_token_cache
    
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "refresh_token": EBAY_REFRESH_TOKEN
        },
        auth=(EBAY_APP_ID, EBAY_CERT_ID)
    )
    
    if response.status_code != 200:
        return {"error": f"Failed to get user token: {response.text}"}
    
    token = response.json().get("access_token")
    _user_token_cache = token
    return token


def make_request(
    method: str,
    endpoint: str,
    token_type: str = "app",
    params: Optional[dict] = None,
    json_data: Optional[dict] = None,
    headers: Optional[dict] = None,
    use_media_api: bool = False
) -> dict:
    """Make an HTTP request to eBay API."""
    base = MEDIA_BASE_URL if use_media_api else BASE_URL
    url = f"{base}{endpoint}"
    
    # Get appropriate token
    if token_type == "app":
        token = get_app_token()
    else:
        token = get_user_token()
    
    if isinstance(token, dict) and "error" in token:
        return token
    
    # Prepare headers
    req_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    if headers:
        req_headers.update(headers)
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
            headers=req_headers,
            timeout=30
        )
        
        # Handle response
        if response.status_code >= 400:
            return {
                "error": f"HTTP {response.status_code}",
                "details": response.text
            }
        
        if response.status_code == 204:
            return {"success": True}
        
        try:
            return response.json()
        except:
            return {"success": True, "body": response.text}
    
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# CATALOG API TOOLS
# ============================================================================

@server.tool()
def catalog_get_product(epid: str, marketplace_id: str = "EBAY_US") -> dict:
    """Get detailed information about a catalog product by ePID."""
    headers = {}
    if marketplace_id != "EBAY_US":
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request(
        "GET",
        f"/commerce/catalog/v1_beta/product/{epid}",
        token_type="app",
        headers=headers
    )


@server.tool()
def catalog_search_products(
    query: Optional[str] = None,
    category_id: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    aspects: Optional[str] = None,
    field_groups: Optional[str] = None,
    page_size: int = 50,
    offset: int = 0,
    marketplace_id: str = "EBAY_US"
) -> dict:
    """Search for products in the eBay catalog."""
    params = {"page_size": page_size, "offset": offset}
    if query:
        params["query"] = query
    if category_id:
        params["category_id"] = category_id
    if gtin:
        params["gtin"] = gtin
    if mpn:
        params["mpn"] = mpn
    if aspects:
        params["aspects"] = aspects
    if field_groups:
        params["field_groups"] = field_groups
    
    headers = {}
    if marketplace_id != "EBAY_US":
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        token_type="app",
        params=params,
        headers=headers
    )


# ============================================================================
# CHARITY API TOOLS
# ============================================================================

@server.tool()
def charity_get_charity_org(charity_org_id: str) -> dict:
    """Get details about a specific charitable organization."""
    return make_request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        token_type="app"
    )


@server.tool()
def charity_search_charity_orgs(
    query: Optional[str] = None,
    registration_id: Optional[str] = None,
    page_size: int = 10,
    offset: int = 0
) -> dict:
    """Search for charitable organizations."""
    params = {"page_size": page_size, "offset": offset}
    if query:
        params["query"] = query
    if registration_id:
        params["registration_id"] = registration_id
    
    return make_request(
        "GET",
        "/commerce/charity/v1/charity_org",
        token_type="app",
        params=params
    )


# ============================================================================
# IDENTITY API TOOLS
# ============================================================================

@server.tool()
def identity_get_user() -> dict:
    """Get public information about the authenticated user."""
    return make_request(
        "GET",
        "/commerce/identity/v1/user",
        token_type="user"
    )


# ============================================================================
# MEDIA API TOOLS
# ============================================================================

@server.tool()
def media_create_image_from_file(content_type: str, file_data: str) -> dict:
    """Create an image from a file upload."""
    try:
        binary_data = base64.b64decode(file_data)
    except:
        binary_data = file_data.encode()
    
    response = requests.post(
        f"{MEDIA_BASE_URL}/commerce/media/v1_beta/image",
        data=binary_data,
        headers={
            "Authorization": f"Bearer {get_user_token()}",
            "Content-Type": content_type
        },
        timeout=30
    )
    
    if response.status_code >= 400:
        return {"error": f"HTTP {response.status_code}", "details": response.text}
    
    try:
        return response.json()
    except:
        return {"success": True, "body": response.text}


@server.tool()
def media_create_image_from_url(image_url: str) -> dict:
    """Create an image by downloading from a URL."""
    return make_request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        token_type="user",
        json_data={"imageUrl": image_url},
        use_media_api=True
    )


@server.tool()
def media_get_image(image_id: str) -> dict:
    """Get details about an image."""
    return make_request(
        "GET",
        f"/commerce/media/v1_beta/image/{image_id}",
        token_type="user",
        use_media_api=True
    )


@server.tool()
def media_create_video(title: str, description: Optional[str] = None) -> dict:
    """Create a video resource."""
    payload = {"title": title}
    if description:
        payload["description"] = description
    
    return make_request(
        "POST",
        "/commerce/media/v1_beta/video",
        token_type="user",
        json_data=payload,
        use_media_api=True
    )


@server.tool()
def media_get_video(video_id: str) -> dict:
    """Get details about a video."""
    return make_request(
        "GET",
        f"/commerce/media/v1_beta/video/{video_id}",
        token_type="user",
        use_media_api=True
    )


@server.tool()
def media_upload_video(video_id: str, content_type: str, file_data: str) -> dict:
    """Upload video content."""
    try:
        binary_data = base64.b64decode(file_data)
    except:
        binary_data = file_data.encode()
    
    response = requests.post(
        f"{MEDIA_BASE_URL}/commerce/media/v1_beta/video/{video_id}/upload",
        data=binary_data,
        headers={
            "Authorization": f"Bearer {get_user_token()}",
            "Content-Type": content_type
        },
        timeout=30
    )
    
    if response.status_code >= 400:
        return {"error": f"HTTP {response.status_code}", "details": response.text}
    
    return {"success": True}


@server.tool()
def media_create_document(document_type: str, content_language: str) -> dict:
    """Create a document resource."""
    return make_request(
        "POST",
        "/commerce/media/v1_beta/document",
        token_type="user",
        json_data={
            "documentType": document_type,
            "contentLanguage": content_language
        },
        use_media_api=True
    )


@server.tool()
def media_get_document(document_id: str) -> dict:
    """Get details about a document."""
    return make_request(
        "GET",
        f"/commerce/media/v1_beta/document/{document_id}",
        token_type="user",
        use_media_api=True
    )


@server.tool()
def media_upload_document(document_id: str, content_type: str, file_data: str) -> dict:
    """Upload document content."""
    try:
        binary_data = base64.b64decode(file_data)
    except:
        binary_data = file_data.encode()
    
    response = requests.post(
        f"{MEDIA_BASE_URL}/commerce/media/v1_beta/document/{document_id}/upload",
        data=binary_data,
        headers={
            "Authorization": f"Bearer {get_user_token()}",
            "Content-Type": content_type
        },
        timeout=30
    )
    
    if response.status_code >= 400:
        return {"error": f"HTTP {response.status_code}", "details": response.text}
    
    return {"success": True}


@server.tool()
def media_create_document_from_url(document_url: str) -> dict:
    """Create a document by downloading from a URL."""
    return make_request(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        token_type="user",
        json_data={"documentUrl": document_url},
        use_media_api=True
    )


# ============================================================================
# NOTIFICATION API TOOLS
# ============================================================================

@server.tool()
def notification_get_config() -> dict:
    """Get the notification configuration."""
    return make_request("GET", "/commerce/notification/v1/config", token_type="user")


@server.tool()
def notification_update_config(
    delivery_url: str,
    verification_token: Optional[str] = None,
    disabled_subscriptions: Optional[list] = None
) -> dict:
    """Update the notification configuration."""
    payload = {"deliveryUrl": delivery_url}
    if verification_token:
        payload["verificationToken"] = verification_token
    if disabled_subscriptions:
        payload["disabledSubscriptions"] = disabled_subscriptions
    
    return make_request(
        "POST",
        "/commerce/notification/v1/config",
        token_type="user",
        json_data=payload
    )


@server.tool()
def notification_create_destination(
    destination_status: str,
    name: str,
    delivery_url: str,
    verification_token: Optional[str] = None
) -> dict:
    """Create a notification destination."""
    payload = {
        "destinationStatus": destination_status,
        "name": name,
        "deliveryUrl": delivery_url
    }
    if verification_token:
        payload["verificationToken"] = verification_token
    
    return make_request(
        "POST",
        "/commerce/notification/v1/destination",
        token_type="user",
        json_data=payload
    )


@server.tool()
def notification_get_destination(destination_id: str) -> dict:
    """Get details about a notification destination."""
    return make_request(
        "GET",
        f"/commerce/notification/v1/destination/{destination_id}",
        token_type="user"
    )


@server.tool()
def notification_get_destinations() -> dict:
    """Get all notification destinations."""
    return make_request(
        "GET",
        "/commerce/notification/v1/destination",
        token_type="user"
    )


@server.tool()
def notification_update_destination(
    destination_id: str,
    destination_status: str,
    name: str,
    delivery_url: str,
    verification_token: Optional[str] = None
) -> dict:
    """Update a notification destination."""
    payload = {
        "destinationStatus": destination_status,
        "name": name,
        "deliveryUrl": delivery_url
    }
    if verification_token:
        payload["verificationToken"] = verification_token
    
    return make_request(
        "PUT",
        f"/commerce/notification/v1/destination/{destination_id}",
        token_type="user",
        json_data=payload
    )


@server.tool()
def notification_delete_destination(destination_id: str) -> dict:
    """Delete a notification destination."""
    return make_request(
        "DELETE",
        f"/commerce/notification/v1/destination/{destination_id}",
        token_type="user"
    )


@server.tool()
def notification_get_public_key() -> dict:
    """Get the public key for verifying notification signatures."""
    return make_request(
        "GET",
        "/commerce/notification/v1/public_key",
        token_type="user"
    )


@server.tool()
def notification_create_subscription(destination_id: str, topic_ids: list) -> dict:
    """Create a notification subscription."""
    return make_request(
        "POST",
        "/commerce/notification/v1/subscription",
        token_type="user",
        json_data={
            "destinationId": destination_id,
            "topicIds": topic_ids
        }
    )


@server.tool()
def notification_get_subscription(subscription_id: str) -> dict:
    """Get details about a notification subscription."""
    return make_request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        token_type="user"
    )


@server.tool()
def notification_get_subscriptions() -> dict:
    """Get all notification subscriptions."""
    return make_request(
        "GET",
        "/commerce/notification/v1/subscription",
        token_type="user"
    )


@server.tool()
def notification_update_subscription(
    subscription_id: str,
    destination_id: str,
    topic_ids: list
) -> dict:
    """Update a notification subscription."""
    return make_request(
        "PUT",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        token_type="user",
        json_data={
            "destinationId": destination_id,
            "topicIds": topic_ids
        }
    )


@server.tool()
def notification_delete_subscription(subscription_id: str) -> dict:
    """Delete a notification subscription."""
    return make_request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        token_type="user"
    )


@server.tool()
def notification_enable_subscription(subscription_id: str) -> dict:
    """Enable a notification subscription."""
    return make_request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/enable",
        token_type="user"
    )


@server.tool()
def notification_disable_subscription(subscription_id: str) -> dict:
    """Disable a notification subscription."""
    return make_request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/disable",
        token_type="user"
    )


@server.tool()
def notification_test_subscription(subscription_id: str) -> dict:
    """Send a test notification to a subscription."""
    return make_request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/test",
        token_type="user"
    )


@server.tool()
def notification_get_topics() -> dict:
    """Get all available notification topics."""
    return make_request(
        "GET",
        "/commerce/notification/v1/topic",
        token_type="user"
    )


@server.tool()
def notification_get_topic(topic_id: str) -> dict:
    """Get details about a notification topic."""
    return make_request(
        "GET",
        f"/commerce/notification/v1/topic/{topic_id}",
        token_type="user"
    )


@server.tool()
def notification_create_subscription_filter(
    subscription_id: str,
    filter_type: str,
    filter_value: str
) -> dict:
    """Create a filter for a notification subscription."""
    return make_request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        token_type="user",
        json_data={
            "filterType": filter_type,
            "filterValue": filter_value
        }
    )


@server.tool()
def notification_get_subscription_filter(
    subscription_id: str,
    filter_id: str
) -> dict:
    """Get details about a subscription filter."""
    return make_request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
        token_type="user"
    )


@server.tool()
def notification_delete_subscription_filter(
    subscription_id: str,
    filter_id: str
) -> dict:
    """Delete a subscription filter."""
    return make_request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
        token_type="user"
    )


# ============================================================================
# TAXONOMY API TOOLS
# ============================================================================

@server.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> dict:
    """Get the default category tree ID for a marketplace."""
    params = {"marketplace_id": marketplace_id}
    return make_request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        token_type="app",
        params=params
    )


@server.tool()
def taxonomy_get_category_tree(category_tree_id: str) -> dict:
    """Get the category tree structure."""
    return make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        token_type="app"
    )


@server.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """Get a subtree of categories."""
    params = {"category_id": category_id}
    return make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        token_type="app",
        params=params
    )


@server.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, keywords: str) -> dict:
    """Get category suggestions based on keywords."""
    params = {"keywords": keywords}
    return make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        token_type="app",
        params=params
    )


@server.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """Get item aspects for a category."""
    params = {"category_id": category_id}
    return make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        token_type="app",
        params=params
    )


@server.tool()
def taxonomy_fetch_item_aspects(category_tree_id: str, category_id: str) -> dict:
    """Fetch item aspects for a category."""
    params = {"category_id": category_id}
    return make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        token_type="app",
        params=params
    )


@server.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str) -> dict:
    """Get compatibility properties for a category."""
    params = {"category_id": category_id}
    return make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        token_type="app",
        params=params
    )


@server.tool()
def taxonomy_get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    property_name: str
) -> dict:
    """Get values for a compatibility property."""
    params = {
        "category_id": category_id,
        "property_name": property_name
    }
    return make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        token_type="app",
        params=params
    )


@server.tool()
def taxonomy_get_expired_categories(category_tree_id: str) -> dict:
    """Get expired categories in a category tree."""
    return make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        token_type="app"
    )


# ============================================================================
# TRANSLATION API TOOLS
# ============================================================================

@server.tool()
def translation_translate(text: str, from_language: str, to_language: str) -> dict:
    """Translate text from one language to another."""
    return make_request(
        "POST",
        "/commerce/translation/v1_beta/translate",
        token_type="app",
        json_data={
            "text": text,
            "fromLanguage": from_language,
            "toLanguage": to_language
        }
    )


if __name__ == "__main__":
    server.run()
