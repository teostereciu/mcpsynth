from mcp.server.fastmcp import FastMCP

from generated_tools import catalog, charity, identity, media, notification, taxonomy, translation

mcp = FastMCP("ebay-commerce")


# Catalog
@mcp.tool()
def catalog_get_product(product_id: str, marketplace_id: str | None = None):
    return catalog.get_product(product_id, marketplace_id=marketplace_id)


@mcp.tool()
def catalog_search_products(
    q: str | None = None,
    gtin: str | None = None,
    epid: str | None = None,
    mpn: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    marketplace_id: str | None = None,
):
    return catalog.search_products(
        q=q,
        gtin=gtin,
        epid=epid,
        mpn=mpn,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id,
    )


# Charity
@mcp.tool()
def charity_get_charity_org(charity_org_id: str, marketplace_id: str | None = None):
    return charity.get_charity_org(charity_org_id, marketplace_id=marketplace_id)


@mcp.tool()
def charity_search_charity_orgs(
    q: str | None = None,
    registration_ids: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    marketplace_id: str | None = None,
):
    return charity.search_charity_orgs(
        q=q,
        registration_ids=registration_ids,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id,
    )


# Identity
@mcp.tool()
def identity_get_user():
    return identity.get_user()


# Media
@mcp.tool()
def media_create_upload_session(
    file_name: str,
    file_size: int,
    marketplace_id: str | None = None,
    upload_type: str = "IMAGE",
):
    return media.create_upload_session(
        file_name=file_name,
        file_size=file_size,
        marketplace_id=marketplace_id,
        upload_type=upload_type,
    )


@mcp.tool()
def media_get_upload_session(upload_session_id: str):
    return media.get_upload_session(upload_session_id)


@mcp.tool()
def media_upload_file_part(
    upload_session_id: str,
    content_range: str,
    data: str,
    content_type: str = "application/octet-stream",
):
    return media.upload_file_part(
        upload_session_id,
        content_range=content_range,
        data=data,
        content_type=content_type,
    )


@mcp.tool()
def media_complete_upload_session(upload_session_id: str):
    return media.complete_upload_session(upload_session_id)


@mcp.tool()
def media_get_asset(asset_id: str):
    return media.get_asset(asset_id)


@mcp.tool()
def media_search_assets(limit: int | None = None, offset: int | None = None, sort: str | None = None):
    return media.search_assets(limit=limit, offset=offset, sort=sort)


@mcp.tool()
def media_delete_asset(asset_id: str):
    return media.delete_asset(asset_id)


# Notification
@mcp.tool()
def notification_get_public_key():
    return notification.get_public_key()


@mcp.tool()
def notification_get_subscriptions():
    return notification.get_subscriptions()


@mcp.tool()
def notification_create_subscription(subscription: str | dict):
    return notification.create_subscription(subscription)


@mcp.tool()
def notification_get_subscription(subscription_id: str):
    return notification.get_subscription(subscription_id)


@mcp.tool()
def notification_update_subscription(subscription_id: str, subscription: str | dict):
    return notification.update_subscription(subscription_id, subscription)


@mcp.tool()
def notification_delete_subscription(subscription_id: str):
    return notification.delete_subscription(subscription_id)


@mcp.tool()
def notification_get_destinations():
    return notification.get_destinations()


@mcp.tool()
def notification_create_destination(destination: str | dict):
    return notification.create_destination(destination)


@mcp.tool()
def notification_get_destination(destination_id: str):
    return notification.get_destination(destination_id)


@mcp.tool()
def notification_update_destination(destination_id: str, destination: str | dict):
    return notification.update_destination(destination_id, destination)


@mcp.tool()
def notification_delete_destination(destination_id: str):
    return notification.delete_destination(destination_id)


# Taxonomy
@mcp.tool()
def taxonomy_get_default_category_tree_id(marketplace_id: str):
    return taxonomy.get_default_category_tree_id(marketplace_id=marketplace_id)


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str):
    return taxonomy.get_category_tree(category_tree_id)


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str):
    return taxonomy.get_category_subtree(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str):
    return taxonomy.get_category_suggestions(category_tree_id=category_tree_id, q=q)


@mcp.tool()
def taxonomy_get_item_aspects_for_category(
    category_tree_id: str,
    category_id: str,
    marketplace_id: str | None = None,
):
    return taxonomy.get_item_aspects_for_category(
        category_tree_id,
        category_id,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def taxonomy_get_compatibility_properties(category_tree_id: str, category_id: str):
    return taxonomy.get_compatibility_properties(category_tree_id, category_id)


@mcp.tool()
def taxonomy_get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return taxonomy.get_compatibility_property_values(
        category_tree_id,
        category_id,
        compatibility_property,
        filter=filter,
        limit=limit,
        offset=offset,
    )


# Translation
@mcp.tool()
def translation_translate(payload: str | dict):
    return translation.translate(payload)


if __name__ == "__main__":
    mcp.run()
