import os
import base64
import requests
from typing import Optional, Dict, Any, List
from fastmcp import FastMCP

mcp = FastMCP("ebay_sell_api")

def get_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"

def get_access_token() -> str:
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
    
    if not all([app_id, cert_id, refresh_token]):
        raise ValueError("Missing required environment variables: EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN")
        
    base_url = get_base_url()
    token_url = f"{base_url}/identity/v1/oauth2/token"
    
    auth_str = f"{app_id}:{cert_id}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    
    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def make_request(method: str, path: str, params: Optional[Dict] = None, json_data: Optional[Dict] = None) -> Dict[str, Any]:
    try:
        token = get_access_token()
    except Exception as e:
        return {"error": f"Authentication failed: {str(e)}"}
        
    base_url = get_base_url()
    url = f"{base_url}{path}"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.request(method, url, headers=headers, params=params, json=json_data)
        if response.status_code == 204:
            return {"success": True}
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                return {"error": e.response.json()}
            except:
                return {"error": e.response.text}
        return {"error": str(e)}

# Inventory API
@mcp.tool()
def get_inventory_item(sku: str) -> Dict[str, Any]:
    """Retrieve an inventory item by SKU."""
    return make_request("GET", f"/sell/inventory/v1/inventory_item/{sku}")

@mcp.tool()
def create_or_replace_inventory_item(sku: str, item_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create or replace an inventory item."""
    return make_request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json_data=item_data)

@mcp.tool()
def delete_inventory_item(sku: str) -> Dict[str, Any]:
    """Delete an inventory item."""
    return make_request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")

@mcp.tool()
def get_inventory_items(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve a list of inventory items."""
    return make_request("GET", "/sell/inventory/v1/inventory_item", params={"limit": limit, "offset": offset})

@mcp.tool()
def get_offer(offer_id: str) -> Dict[str, Any]:
    """Retrieve an offer by ID."""
    return make_request("GET", f"/sell/inventory/v1/offer/{offer_id}")

@mcp.tool()
def create_offer(offer_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create an offer."""
    return make_request("POST", "/sell/inventory/v1/offer", json_data=offer_data)

@mcp.tool()
def update_offer(offer_id: str, offer_data: Dict[str, Any]) -> Dict[str, Any]:
    """Update an offer."""
    return make_request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json_data=offer_data)

@mcp.tool()
def publish_offer(offer_id: str) -> Dict[str, Any]:
    """Publish an offer."""
    return make_request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")

@mcp.tool()
def get_offers(sku: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve a list of offers."""
    params = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    return make_request("GET", "/sell/inventory/v1/offer", params=params)

# Fulfillment API
@mcp.tool()
def get_order(order_id: str) -> Dict[str, Any]:
    """Retrieve an order by ID."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}")

@mcp.tool()
def get_orders(limit: int = 50, offset: int = 0, filter: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of orders."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/sell/fulfillment/v1/order", params=params)

@mcp.tool()
def create_shipping_fulfillment(order_id: str, fulfillment_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create a shipping fulfillment for an order."""
    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json_data=fulfillment_data)

@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    """Retrieve shipping fulfillments for an order."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")

# Account API
@mcp.tool()
def get_fulfillment_policies(marketplace_id: str) -> Dict[str, Any]:
    """Retrieve fulfillment policies for a marketplace."""
    return make_request("GET", "/sell/account/v1/fulfillment_policy", params={"marketplace_id": marketplace_id})

@mcp.tool()
def get_payment_policies(marketplace_id: str) -> Dict[str, Any]:
    """Retrieve payment policies for a marketplace."""
    return make_request("GET", "/sell/account/v1/payment_policy", params={"marketplace_id": marketplace_id})

@mcp.tool()
def get_return_policies(marketplace_id: str) -> Dict[str, Any]:
    """Retrieve return policies for a marketplace."""
    return make_request("GET", "/sell/account/v1/return_policy", params={"marketplace_id": marketplace_id})

# Finances API
@mcp.tool()
def get_transactions(limit: int = 50, offset: int = 0, filter: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of transactions."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/sell/finances/v1/transaction", params=params)

@mcp.tool()
def get_payouts(limit: int = 50, offset: int = 0, filter: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of payouts."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/sell/finances/v1/payout", params=params)

# Marketing API
@mcp.tool()
def get_campaigns(limit: int = 50, offset: int = 0, campaign_name: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of campaigns."""
    params = {"limit": limit, "offset": offset}
    if campaign_name:
        params["campaign_name"] = campaign_name
    return make_request("GET", "/sell/marketing/v1/campaign", params=params)

@mcp.tool()
def create_campaign(campaign_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create a campaign."""
    return make_request("POST", "/sell/marketing/v1/campaign", json_data=campaign_data)

if __name__ == "__main__":
    mcp.run()
