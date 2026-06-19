import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools import catalog, charity, identity, media, notification, taxonomy, translation


mcp = FastMCP("ebay-commerce")


def _err(e: Exception) -> Dict[str, Any]:
    return {"error": str(e)}


@mcp.tool()
def ebay_environment() -> Dict[str, Any]:
    """Return configured environment and base URLs."""
    env = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
    standard = "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"
    media_base = "https://apim.sandbox.ebay.com" if env == "SANDBOX" else "https://apim.ebay.com"
    return {"environment": env, "base_url": standard, "media_base_url": media_base}


# Catalog
@mcp.tool()
def catalog_search(q: str, limit: int = 20, offset: int = 0, fieldgroups: Optional[str] = None) -> Dict[str, Any]:
    try:
        return catalog.catalog_search(q=q, limit=limit, offset=offset, fieldgroups=fieldgroups)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_product(product_id: str) -> Dict[str, Any]:
    try:
        return catalog.get_product(product_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_product_summary(product_id: str) -> Dict[str, Any]:
    try:
        return catalog.get_product_summary(product_id)
    except Exception as e:
        return _err(e)


# Charity
@mcp.tool()
def get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    try:
        return charity.get_charity_org(charity_org_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def charity_search(q: Optional[str] = None, registration_ids: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    try:
        return charity.charity_search(q=q, registration_ids=registration_ids, limit=limit, offset=offset)
    except Exception as e:
        return _err(e)


# Identity
@mcp.tool()
def get_user() -> Dict[str, Any]:
    try:
        return identity.get_user()
    except Exception as e:
        return _err(e)


# Media
@mcp.tool()
def create_upload_session(file_name: str, file_size: int, content_type: str) -> Dict[str, Any]:
    try:
        return media.create_upload_session(file_name=file_name, file_size=file_size, content_type=content_type)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_upload_session(upload_session_id: str) -> Dict[str, Any]:
    try:
        return media.get_upload_session(upload_session_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def upload_part(upload_session_id: str, part_sequence: int, data_b64: str) -> Dict[str, Any]:
    try:
        return media.upload_part(upload_session_id=upload_session_id, part_sequence=part_sequence, data_b64=data_b64)
    except Exception as e:
        return _err(e)


@mcp.tool()
def complete_upload_session(upload_session_id: str) -> Dict[str, Any]:
    try:
        return media.complete_upload_session(upload_session_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_asset(asset_id: str) -> Dict[str, Any]:
    try:
        return media.get_asset(asset_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def delete_asset(asset_id: str) -> Dict[str, Any]:
    try:
        return media.delete_asset(asset_id)
    except Exception as e:
        return _err(e)


# Notification
@mcp.tool()
def get_public_key() -> Dict[str, Any]:
    try:
        return notification.get_public_key()
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_subscriptions(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    try:
        return notification.get_subscriptions(limit=limit, offset=offset)
    except Exception as e:
        return _err(e)


@mcp.tool()
def create_subscription(topic_id: str, notification_endpoint: str, payload_version: str = "1.0", filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    try:
        return notification.create_subscription(
            topic_id=topic_id,
            notification_endpoint=notification_endpoint,
            payload_version=payload_version,
            filter=filter,
        )
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    try:
        return notification.get_subscription(subscription_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    try:
        return notification.delete_subscription(subscription_id)
    except Exception as e:
        return _err(e)


# Taxonomy
@mcp.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    try:
        return taxonomy.get_default_category_tree_id(marketplace_id=marketplace_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    try:
        return taxonomy.get_category_tree(category_tree_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    try:
        return taxonomy.get_category_subtree(category_tree_id=category_tree_id, category_id=category_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    try:
        return taxonomy.get_category_suggestions(category_tree_id=category_tree_id, q=q)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    try:
        return taxonomy.get_item_aspects_for_category(category_tree_id=category_tree_id, category_id=category_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    try:
        return taxonomy.get_compatibility_properties(category_tree_id=category_tree_id, category_id=category_id)
    except Exception as e:
        return _err(e)


@mcp.tool()
def get_compatibility_property_values(category_tree_id: str, category_id: str, compatibility_property: str, filter: Optional[str] = None) -> Dict[str, Any]:
    try:
        return taxonomy.get_compatibility_property_values(
            category_tree_id=category_tree_id,
            category_id=category_id,
            compatibility_property=compatibility_property,
            filter=filter,
        )
    except Exception as e:
        return _err(e)


# Translation
@mcp.tool()
def translate(from_language: str, to_language: str, text: str, translation_context: Optional[str] = None) -> Dict[str, Any]:
    try:
        return translation.translate(
            from_language=from_language,
            to_language=to_language,
            text=text,
            translation_context=translation_context,
        )
    except Exception as e:
        return _err(e)


if __name__ == "__main__":
    mcp.run()
