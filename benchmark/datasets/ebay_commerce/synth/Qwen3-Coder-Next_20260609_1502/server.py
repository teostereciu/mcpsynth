#!/usr/bin/env python3
"""
eBay Commerce API MCP Server

An MCP server for interacting with the eBay Commerce API.
"""

import os
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("ebay-commerce-api")

# Helper functions


def get_app_token() -> Optional[str]:
    """Get app token using client credentials grant."""
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    if not app_id or not cert_id:
        return None

    url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }

    auth = (app_id, cert_id)
    try:
        response = requests.post(url, headers=headers, data=data, auth=auth)
        response.raise_for_status()
        return response.json().get("access_token")
    except Exception:
        return None


def get_user_token() -> Optional[str]:
    """Get user token using refresh token grant."""
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")

    if not app_id or not cert_id or not refresh_token:
        return None

    url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "scope": "https://api.ebay.com/oauth/api_scope"
    }

    auth = (app_id, cert_id)
    try:
        response = requests.post(url, headers=headers, data=data, auth=auth)
        response.raise_for_status()
        return response.json().get("access_token")
    except Exception:
        return None


def make_request(
    method: str,
    endpoint: str,
    base_url: str,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    app_token: bool = False,
    user_token: bool = False
) -> Dict[str, Any]:
    """Make a request to eBay API."""
    if headers is None:
        headers = {}

    # Add appropriate token
    if app_token:
        token = get_app_token()
        if token:
            headers["Authorization"] = f"Bearer {token}"
        else:
            return {"error": "Failed to get app token"}

    elif user_token:
        token = get_user_token()
        if token:
            headers["Authorization"] = f"Bearer {token}"
        else:
            return {"error": "Failed to get user token"}

    url = f"{base_url}{endpoint}"

    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_json = e.response.json()
            return {"error": error_json}
        except Exception:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# CATALOG API
# =============================================================================


@mcp.tool()
def get_product(epid: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """
    Get detailed information about a catalog product.

    Args:
        epid: The eBay product identifier (ePID) of the product.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Product details including title, description, aspects, images, etc.
    """
    endpoint = f"/commerce/catalog/v1_beta/product/{epid}"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        app_token=True
    )


@mcp.tool()
def search_products(
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: str = "50",
    offset: str = "0",
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Search for products in the eBay catalog.

    Args:
        q: Search keywords.
        gtin: GTIN (EAN, ISBN, UPC) to search for.
        mpn: Manufacturer Part Number to search for.
        category_ids: Comma-separated category IDs to filter by.
        aspect_filter: Aspect filter in format: categoryId:cat_id,aspect1:{val1|val2},...
        fieldgroups: Field groups to include (MATCHING_PRODUCTS, ASPECT_REFINEMENTS, FULL).
        limit: Number of results to return (max 200, default 50).
        offset: Number of results to skip (for pagination).
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Product summaries matching the search criteria.
    """
    endpoint = "/commerce/catalog/v1_beta/product_summary/search"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}

    params = {}
    if q:
        params["q"] = q
    if gtin:
        params["gtin"] = gtin
    if mpn:
        params["mpn"] = mpn
    if category_ids:
        params["category_ids"] = category_ids
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    params["limit"] = limit
    params["offset"] = offset

    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


# =============================================================================
# CHARITY API
# =============================================================================


@mcp.tool()
def get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """
    Get detailed information about a charitable organization.

    Args:
        charity_org_id: The unique ID of the charitable organization.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Charity organization details including name, description, location, etc.
    """
    endpoint = f"/commerce/charity/v1/charity_org/{charity_org_id}"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        app_token=True
    )


@mcp.tool()
def search_charity_orgs(
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: str = "20",
    offset: str = "0",
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Search for charitable organizations.

    Args:
        q: Query string to search by name, mission, or description.
        registration_ids: Comma-separated list of registration IDs.
        limit: Number of results per page (max 100, default 20).
        offset: Number of results to skip (for pagination).
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Paginated search results for charity organizations.
    """
    endpoint = "/commerce/charity/v1/charity_org"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}

    params = {}
    if q:
        params["q"] = q
    if registration_ids:
        params["registration_ids"] = registration_ids
    params["limit"] = limit
    params["offset"] = offset

    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


# =============================================================================
# IDENTITY API
# =============================================================================


@mcp.tool()
def get_user() -> Dict[str, Any]:
    """
    Get authenticated user's account profile information.

    Returns:
        User account information including user ID, username, account type, etc.
    """
    endpoint = "/commerce/identity/v1/user/"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://apiz.sandbox.ebay.com",
        user_token=True
    )


# =============================================================================
# MEDIA API (images, documents, videos)
# =============================================================================


@mcp.tool()
def get_image(image_id: str) -> Dict[str, Any]:
    """
    Get details of an uploaded image, including the EPS URL.

    Args:
        image_id: The unique identifier of the image.

    Returns:
        Image details including imageUrl and expirationDate.
    """
    endpoint = f"/commerce/media/v1_beta/image/{image_id}"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://apim.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """
    Upload an image to eBay Picture Services (EPS) from a URL.

    Args:
        image_url: The HTTPS URL of the image to upload.

    Returns:
        Image details including the image ID (in Location header) and expiration date.
    """
    endpoint = "/commerce/media/v1_beta/image/create_image_from_url"
    headers = {"Content-Type": "application/json"}
    data = {"imageUrl": image_url}
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://apim.sandbox.ebay.com",
        headers=headers,
        data=data,
        user_token=True
    )


@mcp.tool()
def create_image_from_file(file_path: str) -> Dict[str, Any]:
    """
    Upload an image to eBay Picture Services (EPS) from a local file.

    Args:
        file_path: Path to the image file to upload.

    Returns:
        Image details including the image ID and expiration date.
    """
    endpoint = "/commerce/media/v1_beta/image/create_image_from_file"
    headers = {"Content-Type": "multipart/form-data"}

    # Read file
    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            return make_request(
                method="POST",
                endpoint=endpoint,
                base_url="https://apim.sandbox.ebay.com",
                headers=headers,
                files=files,
                user_token=True
            )
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}


@mcp.tool()
def create_document(document_type: str, languages: list) -> Dict[str, Any]:
    """
    Create a document reference for upload.

    Args:
        document_type: Type of document (e.g., USER_GUIDE_OR_MANUAL, SAFETY_DATA_SHEET).
        languages: List of languages in the document.

    Returns:
        Document details including documentId for subsequent upload.
    """
    endpoint = "/commerce/media/v1_beta/document"
    headers = {"Content-Type": "application/json"}
    data = {
        "documentType": document_type,
        "languages": languages
    }
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=data,
        user_token=True
    )


@mcp.tool()
def create_document_from_url(document_type: str, languages: list, document_url: str) -> Dict[str, Any]:
    """
    Create a document reference from a URL.

    Args:
        document_type: Type of document (e.g., USER_GUIDE_OR_MANUAL, SAFETY_DATA_SHEET).
        languages: List of languages in the document.
        document_url: URL where the document is hosted.

    Returns:
        Document details including documentId.
    """
    endpoint = "/commerce/media/v1_beta/document/create_document_from_url"
    headers = {"Content-Type": "application/json"}
    data = {
        "documentType": document_type,
        "languages": languages,
        "documentUrl": document_url
    }
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=data,
        user_token=True
    )


@mcp.tool()
def get_document(document_id: str) -> Dict[str, Any]:
    """
    Get details of a created document.

    Args:
        document_id: The unique identifier of the document.

    Returns:
        Document details including status, type, languages.
    """
    endpoint = f"/commerce/media/v1_beta/document/{document_id}"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def upload_document(document_id: str, file_path: str) -> Dict[str, Any]:
    """
    Upload a document file.

    Args:
        document_id: The document ID from create_document.
        file_path: Path to the document file to upload.

    Returns:
        Upload status.
    """
    endpoint = f"/commerce/media/v1_beta/document/{document_id}/upload"
    headers = {"Content-Type": "multipart/form-data"}

    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            return make_request(
                method="POST",
                endpoint=endpoint,
                base_url="https://api.sandbox.ebay.com",
                headers=headers,
                files=files,
                user_token=True
            )
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}


@mcp.tool()
def get_video(video_id: str) -> Dict[str, Any]:
    """
    Get details of an uploaded video.

    Args:
        video_id: The unique identifier of the video.

    Returns:
        Video details.
    """
    endpoint = f"/commerce/media/v1_beta/video/{video_id}"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://apim.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def create_video(title: str, description: str, video_file_path: str) -> Dict[str, Any]:
    """
    Create a video upload.

    Args:
        title: Video title.
        description: Video description.
        video_file_path: Path to the video file.

    Returns:
        Video details including video ID.
    """
    endpoint = "/commerce/media/v1_beta/video"
    headers = {"Content-Type": "multipart/form-data"}

    try:
        with open(video_file_path, "rb") as f:
            files = {"file": (os.path.basename(video_file_path), f)}
            data = {
                "title": title,
                "description": description
            }
            return make_request(
                method="POST",
                endpoint=endpoint,
                base_url="https://apim.sandbox.ebay.com",
                headers=headers,
                data=data,
                files=files,
                user_token=True
            )
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}


@mcp.tool()
def upload_video(video_id: str, file_path: str) -> Dict[str, Any]:
    """
    Upload a video file.

    Args:
        video_id: The video ID from create_video.
        file_path: Path to the video file to upload.

    Returns:
        Upload status.
    """
    endpoint = f"/commerce/media/v1_beta/video/{video_id}/upload"
    headers = {"Content-Type": "multipart/form-data"}

    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            return make_request(
                method="POST",
                endpoint=endpoint,
                base_url="https://apim.sandbox.ebay.com",
                headers=headers,
                files=files,
                user_token=True
            )
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}


# =============================================================================
# NOTIFICATION API
# =============================================================================


@mcp.tool()
def get_config() -> Dict[str, Any]:
    """
    Get notification configuration.

    Returns:
        Notification configuration details.
    """
    endpoint = "/commerce/notification/v1/config"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def update_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update notification configuration.

    Args:
        config: Configuration object to update.

    Returns:
        Updated configuration.
    """
    endpoint = "/commerce/notification/v1/config"
    headers = {"Content-Type": "application/json"}
    return make_request(
        method="PUT",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=config,
        user_token=True
    )


@mcp.tool()
def create_destination(destination: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a notification destination.

    Args:
        destination: Destination configuration.

    Returns:
        Created destination with destinationId.
    """
    endpoint = "/commerce/notification/v1/destination"
    headers = {"Content-Type": "application/json"}
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=destination,
        user_token=True
    )


@mcp.tool()
def delete_destination(destination_id: str) -> Dict[str, Any]:
    """
    Delete a notification destination.

    Args:
        destination_id: The ID of the destination to delete.

    Returns:
        Deletion status.
    """
    endpoint = f"/commerce/notification/v1/destination/{destination_id}"
    return make_request(
        method="DELETE",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def get_destination(destination_id: str) -> Dict[str, Any]:
    """
    Get a notification destination.

    Args:
        destination_id: The ID of the destination.

    Returns:
        Destination details.
    """
    endpoint = f"/commerce/notification/v1/destination/{destination_id}"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def get_destinations() -> Dict[str, Any]:
    """
    Get all notification destinations.

    Returns:
        List of destinations.
    """
    endpoint = "/commerce/notification/v1/destination"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def update_destination(destination_id: str, destination: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update a notification destination.

    Args:
        destination_id: The ID of the destination to update.
        destination: Updated destination configuration.

    Returns:
        Updated destination.
    """
    endpoint = f"/commerce/notification/v1/destination/{destination_id}"
    headers = {"Content-Type": "application/json"}
    return make_request(
        method="PUT",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=destination,
        user_token=True
    )


@mcp.tool()
def get_public_key(public_key_id: str) -> Dict[str, Any]:
    """
    Get a notification public key.

    Args:
        public_key_id: The ID of the public key.

    Returns:
        Public key details.
    """
    endpoint = f"/commerce/notification/v1/public_key/{public_key_id}"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def create_subscription(
    topic_id: str,
    destination_id: str,
    status: str,
    schema_version: str,
    delivery_protocol: str = "HTTPS",
    format_type: str = "JSON"
) -> Dict[str, Any]:
    """
    Create a notification subscription.

    Args:
        topic_id: The topic to subscribe to.
        destination_id: The destination for notifications.
        status: Subscription status (ENABLED or DISABLED).
        schema_version: Schema version for the subscription.
        delivery_protocol: Delivery protocol (default: HTTPS).
        format_type: Data format (default: JSON).

    Returns:
        Subscription creation status.
    """
    endpoint = "/commerce/notification/v1/subscription"
    headers = {"Content-Type": "application/json"}
    data = {
        "topicId": topic_id,
        "destinationId": destination_id,
        "status": status,
        "payload": {
            "schemaVersion": schema_version,
            "deliveryProtocol": delivery_protocol,
            "format": format_type
        }
    }
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=data,
        user_token=True
    )


@mcp.tool()
def create_subscription_filter(
    subscription_id: str,
    filter_expression: str
) -> Dict[str, Any]:
    """
    Create a subscription filter.

    Args:
        subscription_id: The subscription ID.
        filter_expression: The filter expression.

    Returns:
        Filter creation status.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}/filter"
    headers = {"Content-Type": "application/json"}
    data = {"filter": filter_expression}
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=data,
        user_token=True
    )


@mcp.tool()
def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """
    Delete a notification subscription.

    Args:
        subscription_id: The ID of the subscription to delete.

    Returns:
        Deletion status.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}"
    return make_request(
        method="DELETE",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def delete_subscription_filter(
    subscription_id: str,
    filter_id: str
) -> Dict[str, Any]:
    """
    Delete a subscription filter.

    Args:
        subscription_id: The subscription ID.
        filter_id: The filter ID.

    Returns:
        Deletion status.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}"
    return make_request(
        method="DELETE",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """
    Disable a notification subscription.

    Args:
        subscription_id: The ID of the subscription to disable.

    Returns:
        Status of disable operation.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}/disable"
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """
    Enable a notification subscription.

    Args:
        subscription_id: The ID of the subscription to enable.

    Returns:
        Status of enable operation.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}/enable"
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """
    Get a notification subscription.

    Args:
        subscription_id: The ID of the subscription.

    Returns:
        Subscription details.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def get_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    """
    Get a subscription filter.

    Args:
        subscription_id: The subscription ID.
        filter_id: The filter ID.

    Returns:
        Filter details.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def get_subscriptions() -> Dict[str, Any]:
    """
    Get all notification subscriptions.

    Returns:
        List of subscriptions.
    """
    endpoint = "/commerce/notification/v1/subscription"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """
    Test a notification subscription.

    Args:
        subscription_id: The ID of the subscription to test.

    Returns:
        Test result.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}/test"
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def update_subscription(
    subscription_id: str,
    status: Optional[str] = None,
    destination_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update a notification subscription.

    Args:
        subscription_id: The ID of the subscription to update.
        status: New status (ENABLED or DISABLED).
        destination_id: New destination ID.

    Returns:
        Updated subscription.
    """
    endpoint = f"/commerce/notification/v1/subscription/{subscription_id}"
    headers = {"Content-Type": "application/json"}
    data = {}
    if status:
        data["status"] = status
    if destination_id:
        data["destinationId"] = destination_id
    return make_request(
        method="PUT",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=data,
        user_token=True
    )


@mcp.tool()
def get_topic(topic_id: str) -> Dict[str, Any]:
    """
    Get a notification topic.

    Args:
        topic_id: The ID of the topic.

    Returns:
        Topic details including supported payloads.
    """
    endpoint = f"/commerce/notification/v1/topic/{topic_id}"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


@mcp.tool()
def get_topics() -> Dict[str, Any]:
    """
    Get all notification topics.

    Returns:
        List of topics.
    """
    endpoint = "/commerce/notification/v1/topic"
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        user_token=True
    )


# =============================================================================
# TAXONOMY API
# =============================================================================


@mcp.tool()
def get_category_tree(category_tree_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """
    Get a complete category tree.

    Args:
        category_tree_id: The unique identifier of the category tree.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Complete category tree structure.
    """
    endpoint = f"/commerce/taxonomy/v1/category_tree/{category_tree_id}"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        app_token=True
    )


@mcp.tool()
def get_category_subtree(
    category_tree_id: str,
    category_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Get a category subtree.

    Args:
        category_tree_id: The unique identifier of the category tree.
        category_id: The ID of the category to get subtree for.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Category subtree structure.
    """
    endpoint = f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    params = {"category_id": category_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


@mcp.tool()
def get_category_suggestions(
    category_tree_id: str,
    q: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Get category suggestions based on keywords.

    Args:
        category_tree_id: The unique identifier of the category tree.
        q: Search query.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Category suggestions.
    """
    endpoint = f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    params = {"q": q}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


@mcp.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """
    Get the default category tree ID for a marketplace.

    Args:
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Category tree ID.
    """
    endpoint = "/commerce/taxonomy/v1/get_default_category_tree_id"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    params = {"marketplace_id": marketplace_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


@mcp.tool()
def get_compatibility_properties(
    category_tree_id: str,
    category_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Get compatibility properties for a category.

    Args:
        category_tree_id: The unique identifier of the category tree.
        category_id: The category ID.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Compatibility properties.
    """
    endpoint = f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    params = {"category_id": category_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


@mcp.tool()
def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter_str: Optional[str] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Get compatibility property values.

    Args:
        category_tree_id: The unique identifier of the category tree.
        category_id: The category ID.
        compatibility_property: The compatibility property name.
        filter_str: Filter string in format "key:value,key2:value2".
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Compatibility property values.
    """
    endpoint = f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    params = {
        "category_id": category_id,
        "compatibility_property": compatibility_property
    }
    if filter_str:
        params["filter"] = filter_str
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


@mcp.tool()
def get_expired_categories(category_tree_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """
    Get expired categories in a category tree.

    Args:
        category_tree_id: The unique identifier of the category tree.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Expired categories.
    """
    endpoint = f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        app_token=True
    )


@mcp.tool()
def get_item_aspects_for_category(
    category_tree_id: str,
    category_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Get item aspects for a category.

    Args:
        category_tree_id: The unique identifier of the category tree.
        category_id: The category ID.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Item aspects for the category.
    """
    endpoint = f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    params = {"category_id": category_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


@mcp.tool()
def fetch_item_aspects(
    category_tree_id: str,
    category_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Fetch item aspects for a category.

    Args:
        category_tree_id: The unique identifier of the category tree.
        category_id: The category ID.
        marketplace_id: The eBay marketplace ID (default: EBAY_US).

    Returns:
        Item aspects.
    """
    endpoint = f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects"
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    params = {"category_id": category_id}
    return make_request(
        method="GET",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        params=params,
        app_token=True
    )


# =============================================================================
# TRANSLATION API
# =============================================================================


@mcp.tool()
def translate(
    text: str,
    from_lang: str,
    to_lang: str,
    translation_context: str = "ITEM_TITLE"
) -> Dict[str, Any]:
    """
    Translate text from one language to another.

    Args:
        text: Text to translate.
        from_lang: Source language code.
        to_lang: Target language code.
        translation_context: Context (ITEM_TITLE or ITEM_DESCRIPTION).

    Returns:
        Translation result with original and translated text.
    """
    endpoint = "/commerce/translation/v1_beta/translate"
    headers = {"Content-Type": "application/json"}
    data = {
        "text": [text],
        "from": from_lang,
        "to": to_lang,
        "translationContext": translation_context
    }
    return make_request(
        method="POST",
        endpoint=endpoint,
        base_url="https://api.sandbox.ebay.com",
        headers=headers,
        data=data,
        app_token=True
    )


if __name__ == "__main__":
    mcp.run()
