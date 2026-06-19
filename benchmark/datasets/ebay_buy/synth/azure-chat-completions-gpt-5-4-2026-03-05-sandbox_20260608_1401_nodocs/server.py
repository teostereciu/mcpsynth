from mcp.server.fastmcp import FastMCP

from generated_tools.browse import (
    get_item,
    get_item_by_legacy_id,
    get_item_by_legacy_id_and_variations,
    get_items,
    get_items_by_item_group,
    search_by_image,
    search_by_image_with_file,
    search_items,
)
from generated_tools.deal import get_deal_event, get_deal_events, get_deal_items, get_deals
from generated_tools.feed import get_item_feed, get_item_snapshot, get_item_snapshot_file
from generated_tools.order import (
    get_guest_checkout_session,
    get_guest_purchase_order,
    initiate_guest_checkout,
    place_guest_order,
    update_guest_payment_info,
    update_guest_quantity,
    update_guest_shipping_address,
)

mcp = FastMCP("ebay-buy-api")

mcp.tool()(search_items)
mcp.tool()(get_item)
mcp.tool()(get_items)
mcp.tool()(get_item_by_legacy_id)
mcp.tool()(get_items_by_item_group)
mcp.tool()(get_item_by_legacy_id_and_variations)
mcp.tool()(search_by_image)
mcp.tool()(search_by_image_with_file)

mcp.tool()(get_deals)
mcp.tool()(get_deal_items)
mcp.tool()(get_deal_events)
mcp.tool()(get_deal_event)

mcp.tool()(get_item_feed)
mcp.tool()(get_item_snapshot)
mcp.tool()(get_item_snapshot_file)

mcp.tool()(initiate_guest_checkout)
mcp.tool()(get_guest_checkout_session)
mcp.tool()(update_guest_shipping_address)
mcp.tool()(update_guest_quantity)
mcp.tool()(update_guest_payment_info)
mcp.tool()(place_guest_order)
mcp.tool()(get_guest_purchase_order)


if __name__ == "__main__":
    mcp.run()
