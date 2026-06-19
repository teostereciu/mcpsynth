#!/usr/bin/env python3
"""
eBay Sell API MCP Server

This server provides tools for interacting with the eBay Sell API,
covering Inventory, Fulfillment, Account, Marketing, Finances, Feed, and other domains.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("ebay-sell-api")

# Configuration
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID", "")
EBAY_REFRESH_TOKEN = os.getenv("EBAY_REFRESH_TOKEN", "")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

BASE_URL = (
    "https://api.sandbox.ebay.com"
    if EBAY_ENVIRONMENT == "SANDBOX"
    else "https://api.ebay.com"
)

# Token cache
_cached_token = None
_cached_token_expiry = 0


def get_oauth_token() -> str:
    """Get a valid OAuth 2.0 access token using the refresh token."""
    global _cached_token, _cached_token_expiry
    import time

    # Return cached token if still valid
    if _cached_token and time.time() < _cached_token_expiry:
        return _cached_token

    token_url = f"{BASE_URL}/identity/v1/oauth2/token"
    auth = (EBAY_APP_ID, EBAY_CERT_ID)
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN,
    }

    try:
        response = requests.post(token_url, auth=auth, data=data, timeout=10)
        response.raise_for_status()
        token_data = response.json()
        _cached_token = token_data["access_token"]
        _cached_token_expiry = (
            __import__("time").time() + token_data.get("expires_in", 3600) - 60
        )
        return _cached_token
    except Exception as e:
        return {"error": f"Failed to get OAuth token: {str(e)}"}


def make_request(
    method: str,
    path: str,
    params: Optional[dict] = None,
    json_body: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> Any:
    """Make an authenticated request to the eBay API."""
    try:
        token = get_oauth_token()
        if isinstance(token, dict) and "error" in token:
            return token

        url = f"{BASE_URL}{path}"
        auth_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if headers:
            auth_headers.update(headers)

        if method.upper() == "GET":
            response = requests.get(url, params=params, headers=auth_headers, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(
                url, params=params, json=json_body, headers=auth_headers, timeout=30
            )
        elif method.upper() == "PUT":
            response = requests.put(
                url, params=params, json=json_body, headers=auth_headers, timeout=30
            )
        elif method.upper() == "DELETE":
            response = requests.delete(url, params=params, headers=auth_headers, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        # Handle different response codes
        if response.status_code in [200, 201, 202, 204]:
            if response.text:
                return response.json()
            return {"success": True}
        elif response.status_code == 404:
            return {"error": "Not found"}
        elif response.status_code == 400:
            try:
                return {"error": response.json()}
            except:
                return {"error": response.text}
        else:
            try:
                return {"error": response.json()}
            except:
                return {"error": f"HTTP {response.status_code}: {response.text}"}

    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# INVENTORY API TOOLS
# ============================================================================


@mcp.tool()
def create_inventory_item(
    sku: str,
    marketplace_id: str,
    availability: Optional[dict] = None,
    condition: Optional[str] = None,
    product: Optional[dict] = None,
) -> dict:
    """Create or replace an inventory item."""
    body = {
        "sku": sku,
        "marketplaceId": marketplace_id,
    }
    if availability:
        body["availability"] = availability
    if condition:
        body["condition"] = condition
    if product:
        body["product"] = product

    return make_request("PUT", f"/inventory/v1/inventory_item/{sku}", json_body=body)


@mcp.tool()
def get_inventory_item(sku: str) -> dict:
    """Retrieve details of a specific inventory item by SKU."""
    return make_request("GET", f"/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def get_inventory_items(limit: int = 25, offset: int = 0) -> dict:
    """Retrieve a list of inventory items."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/inventory/v1/inventory_item", params=params)


@mcp.tool()
def delete_inventory_item(sku: str) -> dict:
    """Delete an inventory item by SKU."""
    return make_request("DELETE", f"/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def create_offer(
    sku: str,
    marketplace_id: str,
    format: str,
    listing_description: Optional[str] = None,
    pricing_summary: Optional[dict] = None,
    quantity_available: Optional[int] = None,
    merchant_location_key: Optional[str] = None,
) -> dict:
    """Create an offer for an inventory item."""
    body = {
        "sku": sku,
        "marketplaceId": marketplace_id,
        "format": format,
    }
    if listing_description:
        body["listingDescription"] = listing_description
    if pricing_summary:
        body["pricingSummary"] = pricing_summary
    if quantity_available:
        body["quantityAvailable"] = quantity_available
    if merchant_location_key:
        body["merchantLocationKey"] = merchant_location_key

    return make_request("POST", "/inventory/v1/offer", json_body=body)


@mcp.tool()
def get_offer(offer_id: str) -> dict:
    """Retrieve details of a specific offer by offer ID."""
    return make_request("GET", f"/inventory/v1/offer/{offer_id}")


@mcp.tool()
def get_offers(
    sku: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
    format: Optional[str] = None,
) -> dict:
    """Retrieve a list of offers."""
    params = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    if format:
        params["format"] = format
    return make_request("GET", "/inventory/v1/offer", params=params)


@mcp.tool()
def update_offer(offer_id: str, offer_data: dict) -> dict:
    """Update an existing offer."""
    return make_request("PUT", f"/inventory/v1/offer/{offer_id}", json_body=offer_data)


@mcp.tool()
def delete_offer(offer_id: str) -> dict:
    """Delete an offer by offer ID."""
    return make_request("DELETE", f"/inventory/v1/offer/{offer_id}")


@mcp.tool()
def publish_offer(offer_id: str) -> dict:
    """Publish an offer to create an active eBay listing."""
    return make_request("POST", f"/inventory/v1/offer/{offer_id}/publish", json_body={})


@mcp.tool()
def withdraw_offer(offer_id: str) -> dict:
    """Withdraw an offer to end the active eBay listing."""
    return make_request("POST", f"/inventory/v1/offer/{offer_id}/withdraw", json_body={})


@mcp.tool()
def get_listing_fees(offers: list) -> dict:
    """Get estimated fees for publishing offers."""
    body = {"offers": offers}
    return make_request("POST", "/inventory/v1/offer/get_listing_fees", json_body=body)


@mcp.tool()
def create_inventory_location(
    merchant_location_key: str,
    name: str,
    address: dict,
    location_types: Optional[list] = None,
    phone: Optional[str] = None,
) -> dict:
    """Create an inventory location."""
    body = {
        "merchantLocationKey": merchant_location_key,
        "name": name,
        "address": address,
    }
    if location_types:
        body["locationTypes"] = location_types
    if phone:
        body["phone"] = phone

    return make_request(
        "POST", f"/inventory/v1/location/{merchant_location_key}", json_body=body
    )


@mcp.tool()
def get_inventory_location(merchant_location_key: str) -> dict:
    """Retrieve details of a specific inventory location."""
    return make_request("GET", f"/inventory/v1/location/{merchant_location_key}")


@mcp.tool()
def get_inventory_locations() -> dict:
    """Retrieve all inventory locations."""
    return make_request("GET", "/inventory/v1/location")


@mcp.tool()
def update_inventory_location(merchant_location_key: str, location_data: dict) -> dict:
    """Update an inventory location."""
    return make_request(
        "PUT", f"/inventory/v1/location/{merchant_location_key}", json_body=location_data
    )


@mcp.tool()
def delete_inventory_location(merchant_location_key: str) -> dict:
    """Delete an inventory location."""
    return make_request("DELETE", f"/inventory/v1/location/{merchant_location_key}")


@mcp.tool()
def enable_inventory_location(merchant_location_key: str) -> dict:
    """Enable an inventory location."""
    return make_request(
        "POST", f"/inventory/v1/location/{merchant_location_key}/enable", json_body={}
    )


@mcp.tool()
def disable_inventory_location(merchant_location_key: str) -> dict:
    """Disable an inventory location."""
    return make_request(
        "POST", f"/inventory/v1/location/{merchant_location_key}/disable", json_body={}
    )


@mcp.tool()
def bulk_create_offer(offers: list) -> dict:
    """Create multiple offers in a single call (up to 25)."""
    body = {"requests": offers}
    return make_request("POST", "/inventory/v1/bulk_offer", json_body=body)


@mcp.tool()
def bulk_publish_offer(offers: list) -> dict:
    """Publish multiple offers in a single call (up to 25)."""
    body = {"requests": offers}
    return make_request("POST", "/inventory/v1/bulk_publish_offer", json_body=body)


@mcp.tool()
def bulk_update_price_quantity(updates: list) -> dict:
    """Update price and quantity for multiple offers in a single call."""
    body = {"requests": updates}
    return make_request("POST", "/inventory/v1/bulk_update_price_quantity", json_body=body)


# ============================================================================
# FULFILLMENT API TOOLS
# ============================================================================


@mcp.tool()
def get_orders(
    order_status: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
    filter: Optional[str] = None,
) -> dict:
    """Retrieve a list of orders."""
    params = {"limit": limit, "offset": offset}
    if order_status:
        params["orderStatus"] = order_status
    if filter:
        params["filter"] = filter
    return make_request("GET", "/fulfillment/v1/order", params=params)


@mcp.tool()
def get_order(order_id: str, field_groups: Optional[str] = None) -> dict:
    """Retrieve details of a specific order by order ID."""
    params = {}
    if field_groups:
        params["fieldGroups"] = field_groups
    return make_request("GET", f"/fulfillment/v1/order/{order_id}", params=params)


@mcp.tool()
def create_shipping_fulfillment(order_id: str, fulfillment_data: dict) -> dict:
    """Create a shipping fulfillment for an order."""
    return make_request(
        "POST", f"/fulfillment/v1/order/{order_id}/shipping_fulfillment", json_body=fulfillment_data
    )


@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> dict:
    """Retrieve all shipping fulfillments for an order."""
    return make_request("GET", f"/fulfillment/v1/order/{order_id}/shipping_fulfillment")


@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """Retrieve details of a specific shipping fulfillment."""
    return make_request(
        "GET", f"/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}"
    )


@mcp.tool()
def issue_refund(order_id: str, refund_data: dict) -> dict:
    """Issue a refund for an order or line item."""
    return make_request(
        "POST", f"/fulfillment/v1/order/{order_id}/issue_refund", json_body=refund_data
    )


@mcp.tool()
def get_payment_disputes(
    order_id: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Retrieve payment dispute summaries."""
    params = {"limit": limit, "offset": offset}
    if order_id:
        params["orderId"] = order_id
    return make_request("GET", "/fulfillment/v1/payment_dispute_summary", params=params)


@mcp.tool()
def get_payment_dispute(dispute_id: str) -> dict:
    """Retrieve details of a specific payment dispute."""
    return make_request("GET", f"/fulfillment/v1/payment_dispute/{dispute_id}")


@mcp.tool()
def accept_payment_dispute(dispute_id: str, accept_data: dict) -> dict:
    """Accept a payment dispute."""
    return make_request(
        "POST", f"/fulfillment/v1/payment_dispute/{dispute_id}/accept", json_body=accept_data
    )


@mcp.tool()
def contest_payment_dispute(dispute_id: str, contest_data: dict) -> dict:
    """Contest a payment dispute."""
    return make_request(
        "POST", f"/fulfillment/v1/payment_dispute/{dispute_id}/contest", json_body=contest_data
    )


@mcp.tool()
def add_evidence(dispute_id: str, evidence_data: dict) -> dict:
    """Add evidence to a payment dispute."""
    return make_request(
        "POST", f"/fulfillment/v1/payment_dispute/{dispute_id}/add_evidence", json_body=evidence_data
    )


@mcp.tool()
def update_evidence(dispute_id: str, evidence_id: str, evidence_data: dict) -> dict:
    """Update evidence in a payment dispute."""
    return make_request(
        "PUT",
        f"/fulfillment/v1/payment_dispute/{dispute_id}/evidence/{evidence_id}",
        json_body=evidence_data,
    )


@mcp.tool()
def get_fulfillment_activities(order_id: str) -> dict:
    """Retrieve fulfillment activities for an order."""
    return make_request("GET", f"/fulfillment/v1/order/{order_id}/activities")


# ============================================================================
# ACCOUNT API TOOLS
# ============================================================================


@mcp.tool()
def create_fulfillment_policy(policy_data: dict) -> dict:
    """Create a fulfillment policy."""
    return make_request("POST", "/account/v1/fulfillment_policy", json_body=policy_data)


@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Retrieve details of a specific fulfillment policy."""
    return make_request("GET", f"/account/v1/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def get_fulfillment_policies() -> dict:
    """Retrieve all fulfillment policies."""
    return make_request("GET", "/account/v1/fulfillment_policy")


@mcp.tool()
def get_fulfillment_policy_by_name(name: str) -> dict:
    """Retrieve a fulfillment policy by name."""
    params = {"name": name}
    return make_request("GET", "/account/v1/fulfillment_policy_by_name", params=params)


@mcp.tool()
def update_fulfillment_policy(fulfillment_policy_id: str, policy_data: dict) -> dict:
    """Update a fulfillment policy."""
    return make_request(
        "PUT", f"/account/v1/fulfillment_policy/{fulfillment_policy_id}", json_body=policy_data
    )


@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Delete a fulfillment policy."""
    return make_request("DELETE", f"/account/v1/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def create_payment_policy(policy_data: dict) -> dict:
    """Create a payment policy."""
    return make_request("POST", "/account/v1/payment_policy", json_body=policy_data)


@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> dict:
    """Retrieve details of a specific payment policy."""
    return make_request("GET", f"/account/v1/payment_policy/{payment_policy_id}")


@mcp.tool()
def get_payment_policies() -> dict:
    """Retrieve all payment policies."""
    return make_request("GET", "/account/v1/payment_policy")


@mcp.tool()
def get_payment_policy_by_name(name: str) -> dict:
    """Retrieve a payment policy by name."""
    params = {"name": name}
    return make_request("GET", "/account/v1/payment_policy_by_name", params=params)


@mcp.tool()
def update_payment_policy(payment_policy_id: str, policy_data: dict) -> dict:
    """Update a payment policy."""
    return make_request(
        "PUT", f"/account/v1/payment_policy/{payment_policy_id}", json_body=policy_data
    )


@mcp.tool()
def delete_payment_policy(payment_policy_id: str) -> dict:
    """Delete a payment policy."""
    return make_request("DELETE", f"/account/v1/payment_policy/{payment_policy_id}")


@mcp.tool()
def create_return_policy(policy_data: dict) -> dict:
    """Create a return policy."""
    return make_request("POST", "/account/v1/return_policy", json_body=policy_data)


@mcp.tool()
def get_return_policy(return_policy_id: str) -> dict:
    """Retrieve details of a specific return policy."""
    return make_request("GET", f"/account/v1/return_policy/{return_policy_id}")


@mcp.tool()
def get_return_policies() -> dict:
    """Retrieve all return policies."""
    return make_request("GET", "/account/v1/return_policy")


@mcp.tool()
def get_return_policy_by_name(name: str) -> dict:
    """Retrieve a return policy by name."""
    params = {"name": name}
    return make_request("GET", "/account/v1/return_policy_by_name", params=params)


@mcp.tool()
def update_return_policy(return_policy_id: str, policy_data: dict) -> dict:
    """Update a return policy."""
    return make_request(
        "PUT", f"/account/v1/return_policy/{return_policy_id}", json_body=policy_data
    )


@mcp.tool()
def delete_return_policy(return_policy_id: str) -> dict:
    """Delete a return policy."""
    return make_request("DELETE", f"/account/v1/return_policy/{return_policy_id}")


@mcp.tool()
def create_custom_policy(policy_data: dict) -> dict:
    """Create a custom policy."""
    return make_request("POST", "/account/v1/custom_policy", json_body=policy_data)


@mcp.tool()
def get_custom_policy(custom_policy_id: str) -> dict:
    """Retrieve details of a specific custom policy."""
    return make_request("GET", f"/account/v1/custom_policy/{custom_policy_id}")


@mcp.tool()
def get_custom_policies(policy_type: Optional[str] = None) -> dict:
    """Retrieve all custom policies."""
    params = {}
    if policy_type:
        params["policyType"] = policy_type
    return make_request("GET", "/account/v1/custom_policy", params=params)


@mcp.tool()
def update_custom_policy(custom_policy_id: str, policy_data: dict) -> dict:
    """Update a custom policy."""
    return make_request(
        "PUT", f"/account/v1/custom_policy/{custom_policy_id}", json_body=policy_data
    )


@mcp.tool()
def get_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """Retrieve sales tax information."""
    params = {"countryCode": country_code, "jurisdictionId": jurisdiction_id}
    return make_request("GET", "/account/v1/sales_tax", params=params)


@mcp.tool()
def get_sales_taxes() -> dict:
    """Retrieve all sales tax information."""
    return make_request("GET", "/account/v1/sales_tax")


@mcp.tool()
def create_or_replace_sales_tax(
    country_code: str, jurisdiction_id: str, tax_data: dict
) -> dict:
    """Create or replace sales tax information."""
    return make_request(
        "PUT",
        f"/account/v1/sales_tax/{country_code}/{jurisdiction_id}",
        json_body=tax_data,
    )


@mcp.tool()
def delete_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """Delete sales tax information."""
    return make_request("DELETE", f"/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


@mcp.tool()
def get_privileges() -> dict:
    """Retrieve seller privileges."""
    return make_request("GET", "/account/v1/privilege")


@mcp.tool()
def get_opted_in_programs() -> dict:
    """Retrieve programs the seller has opted into."""
    return make_request("GET", "/account/v1/program/opted_in")


@mcp.tool()
def opt_in_to_program(program_data: dict) -> dict:
    """Opt into a seller program."""
    return make_request("POST", "/account/v1/program/opt_in", json_body=program_data)


@mcp.tool()
def opt_out_of_program(program_data: dict) -> dict:
    """Opt out of a seller program."""
    return make_request("POST", "/account/v1/program/opt_out", json_body=program_data)


@mcp.tool()
def get_rate_tables() -> dict:
    """Retrieve shipping rate tables."""
    return make_request("GET", "/account/v1/rate_table")


# ============================================================================
# MARKETING API TOOLS
# ============================================================================


@mcp.tool()
def create_campaign(campaign_data: dict) -> dict:
    """Create an advertising campaign."""
    return make_request("POST", "/marketing/v1/ad_campaign", json_body=campaign_data)


@mcp.tool()
def get_campaign(campaign_id: str) -> dict:
    """Retrieve details of a specific campaign."""
    return make_request("GET", f"/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def get_campaigns(
    campaign_status: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Retrieve a list of campaigns."""
    params = {"limit": limit, "offset": offset}
    if campaign_status:
        params["campaign_status"] = campaign_status
    return make_request("GET", "/marketing/v1/ad_campaign", params=params)


@mcp.tool()
def update_campaign(campaign_id: str, campaign_data: dict) -> dict:
    """Update an advertising campaign."""
    return make_request(
        "PUT", f"/marketing/v1/ad_campaign/{campaign_id}", json_body=campaign_data
    )


@mcp.tool()
def delete_campaign(campaign_id: str) -> dict:
    """Delete an advertising campaign."""
    return make_request("DELETE", f"/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def clone_campaign(campaign_id: str, clone_data: dict) -> dict:
    """Clone an existing campaign."""
    return make_request(
        "POST", f"/marketing/v1/ad_campaign/{campaign_id}/clone", json_body=clone_data
    )


@mcp.tool()
def create_ad(ad_data: dict) -> dict:
    """Create an ad."""
    return make_request("POST", "/marketing/v1/ad", json_body=ad_data)


@mcp.tool()
def get_ad(ad_id: str) -> dict:
    """Retrieve details of a specific ad."""
    return make_request("GET", f"/marketing/v1/ad/{ad_id}")


@mcp.tool()
def get_ads(
    campaign_id: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Retrieve a list of ads."""
    params = {"limit": limit, "offset": offset}
    if campaign_id:
        params["campaign_id"] = campaign_id
    return make_request("GET", "/marketing/v1/ad", params=params)


@mcp.tool()
def update_ad(ad_id: str, ad_data: dict) -> dict:
    """Update an ad."""
    return make_request("PUT", f"/marketing/v1/ad/{ad_id}", json_body=ad_data)


@mcp.tool()
def delete_ad(ad_id: str) -> dict:
    """Delete an ad."""
    return make_request("DELETE", f"/marketing/v1/ad/{ad_id}")


@mcp.tool()
def update_bid(ad_id: str, bid_data: dict) -> dict:
    """Update the bid for an ad."""
    return make_request("PUT", f"/marketing/v1/ad/{ad_id}/bid", json_body=bid_data)


@mcp.tool()
def suggest_bids(suggest_data: dict) -> dict:
    """Get suggested bids for keywords."""
    return make_request("POST", "/marketing/v1/suggest_bids", json_body=suggest_data)


@mcp.tool()
def suggest_keywords(suggest_data: dict) -> dict:
    """Get suggested keywords for a campaign."""
    return make_request("POST", "/marketing/v1/suggest_keywords", json_body=suggest_data)


@mcp.tool()
def suggest_budget(suggest_data: dict) -> dict:
    """Get suggested budget for a campaign."""
    return make_request("POST", "/marketing/v1/suggest_budget", json_body=suggest_data)


# ============================================================================
# FINANCES API TOOLS
# ============================================================================


@mcp.tool()
def get_transactions(
    transaction_type: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Retrieve seller transactions."""
    params = {"limit": limit, "offset": offset}
    if transaction_type:
        params["transactionType"] = transaction_type
    return make_request("GET", "/finances/v1/transaction", params=params)


@mcp.tool()
def get_transaction_summary() -> dict:
    """Retrieve a summary of seller transactions."""
    return make_request("GET", "/finances/v1/transaction_summary")


@mcp.tool()
def get_payouts(limit: int = 25, offset: int = 0) -> dict:
    """Retrieve seller payouts."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/finances/v1/payout", params=params)


@mcp.tool()
def get_payout(payout_id: str) -> dict:
    """Retrieve details of a specific payout."""
    return make_request("GET", f"/finances/v1/payout/{payout_id}")


@mcp.tool()
def get_payout_summary() -> dict:
    """Retrieve a summary of seller payouts."""
    return make_request("GET", "/finances/v1/payout_summary")


@mcp.tool()
def get_seller_funds_summary() -> dict:
    """Retrieve seller funds summary."""
    return make_request("GET", "/finances/v1/seller_funds_summary")


@mcp.tool()
def get_billing_activities(
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Retrieve seller billing activities."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/finances/v1/billing_activity", params=params)


# ============================================================================
# FEED API TOOLS
# ============================================================================


@mcp.tool()
def create_task(task_data: dict) -> dict:
    """Create a feed task."""
    return make_request("POST", "/feed/v1/task", json_body=task_data)


@mcp.tool()
def get_task(task_id: str) -> dict:
    """Retrieve details of a specific task."""
    return make_request("GET", f"/feed/v1/task/{task_id}")


@mcp.tool()
def get_tasks(
    feed_type: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Retrieve a list of tasks."""
    params = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    return make_request("GET", "/feed/v1/task", params=params)


@mcp.tool()
def create_inventory_task(task_data: dict) -> dict:
    """Create an inventory feed task."""
    return make_request("POST", "/feed/v1/inventory_task", json_body=task_data)


@mcp.tool()
def get_inventory_task(task_id: str) -> dict:
    """Retrieve details of an inventory task."""
    return make_request("GET", f"/feed/v1/inventory_task/{task_id}")


@mcp.tool()
def get_inventory_tasks(limit: int = 25, offset: int = 0) -> dict:
    """Retrieve a list of inventory tasks."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/feed/v1/inventory_task", params=params)


@mcp.tool()
def create_order_task(task_data: dict) -> dict:
    """Create an order feed task."""
    return make_request("POST", "/feed/v1/order_task", json_body=task_data)


@mcp.tool()
def get_order_task(task_id: str) -> dict:
    """Retrieve details of an order task."""
    return make_request("GET", f"/feed/v1/order_task/{task_id}")


@mcp.tool()
def get_order_tasks(limit: int = 25, offset: int = 0) -> dict:
    """Retrieve a list of order tasks."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/feed/v1/order_task", params=params)


@mcp.tool()
def create_schedule(schedule_data: dict) -> dict:
    """Create a feed schedule."""
    return make_request("POST", "/feed/v1/schedule", json_body=schedule_data)


@mcp.tool()
def get_schedule(schedule_id: str) -> dict:
    """Retrieve details of a specific schedule."""
    return make_request("GET", f"/feed/v1/schedule/{schedule_id}")


@mcp.tool()
def get_schedules(limit: int = 25, offset: int = 0) -> dict:
    """Retrieve a list of schedules."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/feed/v1/schedule", params=params)


@mcp.tool()
def update_schedule(schedule_id: str, schedule_data: dict) -> dict:
    """Update a feed schedule."""
    return make_request(
        "PUT", f"/feed/v1/schedule/{schedule_id}", json_body=schedule_data
    )


@mcp.tool()
def delete_schedule(schedule_id: str) -> dict:
    """Delete a feed schedule."""
    return make_request("DELETE", f"/feed/v1/schedule/{schedule_id}")


# ============================================================================
# METADATA API TOOLS
# ============================================================================


@mcp.tool()
def get_category_policies(category_id: str, marketplace_id: str) -> dict:
    """Retrieve category policies."""
    params = {"category_id": category_id, "marketplace_id": marketplace_id}
    return make_request("GET", "/metadata/v1/category_policy", params=params)


@mcp.tool()
def get_item_condition_policies(category_id: str, marketplace_id: str) -> dict:
    """Retrieve item condition policies."""
    params = {"category_id": category_id, "marketplace_id": marketplace_id}
    return make_request("GET", "/metadata/v1/item_condition_policy", params=params)


@mcp.tool()
def get_listing_type_policies(category_id: str, marketplace_id: str) -> dict:
    """Retrieve listing type policies."""
    params = {"category_id": category_id, "marketplace_id": marketplace_id}
    return make_request("GET", "/metadata/v1/listing_type_policy", params=params)


@mcp.tool()
def get_currencies() -> dict:
    """Retrieve supported currencies."""
    return make_request("GET", "/metadata/v1/currency")


# ============================================================================
# COMPLIANCE API TOOLS
# ============================================================================


@mcp.tool()
def get_listing_violations(
    compliance_type: str,
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Retrieve listing violations."""
    params = {"complianceType": compliance_type, "limit": limit, "offset": offset}
    return make_request("GET", "/compliance/v1/listing_violation", params=params)


@mcp.tool()
def get_listing_violations_summary(compliance_type: str) -> dict:
    """Retrieve a summary of listing violations."""
    params = {"complianceType": compliance_type}
    return make_request("GET", "/compliance/v1/listing_violation_summary", params=params)


# ============================================================================
# ANALYTICS API TOOLS
# ============================================================================


@mcp.tool()
def get_traffic_report(
    marketplace_id: str,
    metric_type: str,
    dimension: Optional[str] = None,
) -> dict:
    """Retrieve traffic report data."""
    params = {"marketplace_id": marketplace_id, "metric_type": metric_type}
    if dimension:
        params["dimension"] = dimension
    return make_request("GET", "/analytics/v1/traffic_report", params=params)


@mcp.tool()
def get_seller_standards_profile(
    marketplace_id: str,
    metric_type: Optional[str] = None,
) -> dict:
    """Retrieve seller standards profile."""
    params = {"marketplace_id": marketplace_id}
    if metric_type:
        params["metric_type"] = metric_type
    return make_request("GET", "/analytics/v1/seller_standards_profile", params=params)


@mcp.tool()
def find_seller_standards_profiles(
    marketplace_id: str,
    metric_type: Optional[str] = None,
) -> dict:
    """Find seller standards profiles."""
    params = {"marketplace_id": marketplace_id}
    if metric_type:
        params["metric_type"] = metric_type
    return make_request("GET", "/analytics/v1/seller_standards_profile_find", params=params)


# ============================================================================
# STORES API TOOLS
# ============================================================================


@mcp.tool()
def get_store() -> dict:
    """Retrieve store information."""
    return make_request("GET", "/stores/v1/store")


@mcp.tool()
def get_store_categories() -> dict:
    """Retrieve store categories."""
    return make_request("GET", "/stores/v1/store_category")


@mcp.tool()
def add_store_category(category_data: dict) -> dict:
    """Add a store category."""
    return make_request("POST", "/stores/v1/store_category", json_body=category_data)


@mcp.tool()
def rename_store_category(category_id: str, category_data: dict) -> dict:
    """Rename a store category."""
    return make_request(
        "PUT", f"/stores/v1/store_category/{category_id}", json_body=category_data
    )


@mcp.tool()
def delete_store_category(category_id: str) -> dict:
    """Delete a store category."""
    return make_request("DELETE", f"/stores/v1/store_category/{category_id}")


@mcp.tool()
def move_store_category(category_id: str, move_data: dict) -> dict:
    """Move a store category."""
    return make_request(
        "PUT", f"/stores/v1/store_category/{category_id}/move", json_body=move_data
    )


# ============================================================================
# NEGOTIATION API TOOLS
# ============================================================================


@mcp.tool()
def find_eligible_items(
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Find items eligible for best offer."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/negotiation/v1/find_eligible_items", params=params)


@mcp.tool()
def send_offer_to_interested_buyers(offer_data: dict) -> dict:
    """Send an offer to interested buyers."""
    return make_request(
        "POST", "/negotiation/v1/send_offer_to_interested_buyers", json_body=offer_data
    )


# ============================================================================
# RECOMMENDATION API TOOLS
# ============================================================================


@mcp.tool()
def find_listing_recommendations(
    marketplace_id: str,
    limit: int = 25,
    offset: int = 0,
) -> dict:
    """Find listing recommendations."""
    params = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    return make_request("GET", "/recommendation/v1/find_listing_recommendations", params=params)


if __name__ == "__main__":
    mcp.run()


if __name__ == "__main__":
    mcp.run()
