from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools import account, feed, finances, fulfillment, inventory, marketing, metadata

mcp = FastMCP("ebay-sell")


# Inventory
@mcp.tool()
def inventory_create_or_replace_inventory_item(
    sku: str,
    inventory_item: Dict[str, Any],
    content_language: str = "en-US",
) -> Dict[str, Any]:
    return inventory.create_or_replace_inventory_item(sku, inventory_item, content_language=content_language)


@mcp.tool()
def inventory_get_inventory_item(sku: str) -> Dict[str, Any]:
    return inventory.get_inventory_item(sku)


@mcp.tool()
def inventory_delete_inventory_item(sku: str) -> Dict[str, Any]:
    return inventory.delete_inventory_item(sku)


@mcp.tool()
def inventory_get_inventory_items(limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return inventory.get_inventory_items(limit=limit, offset=offset)


@mcp.tool()
def inventory_create_inventory_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    return inventory.create_inventory_location(merchant_location_key, location)


@mcp.tool()
def inventory_get_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return inventory.get_inventory_location(merchant_location_key)


@mcp.tool()
def inventory_get_inventory_locations(limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return inventory.get_inventory_locations(limit=limit, offset=offset)


@mcp.tool()
def inventory_update_inventory_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    return inventory.update_inventory_location(merchant_location_key, location)


@mcp.tool()
def inventory_disable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return inventory.disable_inventory_location(merchant_location_key)


@mcp.tool()
def inventory_enable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return inventory.enable_inventory_location(merchant_location_key)


@mcp.tool()
def inventory_create_offer(offer: Dict[str, Any]) -> Dict[str, Any]:
    return inventory.create_offer(offer)


@mcp.tool()
def inventory_get_offer(offer_id: str) -> Dict[str, Any]:
    return inventory.get_offer(offer_id)


@mcp.tool()
def inventory_update_offer(offer_id: str, offer: Dict[str, Any]) -> Dict[str, Any]:
    return inventory.update_offer(offer_id, offer)


@mcp.tool()
def inventory_delete_offer(offer_id: str) -> Dict[str, Any]:
    return inventory.delete_offer(offer_id)


@mcp.tool()
def inventory_get_offers(
    sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return inventory.get_offers(
        sku=sku,
        marketplace_id=marketplace_id,
        format=format,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def inventory_publish_offer(offer_id: str) -> Dict[str, Any]:
    return inventory.publish_offer(offer_id)


@mcp.tool()
def inventory_withdraw_offer(offer_id: str) -> Dict[str, Any]:
    return inventory.withdraw_offer(offer_id)


@mcp.tool()
def inventory_bulk_update_price_quantity(payload: Dict[str, Any]) -> Dict[str, Any]:
    return inventory.bulk_update_price_quantity(payload)


# Fulfillment
@mcp.tool()
def fulfillment_get_orders(
    filter: Optional[str] = None,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return fulfillment.get_orders(
        filter=filter,
        order_ids=order_ids,
        field_groups=field_groups,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def fulfillment_get_order(order_id: str, field_groups: Optional[str] = None) -> Dict[str, Any]:
    return fulfillment.get_order(order_id, field_groups=field_groups)


@mcp.tool()
def fulfillment_create_shipping_fulfillment(order_id: str, fulfillment_payload: Dict[str, Any]) -> Dict[str, Any]:
    return fulfillment.create_shipping_fulfillment(order_id, fulfillment_payload)


@mcp.tool()
def fulfillment_get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    return fulfillment.get_shipping_fulfillments(order_id)


@mcp.tool()
def fulfillment_get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    return fulfillment.get_shipping_fulfillment(order_id, fulfillment_id)


@mcp.tool()
def fulfillment_get_activities(
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return fulfillment.get_activities(filter=filter, limit=limit, offset=offset)


@mcp.tool()
def fulfillment_issue_refund(order_id: str, refund_payload: Dict[str, Any]) -> Dict[str, Any]:
    return fulfillment.issue_refund(order_id, refund_payload)


# Account
@mcp.tool()
def account_get_payment_policies(marketplace_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    return account.get_payment_policies(marketplace_id=marketplace_id, content_language=content_language)


@mcp.tool()
def account_get_payment_policy(payment_policy_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    return account.get_payment_policy(payment_policy_id, content_language=content_language)


@mcp.tool()
def account_create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return account.create_payment_policy(policy)


@mcp.tool()
def account_update_payment_policy(payment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return account.update_payment_policy(payment_policy_id, policy)


@mcp.tool()
def account_delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    return account.delete_payment_policy(payment_policy_id)


@mcp.tool()
def account_get_fulfillment_policies(marketplace_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    return account.get_fulfillment_policies(marketplace_id=marketplace_id, content_language=content_language)


@mcp.tool()
def account_get_fulfillment_policy(fulfillment_policy_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    return account.get_fulfillment_policy(fulfillment_policy_id, content_language=content_language)


@mcp.tool()
def account_create_fulfillment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return account.create_fulfillment_policy(policy)


@mcp.tool()
def account_update_fulfillment_policy(fulfillment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return account.update_fulfillment_policy(fulfillment_policy_id, policy)


@mcp.tool()
def account_delete_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    return account.delete_fulfillment_policy(fulfillment_policy_id)


@mcp.tool()
def account_get_return_policies(marketplace_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    return account.get_return_policies(marketplace_id=marketplace_id, content_language=content_language)


@mcp.tool()
def account_get_return_policy(return_policy_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    return account.get_return_policy(return_policy_id, content_language=content_language)


@mcp.tool()
def account_create_return_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return account.create_return_policy(policy)


@mcp.tool()
def account_update_return_policy(return_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return account.update_return_policy(return_policy_id, policy)


@mcp.tool()
def account_delete_return_policy(return_policy_id: str) -> Dict[str, Any]:
    return account.delete_return_policy(return_policy_id)


@mcp.tool()
def account_get_sales_taxes(marketplace_id: str) -> Dict[str, Any]:
    return account.get_sales_taxes(marketplace_id=marketplace_id)


@mcp.tool()
def account_get_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    return account.get_sales_tax(country_code, jurisdiction_id)


@mcp.tool()
def account_create_or_replace_sales_tax(country_code: str, jurisdiction_id: str, sales_tax: Dict[str, Any]) -> Dict[str, Any]:
    return account.create_or_replace_sales_tax(country_code, jurisdiction_id, sales_tax)


@mcp.tool()
def account_delete_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    return account.delete_sales_tax(country_code, jurisdiction_id)


@mcp.tool()
def account_get_privileges() -> Dict[str, Any]:
    return account.get_privileges()


@mcp.tool()
def account_get_opted_in_programs() -> Dict[str, Any]:
    return account.get_opted_in_programs()


# Feed
@mcp.tool()
def feed_create_task(marketplace_id: str, task: Dict[str, Any], accept_language: Optional[str] = None) -> Dict[str, Any]:
    return feed.create_task(marketplace_id, task, accept_language=accept_language)


@mcp.tool()
def feed_get_task(task_id: str) -> Dict[str, Any]:
    return feed.get_task(task_id)


@mcp.tool()
def feed_get_tasks(feed_type: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return feed.get_tasks(feed_type=feed_type, limit=limit, offset=offset)


@mcp.tool()
def feed_upload_file(task_id: str, content: str, content_type: str = "application/xml") -> Dict[str, Any]:
    return feed.upload_file(task_id, content, content_type=content_type)


# Finances
@mcp.tool()
def finances_get_transactions(filter: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return finances.get_transactions(filter=filter, limit=limit, offset=offset)


@mcp.tool()
def finances_get_transaction_summary(filter: Optional[str] = None) -> Dict[str, Any]:
    return finances.get_transaction_summary(filter=filter)


@mcp.tool()
def finances_get_payouts(filter: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return finances.get_payouts(filter=filter, limit=limit, offset=offset)


@mcp.tool()
def finances_get_payout(payout_id: str) -> Dict[str, Any]:
    return finances.get_payout(payout_id)


@mcp.tool()
def finances_get_payout_summary() -> Dict[str, Any]:
    return finances.get_payout_summary()


# Marketing
@mcp.tool()
def marketing_get_campaigns(campaign_name: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return marketing.get_campaigns(campaign_name=campaign_name, limit=limit, offset=offset)


@mcp.tool()
def marketing_get_campaign(campaign_id: str) -> Dict[str, Any]:
    return marketing.get_campaign(campaign_id)


@mcp.tool()
def marketing_create_ad_group(campaign_id: str, ad_group: Dict[str, Any]) -> Dict[str, Any]:
    return marketing.create_ad_group(campaign_id, ad_group)


@mcp.tool()
def marketing_get_ad_groups(campaign_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return marketing.get_ad_groups(campaign_id, limit=limit, offset=offset)


# Metadata
@mcp.tool()
def metadata_get_currencies() -> Dict[str, Any]:
    return metadata.get_currencies()


@mcp.tool()
def metadata_get_item_condition_policies(marketplace_id: str, category_id: str) -> Dict[str, Any]:
    return metadata.get_item_condition_policies(marketplace_id, category_id)


if __name__ == "__main__":
    mcp.run()
