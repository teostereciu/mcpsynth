import os
import requests
import json
from typing import Dict, Any, Optional, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("eBay Sell API")

def get_access_token() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
    
    if not all([app_id, cert_id, refresh_token]):
        raise ValueError("Missing required environment variables for eBay API authentication.")
        
    token_url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token" if env == "SANDBOX" else "https://api.ebay.com/identity/v1/oauth2/token"
    
    auth = requests.auth.HTTPBasicAuth(app_id, cert_id)
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    
    response = requests.post(token_url, auth=auth, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def make_request(method: str, path: str, **kwargs) -> Dict[str, Any]:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    base_url = "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"
    
    try:
        token = get_access_token()
    except Exception as e:
        return {"error": f"Authentication failed: {str(e)}"}
        
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Bearer {token}"
    headers["Content-Type"] = "application/json"
    
    url = f"{base_url}{path}"
    
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        if response.status_code == 204:
            return {"success": True}
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_msg = e.response.json()
            except:
                error_msg = e.response.text
        return {"error": error_msg}

# --- Inventory API ---

@mcp.tool()
def get_inventory_item(sku: str) -> Dict[str, Any]:
    """Retrieve an inventory item by SKU."""
    return make_request("GET", f"/sell/inventory/v1/inventory_item/{sku}")

@mcp.tool()
def get_inventory_items(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve all inventory items."""
    return make_request("GET", "/sell/inventory/v1/inventory_item", params={"limit": limit, "offset": offset})

@mcp.tool()
def create_or_replace_inventory_item(sku: str, item_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create or replace an inventory item."""
    return make_request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json=item_data)

@mcp.tool()
def delete_inventory_item(sku: str) -> Dict[str, Any]:
    """Delete an inventory item."""
    return make_request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")

@mcp.tool()
def get_offer(offer_id: str) -> Dict[str, Any]:
    """Retrieve an offer by ID."""
    return make_request("GET", f"/sell/inventory/v1/offer/{offer_id}")

@mcp.tool()
def get_offers(sku: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve offers, optionally filtered by SKU."""
    params = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    return make_request("GET", "/sell/inventory/v1/offer", params=params)

@mcp.tool()
def create_offer(offer_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new offer."""
    return make_request("POST", "/sell/inventory/v1/offer", json=offer_data)

@mcp.tool()
def update_offer(offer_id: str, offer_data: Dict[str, Any]) -> Dict[str, Any]:
    """Update an existing offer."""
    return make_request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json=offer_data)

@mcp.tool()
def publish_offer(offer_id: str) -> Dict[str, Any]:
    """Publish an offer to create an eBay listing."""
    return make_request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")

@mcp.tool()
def withdraw_offer(offer_id: str) -> Dict[str, Any]:
    """Withdraw a published offer (ends the listing)."""
    return make_request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")

@mcp.tool()
def get_inventory_locations(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve inventory locations."""
    return make_request("GET", "/sell/inventory/v1/location", params={"limit": limit, "offset": offset})

# --- Fulfillment API ---

@mcp.tool()
def get_order(order_id: str) -> Dict[str, Any]:
    """Retrieve an order by ID."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}")

@mcp.tool()
def get_orders(filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve orders, optionally filtered."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/sell/fulfillment/v1/order", params=params)

@mcp.tool()
def create_shipping_fulfillment(order_id: str, fulfillment_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create a shipping fulfillment for an order."""
    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json=fulfillment_data)

@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    """Retrieve shipping fulfillments for an order."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")

# --- Finances API ---

@mcp.tool()
def get_transactions(filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve financial transactions."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/sell/finances/v1/transaction", params=params)

@mcp.tool()
def get_payouts(filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve payouts."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/sell/finances/v1/payout", params=params)

@mcp.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """Retrieve a specific payout by ID."""
    return make_request("GET", f"/sell/finances/v1/payout/{payout_id}")

# --- Account API ---

@mcp.tool()
def get_fulfillment_policies(marketplace_id: str) -> Dict[str, Any]:
    """Retrieve fulfillment policies for a marketplace."""
    return make_request("GET", "/sell/account/v1/fulfillment_policy", params={"marketplace_id": marketplace_id})

@mcp.tool()
def get_return_policies(marketplace_id: str) -> Dict[str, Any]:
    """Retrieve return policies for a marketplace."""
    return make_request("GET", "/sell/account/v1/return_policy", params={"marketplace_id": marketplace_id})

@mcp.tool()
def get_payment_policies(marketplace_id: str) -> Dict[str, Any]:
    """Retrieve payment policies for a marketplace."""
    return make_request("GET", "/sell/account/v1/payment_policy", params={"marketplace_id": marketplace_id})

@mcp.tool()
def get_privileges() -> Dict[str, Any]:
    """Retrieve seller privileges."""
    return make_request("GET", "/sell/account/v1/privilege")

# --- Marketing API ---

@mcp.tool()
def get_campaigns(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve marketing campaigns."""
    return make_request("GET", "/sell/marketing/v1/ad_campaign", params={"limit": limit, "offset": offset})

@mcp.tool()
def get_campaign(campaign_id: str) -> Dict[str, Any]:
    """Retrieve a marketing campaign by ID."""
    return make_request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")

# --- Feed API ---

@mcp.tool()
def get_tasks(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Retrieve feed tasks."""
    return make_request("GET", "/sell/feed/v1/task", params={"limit": limit, "offset": offset})

@mcp.tool()
def create_task(task_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new feed task."""
    return make_request("POST", "/sell/feed/v1/task", json=task_data)

if __name__ == "__main__":
    mcp.run()
