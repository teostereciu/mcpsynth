from mcp.server.fastmcp import FastMCP

from generated_tools import catalog, charity, identity, media, notification, taxonomy, translation

mcp = FastMCP("ebay-commerce")


# Catalog
mcp.tool()(catalog.catalog_search)
mcp.tool()(catalog.get_product)
mcp.tool()(catalog.get_product_summary)
mcp.tool()(catalog.get_product_compatibility)

# Charity
mcp.tool()(charity.get_charity_org)
mcp.tool()(charity.charity_search)

# Identity
mcp.tool()(identity.get_user)

# Media
mcp.tool()(media.upload_image)
mcp.tool()(media.get_image)

# Notification
mcp.tool()(notification.list_topics)
mcp.tool()(notification.list_subscriptions)
mcp.tool()(notification.get_subscription)
mcp.tool()(notification.create_subscription)
mcp.tool()(notification.delete_subscription)

# Taxonomy
mcp.tool()(taxonomy.get_default_category_tree_id)
mcp.tool()(taxonomy.get_category_tree)
mcp.tool()(taxonomy.get_category_subtree)
mcp.tool()(taxonomy.get_item_aspects_for_category)
mcp.tool()(taxonomy.get_compatibility_properties)

# Translation
mcp.tool()(translation.translate)


if __name__ == "__main__":
    mcp.run_stdio()
