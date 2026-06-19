"""
eBay Commerce API MCP Server

This MCP server provides comprehensive coverage of the eBay Commerce API,
suitable for use by an autonomous agent completing real-world tasks.

Authentication:
- App tokens (client_credentials) for Catalog and Taxonomy APIs
- User tokens (refresh_token) for Identity, Media, Notification APIs
"""

import os
import base64
from typing import Any, Dict, Optional
import requests
from fastmcp import FastMCP


# Create MCP server instance
mcp = FastMCP(
    name="eBay Commerce API",
    version="1.0.0",
    description="eBay Commerce API for product catalogs, identity, media, notifications, taxonomy, and translation"
)

# ============================================================================
# Configuration and Constants
# ============================================================================

EBAY_ENV = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
BASE_URLS = {
    "catalog": f"https://api.{ EBAY_ENV }.ebay.com/commerce/catalog/v1_beta",
    "charity": f"https://api.{EBAY_ENV}.ebay.com/commerce/charity/v1_beta",
    "identity": f"https://apiz.{ EBAY_ENV }.ebay.com/commerce/identity/v1",
    "media": f"https://apim.{ EBAY_ENV }.ebay.com/commerce/media/v1_beta",
    "notification": f"https://api.{ EBAY_ENV }.ebay.com/commerce/notification/v1",
    "taxonomy": f"https://api.{ EBAY_ENV }.ebay.com/commerce/taxonomy/v1",
    "translation": f"https://api.{ EBAY_ENV }.ebay.com/commerce/translation/v1_beta",
}

# OAuth endpoints
OAUTH_TOKEN_URL = f"https://api.{EBAY_ENV}.ebay.com/identity/v1/oauth2/token"

# Token caching
_tokens: Dict[str, Dict[str, Any]] = {}

# ============================================================================
# Authentication Functions
# ============================================================================


def get_app_token() -> Optional[str]:
    """Get app token using client_credentials grant (for Catalog/Taxonomy APIs)."""
    if "app" in _tokens:
        token_data = _tokens["app"]
        if token_data.get("expires_at", 0) > 0:
            return token_data.get("access_token")

    client_id = os.getenv("EBAY_APP_ID")
    client_secret = os.getenv("EBAY_CERT_ID")
    if not client_id or not client_secret:
        return None

    payload = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope",
    }

    try:
        auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        headers = {
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = requests.post(OAUTH_TOKEN_URL, data=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        expires_in = data.get("expires_in", 7200)
        _tokens["app"] = {
            "access_token": data.get("access_token"),
            "expires_at": 0,  # We don't track expiry for app tokens in this simple version
        }
        return data.get("access_token")
    except Exception:
        return None


def get_user_token() -> Optional[str]:
    """Get user token using refresh_token grant (for Identity/Media/Notification APIs)."""
    if "user" in _tokens:
        token_data = _tokens["user"]
        if token_data.get("expires_at", 0) > 0:
            return token_data.get("access_token")

    client_id = os.getenv("EBAY_APP_ID")
    client_secret = os.getenv("EBAY_CERT_ID")
    refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
    if not client_id or not client_secret or not refresh_token:
        return None

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "scope": "https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/commerce.identity.readonly https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
    }

    try:
        auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        headers = {
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = requests.post(OAUTH_TOKEN_URL, data=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        expires_in = data.get("expires_in", 7200)
        _tokens["user"] = {
            "access_token": data.get("access_token"),
            "expires_at": 0,  # We don't track expiry for user tokens in this simple version
        }
        return data.get("access_token")
    except Exception:
        return None


def make_request(method: str, namespace: str, path: str, params: Optional[Dict] = None,
                 data: Optional[Dict] = None, headers: Optional[Dict] = None,
                 files: Optional[Dict] = None) -> Dict[str, Any]:
    """Make a request to the eBay API with proper authentication."""
    url = BASE_URLS.get(namespace)
    if not url:
        return {"error": f"Unknown namespace: {namespace}"}

    full_url = f"{url}/{path.lstrip('/')}"
    request_headers = headers or {}
    request_headers["Content-Type"] = "application/json"

    # Determine token type based on namespace
    if namespace in ("catalog", "charity", "taxonomy"):
        token = get_app_token()
        if not token:
            return {"error": "Failed to obtain app token"}
        request_headers["Authorization"] = f"Bearer {token}"
    else:
        token = get_user_token()
        if not token:
            return {"error": "Failed to obtain user token"}
        request_headers["Authorization"] = f"Bearer {token}"

    try:
        if method == "GET":
            response = requests.get(full_url, params=params, headers=request_headers, timeout=30)
        elif method == "POST":
            if files:
                # For multipart/form-data requests (Media API)
                response = requests.post(full_url, params=params, headers=request_headers, files=files, timeout=30)
            else:
                response = requests.post(full_url, json=data, headers=request_headers, timeout=30)
        elif method == "PUT":
            response = requests.put(full_url, json=data, headers=request_headers, timeout=30)
        elif method == "DELETE":
            response = requests.delete(full_url, headers=request_headers, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        # Handle 204 No Content
        if response.status_code == 204:
            return {"success": True, "message": "Operation successful (204 No Content)"}

        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_data = e.response.json()
            return {"error": f"HTTP {e.response.status_code}: {error_data}"}
        except Exception:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# API Tools: Catalog (App Token Required)
# ============================================================================


@mcp.tool()
def get_product(epid: str) -> Dict[str, Any]:
    """Get detailed information about a product using its eBay Product ID (ePID).
    
    Args:
        epid: The eBay product identifier (ePID) of the product
        
    Returns:
        Product details including title, description, aspects, images, categories, identifiers
    """
    return make_request("GET", "catalog", f"product/{epid}")


@mcp.tool()
def search_products(query: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """Search for products in the eBay catalog.
    
    Args:
        query: Search terms to find products
        limit: Maximum number of results to return (max 50)
        offset: Number of results to skip for pagination
        
    Returns:
        Product summaries matching the search query
    """
    params = {"q": query, "limit": limit, "offset": offset}
    return make_request("GET", "catalog", "product_summary", params=params)


# ============================================================================
# API Tools: Charity (App Token Required)
# ============================================================================


@mcp.tool()
def get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    """Get information about a specific charity organization.
    
    Args:
        charity_org_id: The charity organization ID
        
    Returns:
        Charity organization details
    """
    return make_request("GET", "charity", f"charity_org/{charity_org_id}")


@mcp.tool()
def search_charity_orgs(query: str = "", limit: int = 20) -> Dict[str, Any]:
    """Search for charity organizations.
    
    Args:
        query: Search terms to find charity organizations
        limit: Maximum number of results to return (max 100)
        
    Returns:
        List of charity organizations matching the search
    """
    params = {"limit": limit}
    if query:
        params["q"] = query
    return make_request("GET", "charity", "charity_org", params=params)


# ============================================================================
# API Tools: Identity (User Token Required)
# ============================================================================


@mcp.tool()
def get_user() -> Dict[str, Any]:
    """Get authenticated user's account profile information.
    
    Returns:
        User account details including user ID, username, account type, contact info
    """
    return make_request("GET", "identity", "user/")


# ============================================================================
# API Tools: Media (User Token Required)
# ============================================================================


@mcp.tool()
def get_image(image_id: str) -> Dict[str, Any]:
    """Get details of an uploaded image including its EPS URL.
    
    Args:
        image_id: The unique identifier of the created image
        
    Returns:
        Image details including expiration date and image URL
    """
    return make_request("GET", "media", f"image/{image_id}")


@mcp.tool()
def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """Create an image from a URL.
    
    Args:
        image_url: The URL of the image to download and upload (must be HTTPS)
        
    Returns:
        Image details with the created image ID
    """
    data = {"imageUrl": image_url}
    return make_request("POST", "media", "create_image_from_url", data=data)


@mcp.tool()
def create_image_from_file(file_path: str) -> Dict[str, Any]:
    """Create an image by uploading a local file.
    
    Note: This tool is designed for files accessible via the file system.
    
    Args:
        file_path: Path to the local image file (JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP)
        
    Returns:
        Image details with the created image ID
    """
    try:
        with open(file_path, "rb") as f:
            files = {"image": (os.path.basename(file_path), f.read())}
        return make_request("POST", "media", "create_image_from_file", files=files)
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}


@mcp.tool()
def get_video(video_id: str) -> Dict[str, Any]:
    """Get details of an uploaded video.
    
    Args:
        video_id: The unique identifier of the created video
        
    Returns:
        Video details
    """
    return make_request("GET", "media", f"video/{video_id}")


@mcp.tool()
def create_video(title: str, size: int, classification: str = "ITEM",
                 description: str = "") -> Dict[str, Any]:
    """Create a video resource.
    
    Args:
        title: The title of the video (required)
        size: The size of the video in bytes (max 157,286,400)
        classification: The intended use for this video content (default: ITEM)
        description: Optional description of the video
        
    Returns:
        Video details with the created video ID
    """
    data = {
        "title": title,
        "size": size,
        "classification": [classification],
    }
    if description:
        data["description"] = description
    return make_request("POST", "media", "video", data=data)


@mcp.tool()
def upload_video(video_id: str, file_path: str) -> Dict[str, Any]:
    """Upload a video file by associating it with a video ID.
    
    Args:
        video_id: The unique identifier of the created video resource
        file_path: Path to the local video file
        
    Returns:
        Video upload results
    """
    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f.read())}
        return make_request("POST", "media", f"video/{video_id}/upload", files=files)
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}


@mcp.tool()
def get_document(document_id: str) -> Dict[str, Any]:
    """Get details of an uploaded document.
    
    Args:
        document_id: The unique identifier of the created document
        
    Returns:
        Document details
    """
    return make_request("GET", "media", f"document/{document_id}")


@mcp.tool()
def create_document(document_type: str, languages: list) -> Dict[str, Any]:
    """Create a document resource that can be uploaded later.
    
    Args:
        document_type: The type of document (e.g., USER_GUIDE_OR_MANUAL, SAFETY_DATA_SHEET)
        languages: List of language codes (e.g., ['en-US'])
        
    Returns:
        Document details with the created document ID
    """
    data = {
        "documentType": document_type,
        "languages": languages,
    }
    return make_request("POST", "media", "document", data=data)


@mcp.tool()
def create_document_from_url(document_url: str, document_type: str, languages: list) -> Dict[str, Any]:
    """Create a document from a URL.
    
    Args:
        document_url: The URL of the document to download and upload (must be HTTPS)
        document_type: The type of document (e.g., USER_GUIDE_OR_MANUAL, SAFETY_DATA_SHEET)
        languages: List of language codes (e.g., ['en-US'])
        
    Returns:
        Document details with the created document ID
    """
    data = {
        "documentUrl": document_url,
        "documentType": document_type,
        "languages": languages,
    }
    return make_request("POST", "media", "create_document_from_url", data=data)


@mcp.tool()
def upload_document(document_id: str, file_path: str) -> Dict[str, Any]:
    """Upload a document file by associating it with a document ID.
    
    Args:
        document_id: The unique identifier of the created document resource
        file_path: Path to the local document file (PDF, PNG, JPG, JPEG)
        
    Returns:
        Document upload results
    """
    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f.read())}
        return make_request("POST", "media", f"document/{document_id}/upload", files=files)
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}


# ============================================================================
# API Tools: Notification (User Token Required)
# ============================================================================


@mcp.tool()
def get_destination(destination_id: str) -> Dict[str, Any]:
    """Get details of a destination endpoint.
    
    Args:
        destination_id: The unique identifier of the destination
        
    Returns:
        Destination details including endpoint URL and status
    """
    return make_request("GET", "notification", f"destination/{destination_id}")


@mcp.tool()
def list_destinations(limit: int = 20) -> Dict[str, Any]:
    """List all destinations for the application.
    
    Args:
        limit: Maximum number of results to return
        
    Returns:
        List of destination objects
    """
    params = {"limit": limit}
    return make_request("GET", "notification", "destination", params=params)


@mcp.tool()
def create_destination(endpoint: str, verification_token: str, 
                       name: str = "", status: str = "ENABLED") -> Dict[str, Any]:
    """Create a new destination endpoint for receiving notifications.
    
    Args:
        endpoint: The HTTPS endpoint URL that will receive notifications
        verification_token: Token for verifying the endpoint (32-80 chars, alphanumeric, _, -)
        name: Optional name for the destination
        status: Status of the destination (ENABLED or DISABLED)
        
    Returns:
        Response indicating success or failure
    """
    data = {
        "deliveryConfig": {
            "endpoint": endpoint,
            "verificationToken": verification_token,
        },
        "status": status,
    }
    if name:
        data["name"] = name
    return make_request("POST", "notification", "destination", data=data)


@mcp.tool()
def update_destination(destination_id: str, endpoint: Optional[str] = None,
                       verification_token: Optional[str] = None,
                       name: Optional[str] = None,
                       status: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing destination endpoint.
    
    Args:
        destination_id: The unique identifier of the destination to update
        endpoint: New endpoint URL (optional)
        verification_token: New verification token (optional)
        name: New name (optional)
        status: New status (optional)
        
    Returns:
        Response indicating success or failure
    """
    data = {}
    if endpoint:
        data["deliveryConfig"] = data.get("deliveryConfig", {})
        data["deliveryConfig"]["endpoint"] = endpoint
    if verification_token:
        data["deliveryConfig"] = data.get("deliveryConfig", {})
        data["deliveryConfig"]["verificationToken"] = verification_token
    if name:
        data["name"] = name
    if status:
        data["status"] = status
    return make_request("PUT", "notification", f"destination/{destination_id}", data=data)


@mcp.tool()
def delete_destination(destination_id: str) -> Dict[str, Any]:
    """Delete a destination endpoint.
    
    Args:
        destination_id: The unique identifier of the destination to delete
        
    Returns:
        Response indicating success or failure
    """
    return make_request("DELETE", "notification", f"destination/{destination_id}")


@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Get details of a subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription
        
    Returns:
        Subscription details including topic, destination, and status
    """
    return make_request("GET", "notification", f"subscription/{subscription_id}")


@mcp.tool()
def list_subscriptions(limit: int = 20) -> Dict[str, Any]:
    """List all subscriptions for the application.
    
    Args:
        limit: Maximum number of results to return
        
    Returns:
        List of subscription objects
    """
    params = {"limit": limit}
    return make_request("GET", "notification", "subscription", params=params)


@mcp.tool()
def create_subscription(topic_id: str, destination_id: str, 
                        filter_id: str = "") -> Dict[str, Any]:
    """Create a new subscription to a notification topic.
    
    Args:
        topic_id: The unique identifier of the topic to subscribe to
        destination_id: The unique identifier of the destination to receive notifications
        filter_id: Optional filter ID to apply to the subscription
        
    Returns:
        Response with the created subscription details
    """
    data = {
        "topicId": topic_id,
        "destinationId": destination_id,
    }
    if filter_id:
        data["filterId"] = filter_id
    return make_request("POST", "notification", "subscription", data=data)


@mcp.tool()
def update_subscription(subscription_id: str, destination_id: Optional[str] = None,
                        filter_id: Optional[str] = None,
                        status: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription to update
        destination_id: New destination ID (optional)
        filter_id: New filter ID (optional)
        status: New status (optional)
        
    Returns:
        Response indicating success or failure
    """
    data = {}
    if destination_id:
        data["destinationId"] = destination_id
    if filter_id:
        data["filterId"] = filter_id
    if status:
        data["status"] = status
    return make_request("PUT", "notification", f"subscription/{subscription_id}", data=data)


@mcp.tool()
def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """Delete a subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription to delete
        
    Returns:
        Response indicating success or failure
    """
    return make_request("DELETE", "notification", f"subscription/{subscription_id}")


@mcp.tool()
def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Enable a disabled subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription to enable
        
    Returns:
        Response indicating success or failure
    """
    return make_request("POST", "notification", f"subscription/{subscription_id}/enable")


@mcp.tool()
def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Disable an enabled subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription to disable
        
    Returns:
        Response indicating success or failure
    """
    return make_request("POST", "notification", f"subscription/{subscription_id}/disable")


@mcp.tool()
def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """Test a subscription by sending a test notification.
    
    Args:
        subscription_id: The unique identifier of the subscription to test
        
    Returns:
        Response with test results
    """
    return make_request("POST", "notification", f"subscription/{subscription_id}/test")


@mcp.tool()
def get_subscription_filter(filter_id: str) -> Dict[str, Any]:
    """Get details of a subscription filter.
    
    Args:
        filter_id: The unique identifier of the filter
        
    Returns:
        Filter details
    """
    return make_request("GET", "notification", f"subscription_filter/{filter_id}")


@mcp.tool()
def create_subscription_filter(topic_id: str, filter_value: str) -> Dict[str, Any]:
    """Create a new subscription filter.
    
    Args:
        topic_id: The unique identifier of the topic
        filter_value: The filter value (specific to the topic)
        
    Returns:
        Response with the created filter details
    """
    data = {
        "topicId": topic_id,
        "filter": filter_value,
    }
    return make_request("POST", "notification", "subscription_filter", data=data)


@mcp.tool()
def delete_subscription_filter(filter_id: str) -> Dict[str, Any]:
    """Delete a subscription filter.
    
    Args:
        filter_id: The unique identifier of the filter to delete
        
    Returns:
        Response indicating success or failure
    """
    return make_request("DELETE", "notification", f"subscription_filter/{filter_id}")


@mcp.tool()
def get_topic(topic_id: str) -> Dict[str, Any]:
    """Get details of a notification topic.
    
    Args:
        topic_id: The unique identifier of the topic
        
    Returns:
        Topic details including supported schemas and payloads
    """
    return make_request("GET", "notification", f"topic/{topic_id}")


@mcp.tool()
def list_topics() -> Dict[str, Any]:
    """List all available notification topics.
    
    Returns:
        List of available topic objects
    """
    return make_request("GET", "notification", "topic")


@mcp.tool()
def get_config() -> Dict[str, Any]:
    """Get notification configuration settings.
    
    Returns:
        Configuration settings for the application
    """
    return make_request("GET", "notification", "config")


@mcp.tool()
def update_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Update notification configuration settings.
    
    Args:
        config: Configuration settings to update
        
    Returns:
        Response indicating success or failure
    """
    return make_request("PUT", "notification", "config", data=config)


@mcp.tool()
def get_public_key() -> Dict[str, Any]:
    """Get the public key used to verify webhook signatures.
    
    Returns:
        Public key information
    """
    return make_request("GET", "notification", "public_key")


# ============================================================================
# API Tools: Taxonomy (App Token Required)
# ============================================================================


@mcp.tool()
def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """Get a complete category tree.
    
    Args:
        category_tree_id: The unique identifier of the category tree
        
    Returns:
        Complete category tree hierarchy
    """
    return make_request("GET", "taxonomy", f"category_tree/{category_tree_id}")


@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a subtree of the category tree starting from a specific category.
    
    Args:
        category_tree_id: The unique identifier of the category tree
        category_id: The category ID to start the subtree from
        
    Returns:
        Category subtree starting from the specified category
    """
    return make_request("GET", "taxonomy", f"category_tree/{category_tree_id}/category/{category_id}")


@mcp.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace.
    
    Args:
        marketplace_id: The marketplace ID (default: EBAY_US)
        
    Returns:
        Category tree ID for the marketplace
    """
    params = {"marketplace_id": marketplace_id}
    return make_request("GET", "taxonomy", "category_tree/default", params=params)


@mcp.tool()
def get_category_suggestions(category_tree_id: str, query: str) -> Dict[str, Any]:
    """Get category suggestions based on search query.
    
    Args:
        category_tree_id: The unique identifier of the category tree
        query: Search query to find relevant categories
        
    Returns:
        List of suggested categories with relevance scores
    """
    return make_request("GET", "taxonomy", f"category_tree/{category_tree_id}/get_category_suggestions", 
                       params={"q": query})


@mcp.tool()
def get_category_tree_id() -> Dict[str, Any]:
    """Get the default category tree ID for the configured marketplace.
    
    Returns:
        Category tree ID for the default marketplace
    """
    return get_default_category_tree_id()


@mcp.tool()
def get_item_aspects_for_category(category_id: str, category_tree_id: str = "") -> Dict[str, Any]:
    """Get item aspects for a specific category.
    
    Args:
        category_id: The category ID
        category_tree_id: Optional category tree ID (uses default if not provided)
        
    Returns:
        Item aspects for the category
    """
    if not category_tree_id:
        tree_result = get_category_tree_id()
        if "categoryTreeId" in tree_result:
            category_tree_id = tree_result["categoryTreeId"]
    return make_request("GET", "taxonomy", f"category_tree/{category_tree_id}/category/{category_id}/item_aspects")


@mcp.tool()
def fetch_item_aspects(category_id: str, category_tree_id: str = "") -> Dict[str, Any]:
    """Fetch item aspects for a category (alias for get_item_aspects_for_category).
    
    Args:
        category_id: The category ID
        category_tree_id: Optional category tree ID
        
    Returns:
        Item aspects for the category
    """
    return get_item_aspects_for_category(category_id, category_tree_id)


@mcp.tool()
def get_compatibility_properties(category_id: str, category_tree_id: str = "") -> Dict[str, Any]:
    """Get compatibility properties for a category.
    
    Args:
        category_id: The category ID
        category_tree_id: Optional category tree ID
        
    Returns:
        Compatibility properties for the category
    """
    if not category_tree_id:
        tree_result = get_category_tree_id()
        if "categoryTreeId" in tree_result:
            category_tree_id = tree_result["categoryTreeId"]
    return make_request("GET", "taxonomy", f"category_tree/{category_tree_id}/category/{category_id}/compatibility_properties")


@mcp.tool()
def get_compatibility_property_values(property_id: str, category_id: str, 
                                      category_tree_id: str = "") -> Dict[str, Any]:
    """Get values for a compatibility property.
    
    Args:
        property_id: The compatibility property ID
        category_id: The category ID
        category_tree_id: Optional category tree ID
        
    Returns:
        Property values for the compatibility property
    """
    if not category_tree_id:
        tree_result = get_category_tree_id()
        if "categoryTreeId" in tree_result:
            category_tree_id = tree_result["categoryTreeId"]
    return make_request("GET", "taxonomy", 
                       f"category_tree/{category_tree_id}/category/{category_id}/compatibility_properties/{property_id}/values")


@mcp.tool()
def get_expired_categories() -> Dict[str, Any]:
    """Get expired categories for the configured marketplace.
    
    Returns:
        List of expired categories
    """
    return make_request("GET", "taxonomy", "expired_categories")


# ============================================================================
# API Tools: Translation (App Token Required)
# ============================================================================


@mcp.tool()
def translate_text(text: str, from_language: str, to_language: str, 
                   context: str = "ITEM_TITLE") -> Dict[str, Any]:
    """Translate text from one language to another.
    
    Args:
        text: The text to translate
        from_language: Source language code (e.g., 'en_US')
        to_language: Target language code (e.g., 'de_DE')
        context: Translation context - 'ITEM_TITLE' or 'ITEM_DESCRIPTION'
        
    Returns:
        Translation results with original and translated text
    """
    data = {
        "from": from_language,
        "to": to_language,
        "translationContext": context,
        "text": [text],
    }
    return make_request("POST", "translation", "translate", data=data)


# ============================================================================
# Entry point
# ============================================================================


if __name__ == "__main__":
    mcp.run()
