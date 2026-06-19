#!/usr/bin/env python3
"""
MCP Server for eBay Commerce API

This server implements tools for interacting with eBay's Commerce API across
multiple namespaces: Catalog, Charity, Identity, Media, Notification, Taxonomy, and Translation.
"""

import os
import requests
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("ebay-commerce-api")

# Configuration
EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_REFRESH_TOKEN = os.environ.get("EBAY_REFRESH_TOKEN")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs based on environment
BASE_URLS = {
    "STANDARD": "https://api.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://api.ebay.com",
    "MEDIA": "https://apim.sandbox.ebay.com" if EBAY_ENVIRONMENT == "SANDBOX" else "https://apim.ebay.com",
}

# Token cache
_app_token = None
_user_token = None
_token_expiry = None

# =============================================================================
# Token Management
# =============================================================================

def get_app_token() -> str:
    """Get or refresh app token using client credentials grant."""
    global _app_token, _token_expiry
    
    # Check if we have a valid token
    if _app_token and _token_expiry and _token_expiry > 0:
        # Token expires in 2 hours (7200 seconds)
        if _token_expiry - 300 > 0:  # Refresh 5 minutes before expiry
            return _app_token
    
    # Request new token
    url = f"{BASE_URLS['STANDARD']}/identity/v1/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    auth = (EBAY_APP_ID, EBAY_CERT_ID)
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope",
    }
    
    response = requests.post(url, headers=headers, auth=auth, data=data)
    response.raise_for_status()
    
    result = response.json()
    _app_token = result["access_token"]
    # Set expiry to 2 hours minus 5 minutes buffer
    _token_expiry = result.get("expires_in", 7200) - 300
    
    return _app_token


def get_user_token() -> str:
    """Get or refresh user token using refresh token grant."""
    global _user_token, _token_expiry
    
    # Check if we have a valid token
    if _user_token and _token_expiry and _token_expiry > 0:
        if _token_expiry - 300 > 0:
            return _user_token
    
    # Request new token
    url = f"{BASE_URLS['STANDARD']}/identity/v1/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    auth = (EBAY_APP_ID, EBAY_CERT_ID)
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN,
        "scope": "https://api.ebay.com/oauth/api_scope",
    }
    
    response = requests.post(url, headers=headers, auth=auth, data=data)
    response.raise_for_status()
    
    result = response.json()
    _user_token = result["access_token"]
    _token_expiry = result.get("expires_in", 7200) - 300
    
    return _user_token


def make_request(
    method: str,
    path: str,
    base: str = "STANDARD",
    params: Optional[Dict] = None,
    data: Optional[Dict] = None,
    headers: Optional[Dict] = None,
    use_user_token: bool = False,
) -> Dict[str, Any]:
    """Make an authenticated request to eBay API."""
    if use_user_token:
        token = get_user_token()
    else:
        token = get_app_token()
    
    url = f"{BASE_URLS[base]}{path}"
    
    request_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    if headers:
        request_headers.update(headers)
    
    response = requests.request(
        method=method,
        url=url,
        headers=request_headers,
        params=params,
        json=data if method in ["POST", "PUT", "PATCH"] else None,
    )
    
    # Handle non-2xx responses gracefully
    if response.status_code >= 400:
        try:
            return {"error": response.json(), "status_code": response.status_code}
        except:
            return {"error": response.text, "status_code": response.status_code}
    
    # Handle 204 No Content
    if response.status_code == 204:
        return {"success": True, "status_code": 204}
    
    try:
        return response.json()
    except:
        return {"response": response.text}


# =============================================================================
# Catalog API Tools
# =============================================================================

@mcp.tool()
def get_product(epid: str) -> Dict[str, Any]:
    """Get detailed information about a product using its eBay Product ID (ePID).
    
    Args:
        epid: The eBay product identifier (ePID) of the product being requested.
        
    Returns:
        Product details including title, description, aspects, images, categories.
    """
    return make_request(
        method="GET",
        path=f"/commerce/catalog/v1_beta/product/{epid}",
        use_user_token=False,
    )


@mcp.tool()
def search_products(
    query: Optional[str] = None,
    category_ids: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    aspect_filter: Optional[Dict] = None,
    field_groups: Optional[str] = None,
    page_size: int = 50,
) -> Dict[str, Any]:
    """Search for products in the eBay catalog.
    
    Args:
        query: Keywords to search for products.
        category_ids: Comma-separated category IDs to filter by.
        gtin: Global Trade Item Number(s) to search for.
        mpn: Manufacturer Part Number(s) to search for.
        aspect_filter: Aspect filter dictionary with categoryId and aspect values.
        field_groups: Type of information to return (MATCHING_PRODUCTS, ASPECT_REFINEMENTS, FULL).
        page_size: Number of results per page (max 200, default 50).
        
    Returns:
        Product summaries matching the search criteria.
    """
    params = {"page_size": page_size}
    
    if query:
        params["query"] = query
    if category_ids:
        params["category_id"] = category_ids
    if gtin:
        params["gtin"] = gtin
    if mpn:
        params["mpn"] = mpn
    if field_groups:
        params["field_groups"] = field_groups
    
    # Build aspect filter if provided
    if aspect_filter:
        aspect_parts = []
        if "categoryId" in aspect_filter:
            aspect_parts.append(f"categoryId:{aspect_filter['categoryId']}")
        for aspect_name, values in aspect_filter.items():
            if aspect_name != "categoryId" and isinstance(values, list):
                values_str = "|".join(values)
                aspect_parts.append(f"{aspect_name}:{{{values_str}}}")
        if aspect_parts:
            params["aspects"] = ",".join(aspect_parts)
    
    return make_request(
        method="GET",
        path="/commerce/catalog/v1_beta/product_summary/search",
        params=params,
        use_user_token=False,
    )


# =============================================================================
# Charity API Tools
# =============================================================================

@mcp.tool()
def get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get detailed information about a charitable organization.
    
    Args:
        charity_org_id: The unique ID of the charitable organization.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).
        
    Returns:
        Charity organization details including name, description, location, logo.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request(
        method="GET",
        path=f"/commerce/charity/v1/charity_org/{charity_org_id}",
        headers=headers,
        use_user_token=False,
    )


# =============================================================================
# Identity API Tools
# =============================================================================

@mcp.tool()
def get_user() -> Dict[str, Any]:
    """Retrieve public account information about the authenticated user.
    
    Returns:
        User account information including user ID, username, account type,
        and contact details (depends on OAuth scope).
    """
    return make_request(
        method="GET",
        path="/commerce/identity/v1/user/",
        use_user_token=True,
    )


@mcp.tool()
def get_public_key(public_key_id: str) -> Dict[str, Any]:
    """Retrieve a public key for validating eBay notification signatures.
    
    Args:
        public_key_id: The unique key ID for the public key.
        
    Returns:
        Public key information including algorithm, digest, and key value.
    """
    return make_request(
        method="GET",
        path=f"/commerce/notification/v1/public_key/{public_key_id}",
        use_user_token=False,
    )


@mcp.tool()
def get_config() -> Dict[str, Any]:
    """Get the current notification configuration.
    
    Returns:
        Configuration details including alert email address.
    """
    return make_request(
        method="GET",
        path="/commerce/notification/v1/config",
        use_user_token=False,
    )


# =============================================================================
# Media API Tools
# =============================================================================

@mcp.tool()
def get_image(image_id: str) -> Dict[str, Any]:
    """Get details of an EPS image including URL and expiration date.
    
    Args:
        image_id: The unique identifier of a created image.
        
    Returns:
        Image details including imageUrl and expirationDate.
    """
    return make_request(
        method="GET",
        path=f"/commerce/media/v1_beta/image/{image_id}",
        base="MEDIA",
        use_user_token=True,
    )


@mcp.tool()
def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """Upload an image to eBay Picture Services (EPS) from a URL.
    
    Args:
        image_url: The URL of the image to upload (must be HTTPS).
        
    Returns:
        Image details including imageUrl and expirationDate.
        The location header contains the image ID URI for future reference.
    """
    headers = {"Content-Type": "application/json"}
    data = {"imageUrl": image_url}
    
    result = make_request(
        method="POST",
        path="/commerce/media/v1_beta/image/create_image_from_url",
        base="MEDIA",
        data=data,
        headers=headers,
        use_user_token=True,
    )
    
    # The actual image ID is in the Location header
    return result


@mcp.tool()
def create_image_from_file(image_file: str) -> Dict[str, Any]:
    """Upload an image to eBay Picture Services (EPS) from a file.
    
    Args:
        image_file: Path to the local image file to upload.
        
    Returns:
        Image details including imageUrl and expirationDate.
    """
    # This would require actual file handling - simplified for now
    return {"error": "File upload not implemented - use create_image_from_url instead"}


@mcp.tool()
def get_video(video_id: str) -> Dict[str, Any]:
    """Get details of a video including metadata and content URLs.
    
    Args:
        video_id: The unique identifier of the video.
        
    Returns:
        Video details including title, size, classification, description,
        playList, status, expiration date, and thumbnail.
    """
    return make_request(
        method="GET",
        path=f"/commerce/media/v1_beta/video/{video_id}",
        base="MEDIA",
        use_user_token=True,
    )


@mcp.tool()
def create_video(title: str, size: int, classification: list, description: Optional[str] = None) -> Dict[str, Any]:
    """Create a video resource for uploading.
    
    Args:
        title: The title of the video.
        size: The size of the video in bytes (max 157,286,400).
        classification: Array of classification objects (currently only "ITEM" is supported).
        description: Optional description of the video.
        
    Returns:
        Video resource details with videoId for upload.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "title": title,
        "size": size,
        "classification": classification,
    }
    if description:
        data["description"] = description
    
    return make_request(
        method="POST",
        path="/commerce/media/v1_beta/video",
        base="MEDIA",
        data=data,
        headers=headers,
        use_user_token=True,
    )


@mcp.tool()
def upload_video(video_id: str, content_length: Optional[int] = None) -> Dict[str, Any]:
    """Upload a video file to a created video resource.
    
    Args:
        video_id: The unique identifier of the video.
        content_length: Optional content length for resumable uploads.
        
    Returns:
        Video upload response.
    """
    headers = {
        "Content-Type": "application/octet-stream",
    }
    if content_length:
        headers["Content-Length"] = str(content_length)
    
    # This would require actual file reading - simplified for now
    return {"error": "Video file upload not implemented - requires file reading and multipart upload"}


@mcp.tool()
def create_document(document_type: str, languages: list) -> Dict[str, Any]:
    """Create a document resource for uploading.
    
    Args:
        document_type: The type of document (e.g., USER_GUIDE_OR_MANUAL).
        languages: Array of language codes (e.g., ["en_US"]).
        
    Returns:
        Document details with documentId for upload.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "documentType": document_type,
        "languages": languages,
    }
    
    return make_request(
        method="POST",
        path="/commerce/media/v1_beta/document",
        data=data,
        headers=headers,
        use_user_token=True,
    )


@mcp.tool()
def upload_document(document_id: str) -> Dict[str, Any]:
    """Upload a document file to a created document resource.
    
    Args:
        document_id: The unique identifier of the document.
        
    Returns:
        Document upload response.
    """
    # This would require actual file handling - simplified for now
    return {"error": "Document file upload not implemented - use multipart form data upload"}


@mcp.tool()
def create_document_from_url(document_url: str, document_type: str, languages: list) -> Dict[str, Any]:
    """Create a document resource by downloading from a URL.
    
    Args:
        document_url: The URL of the document to download (must be HTTPS, max 10MB).
        document_type: The type of document (e.g., USER_GUIDE_OR_MANUAL).
        languages: Array of language codes (e.g., ["en_US"]).
        
    Returns:
        Document details with documentId.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "documentUrl": document_url,
        "documentType": document_type,
        "languages": languages,
    }
    
    return make_request(
        method="POST",
        path="/commerce/media/v1_beta/document/create_document_from_url",
        data=data,
        headers=headers,
        use_user_token=True,
    )


# =============================================================================
# Notification API Tools
# =============================================================================

@mcp.tool()
def create_destination(
    endpoint: str,
    verification_token: str,
    name: Optional[str] = None,
    status: str = "ENABLED",
) -> Dict[str, Any]:
    """Create a destination endpoint for receiving notifications.
    
    Args:
        endpoint: The HTTPS endpoint URL that will receive notifications.
        verification_token: Token for verification (32-80 chars, alphanumeric, underscores, hyphens).
        name: Optional name for the destination.
        status: Destination status (ENABLED or DISABLED).
        
    Returns:
        Destination creation response (204 No Content on success).
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "deliveryConfig": {
            "endpoint": endpoint,
            "verificationToken": verification_token,
        },
        "status": status,
    }
    if name:
        data["name"] = name
    
    return make_request(
        method="POST",
        path="/commerce/notification/v1/destination",
        data=data,
        headers=headers,
        use_user_token=False,
    )


@mcp.tool()
def get_destination(destination_id: str) -> Dict[str, Any]:
    """Get details of a specific destination.
    
    Args:
        destination_id: The unique identifier of the destination.
        
    Returns:
        Destination details including endpoint, status, and configuration.
    """
    return make_request(
        method="GET",
        path=f"/commerce/notification/v1/destination/{destination_id}",
        use_user_token=False,
    )


@mcp.tool()
def update_destination(
    destination_id: str,
    endpoint: Optional[str] = None,
    verification_token: Optional[str] = None,
    name: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """Update an existing destination.
    
    Args:
        destination_id: The unique identifier of the destination.
        endpoint: New endpoint URL (optional).
        verification_token: New verification token (optional).
        name: New name (optional).
        status: New status (optional).
        
    Returns:
        Update response.
    """
    headers = {"Content-Type": "application/json"}
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
    
    return make_request(
        method="PUT",
        path=f"/commerce/notification/v1/destination/{destination_id}",
        data=data,
        headers=headers,
        use_user_token=False,
    )


@mcp.tool()
def delete_destination(destination_id: str) -> Dict[str, Any]:
    """Delete a destination.
    
    Args:
        destination_id: The unique identifier of the destination.
        
    Returns:
        Deletion response.
    """
    return make_request(
        method="DELETE",
        path=f"/commerce/notification/v1/destination/{destination_id}",
        use_user_token=False,
    )


@mcp.tool()
def get_destinations(page_size: int = 20) -> Dict[str, Any]:
    """Get a paginated list of destinations.
    
    Args:
        page_size: Number of destinations per page (10-100, default 20).
        
    Returns:
        List of destinations with pagination info.
    """
    return make_request(
        method="GET",
        path="/commerce/notification/v1/destination",
        params={"page_size": page_size},
        use_user_token=False,
    )


@mcp.tool()
def get_subscriptions(page_size: int = 20) -> Dict[str, Any]:
    """Get a paginated list of subscriptions.
    
    Args:
        page_size: Number of subscriptions per page (10-100, default 20).
        
    Returns:
        List of subscriptions with pagination info.
    """
    return make_request(
        method="GET",
        path="/commerce/notification/v1/subscription",
        params={"page_size": page_size},
        use_user_token=False,
    )


@mcp.tool()
def create_subscription_filter(
    subscription_id: str,
    filter_schema: Dict[str, Any],
) -> Dict[str, Any]:
    """Create a filter for a subscription.
    
    Args:
        subscription_id: The subscription ID to filter.
        filter_schema: JSON Schema document defining the filter criteria.
        
    Returns:
        Subscription filter creation response (201 Created).
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "filterSchema": filter_schema,
    }
    
    return make_request(
        method="POST",
        path=f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        data=data,
        headers=headers,
        use_user_token=False,
    )


@mcp.tool()
def get_subscription_filter(
    subscription_id: str,
    filter_id: str,
) -> Dict[str, Any]:
    """Get details of a subscription filter.
    
    Args:
        subscription_id: The subscription ID.
        filter_id: The filter ID.
        
    Returns:
        Subscription filter details.
    """
    return make_request(
        method="GET",
        path=f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
        use_user_token=False,
    )


@mcp.tool()
def delete_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    """Delete a subscription filter.
    
    Args:
        subscription_id: The subscription ID.
        filter_id: The filter ID.
        
    Returns:
        Deletion response (204 No Content).
    """
    return make_request(
        method="DELETE",
        path=f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
        use_user_token=False,
    )


@mcp.tool()
def update_config(alert_email: str) -> Dict[str, Any]:
    """Update the notification configuration with an alert email.
    
    Args:
        alert_email: The email address for notification alerts.
        
    Returns:
        Configuration update response.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "alertEmail": alert_email,
    }
    
    return make_request(
        method="PUT",
        path="/commerce/notification/v1/config",
        data=data,
        headers=headers,
        use_user_token=False,
    )


@mcp.tool()
def create_subscription(
    topic_id: str,
    destination_id: str,
    status: str,
    schema_version: str,
    delivery_protocol: str = "HTTPS",
    format_type: str = "JSON",
) -> Dict[str, Any]:
    """Create a subscription to a notification topic.
    
    Args:
        topic_id: The unique identifier of the notification topic.
        destination_id: The destination endpoint ID that will receive notifications.
        status: Subscription status (ENABLED or DISABLED).
        schema_version: The schema version for the notification payload.
        delivery_protocol: Delivery protocol (default: HTTPS).
        format_type: Data format (default: JSON).
        
    Returns:
        Subscription creation response (201 Created on success).
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "topicId": topic_id,
        "destinationId": destination_id,
        "status": status,
        "payload": {
            "deliveryProtocol": delivery_protocol,
            "format": format_type,
            "schemaVersion": schema_version,
        },
    }
    
    return make_request(
        method="POST",
        path="/commerce/notification/v1/subscription",
        data=data,
        headers=headers,
        use_user_token=False,
    )


@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Get details of a specific subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription.
        
    Returns:
        Subscription details.
    """
    return make_request(
        method="GET",
        path=f"/commerce/notification/v1/subscription/{subscription_id}",
        use_user_token=False,
    )


@mcp.tool()
def update_subscription(
    subscription_id: str,
    status: Optional[str] = None,
    destination_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Update an existing subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription.
        status: New status (optional).
        destination_id: New destination ID (optional).
        
    Returns:
        Update response.
    """
    headers = {"Content-Type": "application/json"}
    data = {}
    
    if status:
        data["status"] = status
    if destination_id:
        data["destinationId"] = destination_id
    
    return make_request(
        method="PUT",
        path=f"/commerce/notification/v1/subscription/{subscription_id}",
        data=data,
        headers=headers,
        use_user_token=False,
    )


@mcp.tool()
def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """Delete a subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription.
        
    Returns:
        Deletion response.
    """
    return make_request(
        method="DELETE",
        path=f"/commerce/notification/v1/subscription/{subscription_id}",
        use_user_token=False,
    )


@mcp.tool()
def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Enable a disabled subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription.
        
    Returns:
        Enable response.
    """
    return update_subscription(subscription_id, status="ENABLED")


@mcp.tool()
def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Disable an enabled subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription.
        
    Returns:
        Disable response.
    """
    return update_subscription(subscription_id, status="DISABLED")


@mcp.tool()
def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """Test a subscription by sending a test notification.
    
    Args:
        subscription_id: The unique identifier of the subscription.
        
    Returns:
        Test response.
    """
    return make_request(
        method="POST",
        path=f"/commerce/notification/v1/subscription/{subscription_id}/test",
        use_user_token=False,
    )


@mcp.tool()
def get_topics() -> Dict[str, Any]:
    """Get a list of available notification topics.
    
    Returns:
        List of notification topics with supported schemas.
    """
    return make_request(
        method="GET",
        path="/commerce/notification/v1/topic",
        use_user_token=False,
    )


@mcp.tool()
def get_topic(topic_id: str) -> Dict[str, Any]:
    """Get details of a specific notification topic.
    
    Args:
        topic_id: The unique identifier of the topic.
        
    Returns:
        Topic details including supported schemas.
    """
    return make_request(
        method="GET",
        path=f"/commerce/notification/v1/topic/{topic_id}",
        use_user_token=False,
    )


# =============================================================================
# Taxonomy API Tools
# =============================================================================

@mcp.tool()
def get_category_tree(category_tree_id: str = "0") -> Dict[str, Any]:
    """Get the complete category tree for a marketplace.
    
    Args:
        category_tree_id: The unique identifier of the category tree (default: 0).
        
    Returns:
        Complete category tree with all nodes and their hierarchy.
    """
    return make_request(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        use_user_token=False,
    )


@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a subtree of the category tree starting from a specific category.
    
    Args:
        category_tree_id: The unique identifier of the category tree.
        category_id: The category ID to start the subtree from.
        
    Returns:
        Category subtree starting from the specified category.
    """
    return make_request(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/category/{category_id}",
        use_user_token=False,
    )


@mcp.tool()
def get_category_suggestions(
    category_tree_id: str = "0",
    query: str = "",
) -> Dict[str, Any]:
    """Get category suggestions based on keywords.
    
    Args:
        category_tree_id: The unique identifier of the category tree (default: 0).
        query: Free-form text describing the item.
        
    Returns:
        List of suggested categories with relevance scores.
    """
    return make_request(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"query": query},
        use_user_token=False,
    )


@mcp.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace.
    
    Args:
        marketplace_id: The eBay marketplace ID (default: EBAY_US).
        
    Returns:
        Category tree ID for the marketplace.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request(
        method="GET",
        path="/commerce/taxonomy/v1/category_tree/get_default_category_tree_id",
        headers=headers,
        use_user_token=False,
    )


@mcp.tool()
def get_item_aspects_for_category(category_id: str, category_tree_id: str = "0") -> Dict[str, Any]:
    """Get the aspects and their values for a specific category.
    
    Args:
        category_id: The category ID to get aspects for.
        category_tree_id: The category tree ID (default: 0).
        
    Returns:
        List of aspects with their names and possible values.
    """
    return make_request(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/category/{category_id}/item_aspects",
        use_user_token=False,
    )


@mcp.tool()
def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get compatibility properties for a category.
    
    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID.
        
    Returns:
        List of compatibility properties for the category.
    """
    return make_request(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/category/{category_id}/compatibility_properties",
        use_user_token=False,
    )


@mcp.tool()
def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    property_name: str,
) -> Dict[str, Any]:
    """Get values for a specific compatibility property.
    
    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID.
        property_name: The compatibility property name.
        
    Returns:
        List of property values.
    """
    return make_request(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/category/{category_id}/compatibility_properties/{property_name}/values",
        use_user_token=False,
    )


@mcp.tool()
def fetch_item_aspects(epid: str, category_tree_id: str = "0") -> Dict[str, Any]:
    """Fetch item aspects for a product based on its ePID.
    
    Args:
        epid: The eBay product ID.
        category_tree_id: The category tree ID (default: 0).
        
    Returns:
        Item aspects for the product.
    """
    return make_request(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/product/{epid}/item_aspects",
        use_user_token=False,
    )


@mcp.tool()
def get_expired_categories(category_tree_id: str = "0") -> Dict[str, Any]:
    """Get expired category mappings.
    
    Args:
        category_tree_id: The category tree ID (default: 0).
        
    Returns:
        Mapping of expired categories to active categories.
    """
    return make_request(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        use_user_token=False,
    )


# =============================================================================
# Translation API Tools
# =============================================================================

@mcp.tool()
def translate(
    text: str,
    from_lang: str,
    to_lang: str,
    translation_context: str = "ITEM_TITLE",
) -> Dict[str, Any]:
    """Translate text from one language to another.
    
    Args:
        text: The text to translate (max 1000 chars for title, 20000 for description).
        from_lang: Source language code (e.g., "en_US").
        to_lang: Target language code (e.g., "de_DE").
        translation_context: Context of translation (ITEM_TITLE or ITEM_DESCRIPTION).
        
    Returns:
        Translation result with original and translated text.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "from": from_lang,
        "to": to_lang,
        "text": [text],
        "translationContext": translation_context,
    }
    
    return make_request(
        method="POST",
        path="/commerce/translation/v1_beta/translate",
        data=data,
        headers=headers,
        use_user_token=False,
    )


# =============================================================================
# Main entry point
# =============================================================================

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
