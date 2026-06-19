"""eBay Buy API MCP server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

from .http import safe_tool_call
from . import browse as _browse
from . import deal as _deal
from . import feed as _feed
from . import marketing as _marketing

mcp = FastMCP("ebay-buy")


@mcp.tool(name="browse_search_items")
def browse_search_items(**kwargs):
    return safe_tool_call(_browse.search_items, **kwargs)


@mcp.tool(name="browse_get_item")
def browse_get_item(**kwargs):
    return safe_tool_call(_browse.get_item, **kwargs)


@mcp.tool(name="browse_get_items")
def browse_get_items(**kwargs):
    return safe_tool_call(_browse.get_items, **kwargs)


@mcp.tool(name="browse_get_item_by_legacy_id")
def browse_get_item_by_legacy_id(**kwargs):
    return safe_tool_call(_browse.get_item_by_legacy_id, **kwargs)


@mcp.tool(name="browse_get_items_by_item_group")
def browse_get_items_by_item_group(**kwargs):
    return safe_tool_call(_browse.get_items_by_item_group, **kwargs)


@mcp.tool(name="browse_search_by_image")
def browse_search_by_image(**kwargs):
    return safe_tool_call(_browse.search_by_image, **kwargs)


@mcp.tool(name="browse_check_compatibility")
def browse_check_compatibility(**kwargs):
    return safe_tool_call(_browse.check_compatibility, **kwargs)


@mcp.tool(name="deal_get_events")
def deal_get_events(**kwargs):
    return safe_tool_call(_deal.get_events, **kwargs)


@mcp.tool(name="deal_get_event")
def deal_get_event(**kwargs):
    return safe_tool_call(_deal.get_event, **kwargs)


@mcp.tool(name="deal_get_event_items")
def deal_get_event_items(**kwargs):
    return safe_tool_call(_deal.get_event_items, **kwargs)


@mcp.tool(name="deal_get_deal_items")
def deal_get_deal_items(**kwargs):
    return safe_tool_call(_deal.get_deal_items, **kwargs)


@mcp.tool(name="feed_get_item_feed")
def feed_get_item_feed(**kwargs):
    return safe_tool_call(_feed.get_item_feed, **kwargs)


@mcp.tool(name="feed_get_item_group_feed")
def feed_get_item_group_feed(**kwargs):
    return safe_tool_call(_feed.get_item_group_feed, **kwargs)


@mcp.tool(name="feed_get_item_snapshot_feed")
def feed_get_item_snapshot_feed(**kwargs):
    return safe_tool_call(_feed.get_item_snapshot_feed, **kwargs)


@mcp.tool(name="feed_get_item_priority_feed")
def feed_get_item_priority_feed(**kwargs):
    return safe_tool_call(_feed.get_item_priority_feed, **kwargs)


@mcp.tool(name="marketing_get_merchandised_products")
def marketing_get_merchandised_products(**kwargs):
    return safe_tool_call(_marketing.get_merchandised_products, **kwargs)
