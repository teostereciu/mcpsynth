from mcp.server.fastmcp import FastMCP

from generated_tools import (
    create_destination,
    create_document,
    create_document_from_url,
    create_image_from_file,
    create_image_from_url,
    create_subscription,
    create_video,
    delete_destination,
    delete_subscription,
    disable_subscription,
    enable_subscription,
    fetch_item_aspects,
    get_category_subtree,
    get_category_suggestions,
    get_category_tree,
    get_charity_org,
    get_config,
    get_default_category_tree_id,
    get_destination,
    get_destinations,
    get_document,
    get_expired_categories,
    get_image,
    get_item_aspects_for_category,
    get_product,
    get_public_key,
    get_subscription,
    get_subscriptions,
    get_topic,
    get_topics,
    get_user,
    get_video,
    search_charity_orgs,
    search_product_summaries,
    test_subscription,
    translate,
    update_config,
    update_destination,
    update_subscription,
    upload_document,
    upload_video,
)

mcp = FastMCP("ebay-commerce")


@mcp.tool()
def catalog_get_product(epid: str, marketplace_id: str | None = None, use_sell_inventory_scope: bool = False):
    return get_product(epid, marketplace_id=marketplace_id, use_sell_inventory_scope=use_sell_inventory_scope)


@mcp.tool()
def catalog_search_product_summaries(
    q: str | None = None,
    gtin: str | None = None,
    mpn: str | None = None,
    category_ids: str | None = None,
    aspect_filter: str | None = None,
    fieldgroups: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    marketplace_id: str | None = None,
    use_sell_inventory_scope: bool = False,
):
    return search_product_summaries(
        q=q,
        gtin=gtin,
        mpn=mpn,
        category_ids=category_ids,
        aspect_filter=aspect_filter,
        fieldgroups=fieldgroups,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id,
        use_sell_inventory_scope=use_sell_inventory_scope,
    )


@mcp.tool()
def charity_get_charity_org(charity_org_id: str, marketplace_id: str):
    return get_charity_org(charity_org_id, marketplace_id)


@mcp.tool()
def charity_search_charity_orgs(
    marketplace_id: str,
    q: str | None = None,
    registration_ids: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return search_charity_orgs(
        marketplace_id=marketplace_id,
        q=q,
        registration_ids=registration_ids,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def identity_get_user():
    return get_user()


@mcp.tool()
def media_create_image_from_file(file_path: str):
    return create_image_from_file(file_path)


@mcp.tool()
def media_create_image_from_url(image_url: str):
    return create_image_from_url(image_url)


@mcp.tool()
def media_get_image(image_id: str):
    return get_image(image_id)


@mcp.tool()
def media_create_document(metadata: dict):
    return create_document(metadata)


@mcp.tool()
def media_create_document_from_url(source_url: str, document_type: str | None = None):
    return create_document_from_url(source_url, document_type=document_type)


@mcp.tool()
def media_get_document(document_id: str):
    return get_document(document_id)


@mcp.tool()
def media_upload_document(document_id: str, file_path: str):
    return upload_document(document_id, file_path)


@mcp.tool()
def media_create_video(metadata: dict):
    return create_video(metadata)


@mcp.tool()
def media_upload_video(video_id: str, file_path: str):
    return upload_video(video_id, file_path)


@mcp.tool()
def media_get_video(video_id: str):
    return get_video(video_id)


@mcp.tool()
def notification_create_destination(endpoint: str, verification_token: str, status: str = "ENABLED", name: str | None = None):
    return create_destination(endpoint=endpoint, verification_token=verification_token, status=status, name=name)


@mcp.tool()
def notification_get_destinations():
    return get_destinations()


@mcp.tool()
def notification_get_destination(destination_id: str):
    return get_destination(destination_id)


@mcp.tool()
def notification_update_destination(destination_id: str, patch: dict):
    return update_destination(destination_id, patch)


@mcp.tool()
def notification_delete_destination(destination_id: str):
    return delete_destination(destination_id)


@mcp.tool()
def notification_get_topics():
    return get_topics()


@mcp.tool()
def notification_get_topic(topic_id: str):
    return get_topic(topic_id)


@mcp.tool()
def notification_create_subscription(topic_id: str, destination_id: str, payload: dict | None = None):
    return create_subscription(topic_id=topic_id, destination_id=destination_id, payload=payload)


@mcp.tool()
def notification_get_subscriptions():
    return get_subscriptions()


@mcp.tool()
def notification_get_subscription(subscription_id: str):
    return get_subscription(subscription_id)


@mcp.tool()
def notification_update_subscription(subscription_id: str, patch: dict):
    return update_subscription(subscription_id, patch)


@mcp.tool()
def notification_delete_subscription(subscription_id: str):
    return delete_subscription(subscription_id)


@mcp.tool()
def notification_enable_subscription(subscription_id: str):
    return enable_subscription(subscription_id)


@mcp.tool()
def notification_disable_subscription(subscription_id: str):
    return disable_subscription(subscription_id)


@mcp.tool()
def notification_test_subscription(subscription_id: str):
    return test_subscription(subscription_id)


@mcp.tool()
def notification_get_config():
    return get_config()


@mcp.tool()
def notification_update_config(config: dict):
    return update_config(config)


@mcp.tool()
def notification_get_public_key():
    return get_public_key()


@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str):
    return get_default_category_tree_id(marketplace_id)


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str):
    return get_category_tree(category_tree_id)


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str):
    return get_category_subtree(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str):
    return get_category_suggestions(category_tree_id, q)


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str):
    return get_item_aspects_for_category(category_tree_id, category_id)


@mcp.tool()
def taxonomy_fetch_item_aspects(category_tree_id: str, category_id: str, additional_params: dict | None = None):
    return fetch_item_aspects(category_tree_id, category_id, additional_params=additional_params)


@mcp.tool()
def taxonomy_get_expired_categories(category_tree_id: str):
    return get_expired_categories(category_tree_id)


@mcp.tool()
def translation_translate(from_lang: str, to_lang: str, text: str, translation_context: str):
    return translate(from_lang=from_lang, to_lang=to_lang, text=text, translation_context=translation_context)


if __name__ == "__main__":
    mcp.run()
