import os
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.ebay_client import EbayClient
from generated_tools import browse as browse_tools
from generated_tools import deal as deal_tools
from generated_tools import order as order_tools


mcp = FastMCP("ebay-buy-api")


def _client() -> EbayClient:
    return EbayClient(
        app_id=os.getenv("EBAY_APP_ID"),
        cert_id=os.getenv("EBAY_CERT_ID"),
        environment=os.getenv("EBAY_ENVIRONMENT") or "SANDBOX",
    )


@mcp.tool()
def browse_search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    charity_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """Search for items (Browse API)."""
    return browse_tools.search_items(
        _client(),
        q=q,
        category_ids=category_ids,
        charity_ids=charity_ids,
        epid=epid,
        gtin=gtin,
        filter=filter,
        aspect_filter=aspect_filter,
        compatibility_filter=compatibility_filter,
        fieldgroups=fieldgroups,
        sort=sort,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_get_item(
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """Get item details by RESTful item_id (Browse API)."""
    return browse_tools.get_item(
        _client(),
        item_id=item_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def deal_get_events(
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """List deal events for a marketplace (Deal API)."""
    return deal_tools.get_events(
        _client(),
        marketplace_id=marketplace_id,
        limit=limit,
        offset=offset,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_initiate_guest_checkout_session(
    marketplace_id: str,
    contact_email: str,
    line_items: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a guest checkout session (Order API v2)."""
    return order_tools.initiate_guest_checkout_session(
        _client(),
        marketplace_id=marketplace_id,
        contact_email=contact_email,
        line_items=line_items,
        shipping_address=shipping_address,
        enduserctx=enduserctx,
    )


if __name__ == "__main__":
    mcp.run()
