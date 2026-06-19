"""
eBay Sell API — MCP Server entry point.

Runs over stdio using FastMCP. All tools from every domain module are
imported and re-registered onto a single root FastMCP instance so that
list_tools() returns the complete set.
"""

from mcp.server.fastmcp import FastMCP

# ── Domain modules (importing them executes their @mcp.tool() decorators) ──
from generated_tools.auth import ebay_request  # noqa: F401 – side-effect free import
from generated_tools import (
    inventory,
    fulfillment,
    account,
    marketing,
    finances,
    feed,
    catalog,
    analytics,
    compliance,
    recommendation,
    negotiation,
    logistics,
)

# ---------------------------------------------------------------------------
# Root server
# ---------------------------------------------------------------------------
mcp = FastMCP(
    "ebay-sell",
    instructions=(
        "MCP server for the eBay Sell API. "
        "Covers Inventory (items, offers, locations), Fulfillment (orders, "
        "shipping, payment disputes), Account (fulfillment/payment/return "
        "policies, programs, sales tax), Marketing (campaigns, ads, keywords, "
        "promotions), Finances (transactions, payouts, transfers), Feed (bulk "
        "upload/download tasks, schedules), Catalog/Taxonomy, Analytics, "
        "Compliance, Recommendations, Negotiation, and Logistics. "
        "Requires env vars: EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN, "
        "EBAY_ENVIRONMENT (SANDBOX or PRODUCTION)."
    ),
)

# ---------------------------------------------------------------------------
# Mount all domain tools onto the root server.
# FastMCP stores tools in ._tool_manager._tools (dict[str, Tool]).
# We copy every tool object from each domain sub-server into the root.
# ---------------------------------------------------------------------------
_DOMAIN_MCPS = [
    inventory.mcp,
    fulfillment.mcp,
    account.mcp,
    marketing.mcp,
    finances.mcp,
    feed.mcp,
    catalog.mcp,
    analytics.mcp,
    compliance.mcp,
    recommendation.mcp,
    negotiation.mcp,
    logistics.mcp,
]

for _domain_mcp in _DOMAIN_MCPS:
    # FastMCP 3.x exposes tools via ._tool_manager._tools
    try:
        _tools_dict = _domain_mcp._tool_manager._tools
        for _name, _tool in _tools_dict.items():
            mcp._tool_manager._tools[_name] = _tool
    except AttributeError:
        # Fallback: iterate the tool manager's public interface
        for _tool in _domain_mcp._tool_manager.list_tools():
            mcp._tool_manager._tools[_tool.name] = _tool


if __name__ == "__main__":
    mcp.run(transport="stdio")
