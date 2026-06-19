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
mcp.tool()(get_product)
mcp.tool()(search_product_summaries)

# Charity
mcp.tool()(get_charity_org)
mcp.tool()(search_charity_orgs)

# Identity
mcp.tool()(get_user)

# Media
mcp.tool()(create_image_from_file)
mcp.tool()(create_image_from_url)
mcp.tool()(get_image)

mcp.tool()(create_video)
mcp.tool()(upload_video)
mcp.tool()(get_video)

mcp.tool()(create_document)
mcp.tool()(create_document_from_url)
mcp.tool()(upload_document)
mcp.tool()(get_document)

# Notification
mcp.tool()(create_destination)
mcp.tool()(get_destinations)
mcp.tool()(get_destination)
mcp.tool()(update_destination)
mcp.tool()(delete_destination)

mcp.tool()(create_subscription)
mcp.tool()(get_subscriptions)
mcp.tool()(get_subscription)
mcp.tool()(update_subscription)
mcp.tool()(delete_subscription)
mcp.tool()(enable_subscription)
mcp.tool()(disable_subscription)
mcp.tool()(test_subscription)

mcp.tool()(create_subscription_filter)
mcp.tool()(get_subscription_filter)
mcp.tool()(delete_subscription_filter)

mcp.tool()(get_topics)
mcp.tool()(get_topic)

mcp.tool()(get_notification_config)
mcp.tool()(update_notification_config)
mcp.tool()(get_public_key)

# Taxonomy
mcp.tool()(get_default_category_tree_id)
mcp.tool()(get_category_tree)
mcp.tool()(get_category_subtree)
mcp.tool()(get_category_suggestions)
mcp.tool()(get_item_aspects_for_category)
mcp.tool()(fetch_item_aspects)
mcp.tool()(get_expired_categories)
mcp.tool()(get_compatibility_properties)
mcp.tool()(get_compatibility_property_values)

# Translation
mcp.tool()(translate_text)


if __name__ == "__main__":
    mcp.run()
