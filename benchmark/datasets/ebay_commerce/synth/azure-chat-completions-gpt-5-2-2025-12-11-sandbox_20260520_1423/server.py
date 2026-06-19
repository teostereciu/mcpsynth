import os
import json
import base64
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

APP_NAME = "ebay-commerce-mcp"

mcp = FastMCP(APP_NAME)


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def _base_url() -> str:
    # Docs show both api.ebay.com and apim.ebay.com depending on API.
    # Use apim by default; allow override.
    return _env("EBAY_API_BASE_URL", "https://apim.ebay.com").rstrip("/")


def _access_token() -> str:
    token = _env("EBAY_OAUTH_TOKEN")
    if not token:
        raise ValueError(
            "Missing EBAY_OAUTH_TOKEN. Provide an OAuth access token (Authorization: Bearer ...)."
        )
    return token


def _default_headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {
        "Authorization": f"Bearer {_access_token()}",
        "Accept": "application/json",
    }
    if extra:
        headers.update({k: v for k, v in extra.items() if v is not None})
    return headers


async def _request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Any = None,
    headers: Optional[Dict[str, str]] = None,
    files: Any = None,
    data: Any = None,
    timeout: float = 60.0,
) -> Dict[str, Any]:
    url = f"{_base_url()}{path}"
    async with httpx.AsyncClient(timeout=timeout) as client:
        resp = await client.request(
            method,
            url,
            params=params,
            json=json_body,
            headers=_default_headers(headers),
            files=files,
            data=data,
        )

    content_type = resp.headers.get("content-type", "")
    out: Dict[str, Any] = {
        "status_code": resp.status_code,
        "headers": {k: v for k, v in resp.headers.items()},
        "url": str(resp.request.url),
    }

    if "application/json" in content_type:
        try:
            out["json"] = resp.json()
        except Exception:
            out["text"] = resp.text
    else:
        out["text"] = resp.text

    if resp.is_error:
        # Keep payload for debugging; raise a structured error.
        raise RuntimeError(json.dumps(out, ensure_ascii=False)[:20000])

    return out


# -------------------- Catalog API --------------------

@mcp.tool()
async def catalog_search_product_summaries(
    q: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    x_ebay_c_marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Search for product summaries.

    Docs: commerce/catalog/resources/product_summary/methods/search
    GET /commerce/catalog/v1_beta/product_summary/search

    Parameters map to query params used by eBay.
    """
    params: Dict[str, Any] = {"q": q}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if category_ids is not None:
        params["category_ids"] = category_ids
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if filter is not None:
        params["filter"] = filter
    if sort is not None:
        params["sort"] = sort

    headers = {}
    if x_ebay_c_marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = x_ebay_c_marketplace_id

    return await _request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        params=params,
        headers=headers,
    )


@mcp.tool()
async def catalog_get_product(
    ep_id: str,
    x_ebay_c_marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Get product details by ePID.

    Docs: commerce/catalog/resources/product/methods/getProduct
    GET /commerce/catalog/v1_beta/product/{ep_id}
    """
    headers = {}
    if x_ebay_c_marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = x_ebay_c_marketplace_id

    return await _request(
        "GET",
        f"/commerce/catalog/v1_beta/product/{ep_id}",
        headers=headers,
    )


# -------------------- Charity API --------------------

@mcp.tool()
async def charity_get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    """Retrieve a charitable organization by ID.

    Docs: commerce/charity/resources/charity_org/methods/getCharityOrg
    GET /commerce/charity/v1/charity_org/{charity_org_id}
    """
    return await _request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
    )


@mcp.tool()
async def charity_search_charity_orgs(
    q: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Search for charitable organizations.

    Docs: commerce/charity/resources/charity_org/methods/getCharityOrgs
    GET /commerce/charity/v1/charity_org
    """
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    return await _request(
        "GET",
        "/commerce/charity/v1/charity_org",
        params=params or None,
    )


# -------------------- Identity API --------------------

@mcp.tool()
async def identity_get_user(username: str) -> Dict[str, Any]:
    """Retrieve public information about an eBay user.

    Docs: commerce/identity/resources/user/methods/getUser
    GET /commerce/identity/v1/user/{username}
    """
    return await _request(
        "GET",
        f"/commerce/identity/v1/user/{username}",
    )


# -------------------- Media API (v1_beta) --------------------

@mcp.tool()
async def media_create_image_from_url(image_url: str) -> Dict[str, Any]:
    """Upload an image to EPS from an HTTPS URL.

    Docs: commerce/media/resources/image/methods/createImageFromUrl
    POST /commerce/media/v1_beta/image/create_image_from_url
    """
    return await _request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        json_body={"imageUrl": image_url},
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def media_create_image_from_file(
    file_path: Optional[str] = None,
    file_b64: Optional[str] = None,
    filename: Optional[str] = None,
) -> Dict[str, Any]:
    """Upload an image to EPS using multipart/form-data.

    Docs: commerce/media/resources/image/methods/createImageFromFile
    POST /commerce/media/v1_beta/image/create_image_from_file

    Provide either file_path or file_b64 (base64-encoded bytes). If file_b64 is used,
    filename is required.
    """
    if not file_path and not file_b64:
        raise ValueError("Provide either file_path or file_b64")

    if file_path:
        fn = filename or os.path.basename(file_path)
        with open(file_path, "rb") as f:
            content = f.read()
    else:
        if not filename:
            raise ValueError("filename is required when using file_b64")
        fn = filename
        content = base64.b64decode(file_b64)

    files = {"image": (fn, content)}
    # httpx sets multipart boundary and content-type automatically.
    return await _request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_file",
        files=files,
    )


@mcp.tool()
async def media_get_image(image_id: str) -> Dict[str, Any]:
    """Get EPS image details.

    Docs: commerce/media/resources/image/methods/getImage
    GET /commerce/media/v1_beta/image/{image_id}
    """
    return await _request(
        "GET",
        f"/commerce/media/v1_beta/image/{image_id}",
    )


@mcp.tool()
async def media_create_document(document_type: str, languages: list[str]) -> Dict[str, Any]:
    """Stage a document and return a documentId.

    Docs: commerce/media/resources/document/methods/createDocument
    POST /commerce/media/v1_beta/document
    """
    return await _request(
        "POST",
        "/commerce/media/v1_beta/document",
        json_body={"documentType": document_type, "languages": languages},
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def media_create_document_from_url(
    document_type: str, languages: list[str], document_url: str
) -> Dict[str, Any]:
    """Download a document from URL and add it to the account.

    Docs: commerce/media/resources/document/methods/createDocumentFromUrl
    POST /commerce/media/v1_beta/document/create_document_from_url
    """
    return await _request(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        json_body={
            "documentType": document_type,
            "languages": languages,
            "documentUrl": document_url,
        },
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def media_upload_document(
    document_id: str,
    file_path: Optional[str] = None,
    file_b64: Optional[str] = None,
    filename: Optional[str] = None,
) -> Dict[str, Any]:
    """Upload a document file using multipart/form-data.

    Docs: commerce/media/resources/document/methods/uploadDocument
    POST /commerce/media/v1_beta/document/{document_id}/upload

    Provide either file_path or file_b64 (base64-encoded bytes). If file_b64 is used,
    filename is required.
    """
    if not file_path and not file_b64:
        raise ValueError("Provide either file_path or file_b64")

    if file_path:
        fn = filename or os.path.basename(file_path)
        with open(file_path, "rb") as f:
            content = f.read()
    else:
        if not filename:
            raise ValueError("filename is required when using file_b64")
        fn = filename
        content = base64.b64decode(file_b64)

    files = {"file": (fn, content)}
    return await _request(
        "POST",
        f"/commerce/media/v1_beta/document/{document_id}/upload",
        files=files,
    )


@mcp.tool()
async def media_get_document(document_id: str) -> Dict[str, Any]:
    """Get document status and metadata.

    Docs: commerce/media/resources/document/methods/getDocument
    GET /commerce/media/v1_beta/document/{document_id}
    """
    return await _request(
        "GET",
        f"/commerce/media/v1_beta/document/{document_id}",
    )


@mcp.tool()
async def media_create_video(title: str, size: int, classification: str = "ITEM", description: Optional[str] = None) -> Dict[str, Any]:
    """Create a video resource (metadata) prior to upload.

    Docs: commerce/media/resources/video/methods/createVideo
    POST /commerce/media/v1_beta/video

    classification currently supports ITEM.
    """
    body: Dict[str, Any] = {
        "title": title,
        "size": size,
        "classification": [classification],
    }
    if description is not None:
        body["description"] = description

    return await _request(
        "POST",
        "/commerce/media/v1_beta/video",
        json_body=body,
        headers={"Content-Type": "application/json"},
        timeout=120.0,
    )


@mcp.tool()
async def media_upload_video(
    video_id: str,
    file_path: Optional[str] = None,
    file_b64: Optional[str] = None,
    filename: Optional[str] = None,
) -> Dict[str, Any]:
    """Upload video content using multipart/form-data.

    Docs: commerce/media/resources/video/methods/uploadVideo
    POST /commerce/media/v1_beta/video/{video_id}/upload

    Provide either file_path or file_b64 (base64-encoded bytes). If file_b64 is used,
    filename is required.
    """
    if not file_path and not file_b64:
        raise ValueError("Provide either file_path or file_b64")

    if file_path:
        fn = filename or os.path.basename(file_path)
        with open(file_path, "rb") as f:
            content = f.read()
    else:
        if not filename:
            raise ValueError("filename is required when using file_b64")
        fn = filename
        content = base64.b64decode(file_b64)

    files = {"file": (fn, content)}
    return await _request(
        "POST",
        f"/commerce/media/v1_beta/video/{video_id}/upload",
        files=files,
        timeout=300.0,
    )


@mcp.tool()
async def media_get_video(video_id: str) -> Dict[str, Any]:
    """Get video metadata and playlist.

    Docs: commerce/media/resources/video/methods/getVideo
    GET /commerce/media/v1_beta/video/{video_id}
    """
    return await _request(
        "GET",
        f"/commerce/media/v1_beta/video/{video_id}",
        timeout=120.0,
    )


# -------------------- Notification API --------------------

@mcp.tool()
async def notification_get_public_key() -> Dict[str, Any]:
    """Retrieve the public key used to validate notification messages.

    Docs: commerce/notification/resources/public_key/methods/getPublicKey
    GET /commerce/notification/v1/public_key
    """
    return await _request("GET", "/commerce/notification/v1/public_key")


@mcp.tool()
async def notification_get_config() -> Dict[str, Any]:
    """Retrieve notification configuration.

    Docs: commerce/notification/resources/config/methods/getConfig
    GET /commerce/notification/v1/config
    """
    return await _request("GET", "/commerce/notification/v1/config")


@mcp.tool()
async def notification_update_config(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create or update notification configuration.

    Docs: commerce/notification/resources/config/methods/updateConfig
    PUT /commerce/notification/v1/config

    Pass the request body as `payload`.
    """
    return await _request(
        "PUT",
        "/commerce/notification/v1/config",
        json_body=payload,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def notification_get_topics(limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """Get available notification topics.

    Docs: commerce/notification/resources/topic/methods/getTopics
    GET /commerce/notification/v1/topic
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return await _request("GET", "/commerce/notification/v1/topic", params=params or None)


@mcp.tool()
async def notification_get_topic(topic_id: str) -> Dict[str, Any]:
    """Get a notification topic by ID.

    Docs: commerce/notification/resources/topic/methods/getTopic
    GET /commerce/notification/v1/topic/{topic_id}
    """
    return await _request("GET", f"/commerce/notification/v1/topic/{topic_id}")


@mcp.tool()
async def notification_get_destinations(limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """List destinations.

    Docs: commerce/notification/resources/destination/methods/getDestinations
    GET /commerce/notification/v1/destination
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return await _request(
        "GET",
        "/commerce/notification/v1/destination",
        params=params or None,
    )


@mcp.tool()
async def notification_create_destination(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create a destination.

    Docs: commerce/notification/resources/destination/methods/createDestination
    POST /commerce/notification/v1/destination

    Pass the request body as `payload`.
    """
    return await _request(
        "POST",
        "/commerce/notification/v1/destination",
        json_body=payload,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def notification_update_destination(destination_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Update a destination.

    Docs: commerce/notification/resources/destination/methods/updateDestination
    PUT /commerce/notification/v1/destination/{destination_id}
    """
    return await _request(
        "PUT",
        f"/commerce/notification/v1/destination/{destination_id}",
        json_body=payload,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def notification_delete_destination(destination_id: str) -> Dict[str, Any]:
    """Delete a destination.

    Docs: commerce/notification/resources/destination/methods/deleteDestination
    DELETE /commerce/notification/v1/destination/{destination_id}
    """
    return await _request(
        "DELETE",
        f"/commerce/notification/v1/destination/{destination_id}",
    )


@mcp.tool()
async def notification_get_subscriptions(limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """List subscriptions.

    Docs: commerce/notification/resources/subscription/methods/getSubscriptions
    GET /commerce/notification/v1/subscription
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return await _request(
        "GET",
        "/commerce/notification/v1/subscription",
        params=params or None,
    )


@mcp.tool()
async def notification_get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Get a subscription.

    Docs: commerce/notification/resources/subscription/methods/getSubscription
    GET /commerce/notification/v1/subscription/{subscription_id}
    """
    return await _request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}",
    )


@mcp.tool()
async def notification_create_subscription(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create a subscription.

    Docs: commerce/notification/resources/subscription/methods/createSubscription
    POST /commerce/notification/v1/subscription
    """
    return await _request(
        "POST",
        "/commerce/notification/v1/subscription",
        json_body=payload,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def notification_update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Update a subscription.

    Docs: commerce/notification/resources/subscription/methods/updateSubscription
    PUT /commerce/notification/v1/subscription/{subscription_id}
    """
    return await _request(
        "PUT",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        json_body=payload,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def notification_delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """Delete a subscription.

    Docs: commerce/notification/resources/subscription/methods/deleteSubscription
    DELETE /commerce/notification/v1/subscription/{subscription_id}
    """
    return await _request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}",
    )


@mcp.tool()
async def notification_enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Enable a subscription.

    Docs: commerce/notification/resources/subscription/methods/enableSubscription
    POST /commerce/notification/v1/subscription/{subscription_id}/enable
    """
    return await _request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/enable",
    )


@mcp.tool()
async def notification_disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Disable a subscription.

    Docs: commerce/notification/resources/subscription/methods/disableSubscription
    POST /commerce/notification/v1/subscription/{subscription_id}/disable
    """
    return await _request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/disable",
    )


@mcp.tool()
async def notification_test_subscription(subscription_id: str) -> Dict[str, Any]:
    """Test a subscription.

    Docs: commerce/notification/resources/subscription/methods/testSubscription
    POST /commerce/notification/v1/subscription/{subscription_id}/test
    """
    return await _request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/test",
    )


@mcp.tool()
async def notification_test(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Send a test notification.

    Docs: commerce/notification/resources/subscription/methods/test
    POST /commerce/notification/v1/subscription/test

    Pass the request body as `payload`.
    """
    return await _request(
        "POST",
        "/commerce/notification/v1/subscription/test",
        json_body=payload,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def notification_create_subscription_filter(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create a subscription filter.

    Docs: commerce/notification/resources/subscription/methods/createSubscriptionFilter
    POST /commerce/notification/v1/subscription/{subscription_id}/filter
    """
    return await _request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        json_body=payload,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
async def notification_get_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    """Get a subscription filter.

    Docs: commerce/notification/resources/subscription/methods/getSubscriptionFilter
    GET /commerce/notification/v1/subscription/{subscription_id}/filter
    """
    return await _request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
    )


@mcp.tool()
async def notification_delete_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    """Delete a subscription filter.

    Docs: commerce/notification/resources/subscription/methods/deleteSubscriptionFilter
    DELETE /commerce/notification/v1/subscription/{subscription_id}/filter
    """
    return await _request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
    )


# -------------------- Taxonomy API --------------------

@mcp.tool()
async def taxonomy_get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace.

    Docs: commerce/taxonomy/resources/category_tree/methods/getDefaultCategoryTreeId
    GET /commerce/taxonomy/v1/get_default_category_tree_id?marketplace_id=...
    """
    return await _request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
async def taxonomy_get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """Get a complete category tree.

    Docs: commerce/taxonomy/resources/category_tree/methods/getCategoryTree
    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}
    """
    return await _request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
    )


@mcp.tool()
async def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a subtree of the category tree.

    Docs: commerce/taxonomy/resources/category_tree/methods/getCategorySubtree
    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree?category_id=...
    """
    return await _request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
    )


@mcp.tool()
async def taxonomy_get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """Get category suggestions for a query string.

    Docs: commerce/taxonomy/resources/category_tree/methods/getCategorySuggestions
    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions?q=...
    """
    return await _request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
    )


@mcp.tool()
async def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get item aspects for a category.

    Docs: commerce/taxonomy/resources/category_tree/methods/getItemAspectsForCategory
    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category?category_id=...
    """
    return await _request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
    )


@mcp.tool()
async def taxonomy_fetch_item_aspects(category_tree_id: str, category_ids: str) -> Dict[str, Any]:
    """Fetch item aspects for multiple categories.

    Docs: commerce/taxonomy/resources/category_tree/methods/fetchItemAspects
    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects?category_ids=...
    """
    return await _request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        params={"category_ids": category_ids},
    )


@mcp.tool()
async def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get compatibility properties for a category.

    Docs: commerce/taxonomy/resources/category_tree/methods/getCompatibilityProperties
    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties?category_id=...
    """
    return await _request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
    )


@mcp.tool()
async def taxonomy_get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
) -> Dict[str, Any]:
    """Get compatibility property values.

    Docs: commerce/taxonomy/resources/category_tree/methods/getCompatibilityPropertyValues
    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values
    """
    return await _request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params={
            "category_id": category_id,
            "compatibility_property": compatibility_property,
        },
    )


@mcp.tool()
async def taxonomy_get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    """Get expired categories for a category tree.

    Docs: commerce/taxonomy/resources/category_tree/methods/getExpiredCategories
    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories
    """
    return await _request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
    )


# -------------------- Translation API (v1_beta) --------------------

@mcp.tool()
async def translation_translate(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Translate text.

    Docs: commerce/translation/resources/language/methods/translate
    POST /commerce/translation/v1_beta/translate

    Pass the request body as `payload`.
    """
    return await _request(
        "POST",
        "/commerce/translation/v1_beta/translate",
        json_body=payload,
        headers={"Content-Type": "application/json"},
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
