from mcp.server.fastmcp import FastMCP

from generated_tools.browse import browse_search, get_item, get_item_by_legacy_id
from generated_tools.deal import get_events
from generated_tools.feed import get_item_snapshot_feed
from generated_tools.marketing import get_merchandised_products
from generated_tools.offer import get_bidding, place_proxy_bid
from generated_tools.order import apply_guest_coupon, get_guest_checkout_session, initiate_guest_checkout_session


mcp = FastMCP("ebay-buy-api")


@mcp.tool()
def browse_search_tool(**kwargs):
    return browse_search(**kwargs)


@mcp.tool()
def get_item_tool(item_id: str, fieldgroups: str | None = None, marketplace_id: str | None = None, enduserctx: str | None = None):
    return get_item(item_id=item_id, fieldgroups=fieldgroups, marketplace_id=marketplace_id, enduserctx=enduserctx)


@mcp.tool()
def get_item_by_legacy_id_tool(
    legacy_item_id: str,
    legacy_variation_id: str | None = None,
    fieldgroups: str | None = None,
    marketplace_id: str | None = None,
    enduserctx: str | None = None,
):
    return get_item_by_legacy_id(
        legacy_item_id=legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_events_tool(marketplace_id: str, limit: int | None = None, offset: int | None = None, enduserctx: str | None = None):
    return get_events(marketplace_id=marketplace_id, limit=limit, offset=offset, enduserctx=enduserctx)


@mcp.tool()
def get_merchandised_products_tool(
    marketplace_id: str,
    category_id: str,
    metric_name: str = "BEST_SELLING",
    limit: int | None = None,
    aspect_filter: str | None = None,
):
    return get_merchandised_products(
        marketplace_id=marketplace_id,
        category_id=category_id,
        metric_name=metric_name,
        limit=limit,
        aspect_filter=aspect_filter,
    )


@mcp.tool()
def get_item_snapshot_feed_tool(category_id: str, snapshot_date: str, range_header: str | None = None):
    return get_item_snapshot_feed(category_id=category_id, snapshot_date=snapshot_date, range_header=range_header)


@mcp.tool()
def initiate_guest_checkout_session_tool(
    contact_email: str,
    line_item_inputs: list,
    shipping_address: dict,
    marketplace_id: str,
    enduserctx: str | None = None,
):
    return initiate_guest_checkout_session(
        contact_email=contact_email,
        line_item_inputs=line_item_inputs,
        shipping_address=shipping_address,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_guest_checkout_session_tool(checkout_session_id: str, marketplace_id: str, enduserctx: str | None = None):
    return get_guest_checkout_session(
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def apply_guest_coupon_tool(
    checkout_session_id: str,
    marketplace_id: str,
    redemption_code: str,
    enduserctx: str | None = None,
):
    return apply_guest_coupon(
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        redemption_code=redemption_code,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_bidding_tool(item_id: str, marketplace_id: str):
    return get_bidding(item_id=item_id, marketplace_id=marketplace_id)


@mcp.tool()
def place_proxy_bid_tool(
    item_id: str,
    marketplace_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    adult_only_item_consent: bool | None = None,
):
    return place_proxy_bid(
        item_id=item_id,
        marketplace_id=marketplace_id,
        max_amount_value=max_amount_value,
        max_amount_currency=max_amount_currency,
        adult_only_item_consent=adult_only_item_consent,
    )


if __name__ == "__main__":
    mcp.run()
