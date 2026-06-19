"""eBay Sell APIs MCP server.

This package exposes a FastMCP instance (`mcp`) and registers tools that wrap
endpoints across the eBay Sell API family.
"""

from __future__ import annotations

from fastmcp import FastMCP

from . import (
    account,
    analytics,
    compliance,
    feed,
    finances,
    fulfillment,
    inventory,
    logistics,
    marketing,
    metadata,
    negotiation,
    recommendation,
    stores,
)

mcp = FastMCP("ebay-sell")

# Register tools from each domain module
account.register(mcp)
analytics.register(mcp)
compliance.register(mcp)
feed.register(mcp)
finances.register(mcp)
fulfillment.register(mcp)
inventory.register(mcp)
logistics.register(mcp)
marketing.register(mcp)
metadata.register(mcp)
negotiation.register(mcp)
recommendation.register(mcp)
stores.register(mcp)
