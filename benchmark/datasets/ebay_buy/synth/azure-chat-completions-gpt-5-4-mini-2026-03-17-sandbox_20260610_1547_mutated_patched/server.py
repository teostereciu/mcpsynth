from mcp.server.fastmcp import FastMCP
from generated_tools.ebay_buy import *  # noqa

mcp = FastMCP("ebay-buy-api")

for name in [
    "search_items",
    "search_items_by_image",
    "get_item",
    "get_item_by_legacy_id",
    "get_items",
    "get_items_by_item_group",
    "check_compatibility",
    "get_deal_items",
    "get_events",
    "get_event",
    "get_event_items",
    "get_item_feed",
    "get_item_group_feed",
    "get_item_priority_feed",
    "get_item_snapshot_feed",
    "get_merchandised_products",
    "get_bidding",
    "place_proxy_bid",
    "initiate_guest_checkout_session",
    "get_guest_checkout_session",
    "apply_guest_coupon",
    "remove_guest_coupon",
    "update_guest_quantity",
    "update_guest_shipping_address",
    "update_guest_shipping_option",
    "get_guest_purchase_order",
]:
    mcp.tool()(globals()[name])

if __name__ == "__main__":
    mcp.run()
