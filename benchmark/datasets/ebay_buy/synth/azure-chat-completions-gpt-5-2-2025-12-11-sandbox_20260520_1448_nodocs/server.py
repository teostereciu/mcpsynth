import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import EbayBuyApiClient
from generated_tools import browse as browse_tools
from generated_tools import deal as deal_tools
from generated_tools import feed as feed_tools
from generated_tools import order as order_tools


mcp = FastMCP("ebay-buy-api")


def _client() -> EbayBuyApiClient:
    return EbayBuyApiClient(
        app_id=os.getenv("EBAY_APP_ID"),
        cert_id=os.getenv("EBAY_CERT_ID"),
        environment=os.getenv("EBAY_ENVIRONMENT") or "SANDBOX",
    )


# Browse
@mcp.tool()
def browse_search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    fieldgroups: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    auto_correct: Optional[bool] = None,
) -> Dict[str, Any]:
    """Search for items (Browse API item_summary/search)."""
    try:
        return browse_tools.search_items(
            _client(),
            q=q,
            category_ids=category_ids,
            aspect_filter=aspect_filter,
            filter=filter,
            sort=sort,
            limit=limit,
            offset=offset,
            fieldgroups=fieldgroups,
            compatibility_filter=compatibility_filter,
            auto_correct=auto_correct,
        )
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item(item_id: str, fieldgroups: Optional[str] = None) -> Dict[str, Any]:
    """Get item details by RESTful item_id."""
    try:
        return browse_tools.get_item(_client(), item_id=item_id, fieldgroups=fieldgroups)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_group(item_group_id: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_group(_client(), item_group_id=item_group_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_items_by_item_group(item_group_id: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_items_by_item_group(_client(), item_group_id=item_group_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_by_legacy_id(legacy_item_id: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_by_legacy_id(_client(), legacy_item_id=legacy_item_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_by_epid(epid: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_by_epid(_client(), epid=epid)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_by_gtin(gtin: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_by_gtin(_client(), gtin=gtin)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_by_isbn(isbn: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_by_isbn(_client(), isbn=isbn)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_by_upc(upc: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_by_upc(_client(), upc=upc)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_by_product(product_id: str, product_id_type: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_by_product(_client(), product_id=product_id, product_id_type=product_id_type)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_check_item_compatibility(item_id: str, compatibility_properties: str) -> Dict[str, Any]:
    try:
        return browse_tools.check_item_compatibility(_client(), item_id=item_id, compatibility_properties=compatibility_properties)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_compatibility(item_id: str, compatibility_properties: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_compatibility(_client(), item_id=item_id, compatibility_properties=compatibility_properties)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_compatibility_properties(category_id: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_compatibility_properties(_client(), category_id=category_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_merchandised_products(category_id: str, metric_name: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    try:
        return browse_tools.get_merchandised_products(_client(), category_id=category_id, metric_name=metric_name, limit=limit)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_category_tree(_client(), category_tree_id=category_tree_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_category_subtree(_client(), category_tree_id=category_tree_id, category_id=category_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_category_suggestions(_client(), category_tree_id=category_tree_id, q=q)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_default_category_tree_id(_client(), marketplace_id=marketplace_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def browse_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    try:
        return browse_tools.get_item_aspects_for_category(_client(), category_tree_id=category_tree_id, category_id=category_id)
    except Exception as e:
        return {"error": str(e)}


# Deal
@mcp.tool()
def deal_get_deals(
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    try:
        return deal_tools.get_deals(
            _client(),
            marketplace_id=marketplace_id,
            limit=limit,
            offset=offset,
            category_ids=category_ids,
            filter=filter,
            sort=sort,
        )
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def deal_get_deal_item(deal_id: str, marketplace_id: str) -> Dict[str, Any]:
    try:
        return deal_tools.get_deal_item(_client(), deal_id=deal_id, marketplace_id=marketplace_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def deal_get_deal_events(marketplace_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    try:
        return deal_tools.get_deal_events(_client(), marketplace_id=marketplace_id, limit=limit, offset=offset)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def deal_get_deal_event(event_id: str, marketplace_id: str) -> Dict[str, Any]:
    try:
        return deal_tools.get_deal_event(_client(), event_id=event_id, marketplace_id=marketplace_id)
    except Exception as e:
        return {"error": str(e)}


# Feed
@mcp.tool()
def feed_get_item_snapshot_feed(
    feed_scope: str,
    marketplace_id: str,
    date: Optional[str] = None,
    category_id: Optional[str] = None,
) -> Dict[str, Any]:
    try:
        return feed_tools.get_item_snapshot_feed(
            _client(),
            feed_scope=feed_scope,
            marketplace_id=marketplace_id,
            date=date,
            category_id=category_id,
        )
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def feed_get_item_snapshot_feed_file(file_id: str) -> Dict[str, Any]:
    try:
        return feed_tools.get_item_snapshot_feed_file(_client(), file_id=file_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def feed_get_item_feed(
    feed_type: str,
    marketplace_id: str,
    date: Optional[str] = None,
    category_id: Optional[str] = None,
) -> Dict[str, Any]:
    try:
        return feed_tools.get_item_feed(
            _client(),
            feed_type=feed_type,
            marketplace_id=marketplace_id,
            date=date,
            category_id=category_id,
        )
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def feed_get_item_feed_file(file_id: str) -> Dict[str, Any]:
    try:
        return feed_tools.get_item_feed_file(_client(), file_id=file_id)
    except Exception as e:
        return {"error": str(e)}


# Order
@mcp.tool()
def order_initiate_checkout_session(payload: Dict[str, Any], marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    try:
        return order_tools.initiate_checkout_session(_client(), payload=payload, marketplace_id=marketplace_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def order_get_checkout_session(checkout_session_id: str) -> Dict[str, Any]:
    try:
        return order_tools.get_checkout_session(_client(), checkout_session_id=checkout_session_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def order_update_shipping_address(checkout_session_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return order_tools.update_shipping_address(_client(), checkout_session_id=checkout_session_id, payload=payload)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def order_update_quantity(checkout_session_id: str, line_item_id: str, quantity: int) -> Dict[str, Any]:
    try:
        return order_tools.update_quantity(_client(), checkout_session_id=checkout_session_id, line_item_id=line_item_id, quantity=quantity)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def order_apply_coupon(checkout_session_id: str, coupon_code: str) -> Dict[str, Any]:
    try:
        return order_tools.apply_coupon(_client(), checkout_session_id=checkout_session_id, coupon_code=coupon_code)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def order_remove_coupon(checkout_session_id: str) -> Dict[str, Any]:
    try:
        return order_tools.remove_coupon(_client(), checkout_session_id=checkout_session_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def order_place_order(checkout_session_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return order_tools.place_order(_client(), checkout_session_id=checkout_session_id, payload=payload)
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
