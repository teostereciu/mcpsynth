from mcp.server.fastmcp import FastMCP

from generated_tools.products import (
    create_product,
    list_products,
    get_product,
    count_products,
    update_product,
    delete_product,
)
from generated_tools.orders import (
    create_order,
    list_orders,
    get_order,
    count_orders,
    update_order,
    delete_order,
    cancel_order,
    close_order,
    open_order,
)
from generated_tools.customers import (
    create_customer,
    list_customers,
    search_customers,
    count_customers,
    update_customer,
    get_customer_orders,
    create_customer_account_activation_url,
    send_customer_invite,
)
from generated_tools.inventory_items import (
    list_inventory_items,
    get_inventory_item,
    update_inventory_item,
)
from generated_tools.inventory_levels import (
    list_inventory_levels,
    adjust_inventory_level,
    set_inventory_level,
    connect_inventory_level,
    delete_inventory_level,
)
from generated_tools.locations import (
    list_locations,
    get_location,
    list_location_inventory_levels,
    count_locations,
)
from generated_tools.webhooks import (
    create_webhook,
    list_webhooks,
    get_webhook,
    count_webhooks,
    update_webhook,
    delete_webhook,
)
from generated_tools.metafields import (
    create_metafield,
    list_metafields,
    get_metafield,
    count_metafields,
    update_metafield,
    delete_metafield,
)
from generated_tools.price_rules import (
    create_price_rule,
    list_price_rules,
    get_price_rule,
    count_price_rules,
    update_price_rule,
    delete_price_rule,
)
from generated_tools.discount_codes import (
    create_discount_code,
    create_discount_code_batch,
    get_discount_code_creation_job,
    list_discount_codes_for_job,
    list_discount_codes,
    get_discount_code,
    update_discount_code,
    delete_discount_code,
    count_discount_codes,
    lookup_discount_code,
)

mcp = FastMCP("shopify-admin-rest")

# Products
mcp.tool()(create_product)
mcp.tool()(list_products)
mcp.tool()(get_product)
mcp.tool()(count_products)
mcp.tool()(update_product)
mcp.tool()(delete_product)

# Orders
mcp.tool()(create_order)
mcp.tool()(list_orders)
mcp.tool()(get_order)
mcp.tool()(count_orders)
mcp.tool()(update_order)
mcp.tool()(delete_order)
mcp.tool()(cancel_order)
mcp.tool()(close_order)
mcp.tool()(open_order)

# Customers
mcp.tool()(create_customer)
mcp.tool()(list_customers)
mcp.tool()(search_customers)
mcp.tool()(count_customers)
mcp.tool()(update_customer)
mcp.tool()(get_customer_orders)
mcp.tool()(create_customer_account_activation_url)
mcp.tool()(send_customer_invite)

# Inventory
mcp.tool()(list_inventory_items)
mcp.tool()(get_inventory_item)
mcp.tool()(update_inventory_item)

mcp.tool()(list_inventory_levels)
mcp.tool()(adjust_inventory_level)
mcp.tool()(set_inventory_level)
mcp.tool()(connect_inventory_level)
mcp.tool()(delete_inventory_level)

# Locations
mcp.tool()(list_locations)
mcp.tool()(get_location)
mcp.tool()(list_location_inventory_levels)
mcp.tool()(count_locations)

# Webhooks
mcp.tool()(create_webhook)
mcp.tool()(list_webhooks)
mcp.tool()(get_webhook)
mcp.tool()(count_webhooks)
mcp.tool()(update_webhook)
mcp.tool()(delete_webhook)

# Metafields
mcp.tool()(create_metafield)
mcp.tool()(list_metafields)
mcp.tool()(get_metafield)
mcp.tool()(count_metafields)
mcp.tool()(update_metafield)
mcp.tool()(delete_metafield)

# Discounts
mcp.tool()(create_price_rule)
mcp.tool()(list_price_rules)
mcp.tool()(get_price_rule)
mcp.tool()(count_price_rules)
mcp.tool()(update_price_rule)
mcp.tool()(delete_price_rule)

mcp.tool()(create_discount_code)
mcp.tool()(create_discount_code_batch)
mcp.tool()(get_discount_code_creation_job)
mcp.tool()(list_discount_codes_for_job)
mcp.tool()(list_discount_codes)
mcp.tool()(get_discount_code)
mcp.tool()(update_discount_code)
mcp.tool()(delete_discount_code)
mcp.tool()(count_discount_codes)
mcp.tool()(lookup_discount_code)


if __name__ == "__main__":
    mcp.run()
