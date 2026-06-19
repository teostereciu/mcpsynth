"""
eBay Buy API MCP Server

Exposes tools for the eBay Buy API namespaces:
  - Browse: search, item details, item groups, compatibility
  - Deal: deal items, events, event items
  - Feed: item feed, item group feed, item priority feed, item snapshot feed
  - Marketing: merchandised products (best sellers)
  - Offer: auction bidding (get bidding, place proxy bid)
  - Order: guest checkout session management, purchase order retrieval

Authentication:
  Set EBAY_APP_ID and EBAY_CERT_ID environment variables.
  Set EBAY_ENVIRONMENT to SANDBOX (default) or PRODUCTION.
"""

from mcp.server.fastmcp import FastMCP

from generated_tools.browse import register_browse_tools
from generated_tools.deal import register_deal_tools
from generated_tools.feed import register_feed_tools
from generated_tools.marketing import register_marketing_tools
from generated_tools.offer import register_offer_tools
from generated_tools.order import register_order_tools

mcp = FastMCP(
    name="ebay-buy-api",
    instructions=(
        "This server provides tools for the eBay Buy API. "
        "Use search_items to find products, get_item for details, "
        "get_deal_items/get_events for deals, get_item_feed for bulk data, "
        "get_merchandised_products for best sellers, "
        "and the guest checkout tools for the full purchase flow. "
        "Set EBAY_APP_ID, EBAY_CERT_ID, and EBAY_ENVIRONMENT env vars before use."
    ),
)

# Register all domain tools
register_browse_tools(mcp)
register_deal_tools(mcp)
register_feed_tools(mcp)
register_marketing_tools(mcp)
register_offer_tools(mcp)
register_order_tools(mcp)

if __name__ == "__main__":
    mcp.run()
