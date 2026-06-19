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
    get_customer_orders,
    count_customers,
    search_customers,
    update_customer,
    create_customer_account_activation_url,
    send_customer_invite,
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
mcp.tool()(get_customer_orders)
mcp.tool()(count_customers)
mcp.tool()(search_customers)
mcp.tool()(update_customer)
mcp.tool()(create_customer_account_activation_url)
mcp.tool()(send_customer_invite)


if __name__ == "__main__":
    mcp.run()
