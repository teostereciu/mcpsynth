"""
eBay Commerce API — MCP Server
Runs over stdio using FastMCP.

Namespaces covered:
  - Catalog      (app token)
  - Taxonomy     (app token)
  - Charity      (app token)
  - Translation  (app token)
  - Identity     (user token)
  - Media        (user token, apim.* subdomain)
  - Notification (user token)
"""

from mcp.server.fastmcp import FastMCP

# Domain modules
from generated_tools.catalog import (
    search_catalog_products,
    get_catalog_product,
)
from generated_tools.taxonomy import (
    get_default_category_tree_id,
    get_category_tree,
    get_category_subtree,
    get_category_suggestions,
    get_item_aspects_for_category,
    get_compatibility_properties,
    get_compatibility_property_values,
    get_expired_categories,
)
from generated_tools.charity import (
    get_charity_org,
    search_charity_orgs,
    get_charity_org_by_legacy_id,
)
from generated_tools.translation import translate_text
from generated_tools.identity import get_user
from generated_tools.media import (
    create_video,
    get_video,
    get_videos,
    delete_video,
    create_image,
    get_image,
    create_document,
    get_document,
)
from generated_tools.notification import (
    get_subscriptions,
    get_subscription,
    create_subscription,
    update_subscription,
    delete_subscription,
    enable_subscription,
    disable_subscription,
    get_destinations,
    get_destination,
    create_destination,
    update_destination,
    delete_destination,
    get_topics,
    get_topic,
    get_public_key,
    get_notification_config,
    update_notification_config,
)

# ---------------------------------------------------------------------------
# MCP server instance
# ---------------------------------------------------------------------------

mcp = FastMCP(
    name="ebay-commerce-api",
    description=(
        "Comprehensive MCP server for the eBay Commerce API covering Catalog, "
        "Taxonomy, Charity, Translation, Identity, Media, and Notification namespaces."
    ),
)

# ===========================================================================
# CATALOG tools
# ===========================================================================

@mcp.tool()
def catalog_search_products(
    q: str = "",
    gtin: str = "",
    epid: str = "",
    category_ids: str = "",
    aspect_filter: str = "",
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Search the eBay product catalog by keyword, GTIN, ePID, or category.

    Args:
        q: Free-text search query (keywords).
        gtin: Global Trade Item Number (UPC, EAN, ISBN, etc.).
        epid: eBay Product ID to look up directly.
        category_ids: Comma-separated list of category IDs to restrict results.
        aspect_filter: Aspect name/value filter string, e.g. "Brand:Apple".
        limit: Number of results to return (max 200, default 20).
        offset: Pagination offset (default 0).

    Returns:
        Dict with productSummaries list and pagination info.
    """
    return search_catalog_products(
        q=q or None,
        gtin=gtin or None,
        epid=epid or None,
        category_ids=category_ids or None,
        aspect_filter=aspect_filter or None,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def catalog_get_product(epid: str) -> dict:
    """
    Retrieve full details for a single eBay catalog product by its eBay Product ID (ePID).

    Args:
        epid: The eBay Product ID (e.g. "15032").

    Returns:
        Dict with product title, description, aspects, images, GTINs, etc.
    """
    return get_catalog_product(epid)


# ===========================================================================
# TAXONOMY tools
# ===========================================================================

@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> dict:
    """
    Get the default category tree ID for a given eBay marketplace.

    Args:
        marketplace_id: eBay marketplace identifier (e.g. EBAY_US, EBAY_GB, EBAY_DE).

    Returns:
        Dict with categoryTreeId and categoryTreeVersion.
    """
    return get_default_category_tree_id(marketplace_id)


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the complete category tree for the given tree ID.

    Args:
        category_tree_id: The category tree ID (e.g. "0" for eBay US).

    Returns:
        Dict with the full hierarchical category tree.
    """
    return get_category_tree(category_tree_id)


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve a subtree rooted at the specified category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The root category ID for the subtree.

    Returns:
        Dict with the subtree rooted at category_id.
    """
    return get_category_subtree(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str) -> dict:
    """
    Get category suggestions for a search query string.

    Args:
        category_tree_id: The category tree ID.
        q: Keywords describing the item (e.g. "iphone 14 pro").

    Returns:
        Dict with categorySuggestions list ranked by relevance.
    """
    return get_category_suggestions(category_tree_id, q)


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Get the item aspects (attributes) required or recommended for a category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The leaf category ID.

    Returns:
        Dict with aspects list including names, types, and allowed values.
    """
    return get_item_aspects_for_category(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str) -> dict:
    """
    Get the compatibility properties (e.g. Year, Make, Model) for a parts-compatibility category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID (must support parts compatibility).

    Returns:
        Dict with compatibilityProperties list.
    """
    return get_compatibility_properties(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: str = "",
) -> dict:
    """
    Get the allowed values for a specific compatibility property (e.g. all valid "Make" values).

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID.
        compatibility_property: The property name (e.g. "Make", "Model", "Year").
        filter: Optional filter to narrow values, e.g. "Year:2020,Make:Honda".

    Returns:
        Dict with compatibilityPropertyValues list.
    """
    return get_compatibility_property_values(
        category_tree_id, category_id, compatibility_property, filter or None
    )


@mcp.tool()
def taxonomy_get_expired_categories(category_tree_id: str) -> dict:
    """
    Get a list of categories that have been deprecated/expired in the given tree.

    Args:
        category_tree_id: The category tree ID.

    Returns:
        Dict with expiredCategories list.
    """
    return get_expired_categories(category_tree_id)


# ===========================================================================
# CHARITY tools
# ===========================================================================

@mcp.tool()
def charity_get_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve details for a specific charity organization by its eBay charity ID.

    Args:
        charity_org_id: The eBay charity organization ID.
        marketplace_id: Marketplace context (default EBAY_US).

    Returns:
        Dict with charityOrgId, name, missionStatement, website, logoImage, etc.
    """
    return get_charity_org(charity_org_id, marketplace_id)


@mcp.tool()
def charity_search_orgs(
    q: str = "",
    registration_ids: str = "",
    limit: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Search for charity organizations on eBay.

    Args:
        q: Keywords to search charity names/descriptions.
        registration_ids: Comma-separated charity registration IDs (EIN for US).
        limit: Number of results to return (max 100, default 20).
        offset: Pagination offset (default 0).
        marketplace_id: Marketplace context (default EBAY_US).

    Returns:
        Dict with charityOrgs list and pagination info.
    """
    return search_charity_orgs(
        q=q or None,
        registration_ids=registration_ids or None,
        limit=limit,
        offset=offset,
        x_ebay_c_marketplace_id=marketplace_id,
    )


@mcp.tool()
def charity_get_org_by_legacy_id(legacy_charity_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve a charity organization using a legacy charity ID.

    Args:
        legacy_charity_id: The legacy eBay charity ID.
        marketplace_id: Marketplace context (default EBAY_US).

    Returns:
        Dict with charity organization details.
    """
    return get_charity_org_by_legacy_id(legacy_charity_id, marketplace_id)


# ===========================================================================
# TRANSLATION tools
# ===========================================================================

@mcp.tool()
def translation_translate(
    text: list[str],
    from_language: str,
    to_language: str,
    context: str = "",
    marketplace_id: str = "",
) -> dict:
    """
    Translate one or more text strings using eBay's translation service
    (optimized for eBay listing content).

    Args:
        text: List of text strings to translate (max 5 strings, each max 1000 chars).
        from_language: Source language code (e.g. "en", "de", "fr", "zh_Hant").
        to_language: Target language code (e.g. "en", "de", "fr", "zh_Hant").
        context: Translation context hint — ITEM_TITLE, ITEM_DESCRIPTION, or ITEM_ASPECT.
        marketplace_id: Optional eBay marketplace ID for context (e.g. EBAY_US).

    Returns:
        Dict with translations list, each containing translatedText.
    """
    return translate_text(
        text=text,
        from_language=from_language,
        to_language=to_language,
        context=context or None,
        marketplace_id=marketplace_id or None,
    )


# ===========================================================================
# IDENTITY tools
# ===========================================================================

@mcp.tool()
def identity_get_user() -> dict:
    """
    Retrieve the authenticated eBay user's account information.

    Returns:
        Dict with userId, username, accountType, address, contact info, etc.
    """
    return get_user()


# ===========================================================================
# MEDIA tools
# ===========================================================================

@mcp.tool()
def media_create_video(
    title: str,
    size: int,
    classification: list[str] | None = None,
    description: str = "",
) -> dict:
    """
    Create a new video resource on eBay (first step before uploading the video file).

    Args:
        title: Title of the video (max 80 chars).
        size: File size in bytes of the video to be uploaded.
        classification: List of classification strings, e.g. ["ITEM_DESCRIPTION"].
        description: Optional description of the video.

    Returns:
        Dict with videoId and upload URL/instructions.
    """
    return create_video(
        title=title,
        size=size,
        classification=classification,
        description=description or None,
    )


@mcp.tool()
def media_get_video(video_id: str) -> dict:
    """
    Retrieve metadata and status for a video by its ID.

    Args:
        video_id: The eBay video ID returned from media_create_video.

    Returns:
        Dict with videoId, title, status, playList (streaming URLs), thumbnail, etc.
    """
    return get_video(video_id)


@mcp.tool()
def media_list_videos(q: str = "", limit: int = 20, offset: int = 0) -> dict:
    """
    List videos owned by the authenticated user.

    Args:
        q: Optional keyword filter on video title.
        limit: Number of results (max 100, default 20).
        offset: Pagination offset (default 0).

    Returns:
        Dict with videos list and pagination info.
    """
    return get_videos(q=q or None, limit=limit, offset=offset)


@mcp.tool()
def media_delete_video(video_id: str) -> dict:
    """
    Delete a video resource.

    Args:
        video_id: The eBay video ID to delete.

    Returns:
        Dict confirming deletion or error details.
    """
    return delete_video(video_id)


@mcp.tool()
def media_create_image(image_url: str, image_type: str = "JPEG") -> dict:
    """
    Upload an image to eBay by providing a publicly accessible URL.

    Args:
        image_url: Publicly accessible URL of the image to upload.
        image_type: Image format — JPEG, PNG, GIF, TIFF, BMP, WEBP (default JPEG).

    Returns:
        Dict with imageId and status.
    """
    return create_image(image_url=image_url, image_type=image_type)


@mcp.tool()
def media_get_image(image_id: str) -> dict:
    """
    Retrieve metadata for an uploaded image.

    Args:
        image_id: The eBay image ID.

    Returns:
        Dict with imageId, imageUrl, status, etc.
    """
    return get_image(image_id)


@mcp.tool()
def media_create_document(
    document_type: str,
    languages: list[str],
    files: list[dict] | None = None,
) -> dict:
    """
    Create a document resource (e.g. regulatory compliance document).

    Args:
        document_type: Type of document, e.g. "REGULATORY_DOCUMENT".
        languages: List of language codes, e.g. ["en_US"].
        files: Optional list of file metadata dicts with keys: fileName, fileType, fileSize.

    Returns:
        Dict with documentId and upload instructions.
    """
    return create_document(document_type=document_type, languages=languages, files=files)


@mcp.tool()
def media_get_document(document_id: str) -> dict:
    """
    Retrieve metadata for a document resource.

    Args:
        document_id: The eBay document ID.

    Returns:
        Dict with documentId, documentType, status, files, etc.
    """
    return get_document(document_id)


# ===========================================================================
# NOTIFICATION tools
# ===========================================================================

@mcp.tool()
def notification_list_subscriptions(limit: int = 20, continuation_token: str = "") -> dict:
    """
    List all notification subscriptions for the authenticated user.

    Args:
        limit: Number of subscriptions to return (max 100, default 20).
        continuation_token: Token for paginating through results.

    Returns:
        Dict with subscriptions list and pagination info.
    """
    return get_subscriptions(limit=limit, continuation_token=continuation_token or None)


@mcp.tool()
def notification_get_subscription(subscription_id: str) -> dict:
    """
    Retrieve details for a specific notification subscription.

    Args:
        subscription_id: The subscription ID.

    Returns:
        Dict with subscriptionId, topicId, status, destination, etc.
    """
    return get_subscription(subscription_id)


@mcp.tool()
def notification_create_subscription(
    topic_id: str,
    destination_id: str,
    status: str = "ENABLED",
    payload: dict | None = None,
) -> dict:
    """
    Create a new notification subscription for a topic.

    Args:
        topic_id: The notification topic to subscribe to (e.g. "MARKETPLACE_ACCOUNT_DELETION").
        destination_id: The destination endpoint ID to receive notifications.
        status: Subscription status — ENABLED or DISABLED (default ENABLED).
        payload: Optional payload configuration dict.

    Returns:
        Dict with the created subscription details including subscriptionId.
    """
    return create_subscription(
        topic_id=topic_id,
        destination_id=destination_id,
        status=status,
        payload=payload,
    )


@mcp.tool()
def notification_update_subscription(
    subscription_id: str,
    status: str = "",
    destination_id: str = "",
    payload: dict | None = None,
) -> dict:
    """
    Update an existing notification subscription.

    Args:
        subscription_id: The subscription ID to update.
        status: New status — ENABLED or DISABLED.
        destination_id: New destination endpoint ID.
        payload: Updated payload configuration dict.

    Returns:
        Dict with updated subscription details.
    """
    return update_subscription(
        subscription_id=subscription_id,
        status=status or None,
        destination_id=destination_id or None,
        payload=payload,
    )


@mcp.tool()
def notification_delete_subscription(subscription_id: str) -> dict:
    """
    Delete a notification subscription.

    Args:
        subscription_id: The subscription ID to delete.

    Returns:
        Dict confirming deletion or error details.
    """
    return delete_subscription(subscription_id)


@mcp.tool()
def notification_enable_subscription(subscription_id: str) -> dict:
    """
    Enable a previously disabled notification subscription.

    Args:
        subscription_id: The subscription ID to enable.

    Returns:
        Dict with updated subscription status.
    """
    return enable_subscription(subscription_id)


@mcp.tool()
def notification_disable_subscription(subscription_id: str) -> dict:
    """
    Disable an active notification subscription without deleting it.

    Args:
        subscription_id: The subscription ID to disable.

    Returns:
        Dict with updated subscription status.
    """
    return disable_subscription(subscription_id)


@mcp.tool()
def notification_list_destinations(limit: int = 20, continuation_token: str = "") -> dict:
    """
    List all notification destinations (webhook endpoints) for the authenticated user.

    Args:
        limit: Number of destinations to return (max 100, default 20).
        continuation_token: Token for paginating through results.

    Returns:
        Dict with destinations list and pagination info.
    """
    return get_destinations(limit=limit, continuation_token=continuation_token or None)


@mcp.tool()
def notification_get_destination(destination_id: str) -> dict:
    """
    Retrieve details for a specific notification destination.

    Args:
        destination_id: The destination ID.

    Returns:
        Dict with destinationId, name, status, deliveryConfig (endpoint URL), etc.
    """
    return get_destination(destination_id)


@mcp.tool()
def notification_create_destination(
    name: str,
    endpoint_url: str,
    verification_token: str = "",
    alert_email: str = "",
) -> dict:
    """
    Create a new notification destination (webhook endpoint).

    Args:
        name: Human-readable name for this destination.
        endpoint_url: HTTPS URL that will receive notification POST requests.
        verification_token: Optional token eBay will include in verification challenges.
        alert_email: Optional email address for delivery failure alerts.

    Returns:
        Dict with the created destination including destinationId.
    """
    return create_destination(
        name=name,
        endpoint_url=endpoint_url,
        verification_token=verification_token or None,
        alert_email=alert_email or None,
    )


@mcp.tool()
def notification_update_destination(
    destination_id: str,
    name: str = "",
    endpoint_url: str = "",
    verification_token: str = "",
    alert_email: str = "",
) -> dict:
    """
    Update an existing notification destination.

    Args:
        destination_id: The destination ID to update.
        name: New human-readable name.
        endpoint_url: New HTTPS webhook URL.
        verification_token: New verification token.
        alert_email: New alert email address.

    Returns:
        Dict with updated destination details.
    """
    return update_destination(
        destination_id=destination_id,
        name=name or None,
        endpoint_url=endpoint_url or None,
        verification_token=verification_token or None,
        alert_email=alert_email or None,
    )


@mcp.tool()
def notification_delete_destination(destination_id: str) -> dict:
    """
    Delete a notification destination.

    Args:
        destination_id: The destination ID to delete.

    Returns:
        Dict confirming deletion or error details.
    """
    return delete_destination(destination_id)


@mcp.tool()
def notification_list_topics(limit: int = 20, continuation_token: str = "") -> dict:
    """
    List all available notification topics.

    Args:
        limit: Number of topics to return (max 100, default 20).
        continuation_token: Token for paginating through results.

    Returns:
        Dict with topics list including topicId, description, status, etc.
    """
    return get_topics(limit=limit, continuation_token=continuation_token or None)


@mcp.tool()
def notification_get_topic(topic_id: str) -> dict:
    """
    Retrieve details for a specific notification topic.

    Args:
        topic_id: The topic ID (e.g. "MARKETPLACE_ACCOUNT_DELETION").

    Returns:
        Dict with topicId, description, status, supportedPayloadVersion, etc.
    """
    return get_topic(topic_id)


@mcp.tool()
def notification_get_public_key(public_key_id: str) -> dict:
    """
    Retrieve the eBay public key used to verify notification signatures.

    Args:
        public_key_id: The public key ID included in notification headers.

    Returns:
        Dict with publicKeyId, key (PEM), algorithm, digest, etc.
    """
    return get_public_key(public_key_id)


@mcp.tool()
def notification_get_config() -> dict:
    """
    Retrieve the notification configuration for the authenticated application.

    Returns:
        Dict with alertEmail and other application-level notification settings.
    """
    return get_notification_config()


@mcp.tool()
def notification_update_config(alert_email: str) -> dict:
    """
    Update the application-level notification configuration.

    Args:
        alert_email: Email address for notification delivery failure alerts.

    Returns:
        Dict with updated config or confirmation.
    """
    return update_notification_config(alert_email)


# ===========================================================================
# Entry point
# ===========================================================================

if __name__ == "__main__":
    mcp.run(transport="stdio")
