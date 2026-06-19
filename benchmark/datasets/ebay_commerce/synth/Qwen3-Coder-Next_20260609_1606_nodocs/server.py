#!/usr/bin/env python3
"""
eBay Commerce API MCP Server

An MCP server with comprehensive coverage of the eBay Commerce API.
"""

import os
import requests
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    name="eBay-Commerce-API",
    version="1.0.0",
    description="eBay Commerce API MCP Server for autonomous agents"
)

# ============================================================================
# TOKEN MANAGEMENT
# ============================================================================

class TokenManager:
    """Manages eBay OAuth2 tokens (app and user tokens)."""
    
    def __init__(self):
        self._app_token: Optional[str] = None
        self._user_token: Optional[str] = None
        self._app_token_expiry: Optional[float] = None
        self._user_token_expiry: Optional[float] = None
    
    def _get_auth_token(self, grant_type: str, scopes: list[str]) -> dict[str, Any]:
        """Get OAuth2 token from eBay."""
        auth = (
            os.getenv("EBAY_APP_ID", ""),
            os.getenv("EBAY_CERT_ID", ""),
        )
        
        if not auth[0] or not auth[1]:
            return {"error": "EBAY_APP_ID and EBAY_CERT_ID environment variables are required"}
        
        data = {
            "grant_type": grant_type,
            "scope": " ".join(scopes),
        }
        
        if grant_type == "refresh_token":
            data["refresh_token"] = os.getenv("EBAY_REFRESH_TOKEN", "")
        
        env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        base_url = "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"
        
        try:
            response = requests.post(
                f"{base_url}/identity/v1/oauth2/token",
                auth=auth,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to get token: {str(e)}"}
    
    def get_app_token(self) -> Optional[str]:
        """Get or refresh app token for public APIs (taxonomy, catalog)."""
        # Check if we have a valid cached token
        if self._app_token and self._app_token_expiry:
            import time
            if self._app_token_expiry > time.time() + 60:  # Refresh 1 min before expiry
                return self._app_token
        
        result = self._get_auth_token(
            "client_credentials",
            ["https://api.ebay.com/oauth/api_scope"]
        )
        
        if "error" in result:
            return result
        
        if "access_token" in result:
            self._app_token = result["access_token"]
            self._app_token_expiry = result.get("expires_in", 3600) + __import__('time').time()
            return self._app_token
        
        return {"error": result.get("error_description", "Failed to get app token")}
    
    def get_user_token(self) -> Optional[str]:
        """Get or refresh user token for user-scoped APIs."""
        # Check if we have a valid cached token
        if self._user_token and self._user_token_expiry:
            import time
            if self._user_token_expiry > time.time() + 60:  # Refresh 1 min before expiry
                return self._user_token
        
        result = self._get_auth_token(
            "refresh_token",
            [
                "https://api.ebay.com/oauth/api_scope",
                "https://api.ebay.com/oauth/api_scope/sell/marketing",
                "https://api.ebay.com/oauth/api_scope/sell/inventory",
                "https://api.ebay.com/oauth/api_scope/sell/account",
                "https://api.ebay.com/oauth/api_scope/sell/fulfillment",
            ]
        )
        
        if "error" in result:
            return result
        
        if "access_token" in result:
            self._user_token = result["access_token"]
            self._user_token_expiry = result.get("expires_in", 3600) + __import__('time').time()
            return self._user_token
        
        return {"error": result.get("error_description", "Failed to get user token")}
    
    def get_taxonomy_headers(self) -> dict[str, str]:
        """Get headers for taxonomy API calls (app token)."""
        token = self.get_app_token()
        if isinstance(token, dict) and "error" in token:
            return {"Authorization": f"Bearer dummy", "X-ERROR": token["error"]}
        return {"Authorization": f"Bearer {token}"}
    
    def get_catalog_headers(self) -> dict[str, str]:
        """Get headers for catalog API calls (app token)."""
        token = self.get_app_token()
        if isinstance(token, dict) and "error" in token:
            return {"Authorization": f"Bearer dummy", "X-ERROR": token["error"]}
        return {"Authorization": f"Bearer {token}"}
    
    def get_identity_headers(self) -> dict[str, str]:
        """Get headers for identity API calls (user token)."""
        token = self.get_user_token()
        if isinstance(token, dict) and "error" in token:
            return {"Authorization": f"Bearer dummy", "X-ERROR": token["error"]}
        return {"Authorization": f"Bearer {token}"}
    
    def get_media_headers(self) -> dict[str, str]:
        """Get headers for media API calls (user token, different base URL)."""
        token = self.get_user_token()
        if isinstance(token, dict) and "error" in token:
            return {"Authorization": f"Bearer dummy", "X-ERROR": token["error"]}
        return {"Authorization": f"Bearer {token}"}
    
    def get_notification_headers(self) -> dict[str, str]:
        """Get headers for notification API calls (user token)."""
        token = self.get_user_token()
        if isinstance(token, dict) and "error" in token:
            return {"Authorization": f"Bearer dummy", "X-ERROR": token["error"]}
        return {"Authorization": f"Bearer {token}"}
    
    def get_charity_headers(self) -> dict[str, str]:
        """Get headers for charity API calls (user token)."""
        token = self.get_user_token()
        if isinstance(token, dict) and "error" in token:
            return {"Authorization": f"Bearer dummy", "X-ERROR": token["error"]}
        return {"Authorization": f"Bearer {token}"}
    
    def get_translation_headers(self) -> dict[str, str]:
        """Get headers for translation API calls (user token)."""
        token = self.get_user_token()
        if isinstance(token, dict) and "error" in token:
            return {"Authorization": f"Bearer dummy", "X-ERROR": token["error"]}
        return {"Authorization": f"Bearer {token}"}


# Global token manager instance
token_manager = TokenManager()


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def _make_request(
    method: str,
    endpoint: str,
    headers: dict[str, str],
    params: Optional[dict[str, Any]] = None,
    json: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Make an API request to eBay."""
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    
    # Handle different base URLs
    if "/commerce/media/" in endpoint:
        base_url = "https://apim.sandbox.ebay.com" if env == "SANDBOX" else "https://apim.ebay.com"
    else:
        base_url = "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"
    
    url = f"{base_url}{endpoint}"
    
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
        error_body = {}
        try:
            error_body = response.json()
        except:
            error_body = {"message": response.text}
        return {"error": f"HTTP {e.response.status_code}: {error_body.get('errors', error_body)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# TAXONOMY API (App Token)
# ============================================================================

@mcp.tool()
def get_taxonomy_categories(country: str = "US", language: str = "en-US") -> dict[str, Any]:
    """
    Get the complete category tree for a specific country and language.
    
    Args:
        country: Country code (e.g., US, UK, DE)
        language: Language code (e.g., en-US, en-GB, de-DE)
    
    Returns:
        Category tree structure with category IDs, names, and hierarchy
    """
    headers = token_manager.get_taxonomy_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    params = {"country_code": country, "language": language}
    result = _make_request(
        "GET",
        "/commerce/taxonomy/v1/category_tree/get_category_tree",
        headers,
        params=params,
    )
    return result


@mcp.tool()
def get_taxonomy_category(category_id: str) -> dict[str, Any]:
    """
    Get detailed information about a specific category.
    
    Args:
        category_id: The eBay category ID
    
    Returns:
        Category details including attributes, recommendations, and policies
    """
    headers = token_manager.get_taxonomy_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_id}",
        headers,
    )
    return result


@mcp.tool()
def get_taxonomy_aspects(category_id: str) -> dict[str, Any]:
    """
    Get the list of aspects (attributes) for a specific category.
    
    Args:
        category_id: The eBay category ID
    
    Returns:
        List of aspects with their names, types, and value ranges
    """
    headers = token_manager.get_taxonomy_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_id}/aspect_heuristics",
        headers,
    )
    return result


@mcp.tool()
def get_taxonomy_compatibility(category_id: str) -> dict[str, Any]:
    """
    Get compatibility properties for a specific category.
    
    Args:
        category_id: The eBay category ID
    
    Returns:
        Compatibility template information for vehicle/part compatibility
    """
    headers = token_manager.get_taxonomy_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_id}/compatibility",
        headers,
    )
    return result


@mcp.tool()
def search_taxonomy_categories(
    name: str,
    country: str = "US",
    language: str = "en-US",
    limit: int = 10,
) -> dict[str, Any]:
    """
    Search for categories by name.
    
    Args:
        name: Category name to search for
        country: Country code
        language: Language code
        limit: Maximum number of results
    
    Returns:
        List of matching categories
    """
    headers = token_manager.get_taxonomy_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    params = {
        "name": name,
        "country_code": country,
        "language": language,
        "limit": limit,
    }
    result = _make_request(
        "GET",
        "/commerce/taxonomy/v1/category_tree/search_categories",
        headers,
        params=params,
    )
    return result


# ============================================================================
# CATALOG API (App Token)
# ============================================================================

@mcp.tool()
def get_catalog_product(product_id: str) -> dict[str, Any]:
    """
    Get detailed product information from the eBay catalog.
    
    Args:
        product_id: The eBay catalog product ID
    
    Returns:
        Complete product details including title, description, images, specs
    """
    headers = token_manager.get_catalog_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/catalog/v1/product/{product_id}",
        headers,
    )
    return result


@mcp.tool()
def search_catalog_products(
    query: str,
    category_id: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict[str, Any]:
    """
    Search for products in the eBay catalog.
    
    Args:
        query: Search query string
        category_id: Optional category to filter by
        limit: Number of results per page
        offset: Pagination offset
    
    Returns:
        Search results with product matches
    """
    headers = token_manager.get_catalog_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    params = {
        "query": query,
        "limit": limit,
        "offset": offset,
    }
    if category_id:
        params["category_id"] = category_id
    
    result = _make_request(
        "GET",
        "/commerce/catalog/v1/product/search",
        headers,
        params=params,
    )
    return result


@mcp.tool()
def get_catalog_product_variants(product_id: str) -> dict[str, Any]:
    """
    Get variant information for a catalog product.
    
    Args:
        product_id: The eBay catalog product ID
    
    Returns:
        List of variants with their attributes and identifiers
    """
    headers = token_manager.get_catalog_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/catalog/v1/product/{product_id}/variants",
        headers,
    )
    return result


@mcp.tool()
def get_catalog_eans(product_id: str) -> dict[str, Any]:
    """
    Get EANs (European Article Numbers) for a catalog product.
    
    Args:
        product_id: The eBay catalog product ID
    
    Returns:
        List of EANs for the product
    """
    headers = token_manager.get_catalog_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/catalog/v1/product/{product_id}/ean",
        headers,
    )
    return result


@mcp.tool()
def get_catalog_isbns(product_id: str) -> dict[str, Any]:
    """
    Get ISBNs (International Standard Book Numbers) for a catalog product.
    
    Args:
        product_id: The eBay catalog product ID
    
    Returns:
        List of ISBNs for the product
    """
    headers = token_manager.get_catalog_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/catalog/v1/product/{product_id}/isbn",
        headers,
    )
    return result


@mcp.tool()
def get_catalog_upcs(product_id: str) -> dict[str, Any]:
    """
    Get UPCs (Universal Product Codes) for a catalog product.
    
    Args:
        product_id: The eBay catalog product ID
    
    Returns:
        List of UPCs for the product
    """
    headers = token_manager.get_catalog_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/catalog/v1/product/{product_id}/upc",
        headers,
    )
    return result


# ============================================================================
# IDENTITY API (User Token)
# ============================================================================

@mcp.tool()
def get_user_profile() -> dict[str, Any]:
    """
    Get the current user's profile information.
    
    Returns:
        User profile including user ID, username, email, and account details
    """
    headers = token_manager.get_identity_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        "/commerce/identity/v1/user",
        headers,
    )
    return result


@mcp.tool()
def get_user_account() -> dict[str, Any]:
    """
    Get the current user's account information.
    
    Returns:
        Account details including status, policies, and performance metrics
    """
    headers = token_manager.get_identity_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        "/commerce/identity/v1/user/account",
        headers,
    )
    return result


@mcp.tool()
def get_user_disputes() -> dict[str, Any]:
    """
    Get disputes filed by the current user.
    
    Returns:
        List of disputes with case details and status
    """
    headers = token_manager.get_identity_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        "/commerce/identity/v1/user/disputes",
        headers,
    )
    return result


# ============================================================================
# MEDIA API (User Token - Different Base URL)
# ============================================================================

@mcp.tool()
def upload_media_from_url(
    media_type: str = "IMAGE",
    content_type: str = "image/jpeg",
    content_url: str = "",
    filename: str = "",
) -> dict[str, Any]:
    """
    Upload media to eBay by providing a URL.
    
    Args:
        media_type: Type of media (IMAGE, VIDEO, DOCUMENT, AUDIO)
        content_type: MIME type of the content
        content_url: URL where the media is hosted
        filename: Optional filename for the media
    
    Returns:
        Media details including eBay media ID and URLs
    """
    headers = token_manager.get_media_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    payload = {
        "media_type": media_type,
        "content_type": content_type,
        "content_url": content_url,
    }
    if filename:
        payload["filename"] = filename
    
    result = _make_request(
        "POST",
        "/commerce/media/v1/upload_url",
        headers,
        json=payload,
    )
    return result


@mcp.tool()
def get_media_status(media_id: str) -> dict[str, Any]:
    """
    Get the status of a media upload.
    
    Args:
        media_id: The eBay media ID
    
    Returns:
        Upload status and media URLs
    """
    headers = token_manager.get_media_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/media/v1/upload_status/{media_id}",
        headers,
    )
    return result


@mcp.tool()
def create_media_repository(
    media_type: str = "IMAGE",
    title: str = "",
    description: str = "",
    folder_path: str = "",
) -> dict[str, Any]:
    """
    Create a new media repository (folder) for organizing media.
    
    Args:
        media_type: Type of media to store (IMAGE, VIDEO, DOCUMENT, AUDIO)
        title: Title for the repository
        description: Description of the repository contents
        folder_path: Optional folder path for organization
    
    Returns:
        Created repository details
    """
    headers = token_manager.get_media_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    payload = {"media_type": media_type}
    if title:
        payload["title"] = title
    if description:
        payload["description"] = description
    if folder_path:
        payload["folder_path"] = folder_path
    
    result = _make_request(
        "POST",
        "/commerce/media/v1/media_repository",
        headers,
        json=payload,
    )
    return result


@mcp.tool()
def list_media_repositories(
    media_type: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict[str, Any]:
    """
    List media repositories (folders) for the user.
    
    Args:
        media_type: Optional filter by media type
        limit: Number of results per page
        offset: Pagination offset
    
    Returns:
        List of media repositories
    """
    headers = token_manager.get_media_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    if media_type:
        params["media_type"] = media_type
    
    result = _make_request(
        "GET",
        "/commerce/media/v1/media_repository",
        headers,
        params=params,
    )
    return result


# ============================================================================
# NOTIFICATION API (User Token)
# ============================================================================

@mcp.tool()
def create_webhook_subscription(
    topic: str,
    callback_url: str,
    delivery_mode: str = "REST_PUSH",
    media_types: Optional[list[str]] = None,
) -> dict[str, Any]:
    """
    Create a webhook subscription to receive eBay events.
    
    Args:
        topic: Event topic to subscribe to (e.g., order, feedback, payout)
        callback_url: URL to receive webhook notifications
        delivery_mode: Delivery method (REST_PUSH or HTTP_PULL)
        media_types: Optional list of media types for image/video events
    
    Returns:
        Subscription details including ID and status
    """
    headers = token_manager.get_notification_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    payload = {
        "topic": topic,
        "callbackUrl": callback_url,
        "deliveryMode": delivery_mode,
    }
    if media_types:
        payload["mediaTypes"] = media_types
    
    result = _make_request(
        "POST",
        "/commerce/notification/subscription",
        headers,
        json=payload,
    )
    return result


@mcp.tool()
def list_webhook_subscriptions() -> dict[str, Any]:
    """
    List all webhook subscriptions for the user.
    
    Returns:
        List of subscriptions with their configurations
    """
    headers = token_manager.get_notification_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        "/commerce/notification/subscription",
        headers,
    )
    return result


@mcp.tool()
def get_webhook_subscription(subscription_id: str) -> dict[str, Any]:
    """
    Get details of a specific webhook subscription.
    
    Args:
        subscription_id: The subscription ID
    
    Returns:
        Subscription configuration and status
    """
    headers = token_manager.get_notification_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "GET",
        f"/commerce/notification/subscription/{subscription_id}",
        headers,
    )
    return result


@mcp.tool()
def delete_webhook_subscription(subscription_id: str) -> dict[str, Any]:
    """
    Delete a webhook subscription.
    
    Args:
        subscription_id: The subscription ID to delete
    
    Returns:
        Deletion confirmation
    """
    headers = token_manager.get_notification_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    result = _make_request(
        "DELETE",
        f"/commerce/notification/subscription/{subscription_id}",
        headers,
    )
    return result


@mcp.tool()
def get_notification_events(
    subscription_id: str,
    limit: int = 20,
    offset: int = 0,
) -> dict[str, Any]:
    """
    Get events delivered to a webhook subscription.
    
    Args:
        subscription_id: The subscription ID
        limit: Number of results per page
        offset: Pagination offset
    
    Returns:
        List of delivered events with details
    """
    headers = token_manager.get_notification_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    result = _make_request(
        "GET",
        f"/commerce/notification/subscription/{subscription_id}/event",
        headers,
        params=params,
    )
    return result


# ============================================================================
# CHARITY API (User Token)
# ============================================================================

@mcp.tool()
def get_charity_organizations(
    organization_id: Optional[str] = None,
    name: Optional[str] = None,
    category: Optional[str] = None,
) -> dict[str, Any]:
    """
    Search for eBay for Charity organizations.
    
    Args:
        organization_id: Optional specific organization ID
        name: Search by organization name
        category: Filter by charity category
    
    Returns:
        Charity organization details including EIN and category
    """
    headers = token_manager.get_charity_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    params = {}
    if organization_id:
        params["organization_id"] = organization_id
    if name:
        params["name"] = name
    if category:
        params["category"] = category
    
    result = _make_request(
        "GET",
        "/commerce/charity/v1/organization",
        headers,
        params=params,
    )
    return result


@mcp.tool()
def get_charity_campaigns(
    organization_id: str,
    limit: int = 20,
    offset: int = 0,
) -> dict[str, Any]:
    """
    Get campaigns for a specific charity organization.
    
    Args:
        organization_id: The charity organization ID
        limit: Number of results per page
        offset: Pagination offset
    
    Returns:
        List of charity campaigns
    """
    headers = token_manager.get_charity_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    result = _make_request(
        "GET",
        f"/commerce/charity/v1/organization/{organization_id}/campaign",
        headers,
        params=params,
    )
    return result


@mcp.tool()
def create_charity_donation(
    organization_id: str,
    amount: float,
    currency: str = "USD",
) -> dict[str, Any]:
    """
    Create a donation to a charity organization.
    
    Args:
        organization_id: The charity organization ID
        amount: Donation amount
        currency: Currency code (USD, EUR, GBP, etc.)
    
    Returns:
        Donation confirmation with transaction ID
    """
    headers = token_manager.get_charity_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    payload = {
        "organization_id": organization_id,
        "amount": amount,
        "currency": currency,
    }
    
    result = _make_request(
        "POST",
        "/commerce/charity/v1/donation",
        headers,
        json=payload,
    )
    return result


# ============================================================================
# TRANSLATION API (User Token)
# ============================================================================

@mcp.tool()
def translate_text(
    text: str,
    source_language: str = "en",
    target_language: str = "es",
    context: str = "general",
) -> dict[str, Any]:
    """
    Translate text between languages.
    
    Args:
        text: Text to translate
        source_language: Source language code (e.g., en, es, fr)
        target_language: Target language code
        context: Translation context (general, commerce, automotive)
    
    Returns:
        Translated text and metadata
    """
    headers = token_manager.get_translation_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    payload = {
        "text": text,
        "source_language": source_language,
        "target_language": target_language,
        "context": context,
    }
    
    result = _make_request(
        "POST",
        "/commerce/translation/v1/translate",
        headers,
        json=payload,
    )
    return result


@mcp.tool()
def detect_language(text: str) -> dict[str, Any]:
    """
    Detect the language of provided text.
    
    Args:
        text: Text to analyze
    
    Returns:
        Detected language code and confidence score
    """
    headers = token_manager.get_translation_headers()
    if "Authorization" not in headers or "X-ERROR" in headers:
        return headers
    
    payload = {"text": text}
    
    result = _make_request(
        "POST",
        "/commerce/translation/v1/detect",
        headers,
        json=payload,
    )
    return result


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    import sys
    import asyncio
    
    # Run the server over stdio
    mcp.run()
