import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-buy-api")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _env() -> str:
    return os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()


def _base_url() -> str:
    return BASE_URLS.get(_env(), BASE_URLS["SANDBOX"])


def _token() -> str:
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    if not app_id or not cert_id:
        raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")
    auth = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    resp = requests.post(
        "https://api.ebay.com/identity/v1/oauth2/token",
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/buy.guest.order"},
        timeout=30,
    )
    if not resp.ok:
        raise RuntimeError(f"Token request failed: {resp.status_code} {resp.text}")
    return resp.json()["access_token"]


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None, headers: Optional[Dict[str, str]] = None) -> Any:
    try:
        token = _token()
        h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        if headers:
            h.update(headers)
        resp = requests.request(method, _base_url() + path, params=params, json=json_body, headers=h, timeout=60)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text, "status": resp.status_code}
        if resp.status_code == 204:
            return {"ok": True}
        ctype = resp.headers.get("Content-Type", "")
        return resp.json() if "json" in ctype else {"content": resp.text}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_items(q: Optional[str] = None, category_ids: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, fieldgroups: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"q": q, "category_ids": category_ids, "limit": limit, "offset": offset, "fieldgroups": fieldgroups, "filter": filter, "sort": sort}.items() if v is not None}
    return _request("GET", "/buy/browse/v1/item_summary/search", params=params)


@mcp.tool()
def search_items_by_image(image_url: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"image_url": image_url, "limit": limit, "offset": offset}.items() if v is not None}
    return _request("GET", "/buy/browse/v1/item_summary/search_by_image", params=params)


@mcp.tool()
def get_item(listing_id: str, fieldgroups: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"fieldgroups": fieldgroups}.items() if v is not None}
    return _request("GET", f"/buy/browse/v1/item/{listing_id}", params=params)


@mcp.tool()
def get_item_by_legacy_id(legacy_item_id: str, legacy_variation_id: Optional[str] = None, fieldgroups: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"legacy_item_id": legacy_item_id, "legacy_variation_id": legacy_variation_id, "fieldgroups": fieldgroups}.items() if v is not None}
    return _request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params=params)


@mcp.tool()
def get_items(item_ids: str, fieldgroups: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"item_ids": item_ids, "fieldgroups": fieldgroups}.items() if v is not None}
    return _request("GET", "/buy/browse/v1/item/get_items", params=params)


@mcp.tool()
def get_items_by_item_group(item_group_id: str, fieldgroups: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"item_group_id": item_group_id, "fieldgroups": fieldgroups}.items() if v is not None}
    return _request("GET", "/buy/browse/v1/item/get_items_by_item_group", params=params)


@mcp.tool()
def check_compatibility(listing_id: str, compatibility_filter: str) -> Any:
    return _request("GET", f"/buy/browse/v1/item/{listing_id}/check_compatibility", params={"compatibility_filter": compatibility_filter})


@mcp.tool()
def get_deal_items(marketplace_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}.items() if v is not None}
    return _request("GET", "/buy/deal/v1/deal_item", params=params)


@mcp.tool()
def get_events(marketplace_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}.items() if v is not None}
    return _request("GET", "/buy/deal/v1/event", params=params)


@mcp.tool()
def get_event(event_id: str) -> Any:
    return _request("GET", f"/buy/deal/v1/event/{event_id}")


@mcp.tool()
def get_event_items(event_id: str, marketplace_id: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"marketplace_id": marketplace_id}.items() if v is not None}
    return _request("GET", f"/buy/deal/v1/event/{event_id}/item", params=params)


@mcp.tool()
def get_item_feed(feed_type: str, marketplace_id: str) -> Any:
    return _request("GET", "/buy/feed/v1/item", params={"feed_type": feed_type, "marketplace_id": marketplace_id})


@mcp.tool()
def get_item_group_feed(feed_type: str, marketplace_id: str) -> Any:
    return _request("GET", "/buy/feed/v1/item_group", params={"feed_type": feed_type, "marketplace_id": marketplace_id})


@mcp.tool()
def get_item_priority_feed(feed_type: str, marketplace_id: str) -> Any:
    return _request("GET", "/buy/feed/v1/item_priority", params={"feed_type": feed_type, "marketplace_id": marketplace_id})


@mcp.tool()
def get_item_snapshot_feed(feed_type: str, marketplace_id: str) -> Any:
    return _request("GET", "/buy/feed/v1/item_snapshot", params={"feed_type": feed_type, "marketplace_id": marketplace_id})


@mcp.tool()
def get_merchandised_products(marketplace_id: str, aspect_filter: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"marketplace_id": marketplace_id, "aspect_filter": aspect_filter}.items() if v is not None}
    return _request("GET", "/buy/marketing/v1/merchandised_product", params=params)


@mcp.tool()
def get_bidding(item_id: str) -> Any:
    return _request("GET", "/buy/offer/v1/bidding", params={"item_id": item_id})


@mcp.tool()
def place_proxy_bid(item_id: str, max_bid: Dict[str, Any]) -> Any:
    return _request("POST", "/buy/offer/v1/bidding/place_proxy_bid", json_body={"itemId": item_id, "maxBid": max_bid})


@mcp.tool()
def initiate_guest_checkout_session(contact_email: str, line_item_inputs: list, shipping_address: dict) -> Any:
    return _request("POST", "/buy/order/v2/guest_checkout_session/initiate", json_body={"contactEmail": contact_email, "lineItemInputs": line_item_inputs, "shippingAddress": shipping_address}, headers={"Content-Type": "application/json"})


@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str) -> Any:
    return _request("GET", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}")


@mcp.tool()
def apply_guest_coupon(checkout_session_id: str, coupon_code: str) -> Any:
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon", json_body={"couponCode": coupon_code}, headers={"Content-Type": "application/json"})


@mcp.tool()
def remove_guest_coupon(checkout_session_id: str, coupon_code: str) -> Any:
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon", json_body={"couponCode": coupon_code}, headers={"Content-Type": "application/json"})


@mcp.tool()
def update_guest_quantity(checkout_session_id: str, line_item_id: str, quantity: int) -> Any:
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity", json_body={"lineItemId": line_item_id, "quantity": quantity}, headers={"Content-Type": "application/json"})


@mcp.tool()
def update_guest_shipping_address(checkout_session_id: str, shipping_address: dict) -> Any:
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address", json_body={"shippingAddress": shipping_address}, headers={"Content-Type": "application/json"})


@mcp.tool()
def update_guest_shipping_option(checkout_session_id: str, line_item_id: str, shipping_option_id: str) -> Any:
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option", json_body={"lineItemId": line_item_id, "shippingOptionId": shipping_option_id}, headers={"Content-Type": "application/json"})


@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str) -> Any:
    return _request("GET", f"/buy/order/v2/guest_purchase_order/{purchase_order_id}")
