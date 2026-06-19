from mcp.server.fastmcp import FastMCP

from generated_tools.products import (
    count_products,
    create_product,
    delete_product,
    get_product,
    list_products,
    update_product,
)
from generated_tools.variants import (
    count_variants,
    create_variant,
    delete_variant,
    get_variant,
    list_variants,
    update_variant,
)
from generated_tools.orders import (
    cancel_order,
    close_order,
    count_orders,
    create_order,
    delete_order,
    get_order,
    list_orders,
    open_order,
    update_order,
)
from generated_tools.customers import (
    count_customers,
    create_customer,
    create_customer_account_activation_url,
    customer_orders,
    get_customer,
    list_customers,
    search_customers,
    send_customer_invite,
    update_customer,
)
from generated_tools.inventory_levels import (
    adjust_inventory_level,
    connect_inventory_level,
    delete_inventory_level,
    list_inventory_levels,
    set_inventory_level,
)
from generated_tools.locations import (
    count_locations,
    get_location,
    list_locations,
    location_inventory_levels,
)
from generated_tools.webhooks import (
    count_webhooks,
    create_webhook,
    delete_webhook,
    get_webhook,
    list_webhooks,
    update_webhook,
)
from generated_tools.metafields import (
    count_metafields,
    create_metafield,
    delete_metafield,
    get_metafield,
    list_metafields,
    update_metafield,
)

mcp = FastMCP("shopify-admin-rest")

# Products
mcp.tool()(create_product)
mcp.tool()(list_products)
mcp.tool()(get_product)
mcp.tool()(count_products)
mcp.tool()(update_product)
mcp.tool()(delete_product)

# Variants
mcp.tool()(create_variant)
mcp.tool()(list_variants)
mcp.tool()(count_variants)
mcp.tool()(get_variant)
mcp.tool()(update_variant)
mcp.tool()(delete_variant)

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
mcp.tool()(get_customer)
mcp.tool()(count_customers)
mcp.tool()(search_customers)
mcp.tool()(update_customer)
mcp.tool()(customer_orders)
mcp.tool()(create_customer_account_activation_url)
mcp.tool()(send_customer_invite)

# Inventory levels
mcp.tool()(list_inventory_levels)
mcp.tool()(adjust_inventory_level)
mcp.tool()(set_inventory_level)
mcp.tool()(connect_inventory_level)
mcp.tool()(delete_inventory_level)

# Locations
mcp.tool()(list_locations)
mcp.tool()(get_location)
mcp.tool()(count_locations)
mcp.tool()(location_inventory_levels)

# Webhooks
mcp.tool()(create_webhook)
mcp.tool()(list_webhooks)
mcp.tool()(get_webhook)
mcp.tool()(count_webhooks)
mcp.tool()(update_webhook)
mcp.tool()(delete_webhook)

# Metafields (generic resource path)
mcp.tool()(create_metafield)
mcp.tool()(list_metafields)
mcp.tool()(get_metafield)
mcp.tool()(count_metafields)
mcp.tool()(update_metafield)
mcp.tool()(delete_metafield)


if __name__ == "__main__":
    mcp.run()
