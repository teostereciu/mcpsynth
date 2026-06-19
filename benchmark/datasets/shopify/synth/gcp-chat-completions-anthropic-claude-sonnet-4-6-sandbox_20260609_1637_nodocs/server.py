"""
Shopify Admin REST API — MCP Server
Runs over stdio using FastMCP.

Required environment variables:
  SHOPIFY_ACCESS_TOKEN  — store access token
  SHOPIFY_STORE_URL     — store domain (e.g. your-store.myshopify.com)
"""

from mcp.server.fastmcp import FastMCP

from generated_tools import (
    products,
    collections,
    orders,
    draft_orders,
    customers,
    fulfillment,
    inventory,
    discounts,
    metafields,
    webhooks,
    pages_blogs,
    shop_misc,
    shipping,
    marketing,
)

mcp = FastMCP(
    name="shopify-admin",
    description=(
        "Comprehensive Shopify Admin REST API tools covering products, variants, "
        "images, collections, orders, draft orders, refunds, transactions, "
        "customers, fulfillment, inventory, discounts, metafields, webhooks, "
        "pages, blogs, articles, themes, shipping, gift cards, and more."
    ),
)

# Register all domain modules
products.register(mcp)
collections.register(mcp)
orders.register(mcp)
draft_orders.register(mcp)
customers.register(mcp)
fulfillment.register(mcp)
inventory.register(mcp)
discounts.register(mcp)
metafields.register(mcp)
webhooks.register(mcp)
pages_blogs.register(mcp)
shop_misc.register(mcp)
shipping.register(mcp)
marketing.register(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
