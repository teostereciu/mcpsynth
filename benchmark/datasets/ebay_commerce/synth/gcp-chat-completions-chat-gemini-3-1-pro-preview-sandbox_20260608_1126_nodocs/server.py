import os
import base64
import requests
from typing import Optional, Dict, Any, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-commerce")

def get_env() -> str:
    return os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

def get_base_url() -> str:
    if get_env() == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"

def get_media_base_url() -> str:
    if get_env() == "PRODUCTION":
        return "https://apim.ebay.com"
    return "https://apim.sandbox.ebay.com"

def get_auth_headers(token_type: str = "app") -> Dict[str, str]:
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    
    if not app_id or not cert_id:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID must be set")
        
    auth_str = f"{app_id}:{cert_id}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    
    token_url = f"{get_base_url()}/identity/v1/oauth2/token"
    
    if token_type == "app":
        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope"
        }
    elif token_type == "user":
        refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
        if not refresh_token:
            raise ValueError("EBAY_REFRESH_TOKEN must be set for user token")
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
    else:
        raise ValueError("Invalid token type")
        
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {b64_auth}"
    }
    
    response = requests.post(token_url, data=data, headers=headers)
    response.raise_for_status()
    token = response.json()["access_token"]
    
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

# Catalog API (App token)
@mcp.tool()
def search_products(q: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """Search for products in the eBay catalog."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/catalog/v1_beta/product_summary/search"
        params = {"q": q, "limit": limit, "offset": offset}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_product(epid: str) -> Dict[str, Any]:
    """Get details of a specific product by its eBay Product ID (ePID)."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/catalog/v1_beta/product/{epid}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Taxonomy API (App token)
@mcp.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get the default category tree ID for a given marketplace."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/taxonomy/v1/get_default_category_tree_id"
        params = {"marketplace_id": marketplace_id}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """Get the complete category tree for a given category tree ID."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a subtree of categories under a specific category."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree"
        params = {"category_id": category_id}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get the item aspects (attributes) required or recommended for a category."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category"
        params = {"category_id": category_id}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Identity API (User token)
@mcp.tool()
def get_user() -> Dict[str, Any]:
    """Get the profile of the authenticated user."""
    try:
        headers = get_auth_headers("user")
        url = f"{get_base_url()}/commerce/identity/v1/user/"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Charity API (App token)
@mcp.tool()
def get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    """Get details of a specific charity organization."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/charity/v1/charity_org/{charity_org_id}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def search_charity_orgs(q: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """Search for charity organizations."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/charity/v1/charity_org"
        params = {"q": q, "limit": limit, "offset": offset}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Translation API (App token)
@mcp.tool()
def translate(text: str, from_lang: str, to_lang: str) -> Dict[str, Any]:
    """Translate text from one language to another."""
    try:
        headers = get_auth_headers("app")
        url = f"{get_base_url()}/commerce/translation/v1/translate"
        payload = {
            "text": [text],
            "from": from_lang,
            "to": to_lang
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Media API (User token)
@mcp.tool()
def create_video(title: str, size: int) -> Dict[str, Any]:
    """Create a video upload session."""
    try:
        headers = get_auth_headers("user")
        url = f"{get_media_base_url()}/commerce/media/v1_beta/video"
        payload = {
            "title": title,
            "size": size
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_video(video_id: str) -> Dict[str, Any]:
    """Get details of an uploaded video."""
    try:
        headers = get_auth_headers("user")
        url = f"{get_media_base_url()}/commerce/media/v1_beta/video/{video_id}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Notification API (User token)
@mcp.tool()
def get_subscriptions() -> Dict[str, Any]:
    """Get all notification subscriptions for the user."""
    try:
        headers = get_auth_headers("user")
        url = f"{get_base_url()}/commerce/notification/v1/subscription"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Get details of a specific notification subscription."""
    try:
        headers = get_auth_headers("user")
        url = f"{get_base_url()}/commerce/notification/v1/subscription/{subscription_id}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
