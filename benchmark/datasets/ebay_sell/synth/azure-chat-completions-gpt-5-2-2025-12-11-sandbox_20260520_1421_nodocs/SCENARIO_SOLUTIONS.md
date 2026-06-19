# Scenario Solutions (eBay Sell MCP Server)

This repository provides an MCP server (`server.py`) exposing named tools for common eBay Sell workflows.

## Scenario 1: Create and publish a new listing (Inventory Item -> Offer -> Publish)

1. Create/replace an inventory item:
   - Tool: `inventory_create_or_replace_inventory_item`
   - Inputs: `sku`, `inventory_item`
2. Create an offer for that SKU:
   - Tool: `inventory_create_offer`
   - Input: `offer` (must reference the SKU and marketplace)
3. Publish the offer:
   - Tool: `inventory_publish_offer`
   - Input: `offer_id`

## Scenario 2: Update price/quantity for an existing offer

1. Fetch offer:
   - Tool: `inventory_get_offer`
2. Patch offer fields (JSON Patch semantics):
   - Tool: `inventory_update_offer`
3. (Optional) Re-publish if required by the change:
   - Tool: `inventory_publish_offer`

## Scenario 3: Manage inventory locations

- Create a location: `inventory_create_inventory_location`
- Get a location: `inventory_get_location`
- Enable/disable: `inventory_enable_inventory_location` / `inventory_disable_inventory_location`

## Scenario 4: Retrieve orders and create shipping fulfillments

1. List orders:
   - Tool: `fulfillment_get_orders` (use `filter` for date ranges/status)
2. Get a specific order:
   - Tool: `fulfillment_get_order`
3. Create shipping fulfillment (tracking, line items):
   - Tool: `fulfillment_create_shipping_fulfillment`
4. Verify fulfillments:
   - Tool: `fulfillment_get_shipping_fulfillments`

## Scenario 5: Configure business policies (Account API)

- Fulfillment policies: `account_get_fulfillment_policies`, `account_create_fulfillment_policy`, `account_update_fulfillment_policy`, `account_delete_fulfillment_policy`
- Payment policies: `account_get_payment_policies`, `account_create_payment_policy`, `account_update_payment_policy`, `account_delete_payment_policy`
- Return policies: `account_get_return_policies`, `account_create_return_policy`, `account_update_return_policy`, `account_delete_return_policy`

## Scenario 6: Run promotions/campaigns (Marketing API)

- Ad campaigns: `marketing_get_campaigns`, `marketing_create_campaign`, `marketing_update_campaign`, `marketing_delete_campaign`
- Item promotions: `marketing_create_item_promotion`, `marketing_get_item_promotion`, `marketing_update_item_promotion`, `marketing_delete_item_promotion`

## Scenario 7: Reconcile payouts and transactions (Finances API)

- List transactions: `finances_get_transactions`
- Get transaction: `finances_get_transaction`
- List payouts: `finances_get_payouts`
- Get payout: `finances_get_payout`

## Scenario 8: Bulk operations via Feed API

1. Create a feed task: `feed_create_task`
2. Poll task status: `feed_get_task`
3. List tasks: `feed_get_tasks`
4. Download result file (if supported by task): `feed_get_result_file`

