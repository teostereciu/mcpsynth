#!/usr/bin/env python3
"""
eBay Sell API MCP Server

This server provides MCP tools for interacting with the eBay Sell API,
enabling autonomous agents to manage listings, orders, inventory, and more.
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("ebay-sell")

# Base URLs for eBay API
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com"
}

def get_base_url():
    """Get the eBay base URL based on environment variable."""
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return BASE_URLS.get(env, BASE_URLS["SANDBOX"])

def get_auth_headers():
    """Get OAuth 2.0 authorization headers."""
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    
    if not all([refresh_token, app_id, cert_id]):
        return {"error": "Missing eBay credentials. Please set EBAY_APP_ID, EBAY_CERT_ID, and EBAY_REFRESH_TOKEN environment variables."}
    
    # Get access token using refresh token
    token_url = "https://api.ebay.com/oauth2/token"
    auth = requests.auth.HTTPBasicAuth(app_id, cert_id)
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    
    try:
        response = requests.post(token_url, auth=auth, data=data)
        response.raise_for_status()
        access_token = response.json().get("access_token")
        return {"Authorization": f"Bearer {access_token}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to get access token: {str(e)}"}

def _process_response(response):
    """Process HTTP response and return JSON or error."""
    try:
        if response.status_code >= 200 and response.status_code < 300:
            if response.status_code == 204:  # No Content
                return {"success": True, "message": "Operation completed successfully"}
            return response.json()
        else:
            # Try to get error details
            try:
                error_detail = response.json()
                return {"error": f"API error {response.status_code}: {error_detail}"}
            except:
                return {"error": f"API error {response.status_code}: {response.text}"}
    except requests.exceptions.JSONDecodeError:
        return {"error": f"Failed to parse response: {response.text}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

# =============================================================================
# INVENTORY API
# =============================================================================

@mcp.tool()
def get_inventory_item(seller_sku: str) -> dict:
    """Retrieves an inventory item record by SKU."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/inventory_item/{seller_sku}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def create_or_replace_inventory_item(seller_sku: str, inventory_item: dict, content_language: str = "en-US") -> dict:
    """Creates or replaces an inventory item record."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/inventory_item/{seller_sku}"
    
    try:
        response = requests.put(url, headers=headers, json=inventory_item)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def update_inventory_item(seller_sku: str, inventory_item: dict, content_language: str = "en-US") -> dict:
    """Updates an existing inventory item record."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/inventory_item/{seller_sku}"
    
    try:
        response = requests.put(url, headers=headers, json=inventory_item)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def delete_inventory_item(seller_sku: str) -> dict:
    """Deletes an inventory item record."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/inventory_item/{seller_sku}"
    
    try:
        response = requests.delete(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_inventory_items(limit: str = "25", offset: str = "0") -> dict:
    """Retrieves all inventory item records for the seller's account."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    
    base_url = get_base_url()
    url = f"{base_url}/inventory_item"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_offers(seller_sku: str = None, market_id: str = None, format_type: str = None, 
               limit: str = "100", offset: str = "0") -> dict:
    """Retrieves offers associated with a SKU."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    if seller_sku:
        params["seller_sku"] = seller_sku
    if market_id:
        params["market_id"] = market_id
    if format_type:
        params["format"] = format_type
    
    base_url = get_base_url()
    url = f"{base_url}/offer"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_offer(offer_id: str) -> dict:
    """Retrieves an offer by its unique identifier."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/offer/{offer_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def create_offer(offer: dict, content_language: str = "en-US") -> dict:
    """Creates a new offer."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/offer"
    
    try:
        response = requests.post(url, headers=headers, json=offer)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def update_offer(offer_id: str, offer: dict, content_language: str = "en-US") -> dict:
    """Updates an existing offer."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/offer/{offer_id}"
    
    try:
        response = requests.put(url, headers=headers, json=offer)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def delete_offer(offer_id: str) -> dict:
    """Deletes an offer."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/offer/{offer_id}"
    
    try:
        response = requests.delete(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def publish_offer(offer_id: str) -> dict:
    """Publishes (activates) an offer to create an eBay listing."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/offer/{offer_id}/publish"
    
    try:
        response = requests.post(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_update_price_quantity(bulk_price_quantity: dict) -> dict:
    """Updates price and quantity for multiple offers associated with an inventory item."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_update_price_quantity"
    
    try:
        response = requests.post(url, headers=headers, json=bulk_price_quantity)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Inventory Location API

@mcp.tool()
def create_inventory_location(location: dict, merchant_location_key: str, content_language: str = "en-US") -> dict:
    """Creates a new inventory location."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/location/{merchant_location_key}"
    
    try:
        response = requests.post(url, headers=headers, json=location)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_inventory_locations(limit: str = "100", offset: str = "0") -> dict:
    """Retrieves all inventory locations associated with the seller's account."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    
    base_url = get_base_url()
    url = f"{base_url}/location"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_inventory_location(merchant_location_key: str) -> dict:
    """Retrieves details for a specific inventory location."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/location/{merchant_location_key}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def update_inventory_location(merchant_location_key: str, location: dict, content_language: str = "en-US") -> dict:
    """Updates an existing inventory location."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/location/{merchant_location_key}"
    
    try:
        response = requests.put(url, headers=headers, json=location)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def delete_inventory_location(merchant_location_key: str) -> dict:
    """Deletes an inventory location."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/location/{merchant_location_key}"
    
    try:
        response = requests.delete(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# =============================================================================
# FULFILLMENT API
# =============================================================================

@mcp.tool()
def get_order(order_id: str, field_groups: str = None) -> dict:
    """Retrieves an order by its unique identifier."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {}
    if field_groups:
        params["field_groups"] = field_groups
    
    base_url = get_base_url()
    url = f"{base_url}/order/{order_id}"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_orders(filter: str = None, limit: str = "50", offset: str = "0", 
               order_ids: str = None, field_groups: str = None) -> dict:
    """Retrieves orders based on filters."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    if field_groups:
        params["fieldGroups"] = field_groups
    
    base_url = get_base_url()
    url = f"{base_url}/order"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def create_shipping_fulfillment(order_id: str, shipping_fulfillment: dict, content_language: str = "en-US") -> dict:
    """Creates a shipping fulfillment for an order."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/order/{order_id}/shipping_fulfillment"
    
    try:
        response = requests.post(url, headers=headers, json=shipping_fulfillment)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """Retrieves a shipping fulfillment by its unique identifier."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/order/{order_id}/shipping_fulfillment/{fulfillment_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_shipping_fulfillments(order_id: str, limit: str = "50", offset: str = "0") -> dict:
    """Retrieves all shipping fulfillments for an order."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    
    base_url = get_base_url()
    url = f"{base_url}/order/{order_id}/shipping_fulfillment"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def issue_refund(order_id: str, refund_request: dict, content_language: str = "en-US") -> dict:
    """Issues a refund for an order."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/order/{order_id}/issue_refund"
    
    try:
        response = requests.post(url, headers=headers, json=refund_request)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Payment Dispute API

@mcp.tool()
def get_payment_dispute(dispute_id: str) -> dict:
    """Retrieves a payment dispute by its unique identifier."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/payment_dispute/{dispute_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_payment_disputes() -> dict:
    """Retrieves all payment dispute summaries for the seller."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/payment_dispute_summaries"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def accept_payment_dispute(dispute_id: str) -> dict:
    """Accepts a payment dispute."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/payment_dispute/{dispute_id}/accept"
    
    try:
        response = requests.post(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def contest_payment_dispute(dispute_id: str, evidence: dict) -> dict:
    """Contest a payment dispute by providing evidence."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/payment_dispute/{dispute_id}/contest"
    
    try:
        response = requests.post(url, headers=headers, json=evidence)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# =============================================================================
# ACCOUNT API (Business Policies)
# =============================================================================

@mcp.tool()
def get_fulfillment_policies(market_id: str, content_language: str = None) -> dict:
    """Retrieves all fulfillment policies for a marketplace."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"market_id": market_id}
    if content_language:
        headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/fulfillment_policy"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Retrieves a specific fulfillment policy by its ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/fulfillment_policy/{fulfillment_policy_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_fulfillment_policy_by_name(market_id: str, policy_name: str, content_language: str = None) -> dict:
    """Retrieves a fulfillment policy by its name."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"market_id": market_id}
    if content_language:
        headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/fulfillment_policy_by_name/{policy_name}"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def create_fulfillment_policy(policy: dict, content_language: str = "en-US") -> dict:
    """Creates a new fulfillment policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/fulfillment_policy/"
    
    try:
        response = requests.post(url, headers=headers, json=policy)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def update_fulfillment_policy(fulfillment_policy_id: str, policy: dict, content_language: str = "en-US") -> dict:
    """Updates an existing fulfillment policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/fulfillment_policy/{fulfillment_policy_id}"
    
    try:
        response = requests.put(url, headers=headers, json=policy)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Deletes a fulfillment policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/fulfillment_policy/{fulfillment_policy_id}"
    
    try:
        response = requests.delete(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Payment Policy API

@mcp.tool()
def get_payment_policies(market_id: str, content_language: str = None) -> dict:
    """Retrieves all payment policies for a marketplace."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"market_id": market_id}
    if content_language:
        headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/payment_policy"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> dict:
    """Retrieves a specific payment policy by its ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/payment_policy/{payment_policy_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_payment_policy_by_name(market_id: str, policy_name: str, content_language: str = None) -> dict:
    """Retrieves a payment policy by its name."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"market_id": market_id}
    if content_language:
        headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/payment_policy_by_name/{policy_name}"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def create_payment_policy(policy: dict, content_language: str = "en-US") -> dict:
    """Creates a new payment policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/payment_policy/"
    
    try:
        response = requests.post(url, headers=headers, json=policy)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def update_payment_policy(payment_policy_id: str, policy: dict, content_language: str = "en-US") -> dict:
    """Updates an existing payment policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/payment_policy/{payment_policy_id}"
    
    try:
        response = requests.put(url, headers=headers, json=policy)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def delete_payment_policy(payment_policy_id: str) -> dict:
    """Deletes a payment policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/payment_policy/{payment_policy_id}"
    
    try:
        response = requests.delete(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Return Policy API

@mcp.tool()
def get_return_policies(market_id: str, content_language: str = None) -> dict:
    """Retrieves all return policies for a marketplace."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"market_id": market_id}
    if content_language:
        headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/return_policy"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_return_policy(return_policy_id: str) -> dict:
    """Retrieves a specific return policy by its ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/return_policy/{return_policy_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_return_policy_by_name(market_id: str, policy_name: str, content_language: str = None) -> dict:
    """Retrieves a return policy by its name."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"market_id": market_id}
    if content_language:
        headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/return_policy_by_name/{policy_name}"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def create_return_policy(policy: dict, content_language: str = "en-US") -> dict:
    """Creates a new return policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/return_policy/"
    
    try:
        response = requests.post(url, headers=headers, json=policy)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def update_return_policy(return_policy_id: str, policy: dict, content_language: str = "en-US") -> dict:
    """Updates an existing return policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/return_policy/{return_policy_id}"
    
    try:
        response = requests.put(url, headers=headers, json=policy)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def delete_return_policy(return_policy_id: str) -> dict:
    """Deletes a return policy."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/return_policy/{return_policy_id}"
    
    try:
        response = requests.delete(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# =============================================================================
# FINANCES API
# =============================================================================

@mcp.tool()
def get_payouts(filter: str = None, limit: str = "20", offset: str = "0", 
                sort_by: str = None, marketplace_id: str = None) -> dict:
    """Retrieves seller payout details."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort_by:
        params["sort_by"] = sort_by
    
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    else:
        headers["X-EBAY-C-MARKETPLACE-ID"] = "EBAY_US"
    
    base_url = get_base_url()
    url = f"{base_url}/payout"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_payout(payout_id: str, marketplace_id: str = None) -> dict:
    """Retrieves a specific payout by its ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    else:
        headers["X-EBAY-C-MARKETPLACE-ID"] = "EBAY_US"
    
    base_url = get_base_url()
    url = f"{base_url}/payout/{payout_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_transactions(filter: str = None, limit: str = "20", offset: str = "0", 
                    sort_by: str = None, marketplace_id: str = None) -> dict:
    """Retrieves monetary transaction details."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort_by:
        params["sort_by"] = sort_by
    
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    else:
        headers["X-EBAY-C-MARKETPLACE-ID"] = "EBAY_US"
    
    base_url = get_base_url()
    url = f"{base_url}/transaction"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_payout_summary(marketplace_id: str = None) -> dict:
    """Retrieves a summary of all payouts."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    else:
        headers["X-EBAY-C-MARKETPLACE-ID"] = "EBAY_US"
    
    base_url = get_base_url()
    url = f"{base_url}/payout_summary"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_seller_funds_summary(marketplace_id: str = None) -> dict:
    """Retrieves a summary of seller funds."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    else:
        headers["X-EBAY-C-MARKETPLACE-ID"] = "EBAY_US"
    
    base_url = get_base_url()
    url = f"{base_url}/seller_funds_summary"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# =============================================================================
# MARKETING API (Promoted Listings)
# =============================================================================

@mcp.tool()
def get_campaigns(campaign_title: str = None, campaign_status: str = None, 
                 channels: str = None, start_date_range: str = None, 
                 end_date_range: str = None, funding_strategy: str = None,
                 limit: str = "10", offset: str = "0") -> dict:
    """Retrieves all campaigns for the seller."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    if campaign_title:
        params["campaign_title"] = campaign_title
    if campaign_status:
        params["campaign_status"] = campaign_status
    if channels:
        params["channels"] = channels
    if start_date_range:
        params["start_date_range"] = start_date_range
    if end_date_range:
        params["end_date_range"] = end_date_range
    if funding_strategy:
        params["funding_strategy"] = funding_strategy
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_campaign(campaign_id: str) -> dict:
    """Retrieves a specific campaign by its ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_campaign_by_name(campaign_name: str) -> dict:
    """Retrieves a campaign by its name."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign_by_name/{campaign_name}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def create_ad_group(campaign_id: str, ad_group: dict, content_language: str = "en-US") -> dict:
    """Creates an ad group for a campaign."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad_group"
    
    try:
        response = requests.post(url, headers=headers, json=ad_group)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_ad_group(campaign_id: str, ad_group_id: str) -> dict:
    """Retrieves an ad group by its ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad_group/{ad_group_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_ad_groups(campaign_id: str, limit: str = "10", offset: str = "0") -> dict:
    """Retrieves all ad groups for a campaign."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad_group"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def update_ad_group(campaign_id: str, ad_group_id: str, ad_group: dict, content_language: str = "en-US") -> dict:
    """Updates an ad group."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad_group/{ad_group_id}"
    
    try:
        response = requests.put(url, headers=headers, json=ad_group)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def delete_ad_group(campaign_id: str, ad_group_id: str) -> dict:
    """Deletes an ad group."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad_group/{ad_group_id}"
    
    try:
        response = requests.delete(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_ads(campaign_id: str, limit: str = "10", offset: str = "0") -> dict:
    """Retrieves all ads for a campaign."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_ad(campaign_id: str, ad_id: str) -> dict:
    """Retrieves an ad by its ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad/{ad_id}"
    
    try:
        response = requests.get(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def create_ad(campaign_id: str, ad: dict, content_language: str = "en-US") -> dict:
    """Creates an ad for a campaign."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad"
    
    try:
        response = requests.post(url, headers=headers, json=ad)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def update_bid(campaign_id: str, ad_id: str, bid_percentage: dict, content_language: str = "en-US") -> dict:
    """Updates the bid percentage for an ad."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    headers["Content-Language"] = content_language
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid"
    
    try:
        response = requests.post(url, headers=headers, json=bid_percentage)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def delete_ad(campaign_id: str, ad_id: str) -> dict:
    """Deletes an ad."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    base_url = get_base_url()
    url = f"{base_url}/ad_campaign/{campaign_id}/ad/{ad_id}"
    
    try:
        response = requests.delete(url, headers=headers)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def get_ads_by_inventory_reference(inventory_reference_id: str, limit: str = "10", offset: str = "0") -> dict:
    """Retrieves ads by inventory reference ID (SKU)."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    params = {"limit": limit, "offset": offset}
    
    base_url = get_base_url()
    url = f"{base_url}/ad_by_inventory_reference/{inventory_reference_id}"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_create_ads_by_inventory_reference(inventory_references: dict) -> dict:
    """Creates multiple ads by inventory reference ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_create_ad_by_inventory_reference"
    
    try:
        response = requests.post(url, headers=headers, json=inventory_references)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_update_ads_status_by_listing_id(status_update: dict) -> dict:
    """Updates the status of multiple ads by listing ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_update_ad_status_by_listing_id"
    
    try:
        response = requests.post(url, headers=headers, json=status_update)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_update_ads_bid_by_listing_id(bid_update: dict) -> dict:
    """Updates the bid percentage of multiple ads by listing ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_update_ad_bid_by_listing_id"
    
    try:
        response = requests.post(url, headers=headers, json=bid_update)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_delete_ads_by_listing_id(listing_ids: dict) -> dict:
    """Deletes multiple ads by listing ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_delete_ad_by_listing_id"
    
    try:
        response = requests.post(url, headers=headers, json=listing_ids)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_create_ads_by_listing_id(listing_ads: dict) -> dict:
    """Creates multiple ads by listing ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_create_ad_by_listing_id"
    
    try:
        response = requests.post(url, headers=headers, json=listing_ads)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_update_ads_bid_by_inventory_reference(bid_update: dict) -> dict:
    """Updates the bid percentage of multiple ads by inventory reference ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_update_ad_bid_by_inventory_reference"
    
    try:
        response = requests.post(url, headers=headers, json=bid_update)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_delete_ads_by_inventory_reference(delete_request: dict) -> dict:
    """Deletes multiple ads by inventory reference ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_delete_ad_by_inventory_reference"
    
    try:
        response = requests.post(url, headers=headers, json=delete_request)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_update_ads_status(bulk_status_update: dict) -> dict:
    """Updates the status of multiple ads."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_update_ad_status"
    
    try:
        response = requests.post(url, headers=headers, json=bulk_status_update)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def bulk_update_ads_status_by_listing_id(bulk_status_update: dict) -> dict:
    """Updates the status of multiple ads by listing ID."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/bulk_update_ad_status_by_listing_id"
    
    try:
        response = requests.post(url, headers=headers, json=bulk_status_update)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def suggest_bids(suggestion_request: dict) -> dict:
    """Gets bid suggestions for a campaign."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/suggest_bids"
    
    try:
        response = requests.post(url, headers=headers, json=suggestion_request)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def suggest_budget(suggestion_request: dict) -> dict:
    """Gets budget suggestions for a campaign."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/suggest_budget"
    
    try:
        response = requests.post(url, headers=headers, json=suggestion_request)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@mcp.tool()
def suggest_keywords(suggestion_request: dict) -> dict:
    """Gets keyword suggestions for a campaign."""
    headers = get_auth_headers()
    if "error" in headers:
        return headers
    
    headers["Content-Type"] = "application/json"
    
    base_url = get_base_url()
    url = f"{base_url}/suggest_keywords"
    
    try:
        response = requests.post(url, headers=headers, json=suggestion_request)
        return _process_response(response)
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
