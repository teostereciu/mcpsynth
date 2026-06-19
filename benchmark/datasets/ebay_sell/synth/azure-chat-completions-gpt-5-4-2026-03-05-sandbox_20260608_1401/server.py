from mcp.server.fastmcp import FastMCP

from generated_tools.account import (
    create_fulfillment_policy,
    create_payment_policy,
    get_fulfillment_policies,
    get_payment_policies,
)
from generated_tools.feed import create_task, get_result_file, get_task, get_tasks
from generated_tools.finances import get_payouts, get_transactions
from generated_tools.fulfillment import (
    create_shipping_fulfillment,
    get_order,
    get_orders,
    get_shipping_fulfillments,
)
from generated_tools.inventory import (
    create_offer,
    create_or_replace_inventory_item,
    get_inventory_item,
    get_inventory_items,
    get_offer,
    publish_offer,
)
from generated_tools.marketing import (
    bulk_create_ads_by_listing_id,
    create_ad_by_listing_id,
    get_campaigns,
)

mcp = FastMCP("ebay-sell")

mcp.tool()(get_inventory_item)
mcp.tool()(create_or_replace_inventory_item)
mcp.tool()(get_inventory_items)
mcp.tool()(create_offer)
mcp.tool()(get_offer)
mcp.tool()(publish_offer)

mcp.tool()(get_fulfillment_policies)
mcp.tool()(create_fulfillment_policy)
mcp.tool()(get_payment_policies)
mcp.tool()(create_payment_policy)

mcp.tool()(get_orders)
mcp.tool()(get_order)
mcp.tool()(create_shipping_fulfillment)
mcp.tool()(get_shipping_fulfillments)

mcp.tool()(get_transactions)
mcp.tool()(get_payouts)

mcp.tool()(get_campaigns)
mcp.tool()(create_ad_by_listing_id)
mcp.tool()(bulk_create_ads_by_listing_id)

mcp.tool()(create_task)
mcp.tool()(get_task)
mcp.tool()(get_tasks)
mcp.tool()(get_result_file)


if __name__ == "__main__":
    mcp.run()
