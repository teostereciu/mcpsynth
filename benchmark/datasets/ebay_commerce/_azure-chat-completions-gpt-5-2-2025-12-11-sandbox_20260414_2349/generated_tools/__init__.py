from __future__ import annotations

from fastmcp import FastMCP

from . import catalog, charity, identity, media, notification, taxonomy, translation

mcp = FastMCP("ebay-commerce")


# Taxonomy
@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str):
    return taxonomy.get_default_category_tree_id(marketplace_id)


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str):
    return taxonomy.get_category_tree(category_tree_id)


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str):
    return taxonomy.get_category_subtree(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str):
    return taxonomy.get_category_suggestions(category_tree_id, q)


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str):
    return taxonomy.get_item_aspects_for_category(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str):
    return taxonomy.get_compatibility_properties(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: str | None = None,
):
    return taxonomy.get_compatibility_property_values(
        category_tree_id, category_id, compatibility_property, filter=filter
    )


@mcp.tool()
def taxonomy_get_expired_categories(category_tree_id: str):
    return taxonomy.get_expired_categories(category_tree_id)


# Charity
@mcp.tool()
def charity_search_charity_orgs(
    q: str | None = None,
    registration_ids: str | None = None,
    limit: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
):
    return charity.search_charity_orgs(
        marketplace_id=marketplace_id,
        q=q,
        registration_ids=registration_ids,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def charity_get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US"):
    return charity.get_charity_org(charity_org_id, marketplace_id=marketplace_id)


# Media
@mcp.tool()
def media_create_image_from_url(image_url: str):
    return media.create_image_from_url(image_url)


@mcp.tool()
def media_get_image(image_id: str):
    return media.get_image(image_id)


@mcp.tool()
def media_create_document_from_url(document_url: str):
    return media.create_document_from_url(document_url)


@mcp.tool()
def media_get_document(document_id: str):
    return media.get_document(document_id)


@mcp.tool()
def media_get_video(video_id: str):
    return media.get_video(video_id)


# Translation
@mcp.tool()
def translation_translate_text(text: str, from_language: str, to_language: str, translation_context: str):
    return translation.translate_text(text, from_language, to_language, translation_context)


# Catalog
@mcp.tool()
def catalog_search_product_summaries(
    q: str | None = None,
    gtin: str | None = None,
    mpn: str | None = None,
    category_ids: str | None = None,
    aspect_filter: str | None = None,
    fieldgroups: str | None = None,
    limit: int = 50,
    offset: int | None = None,
    marketplace_id: str | None = None,
    user_auth: bool = False,
):
    return catalog.search_product_summaries(
        q=q,
        gtin=gtin,
        mpn=mpn,
        category_ids=category_ids,
        aspect_filter=aspect_filter,
        fieldgroups=fieldgroups,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id,
        user_auth=user_auth,
    )


@mcp.tool()
def catalog_get_product(epid: str, user_auth: bool = False):
    return catalog.get_product(epid, user_auth=user_auth)


# Identity
@mcp.tool()
def identity_get_user():
    return identity.get_user()


# Notification
@mcp.tool()
def notification_get_config():
    return notification.get_config()


@mcp.tool()
def notification_update_config(payload: dict):
    return notification.update_config(payload)


@mcp.tool()
def notification_get_destinations(limit: int = 20, continuation_token: str | None = None):
    return notification.get_destinations(limit=limit, continuation_token=continuation_token)


@mcp.tool()
def notification_get_destination(destination_id: str):
    return notification.get_destination(destination_id)


@mcp.tool()
def notification_create_destination(name: str, endpoint: str, verification_token: str):
    return notification.create_destination(name, endpoint, verification_token)


@mcp.tool()
def notification_update_destination(destination_id: str, payload: dict):
    return notification.update_destination(destination_id, payload)


@mcp.tool()
def notification_delete_destination(destination_id: str):
    return notification.delete_destination(destination_id)


@mcp.tool()
def notification_get_topics(limit: int = 20, continuation_token: str | None = None):
    return notification.get_topics(limit=limit, continuation_token=continuation_token)


@mcp.tool()
def notification_get_topic(topic_id: str):
    return notification.get_topic(topic_id)


@mcp.tool()
def notification_get_subscriptions(limit: int = 20, continuation_token: str | None = None):
    return notification.get_subscriptions(limit=limit, continuation_token=continuation_token)


@mcp.tool()
def notification_get_subscription(subscription_id: str):
    return notification.get_subscription(subscription_id)


@mcp.tool()
def notification_create_subscription(topic_id: str, destination_id: str, payload: dict | None = None):
    return notification.create_subscription(topic_id, destination_id, payload)


@mcp.tool()
def notification_update_subscription(subscription_id: str, payload: dict):
    return notification.update_subscription(subscription_id, payload)


@mcp.tool()
def notification_delete_subscription(subscription_id: str):
    return notification.delete_subscription(subscription_id)


@mcp.tool()
def notification_enable_subscription(subscription_id: str):
    return notification.enable_subscription(subscription_id)


@mcp.tool()
def notification_disable_subscription(subscription_id: str):
    return notification.disable_subscription(subscription_id)


@mcp.tool()
def notification_test_subscription(subscription_id: str):
    return notification.test_subscription(subscription_id)


@mcp.tool()
def notification_get_public_key():
    return notification.get_public_key()
