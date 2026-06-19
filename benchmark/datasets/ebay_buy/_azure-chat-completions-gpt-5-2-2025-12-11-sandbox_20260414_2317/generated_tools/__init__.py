"""eBay Buy API MCP server (FastMCP)."""

from __future__ import annotations

from fastmcp import FastMCP

from .browse import (
    browse_check_compatibility,
    browse_get_item,
    browse_get_item_by_legacy_id,
    browse_get_items,
    browse_get_items_by_item_group,
    browse_search,
    browse_search_by_image,
)
from .deal import deal_get_deal_items, deal_get_event, deal_get_event_items, deal_get_events
from .feed import (
    feed_get_item_feed,
    feed_get_item_group_feed,
    feed_get_item_priority_feed,
    feed_get_item_snapshot_feed,
)
from .marketing import marketing_get_merchandised_products
from ._extra_domains import (
    offer_get_bidding,
    offer_place_proxy_bid,
    order_get_guest_checkout_session,
    order_initiate_guest_checkout_session,
)

mcp = FastMCP("ebay-buy-api")

# Browse
mcp.tool()(browse_search)
mcp.tool()(browse_get_item)
mcp.tool()(browse_get_items)
mcp.tool()(browse_get_item_by_legacy_id)
mcp.tool()(browse_get_items_by_item_group)
mcp.tool()(browse_search_by_image)
mcp.tool()(browse_check_compatibility)

# Deal
mcp.tool()(deal_get_deal_items)
mcp.tool()(deal_get_events)
mcp.tool()(deal_get_event)
mcp.tool()(deal_get_event_items)

# Feed
mcp.tool()(feed_get_item_feed)
mcp.tool()(feed_get_item_snapshot_feed)
mcp.tool()(feed_get_item_group_feed)
mcp.tool()(feed_get_item_priority_feed)

# Marketing
mcp.tool()(marketing_get_merchandised_products)

# Offer
mcp.tool()(offer_get_bidding)
mcp.tool()(offer_place_proxy_bid)

# Order
mcp.tool()(order_initiate_guest_checkout_session)
mcp.tool()(order_get_guest_checkout_session)
