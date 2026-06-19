from __future__ import annotations

from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.catalog import get_product, search_product_summaries
from generated_tools.charity import get_charity_org, search_charity_orgs
from generated_tools.identity import get_user
from generated_tools.media import (
    create_document,
    create_document_from_url,
    create_image_from_file,
    create_image_from_url,
    create_video,
    get_document,
    get_image,
    get_video,
    upload_document,
    upload_video,
)
from generated_tools.notification import (
    create_destination,
    create_subscription,
    create_subscription_filter,
    delete_destination,
    delete_subscription,
    delete_subscription_filter,
    disable_subscription,
    enable_subscription,
    get_destination,
    get_destinations,
    get_notification_config,
    get_public_key,
    get_subscription,
    get_subscription_filter,
    get_subscriptions,
    get_topic,
    get_topics,
    test_subscription,
    update_destination,
    update_notification_config,
    update_subscription,
)
from generated_tools.taxonomy import (
    fetch_item_aspects,
    get_category_subtree,
    get_category_suggestions,
    get_category_tree,
    get_compatibility_properties,
    get_compatibility_property_values,
    get_default_category_tree_id,
    get_expired_categories,
    get_item_aspects_for_category,
)
from generated_tools.translation import translate_text

mcp = FastMCP("ebay-commerce")


# Catalog
@mcp.tool()
def catalog_search_product_summaries(
    query: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_id: Optional[str] = None,
    aspects: Optional[str] = None,
    field_groups: Optional[str] = None,
    page_size: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    return search_product_summaries(
        query=query,
        gtin=gtin,
        mpn=mpn,
        category_id=category_id,
        aspects=aspects,
        field_groups=field_groups,
        page_size=page_size,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def catalog_get_product(epid: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    return get_product(epid=epid, marketplace_id=marketplace_id)


# Charity
@mcp.tool()
def charity_get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    return get_charity_org(charity_org_id=charity_org_id, marketplace_id=marketplace_id)


@mcp.tool()
def charity_search_charity_orgs(
    marketplace_id: str,
    query: Optional[str] = None,
    registration_ids: Optional[str] = None,
    page_size: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return search_charity_orgs(
        marketplace_id=marketplace_id,
        query=query,
        registration_ids=registration_ids,
        page_size=page_size,
        offset=offset,
    )


# Identity
@mcp.tool()
def identity_get_user() -> Dict[str, Any]:
    return get_user()


# Media
@mcp.tool()
def media_create_image_from_file(file_path: str) -> Dict[str, Any]:
    return create_image_from_file(file_path=file_path)


@mcp.tool()
def media_create_image_from_url(image_url: str) -> Dict[str, Any]:
    return create_image_from_url(image_url=image_url)


@mcp.tool()
def media_get_image(image_id: str) -> Dict[str, Any]:
    return get_image(image_id=image_id)


@mcp.tool()
def media_create_document(type: str, languages: list[str]) -> Dict[str, Any]:
    return create_document(type=type, languages=languages)


@mcp.tool()
def media_create_document_from_url(type: str, languages: list[str], document_url: str) -> Dict[str, Any]:
    return create_document_from_url(type=type, languages=languages, document_url=document_url)


@mcp.tool()
def media_upload_document(document_id: str, file_path: str) -> Dict[str, Any]:
    return upload_document(document_id=document_id, file_path=file_path)


@mcp.tool()
def media_get_document(document_id: str) -> Dict[str, Any]:
    return get_document(document_id=document_id)


@mcp.tool()
def media_create_video(title: str, size: int, classification: str, description: Optional[str] = None) -> Dict[str, Any]:
    return create_video(title=title, size=size, classification=classification, description=description)


@mcp.tool()
def media_upload_video(video_id: str, file_path: str) -> Dict[str, Any]:
    return upload_video(video_id=video_id, file_path=file_path)


@mcp.tool()
def media_get_video(video_id: str) -> Dict[str, Any]:
    return get_video(video_id=video_id)


# Notification
@mcp.tool()
def notification_get_config() -> Dict[str, Any]:
    return get_notification_config()


@mcp.tool()
def notification_update_config(alert_email: str) -> Dict[str, Any]:
    return update_notification_config(alert_email=alert_email)


@mcp.tool()
def notification_create_destination(name: str, status: str, delivery_config: Dict[str, Any]) -> Dict[str, Any]:
    return create_destination(name=name, status=status, delivery_config=delivery_config)


@mcp.tool()
def notification_get_destinations() -> Dict[str, Any]:
    return get_destinations()


@mcp.tool()
def notification_get_destination(destination_id: str) -> Dict[str, Any]:
    return get_destination(destination_id=destination_id)


@mcp.tool()
def notification_update_destination(
    destination_id: str,
    name: Optional[str] = None,
    status: Optional[str] = None,
    delivery_config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return update_destination(destination_id=destination_id, name=name, status=status, delivery_config=delivery_config)


@mcp.tool()
def notification_delete_destination(destination_id: str) -> Dict[str, Any]:
    return delete_destination(destination_id=destination_id)


@mcp.tool()
def notification_get_public_key(public_key_id: str) -> Dict[str, Any]:
    return get_public_key(public_key_id=public_key_id)


@mcp.tool()
def notification_create_subscription(
    topic_id: str,
    status: str,
    destination_id: str,
    payload: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return create_subscription(topic_id=topic_id, status=status, destination_id=destination_id, payload=payload)


@mcp.tool()
def notification_get_subscriptions() -> Dict[str, Any]:
    return get_subscriptions()


@mcp.tool()
def notification_get_subscription(subscription_id: str) -> Dict[str, Any]:
    return get_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return update_subscription(subscription_id=subscription_id, payload=payload)


@mcp.tool()
def notification_delete_subscription(subscription_id: str) -> Dict[str, Any]:
    return delete_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_enable_subscription(subscription_id: str) -> Dict[str, Any]:
    return enable_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_disable_subscription(subscription_id: str) -> Dict[str, Any]:
    return disable_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_test_subscription(subscription_id: str) -> Dict[str, Any]:
    return test_subscription(subscription_id=subscription_id)


@mcp.tool()
def notification_create_subscription_filter(subscription_id: str, filter_payload: Dict[str, Any]) -> Dict[str, Any]:
    return create_subscription_filter(subscription_id=subscription_id, filter_payload=filter_payload)


@mcp.tool()
def notification_get_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    return get_subscription_filter(subscription_id=subscription_id, filter_id=filter_id)


@mcp.tool()
def notification_delete_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    return delete_subscription_filter(subscription_id=subscription_id, filter_id=filter_id)


@mcp.tool()
def notification_get_topics() -> Dict[str, Any]:
    return get_topics()


@mcp.tool()
def notification_get_topic(topic_id: str) -> Dict[str, Any]:
    return get_topic(topic_id=topic_id)


# Taxonomy
@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    return get_default_category_tree_id(marketplace_id=marketplace_id)


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    return get_category_tree(category_tree_id=category_tree_id)


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return get_category_subtree(category_tree_id=category_tree_id, category_id=category_id)


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, query: str) -> Dict[str, Any]:
    return get_category_suggestions(category_tree_id=category_tree_id, query=query)


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return get_item_aspects_for_category(category_tree_id=category_tree_id, category_id=category_id)


@mcp.tool()
def taxonomy_fetch_item_aspects(category_tree_id: str, item: Dict[str, Any]) -> Dict[str, Any]:
    return fetch_item_aspects(category_tree_id=category_tree_id, item=item)


@mcp.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return get_compatibility_properties(category_tree_id=category_tree_id, category_id=category_id)


@mcp.tool()
def taxonomy_get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    return get_compatibility_property_values(
        category_tree_id=category_tree_id,
        category_id=category_id,
        compatibility_property=compatibility_property,
        filter=filter,
    )


@mcp.tool()
def taxonomy_get_expired_categories(category_tree_id: str, category_version: Optional[str] = None) -> Dict[str, Any]:
    return get_expired_categories(category_tree_id=category_tree_id, category_version=category_version)


# Translation
@mcp.tool()
def translation_translate_text(from_lang: str, to_lang: str, text: str, translation_context: str) -> Dict[str, Any]:
    return translate_text(from_lang=from_lang, to_lang=to_lang, text=text, translation_context=translation_context)


if __name__ == "__main__":
    mcp.run()
