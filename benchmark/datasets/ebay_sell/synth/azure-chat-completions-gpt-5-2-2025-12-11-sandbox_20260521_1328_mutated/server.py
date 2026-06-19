from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.account import create_payment_policy, get_fulfillment_policies, get_payment_policies
from generated_tools.finances import get_transactions
from generated_tools.fulfillment import create_shipping_fulfillment, get_order, get_orders
from generated_tools.inventory import (
    create_offer,
    create_or_replace_inventory_item,
    get_inventory_item,
    get_inventory_items,
    publish_offer,
)

mcp = FastMCP("ebay-sell")


@mcp.tool()
def inventory_create_or_replace_inventory_item(
    seller_sku: str,
    inventory_item: Dict[str, Any],
    content_language: str = "en-US",
) -> Dict[str, Any]:
    return create_or_replace_inventory_item(
        seller_sku=seller_sku,
        inventory_item=inventory_item,
        content_language=content_language,
    )


@mcp.tool()
def inventory_get_inventory_item(seller_sku: str) -> Dict[str, Any]:
    return get_inventory_item(seller_sku=seller_sku)


@mcp.tool()
def inventory_get_inventory_items(limit: int | None = None, offset: int | None = None) -> Dict[str, Any]:
    return get_inventory_items(limit=limit, offset=offset)


@mcp.tool()
def inventory_create_offer(offer: Dict[str, Any], content_language: str = "en-US") -> Dict[str, Any]:
    return create_offer(offer=offer, content_language=content_language)


@mcp.tool()
def inventory_publish_offer(offer_id: str) -> Dict[str, Any]:
    return publish_offer(offer_id=offer_id)


@mcp.tool()
def fulfillment_get_orders(
    field_groups: str | None = None,
    filter: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    order_ids: str | None = None,
) -> Dict[str, Any]:
    return get_orders(
        field_groups=field_groups,
        filter=filter,
        limit=limit,
        offset=offset,
        order_ids=order_ids,
    )


@mcp.tool()
def fulfillment_get_order(order_id: str, field_groups: str | None = None) -> Dict[str, Any]:
    return get_order(order_id=order_id, field_groups=field_groups)


@mcp.tool()
def fulfillment_create_shipping_fulfillment(
    order_id: str,
    shipping_fulfillment_details: Dict[str, Any],
) -> Dict[str, Any]:
    return create_shipping_fulfillment(order_id=order_id, shipping_fulfillment_details=shipping_fulfillment_details)


@mcp.tool()
def account_get_payment_policies(
    market_id: str,
    content_language: str | None = None,
) -> Dict[str, Any]:
    return get_payment_policies(market_id=market_id, content_language=content_language)


@mcp.tool()
def account_create_payment_policy(payment_policy: Dict[str, Any]) -> Dict[str, Any]:
    return create_payment_policy(payment_policy=payment_policy)


@mcp.tool()
def account_get_fulfillment_policies(
    market_id: str,
    content_language: str | None = None,
) -> Dict[str, Any]:
    return get_fulfillment_policies(market_id=market_id, content_language=content_language)


@mcp.tool()
def finances_get_transactions(
    marketplace_id: str = "EBAY_US",
    filter: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    sort_by: str | None = None,
) -> Dict[str, Any]:
    return get_transactions(
        marketplace_id=marketplace_id,
        filter=filter,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
    )


if __name__ == "__main__":
    mcp.run()
