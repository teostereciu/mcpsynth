from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import EbayClient
from generated_tools import browse, deal, feed, marketing, offer, order


mcp = FastMCP("ebay-buy-api")
client = EbayClient()


@mcp.tool()
def browse_search(
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
    return browse.browse_search(
        client,
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
def browse_search_by_image(
    image_url: str,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return browse.browse_search_by_image(
        client,
        image_url=image_url,
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
def browse_get_item(
    item_id: str,
    fieldgroups: Optional[str] = None,
    if_none_match: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    return browse.browse_get_item(
        client,
        item_id,
        fieldgroups=fieldgroups,
        if_none_match=if_none_match,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def browse_get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    return browse.browse_get_item_by_legacy_id(
        client,
        legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def browse_get_items(
    item_ids: Optional[List[str]] = None,
    item_group_ids: Optional[List[str]] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    return browse.browse_get_items(client, item_ids=item_ids, item_group_ids=item_group_ids, marketplace_id=marketplace_id)


@mcp.tool()
def browse_get_items_by_item_group(
    item_group_id: str,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    return browse.browse_get_items_by_item_group(client, item_group_id, marketplace_id=marketplace_id)


@mcp.tool()
def browse_check_compatibility(
    item_id: str,
    compatibility_properties: List[Dict[str, str]],
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    return browse.browse_check_compatibility(
        client,
        item_id,
        compatibility_properties=compatibility_properties,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def deal_get_events(
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal.deal_get_events(client, marketplace_id=marketplace_id, limit=limit, offset=offset, enduserctx=enduserctx)


@mcp.tool()
def deal_get_event(
    event_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal.deal_get_event(client, event_id, marketplace_id=marketplace_id, enduserctx=enduserctx)


@mcp.tool()
def deal_get_event_items(
    event_id: str,
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal.deal_get_event_items(
        client,
        event_id,
        marketplace_id=marketplace_id,
        limit=limit,
        offset=offset,
        enduserctx=enduserctx,
    )


@mcp.tool()
def deal_get_deal_items(
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return deal.deal_get_deal_items(client, marketplace_id=marketplace_id, limit=limit, offset=offset, enduserctx=enduserctx)


@mcp.tool()
def feed_get_item_feed(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed.feed_get_item_feed(
        client,
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
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed.feed_get_item_group_feed(
        client,
        feed_scope=feed_scope,
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def feed_get_item_priority_feed(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed.feed_get_item_priority_feed(
        client,
        feed_scope=feed_scope,
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def feed_get_item_snapshot_feed(
    snapshot_date: str,
    marketplace_id: str,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    return feed.feed_get_item_snapshot_feed(
        client,
        snapshot_date=snapshot_date,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


@mcp.tool()
def marketing_get_merchandised_products(
    category_id: str,
    metric_name: str = "BEST_SELLING",
    limit: Optional[int] = None,
    aspect_filter: Optional[str] = None,
) -> Dict[str, Any]:
    return marketing.marketing_get_merchandised_products(
        client,
        category_id=category_id,
        metric_name=metric_name,
        limit=limit,
        aspect_filter=aspect_filter,
    )


@mcp.tool()
def offer_get_bidding(
    item_id: str,
    marketplace_id: str,
) -> Dict[str, Any]:
    return offer.offer_get_bidding(client, item_id, marketplace_id=marketplace_id)


@mcp.tool()
def offer_place_proxy_bid(
    item_id: str,
    marketplace_id: str,
    max_amount_currency: str,
    max_amount_value: str,
    adult_only_item_consent: Optional[bool] = None,
) -> Dict[str, Any]:
    return offer.offer_place_proxy_bid(
        client,
        item_id,
        marketplace_id=marketplace_id,
        max_amount_currency=max_amount_currency,
        max_amount_value=max_amount_value,
        adult_only_item_consent=adult_only_item_consent,
    )


@mcp.tool()
def order_initiate_guest_checkout_session(
    marketplace_id: str,
    contact_email: str,
    line_item_inputs: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order.order_initiate_guest_checkout_session(
        client,
        marketplace_id=marketplace_id,
        contact_email=contact_email,
        line_item_inputs=line_item_inputs,
        shipping_address=shipping_address,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_get_guest_checkout_session(
    checkout_session_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order.order_get_guest_checkout_session(
        client,
        checkout_session_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order.order_update_guest_quantity(
        client,
        checkout_session_id,
        line_item_id,
        quantity,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_shipping_address(
    checkout_session_id: str,
    shipping_address: Dict[str, Any],
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order.order_update_guest_shipping_address(
        client,
        checkout_session_id,
        shipping_address,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order.order_update_guest_shipping_option(
        client,
        checkout_session_id,
        line_item_id,
        shipping_option_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_apply_guest_coupon(
    checkout_session_id: str,
    coupon_code: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order.order_apply_guest_coupon(
        client,
        checkout_session_id,
        coupon_code,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_remove_guest_coupon(
    checkout_session_id: str,
    coupon_code: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order.order_remove_guest_coupon(
        client,
        checkout_session_id,
        coupon_code,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


@mcp.tool()
def order_get_guest_purchase_order(
    purchase_order_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    return order.order_get_guest_purchase_order(
        client,
        purchase_order_id,
        marketplace_id=marketplace_id,
        enduserctx=enduserctx,
    )


if __name__ == "__main__":
    mcp.run()
