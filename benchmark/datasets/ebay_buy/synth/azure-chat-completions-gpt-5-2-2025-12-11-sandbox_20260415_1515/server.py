from mcp.server.fastmcp import FastMCP

from generated_tools.browse import (
    browse_check_compatibility,
    browse_get_item,
    browse_get_item_by_legacy_id,
    browse_get_items,
    browse_get_items_by_item_group,
    browse_search,
    browse_search_by_image,
)
from generated_tools.deal import deal_get_deal_items, deal_get_event, deal_get_event_items, deal_get_events
from generated_tools.feed import feed_get_item_snapshot
from generated_tools.marketing import marketing_get_merchandised_products
from generated_tools.offer import offer_get_bidding, offer_place_proxy_bid
from generated_tools.order import (
    order_apply_guest_coupon,
    order_get_guest_checkout_session,
    order_get_guest_purchase_order,
    order_initiate_guest_checkout_session,
    order_remove_guest_coupon,
    order_update_guest_quantity,
    order_update_guest_shipping_address,
    order_update_guest_shipping_option,
)


mcp = FastMCP("ebay-buy-api")


# Browse
mcp.tool()(browse_search)
mcp.tool()(browse_search_by_image)
mcp.tool()(browse_get_item)
mcp.tool()(browse_get_item_by_legacy_id)
mcp.tool()(browse_get_items_by_item_group)
mcp.tool()(browse_get_items)
mcp.tool()(browse_check_compatibility)

# Deal
mcp.tool()(deal_get_events)
mcp.tool()(deal_get_event)
mcp.tool()(deal_get_deal_items)
mcp.tool()(deal_get_event_items)

# Feed
mcp.tool()(feed_get_item_snapshot)

# Marketing
mcp.tool()(marketing_get_merchandised_products)

# Offer
mcp.tool()(offer_get_bidding)
mcp.tool()(offer_place_proxy_bid)

# Order
mcp.tool()(order_initiate_guest_checkout_session)
mcp.tool()(order_get_guest_checkout_session)
mcp.tool()(order_apply_guest_coupon)
mcp.tool()(order_remove_guest_coupon)
mcp.tool()(order_update_guest_quantity)
mcp.tool()(order_update_guest_shipping_address)
mcp.tool()(order_update_guest_shipping_option)
mcp.tool()(order_get_guest_purchase_order)


if __name__ == "__main__":
    mcp.run()
