import os
import base64
import requests
from typing import Optional, Dict, Any, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("eBay Buy API")

def get_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"

def get_access_token() -> str:
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    if not app_id or not cert_id:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID environment variables are required")

    auth_str = f"{app_id}:{cert_id}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    url = f"{get_base_url()}/identity/v1/oauth2/token"
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
        "https://api.ebay.com/oauth/api_scope/buy.guest.order"
    ]
    
    data = {
        "grant_type": "client_credentials",
        "scope": " ".join(scopes)
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def make_request(method: str, path: str, params: Optional[Dict] = None, json_data: Optional[Dict] = None) -> Dict[str, Any]:
    try:
        token = get_access_token()
    except Exception as e:
        return {"error": f"Authentication failed: {str(e)}"}

    url = f"{get_base_url()}{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        response = requests.request(method, url, headers=headers, params=params, json=json_data)
        if response.status_code == 204:
            return {"status": "success"}
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}

# Browse API
@mcp.tool()
def check_compatibility(item_id: str, compatibility_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Check compatibility of an item with specific attributes."""
    return make_request("POST", f"/buy/browse/v1/item/{item_id}/check_compatibility", json_data=compatibility_payload)

@mcp.tool()
def get_item(item_id: str) -> Dict[str, Any]:
    """Get the details of a specific item."""
    return make_request("GET", f"/buy/browse/v1/item/{item_id}")

@mcp.tool()
def get_item_by_legacy_id(legacy_item_id: str) -> Dict[str, Any]:
    """Get the details of a specific item using its legacy ID."""
    return make_request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params={"legacy_item_id": legacy_item_id})

@mcp.tool()
def get_items(item_ids: str) -> Dict[str, Any]:
    """Get the details of multiple items. item_ids is a comma-separated list."""
    return make_request("GET", "/buy/browse/v1/item", params={"item_ids": item_ids})

@mcp.tool()
def get_items_by_item_group(item_group_id: str) -> Dict[str, Any]:
    """Get the details of items in an item group."""
    return make_request("GET", "/buy/browse/v1/item/get_items_by_item_group", params={"item_group_id": item_group_id})

@mcp.tool()
def search(q: Optional[str] = None, category_ids: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """Search for items."""
    params = {}
    if q: params["q"] = q
    if category_ids: params["category_ids"] = category_ids
    if limit: params["limit"] = limit
    return make_request("GET", "/buy/browse/v1/item_summary/search", params=params)

@mcp.tool()
def search_by_image(image_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Search for items by image."""
    return make_request("POST", "/buy/browse/v1/item_summary/search_by_image", json_data=image_payload)

# Deal API
@mcp.tool()
def get_deal_items(category_ids: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """Get deal items."""
    params = {}
    if category_ids: params["category_ids"] = category_ids
    if limit: params["limit"] = limit
    return make_request("GET", "/buy/deal/v1/deal_item", params=params)

@mcp.tool()
def get_event_items(event_ids: str, category_ids: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """Get items for specific events."""
    params = {"event_ids": event_ids}
    if category_ids: params["category_ids"] = category_ids
    if limit: params["limit"] = limit
    return make_request("GET", "/buy/deal/v1/event_item", params=params)

@mcp.tool()
def get_event(event_id: str) -> Dict[str, Any]:
    """Get details of a specific event."""
    return make_request("GET", f"/buy/deal/v1/event/{event_id}")

@mcp.tool()
def get_events(limit: Optional[int] = None) -> Dict[str, Any]:
    """Get events."""
    params = {}
    if limit: params["limit"] = limit
    return make_request("GET", "/buy/deal/v1/event", params=params)

# Feed API
@mcp.tool()
def get_item_group_feed(category_id: str, date: str) -> Dict[str, Any]:
    """Get item group feed."""
    return make_request("GET", "/buy/feed/v1/item_group", params={"category_id": category_id, "date": date})

@mcp.tool()
def get_item_feed(category_id: str, date: str) -> Dict[str, Any]:
    """Get item feed."""
    return make_request("GET", "/buy/feed/v1/item", params={"category_id": category_id, "date": date})

@mcp.tool()
def get_item_priority_feed(category_id: str, date: str) -> Dict[str, Any]:
    """Get item priority feed."""
    return make_request("GET", "/buy/feed/v1/item_priority", params={"category_id": category_id, "date": date})

@mcp.tool()
def get_item_snapshot_feed(category_id: str, date: str) -> Dict[str, Any]:
    """Get item snapshot feed."""
    return make_request("GET", "/buy/feed/v1/item_snapshot", params={"category_id": category_id, "date": date})

# Marketing API
@mcp.tool()
def get_merchandised_products(metric_name: str, category_id: str) -> Dict[str, Any]:
    """Get merchandised products."""
    return make_request("GET", "/buy/marketing/v1/merchandised_product", params={"metric_name": metric_name, "category_id": category_id})

# Order API (Guest Checkout)
@mcp.tool()
def apply_guest_coupon(checkout_session_id: str, coupon_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Apply a coupon to a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/apply_coupon", json_data=coupon_payload)

@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str) -> Dict[str, Any]:
    """Get a guest checkout session."""
    return make_request("GET", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}")

@mcp.tool()
def initiate_guest_checkout_session(session_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Initiate a guest checkout session."""
    return make_request("POST", "/buy/order/v1/guest_checkout_session/initiate", json_data=session_payload)

@mcp.tool()
def remove_guest_coupon(checkout_session_id: str, coupon_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Remove a coupon from a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/remove_coupon", json_data=coupon_payload)

@mcp.tool()
def update_guest_quantity(checkout_session_id: str, quantity_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Update quantity in a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_quantity", json_data=quantity_payload)

@mcp.tool()
def update_guest_shipping_address(checkout_session_id: str, address_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Update shipping address in a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_address", json_data=address_payload)

@mcp.tool()
def update_guest_shipping_option(checkout_session_id: str, option_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Update shipping option in a guest checkout session."""
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_option", json_data=option_payload)

@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str) -> Dict[str, Any]:
    """Get a guest purchase order."""
    return make_request("GET", f"/buy/order/v1/guest_purchase_order/{purchase_order_id}")

if __name__ == "__main__":
    mcp.run()
