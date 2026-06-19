from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.ebay_client import EbayClient
from generated_tools.inventory import InventoryTools
from generated_tools.fulfillment import FulfillmentTools
from generated_tools.account import AccountTools
from generated_tools.marketing import MarketingTools
from generated_tools.finances import FinancesTools
from generated_tools.feed import FeedTools


mcp = FastMCP("ebay-sell")

_client = EbayClient()
_inventory = InventoryTools(_client)
_fulfillment = FulfillmentTools(_client)
_account = AccountTools(_client)
_marketing = MarketingTools(_client)
_finances = FinancesTools(_client)
_feed = FeedTools(_client)


# Inventory
@mcp.tool()
def get_inventory_item(sku: str) -> Dict[str, Any]:
    return _inventory.get_inventory_item(sku)


@mcp.tool()
def create_or_replace_inventory_item(sku: str, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    return _inventory.create_or_replace_inventory_item(sku, inventory_item)


@mcp.tool()
def delete_inventory_item(sku: str) -> Dict[str, Any]:
    return _inventory.delete_inventory_item(sku)


@mcp.tool()
def bulk_get_inventory_item(requests: Dict[str, Any]) -> Dict[str, Any]:
    return _inventory.bulk_get_inventory_item(requests)


@mcp.tool()
def bulk_create_or_replace_inventory_item(requests: Dict[str, Any]) -> Dict[str, Any]:
    return _inventory.bulk_create_or_replace_inventory_item(requests)


@mcp.tool()
def get_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    return _inventory.get_inventory_item_group(inventory_item_group_key)


@mcp.tool()
def create_or_replace_inventory_item_group(inventory_item_group_key: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return _inventory.create_or_replace_inventory_item_group(inventory_item_group_key, body)


@mcp.tool()
def delete_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    return _inventory.delete_inventory_item_group(inventory_item_group_key)


@mcp.tool()
def get_offer(offer_id: str) -> Dict[str, Any]:
    return _inventory.get_offer(offer_id)


@mcp.tool()
def create_offer(offer: Dict[str, Any]) -> Dict[str, Any]:
    return _inventory.create_offer(offer)


@mcp.tool()
def update_offer(offer_id: str, offer_patch: Dict[str, Any]) -> Dict[str, Any]:
    return _inventory.update_offer(offer_id, offer_patch)


@mcp.tool()
def publish_offer(offer_id: str) -> Dict[str, Any]:
    return _inventory.publish_offer(offer_id)


@mcp.tool()
def withdraw_offer(offer_id: str) -> Dict[str, Any]:
    return _inventory.withdraw_offer(offer_id)


@mcp.tool()
def delete_offer(offer_id: str) -> Dict[str, Any]:
    return _inventory.delete_offer(offer_id)


@mcp.tool()
def get_offers(sku: Optional[str] = None, marketplace_id: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return _inventory.get_offers(sku=sku, marketplace_id=marketplace_id, limit=limit, offset=offset)


@mcp.tool()
def get_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return _inventory.get_inventory_location(merchant_location_key)


@mcp.tool()
def create_inventory_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    return _inventory.create_inventory_location(merchant_location_key, location)


@mcp.tool()
def update_inventory_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    return _inventory.update_inventory_location(merchant_location_key, location)


@mcp.tool()
def delete_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return _inventory.delete_inventory_location(merchant_location_key)


@mcp.tool()
def get_inventory_locations(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return _inventory.get_inventory_locations(limit=limit, offset=offset)


# Fulfillment
@mcp.tool()
def get_orders(filter: Optional[str] = None, limit: int = 50, offset: int = 0, sort: Optional[str] = None) -> Dict[str, Any]:
    return _fulfillment.get_orders(filter=filter, limit=limit, offset=offset, sort=sort)


@mcp.tool()
def get_order(order_id: str) -> Dict[str, Any]:
    return _fulfillment.get_order(order_id)


@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    return _fulfillment.get_shipping_fulfillments(order_id)


@mcp.tool()
def create_shipping_fulfillment(order_id: str, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    return _fulfillment.create_shipping_fulfillment(order_id, fulfillment)


# Account
@mcp.tool()
def get_fulfillment_policies(marketplace_id: str) -> Dict[str, Any]:
    return _account.get_fulfillment_policies(marketplace_id)


@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    return _account.get_fulfillment_policy(fulfillment_policy_id)


@mcp.tool()
def create_fulfillment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return _account.create_fulfillment_policy(policy)


@mcp.tool()
def update_fulfillment_policy(fulfillment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return _account.update_fulfillment_policy(fulfillment_policy_id, policy)


@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    return _account.delete_fulfillment_policy(fulfillment_policy_id)


@mcp.tool()
def get_payment_policies(marketplace_id: str) -> Dict[str, Any]:
    return _account.get_payment_policies(marketplace_id)


@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    return _account.get_payment_policy(payment_policy_id)


@mcp.tool()
def create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return _account.create_payment_policy(policy)


@mcp.tool()
def update_payment_policy(payment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return _account.update_payment_policy(payment_policy_id, policy)


@mcp.tool()
def delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    return _account.delete_payment_policy(payment_policy_id)


@mcp.tool()
def get_return_policies(marketplace_id: str) -> Dict[str, Any]:
    return _account.get_return_policies(marketplace_id)


@mcp.tool()
def get_return_policy(return_policy_id: str) -> Dict[str, Any]:
    return _account.get_return_policy(return_policy_id)


@mcp.tool()
def create_return_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return _account.create_return_policy(policy)


@mcp.tool()
def update_return_policy(return_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return _account.update_return_policy(return_policy_id, policy)


@mcp.tool()
def delete_return_policy(return_policy_id: str) -> Dict[str, Any]:
    return _account.delete_return_policy(return_policy_id)


@mcp.tool()
def get_sales_taxes(marketplace_id: str) -> Dict[str, Any]:
    return _account.get_sales_taxes(marketplace_id)


@mcp.tool()
def get_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    return _account.get_sales_tax(country_code, jurisdiction_id)


@mcp.tool()
def create_or_replace_sales_tax(country_code: str, jurisdiction_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return _account.create_or_replace_sales_tax(country_code, jurisdiction_id, body)


@mcp.tool()
def delete_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    return _account.delete_sales_tax(country_code, jurisdiction_id)


# Marketing
@mcp.tool()
def get_campaigns(marketplace_id: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return _marketing.get_campaigns(marketplace_id=marketplace_id, limit=limit, offset=offset)


@mcp.tool()
def get_campaign(campaign_id: str) -> Dict[str, Any]:
    return _marketing.get_campaign(campaign_id)


@mcp.tool()
def create_campaign(campaign: Dict[str, Any]) -> Dict[str, Any]:
    return _marketing.create_campaign(campaign)


@mcp.tool()
def update_campaign(campaign_id: str, campaign: Dict[str, Any]) -> Dict[str, Any]:
    return _marketing.update_campaign(campaign_id, campaign)


@mcp.tool()
def delete_campaign(campaign_id: str) -> Dict[str, Any]:
    return _marketing.delete_campaign(campaign_id)


@mcp.tool()
def get_ad_report_task(report_task_id: str) -> Dict[str, Any]:
    return _marketing.get_ad_report_task(report_task_id)


# Finances
@mcp.tool()
def get_transactions(filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return _finances.get_transactions(filter=filter, limit=limit, offset=offset)


@mcp.tool()
def get_payouts(filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return _finances.get_payouts(filter=filter, limit=limit, offset=offset)


@mcp.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    return _finances.get_payout(payout_id)


# Feed
@mcp.tool()
def create_upload_job(job: Dict[str, Any]) -> Dict[str, Any]:
    return _feed.create_upload_job(job)


@mcp.tool()
def get_upload_job(upload_job_id: str) -> Dict[str, Any]:
    return _feed.get_upload_job(upload_job_id)


@mcp.tool()
def get_upload_jobs(feed_type: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return _feed.get_upload_jobs(feed_type=feed_type, limit=limit, offset=offset)


@mcp.tool()
def create_download_job(job: Dict[str, Any]) -> Dict[str, Any]:
    return _feed.create_download_job(job)


@mcp.tool()
def get_download_job(download_job_id: str) -> Dict[str, Any]:
    return _feed.get_download_job(download_job_id)


@mcp.tool()
def get_download_jobs(feed_type: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return _feed.get_download_jobs(feed_type=feed_type, limit=limit, offset=offset)


if __name__ == "__main__":
    mcp.run()
