from mcp.server.fastmcp import FastMCP

from generated_tools import (
    customers,
    discounts,
    draft_orders,
    fulfillment_orders,
    inventory,
    locations,
    metafields,
    orders,
    products,
    webhooks,
)

mcp = FastMCP("shopify-admin-rest")

# Products
mcp.tool()(products.product_create)
mcp.tool()(products.products_list)
mcp.tool()(products.product_get)
mcp.tool()(products.products_count)
mcp.tool()(products.product_update)
mcp.tool()(products.product_delete)

# Orders
mcp.tool()(orders.order_create)
mcp.tool()(orders.orders_list)
mcp.tool()(orders.order_get)
mcp.tool()(orders.orders_count)
mcp.tool()(orders.order_update)
mcp.tool()(orders.order_delete)
mcp.tool()(orders.order_cancel)
mcp.tool()(orders.order_close)
mcp.tool()(orders.order_open)

# Customers
mcp.tool()(customers.customer_create)
mcp.tool()(customers.customers_list)
mcp.tool()(customers.customers_count)
mcp.tool()(customers.customers_search)
mcp.tool()(customers.customer_update)
mcp.tool()(customers.customer_orders_list)
mcp.tool()(customers.customer_account_activation_url)
mcp.tool()(customers.customer_send_invite)

# Draft orders
mcp.tool()(draft_orders.draft_order_create)
mcp.tool()(draft_orders.draft_orders_list)
mcp.tool()(draft_orders.draft_order_get)
mcp.tool()(draft_orders.draft_orders_count)
mcp.tool()(draft_orders.draft_order_update)
mcp.tool()(draft_orders.draft_order_delete)
mcp.tool()(draft_orders.draft_order_complete)
mcp.tool()(draft_orders.draft_order_send_invoice)

# Inventory
mcp.tool()(inventory.inventory_items_list)
mcp.tool()(inventory.inventory_item_get)
mcp.tool()(inventory.inventory_item_update)
mcp.tool()(inventory.inventory_levels_list)
mcp.tool()(inventory.inventory_levels_adjust)
mcp.tool()(inventory.inventory_levels_set)
mcp.tool()(inventory.inventory_levels_connect)
mcp.tool()(inventory.inventory_levels_delete)

# Locations
mcp.tool()(locations.locations_list)
mcp.tool()(locations.locations_count)
mcp.tool()(locations.location_get)
mcp.tool()(locations.location_inventory_levels)

# Fulfillment orders
mcp.tool()(fulfillment_orders.fulfillment_orders_list_by_order)
mcp.tool()(fulfillment_orders.fulfillment_order_get)
mcp.tool()(fulfillment_orders.fulfillment_order_cancel)
mcp.tool()(fulfillment_orders.fulfillment_order_close)
mcp.tool()(fulfillment_orders.fulfillment_order_open)
mcp.tool()(fulfillment_orders.fulfillment_order_hold)
mcp.tool()(fulfillment_orders.fulfillment_order_release_hold)
mcp.tool()(fulfillment_orders.fulfillment_order_move)
mcp.tool()(fulfillment_orders.fulfillment_order_reschedule)
mcp.tool()(fulfillment_orders.fulfillment_orders_set_deadline)

# Discounts
mcp.tool()(discounts.price_rule_create)
mcp.tool()(discounts.price_rules_list)
mcp.tool()(discounts.price_rule_get)
mcp.tool()(discounts.price_rules_count)
mcp.tool()(discounts.price_rule_update)
mcp.tool()(discounts.price_rule_delete)
mcp.tool()(discounts.discount_code_create)
mcp.tool()(discounts.discount_codes_list)
mcp.tool()(discounts.discount_code_get)
mcp.tool()(discounts.discount_code_update)
mcp.tool()(discounts.discount_code_delete)
mcp.tool()(discounts.discount_codes_count)
mcp.tool()(discounts.discount_code_lookup)
mcp.tool()(discounts.discount_code_batch_create)
mcp.tool()(discounts.discount_code_batch_get)
mcp.tool()(discounts.discount_code_batch_codes_list)

# Webhooks
mcp.tool()(webhooks.webhook_create)
mcp.tool()(webhooks.webhooks_list)
mcp.tool()(webhooks.webhook_get)
mcp.tool()(webhooks.webhooks_count)
mcp.tool()(webhooks.webhook_update)
mcp.tool()(webhooks.webhook_delete)

# Metafields (generic)
mcp.tool()(metafields.metafield_create)
mcp.tool()(metafields.metafields_list)
mcp.tool()(metafields.metafield_get)
mcp.tool()(metafields.metafields_count)
mcp.tool()(metafields.metafield_update)
mcp.tool()(metafields.metafield_delete)


if __name__ == "__main__":
    mcp.run()
