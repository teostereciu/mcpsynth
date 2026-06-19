from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools import catalog, charity, identity, media, notification, taxonomy, translation


mcp = FastMCP("ebay-commerce")


# Catalog
@mcp.tool()
def catalog_get_product(epid: str, marketplace_id: Optional[str] = None, use_sell_inventory_scope: bool = False) -> Any:
    return catalog.get_product(epid=epid, marketplace_id=marketplace_id, use_sell_inventory_scope=use_sell_inventory_scope)


@mcp.tool()
def catalog_search_product_summaries(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    aspects: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Any:
    return catalog.search_product_summaries(
        q=q,
        category_ids=category_ids,
        gtin=gtin,
        mpn=mpn,
        aspects=aspects,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id,
    )


# Charity
@mcp.tool()
def charity_get_charity_org(charity_org_id: str, marketplace_id: str) -> Any:
    return charity.get_charity_org(charity_org_id=charity_org_id, marketplace_id=marketplace_id)


@mcp.tool()
def charity_get_charity_orgs(
    marketplace_id: str,
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Any:
    return charity.get_charity_orgs(
        marketplace_id=marketplace_id,
        q=q,
        registration_ids=registration_ids,
        limit=limit,
        offset=offset,
    )


# Identity
@mcp.tool()
def identity_get_user() -> Any:
    return identity.get_user()


# Media
@mcp.tool()
def media_create_image_from_file(file_path: str) -> Any:
    return media.create_image_from_file(file_path=file_path)


@mcp.tool()
def media_create_image_from_url(image_url: str) -> Any:
    return media.create_image_from_url(image_url=image_url)


@mcp.tool()
def media_get_image(image_id: str) -> Any:
    return media.get_image(image_id=image_id)


@mcp.tool()
def media_create_document(metadata: Dict[str, Any]) -> Any:
    return media.create_document(metadata=metadata)


@mcp.tool()
def media_create_document_from_url(url: str) -> Any:
    return media.create_document_from_url(url=url)


@mcp.tool()
def media_upload_document(document_id: str, file_path: str, content_type: Optional[str] = None) -> Any:
    return media.upload_document(document_id=document_id, file_path=file_path, content_type=content_type)


@mcp.tool()
def media_get_document(document_id: str) -> Any:
    return media.get_document(document_id=document_id)


@mcp.tool()
def media_create_video(metadata: Dict[str, Any]) -> Any:
    return media.create_video(metadata=metadata)


@mcp.tool()
def media_upload_video(video_id: str, file_path: str, content_type: Optional[str] = None) -> Any:
    return media.upload_video(video_id=video_id, file_path=file_path, content_type=content_type)


@mcp.tool()
def media_get_video(video_id: str) -> Any:
    return media.get_video(video_id=video_id)


# Notification
@mcp.tool()
def notification_get_config() -> Any:
    return notification.get_config()


@mcp.tool()
def notification_update_config(payload: Dict[str, Any]) -> Any:
    return notification.update_config(payload=payload)


@mcp.tool()
def notification_create_destination(delivery_config: Dict[str, Any], status: str, name: Optional[str] = None) -> Any:
    return notification.create_destination(delivery_config=delivery_config, status=status, name=name)


@mcp.tool()
def notification_get_destinations() -> Any:
    return notification.get_destinations()


@mcp.tool()
def notification_get_destination(destination_id: str) -> Any:
    return notification.get_destination(destination_id=destination_id)


@mcp.tool()
def notification_update_destination(destination_id: str, payload: Dict[str, Any]) -> Any:
    return notification.update_destination(destination_id=destination_id, payload=payload)


@mcp.tool()
def notification_delete_destination(destination_id: str) -> Any:
    return notification.delete_destination(destination_id=destination_id)


@mcp.tool()
def notification_get_topics() -> Any:
    return notification.get_topics()


@mcp.tool()
def notification_get_topic(topic_id: str) -> Any:
    return notification.get_topic(topic_id=topic_id)


@mcp.tool()
def notification_create_subscription(payload: Dict[str, Any]) -> Any:
    return notification.create_subscription(payload=payload)


@mcp.tool()
def notification_get_subscriptions() -> Any:
    return notification.get_subscriptions()


@mcp.tool()
def notification_get_subscription(subscription_id: str) -> Any:
    return notification.get_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Any:
    return notification.update_subscription(subscription_id=subscription_id, payload=payload)


@mcp.tool()
def notification_delete_subscription(subscription_id: str) -> Any:
    return notification.delete_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_enable_subscription(subscription_id: str) -> Any:
    return notification.enable_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_disable_subscription(subscription_id: str) -> Any:
    return notification.disable_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_test_subscription(subscription_id: str) -> Any:
    return notification.test_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_create_subscription_filter(subscription_id: str, payload: Dict[str, Any]) -> Any:
    return notification.create_subscription_filter(subscription_id=subscription_id, payload=payload)


@mcp.tool()
def notification_get_subscription_filter(subscription_id: str) -> Any:
    return notification.get_subscription_filter(subscription_id=subscription_id)


@mcp.tool()
def notification_delete_subscription_filter(subscription_id: str) -> Any:
    return notification.delete_subscription_filter(subscription_id=subscription_id)


@mcp.tool()
def notification_get_public_key() -> Any:
    return notification.get_public_key()


# Taxonomy
@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str) -> Any:
    return taxonomy.get_default_category_tree_id(marketplace_id=marketplace_id)


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str) -> Any:
    return taxonomy.get_category_tree(category_tree_id=category_tree_id)


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> Any:
    return taxonomy.get_category_subtree(category_tree_id=category_tree_id, category_id=category_id)


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str) -> Any:
    return taxonomy.get_category_suggestions(category_tree_id=category_tree_id, q=q)


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Any:
    return taxonomy.get_item_aspects_for_category(category_tree_id=category_tree_id, category_id=category_id)


@mcp.tool()
def taxonomy_fetch_item_aspects(category_tree_id: str, payload: Dict[str, Any]) -> Any:
    return taxonomy.fetch_item_aspects(category_tree_id=category_tree_id, payload=payload)


@mcp.tool()
def taxonomy_get_expired_categories(category_tree_id: str, date: Optional[str] = None) -> Any:
    return taxonomy.get_expired_categories(category_tree_id=category_tree_id, date=date)


@mcp.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str) -> Any:
    return taxonomy.get_compatibility_properties(category_tree_id=category_tree_id, category_id=category_id)


@mcp.tool()
def taxonomy_get_compatibility_property_values(category_tree_id: str, category_id: str, compatibility_property: str) -> Any:
    return taxonomy.get_compatibility_property_values(
        category_tree_id=category_tree_id,
        category_id=category_id,
        compatibility_property=compatibility_property,
    )


# Translation
@mcp.tool()
def translation_translate(from_lang: str, to_lang: str, text: str, translation_context: str) -> Any:
    return translation.translate(from_lang=from_lang, to_lang=to_lang, text=text, translation_context=translation_context)


if __name__ == "__main__":
    mcp.run()
