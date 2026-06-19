from mcp.server.fastmcp import FastMCP

from generated_tools import (
    customers,
    discount_codes,
    draft_orders,
    inventory_items,
    inventory_levels,
    locations,
    metafields,
    orders,
    price_rules,
    product_images,
    product_variants,
    products,
    webhooks,
)

mcp = FastMCP("shopify-admin-rest")


# Products
mcp.tool()(products.create_product)
mcp.tool()(products.list_products)
mcp.tool()(products.get_product)
mcp.tool()(products.count_products)
mcp.tool()(products.update_product)
mcp.tool()(products.delete_product)

# Product variants
mcp.tool()(product_variants.create_product_variant)
mcp.tool()(product_variants.list_product_variants)
mcp.tool()(product_variants.count_product_variants)
mcp.tool()(product_variants.get_variant)
mcp.tool()(product_variants.update_variant)
mcp.tool()(product_variants.delete_product_variant)

# Product images
mcp.tool()(product_images.create_product_image)
mcp.tool()(product_images.list_product_images)
mcp.tool()(product_images.get_product_image)
mcp.tool()(product_images.count_product_images)
mcp.tool()(product_images.update_product_image)
mcp.tool()(product_images.delete_product_image)

# Orders
mcp.tool()(orders.create_order)
mcp.tool()(orders.list_orders)
mcp.tool()(orders.get_order)
mcp.tool()(orders.count_orders)
mcp.tool()(orders.update_order)
mcp.tool()(orders.delete_order)
mcp.tool()(orders.cancel_order)
mcp.tool()(orders.close_order)
mcp.tool()(orders.open_order)

# Draft orders
mcp.tool()(draft_orders.create_draft_order)
mcp.tool()(draft_orders.list_draft_orders)
mcp.tool()(draft_orders.get_draft_order)
mcp.tool()(draft_orders.count_draft_orders)
mcp.tool()(draft_orders.update_draft_order)
mcp.tool()(draft_orders.delete_draft_order)
mcp.tool()(draft_orders.complete_draft_order)
mcp.tool()(draft_orders.send_draft_order_invoice)

# Customers
mcp.tool()(customers.create_customer)
mcp.tool()(customers.list_customers)
mcp.tool()(customers.count_customers)
mcp.tool()(customers.search_customers)
mcp.tool()(customers.update_customer)
mcp.tool()(customers.get_customer_orders)
mcp.tool()(customers.create_customer_account_activation_url)
mcp.tool()(customers.send_customer_invite)

# Inventory
mcp.tool()(inventory_items.list_inventory_items)
mcp.tool()(inventory_items.get_inventory_item)
mcp.tool()(inventory_items.update_inventory_item)

mcp.tool()(inventory_levels.list_inventory_levels)
mcp.tool()(inventory_levels.adjust_inventory_level)
mcp.tool()(inventory_levels.set_inventory_level)
mcp.tool()(inventory_levels.connect_inventory_level)
mcp.tool()(inventory_levels.delete_inventory_level)

# Locations
mcp.tool()(locations.list_locations)
mcp.tool()(locations.get_location)
mcp.tool()(locations.count_locations)
mcp.tool()(locations.list_location_inventory_levels)

# Discounts
mcp.tool()(price_rules.create_price_rule)
mcp.tool()(price_rules.list_price_rules)
mcp.tool()(price_rules.get_price_rule)
mcp.tool()(price_rules.count_price_rules)
mcp.tool()(price_rules.update_price_rule)
mcp.tool()(price_rules.delete_price_rule)

mcp.tool()(discount_codes.create_discount_code)
mcp.tool()(discount_codes.list_discount_codes)
mcp.tool()(discount_codes.get_discount_code)
mcp.tool()(discount_codes.update_discount_code)
mcp.tool()(discount_codes.delete_discount_code)
mcp.tool()(discount_codes.create_discount_code_batch)
mcp.tool()(discount_codes.get_discount_code_batch)
mcp.tool()(discount_codes.list_discount_codes_for_batch)
mcp.tool()(discount_codes.count_discount_codes)
mcp.tool()(discount_codes.lookup_discount_code)

# Webhooks
mcp.tool()(webhooks.create_webhook)
mcp.tool()(webhooks.list_webhooks)
mcp.tool()(webhooks.get_webhook)
mcp.tool()(webhooks.count_webhooks)
mcp.tool()(webhooks.update_webhook)
mcp.tool()(webhooks.delete_webhook)

# Metafields (generic)
mcp.tool()(metafields.create_metafield)
mcp.tool()(metafields.list_metafields)
mcp.tool()(metafields.get_metafield)
mcp.tool()(metafields.count_metafields)
mcp.tool()(metafields.update_metafield)
mcp.tool()(metafields.delete_metafield)


if __name__ == "__main__":
    mcp.run()
