from mcp.server.fastmcp import FastMCP

from generated_tools import (
    customers,
    discounts,
    draft_orders,
    fulfillment_orders,
    fulfillments,
    inventory,
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
mcp.tool()(products.create_product)
mcp.tool()(products.list_products)
mcp.tool()(products.get_product)
mcp.tool()(products.count_products)
mcp.tool()(products.update_product)
mcp.tool()(products.delete_product)

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

# Customers
mcp.tool()(customers.create_customer)
mcp.tool()(customers.list_customers)
mcp.tool()(customers.get_customer)
mcp.tool()(customers.update_customer)
mcp.tool()(customers.count_customers)
mcp.tool()(customers.search_customers)
mcp.tool()(customers.get_customer_orders)
mcp.tool()(customers.create_customer_account_activation_url)
mcp.tool()(customers.send_customer_invite)

# Inventory + Locations
mcp.tool()(inventory.list_inventory_items)
mcp.tool()(inventory.get_inventory_item)
mcp.tool()(inventory.update_inventory_item)
mcp.tool()(inventory.list_inventory_levels)
mcp.tool()(inventory.adjust_inventory_level)
mcp.tool()(inventory.set_inventory_level)
mcp.tool()(inventory.connect_inventory_level)
mcp.tool()(inventory.delete_inventory_level)

mcp.tool()(locations.list_locations)
mcp.tool()(locations.get_location)
mcp.tool()(locations.count_locations)
mcp.tool()(locations.get_location_inventory_levels)

# Fulfillment Orders + Fulfillments
mcp.tool()(fulfillment_orders.list_fulfillment_orders_for_order)
mcp.tool()(fulfillment_orders.get_fulfillment_order)
mcp.tool()(fulfillment_orders.cancel_fulfillment_order)
mcp.tool()(fulfillment_orders.close_fulfillment_order)
mcp.tool()(fulfillment_orders.open_fulfillment_order)
mcp.tool()(fulfillment_orders.hold_fulfillment_order)
mcp.tool()(fulfillment_orders.release_hold_fulfillment_order)
mcp.tool()(fulfillment_orders.move_fulfillment_order)
mcp.tool()(fulfillment_orders.reschedule_fulfillment_order)
mcp.tool()(fulfillment_orders.set_fulfillment_orders_deadline)

mcp.tool()(fulfillments.create_fulfillment)
mcp.tool()(fulfillments.cancel_fulfillment)
mcp.tool()(fulfillments.update_fulfillment_tracking)
mcp.tool()(fulfillments.list_fulfillments_for_order)
mcp.tool()(fulfillments.get_fulfillment)
mcp.tool()(fulfillments.count_fulfillments_for_order)
mcp.tool()(fulfillments.list_fulfillments_for_fulfillment_order)

# Transactions + Refunds
mcp.tool()(transactions.list_transactions)
mcp.tool()(transactions.get_transaction)
mcp.tool()(transactions.count_transactions)
mcp.tool()(transactions.create_transaction)

mcp.tool()(refunds.list_refunds)
mcp.tool()(refunds.get_refund)
mcp.tool()(refunds.calculate_refund)
mcp.tool()(refunds.create_refund)

# Draft Orders
mcp.tool()(draft_orders.create_draft_order)
mcp.tool()(draft_orders.list_draft_orders)
mcp.tool()(draft_orders.get_draft_order)
mcp.tool()(draft_orders.count_draft_orders)
mcp.tool()(draft_orders.update_draft_order)
mcp.tool()(draft_orders.delete_draft_order)
mcp.tool()(draft_orders.complete_draft_order)
mcp.tool()(draft_orders.send_draft_order_invoice)

# Discounts
mcp.tool()(discounts.create_price_rule)
mcp.tool()(discounts.list_price_rules)
mcp.tool()(discounts.get_price_rule)
mcp.tool()(discounts.count_price_rules)
mcp.tool()(discounts.update_price_rule)
mcp.tool()(discounts.delete_price_rule)
mcp.tool()(discounts.create_discount_code)
mcp.tool()(discounts.list_discount_codes)
mcp.tool()(discounts.get_discount_code)
mcp.tool()(discounts.update_discount_code)
mcp.tool()(discounts.delete_discount_code)
mcp.tool()(discounts.create_discount_code_batch)
mcp.tool()(discounts.get_discount_code_batch)
mcp.tool()(discounts.list_discount_codes_for_batch)
mcp.tool()(discounts.count_discount_codes)
mcp.tool()(discounts.lookup_discount_code)

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
