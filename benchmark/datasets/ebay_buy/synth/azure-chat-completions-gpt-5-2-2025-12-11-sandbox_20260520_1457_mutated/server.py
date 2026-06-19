from __future__ import annotations

from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import EbayClient
from generated_tools import browse as browse_tools
from generated_tools import deal as deal_tools
from generated_tools import feed as feed_tools
from generated_tools import marketing as marketing_tools
from generated_tools import offer as offer_tools
from generated_tools import order as order_tools


mcp = FastMCP("ebay-buy-api")


def _client() -> Dict[str, Any]:
    try:
        return {"client": EbayClient()}
    except Exception as e:
        return {"error": str(e)}


# -------------------- Browse --------------------


@mcp.tool()
def browse_search(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    charity_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return browse_tools.browse_search(
        c["client"],
        q=q,
        category_ids=category_ids,
        epid=epid,
        gtin=gtin,
        charity_ids=charity_ids,
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
def get_item(
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return browse_tools.get_item(
        c["client"],
        item_id=item_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_search_by_image(
    image: str,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return browse_tools.browse_search_by_image(
        c["client"],
        image=image,
        category_ids=category_ids,
        filter=filter,
        aspect_filter=aspect_filter,
        fieldgroups=fieldgroups,
        sort=sort,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return browse_tools.get_item_by_legacy_id(
        c["client"],
        legacy_item_id=legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_items_bulk(
    item_ids: Optional[str] = None,
    item_group_ids: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return browse_tools.get_items_bulk(
        c["client"],
        item_ids=item_ids,
        item_group_ids=item_group_ids,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_items_by_item_group(
    item_group_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return browse_tools.get_items_by_item_group(
        c["client"],
        item_group_id=item_group_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def check_compatibility(
    item_id: str,
    compatibility_properties: list[dict[str, str]],
    marketplace_id: str = "EBAY_US",
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return browse_tools.check_compatibility(
        c["client"],
        item_id=item_id,
        compatibility_properties=compatibility_properties,
        marketplace_id=marketplace_id,
        accept_language=accept_language,
    )


# -------------------- Deal --------------------


@mcp.tool()
def get_events(
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return deal_tools.get_events(
        c["client"],
        max_results=max_results,
        skip=skip,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_event(
    event_id: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return deal_tools.get_event(c["client"], event_id=event_id, marketplace_id=marketplace_id, enduserctx=enduserctx)


@mcp.tool()
def get_deal_items(
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    category_ids: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return deal_tools.get_deal_items(
        c["client"],
        max_results=max_results,
        skip=skip,
        category_ids=category_ids,
        commissionable=commissionable,
        delivery_country=delivery_country,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_event_items(
    event_ids: str,
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return deal_tools.get_event_items(
        c["client"],
        event_ids=event_ids,
        max_results=max_results,
        skip=skip,
        category_ids=category_ids,
        delivery_country=delivery_country,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


# -------------------- Feed --------------------


@mcp.tool()
def get_item_feed(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return feed_tools.get_item_feed(
        c["client"],
        feed_scope=feed_scope,
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    marketplace_id: str = "EBAY_US",
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return feed_tools.get_item_snapshot_feed(
        c["client"],
        category_id=category_id,
        snapshot_date=snapshot_date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def get_item_priority_feed(
    category_id: str,
    date: str,
    marketplace_id: str = "EBAY_US",
    range_header: str = "bytes=0-1048576",
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return feed_tools.get_item_priority_feed(
        c["client"],
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def get_item_group_feed(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return feed_tools.get_item_group_feed(
        c["client"],
        feed_scope=feed_scope,
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


# -------------------- Marketing --------------------


@mcp.tool()
def get_merchandised_products(
    metric_name: str,
    category_id: str,
    max_results: Optional[int] = None,
    aspect_filter: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return marketing_tools.get_merchandised_products(
        c["client"],
        metric_name=metric_name,
        category_id=category_id,
        max_results=max_results,
        aspect_filter=aspect_filter,
    )


# -------------------- Offer (Auction) --------------------


@mcp.tool()
def get_bidding(
    listing_id: str,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return offer_tools.get_bidding(c["client"], listing_id=listing_id, marketplace_id=marketplace_id)


@mcp.tool()
def place_proxy_bid(
    listing_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    adult_only_item_consent: Optional[bool] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return offer_tools.place_proxy_bid(
        c["client"],
        listing_id=listing_id,
        max_amount_value=max_amount_value,
        max_amount_currency=max_amount_currency,
        adult_only_item_consent=adult_only_item_consent,
        marketplace_id=marketplace_id,
    )


# -------------------- Order (Guest) --------------------


@mcp.tool()
def initiate_guest_checkout_session(
    contact_email: str,
    line_item_inputs: list[dict[str, Any]],
    shipping_address: dict[str, Any],
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return order_tools.initiate_guest_checkout_session(
        c["client"],
        contact_email=contact_email,
        line_item_inputs=line_item_inputs,
        shipping_address=shipping_address,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_guest_checkout_session(
    checkout_session_id: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return order_tools.get_guest_checkout_session(
        c["client"],
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return order_tools.update_guest_quantity(
        c["client"],
        checkout_session_id=checkout_session_id,
        line_item_id=line_item_id,
        quantity=quantity,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def update_guest_shipping_address(
    checkout_session_id: str,
    shipping_address: dict[str, Any],
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return order_tools.update_guest_shipping_address(
        c["client"],
        checkout_session_id=checkout_session_id,
        shipping_address=shipping_address,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return order_tools.update_guest_shipping_option(
        c["client"],
        checkout_session_id=checkout_session_id,
        line_item_id=line_item_id,
        shipping_option_id=shipping_option_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def apply_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return order_tools.apply_guest_coupon(
        c["client"],
        checkout_session_id=checkout_session_id,
        redemption_code=redemption_code,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def remove_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return order_tools.remove_guest_coupon(
        c["client"],
        checkout_session_id=checkout_session_id,
        redemption_code=redemption_code,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def get_guest_purchase_order(
    purchase_order_id: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    c = _client()
    if "error" in c:
        return c
    return order_tools.get_guest_purchase_order(
        c["client"],
        purchase_order_id=purchase_order_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


if __name__ == "__main__":
    mcp.run()
