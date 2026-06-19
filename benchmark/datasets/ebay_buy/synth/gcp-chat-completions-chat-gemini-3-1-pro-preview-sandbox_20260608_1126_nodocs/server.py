import os
import base64
import requests
from typing import Optional, Dict, Any, List
from fastmcp import FastMCP

mcp = FastMCP("ebay_buy_api")

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
    
    credentials = f"{app_id}:{cert_id}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    
    url = f"{get_base_url()}/identity/v1/oauth2/token"
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def make_request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    try:
        token = get_access_token()
    except Exception as e:
        return {"error": f"Authentication failed: {str(e)}"}
        
    url = f"{get_base_url()}{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": "EBAY_US"
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

@mcp.tool()
def search_items(q: str, limit: int = 10, offset: int = 0, category_ids: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None) -> Dict[str, Any]:
    """
    Search for items on eBay.
    """
    params = {"q": q, "limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return make_request("GET", "/buy/browse/v1/item_summary/search", params=params)

@mcp.tool()
def get_item(item_id: str) -> Dict[str, Any]:
    """
    Get details of a specific item by its RESTful item ID.
    """
    return make_request("GET", f"/buy/browse/v1/item/{item_id}")

@mcp.tool()
def get_item_by_legacy_id(legacy_item_id: str, legacy_variation_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Get details of a specific item by its legacy item ID.
    """
    params = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id:
        params["legacy_variation_id"] = legacy_variation_id
    return make_request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params=params)

@mcp.tool()
def get_items_by_item_group(item_group_id: str) -> Dict[str, Any]:
    """
    Get details of an item group (e.g., an item with variations like color and size).
    """
    params = {"item_group_id": item_group_id}
    return make_request("GET", "/buy/browse/v1/item/get_items_by_item_group", params=params)

@mcp.tool()
def get_deals(category_ids: Optional[str] = None, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of deals.
    """
    params = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    return make_request("GET", "/buy/deal/v1/deal_item", params=params)

@mcp.tool()
def get_events(limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of events.
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/buy/deal/v1/event", params=params)

@mcp.tool()
def get_event(event_id: str) -> Dict[str, Any]:
    """
    Get details of a specific event.
    """
    return make_request("GET", f"/buy/deal/v1/event/{event_id}")

@mcp.tool()
def initiate_guest_checkout_session(contact_email: str, contact_first_name: str, contact_last_name: str, line_item_inputs: List[Dict[str, Any]], shipping_address: Dict[str, Any]) -> Dict[str, Any]:
    """
    Initiate a guest checkout session.
    line_item_inputs: list of dicts with itemId and quantity.
    shipping_address: dict with recipient, addressLine1, city, stateOrProvince, postalCode, country.
    """
    data = {
        "contactEmail": contact_email,
        "contactFirstName": contact_first_name,
        "contactLastName": contact_last_name,
        "lineItemInputs": line_item_inputs,
        "shippingAddress": shipping_address
    }
    return make_request("POST", "/buy/order/v1/guest_checkout_session/initiate", json_data=data)

@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str) -> Dict[str, Any]:
    """
    Get details of a guest checkout session.
    """
    return make_request("GET", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}")

@mcp.tool()
def place_guest_order(checkout_session_id: str) -> Dict[str, Any]:
    """
    Place an order for a guest checkout session.
    """
    return make_request("POST", f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/place_order")

@mcp.tool()
def get_item_feed(category_id: str, date: str) -> Dict[str, Any]:
    """
    Get an item feed for a specific category and date.
    """
    params = {"category_id": category_id, "date": date}
    return make_request("GET", "/buy/feed/v1/item", params=params)

@mcp.tool()
def get_item_priority_feed(category_id: str, date: str) -> Dict[str, Any]:
    """
    Get an item priority feed for a specific category and date.
    """
    params = {"category_id": category_id, "date": date}
    return make_request("GET", "/buy/feed/v1/item_priority", params=params)

if __name__ == "__main__":
    mcp.run()
