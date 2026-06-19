import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools import collections, customers, discounts, fulfillment, inventory, metafields, orders, products, webhooks

mcp = FastMCP("shopify-admin-rest")


def _env_check() -> Dict[str, Any]:
    missing = [k for k in ("SHOPIFY_STORE_URL", "SHOPIFY_ACCESS_TOKEN") if not os.getenv(k)]
    if missing:
        return {"error": f"Missing environment variables: {', '.join(missing)}"}
    return {"ok": True}


@mcp.tool()
def shopify_env_check() -> Dict[str, Any]:
    return _env_check()


# Products
mcp.tool()(products.list_products)
mcp.tool()(products.get_product)
mcp.tool()(products.create_product)
mcp.tool()(products.update_product)
mcp.tool()(products.delete_product)

mcp.tool()(products.list_product_variants)
mcp.tool()(products.get_variant)
mcp.tool()(products.create_variant)
mcp.tool()(products.update_variant)
mcp.tool()(products.delete_variant)

mcp.tool()(products.list_product_images)
mcp.tool()(products.get_product_image)
mcp.tool()(products.create_product_image)
mcp.tool()(products.update_product_image)
mcp.tool()(products.delete_product_image)


# Collections
mcp.tool()(collections.list_custom_collections)
mcp.tool()(collections.get_custom_collection)
mcp.tool()(collections.create_custom_collection)
mcp.tool()(collections.update_custom_collection)
mcp.tool()(collections.delete_custom_collection)

mcp.tool()(collections.list_smart_collections)
mcp.tool()(collections.get_smart_collection)
mcp.tool()(collections.create_smart_collection)
mcp.tool()(collections.update_smart_collection)
mcp.tool()(collections.delete_smart_collection)

mcp.tool()(collections.list_collects)
mcp.tool()(collections.create_collect)
mcp.tool()(collections.delete_collect)


# Orders
mcp.tool()(orders.list_orders)
mcp.tool()(orders.get_order)
mcp.tool()(orders.update_order)
mcp.tool()(orders.close_order)
mcp.tool()(orders.open_order)
mcp.tool()(orders.cancel_order)

mcp.tool()(orders.list_draft_orders)
mcp.tool()(orders.get_draft_order)
mcp.tool()(orders.create_draft_order)
mcp.tool()(orders.update_draft_order)
mcp.tool()(orders.complete_draft_order)

mcp.tool()(orders.calculate_refund)
mcp.tool()(orders.create_refund)
mcp.tool()(orders.list_transactions)
mcp.tool()(orders.get_transaction)
mcp.tool()(orders.create_transaction)


# Fulfillment
mcp.tool()(fulfillment.list_locations)
mcp.tool()(fulfillment.get_location)

mcp.tool()(fulfillment.list_fulfillment_orders)
mcp.tool()(fulfillment.get_fulfillment_order)
mcp.tool()(fulfillment.move_fulfillment_order)
mcp.tool()(fulfillment.cancel_fulfillment_order)
mcp.tool()(fulfillment.close_fulfillment_order)

mcp.tool()(fulfillment.list_fulfillments)
mcp.tool()(fulfillment.get_fulfillment)
mcp.tool()(fulfillment.create_fulfillment)
mcp.tool()(fulfillment.update_fulfillment_tracking)
mcp.tool()(fulfillment.cancel_fulfillment)
mcp.tool()(fulfillment.create_fulfillment_event)


# Customers
mcp.tool()(customers.list_customers)
mcp.tool()(customers.search_customers)
mcp.tool()(customers.get_customer)
mcp.tool()(customers.create_customer)
mcp.tool()(customers.update_customer)
mcp.tool()(customers.delete_customer)


# Inventory
mcp.tool()(inventory.get_inventory_item)
mcp.tool()(inventory.update_inventory_item)

mcp.tool()(inventory.list_inventory_levels)
mcp.tool()(inventory.adjust_inventory_level)
mcp.tool()(inventory.set_inventory_level)
mcp.tool()(inventory.connect_inventory_level)
mcp.tool()(inventory.delete_inventory_level)


# Discounts
mcp.tool()(discounts.list_price_rules)
mcp.tool()(discounts.get_price_rule)
mcp.tool()(discounts.create_price_rule)
mcp.tool()(discounts.update_price_rule)
mcp.tool()(discounts.delete_price_rule)

mcp.tool()(discounts.list_discount_codes)
mcp.tool()(discounts.get_discount_code)
mcp.tool()(discounts.create_discount_code)
mcp.tool()(discounts.update_discount_code)
mcp.tool()(discounts.delete_discount_code)


# Webhooks
mcp.tool()(webhooks.list_webhooks)
mcp.tool()(webhooks.get_webhook)
mcp.tool()(webhooks.create_webhook)
mcp.tool()(webhooks.update_webhook)
mcp.tool()(webhooks.delete_webhook)


# Metafields
mcp.tool()(metafields.list_metafields)
mcp.tool()(metafields.get_metafield)
mcp.tool()(metafields.create_metafield)
mcp.tool()(metafields.update_metafield)
mcp.tool()(metafields.delete_metafield)


if __name__ == "__main__":
    mcp.run()
