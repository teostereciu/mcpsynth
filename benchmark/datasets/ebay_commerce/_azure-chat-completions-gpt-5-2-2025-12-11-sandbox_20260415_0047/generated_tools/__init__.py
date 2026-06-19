"""eBay Commerce API MCP server (FastMCP)."""

from __future__ import annotations

from fastmcp import FastMCP

from . import catalog, charity, identity, media, notification, taxonomy, translation

mcp = FastMCP("ebay-commerce")


# Taxonomy
mcp.tool()(taxonomy.get_default_category_tree_id)
mcp.tool()(taxonomy.get_category_tree)
mcp.tool()(taxonomy.get_category_subtree)
mcp.tool()(taxonomy.get_category_suggestions)
mcp.tool()(taxonomy.get_item_aspects_for_category)
mcp.tool()(taxonomy.get_compatibility_properties)
mcp.tool()(taxonomy.get_compatibility_property_values)
mcp.tool()(taxonomy.get_expired_categories)
mcp.tool()(taxonomy.fetch_item_aspects)

# Charity
mcp.tool()(charity.search_charity_orgs)
mcp.tool()(charity.get_charity_org)

# Media
mcp.tool()(media.create_image_from_url)
mcp.tool()(media.get_image)
mcp.tool()(media.create_document_from_url)
mcp.tool()(media.get_document)
mcp.tool()(media.upload_document)

# Translation
mcp.tool()(translation.translate_text)

# Catalog
mcp.tool()(catalog.search_product_summaries)
mcp.tool()(catalog.get_product)

# Identity
mcp.tool()(identity.get_user)

# Notification
mcp.tool()(notification.get_config)
mcp.tool()(notification.update_config)
mcp.tool()(notification.get_public_key)

mcp.tool()(notification.create_destination)
mcp.tool()(notification.get_destinations)
mcp.tool()(notification.get_destination)
mcp.tool()(notification.update_destination)
mcp.tool()(notification.delete_destination)

mcp.tool()(notification.get_topics)
mcp.tool()(notification.get_topic)

mcp.tool()(notification.create_subscription)
mcp.tool()(notification.get_subscriptions)
mcp.tool()(notification.get_subscription)
mcp.tool()(notification.update_subscription)
mcp.tool()(notification.delete_subscription)
mcp.tool()(notification.enable_subscription)
mcp.tool()(notification.disable_subscription)
mcp.tool()(notification.test_subscription)
mcp.tool()(notification.test)

mcp.tool()(notification.create_subscription_filter)
mcp.tool()(notification.get_subscription_filter)
mcp.tool()(notification.delete_subscription_filter)
