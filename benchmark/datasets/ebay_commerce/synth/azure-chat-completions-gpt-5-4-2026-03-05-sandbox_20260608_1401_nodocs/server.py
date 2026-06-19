from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.catalog import (
    get_product,
    get_product_by_compatibility,
    get_product_metadata,
    search_products,
)
from generated_tools.charity import get_charity_org, get_charity_orgs
from generated_tools.identity import get_user
from generated_tools.media import create_image_from_url, create_video, get_image, get_video, upload_video
from generated_tools.notification import (
    create_destination,
    create_subscription,
    delete_destination,
    delete_subscription,
    get_config,
    get_destination,
    get_destinations,
    get_subscription,
    get_subscriptions,
    get_topic,
    get_topics,
    update_config,
    update_subscription,
)
from generated_tools.taxonomy import (
    get_category_suggestions,
    get_category_subtree,
    get_category_tree,
    get_compatibility_properties,
    get_compatibility_property_values,
    get_default_category_tree_id,
    get_item_aspects_for_category,
)
from generated_tools.translation import translate


mcp = FastMCP("ebay-commerce")


@mcp.tool()
def catalog_get_product(epa_id: str) -> Dict[str, Any]:
    return get_product(epa_id)


@mcp.tool()
def catalog_search_products(
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    brand: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    return search_products(q=q, gtin=gtin, mpn=mpn, brand=brand, limit=limit, offset=offset, filter=filter)


@mcp.tool()
def catalog_search_by_compatibility(
    q: Optional[str] = None,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return get_product_by_compatibility(q=q, filter=filter, limit=limit, offset=offset)


@mcp.tool()
def catalog_get_product_metadata(epa_id: str) -> Dict[str, Any]:
    return get_product_metadata(epa_id)


@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return get_default_category_tree_id(marketplace_id)


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    return get_category_tree(category_tree_id)


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return get_category_subtree(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    return get_category_suggestions(category_tree_id, q)


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return get_item_aspects_for_category(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return get_compatibility_properties(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_compatibility_property_values(category_tree_id: str, category_id: str, property_name: str) -> Dict[str, Any]:
    return get_compatibility_property_values(category_tree_id, category_id, property_name)


@mcp.tool()
def identity_get_user() -> Dict[str, Any]:
    return get_user()


@mcp.tool()
def media_create_image_from_url(image_url: str, classification: Optional[str] = None) -> Dict[str, Any]:
    return create_image_from_url(image_url, classification)


@mcp.tool()
def media_get_image(image_id: str) -> Dict[str, Any]:
    return get_image(image_id)


@mcp.tool()
def media_create_video(body: Dict[str, Any]) -> Dict[str, Any]:
    return create_video(body)


@mcp.tool()
def media_get_video(video_id: str) -> Dict[str, Any]:
    return get_video(video_id)


@mcp.tool()
def media_upload_video(video_id: str, size: Optional[int] = None, content_type: str = "application/octet-stream") -> Dict[str, Any]:
    return upload_video(video_id, size, content_type)


@mcp.tool()
def notification_get_config() -> Dict[str, Any]:
    return get_config()


@mcp.tool()
def notification_update_config(body: Dict[str, Any]) -> Dict[str, Any]:
    return update_config(body)


@mcp.tool()
def notification_create_destination(body: Dict[str, Any]) -> Dict[str, Any]:
    return create_destination(body)


@mcp.tool()
def notification_get_destination(destination_id: str) -> Dict[str, Any]:
    return get_destination(destination_id)


@mcp.tool()
def notification_delete_destination(destination_id: str) -> Dict[str, Any]:
    return delete_destination(destination_id)


@mcp.tool()
def notification_get_destinations(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return get_destinations(limit, continuation_token)


@mcp.tool()
def notification_create_subscription(body: Dict[str, Any]) -> Dict[str, Any]:
    return create_subscription(body)


@mcp.tool()
def notification_get_subscription(subscription_id: str) -> Dict[str, Any]:
    return get_subscription(subscription_id)


@mcp.tool()
def notification_update_subscription(subscription_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return update_subscription(subscription_id, body)


@mcp.tool()
def notification_delete_subscription(subscription_id: str) -> Dict[str, Any]:
    return delete_subscription(subscription_id)


@mcp.tool()
def notification_get_subscriptions(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return get_subscriptions(limit, continuation_token)


@mcp.tool()
def notification_get_topics(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return get_topics(limit, continuation_token)


@mcp.tool()
def notification_get_topic(topic_id: str) -> Dict[str, Any]:
    return get_topic(topic_id)


@mcp.tool()
def charity_get_org(charity_org_id: str) -> Dict[str, Any]:
    return get_charity_org(charity_org_id)


@mcp.tool()
def charity_search_orgs(
    q: Optional[str] = None,
    registration_id: Optional[str] = None,
    nonprofit_org_name: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return get_charity_orgs(q=q, registration_id=registration_id, nonprofit_org_name=nonprofit_org_name, limit=limit, offset=offset)


@mcp.tool()
def translation_translate(body: Dict[str, Any]) -> Dict[str, Any]:
    return translate(body)


if __name__ == "__main__":
    mcp.run()
