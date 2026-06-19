"""eBay Commerce API MCP Server"""
import os
import requests
from typing import Any
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="ebay-commerce-api")

# Environment variables
EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_REFRESH_TOKEN = os.environ.get("EBAY_REFRESH_TOKEN")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URLS = {
    "standard": f"https://api.{EBAY_ENVIRONMENT.lower()}.ebay.com",
    "media": f"https://apim.{EBAY_ENVIRONMENT.lower()}.ebay.com",
}

# OAuth endpoints
OAUTH_TOKEN_URL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"


def get_app_token() -> str:
    """Get app token using client credentials grant."""
    if not EBAY_APP_ID or not EBAY_CERT_ID:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID must be set")
    
    response = requests.post(
        OAUTH_TOKEN_URL,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {requests.auth._basic_auth_str(EBAY_APP_ID, EBAY_CERT_ID)}",
        },
        data={
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


def get_user_token() -> str:
    """Get user token using refresh token grant."""
    if not EBAY_APP_ID or not EBAY_CERT_ID or not EBAY_REFRESH_TOKEN:
        raise ValueError("EBAY_APP_ID, EBAY_CERT_ID, and EBAY_REFRESH_TOKEN must be set")
    
    response = requests.post(
        OAUTH_TOKEN_URL,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {requests.auth._basic_auth_str(EBAY_APP_ID, EBAY_CERT_ID)}",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": EBAY_REFRESH_TOKEN,
            "scope": "https://api.ebay.com/oauth/api_scope",
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


def make_request(method: str, url: str, token: str = None, headers: dict = None, params: dict = None, json: dict = None) -> dict:
    """Make an HTTP request to eBay API."""
    if headers is None:
        headers = {}
    
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    headers["Content-Type"] = "application/json"
    
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=json,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_data = e.response.json()
            return {"error": error_data.get("message", str(e))}
        except:
            return {"error": str(e)}


# ========== Taxonomy API (App Token Required) ==========

@mcp.tool()
def get_taxonomy_categories() -> dict:
    """Get complete eBay category taxonomy tree.
    
    Returns the full category hierarchy for all eBay sites.
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/taxonomy/v1/category_tree"
    return make_request("GET", url, token)


@mcp.tool()
def get_category_mapping(item_id: str) -> dict:
    """Get recommended category for an item based on its title and details.
    
    Args:
        item_id: The item ID to get category mapping for
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/taxonomy/v1/category_mapping"
    return make_request("GET", url, token, params={"itemId": item_id})


@mcp.tool()
def get_category_aspects(category_id: str) -> dict:
    """Get aspect hints for a specific category.
    
    Args:
        category_id: The category ID to get aspects for
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/taxonomy/v1/category_tree/{category_id}/aspect_hints"
    return make_request("GET", url, token)


@mcp.tool()
def get_compatibility_properties(category_id: str, product_id: str = None) -> dict:
    """Get compatibility properties for a category or specific product.
    
    Args:
        category_id: The category ID
        product_id: Optional product ID (UPC, EAN, or ISBN)
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/taxonomy/v1/category_tree/{category_id}/compatibility_properties"
    params = {}
    if product_id:
        params["productId"] = product_id
    return make_request("GET", url, token, params=params)


# ========== Catalog API (App Token Required) ==========

@mcp.tool()
def get_catalog_product(product_id: str) -> dict:
    """Get detailed information about a catalog product.
    
    Args:
        product_id: The eBay catalog product ID (ePID)
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/catalog/v1_beta/product/{product_id}"
    return make_request("GET", url, token)


@mcp.tool()
def search_catalog_products(query: str, category_id: str = None, limit: int = 10) -> dict:
    """Search for products in the eBay catalog.
    
    Args:
        query: Search query string
        category_id: Optional category ID to filter results
        limit: Maximum number of results (default: 10)
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/catalog/v1_beta/product/search"
    params = {
        "query": query,
        "limit": str(limit),
    }
    if category_id:
        params["categoryId"] = category_id
    return make_request("GET", url, token, params=params)


@mcp.tool()
def get_product_recommendations(category_id: str, title: str, description: str = None) -> dict:
    """Get product recommendations based on listing details.
    
    Args:
        category_id: The category ID
        title: Listing title
        description: Optional listing description
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/catalog/v1_beta/product/recommendation"
    json_data = {
        "categoryId": category_id,
        "title": title,
    }
    if description:
        json_data["description"] = description
    return make_request("POST", url, token, json=json_data)


@mcp.tool()
def get_upc_recommended_product(upc: str) -> dict:
    """Get recommended product for a given UPC.
    
    Args:
        upc: Universal Product Code
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/catalog/v1_beta/product/recommendation/upc/{upc}"
    return make_request("GET", url, token)


# ========== Identity API (User Token Required) ==========

@mcp.tool()
def get_user_profile() -> dict:
    """Get the authenticated user's profile information."""
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/identity/v1/user/profile"
    return make_request("GET", url, token)


@mcp.tool()
def get_user_account() -> dict:
    """Get the authenticated user's account information."""
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/identity/v1/user/account"
    return make_request("GET", url, token)


# ========== Media API (User Token Required, Different Base URL) ==========

@mcp.tool()
def upload_media(media_type: str, file_path: str, content_type: str = "image/jpeg") -> dict:
    """Upload media (images, videos, documents) to eBay.
    
    Args:
        media_type: Type of media ('IMAGE', 'VIDEO', 'DOCUMENT')
        file_path: Path to the file to upload
        content_type: MIME type of the file (default: image/jpeg)
    """
    token = get_user_token()
    url = f"{BASE_URLS['media']}/commerce/media/v1_beta/upload_media"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": content_type,
    }
    
    try:
        with open(file_path, "rb") as f:
            response = requests.post(
                url,
                headers=headers,
                data=f,
                params={"mediaType": media_type},
            )
        response.raise_for_status()
        return response.json()
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except requests.exceptions.HTTPError as e:
        try:
            error_data = e.response.json()
            return {"error": error_data.get("message", str(e))}
        except:
            return {"error": str(e)}


@mcp.tool()
def get_media_status(upload_token: str) -> dict:
    """Get the status of a media upload.
    
    Args:
        upload_token: The upload token returned from upload_media
    """
    token = get_user_token()
    url = f"{BASE_URLS['media']}/commerce/media/v1_beta/upload_status"
    return make_request("GET", url, token, params={"uploadToken": upload_token})


# ========== Notification API (User Token Required) ==========

@mcp.tool()
def list_webhook_subscriptions() -> dict:
    """List all webhook subscriptions for the authenticated user."""
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/notification/v1_beta/subscription"
    return make_request("GET", url, token)


@mcp.tool()
def create_webhook_subscription(payload: dict) -> dict:
    """Create a new webhook subscription.
    
    Args:
        payload: Subscription configuration including event filters and callback URL
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/notification/v1_beta/subscription"
    return make_request("POST", url, token, json=payload)


@mcp.tool()
def delete_webhook_subscription(subscription_id: str) -> dict:
    """Delete a webhook subscription.
    
    Args:
        subscription_id: The subscription ID to delete
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/notification/v1_beta/subscription/{subscription_id}"
    return make_request("DELETE", url, token)


@mcp.tool()
def list_webhook_events(subscription_id: str, limit: int = 10) -> dict:
    """List webhook events for a subscription.
    
    Args:
        subscription_id: The subscription ID
        limit: Maximum number of events to return (default: 10)
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/notification/v1_beta/subscription/{subscription_id}/event"
    return make_request("GET", url, token, params={"limit": str(limit)})


# ========== Translation API (App Token Required) ==========

@mcp.tool()
def translate_text(text: str, source_lang: str, target_lang: str) -> dict:
    """Translate text between languages.
    
    Args:
        text: Text to translate
        source_lang: Source language code (e.g., 'en_US')
        target_lang: Target language code (e.g., 'es_ES')
    """
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/translation/v1_beta/translate"
    json_data = {
        "text": text,
        "sourceLanguage": source_lang,
        "targetLanguage": target_lang,
    }
    return make_request("POST", url, token, json=json_data)


@mcp.tool()
def get_translation_supported_languages() -> dict:
    """Get list of supported languages for translation."""
    token = get_app_token()
    url = f"{BASE_URLS['standard']}/commerce/translation/v1_beta/supported_languages"
    return make_request("GET", url, token)


# ========== Charity API (User Token Required) ==========

@mcp.tool()
def search_charity_organizations(query: str, limit: int = 10) -> dict:
    """Search for eBay for Charity organizations.
    
    Args:
        query: Search query
        limit: Maximum number of results (default: 10)
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/charity/v1_beta/organization/search"
    params = {
        "query": query,
        "limit": str(limit),
    }
    return make_request("GET", url, token, params=params)


@mcp.tool()
def get_charity_organization(organization_id: str) -> dict:
    """Get detailed information about a charity organization.
    
    Args:
        organization_id: The charity organization ID
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/charity/v1_beta/organization/{organization_id}"
    return make_request("GET", url, token)


@mcp.tool()
def create_charity_donor_record(charity_id: str, donation_amount: float, transaction_id: str) -> dict:
    """Create a donor record for a charity donation.
    
    Args:
        charity_id: The charity organization ID
        donation_amount: Donation amount in the currency of the site
        transaction_id: Transaction ID for tracking
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/charity/v1_beta/donor_record"
    json_data = {
        "charityId": charity_id,
        "donationAmount": {
            "value": str(donation_amount),
        },
        "transactionId": transaction_id,
    }
    return make_request("POST", url, token, json=json_data)


@mcp.tool()
def get_charity_donor_records(limit: int = 10) -> dict:
    """Get donor records for the authenticated user.
    
    Args:
        limit: Maximum number of records to return (default: 10)
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/commerce/charity/v1_beta/donor_record"
    return make_request("GET", url, token, params={"limit": str(limit)})


# ========== Item/Listing Operations ==========

@mcp.tool()
def create_item(category_id: str, title: str, description: str, price: float, currency: str = "USD", quantity: int = 1) -> dict:
    """Create a new listing/item on eBay.
    
    Args:
        category_id: The category ID where the item will be listed
        title: Item title
        description: Item description
        price: Starting price
        currency: Currency code (default: USD)
        quantity: Available quantity (default: 1)
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/item"
    json_data = {
        "categoryId": category_id,
        "title": title,
        "description": description,
        "price": {
            "value": str(price),
            "currency": currency,
        },
        "quantity": quantity,
    }
    return make_request("POST", url, token, json=json_data)


@mcp.tool()
def get_item(item_id: str) -> dict:
    """Get detailed information about a listing.
    
    Args:
        item_id: The item ID to retrieve
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/item/{item_id}"
    return make_request("GET", url, token)


@mcp.tool()
def update_item(item_id: str, **kwargs) -> dict:
    """Update an existing listing.
    
    Args:
        item_id: The item ID to update
        **kwargs: Fields to update (title, description, price, quantity, etc.)
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/item/{item_id}"
    return make_request("PUT", url, token, json=kwargs)


@mcp.tool()
def delete_item(item_id: str) -> dict:
    """Delete/End an active listing.
    
    Args:
        item_id: The item ID to delete
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/item/{item_id}"
    return make_request("DELETE", url, token)


@mcp.tool()
def list_items(limit: int = 10, offset: int = 0) -> dict:
    """List items created by the authenticated user.
    
    Args:
        limit: Maximum number of items to return (default: 10)
        offset: Number of items to skip (for pagination)
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/item"
    params = {
        "limit": str(limit),
        "offset": str(offset),
    }
    return make_request("GET", url, token, params=params)


# ========== Inventory Management ==========

@mcp.tool()
def create_inventory_item(sku: str, title: str, description: str, condition: str = "NEW") -> dict:
    """Create an inventory item.
    
    Args:
        sku: Stock Keeping Unit
        title: Item title
        description: Item description
        condition: Item condition (NEW, USED, REFURBISHED)
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/inventory_item"
    json_data = {
        "sku": sku,
        "title": title,
        "description": description,
        "condition": condition,
    }
    return make_request("POST", url, token, json=json_data)


@mcp.tool()
def get_inventory_item(sku: str) -> dict:
    """Get inventory item details.
    
    Args:
        sku: The SKU to retrieve
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/inventory_item/{sku}"
    return make_request("GET", url, token)


@mcp.tool()
def list_inventory_items(limit: int = 10) -> dict:
    """List inventory items.
    
    Args:
        limit: Maximum number of items to return (default: 10)
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/inventory_item"
    return make_request("GET", url, token, params={"limit": str(limit)})


@mcp.tool()
def add_inventory_item_location(sku: str, location_id: str, quantity: int, price: float) -> dict:
    """Add location availability for an inventory item.
    
    Args:
        sku: The SKU
        location_id: Location identifier
        quantity: Available quantity
        price: Price at this location
    """
    token = get_user_token()
    url = f"{BASE_URLS['standard']}/sell/inventory/v1_beta/inventory_item/{sku}/location/{location_id}"
    json_data = {
        "quantity": quantity,
        "price": {
            "value": str(price),
            "currency": "USD",
        },
    }
    return make_request("PUT", url, token, json=json_data)


# ========== Grounding Configuration ==========

def get_grounding_map() -> dict:
    """Return mapping of tools to documentation sources."""
    return {
        "get_taxonomy_categories": {
            "doc": "docs/taxonomy/get-categories.md",
            "endpoint": "GET /commerce/taxonomy/v1/category_tree",
        },
        "get_category_mapping": {
            "doc": "docs/taxonomy/get-category-mapping.md",
            "endpoint": "GET /commerce/taxonomy/v1/category_mapping",
        },
        "get_category_aspects": {
            "doc": "docs/taxonomy/get-category-aspects.md",
            "endpoint": "GET /commerce/taxonomy/v1/category_tree/{categoryId}/aspect_hints",
        },
        "get_compatibility_properties": {
            "doc": "docs/taxonomy/get-compatibility.md",
            "endpoint": "GET /commerce/taxonomy/v1/category_tree/{categoryId}/compatibility_properties",
        },
        "get_catalog_product": {
            "doc": "docs/catalog/get-product.md",
            "endpoint": "GET /commerce/catalog/v1_beta/product/{productId}",
        },
        "search_catalog_products": {
            "doc": "docs/catalog/search-products.md",
            "endpoint": "GET /commerce/catalog/v1_beta/product/search",
        },
        "get_product_recommendations": {
            "doc": "docs/catalog/get-recommendations.md",
            "endpoint": "POST /commerce/catalog/v1_beta/product/recommendation",
        },
        "get_upc_recommended_product": {
            "doc": "docs/catalog/get-upc-recommendation.md",
            "endpoint": "GET /commerce/catalog/v1_beta/product/recommendation/upc/{upc}",
        },
        "get_user_profile": {
            "doc": "docs/identity/get-profile.md",
            "endpoint": "GET /commerce/identity/v1/user/profile",
        },
        "get_user_account": {
            "doc": "docs/identity/get-account.md",
            "endpoint": "GET /commerce/identity/v1/user/account",
        },
        "upload_media": {
            "doc": "docs/media/upload-media.md",
            "endpoint": "POST /commerce/media/v1_beta/upload_media",
        },
        "get_media_status": {
            "doc": "docs/media/get-upload-status.md",
            "endpoint": "GET /commerce/media/v1_beta/upload_status",
        },
        "list_webhook_subscriptions": {
            "doc": "docs/notification/list-subscriptions.md",
            "endpoint": "GET /commerce/notification/v1_beta/subscription",
        },
        "create_webhook_subscription": {
            "doc": "docs/notification/create-subscription.md",
            "endpoint": "POST /commerce/notification/v1_beta/subscription",
        },
        "delete_webhook_subscription": {
            "doc": "docs/notification/delete-subscription.md",
            "endpoint": "DELETE /commerce/notification/v1_beta/subscription/{subscriptionId}",
        },
        "list_webhook_events": {
            "doc": "docs/notification/list-events.md",
            "endpoint": "GET /commerce/notification/v1_beta/subscription/{subscriptionId}/event",
        },
        "translate_text": {
            "doc": "docs/translation/translate.md",
            "endpoint": "POST /commerce/translation/v1_beta/translate",
        },
        "get_translation_supported_languages": {
            "doc": "docs/translation/get-languages.md",
            "endpoint": "GET /commerce/translation/v1_beta/supported_languages",
        },
        "search_charity_organizations": {
            "doc": "docs/charity/search-charities.md",
            "endpoint": "GET /commerce/charity/v1_beta/organization/search",
        },
        "get_charity_organization": {
            "doc": "docs/charity/get-charity.md",
            "endpoint": "GET /commerce/charity/v1_beta/organization/{organizationId}",
        },
        "create_charity_donor_record": {
            "doc": "docs/charity/create-donor.md",
            "endpoint": "POST /commerce/charity/v1_beta/donor_record",
        },
        "get_charity_donor_records": {
            "doc": "docs/charity/list-donors.md",
            "endpoint": "GET /commerce/charity/v1_beta/donor_record",
        },
        "create_item": {
            "doc": "docs/sell/create-item.md",
            "endpoint": "POST /sell/inventory/v1_beta/item",
        },
        "get_item": {
            "doc": "docs/sell/get-item.md",
            "endpoint": "GET /sell/inventory/v1_beta/item/{itemId}",
        },
        "update_item": {
            "doc": "docs/sell/update-item.md",
            "endpoint": "PUT /sell/inventory/v1_beta/item/{itemId}",
        },
        "delete_item": {
            "doc": "docs/sell/delete-item.md",
            "endpoint": "DELETE /sell/inventory/v1_beta/item/{itemId}",
        },
        "list_items": {
            "doc": "docs/sell/list-items.md",
            "endpoint": "GET /sell/inventory/v1_beta/item",
        },
        "create_inventory_item": {
            "doc": "docs/sell/create-inventory.md",
            "endpoint": "POST /sell/inventory/v1_beta/inventory_item",
        },
        "get_inventory_item": {
            "doc": "docs/sell/get-inventory.md",
            "endpoint": "GET /sell/inventory/v1_beta/inventory_item/{sku}",
        },
        "list_inventory_items": {
            "doc": "docs/sell/list-inventory.md",
            "endpoint": "GET /sell/inventory/v1_beta/inventory_item",
        },
        "add_inventory_item_location": {
            "doc": "docs/sell/add-location.md",
            "endpoint": "PUT /sell/inventory/v1_beta/inventory_item/{sku}/location/{locationId}",
        },
    }


if __name__ == "__main__":
    # Run the server over stdio
    mcp.run(transport="stdio")
