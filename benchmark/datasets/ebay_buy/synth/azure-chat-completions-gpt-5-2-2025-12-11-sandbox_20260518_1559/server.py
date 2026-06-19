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
client = EbayClient()


# Browse
@mcp.tool()
def browse_get_item(
    item_id: str,
    fieldgroups: Optional[str] = None,
    if_none_match: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.get_item(
        client,
        item_id=item_id,
        fieldgroups=fieldgroups,
        if_none_match=if_none_match,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_search_items(
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
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.search_items(
        client,
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
def browse_search_items_by_image(
    image_base64: str,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.search_items_by_image(
        client,
        image_base64=image_base64,
        category_ids=category_ids,
        filter=filter,
        aspect_filter=aspect_filter,
        sort=sort,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.get_item_by_legacy_id(
        client,
        legacy_item_id=legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_get_items(
    item_ids: Optional[str] = None,
    item_group_ids: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.get_items(
        client,
        item_ids=item_ids,
        item_group_ids=item_group_ids,
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
        client,
        item_group_id=item_group_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def browse_check_compatibility(
    item_id: str,
    compatibility_properties: list[dict[str, str]],
    marketplace_id: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    return browse_tools.check_compatibility(
        client,
        item_id=item_id,
        compatibility_properties=compatibility_properties,
        marketplace_id=marketplace_id,
        accept_language=accept_language,
    )


# Deal
@mcp.tool()
def deal_get_events(
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal_tools.get_events(
        client,
        marketplace_id=marketplace_id,
        limit=limit,
        offset=offset,
        enduserctx=enduserctx,
    )


@mcp.tool()
def deal_get_event(
    marketplace_id: str,
    event_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal_tools.get_event(client, marketplace_id=marketplace_id, event_id=event_id, enduserctx=enduserctx)


@mcp.tool()
def deal_get_deal_items(
    marketplace_id: str,
    category_ids: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal_tools.get_deal_items(
        client,
        marketplace_id=marketplace_id,
        category_ids=category_ids,
        commissionable=commissionable,
        delivery_country=delivery_country,
        limit=limit,
        offset=offset,
        enduserctx=enduserctx,
    )


@mcp.tool()
def deal_get_event_items(
    marketplace_id: str,
    event_ids: str,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal_tools.get_event_items(
        client,
        marketplace_id=marketplace_id,
        event_ids=event_ids,
        category_ids=category_ids,
        delivery_country=delivery_country,
        limit=limit,
        offset=offset,
        enduserctx=enduserctx,
    )


# Feed (download instructions)
@mcp.tool()
def feed_get_item_feed(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed_tools.get_item_feed(
        client,
        feed_scope=feed_scope,
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def feed_get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed_tools.get_item_snapshot_feed(
        client,
        category_id=category_id,
        snapshot_date=snapshot_date,
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
        client,
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
    range_header: Optional[str] = None,
    date: Optional[str] = None,
) -> Dict[str, Any]:
    return feed_tools.get_item_group_feed(
        client,
        feed_scope=feed_scope,
        category_id=category_id,
        marketplace_id=marketplace_id,
        range_header=range_header,
        date=date,
    )


# Marketing
@mcp.tool()
def marketing_get_merchandised_products(
    category_id: str,
    metric_name: str = "BEST_SELLING",
    limit: Optional[int] = None,
    aspect_filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    return marketing_tools.get_merchandised_products(
        client,
        category_id=category_id,
        metric_name=metric_name,
        limit=limit,
        aspect_filter=aspect_filter,
        marketplace_id=marketplace_id,
    )


# Offer (may require user token)
@mcp.tool()
def offer_get_bidding(item_id: str, marketplace_id: str) -> Dict[str, Any]:
    return offer_tools.get_bidding(client, item_id=item_id, marketplace_id=marketplace_id)


@mcp.tool()
def offer_place_proxy_bid(
    item_id: str,
    marketplace_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    adult_only_item_consent: Optional[bool] = None,
) -> Dict[str, Any]:
    return offer_tools.place_proxy_bid(
        client,
        item_id=item_id,
        marketplace_id=marketplace_id,
        max_amount_value=max_amount_value,
        max_amount_currency=max_amount_currency,
        adult_only_item_consent=adult_only_item_consent,
    )


# Order
@mcp.tool()
def order_initiate_guest_checkout_session(
    marketplace_id: str,
    contact_email: str,
    line_item_inputs: list[dict[str, Any]],
    shipping_address: dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.initiate_guest_checkout_session(
        client,
        marketplace_id=marketplace_id,
        contact_email=contact_email,
        line_item_inputs=line_item_inputs,
        shipping_address=shipping_address,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_get_guest_checkout_session(
    marketplace_id: str,
    checkout_session_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.get_guest_checkout_session(
        client,
        marketplace_id=marketplace_id,
        checkout_session_id=checkout_session_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_shipping_address(
    marketplace_id: str,
    checkout_session_id: str,
    shipping_address: dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.update_guest_shipping_address(
        client,
        marketplace_id=marketplace_id,
        checkout_session_id=checkout_session_id,
        shipping_address=shipping_address,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_shipping_option(
    marketplace_id: str,
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.update_guest_shipping_option(
        client,
        marketplace_id=marketplace_id,
        checkout_session_id=checkout_session_id,
        line_item_id=line_item_id,
        shipping_option_id=shipping_option_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_quantity(
    marketplace_id: str,
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.update_guest_quantity(
        client,
        marketplace_id=marketplace_id,
        checkout_session_id=checkout_session_id,
        line_item_id=line_item_id,
        quantity=quantity,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_apply_guest_coupon(
    marketplace_id: str,
    checkout_session_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.apply_guest_coupon(
        client,
        marketplace_id=marketplace_id,
        checkout_session_id=checkout_session_id,
        redemption_code=redemption_code,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_remove_guest_coupon(
    marketplace_id: str,
    checkout_session_id: str,
    redemption_code: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order_tools.remove_guest_coupon(
        client,
        marketplace_id=marketplace_id,
        checkout_session_id=checkout_session_id,
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
        client,
        purchase_order_id=purchase_order_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


if __name__ == "__main__":
    mcp.run()
