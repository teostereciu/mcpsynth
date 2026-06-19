from mcp.server.fastmcp import FastMCP

from generated_tools.account import (
    account_create_fulfillment_policy,
    account_create_or_replace_sales_tax,
    account_create_payment_policy,
    account_create_return_policy,
    account_create_shipping_policy,
    account_delete_fulfillment_policy,
    account_delete_payment_policy,
    account_delete_return_policy,
    account_delete_sales_tax,
    account_delete_shipping_policy,
    account_get_fulfillment_policies,
    account_get_fulfillment_policy,
    account_get_payment_policies,
    account_get_payment_policy,
    account_get_return_policies,
    account_get_return_policy,
    account_get_sales_tax,
    account_get_sales_taxes,
    account_get_shipping_policies,
    account_get_shipping_policy,
    account_update_fulfillment_policy,
    account_update_payment_policy,
    account_update_return_policy,
    account_update_shipping_policy,
)
from generated_tools.feed import (
    feed_create_task,
    feed_get_task,
    feed_get_task_download_url,
    feed_get_tasks,
)
from generated_tools.finances import (
    finances_get_payout,
    finances_get_payouts,
    finances_get_transaction,
    finances_get_transactions,
)
from generated_tools.fulfillment import (
    fulfillment_create_shipping_fulfillment,
    fulfillment_get_order,
    fulfillment_get_orders,
    fulfillment_get_shipping_fulfillment,
    fulfillment_get_shipping_fulfillments,
)
from generated_tools.inventory import (
    inventory_bulk_create_or_replace_inventory_item,
    inventory_create_offer,
    inventory_create_or_replace_inventory_item,
    inventory_create_or_replace_location,
    inventory_delete_inventory_item,
    inventory_delete_location,
    inventory_delete_offer,
    inventory_get_inventory_item,
    inventory_get_location,
    inventory_get_locations,
    inventory_get_offer,
    inventory_get_offers,
    inventory_publish_offer,
    inventory_update_offer,
    inventory_withdraw_offer,
)
from generated_tools.marketing import (
    marketing_create_campaign,
    marketing_create_promotion,
    marketing_delete_campaign,
    marketing_delete_promotion,
    marketing_get_campaign,
    marketing_get_campaigns,
    marketing_get_promotion,
    marketing_get_promotions,
    marketing_update_campaign,
    marketing_update_promotion,
)


mcp = FastMCP("ebay-sell")

# Inventory
mcp.tool()(inventory_get_inventory_item)
mcp.tool()(inventory_create_or_replace_inventory_item)
mcp.tool()(inventory_delete_inventory_item)
mcp.tool()(inventory_bulk_create_or_replace_inventory_item)
mcp.tool()(inventory_get_offers)
mcp.tool()(inventory_get_offer)
mcp.tool()(inventory_create_offer)
mcp.tool()(inventory_update_offer)
mcp.tool()(inventory_delete_offer)
mcp.tool()(inventory_publish_offer)
mcp.tool()(inventory_withdraw_offer)
mcp.tool()(inventory_get_locations)
mcp.tool()(inventory_get_location)
mcp.tool()(inventory_create_or_replace_location)
mcp.tool()(inventory_delete_location)

# Fulfillment
mcp.tool()(fulfillment_get_orders)
mcp.tool()(fulfillment_get_order)
mcp.tool()(fulfillment_create_shipping_fulfillment)
mcp.tool()(fulfillment_get_shipping_fulfillments)
mcp.tool()(fulfillment_get_shipping_fulfillment)

# Account
mcp.tool()(account_get_sales_taxes)
mcp.tool()(account_get_sales_tax)
mcp.tool()(account_create_or_replace_sales_tax)
mcp.tool()(account_delete_sales_tax)

mcp.tool()(account_get_fulfillment_policies)
mcp.tool()(account_get_fulfillment_policy)
mcp.tool()(account_create_fulfillment_policy)
mcp.tool()(account_update_fulfillment_policy)
mcp.tool()(account_delete_fulfillment_policy)

mcp.tool()(account_get_payment_policies)
mcp.tool()(account_get_payment_policy)
mcp.tool()(account_create_payment_policy)
mcp.tool()(account_update_payment_policy)
mcp.tool()(account_delete_payment_policy)

mcp.tool()(account_get_return_policies)
mcp.tool()(account_get_return_policy)
mcp.tool()(account_create_return_policy)
mcp.tool()(account_update_return_policy)
mcp.tool()(account_delete_return_policy)

mcp.tool()(account_get_shipping_policies)
mcp.tool()(account_get_shipping_policy)
mcp.tool()(account_create_shipping_policy)
mcp.tool()(account_update_shipping_policy)
mcp.tool()(account_delete_shipping_policy)

# Marketing
mcp.tool()(marketing_get_campaigns)
mcp.tool()(marketing_get_campaign)
mcp.tool()(marketing_create_campaign)
mcp.tool()(marketing_update_campaign)
mcp.tool()(marketing_delete_campaign)

mcp.tool()(marketing_get_promotions)
mcp.tool()(marketing_get_promotion)
mcp.tool()(marketing_create_promotion)
mcp.tool()(marketing_update_promotion)
mcp.tool()(marketing_delete_promotion)

# Finances
mcp.tool()(finances_get_transactions)
mcp.tool()(finances_get_transaction)
mcp.tool()(finances_get_payouts)
mcp.tool()(finances_get_payout)

# Feed
mcp.tool()(feed_create_task)
mcp.tool()(feed_get_tasks)
mcp.tool()(feed_get_task)
mcp.tool()(feed_get_task_download_url)


if __name__ == "__main__":
    mcp.run()
