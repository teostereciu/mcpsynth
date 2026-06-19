from mcp.server.fastmcp import FastMCP

from generated_tools import (
    customers,
    discounts,
    draft_orders,
    fulfillment_orders,
    fulfillments,
    inventory_levels,
    locations,
    metafields,
    orders,
    products,
    refunds,
    transactions,
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

mcp.tool()(products.product_variant_create)
mcp.tool()(products.product_variants_list)
mcp.tool()(products.product_variants_count)
mcp.tool()(products.product_variant_get)
mcp.tool()(products.product_variant_update)
mcp.tool()(products.product_variant_delete)

mcp.tool()(products.product_image_create)
mcp.tool()(products.product_images_list)
mcp.tool()(products.product_images_count)
mcp.tool()(products.product_image_get)
mcp.tool()(products.product_image_update)
mcp.tool()(products.product_image_delete)


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


# Inventory + Locations
mcp.tool()(locations.locations_list)
mcp.tool()(locations.location_get)
mcp.tool()(locations.locations_count)
mcp.tool()(locations.location_inventory_levels)

mcp.tool()(inventory_levels.inventory_levels_list)
mcp.tool()(inventory_levels.inventory_levels_adjust)
mcp.tool()(inventory_levels.inventory_levels_set)
mcp.tool()(inventory_levels.inventory_levels_connect)
mcp.tool()(inventory_levels.inventory_levels_delete)


# Fulfillment
mcp.tool()(fulfillment_orders.fulfillment_orders_list)
mcp.tool()(fulfillment_orders.fulfillment_order_get)
mcp.tool()(fulfillment_orders.fulfillment_order_cancel)
mcp.tool()(fulfillment_orders.fulfillment_order_close)
mcp.tool()(fulfillment_orders.fulfillment_order_open)
mcp.tool()(fulfillment_orders.fulfillment_order_hold)
mcp.tool()(fulfillment_orders.fulfillment_order_release_hold)
mcp.tool()(fulfillment_orders.fulfillment_order_move)
mcp.tool()(fulfillment_orders.fulfillment_order_reschedule)
mcp.tool()(fulfillment_orders.fulfillment_orders_set_deadline)

mcp.tool()(fulfillments.fulfillment_create)
mcp.tool()(fulfillments.fulfillments_list_for_order)
mcp.tool()(fulfillments.fulfillments_count_for_order)
mcp.tool()(fulfillments.fulfillment_get)
mcp.tool()(fulfillments.fulfillments_list_for_fulfillment_order)
mcp.tool()(fulfillments.fulfillment_cancel)
mcp.tool()(fulfillments.fulfillment_update_tracking)


# Refunds + Transactions
mcp.tool()(refunds.refunds_list)
mcp.tool()(refunds.refund_get)
mcp.tool()(refunds.refund_calculate)
mcp.tool()(refunds.refund_create)

mcp.tool()(transactions.transactions_list)
mcp.tool()(transactions.transactions_count)
mcp.tool()(transactions.transaction_get)
mcp.tool()(transactions.transaction_create)


# Draft orders
mcp.tool()(draft_orders.draft_order_create)
mcp.tool()(draft_orders.draft_orders_list)
mcp.tool()(draft_orders.draft_order_get)
mcp.tool()(draft_orders.draft_orders_count)
mcp.tool()(draft_orders.draft_order_update)
mcp.tool()(draft_orders.draft_order_delete)
mcp.tool()(draft_orders.draft_order_complete)
mcp.tool()(draft_orders.draft_order_send_invoice)


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
