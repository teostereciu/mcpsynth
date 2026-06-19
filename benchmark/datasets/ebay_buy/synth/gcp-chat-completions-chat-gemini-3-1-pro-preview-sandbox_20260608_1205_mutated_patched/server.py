import os
import base64
import requests
from typing import Optional, Dict, Any, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-buy-api")

EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

if EBAY_ENVIRONMENT == "PRODUCTION":
    BASE_URL = "https://api.ebay.com"
else:
    BASE_URL = "https://api.sandbox.ebay.com"

_token_cache = None

def get_access_token() -> str:
    global _token_cache
    if _token_cache:
        return _token_cache
    
    if not EBAY_APP_ID or not EBAY_CERT_ID:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID environment variables must be set")
        
    auth_str = f"{EBAY_APP_ID}:{EBAY_CERT_ID}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {b64_auth}"
    }
    
    scopes = [
        "https://api.ebay.com/oauth/api_scope",
        "https://api.ebay.com/oauth/api_scope/buy.item.bulk",
        "https://api.ebay.com/oauth/api_scope/buy.deal",
        "https://api.ebay.com/oauth/api_scope/buy.item.feed",
        "https://api.ebay.com/oauth/api_scope/buy.marketing",
        "https://api.ebay.com/oauth/api_scope/buy.offer.auction",
        "https://api.ebay.com/oauth/api_scope/buy.guest.order"
    ]
    
    data = {
        "grant_type": "client_credentials",
        "scope": " ".join(scopes)
    }
    
    response = requests.post(f"{BASE_URL}/identity/v1/oauth2/token", headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(f"Failed to get access token: {response.text}")
        
    _token_cache = response.json()["access_token"]
    return _token_cache

def make_request(method: str, path: str, params: Optional[Dict] = None, json_data: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict[str, Any]:
    try:
        token = get_access_token()
    except Exception as e:
        return {"error": str(e)}
        
    req_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if headers:
        req_headers.update(headers)
    
    url = f"{BASE_URL}{path}"
    
    try:
        response = requests.request(method, url, headers=req_headers, params=params, json=json_data)
        if response.status_code == 204:
            return {"status": "success"}
        try:
            return response.json()
        except ValueError:
            if response.status_code >= 400:
                return {"error": f"HTTP {response.status_code}: {response.text}"}
            return {"text": response.text}
    except Exception as e:
        return {"error": str(e)}

# Browse API
@mcp.tool()
def get_item(item_id: str) -> Dict[str, Any]:
    """Get details of a specific item."""
    return make_request("GET", f"/buy/browse/v1/item/{item_id}")

@mcp.tool()
def get_item_by_legacy_id(legacy_item_id: str) -> Dict[str, Any]:
    """Get details of an item by its legacy ID."""
    return make_request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params={"legacy_item_id": legacy_item_id})

@mcp.tool()
def get_items(item_group_ids: Optional[str] = None, item_ids: Optional[str] = None) -> Dict[str, Any]:
    """Get details of multiple items."""
    params = {}
    if item_group_ids: params["item_group_ids"] = item_group_ids
    if item_ids: params["item_ids"] = item_ids
    return make_request("GET", "/buy/browse/v1/item", params=params)

@mcp.tool()
def get_items_by_item_group(item_group_id: str) -> Dict[str, Any]:
    """Get items belonging to a specific item group."""
    return make_request("GET", "/buy/browse/v1/item/get_items_by_item_group", params={"item_group_id": item_group_id})

@mcp.tool()
def search(q: Optional[str] = None, category_ids: Optional[str] = None, limit: Optional[str] = None, offset: Optional[str] = None) -> Dict[str, Any]:
    """Search for items."""
    params = {}
    if q: params["q"] = q
    if category_ids: params["category_ids"] = category_ids
    if limit: params["limit"] = limit
    if offset: params["offset"] = offset
    return make_request("GET", "/buy/browse/v1/item_summary/search", params=params)

@mcp.tool()
def check_compatibility(item_id: str, compatibility_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Check compatibility of an item."""
    return make_request("POST", f"/buy/browse/v1/item/{item_id}/check_compatibility", json_data=compatibility_payload)

# Deal API
@mcp.tool()
def get_deal_items(category_ids: Optional[str] = None, limit: Optional[str] = None, offset: Optional[str] = None) -> Dict[str, Any]:
    """Get deal items."""
    params = {}
    if category_ids: params["category_ids"] = category_ids
    if limit: params["limit"] = limit
    if offset: params["offset"] = offset
    return make_request("GET", "/buy/deal/v1/deal_item", params=params)

@mcp.tool()
def get_event_items(event_ids: str, category_ids: Optional[str] = None, limit: Optional[str] = None, offset: Optional[str] = None) -> Dict[str, Any]:
    """Get items for a specific event."""
    params = {"event_ids": event_ids}
    if category_ids: params["category_ids"] = category_ids
    if limit: params["limit"] = limit
    if offset: params["offset"] = offset
    return make_request("GET", "/buy/deal/v1/event_item", params=params)

@mcp.tool()
def get_event(event_id: str) -> Dict[str, Any]:
    """Get details of a specific event."""
    return make_request("GET", f"/buy/deal/v1/event/{event_id}")

@mcp.tool()
def get_events(limit: Optional[str] = None, offset: Optional[str] = None) -> Dict[str, Any]:
    """Get a list of events."""
    params = {}
    if limit: params["limit"] = limit
    if offset: params["offset"] = offset
    return make_request("GET", "/buy/deal/v1/event", params=params)

# Feed API
@mcp.tool()
def get_item_group_feed(feed_scope: str, category_id: str, date: str) -> Dict[str, Any]:
    """Get item group feed."""
    params = {"feed_scope": feed_scope, "category_id": category_id, "date": date}
    return make_request("GET", "/buy/feed/v1/item_group", params=params)

@mcp.tool()
def get_item_feed(feed_scope: str, category_id: str, date: str) -> Dict[str, Any]:
    """Get item feed."""
    params = {"feed_scope": feed_scope, "category_id": category_id, "date": date}
    return make_request("GET", "/buy/feed/v1/item", params=params)

@mcp.tool()
def get_item_priority_feed(feed_scope: str, category_id: str, date: str) -> Dict[str, Any]:
    """Get item priority feed."""
    params = {"feed_scope": feed_scope, "category_id": category_id, "date": date}
    return make_request("GET", "/buy/feed/v1/item_priority", params=params)

@mcp.tool()
def get_item_snapshot_feed(feed_scope: str, category_id: str, date: str) -> Dict[str, Any]:
    """Get item snapshot feed."""
    params = {"feed_scope": feed_scope, "category_id": category_id, "date": date}
    return make_request("GET", "/buy/feed/v1/item_snapshot", params=params)

# Marketing API
@mcp.tool()
def get_merchandised_products(category_id: str, metric_name: str) -> Dict[str, Any]:
    """Get merchandised products."""
    params = {"category_id": category_id, "metric_name": metric_name}
    return make_request("GET", "/buy/marketing/v1/merchandised_product", params=params)

# Offer API
@mcp.tool()
def get_bidding(item_id: str) -> Dict[str, Any]:
    """Get bidding details for an item."""
    return make_request("GET", f"/buy/offer/v1/bidding/{item_id}")

@mcp.tool()
def place_proxy_bid(item_id: str, max_amount: Dict[str, Any]) -> Dict[str, Any]:
    """Place a proxy bid on an item."""
    return make_request("POST", f"/buy/offer/v1/bidding/{item_id}/place_proxy_bid", json_data={"maxAmount": max_amount})

# Order API
@mcp.tool()
def apply_guest_coupon(checkout_session_id: str, coupon_code: str) -> Dict[str, Any]:
    """Apply a coupon to a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/apply_guest_coupon", json_data={"couponCode": coupon_code})

@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str) -> Dict[str, Any]:
    """Get details of a guest checkout session."""
    return make_request("GET", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}")

@mcp.tool()
def initiate_guest_checkout_session(contact_email: str, line_item_inputs: List[Dict[str, Any]], shipping_address: Dict[str, Any]) -> Dict[str, Any]:
    """Initiate a guest checkout session."""
    payload = {
        "contactEmail": contact_email,
        "lineItemInputs": line_item_inputs,
        "shippingAddress": shipping_address
    }
    return make_request("POST", "/buy/order/v1/guest_checkout_session/initiate", json_data=payload)

@mcp.tool()
def remove_guest_coupon(checkout_session_id: str, coupon_code: str) -> Dict[str, Any]:
    """Remove a coupon from a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/remove_guest_coupon", json_data={"couponCode": coupon_code})

@mcp.tool()
def update_guest_quantity(checkout_session_id: str, line_item_id: str, quantity: int) -> Dict[str, Any]:
    """Update quantity of an item in a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_quantity", json_data={"lineItemId": line_item_id, "quantity": quantity})

@mcp.tool()
def update_guest_shipping_address(checkout_session_id: str, shipping_address: Dict[str, Any]) -> Dict[str, Any]:
    """Update shipping address for a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_address", json_data={"shippingAddress": shipping_address})

@mcp.tool()
def update_guest_shipping_option(checkout_session_id: str, shipping_option_id: str) -> Dict[str, Any]:
    """Update shipping option for a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_option", json_data={"shippingOptionId": shipping_option_id})

@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str) -> Dict[str, Any]:
    """Get details of a guest purchase order."""
    return make_request("GET", f"/buy/order/v1/guest_purchase_order/{purchase_order_id}")

if __name__ == "__main__":
    mcp.run()
