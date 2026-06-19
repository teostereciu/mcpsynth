from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools import (
    CatalogTools,
    CharityTools,
    IdentityTools,
    MediaTools,
    NotificationTools,
    TaxonomyTools,
    TranslationTools,
)

mcp = FastMCP("ebay-commerce")

catalog = CatalogTools()
charity = CharityTools()
identity = IdentityTools()
media = MediaTools()
notification = NotificationTools()
taxonomy = TaxonomyTools()
translation = TranslationTools()


# Catalog
@mcp.tool()
def catalog_search_product_summaries(
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
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
    )


@mcp.tool()
def catalog_get_product(epid: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    return catalog.get_product(epid, marketplace_id=marketplace_id)


# Charity
@mcp.tool()
def charity_get_charity_orgs(
    marketplace_id: str,
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return charity.get_charity_orgs(
        marketplace_id=marketplace_id,
        q=q,
        registration_ids=registration_ids,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def charity_get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    return charity.get_charity_org(charity_org_id, marketplace_id=marketplace_id)


# Identity
@mcp.tool()
def identity_get_user() -> Dict[str, Any]:
    return identity.get_user()


# Taxonomy
@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    return taxonomy.get_default_category_tree_id(marketplace_id)


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    return taxonomy.get_category_tree(category_tree_id)


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return taxonomy.get_category_subtree(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    return taxonomy.get_category_suggestions(category_tree_id, q)


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return taxonomy.get_item_aspects_for_category(category_tree_id, category_id)


@mcp.tool()
def taxonomy_fetch_item_aspects(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return taxonomy.fetch_item_aspects(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    return taxonomy.get_expired_categories(category_tree_id)


@mcp.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return taxonomy.get_compatibility_properties(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    return taxonomy.get_compatibility_property_values(
        category_tree_id,
        category_id,
        compatibility_property,
        filter=filter,
    )


# Translation
@mcp.tool()
def translation_translate(from_lang: str, to_lang: str, text: str, translation_context: str) -> Dict[str, Any]:
    return translation.translate(
        from_lang=from_lang,
        to_lang=to_lang,
        text=text,
        translation_context=translation_context,
    )


# Notification
@mcp.tool()
def notification_get_config() -> Dict[str, Any]:
    return notification.get_config()


@mcp.tool()
def notification_update_config(config: Dict[str, Any]) -> Dict[str, Any]:
    return notification.update_config(config)


@mcp.tool()
def notification_create_destination(
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: Optional[str] = None,
) -> Dict[str, Any]:
    return notification.create_destination(
        endpoint=endpoint,
        verification_token=verification_token,
        status=status,
        name=name,
    )


@mcp.tool()
def notification_get_destinations(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return notification.get_destinations(limit=limit, continuation_token=continuation_token)


@mcp.tool()
def notification_get_destination(destination_id: str) -> Dict[str, Any]:
    return notification.get_destination(destination_id)


@mcp.tool()
def notification_update_destination(
    destination_id: str,
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: Optional[str] = None,
) -> Dict[str, Any]:
    return notification.update_destination(
        destination_id,
        endpoint=endpoint,
        verification_token=verification_token,
        status=status,
        name=name,
    )


@mcp.tool()
def notification_delete_destination(destination_id: str) -> Dict[str, Any]:
    return notification.delete_destination(destination_id)


@mcp.tool()
def notification_get_topics(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return notification.get_topics(limit=limit, continuation_token=continuation_token)


@mcp.tool()
def notification_get_topic(topic_id: str) -> Dict[str, Any]:
    return notification.get_topic(topic_id)


@mcp.tool()
def notification_create_subscription(
    topic_id: str,
    destination_id: str,
    payload: Optional[Dict[str, Any]] = None,
    user_based: bool = False,
) -> Dict[str, Any]:
    return notification.create_subscription(
        topic_id=topic_id,
        destination_id=destination_id,
        payload=payload,
        user_based=user_based,
    )


@mcp.tool()
def notification_get_subscriptions(
    limit: Optional[int] = None,
    continuation_token: Optional[str] = None,
    user_based: bool = False,
) -> Dict[str, Any]:
    return notification.get_subscriptions(limit=limit, continuation_token=continuation_token, user_based=user_based)


@mcp.tool()
def notification_get_subscription(subscription_id: str, user_based: bool = False) -> Dict[str, Any]:
    return notification.get_subscription(subscription_id, user_based=user_based)


@mcp.tool()
def notification_update_subscription(subscription_id: str, subscription: Dict[str, Any], user_based: bool = False) -> Dict[str, Any]:
    return notification.update_subscription(subscription_id, subscription, user_based=user_based)


@mcp.tool()
def notification_delete_subscription(subscription_id: str, user_based: bool = False) -> Dict[str, Any]:
    return notification.delete_subscription(subscription_id, user_based=user_based)


@mcp.tool()
def notification_enable_subscription(subscription_id: str, user_based: bool = False) -> Dict[str, Any]:
    return notification.enable_subscription(subscription_id, user_based=user_based)


@mcp.tool()
def notification_disable_subscription(subscription_id: str, user_based: bool = False) -> Dict[str, Any]:
    return notification.disable_subscription(subscription_id, user_based=user_based)


@mcp.tool()
def notification_test_subscription(subscription_id: str, user_based: bool = False) -> Dict[str, Any]:
    return notification.test_subscription(subscription_id, user_based=user_based)


@mcp.tool()
def notification_test() -> Dict[str, Any]:
    return notification.test()


@mcp.tool()
def notification_create_subscription_filter(subscription_id: str, filter_payload: Dict[str, Any]) -> Dict[str, Any]:
    return notification.create_subscription_filter(subscription_id, filter_payload)


@mcp.tool()
def notification_get_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    return notification.get_subscription_filter(subscription_id)


@mcp.tool()
def notification_delete_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    return notification.delete_subscription_filter(subscription_id)


@mcp.tool()
def notification_get_public_key() -> Dict[str, Any]:
    return notification.get_public_key()


# Media
@mcp.tool()
def media_create_image_from_url(image_url: str) -> Dict[str, Any]:
    return media.create_image_from_url(image_url)


@mcp.tool()
def media_create_image_from_file(file_path: str) -> Dict[str, Any]:
    return media.create_image_from_file(file_path)


@mcp.tool()
def media_get_image(image_id: str) -> Dict[str, Any]:
    return media.get_image(image_id)


@mcp.tool()
def media_create_video(title: str, size: int) -> Dict[str, Any]:
    return media.create_video(title=title, size=size)


@mcp.tool()
def media_upload_video(video_id: str, file_path: str) -> Dict[str, Any]:
    return media.upload_video(video_id, file_path)


@mcp.tool()
def media_get_video(video_id: str) -> Dict[str, Any]:
    return media.get_video(video_id)


@mcp.tool()
def media_create_document(title: str, size: int) -> Dict[str, Any]:
    return media.create_document(title=title, size=size)


@mcp.tool()
def media_create_document_from_url(url: str) -> Dict[str, Any]:
    return media.create_document_from_url(url=url)


@mcp.tool()
def media_upload_document(document_id: str, file_path: str) -> Dict[str, Any]:
    return media.upload_document(document_id, file_path)


@mcp.tool()
def media_get_document(document_id: str) -> Dict[str, Any]:
    return media.get_document(document_id)


if __name__ == "__main__":
    mcp.run()
