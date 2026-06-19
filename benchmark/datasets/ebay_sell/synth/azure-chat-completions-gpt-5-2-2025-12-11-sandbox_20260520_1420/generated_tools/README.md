# Generated Tools

This server exposes:

- `ebay_sell_request` (generic): call any documented eBay Sell REST endpoint by specifying `api`, `method`, `path`, and optional query/headers/body.
- Convenience tools for common flows:
  - `inventory_create_or_replace_inventory_item`
  - `inventory_get_inventory_items`
  - `inventory_create_offer`
  - `inventory_update_offer`
  - `inventory_publish_offer`
  - `fulfillment_get_orders`
  - `fulfillment_create_shipping_fulfillment`
  - `account_get_fulfillment_policies`
  - `account_get_payment_policies`
  - `feed_create_task`
  - `marketing_get_campaigns`
  - `finances_get_payouts`

Auth is via `EBAY_OAUTH_TOKEN` environment variable.
