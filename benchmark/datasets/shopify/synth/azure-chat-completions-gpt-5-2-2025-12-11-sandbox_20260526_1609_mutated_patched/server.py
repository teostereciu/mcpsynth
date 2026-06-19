from mcp.server.fastmcp import FastMCP

from generated_tools.customers import (
    count_customers,
    create_customer,
    create_customer_account_activation_url,
    get_customer_orders,
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
from generated_tools.metafields import (
    create_customer_metafield,
    create_order_metafield,
    create_product_metafield,
    delete_metafield,
    get_metafield,
    list_customer_metafields,
    list_order_metafields,
    list_product_metafields,
    update_metafield,
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
from generated_tools.products import (
    count_products,
    create_product,
    delete_product,
    get_product,
    list_products,
    update_product,
)
from generated_tools.webhooks import (
    count_webhooks,
    create_webhook,
    delete_webhook,
    get_webhook,
    list_webhooks,
    update_webhook,
)


mcp = FastMCP("shopify-admin-rest")


# Products
mcp.tool()(list_products)
mcp.tool()(get_product)
mcp.tool()(count_products)
mcp.tool()(create_product)
mcp.tool()(update_product)
mcp.tool()(delete_product)

# Orders
mcp.tool()(list_orders)
mcp.tool()(get_order)
mcp.tool()(count_orders)
mcp.tool()(create_order)
mcp.tool()(update_order)
mcp.tool()(delete_order)
mcp.tool()(cancel_order)
mcp.tool()(close_order)
mcp.tool()(open_order)

# Customers
mcp.tool()(list_customers)
mcp.tool()(search_customers)
mcp.tool()(count_customers)
mcp.tool()(create_customer)
mcp.tool()(update_customer)
mcp.tool()(get_customer_orders)
mcp.tool()(create_customer_account_activation_url)
mcp.tool()(send_customer_invite)

# Inventory levels
mcp.tool()(list_inventory_levels)
mcp.tool()(adjust_inventory_level)
mcp.tool()(set_inventory_level)
mcp.tool()(connect_inventory_level)
mcp.tool()(delete_inventory_level)

# Metafields
mcp.tool()(list_product_metafields)
mcp.tool()(create_product_metafield)
mcp.tool()(list_order_metafields)
mcp.tool()(create_order_metafield)
mcp.tool()(list_customer_metafields)
mcp.tool()(create_customer_metafield)
mcp.tool()(get_metafield)
mcp.tool()(update_metafield)
mcp.tool()(delete_metafield)

# Webhooks
mcp.tool()(list_webhooks)
mcp.tool()(get_webhook)
mcp.tool()(count_webhooks)
mcp.tool()(create_webhook)
mcp.tool()(update_webhook)
mcp.tool()(delete_webhook)


if __name__ == "__main__":
    mcp.run()
