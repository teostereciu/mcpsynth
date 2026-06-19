import os
import json
import requests
from typing import Any, Dict

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
        raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID")
    resp = requests.post(
        f"{_base_url()}/identity/v1/oauth2/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        auth=(app_id, cert_id),
        data={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/buy.guest.order"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def _request(method: str, path: str, params=None, json_body=None, headers=None) -> Dict[str, Any]:
    token = _token()
    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if headers:
        h.update(headers)
    resp = requests.request(method, f"{_base_url()}{path}", params=params, json=json_body, headers=h, timeout=30)
    try:
        data = resp.json()
    except Exception:
        data = resp.text
    if resp.status_code >= 400:
        return {"error": data if isinstance(data, str) else data, "status": resp.status_code}
    return data


def search_items(q=None, category_ids=None, limit=None, offset=None, sort=None, fieldgroups=None, filter=None, aspect_filter=None, compatibility_filter=None, gtin=None, epid=None):
    params = {k: v for k, v in {"q": q, "category_ids": category_ids, "limit": limit, "offset": offset, "sort": sort, "fieldgroups": fieldgroups, "filter": filter, "aspect_filter": aspect_filter, "compatibility_filter": compatibility_filter, "gtin": gtin, "epid": epid}.items() if v is not None}
    return _request("GET", "/buy/browse/v1/item_summary/search", params=params)


def search_items_by_image(image_url):
    return _request("GET", "/buy/browse/v1/item_summary/search_by_image", params={"image_url": image_url})


def get_item(item_id, fieldgroups=None):
    params = {k: v for k, v in {"fieldgroups": fieldgroups}.items() if v is not None}
    return _request("GET", f"/buy/browse/v1/item/{item_id}", params=params)


def get_item_by_legacy_id(legacy_item_id, legacy_variation_id=None, legacy_sku=None):
    params = {k: v for k, v in {"legacy_item_id": legacy_item_id, "legacy_variation_id": legacy_variation_id, "legacy_sku": legacy_sku}.items() if v is not None}
    return _request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params=params)


def get_items(item_ids):
    return _request("GET", "/buy/browse/v1/item/get_items", params={"item_ids": item_ids})


def get_items_by_item_group(item_group_id):
    return _request("GET", "/buy/browse/v1/item/get_items_by_item_group", params={"item_group_id": item_group_id})


def check_compatibility(item_id, compatibility_filter):
    return _request("POST", f"/buy/browse/v1/item/{item_id}/check_compatibility", json_body=compatibility_filter)


def get_deal_items(limit=None, offset=None, marketplace_id=None):
    params = {k: v for k, v in {"limit": limit, "offset": offset, "marketplace_id": marketplace_id}.items() if v is not None}
    return _request("GET", "/buy/deal/v1/deal_item", params=params)


def get_events(limit=None, offset=None, marketplace_id=None):
    params = {k: v for k, v in {"limit": limit, "offset": offset, "marketplace_id": marketplace_id}.items() if v is not None}
    return _request("GET", "/buy/deal/v1/event", params=params)


def get_event(event_id):
    return _request("GET", f"/buy/deal/v1/event/{event_id}")


def get_event_items(event_id, limit=None, offset=None):
    params = {k: v for k, v in {"limit": limit, "offset": offset}.items() if v is not None}
    return _request("GET", f"/buy/deal/v1/event/{event_id}/item", params=params)


def get_item_feed(feed_type=None):
    return _request("GET", "/buy/feed/v1/item_feed", params={"feed_type": feed_type} if feed_type else None)


def get_item_group_feed(feed_type=None):
    return _request("GET", "/buy/feed/v1/item_group_feed", params={"feed_type": feed_type} if feed_type else None)


def get_item_priority_feed(feed_type=None):
    return _request("GET", "/buy/feed/v1/item_priority_feed", params={"feed_type": feed_type} if feed_type else None)


def get_item_snapshot_feed(feed_type=None):
    return _request("GET", "/buy/feed/v1/item_snapshot_feed", params={"feed_type": feed_type} if feed_type else None)


def get_merchandised_products(category_id=None, limit=None, offset=None):
    params = {k: v for k, v in {"category_id": category_id, "limit": limit, "offset": offset}.items() if v is not None}
    return _request("GET", "/buy/marketing/v1/merchandised_product", params=params)


def get_bidding(item_id):
    return _request("GET", f"/buy/offer/v1/bidding/{item_id}")


def place_proxy_bid(item_id, bid):
    return _request("POST", f"/buy/offer/v1/bidding/{item_id}/place_proxy_bid", json_body=bid)


def initiate_guest_checkout_session(payload):
    return _request("POST", "/buy/order/v2/guest_checkout_session/initiate", json_body=payload, headers={"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": payload.get("marketplaceId", "EBAY_US")})


def get_guest_checkout_session(checkout_session_id):
    return _request("GET", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}")


def apply_guest_coupon(checkout_session_id, payload):
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon", json_body=payload)


def remove_guest_coupon(checkout_session_id, coupon_code):
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon", json_body={"couponCode": coupon_code})


def update_guest_quantity(checkout_session_id, payload):
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity", json_body=payload)


def update_guest_shipping_address(checkout_session_id, payload):
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address", json_body=payload)


def update_guest_shipping_option(checkout_session_id, payload):
    return _request("POST", f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option", json_body=payload)


def get_guest_purchase_order(purchase_order_id):
    return _request("GET", f"/buy/order/v2/guest_purchase_order/{purchase_order_id}")
