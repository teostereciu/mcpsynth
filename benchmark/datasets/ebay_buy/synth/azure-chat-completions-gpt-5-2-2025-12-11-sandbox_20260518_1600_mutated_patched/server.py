import os
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import EbayClient
from generated_tools import browse as browse_tools
from generated_tools import deal as deal_tools
from generated_tools import feed as feed_tools
from generated_tools import marketing as marketing_tools
from generated_tools import offer as offer_tools
from generated_tools import order as order_tools


mcp = FastMCP("ebay-buy-api")


def _client() -> EbayClient:
    return EbayClient(
        app_id=os.getenv("EBAY_APP_ID"),
        cert_id=os.getenv("EBAY_CERT_ID"),
        environment=os.getenv("EBAY_ENVIRONMENT", "SANDBOX"),
    )


# -------------------- Browse API --------------------


@mcp.tool()
def browse_search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    fieldgroups: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    auto_correct: Optional[bool] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.search_items(
        _client(),
        q=q,
        category_ids=category_ids,
        filter=filter,
        sort=sort,
        limit=limit,
        offset=offset,
        fieldgroups=fieldgroups,
        aspect_filter=aspect_filter,
        compatibility_filter=compatibility_filter,
        auto_correct=auto_correct,
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
    return browse_tools.get_item(
        _client(),
        item_id=item_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_search_items_by_image(
    image_base64: str,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    aspect_filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.search_items_by_image(
        _client(),
        image_base64=image_base64,
        category_ids=category_ids,
        filter=filter,
        sort=sort,
        limit=limit,
        offset=offset,
        aspect_filter=aspect_filter,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_get_items(
    item_ids: List[str],
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.get_items(_client(), item_ids=item_ids, marketplace_id=marketplace_id, enduserctx=enduserctx)


@mcp.tool()
def browse_get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.get_item_by_legacy_id(
        _client(),
        legacy_item_id=legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_get_items_by_item_group(
    item_group_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.get_items_by_item_group(
        _client(),
        item_group_id=item_group_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_check_compatibility(
    item_id: str,
    compatibility_properties: List[Dict[str, str]],
    marketplace_id: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.check_compatibility(
        _client(),
        item_id=item_id,
        compatibility_properties=compatibility_properties,
        marketplace_id=marketplace_id,
        accept_language=accept_language,
    )


# -------------------- Deal API --------------------


@mcp.tool()
def deal_get_events(
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal_tools.get_events(_client(), marketplace_id=marketplace_id, limit=limit, offset=offset, enduserctx=enduserctx)


@mcp.tool()
def deal_get_event(
    event_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal_tools.get_event(_client(), event_id=event_id, marketplace_id=marketplace_id, enduserctx=enduserctx)


@mcp.tool()
def deal_get_deal_items(
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    category_list: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal_tools.get_deal_items(
        _client(),
        marketplace_id=marketplace_id,
        limit=limit,
        offset=offset,
        category_list=category_list,
        commissionable=commissionable,
        delivery_country=delivery_country,
        enduserctx=enduserctx,
    )


@mcp.tool()
def deal_get_event_items(
    marketplace_id: str,
    event_ids: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    category_list: Optional[str] = None,
    delivery_country: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal_tools.get_event_items(
        _client(),
        marketplace_id=marketplace_id,
        event_ids=event_ids,
        limit=limit,
        offset=offset,
        category_list=category_list,
        delivery_country=delivery_country,
        enduserctx=enduserctx,
    )


# -------------------- Feed API --------------------


@mcp.tool()
def feed_get_item_feed(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed_tools.get_item_feed(
        _client(),
        feed_scope=feed_scope,
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def feed_get_item_group_feed(
    feed_scope: str,
    category_id: str,
    marketplace_id: str,
    date: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed_tools.get_item_group_feed(
        _client(),
        feed_scope=feed_scope,
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def feed_get_item_priority_feed(
    category_id: str,
    date: str,
    marketplace_id: str,
    range_header: str,
) -> Dict[str, Any]:
    return feed_tools.get_item_priority_feed(
        _client(),
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def feed_get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    marketplace_id: str,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed_tools.get_item_snapshot_feed(
        _client(),
        category_id=category_id,
        snapshot_date=snapshot_date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


# -------------------- Marketing API --------------------


@mcp.tool()
def marketing_get_merchandised_products(
    metric_name: str,
    category_id: str,
    limit: Optional[int] = None,
    facet_filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    return marketing_tools.get_merchandised_products(
        _client(),
        metric_name=metric_name,
        category_id=category_id,
        limit=limit,
        facet_filter=facet_filter,
        marketplace_id=marketplace_id,
    )


# -------------------- Offer API (user-token required) --------------------


@mcp.tool()
def offer_get_bidding(
    item_id: str,
    marketplace_id: str,
) -> Dict[str, Any]:
    return offer_tools.get_bidding(_client(), item_id=item_id, marketplace_id=marketplace_id)


@mcp.tool()
def offer_place_proxy_bid(
    item_id: str,
    marketplace_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    adult_only_item_consent: bool = False,
) -> Dict[str, Any]:
    return offer_tools.place_proxy_bid(
        _client(),
        item_id=item_id,
        marketplace_id=marketplace_id,
        max_amount_value=max_amount_value,
        max_amount_currency=max_amount_currency,
        adult_only_item_consent=adult_only_item_consent,
    )


# -------------------- Order API (guest checkout) --------------------


@mcp.tool()
def order_initiate_guest_checkout_session(
    marketplace_id: str,
    contact_email: str,
    line_items: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.initiate_guest_checkout_session(
        _client(),
        marketplace_id=marketplace_id,
        contact_email=contact_email,
        line_items=line_items,
        shipping_address=shipping_address,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_get_guest_checkout_session(
    checkout_session_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.get_guest_checkout_session(
        _client(),
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_shipping_address(
    checkout_session_id: str,
    marketplace_id: str,
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.update_guest_shipping_address(
        _client(),
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        shipping_address=shipping_address,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_shipping_option(
    checkout_session_id: str,
    marketplace_id: str,
    line_item_id: str,
    shipping_option_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.update_guest_shipping_option(
        _client(),
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        line_item_id=line_item_id,
        shipping_option_id=shipping_option_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_quantity(
    checkout_session_id: str,
    marketplace_id: str,
    line_item_id: str,
    quantity: int,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.update_guest_quantity(
        _client(),
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        line_item_id=line_item_id,
        quantity=quantity,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_apply_guest_coupon(
    checkout_session_id: str,
    marketplace_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.apply_guest_coupon(
        _client(),
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        redemption_code=redemption_code,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_remove_guest_coupon(
    checkout_session_id: str,
    marketplace_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.remove_guest_coupon(
        _client(),
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id,
        redemption_code=redemption_code,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_get_guest_purchase_order(
    purchase_order_id: str,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.get_guest_purchase_order(
        _client(),
        purchase_order_id=purchase_order_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


if __name__ == "__main__":
    mcp.run()
