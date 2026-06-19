"""
eBay Buy Deal API tools.
Covers: getDeals (deal items), getDealItems, getEvent, getEvents, getEventItems.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get

mcp = FastMCP("ebay-deal")

DEAL_BASE = "/buy/deal/v1"


# ---------------------------------------------------------------------------
# Deal Items
# ---------------------------------------------------------------------------

@mcp.tool()
def get_deal_items(
    category_ids: str = "",
    commissionable_only: bool = False,
    delivery_country: str = "",
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Retrieve a paginated list of eBay deal items (items with special pricing).

    Args:
        category_ids: Comma-separated category IDs to filter deals.
        commissionable_only: If True, return only commissionable deals.
        delivery_country: ISO 3166-1 alpha-2 country code for delivery filtering.
        limit: Number of results per page (1-100, default 20).
        offset: Pagination offset.
    Returns:
        dict with dealItems list and pagination metadata.
    """
    params: dict = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    if commissionable_only:
        params["commissionable_only"] = "true"
    if delivery_country:
        params["delivery_country"] = delivery_country
    return api_get(f"{DEAL_BASE}/deal_item", params=params)


# ---------------------------------------------------------------------------
# Events
# ---------------------------------------------------------------------------

@mcp.tool()
def get_events(
    category_ids: str = "",
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Retrieve a paginated list of eBay sale events.

    Args:
        category_ids: Comma-separated category IDs to filter events.
        limit: Number of results per page (1-100, default 20).
        offset: Pagination offset.
    Returns:
        dict with events list and pagination metadata.
    """
    params: dict = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    return api_get(f"{DEAL_BASE}/event", params=params)


@mcp.tool()
def get_event(event_id: str) -> dict:
    """
    Retrieve details for a specific eBay sale event by its ID.

    Args:
        event_id: The unique eBay event ID.
    Returns:
        dict with event details including title, dates, and terms.
    """
    return api_get(f"{DEAL_BASE}/event/{event_id}")


@mcp.tool()
def get_event_items(
    event_id: str,
    category_ids: str = "",
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Retrieve items associated with a specific eBay sale event.

    Args:
        event_id: The unique eBay event ID.
        category_ids: Comma-separated category IDs to filter event items.
        limit: Number of results per page (1-100, default 20).
        offset: Pagination offset.
    Returns:
        dict with eventItems list and pagination metadata.
    """
    params: dict = {"event_id": event_id, "limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    return api_get(f"{DEAL_BASE}/event_item", params=params)
