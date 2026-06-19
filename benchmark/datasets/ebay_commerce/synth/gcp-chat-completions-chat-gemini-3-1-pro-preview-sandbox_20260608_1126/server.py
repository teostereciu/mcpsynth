import os
import base64
import json
import requests
from typing import Dict, Any, Optional, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-commerce")

EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_REFRESH_TOKEN = os.environ.get("EBAY_REFRESH_TOKEN")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

if EBAY_ENVIRONMENT == "PRODUCTION":
    BASE_URL = "https://api.ebay.com"
    MEDIA_BASE_URL = "https://apim.ebay.com"
else:
    BASE_URL = "https://api.sandbox.ebay.com"
    MEDIA_BASE_URL = "https://apim.sandbox.ebay.com"

_app_token = None
_user_token = None

def get_app_token() -> str:
    global _app_token
    if _app_token:
        return _app_token
    
    if not EBAY_APP_ID or not EBAY_CERT_ID:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID are required for app token")
        
    auth_str = f"{EBAY_APP_ID}:{EBAY_CERT_ID}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    
    resp = requests.post(f"{BASE_URL}/identity/v1/oauth2/token", headers=headers, data=data)
    resp.raise_for_status()
    _app_token = resp.json()["access_token"]
    return _app_token

def get_user_token() -> str:
    global _user_token
    if _user_token:
        return _user_token
        
    if not EBAY_APP_ID or not EBAY_CERT_ID or not EBAY_REFRESH_TOKEN:
        raise ValueError("EBAY_APP_ID, EBAY_CERT_ID, and EBAY_REFRESH_TOKEN are required for user token")
        
    auth_str = f"{EBAY_APP_ID}:{EBAY_CERT_ID}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN
    }
    
    resp = requests.post(f"{BASE_URL}/identity/v1/oauth2/token", headers=headers, data=data)
    resp.raise_for_status()
    _user_token = resp.json()["access_token"]
    return _user_token

def make_request(method: str, url: str, token_type: str, params: dict = None, json_data: dict = None, headers: dict = None) -> dict:
    if token_type == "app":
        token = get_app_token()
    elif token_type == "user":
        token = get_user_token()
    else:
        raise ValueError("Invalid token type")
        
    req_headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    if headers:
        req_headers.update(headers)
        
    try:
        resp = requests.request(method, url, headers=req_headers, params=params, json=json_data)
        if resp.status_code == 204:
            return {"status": "success"}
        resp.raise_for_status()
        if resp.headers.get("Content-Type", "").startswith("application/json"):
            return resp.json()
        return {"response": resp.text}
    except requests.exceptions.RequestException as e:
        if hasattr(e, "response") and e.response is not None:
            try:
                return {"error": e.response.json()}
            except:
                return {"error": e.response.text}
        return {"error": str(e)}

# Catalog API (App Token)
@mcp.tool()
def search_products(q: str = None, gtin: str = None, mpn: str = None, category_ids: str = None, limit: str = "50") -> dict:
    """Search for and retrieve summaries of one or more products in the eBay catalog."""
    params = {}
    if q: params["q"] = q
    if gtin: params["gtin"] = gtin
    if mpn: params["mpn"] = mpn
    if category_ids: params["category_ids"] = category_ids
    if limit: params["limit"] = limit
    return make_request("GET", f"{BASE_URL}/commerce/catalog/v1_beta/product_summary/search", "app", params=params)

@mcp.tool()
def get_product(epid: str) -> dict:
    """Retrieve the full details of a product by its eBay Product ID (ePID)."""
    return make_request("GET", f"{BASE_URL}/commerce/catalog/v1_beta/product/{epid}", "app")

# Charity API (App Token)
@mcp.tool()
def get_charity_org(charity_org_id: str) -> dict:
    """Retrieve details for a specific charity organization."""
    return make_request("GET", f"{BASE_URL}/commerce/charity/v1/charity_org/{charity_org_id}", "app")

@mcp.tool()
def get_charity_orgs(q: str = None, limit: str = "50") -> dict:
    """Search for charity organizations."""
    params = {"limit": limit}
    if q: params["q"] = q
    return make_request("GET", f"{BASE_URL}/commerce/charity/v1/charity_org", "app", params=params)

# Identity API (User Token)
@mcp.tool()
def get_user() -> dict:
    """Retrieve the authenticated user's profile."""
    return make_request("GET", f"{BASE_URL}/commerce/identity/v1/user", "user")

# Media API (User Token, MEDIA_BASE_URL)
@mcp.tool()
def create_document(data: dict) -> dict:
    """Create a document."""
    return make_request("POST", f"{MEDIA_BASE_URL}/commerce/media/v1/document", "user", json_data=data)

@mcp.tool()
def get_document(document_id: str) -> dict:
    """Retrieve a document."""
    return make_request("GET", f"{MEDIA_BASE_URL}/commerce/media/v1/document/{document_id}", "user")

@mcp.tool()
def create_image(data: dict) -> dict:
    """Create an image."""
    return make_request("POST", f"{MEDIA_BASE_URL}/commerce/media/v1/image", "user", json_data=data)

@mcp.tool()
def get_image(image_id: str) -> dict:
    """Retrieve an image."""
    return make_request("GET", f"{MEDIA_BASE_URL}/commerce/media/v1/image/{image_id}", "user")

@mcp.tool()
def create_video(data: dict) -> dict:
    """Create a video."""
    return make_request("POST", f"{MEDIA_BASE_URL}/commerce/media/v1/video", "user", json_data=data)

@mcp.tool()
def get_video(video_id: str) -> dict:
    """Retrieve a video."""
    return make_request("GET", f"{MEDIA_BASE_URL}/commerce/media/v1/video/{video_id}", "user")

# Notification API (User Token)
@mcp.tool()
def get_config() -> dict:
    """Get notification configuration."""
    return make_request("GET", f"{BASE_URL}/commerce/notification/v1/config", "user")

@mcp.tool()
def update_config(data: dict) -> dict:
    """Update notification configuration."""
    return make_request("PUT", f"{BASE_URL}/commerce/notification/v1/config", "user", json_data=data)

@mcp.tool()
def create_destination(data: dict) -> dict:
    """Create a notification destination."""
    return make_request("POST", f"{BASE_URL}/commerce/notification/v1/destination", "user", json_data=data)

@mcp.tool()
def get_destinations() -> dict:
    """Get all notification destinations."""
    return make_request("GET", f"{BASE_URL}/commerce/notification/v1/destination", "user")

@mcp.tool()
def get_destination(destination_id: str) -> dict:
    """Get a specific notification destination."""
    return make_request("GET", f"{BASE_URL}/commerce/notification/v1/destination/{destination_id}", "user")

@mcp.tool()
def delete_destination(destination_id: str) -> dict:
    """Delete a notification destination."""
    return make_request("DELETE", f"{BASE_URL}/commerce/notification/v1/destination/{destination_id}", "user")

@mcp.tool()
def create_subscription(data: dict) -> dict:
    """Create a notification subscription."""
    return make_request("POST", f"{BASE_URL}/commerce/notification/v1/subscription", "user", json_data=data)

@mcp.tool()
def get_subscriptions() -> dict:
    """Get all notification subscriptions."""
    return make_request("GET", f"{BASE_URL}/commerce/notification/v1/subscription", "user")

@mcp.tool()
def get_subscription(subscription_id: str) -> dict:
    """Get a specific notification subscription."""
    return make_request("GET", f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}", "user")

@mcp.tool()
def delete_subscription(subscription_id: str) -> dict:
    """Delete a notification subscription."""
    return make_request("DELETE", f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}", "user")

@mcp.tool()
def enable_subscription(subscription_id: str) -> dict:
    """Enable a notification subscription."""
    return make_request("POST", f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}/enable", "user")

@mcp.tool()
def disable_subscription(subscription_id: str) -> dict:
    """Disable a notification subscription."""
    return make_request("POST", f"{BASE_URL}/commerce/notification/v1/subscription/{subscription_id}/disable", "user")

@mcp.tool()
def get_topics() -> dict:
    """Get all notification topics."""
    return make_request("GET", f"{BASE_URL}/commerce/notification/v1/topic", "user")

@mcp.tool()
def get_topic(topic_id: str) -> dict:
    """Get a specific notification topic."""
    return make_request("GET", f"{BASE_URL}/commerce/notification/v1/topic/{topic_id}", "user")

# Taxonomy API (App Token)
@mcp.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> dict:
    """Get the default category tree ID for a marketplace."""
    params = {"marketplace_id": marketplace_id}
    return make_request("GET", f"{BASE_URL}/commerce/taxonomy/v1/get_default_category_tree_id", "app", params=params)

@mcp.tool()
def get_category_tree(category_tree_id: str) -> dict:
    """Get a category tree by ID."""
    return make_request("GET", f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}", "app")

@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """Get a category subtree."""
    params = {"category_id": category_id}
    return make_request("GET", f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree", "app", params=params)

@mcp.tool()
def get_category_suggestions(category_tree_id: str, q: str) -> dict:
    """Get category suggestions for a keyword."""
    params = {"q": q}
    return make_request("GET", f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions", "app", params=params)

@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """Get item aspects for a category."""
    params = {"category_id": category_id}
    return make_request("GET", f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category", "app", params=params)

# Translation API (App Token)
@mcp.tool()
def translate(data: dict) -> dict:
    """Translate text."""
    return make_request("POST", f"{BASE_URL}/commerce/translation/v1/translate", "app", json_data=data)

if __name__ == "__main__":
    mcp.run()
