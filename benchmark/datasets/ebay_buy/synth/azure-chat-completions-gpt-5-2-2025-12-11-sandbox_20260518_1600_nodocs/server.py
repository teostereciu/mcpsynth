from __future__ import annotations

from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools import browse, deal, feed, order

mcp = FastMCP("ebay-buy-api")


@mcp.tool()
def browse_search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    auto_correct: Optional[bool] = None,
    charity_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    buyer_postal_code: Optional[str] = None,
) -> Dict[str, Any]:
    return browse.search_items(
        q=q,
        category_ids=category_ids,
        filter=filter,
        sort=sort,
        limit=limit,
        offset=offset,
        aspect_filter=aspect_filter,
        fieldgroups=fieldgroups,
        compatibility_filter=compatibility_filter,
        auto_correct=auto_correct,
        charity_ids=charity_ids,
        epid=epid,
        gtin=gtin,
        buyer_postal_code=buyer_postal_code,
    )


@mcp.tool()
def browse_get_item(item_id: str, fieldgroups: Optional[str] = None) -> Dict[str, Any]:
    return browse.get_item(item_id=item_id, fieldgroups=fieldgroups)


@mcp.tool()
def browse_get_item_by_legacy_id(legacy_item_id: str) -> Dict[str, Any]:
    return browse.get_item_by_legacy_id(legacy_item_id=legacy_item_id)


@mcp.tool()
def browse_get_items_by_item_group(item_group_id: str) -> Dict[str, Any]:
    return browse.get_items_by_item_group(item_group_id=item_group_id)


@mcp.tool()
def browse_get_item_group(item_group_id: str) -> Dict[str, Any]:
    return browse.get_item_group(item_group_id=item_group_id)


@mcp.tool()
def browse_check_item_compatibility(item_id: str, compatibility_properties: str) -> Dict[str, Any]:
    return browse.check_item_compatibility(item_id=item_id, compatibility_properties=compatibility_properties)


@mcp.tool()
def browse_get_item_compatibility(item_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return browse.get_item_compatibility(item_id=item_id, limit=limit, offset=offset)


@mcp.tool()
def browse_get_item_merchandising(item_id: str) -> Dict[str, Any]:
    return browse.get_item_merchandising(item_id=item_id)


@mcp.tool()
def browse_get_item_location(item_id: str) -> Dict[str, Any]:
    return browse.get_item_location(item_id=item_id)


@mcp.tool()
def deal_get_deals(limit: Optional[int] = None, offset: Optional[int] = None, sort: Optional[str] = None, filter: Optional[str] = None) -> Dict[str, Any]:
    return deal.get_deals(limit=limit, offset=offset, sort=sort, filter=filter)


@mcp.tool()
def deal_get_deal_item(deal_item_id: str) -> Dict[str, Any]:
    return deal.get_deal_item(deal_item_id=deal_item_id)


@mcp.tool()
def deal_get_events(limit: Optional[int] = None, offset: Optional[int] = None, sort: Optional[str] = None, filter: Optional[str] = None) -> Dict[str, Any]:
    return deal.get_events(limit=limit, offset=offset, sort=sort, filter=filter)


@mcp.tool()
def deal_get_event(event_id: str) -> Dict[str, Any]:
    return deal.get_event(event_id=event_id)


@mcp.tool()
def feed_get_item_feed(feed_type: str, date: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return feed.get_item_feed(feed_type=feed_type, date=date, limit=limit, offset=offset)


@mcp.tool()
def feed_get_item_snapshot(feed_scope: str, date: Optional[str] = None) -> Dict[str, Any]:
    return feed.get_item_snapshot(feed_scope=feed_scope, date=date)


@mcp.tool()
def feed_get_item_snapshot_feed(feed_scope: str, date: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return feed.get_item_snapshot_feed(feed_scope=feed_scope, date=date, limit=limit, offset=offset)


@mcp.tool()
def order_initiate_checkout_session(payload: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order.initiate_checkout_session(payload=payload, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_get_checkout_session(checkout_session_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order.get_checkout_session(checkout_session_id=checkout_session_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_update_shipping_address(checkout_session_id: str, payload: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order.update_shipping_address(checkout_session_id=checkout_session_id, payload=payload, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_update_quantity(checkout_session_id: str, payload: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order.update_quantity(checkout_session_id=checkout_session_id, payload=payload, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_apply_coupon(checkout_session_id: str, payload: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order.apply_coupon(checkout_session_id=checkout_session_id, payload=payload, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_remove_coupon(checkout_session_id: str, payload: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order.remove_coupon(checkout_session_id=checkout_session_id, payload=payload, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_place_order(checkout_session_id: str, payload: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order.place_order(checkout_session_id=checkout_session_id, payload=payload, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


if __name__ == "__main__":
    mcp.run()
