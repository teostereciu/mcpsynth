import os
import requests
from fastmcp import FastMCP

mcp = FastMCP("eBay Sell API")

def get_ebay_client():
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    base_url = "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"
    
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
    
    if not all([app_id, cert_id, refresh_token]):
        raise ValueError("Missing required environment variables: EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN")
        
    auth_url = f"{base_url}/identity/v1/oauth2/token"
    auth_data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    
    auth_response = requests.post(
        auth_url,
        data=auth_data,
        auth=(app_id, cert_id)
    )
    
    if not auth_response.ok:
        raise ValueError(f"Failed to authenticate: {auth_response.text}")
        
    access_token = auth_response.json()["access_token"]
    
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    return base_url, session

def make_request(method, path, **kwargs):
    try:
        base_url, session = get_ebay_client()
        url = f"{base_url}{path}"
        response = session.request(method, url, **kwargs)
        
        if response.status_code == 204:
            return {"status": "success"}
            
        try:
            return response.json()
        except ValueError:
            return {"status": "success", "text": response.text}
    except Exception as e:
        return {"error": str(e)}

# Inventory API
@mcp.tool()
def get_inventory_item(sku: str) -> dict:
    """Retrieve an inventory item by SKU."""
    return make_request("GET", f"/sell/inventory/v1/inventory_item/{sku}")

@mcp.tool()
def create_or_replace_inventory_item(sku: str, payload: dict) -> dict:
    """Create or replace an inventory item."""
    return make_request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json=payload)

@mcp.tool()
def delete_inventory_item(sku: str) -> dict:
    """Delete an inventory item."""
    return make_request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")

@mcp.tool()
def get_inventory_items(limit: int = 50, offset: int = 0) -> dict:
    """Retrieve all inventory items."""
    return make_request("GET", "/sell/inventory/v1/inventory_item", params={"limit": limit, "offset": offset})

@mcp.tool()
def get_offer(offer_id: str) -> dict:
    """Retrieve an offer by ID."""
    return make_request("GET", f"/sell/inventory/v1/offer/{offer_id}")

@mcp.tool()
def create_offer(payload: dict) -> dict:
    """Create an offer."""
    return make_request("POST", "/sell/inventory/v1/offer", json=payload)

@mcp.tool()
def update_offer(offer_id: str, payload: dict) -> dict:
    """Update an offer."""
    return make_request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json=payload)

@mcp.tool()
def delete_offer(offer_id: str) -> dict:
    """Delete an offer."""
    return make_request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")

@mcp.tool()
def get_offers(sku: str = None, limit: int = 50, offset: int = 0) -> dict:
    """Retrieve offers."""
    params = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    return make_request("GET", "/sell/inventory/v1/offer", params=params)

@mcp.tool()
def publish_offer(offer_id: str) -> dict:
    """Publish an offer."""
    return make_request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")

# Fulfillment API
@mcp.tool()
def get_order(order_id: str) -> dict:
    """Retrieve an order by ID."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}")

@mcp.tool()
def get_orders(limit: int = 50, offset: int = 0) -> dict:
    """Retrieve orders."""
    return make_request("GET", "/sell/fulfillment/v1/order", params={"limit": limit, "offset": offset})

@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> dict:
    """Retrieve shipping fulfillments for an order."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")

@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """Retrieve a specific shipping fulfillment."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}")

@mcp.tool()
def create_shipping_fulfillment(order_id: str, payload: dict) -> dict:
    """Create a shipping fulfillment for an order."""
    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json=payload)

# Account API
@mcp.tool()
def get_fulfillment_policies(marketplace_id: str) -> dict:
    """Retrieve fulfillment policies."""
    return make_request("GET", "/sell/account/v1/fulfillment_policy", params={"marketplace_id": marketplace_id})

@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Retrieve a fulfillment policy by ID."""
    return make_request("GET", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")

@mcp.tool()
def create_fulfillment_policy(payload: dict) -> dict:
    """Create a fulfillment policy."""
    return make_request("POST", "/sell/account/v1/fulfillment_policy", json=payload)

@mcp.tool()
def update_fulfillment_policy(fulfillment_policy_id: str, payload: dict) -> dict:
    """Update a fulfillment policy."""
    return make_request("PUT", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}", json=payload)

@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Delete a fulfillment policy."""
    return make_request("DELETE", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")

@mcp.tool()
def get_payment_policies(marketplace_id: str) -> dict:
    """Retrieve payment policies."""
    return make_request("GET", "/sell/account/v1/payment_policy", params={"marketplace_id": marketplace_id})

@mcp.tool()
def get_return_policies(marketplace_id: str) -> dict:
    """Retrieve return policies."""
    return make_request("GET", "/sell/account/v1/return_policy", params={"marketplace_id": marketplace_id})

# Marketing API
@mcp.tool()
def get_campaigns(limit: int = 50, offset: int = 0) -> dict:
    """Retrieve campaigns."""
    return make_request("GET", "/sell/marketing/v1/campaign", params={"limit": limit, "offset": offset})

@mcp.tool()
def get_campaign(campaign_id: str) -> dict:
    """Retrieve a campaign by ID."""
    return make_request("GET", f"/sell/marketing/v1/campaign/{campaign_id}")

@mcp.tool()
def delete_campaign(campaign_id: str) -> dict:
    """Delete a campaign."""
    return make_request("DELETE", f"/sell/marketing/v1/campaign/{campaign_id}")

# Finances API
@mcp.tool()
def get_transactions(limit: int = 50, offset: int = 0) -> dict:
    """Retrieve transactions."""
    return make_request("GET", "/sell/finances/v1/transaction", params={"limit": limit, "offset": offset})

@mcp.tool()
def get_payouts(limit: int = 50, offset: int = 0) -> dict:
    """Retrieve payouts."""
    return make_request("GET", "/sell/finances/v1/payout", params={"limit": limit, "offset": offset})

# Feed API
@mcp.tool()
def get_tasks(limit: int = 50, offset: int = 0) -> dict:
    """Retrieve tasks."""
    return make_request("GET", "/sell/feed/v1/task", params={"limit": limit, "offset": offset})

@mcp.tool()
def create_task(payload: dict) -> dict:
    """Create a task."""
    return make_request("POST", "/sell/feed/v1/task", json=payload)

@mcp.tool()
def get_task(task_id: str) -> dict:
    """Retrieve a task by ID."""
    return make_request("GET", f"/sell/feed/v1/task/{task_id}")

if __name__ == "__main__":
    mcp.run()
