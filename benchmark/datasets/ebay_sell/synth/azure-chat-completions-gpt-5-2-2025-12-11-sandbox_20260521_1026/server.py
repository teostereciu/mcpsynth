from mcp.server.fastmcp import FastMCP

from generated_tools.account import (
    create_fulfillment_policy,
    create_payment_policy,
    create_return_policy,
    get_fulfillment_policies,
    get_payment_policies,
    get_return_policies,
)
from generated_tools.feed import (
    create_inventory_task,
    get_inventory_task,
    get_inventory_tasks,
    get_task,
    get_tasks,
)
from generated_tools.finances import get_payout, get_payouts, get_transactions
from generated_tools.fulfillment import create_shipping_fulfillment, get_order, get_orders, issue_refund
from generated_tools.inventory import (
    create_offer,
    create_or_replace_inventory_item,
    delete_inventory_item,
    get_inventory_item,
    get_inventory_items,
    get_offer,
    publish_offer,
    update_offer,
)
from generated_tools.marketing import create_ad_by_listing_id, delete_campaign, get_campaign, get_campaigns

mcp = FastMCP("ebay-sell")


# Inventory
mcp.tool()(get_inventory_item)
mcp.tool()(get_inventory_items)
mcp.tool()(create_or_replace_inventory_item)
mcp.tool()(delete_inventory_item)

mcp.tool()(create_offer)
mcp.tool()(get_offer)
mcp.tool()(update_offer)
mcp.tool()(publish_offer)

# Account
mcp.tool()(get_payment_policies)
mcp.tool()(create_payment_policy)
mcp.tool()(get_fulfillment_policies)
mcp.tool()(create_fulfillment_policy)
mcp.tool()(get_return_policies)
mcp.tool()(create_return_policy)

# Fulfillment
mcp.tool()(get_orders)
mcp.tool()(get_order)
mcp.tool()(create_shipping_fulfillment)
mcp.tool()(issue_refund)

# Finances
mcp.tool()(get_transactions)
mcp.tool()(get_payouts)
mcp.tool()(get_payout)

# Feed
mcp.tool()(create_inventory_task)
mcp.tool()(get_inventory_task)
mcp.tool()(get_inventory_tasks)
mcp.tool()(get_task)
mcp.tool()(get_tasks)

# Marketing
mcp.tool()(get_campaigns)
mcp.tool()(get_campaign)
mcp.tool()(create_ad_by_listing_id)
mcp.tool()(delete_campaign)


if __name__ == "__main__":
    mcp.run()
