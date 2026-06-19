from mcp.server.fastmcp import FastMCP

from generated_tools import account, feed, finances, fulfillment, inventory, marketing


mcp = FastMCP("ebay-sell")

# Inventory
mcp.tool()(inventory.inventory_get_inventory_item)
mcp.tool()(inventory.inventory_create_or_replace_inventory_item)
mcp.tool()(inventory.inventory_delete_inventory_item)
mcp.tool()(inventory.inventory_bulk_create_or_replace_inventory_item)
mcp.tool()(inventory.inventory_get_offers)
mcp.tool()(inventory.inventory_get_offer)
mcp.tool()(inventory.inventory_create_offer)
mcp.tool()(inventory.inventory_update_offer)
mcp.tool()(inventory.inventory_delete_offer)
mcp.tool()(inventory.inventory_publish_offer)
mcp.tool()(inventory.inventory_withdraw_offer)
mcp.tool()(inventory.inventory_get_locations)
mcp.tool()(inventory.inventory_get_location)
mcp.tool()(inventory.inventory_create_or_replace_location)
mcp.tool()(inventory.inventory_delete_location)

# Fulfillment
mcp.tool()(fulfillment.fulfillment_get_orders)
mcp.tool()(fulfillment.fulfillment_get_order)
mcp.tool()(fulfillment.fulfillment_get_shipping_fulfillments)
mcp.tool()(fulfillment.fulfillment_create_shipping_fulfillment)

# Account
mcp.tool()(account.account_get_sales_tax)
mcp.tool()(account.account_get_sales_taxes)
mcp.tool()(account.account_create_or_replace_sales_tax)
mcp.tool()(account.account_delete_sales_tax)
mcp.tool()(account.account_get_fulfillment_policies)
mcp.tool()(account.account_get_fulfillment_policy)
mcp.tool()(account.account_create_fulfillment_policy)
mcp.tool()(account.account_update_fulfillment_policy)
mcp.tool()(account.account_delete_fulfillment_policy)
mcp.tool()(account.account_get_payment_policies)
mcp.tool()(account.account_get_payment_policy)
mcp.tool()(account.account_create_payment_policy)
mcp.tool()(account.account_update_payment_policy)
mcp.tool()(account.account_delete_payment_policy)
mcp.tool()(account.account_get_return_policies)
mcp.tool()(account.account_get_return_policy)
mcp.tool()(account.account_create_return_policy)
mcp.tool()(account.account_update_return_policy)
mcp.tool()(account.account_delete_return_policy)

# Marketing
mcp.tool()(marketing.marketing_get_campaigns)
mcp.tool()(marketing.marketing_get_campaign)
mcp.tool()(marketing.marketing_create_campaign)
mcp.tool()(marketing.marketing_update_campaign)
mcp.tool()(marketing.marketing_delete_campaign)
mcp.tool()(marketing.marketing_get_promotions)
mcp.tool()(marketing.marketing_get_promotion)
mcp.tool()(marketing.marketing_create_promotion)
mcp.tool()(marketing.marketing_update_promotion)
mcp.tool()(marketing.marketing_delete_promotion)

# Finances
mcp.tool()(finances.finances_get_transactions)
mcp.tool()(finances.finances_get_transaction)
mcp.tool()(finances.finances_get_payouts)
mcp.tool()(finances.finances_get_payout)

# Feed
mcp.tool()(feed.feed_create_task)
mcp.tool()(feed.feed_get_task)
mcp.tool()(feed.feed_get_tasks)
mcp.tool()(feed.feed_get_result_file)


if __name__ == "__main__":
    mcp.run()
