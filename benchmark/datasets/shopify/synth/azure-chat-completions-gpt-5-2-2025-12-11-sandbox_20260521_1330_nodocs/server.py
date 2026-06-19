from mcp.server.fastmcp import FastMCP

from generated_tools import products, orders, customers, inventory, fulfillment, discounts, webhooks, metafields

mcp = FastMCP("shopify-admin-rest")

# Products
mcp.tool()(products.list_products)
mcp.tool()(products.get_product)
mcp.tool()(products.create_product)
mcp.tool()(products.update_product)
mcp.tool()(products.delete_product)
mcp.tool()(products.list_product_variants)
mcp.tool()(products.get_variant)
mcp.tool()(products.update_variant)
mcp.tool()(products.create_product_image)
mcp.tool()(products.list_product_images)
mcp.tool()(products.delete_product_image)

# Orders / Draft orders / Refunds / Transactions
mcp.tool()(orders.list_orders)
mcp.tool()(orders.get_order)
mcp.tool()(orders.update_order)
mcp.tool()(orders.close_order)
mcp.tool()(orders.open_order)
mcp.tool()(orders.cancel_order)
mcp.tool()(orders.list_transactions)
mcp.tool()(orders.create_refund)
mcp.tool()(orders.create_draft_order)
mcp.tool()(orders.get_draft_order)
mcp.tool()(orders.complete_draft_order)

# Customers
mcp.tool()(customers.list_customers)
mcp.tool()(customers.search_customers)
mcp.tool()(customers.get_customer)
mcp.tool()(customers.create_customer)
mcp.tool()(customers.update_customer)
mcp.tool()(customers.delete_customer)
mcp.tool()(customers.list_customer_orders)
mcp.tool()(customers.create_customer_address)
mcp.tool()(customers.update_customer_address)
mcp.tool()(customers.delete_customer_address)

# Inventory
mcp.tool()(inventory.list_inventory_items)
mcp.tool()(inventory.get_inventory_item)
mcp.tool()(inventory.update_inventory_item)
mcp.tool()(inventory.list_inventory_levels)
mcp.tool()(inventory.adjust_inventory_level)
mcp.tool()(inventory.set_inventory_level)
mcp.tool()(inventory.connect_inventory_level)

# Fulfillment / Locations
mcp.tool()(fulfillment.list_locations)
mcp.tool()(fulfillment.list_fulfillment_orders)
mcp.tool()(fulfillment.get_fulfillment_order)
mcp.tool()(fulfillment.move_fulfillment_order)
mcp.tool()(fulfillment.cancel_fulfillment_order)
mcp.tool()(fulfillment.create_fulfillment)
mcp.tool()(fulfillment.get_fulfillment)
mcp.tool()(fulfillment.update_fulfillment)
mcp.tool()(fulfillment.cancel_fulfillment)

# Discounts
mcp.tool()(discounts.list_price_rules)
mcp.tool()(discounts.get_price_rule)
mcp.tool()(discounts.create_price_rule)
mcp.tool()(discounts.update_price_rule)
mcp.tool()(discounts.delete_price_rule)
mcp.tool()(discounts.list_discount_codes)
mcp.tool()(discounts.create_discount_code)
mcp.tool()(discounts.delete_discount_code)

# Webhooks
mcp.tool()(webhooks.list_webhooks)
mcp.tool()(webhooks.get_webhook)
mcp.tool()(webhooks.create_webhook)
mcp.tool()(webhooks.update_webhook)
mcp.tool()(webhooks.delete_webhook)

# Metafields
mcp.tool()(metafields.list_metafields)
mcp.tool()(metafields.get_metafield)
mcp.tool()(metafields.create_metafield)
mcp.tool()(metafields.update_metafield)
mcp.tool()(metafields.delete_metafield)
mcp.tool()(metafields.list_metafield_definitions)


if __name__ == "__main__":
    mcp.run()
