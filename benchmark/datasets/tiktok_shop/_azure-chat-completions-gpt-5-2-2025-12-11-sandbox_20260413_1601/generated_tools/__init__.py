"""TikTok Shop MCP Server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

from . import customer_service, finance, fulfillment, orders, products, promotions, returns, seller

mcp = FastMCP("tiktok-shop")


# Seller / Authorization
mcp.tool()(seller.get_authorized_shops)
mcp.tool()(seller.get_active_shops)
mcp.tool()(seller.get_seller_permissions)

# Products
mcp.tool()(products.get_categories)
mcp.tool()(products.recommend_category)
mcp.tool()(products.get_brands)
mcp.tool()(products.get_attributes)
mcp.tool()(products.create_product)
mcp.tool()(products.search_products)
mcp.tool()(products.get_product)
mcp.tool()(products.update_price)
mcp.tool()(products.update_inventory)

# Orders
mcp.tool()(orders.get_order_list)
mcp.tool()(orders.get_order_detail)

# Fulfillment
mcp.tool()(fulfillment.get_warehouse_list)
mcp.tool()(fulfillment.search_packages)
mcp.tool()(fulfillment.ship_package)
mcp.tool()(fulfillment.get_package_shipping_document)

# Promotions
mcp.tool()(promotions.create_activity)
mcp.tool()(promotions.update_activity_product)

# Returns/Refunds/Cancellations
mcp.tool()(returns.search_returns)
mcp.tool()(returns.search_cancellations)

# Customer Service
mcp.tool()(customer_service.get_conversations)
mcp.tool()(customer_service.send_message)
