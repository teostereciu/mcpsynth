from mcp.server.fastmcp import FastMCP

from generated_tools.account import (
    create_payment_policy,
    delete_payment_policy,
    get_payment_policies,
    get_payment_policy,
    update_payment_policy,
)
from generated_tools.feed import create_inventory_task, get_inventory_task, get_result_file
from generated_tools.finances import get_transactions
from generated_tools.fulfillment import create_shipping_fulfillment, get_order, get_orders
from generated_tools.inventory import (
    create_offer,
    create_or_replace_inventory_item,
    delete_inventory_item,
    get_inventory_item,
    get_inventory_items,
    get_offer,
    get_offers,
    publish_offer,
    update_offer,
    withdraw_offer,
)

mcp = FastMCP("ebay-sell")


# Inventory
mcp.tool()(create_or_replace_inventory_item)
mcp.tool()(get_inventory_item)
mcp.tool()(get_inventory_items)
mcp.tool()(delete_inventory_item)

mcp.tool()(create_offer)
mcp.tool()(get_offer)
mcp.tool()(get_offers)
mcp.tool()(update_offer)
mcp.tool()(publish_offer)
mcp.tool()(withdraw_offer)

# Fulfillment
mcp.tool()(get_orders)
mcp.tool()(get_order)
mcp.tool()(create_shipping_fulfillment)

# Account
mcp.tool()(get_payment_policies)
mcp.tool()(get_payment_policy)
mcp.tool()(create_payment_policy)
mcp.tool()(update_payment_policy)
mcp.tool()(delete_payment_policy)

# Feed
mcp.tool()(create_inventory_task)
mcp.tool()(get_inventory_task)
mcp.tool()(get_result_file)

# Finances
mcp.tool()(get_transactions)


if __name__ == "__main__":
    mcp.run()
