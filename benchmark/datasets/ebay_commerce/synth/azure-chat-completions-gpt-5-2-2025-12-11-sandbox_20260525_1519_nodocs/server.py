import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from ebay_client import EbayClient


mcp = FastMCP("ebay-commerce")
client = EbayClient()


def _ok(x: Any) -> Any:
    return x


# ---- Taxonomy (app token) ----
@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace."""
    return _ok(client.get_default_category_tree_id(marketplace_id=marketplace_id))


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """Get a full category tree."""
    return _ok(client.get_category_tree(category_tree_id=category_tree_id))


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a subtree of a category tree rooted at category_id."""
    return _ok(client.get_category_subtree(category_tree_id=category_tree_id, category_id=category_id))


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """Get category suggestions for a query string."""
    return _ok(client.get_category_suggestions(category_tree_id=category_tree_id, q=q))


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get required/recommended item aspects for a category."""
    return _ok(client.get_item_aspects_for_category(category_tree_id=category_tree_id, category_id=category_id))


@mcp.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get compatibility properties for a category."""
    return _ok(client.get_compatibility_properties(category_tree_id=category_tree_id, category_id=category_id))


@mcp.tool()
def taxonomy_get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """Get compatibility property values for a category."""
    return _ok(
        client.get_compatibility_property_values(
            category_tree_id=category_tree_id,
            category_id=category_id,
            compatibility_property=compatibility_property,
            filter=filter,
        )
    )


# ---- Catalog (app token) ----
@mcp.tool()
def catalog_get_product(epid: str) -> Dict[str, Any]:
    """Get a product by ePID."""
    return _ok(client.get_product(epid=epid))


@mcp.tool()
def catalog_get_product_by_gtin(gtin: str) -> Dict[str, Any]:
    """Get a product by GTIN."""
    return _ok(client.get_product_by_gtin(gtin=gtin))


@mcp.tool()
def catalog_search_products(q: str, limit: int = 20, offset: int = 0, category_ids: Optional[str] = None) -> Dict[str, Any]:
    """Search product summaries."""
    return _ok(client.search_products(q=q, limit=limit, offset=offset, category_ids=category_ids))


# ---- Identity (user token) ----
@mcp.tool()
def identity_get_user() -> Dict[str, Any]:
    """Get the authenticated user's identity."""
    return _ok(client.get_user())


# ---- Notification (user token) ----
@mcp.tool()
def notification_get_public_key(public_key_id: str) -> Dict[str, Any]:
    """Get a notification public key."""
    return _ok(client.get_public_key(public_key_id=public_key_id))


@mcp.tool()
def notification_get_public_keys(limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """List notification public keys."""
    return _ok(client.get_public_keys(limit=limit, offset=offset))


@mcp.tool()
def notification_create_subscription(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create a notification subscription."""
    return _ok(client.create_subscription(payload=payload))


@mcp.tool()
def notification_get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Get a notification subscription."""
    return _ok(client.get_subscription(subscription_id=subscription_id))


@mcp.tool()
def notification_get_subscriptions(limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """List notification subscriptions."""
    return _ok(client.get_subscriptions(limit=limit, offset=offset))


@mcp.tool()
def notification_update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Update a notification subscription."""
    return _ok(client.update_subscription(subscription_id=subscription_id, payload=payload))


@mcp.tool()
def notification_delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """Delete a notification subscription."""
    return _ok(client.delete_subscription(subscription_id=subscription_id))


# ---- Media (user token; apim.* base) ----
@mcp.tool()
def media_create_upload_job(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create a media upload job."""
    return _ok(client.create_upload_job(payload=payload))


@mcp.tool()
def media_get_upload_job(upload_job_id: str) -> Dict[str, Any]:
    """Get a media upload job."""
    return _ok(client.get_upload_job(upload_job_id=upload_job_id))


@mcp.tool()
def media_upload_file_part(
    upload_job_id: str,
    part_sequence: int,
    content_base64: str,
    content_type: str = "application/octet-stream",
) -> Dict[str, Any]:
    """Upload a part for an upload job. content_base64 must be base64-encoded bytes."""
    return _ok(
        client.upload_file_part(
            upload_job_id=upload_job_id,
            part_sequence=part_sequence,
            content=content_base64,
            content_type=content_type,
        )
    )


@mcp.tool()
def media_complete_upload_job(upload_job_id: str) -> Dict[str, Any]:
    """Complete a media upload job."""
    return _ok(client.complete_upload_job(upload_job_id=upload_job_id))


# ---- Charity (app token) ----
@mcp.tool()
def charity_get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    """Get a charity organization."""
    return _ok(client.get_charity_org(charity_org_id=charity_org_id))


@mcp.tool()
def charity_get_charity_orgs(limit: int = 20, offset: int = 0, q: Optional[str] = None) -> Dict[str, Any]:
    """Search/list charity organizations."""
    return _ok(client.get_charity_orgs(limit=limit, offset=offset, q=q))


# ---- Translation (app token) ----
@mcp.tool()
def translation_translate(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Translate text using the Translation API."""
    return _ok(client.translate(payload=payload))


if __name__ == "__main__":
    # FastMCP runs over stdio by default.
    # Ensure env vars are present early for clearer errors.
    os.getenv("EBAY_APP_ID")
    os.getenv("EBAY_CERT_ID")
    mcp.run()
