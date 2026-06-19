from mcp.server.fastmcp import FastMCP

from generated_tools.account import create_payment_policy, get_payment_policies
from generated_tools.fulfillment import get_order, get_orders
from generated_tools.inventory import (
    create_or_replace_inventory_item,
    get_inventory_item,
    get_inventory_items,
)

mcp = FastMCP("ebay-sell")


@mcp.tool()
def inventory_create_or_replace_inventory_item(sku: str, inventory_item: dict, content_language: str = "en-US") -> dict:
    return create_or_replace_inventory_item(sku, inventory_item, content_language=content_language)


@mcp.tool()
def inventory_get_inventory_item(sku: str) -> dict:
    return get_inventory_item(sku)


@mcp.tool()
def inventory_get_inventory_items(limit: int = 25, offset: int = 0) -> dict:
    return get_inventory_items(limit=limit, offset=offset)


@mcp.tool()
def fulfillment_get_orders(
    filter: str | None = None,
    order_ids: str | None = None,
    field_groups: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> dict:
    return get_orders(
        filter=filter,
        order_ids=order_ids,
        field_groups=field_groups,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def fulfillment_get_order(order_id: str, field_groups: str | None = None) -> dict:
    return get_order(order_id, field_groups=field_groups)


@mcp.tool()
def account_get_payment_policies(marketplace_id: str, content_language: str | None = None) -> dict:
    return get_payment_policies(marketplace_id, content_language=content_language)


@mcp.tool()
def account_create_payment_policy(payment_policy: dict) -> dict:
    return create_payment_policy(payment_policy)


if __name__ == "__main__":
    mcp.run()
