"""
eBay Buy API — MCP Server
=========================
Exposes tools for the eBay Buy API namespaces:
  • Browse  — search, item details, compatibility
  • Deal    — deal items, events, event items
  • Feed    — item feeds, snapshots, feed file catalog
  • Order   — guest checkout flow, purchase orders
  • Marketplace Insights — sold-item analytics
  • Taxonomy — category tree, suggestions, aspects

Run:
    python server.py

Environment variables required:
    EBAY_APP_ID      — OAuth client ID
    EBAY_CERT_ID     — OAuth client secret
    EBAY_ENVIRONMENT — SANDBOX (default) or PRODUCTION
    EBAY_MARKETPLACE_ID — e.g. EBAY_US (default)
"""

import sys
import os

# Ensure the project root is on the path so generated_tools imports work.
sys.path.insert(0, os.path.dirname(__file__))

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Create the top-level MCP server
# ---------------------------------------------------------------------------
mcp = FastMCP(
    "eBay Buy API",
    instructions=(
        "This server provides tools for the eBay Buy API. "
        "Use search_items to find listings, get_item for details, "
        "the guest checkout tools to place orders, deal/event tools for promotions, "
        "feed tools for bulk data, and taxonomy tools for category discovery."
    ),
)

# ---------------------------------------------------------------------------
# Import and register all domain tools
# ---------------------------------------------------------------------------

# --- Browse ---
from generated_tools.browse import (
    search_items,
    search_items_by_image,
    get_item,
    get_item_by_legacy_id,
    get_items_by_item_group,
    get_items,
    check_compatibility,
    get_compatibility_properties,
    get_compatibility_property_values,
)

# --- Deal ---
from generated_tools.deal import (
    get_deal_items,
    get_events,
    get_event,
    get_event_items,
)

# --- Feed ---
from generated_tools.feed import (
    get_item_feed,
    get_item_group_feed,
    get_item_snapshot_feed,
    get_feed_files,
    get_feed_file,
    get_feed_access,
)

# --- Order ---
from generated_tools.order import (
    initiate_guest_checkout_session,
    get_guest_checkout_session,
    update_guest_checkout_session,
    apply_guest_coupon,
    remove_guest_coupon,
    update_guest_quantity,
    update_guest_shipping_option,
    initiate_guest_payment,
    place_guest_order,
    get_guest_purchase_order,
)

# --- Marketplace Insights ---
from generated_tools.marketplace_insights import (
    search_sold_items,
    search_sold_items_by_image,
)

# --- Taxonomy ---
from generated_tools.taxonomy import (
    get_default_category_tree_id,
    get_category_tree,
    get_category_subtree,
    get_category_suggestions,
    get_item_aspects_for_category,
    get_categories_by_level,
)

# ---------------------------------------------------------------------------
# Register Browse tools
# ---------------------------------------------------------------------------
mcp.tool()(search_items)
mcp.tool()(search_items_by_image)
mcp.tool()(get_item)
mcp.tool()(get_item_by_legacy_id)
mcp.tool()(get_items_by_item_group)
mcp.tool()(get_items)
mcp.tool()(check_compatibility)
mcp.tool()(get_compatibility_properties)
mcp.tool()(get_compatibility_property_values)

# ---------------------------------------------------------------------------
# Register Deal tools
# ---------------------------------------------------------------------------
mcp.tool()(get_deal_items)
mcp.tool()(get_events)
mcp.tool()(get_event)
mcp.tool()(get_event_items)

# ---------------------------------------------------------------------------
# Register Feed tools
# ---------------------------------------------------------------------------
mcp.tool()(get_item_feed)
mcp.tool()(get_item_group_feed)
mcp.tool()(get_item_snapshot_feed)
mcp.tool()(get_feed_files)
mcp.tool()(get_feed_file)
mcp.tool()(get_feed_access)

# ---------------------------------------------------------------------------
# Register Order tools
# ---------------------------------------------------------------------------
mcp.tool()(initiate_guest_checkout_session)
mcp.tool()(get_guest_checkout_session)
mcp.tool()(update_guest_checkout_session)
mcp.tool()(apply_guest_coupon)
mcp.tool()(remove_guest_coupon)
mcp.tool()(update_guest_quantity)
mcp.tool()(update_guest_shipping_option)
mcp.tool()(initiate_guest_payment)
mcp.tool()(place_guest_order)
mcp.tool()(get_guest_purchase_order)

# ---------------------------------------------------------------------------
# Register Marketplace Insights tools
# ---------------------------------------------------------------------------
mcp.tool()(search_sold_items)
mcp.tool()(search_sold_items_by_image)

# ---------------------------------------------------------------------------
# Register Taxonomy tools
# ---------------------------------------------------------------------------
mcp.tool()(get_default_category_tree_id)
mcp.tool()(get_category_tree)
mcp.tool()(get_category_subtree)
mcp.tool()(get_category_suggestions)
mcp.tool()(get_item_aspects_for_category)
mcp.tool()(get_categories_by_level)

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    mcp.run(transport="stdio")
