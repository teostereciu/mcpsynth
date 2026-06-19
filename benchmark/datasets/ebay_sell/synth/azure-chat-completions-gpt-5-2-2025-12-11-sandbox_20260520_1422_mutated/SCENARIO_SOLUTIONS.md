# Scenario Solutions

## Environment setup

Set these environment variables:

- `EBAY_ENVIRONMENT`: `SANDBOX` (default) or `PRODUCTION`
- `EBAY_APP_ID`: OAuth client id
- `EBAY_CERT_ID`: OAuth client secret
- `EBAY_REFRESH_TOKEN`: refresh token

Run:

```bash
pip install -r requirements.txt
python server.py
```

## Scenario 1: Create an inventory item and publish an offer

1) Create/replace inventory item:
- Tool: `inventory_create_or_replace_inventory_item`
- Inputs: `seller_sku`, `inventory_item`, `content_language`

2) Create offer:
- Tool: `inventory_create_offer`

3) (Optional) Check listing fees:
- Tool: `inventory_get_listing_fees`

4) Publish offer:
- Tool: `inventory_publish_offer`

## Scenario 2: Retrieve orders and create a shipping fulfillment

1) Search orders:
- Tool: `fulfillment_get_orders`
- Use `filter` like `orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}`

2) Get a specific order:
- Tool: `fulfillment_get_order`

3) Create shipping fulfillment:
- Tool: `fulfillment_create_shipping_fulfillment`

4) Verify fulfillments:
- Tool: `fulfillment_get_shipping_fulfillments`

## Scenario 3: Manage business policies

- Fulfillment policies:
  - `account_get_fulfillment_policies`, `account_create_fulfillment_policy`, `account_update_fulfillment_policy`, `account_delete_fulfillment_policy`
- Payment policies:
  - `account_get_payment_policies`, `account_create_payment_policy`, `account_update_payment_policy`, `account_delete_payment_policy`
- Return policies:
  - `account_get_return_policies`, `account_create_return_policy`, `account_update_return_policy`, `account_delete_return_policy`

## Scenario 4: Marketing campaigns

- List campaigns: `marketing_get_campaigns`
- Get campaign: `marketing_get_campaign`
- Clone campaign: `marketing_clone_campaign`
- Delete campaign: `marketing_delete_campaign`

## Scenario 5: Create and monitor a Feed task

1) Create task:
- Tool: `feed_create_task` (requires `marketplace_id` header)

2) Poll task:
- Tool: `feed_get_task`

3) Retrieve result file:
- Tool: `feed_get_result_file` or `feed_get_latest_result_file`
