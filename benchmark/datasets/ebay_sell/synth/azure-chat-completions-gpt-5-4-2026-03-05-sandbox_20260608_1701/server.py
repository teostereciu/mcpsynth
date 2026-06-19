from mcp.server.fastmcp import FastMCP

from generated_tools.account import create_payment_policy, get_payment_policies
from generated_tools.feed import create_task, get_task
from generated_tools.finances import get_payouts, get_transactions
from generated_tools.fulfillment import get_order, get_orders
from generated_tools.inventory import (
    create_offer,
    create_or_replace_inventory_item,
    get_inventory_item,
    get_offers,
)
from generated_tools.marketing import get_campaign, get_campaigns

mcp = FastMCP("ebay-sell")

mcp.tool()(get_inventory_item)
mcp.tool()(create_or_replace_inventory_item)
mcp.tool()(get_offers)
mcp.tool()(create_offer)

mcp.tool()(get_payment_policies)
mcp.tool()(create_payment_policy)

mcp.tool()(get_orders)
mcp.tool()(get_order)

mcp.tool()(get_transactions)
mcp.tool()(get_payouts)

mcp.tool()(create_task)
mcp.tool()(get_task)

mcp.tool()(get_campaigns)
mcp.tool()(get_campaign)


if __name__ == "__main__":
    mcp.run()
