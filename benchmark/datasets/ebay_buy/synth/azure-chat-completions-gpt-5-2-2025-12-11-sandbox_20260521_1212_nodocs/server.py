from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.ebay_client import EbayClient
from generated_tools import browse as browse_tools
from generated_tools import deal as deal_tools
from generated_tools import feed as feed_tools
from generated_tools import order as order_tools


mcp = FastMCP("ebay-buy-api")
client = EbayClient()


@mcp.tool()
def browse_search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    epn_category_id: Optional[str] = None,
    charity_ids: Optional[str] = None,
    auto_correct: Optional[bool] = None,
    compatibility_filter: Optional[str] = None,
    buyer_postal_code: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    return browse_tools.search_items(
        client,
        q=q,
        category_ids=category_ids,
        limit=limit,
        offset=offset,
        sort=sort,
        filter=filter,
        fieldgroups=fieldgroups,
        aspect_filter=aspect_filter,
        epn_category_id=epn_category_id,
        charity_ids=charity_ids,
        auto_correct=auto_correct,
        compatibility_filter=compatibility_filter,
        buyer_postal_code=buyer_postal_code,
        x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
    )


@mcp.tool()
def browse_get_item(item_id: str, fieldgroups: Optional[str] = None, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return browse_tools.get_item(client, item_id, fieldgroups=fieldgroups, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def browse_get_item_by_legacy_id(legacy_item_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return browse_tools.get_item_by_legacy_id(client, legacy_item_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def browse_get_item_group(item_group_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return browse_tools.get_item_group(client, item_group_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def browse_get_items_by_item_group(item_group_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return browse_tools.get_items_by_item_group(client, item_group_id, x__ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def browse_get_item_snapshot(item_id: str, snapshot_id: Optional[str] = None, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return browse_tools.get_item_snapshot(client, item_id, snapshot_id=snapshot_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def browse_check_compatibility(item_id: str, compatibility_filter: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return browse_tools.check_compatibility(client, item_id, compatibility_filter=compatibility_filter, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def browse_get_merchandised_products(
    category_id: Optional[str] = None,
    metric_name: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    return browse_tools.get_merchandised_products(
        client,
        category_id=category_id,
        metric_name=metric_name,
        limit=limit,
        offset=offset,
        filter=filter,
        x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
    )


@mcp.tool()
def browse_get_item_summary_by_gtin(gtin: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return browse_tools.get_item_summary_by_gtin(client, gtin, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def browse_get_item_summary_by_epid(epid: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return browse_tools.get_item_summary_by_epid(client, epid, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def browse_get_item_summary_by_product(
    gtin: Optional[str] = None,
    epid: Optional[str] = None,
    mpn: Optional[str] = None,
    brand: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    return browse_tools.get_item_summary_by_product(
        client,
        gtin=gtin,
        epid=epid,
        mpn=mpn,
        brand=brand,
        x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
    )


@mcp.tool()
def deal_get_deals(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    filter: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    return deal_tools.get_deals(client, limit=limit, offset=offset, sort=sort, filter=filter, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def deal_get_deal(deal_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return deal_tools.get_deal(client, deal_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def deal_get_events(limit: Optional[int] = None, offset: Optional[int] = None, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return deal_tools.get_events(client, limit=limit, offset=offset, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def deal_get_event(event_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return deal_tools.get_event(client, event_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def feed_get_item_feed(feed_type: str, date: Optional[str] = None, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return feed_tools.get_item_feed(client, feed_type, date=date, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def feed_get_item_snapshot_feed(snapshot_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return feed_tools.get_item_snapshot_feed(client, snapshot_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def feed_get_item_snapshot_status(snapshot_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return feed_tools.get_item_snapshot_status(client, snapshot_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def feed_get_item_snapshot_download(snapshot_id: str, range_header: Optional[str] = None, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return feed_tools.get_item_snapshot_download(client, snapshot_id, range_header=range_header, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_initiate_checkout_session(body: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order_tools.initiate_checkout_session(client, body=body, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_get_checkout_session(checkout_session_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order_tools.get_checkout_session(client, checkout_session_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_update_shipping_address(checkout_session_id: str, body: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order_tools.update_shipping_address(client, checkout_session_id, body=body, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_update_quantity(checkout_session_id: str, line_item_id: str, body: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order_tools.update_quantity(client, checkout_session_id, line_item_id, body=body, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_apply_coupon(checkout_session_id: str, body: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order_tools.apply_coupon(client, checkout_session_id, body=body, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_remove_coupon(checkout_session_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order_tools.remove_coupon(client, checkout_session_id, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


@mcp.tool()
def order_place_order(checkout_session_id: str, body: Dict[str, Any], x_ebay_c_marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return order_tools.place_order(client, checkout_session_id, body=body, x_ebay_c_marketplace_id=x_ebay_c_marketplace_id)


if __name__ == "__main__":
    mcp.run()
