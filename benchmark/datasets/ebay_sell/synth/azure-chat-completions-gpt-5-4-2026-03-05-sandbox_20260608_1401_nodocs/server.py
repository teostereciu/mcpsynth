from mcp.server.fastmcp import FastMCP

from generated_tools.account import (
    create_fulfillment_policy,
    create_payment_policy,
    create_return_policy,
    delete_fulfillment_policy,
    delete_payment_policy,
    delete_return_policy,
    get_fulfillment_policies,
    get_fulfillment_policy,
    get_payment_policies,
    get_payment_policy,
    get_privileges,
    get_return_policies,
    get_return_policy,
    get_sales_tax,
    update_fulfillment_policy,
    update_payment_policy,
    update_return_policy,
)
from generated_tools.feed import create_task, download_result_file, get_task, get_tasks, upload_file
from generated_tools.finances import get_payout, get_payout_transactions, get_payouts, get_transaction, get_transactions
from generated_tools.fulfillment import (
    create_shipping_fulfillment,
    get_order,
    get_orders,
    get_shipping_fulfillment,
    get_shipping_fulfillments,
    issue_refund,
    update_shipping_fulfillment,
)
from generated_tools.inventory import (
    bulk_get_inventory_item,
    create_inventory_location,
    create_offer,
    create_or_replace_inventory_item,
    delete_inventory_item,
    delete_inventory_location,
    delete_offer,
    get_inventory_item,
    get_inventory_items,
    get_inventory_location,
    get_inventory_locations,
    get_offer,
    get_offers,
    publish_offer,
    update_inventory_location,
    update_offer,
    withdraw_offer,
)
from generated_tools.marketing import create_ads, create_campaign, delete_campaign, get_ads, get_campaign, get_campaigns, update_bids, update_campaign


mcp = FastMCP("ebay-sell")

mcp.tool()(get_inventory_item)
mcp.tool()(create_or_replace_inventory_item)
mcp.tool()(delete_inventory_item)
mcp.tool()(bulk_get_inventory_item)
mcp.tool()(get_inventory_items)
mcp.tool()(create_offer)
mcp.tool()(get_offer)
mcp.tool()(update_offer)
mcp.tool()(delete_offer)
mcp.tool()(publish_offer)
mcp.tool()(withdraw_offer)
mcp.tool()(get_offers)
mcp.tool()(create_inventory_location)
mcp.tool()(get_inventory_location)
mcp.tool()(update_inventory_location)
mcp.tool()(delete_inventory_location)
mcp.tool()(get_inventory_locations)

mcp.tool()(get_orders)
mcp.tool()(get_order)
mcp.tool()(issue_refund)
mcp.tool()(get_shipping_fulfillment)
mcp.tool()(get_shipping_fulfillments)
mcp.tool()(create_shipping_fulfillment)
mcp.tool()(update_shipping_fulfillment)

mcp.tool()(get_payment_policies)
mcp.tool()(get_payment_policy)
mcp.tool()(create_payment_policy)
mcp.tool()(update_payment_policy)
mcp.tool()(delete_payment_policy)
mcp.tool()(get_fulfillment_policies)
mcp.tool()(get_fulfillment_policy)
mcp.tool()(create_fulfillment_policy)
mcp.tool()(update_fulfillment_policy)
mcp.tool()(delete_fulfillment_policy)
mcp.tool()(get_return_policies)
mcp.tool()(get_return_policy)
mcp.tool()(create_return_policy)
mcp.tool()(update_return_policy)
mcp.tool()(delete_return_policy)
mcp.tool()(get_sales_tax)
mcp.tool()(get_privileges)

mcp.tool()(get_campaigns)
mcp.tool()(create_campaign)
mcp.tool()(get_campaign)
mcp.tool()(update_campaign)
mcp.tool()(delete_campaign)
mcp.tool()(get_ads)
mcp.tool()(create_ads)
mcp.tool()(update_bids)

mcp.tool()(get_transactions)
mcp.tool()(get_transaction)
mcp.tool()(get_payouts)
mcp.tool()(get_payout)
mcp.tool()(get_payout_transactions)

mcp.tool()(create_task)
mcp.tool()(get_tasks)
mcp.tool()(get_task)
mcp.tool()(upload_file)
mcp.tool()(download_result_file)


if __name__ == "__main__":
    mcp.run()
