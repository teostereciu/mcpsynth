"""eBay Buy API MCP server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

from . import browse as _browse
from . import deal as _deal
from . import feed as _feed
from . import marketing as _marketing

mcp = FastMCP("ebay-buy-api")


# Browse
mcp.tool()(_browse.browse_search)
mcp.tool()(_browse.browse_search_by_image)
mcp.tool()(_browse.browse_get_item)
mcp.tool()(_browse.browse_get_item_by_legacy_id)
mcp.tool()(_browse.browse_get_items)
mcp.tool()(_browse.browse_get_items_by_item_group)
mcp.tool()(_browse.browse_check_compatibility)

# Deal
mcp.tool()(_deal.deal_get_deal_items)
mcp.tool()(_deal.deal_get_events)
mcp.tool()(_deal.deal_get_event)
mcp.tool()(_deal.deal_get_event_items)

# Feed
mcp.tool()(_feed.feed_get_item_feed)
mcp.tool()(_feed.feed_get_item_group_feed)
mcp.tool()(_feed.feed_get_item_priority_feed)
mcp.tool()(_feed.feed_get_item_snapshot_feed)

# Marketing
mcp.tool()(_marketing.marketing_get_merchandised_products)
