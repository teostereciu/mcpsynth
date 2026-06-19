"""
Shopify Admin REST API MCP Server
Runs over stdio using FastMCP.
"""
import os
from mcp.server.fastmcp import FastMCP

from generated_tools.products import register_products
from generated_tools.collections import register_collections
from generated_tools.orders import register_orders
from generated_tools.fulfillment import register_fulfillment
from generated_tools.inventory import register_inventory
from generated_tools.customers import register_customers
from generated_tools.discounts import register_discounts
from generated_tools.webhooks import register_webhooks
from generated_tools.metafields import register_metafields
from generated_tools.shop_misc import register_shop_misc

# Validate required environment variables at startup
_store_url = os.environ.get("SHOPIFY_STORE_URL", "")
_access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN", "")

if not _store_url:
    import sys
    print("WARNING: SHOPIFY_STORE_URL environment variable is not set", file=sys.stderr)
if not _access_token:
    import sys
    print("WARNING: SHOPIFY_ACCESS_TOKEN environment variable is not set", file=sys.stderr)

mcp = FastMCP(
    name="shopify-admin",
    instructions=(
        "MCP server for the Shopify Admin REST API (2026-01). "
        "Provides tools for managing products, orders, customers, inventory, "
        "fulfillment, discounts, webhooks, metafields, and more. "
        "Requires SHOPIFY_STORE_URL and SHOPIFY_ACCESS_TOKEN environment variables."
    ),
)

# Register all tool domains
register_products(mcp)
register_collections(mcp)
register_orders(mcp)
register_fulfillment(mcp)
register_inventory(mcp)
register_customers(mcp)
register_discounts(mcp)
register_webhooks(mcp)
register_metafields(mcp)
register_shop_misc(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
