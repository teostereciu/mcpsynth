from mcp.server.fastmcp import FastMCP

from generated_tools.browse import (
    check_compatibility,
    get_item,
    get_item_by_legacy_id,
    get_items,
    get_items_by_item_group,
    search_items,
    search_items_by_image,
)
from generated_tools.deal import get_deal_items, get_event, get_event_items, get_events
from generated_tools.feed import get_item_feed, get_item_group_feed, get_item_priority_feed, get_item_snapshot_feed
from generated_tools.order import (
    apply_guest_coupon,
    get_guest_checkout_session,
    get_guest_purchase_order,
    initiate_guest_checkout_session,
    remove_guest_coupon,
    update_guest_quantity,
    update_guest_shipping_address,
    update_guest_shipping_option,
)

mcp = FastMCP("ebay-buy-api")

mcp.tool()(search_items)
mcp.tool()(search_items_by_image)
mcp.tool()(get_item)
mcp.tool()(get_item_by_legacy_id)
mcp.tool()(get_items)
mcp.tool()(get_items_by_item_group)
mcp.tool()(check_compatibility)
mcp.tool()(get_deal_items)
mcp.tool()(get_event)
mcp.tool()(get_events)
mcp.tool()(get_event_items)
mcp.tool()(get_item_feed)
mcp.tool()(get_item_group_feed)
mcp.tool()(get_item_priority_feed)
mcp.tool()(get_item_snapshot_feed)
mcp.tool()(initiate_guest_checkout_session)
mcp.tool()(get_guest_checkout_session)
mcp.tool()(apply_guest_coupon)
mcp.tool()(remove_guest_coupon)
mcp.tool()(update_guest_quantity)
mcp.tool()(update_guest_shipping_address)
mcp.tool()(update_guest_shipping_option)
mcp.tool()(get_guest_purchase_order)

if __name__ == "__main__":
    mcp.run()
