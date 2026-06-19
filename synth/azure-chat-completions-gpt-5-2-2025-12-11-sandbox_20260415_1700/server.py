from mcp.server.fastmcp import FastMCP

from generated_tools.products import (
    product_create,
    product_delete,
    product_get,
    product_update,
    products_count,
    products_list,
)
from generated_tools.orders import (
    order_cancel,
    order_close,
    order_create,
    order_delete,
    order_get,
    order_open,
    order_update,
    orders_count,
    orders_list,
)
from generated_tools.customers import (
    customer_account_activation_url,
    customer_create,
    customer_orders_list,
    customer_send_invite,
    customer_update,
    customers_count,
    customers_list,
    customers_search,
)
from generated_tools.locations import (
    location_get,
    location_inventory_levels,
    locations_count,
    locations_list,
)
from generated_tools.inventory_levels import (
    inventory_levels_adjust,
    inventory_levels_connect,
    inventory_levels_delete,
    inventory_levels_list,
    inventory_levels_set,
)
from generated_tools.price_rules import (
    price_rule_create,
    price_rule_delete,
    price_rule_get,
    price_rule_update,
    price_rules_count,
    price_rules_list,
)
from generated_tools.discount_codes import (
    discount_code_create,
    discount_code_delete,
    discount_code_get,
    discount_code_lookup,
    discount_code_update,
    discount_codes_batch_create,
    discount_codes_batch_get,
    discount_codes_batch_list_codes,
    discount_codes_count,
    discount_codes_list,
)
from generated_tools.webhooks import (
    webhook_create,
    webhook_delete,
    webhook_get,
    webhook_update,
    webhooks_count,
    webhooks_list,
)
from generated_tools.metafields import (
    metafield_create,
    metafield_delete,
    metafield_get,
    metafield_update,
    metafields_count,
    metafields_list,
)

mcp = FastMCP("shopify-admin-rest")

# Products
mcp.tool()(product_create)
mcp.tool()(products_list)
mcp.tool()(product_get)
mcp.tool()(products_count)
mcp.tool()(product_update)
mcp.tool()(product_delete)

# Orders
mcp.tool()(order_create)
mcp.tool()(orders_list)
mcp.tool()(order_get)
mcp.tool()(orders_count)
mcp.tool()(order_update)
mcp.tool()(order_delete)
mcp.tool()(order_cancel)
mcp.tool()(order_close)
mcp.tool()(order_open)

# Customers
mcp.tool()(customer_create)
mcp.tool()(customers_list)
mcp.tool()(customers_count)
mcp.tool()(customers_search)
mcp.tool()(customer_update)
mcp.tool()(customer_orders_list)
mcp.tool()(customer_account_activation_url)
mcp.tool()(customer_send_invite)

# Locations
mcp.tool()(locations_list)
mcp.tool()(location_get)
mcp.tool()(locations_count)
mcp.tool()(location_inventory_levels)

# Inventory levels
mcp.tool()(inventory_levels_list)
mcp.tool()(inventory_levels_adjust)
mcp.tool()(inventory_levels_set)
mcp.tool()(inventory_levels_connect)
mcp.tool()(inventory_levels_delete)

# Discounts
mcp.tool()(price_rule_create)
mcp.tool()(price_rules_list)
mcp.tool()(price_rule_get)
mcp.tool()(price_rules_count)
mcp.tool()(price_rule_update)
mcp.tool()(price_rule_delete)

mcp.tool()(discount_code_create)
mcp.tool()(discount_codes_list)
mcp.tool()(discount_code_get)
mcp.tool()(discount_code_update)
mcp.tool()(discount_code_delete)
mcp.tool()(discount_codes_count)
mcp.tool()(discount_code_lookup)
mcp.tool()(discount_codes_batch_create)
mcp.tool()(discount_codes_batch_get)
mcp.tool()(discount_codes_batch_list_codes)

# Webhooks
mcp.tool()(webhook_create)
mcp.tool()(webhooks_list)
mcp.tool()(webhook_get)
mcp.tool()(webhooks_count)
mcp.tool()(webhook_update)
mcp.tool()(webhook_delete)

# Metafields
mcp.tool()(metafield_create)
mcp.tool()(metafields_list)
mcp.tool()(metafield_get)
mcp.tool()(metafields_count)
mcp.tool()(metafield_update)
mcp.tool()(metafield_delete)


if __name__ == "__main__":
    mcp.run()
