#!/usr/bin/env python3
"""
eBay Sell API MCP Server

This server provides MCP tools for interacting with eBay's Sell API.
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("ebay-sell-api")

# Base URLs
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com"
}

def get_environment():
    """Get the eBay environment from environment variable."""
    return os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

def get_base_url():
    """Get the base URL based on environment."""
    return BASE_URLS.get(get_environment(), BASE_URLS["SANDBOX"])

def get_auth_headers():
    """Get authentication headers from environment variables."""
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
    
    if not all([app_id, cert_id, refresh_token]):
        return None
    
    # Get access token using refresh token
    token_url = "https://api.ebay.com/oauth2/token"
    auth = requests.auth.HTTPBasicAuth(app_id, cert_id)
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    
    try:
        response = requests.post(token_url, auth=auth, data=payload)
        response.raise_for_status()
        access_token = response.json().get("access_token")
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    except Exception as e:
        return {"error": f"Authentication failed: {str(e)}"}

def make_request(method, path, params=None, data=None, headers=None):
    """Make a request to the eBay API."""
    auth_headers = get_auth_headers()
    if auth_headers is None:
        return {"error": "Missing required authentication credentials"}
    if isinstance(auth_headers, dict) and "error" in auth_headers:
        return auth_headers
    
    all_headers = {**auth_headers}
    if headers:
        all_headers.update(headers)
    
    url = f"{get_base_url()}{path}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=all_headers,
            params=params,
            json=data
        )
        response.raise_for_status()
        
        if response.status_code == 204:  # No Content
            return {"message": "Operation successful"}
        
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {"error": f"Resource not found: {path}"}
        try:
            error_response = e.response.json()
            return {"error": str(error_response)}
        except:
            return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

# ============================================================================
# INVENTORY API
# ============================================================================

@mcp.tool()
def get_offer(offer_id: str) -> dict:
    """
    Retrieves a specific published or unpublished offer by offerId.
    """
    return make_request("GET", f"/offer/{offer_id}")

@mcp.tool()
def create_offer(content_language: str = "en-US", content_type: str = "application/json", **kwargs) -> dict:
    """
    Creates an offer for a specific inventory item.
    """
    headers = {
        "Content-Language": content_language,
        "Content-Type": content_type
    }
    return make_request("POST", "/offer", data=kwargs, headers=headers)

@mcp.tool()
def update_offer(offer_id: str, content_language: str = "en-US", content_type: str = "application/json", **kwargs) -> dict:
    """
    Updates an existing offer.
    """
    headers = {
        "Content-Language": content_language,
        "Content-Type": content_type
    }
    return make_request("PUT", f"/offer/{offer_id}", data=kwargs, headers=headers)

@mcp.tool()
def delete_offer(offer_id: str) -> dict:
    """
    Deletes an offer.
    """
    return make_request("DELETE", f"/offer/{offer_id}")

@mcp.tool()
def get_offers(limit: int = 50, offset: int = 0, **kwargs) -> dict:
    """
    Retrieves multiple offers with optional filtering.
    """
    params = {"limit": str(limit), "offset": str(offset), **kwargs}
    return make_request("GET", "/offer", params=params)

@mcp.tool()
def publish_offer(offer_id: str) -> dict:
    """
    Publishes an offer to create an active eBay listing.
    """
    return make_request("POST", f"/offer/{offer_id}/publish")

@mcp.tool()
def withdraw_offer(offer_id: str) -> dict:
    """
    Withdraws a published offer, ending the listing.
    """
    return make_request("POST", f"/offer/{offer_id}/withdraw")

@mcp.tool()
def bulk_update_price_quantity(sku: str, price: float, quantity: int) -> dict:
    """
    Bulk updates price and quantity for an inventory item.
    """
    data = {
        "sku": sku,
        "price": {"value": str(price), "currency": "USD"},
        "quantity": quantity
    }
    return make_request("POST", "/inventory/bulk_update_price_quantity", data=data)

@mcp.tool()
def get_inventory_item(sku: str) -> dict:
    """
    Retrieves an inventory item by SKU.
    """
    return make_request("GET", f"/inventory_item/{sku}")

@mcp.tool()
def create_inventory_item(sku: str, title: str, description: str, condition: str = "NEW", **kwargs) -> dict:
    """
    Creates or replaces an inventory item.
    """
    data = {
        "sku": sku,
        "title": title,
        "description": description,
        "condition": condition,
        **kwargs
    }
    return make_request("POST", "/inventory_item", data=data)

@mcp.tool()
def update_inventory_item(sku: str, **kwargs) -> dict:
    """
    Updates an existing inventory item.
    """
    return make_request("PUT", f"/inventory_item/{sku}", data=kwargs)

@mcp.tool()
def delete_inventory_item(sku: str) -> dict:
    """
    Deletes an inventory item.
    """
    return make_request("DELETE", f"/inventory_item/{sku}")

@mcp.tool()
def get_inventory_locations(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves inventory locations.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/inventory_location", params=params)

@mcp.tool()
def get_inventory_location(location_id: str) -> dict:
    """
    Retrieves a specific inventory location by ID.
    """
    return make_request("GET", f"/inventory_location/{location_id}")

@mcp.tool()
def create_inventory_location(name: str, address: dict, **kwargs) -> dict:
    """
    Creates a new inventory location.
    """
    data = {"name": name, "address": address, **kwargs}
    return make_request("POST", "/inventory_location", data=data)

@mcp.tool()
def update_inventory_location(location_id: str, **kwargs) -> dict:
    """
    Updates an existing inventory location.
    """
    return make_request("PUT", f"/inventory_location/{location_id}", data=kwargs)

@mcp.tool()
def delete_inventory_location(location_id: str) -> dict:
    """
    Deletes an inventory location.
    """
    return make_request("DELETE", f"/inventory_location/{location_id}")

@mcp.tool()
def enable_inventory_location(location_id: str) -> dict:
    """
    Enables an inventory location.
    """
    return make_request("POST", f"/inventory_location/{location_id}/enable")

@mcp.tool()
def disable_inventory_location(location_id: str) -> dict:
    """
    Disables an inventory location.
    """
    return make_request("POST", f"/inventory_location/{location_id}/disable")

@mcp.tool()
def bulk_create_offer(**kwargs) -> dict:
    """
    Creates multiple offers (up to 25) for specific inventory items.
    """
    return make_request("POST", "/bulk_create_offer", data=kwargs)

@mcp.tool()
def bulk_publish_offer(**kwargs) -> dict:
    """
    Publishes multiple offers at once.
    """
    return make_request("POST", "/bulk_publish_offer", data=kwargs)

@mcp.tool()
def bulk_create_or_replace_inventory_item(**kwargs) -> dict:
    """
    Creates or replaces up to 25 inventory items at once.
    """
    return make_request("POST", "/bulk_create_or_replace_inventory_item", data=kwargs)

@mcp.tool()
def bulk_migrate_listing(**kwargs) -> dict:
    """
    Bulk migrates listings.
    """
    return make_request("POST", "/bulk_migrate_listing", data=kwargs)

@mcp.tool()
def bulk_get_inventory_item(skus: list) -> dict:
    """
    Retrieves up to 25 inventory items by SKU.
    """
    return make_request("POST", "/bulk_get_inventory_item", data={"sku": skus})

@mcp.tool()
def get_inventory_items(limit: int = 50, offset: int = 0) -> dict:
    """
    Retrieves all inventory items with pagination.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/inventory_item", params=params)

@mcp.tool()
def create_or_replace_inventory_item_group(name: str, **kwargs) -> dict:
    """
    Creates or replaces an inventory item group.
    """
    data = {"name": name, **kwargs}
    return make_request("POST", "/inventory_item_group", data=data)

@mcp.tool()
def get_inventory_item_group(group_id: str) -> dict:
    """
    Retrieves an inventory item group by ID.
    """
    return make_request("GET", f"/inventory_item_group/{group_id}")

@mcp.tool()
def delete_inventory_item_group(group_id: str) -> dict:
    """
    Deletes an inventory item group.
    """
    return make_request("DELETE", f"/inventory_item_group/{group_id}")

@mcp.tool()
def publish_offer_by_inventory_item_group(group_id: str) -> dict:
    """
    Publishes all offers in an inventory item group.
    """
    return make_request("POST", f"/inventory_item_group/{group_id}/publish")

@mcp.tool()
def withdraw_offer_by_inventory_item_group(group_id: str) -> dict:
    """
    Withdraws all offers in an inventory item group.
    """
    return make_request("POST", f"/inventory_item_group/{group_id}/withdraw")

@mcp.tool()
def create_or_replace_product_compatibility(sku: str, **kwargs) -> dict:
    """
    Creates or replaces product compatibility for an inventory item.
    """
    return make_request("POST", f"/inventory_item/{sku}/product_compatibility", data=kwargs)

@mcp.tool()
def get_product_compatibility(sku: str, compatibility_id: str) -> dict:
    """
    Retrieves product compatibility for an inventory item.
    """
    return make_request("GET", f"/inventory_item/{sku}/product_compatibility/{compatibility_id}")

@mcp.tool()
def delete_product_compatibility(sku: str, compatibility_id: str) -> dict:
    """
    Deletes product compatibility for an inventory item.
    """
    return make_request("DELETE", f"/inventory_item/{sku}/product_compatibility/{compatibility_id}")

@mcp.tool()
def create_or_replace_sku_location_mapping(sku: str, location_id: str, **kwargs) -> dict:
    """
    Creates or replaces SKU location mapping.
    """
    return make_request("POST", f"/inventory_item/{sku}/location/{location_id}", data=kwargs)

@mcp.tool()
def get_sku_location_mapping(sku: str, location_id: str) -> dict:
    """
    Retrieves SKU location mapping.
    """
    return make_request("GET", f"/inventory_item/{sku}/location/{location_id}")

@mcp.tool()
def delete_sku_location_mapping(sku: str, location_id: str) -> dict:
    """
    Deletes SKU location mapping.
    """
    return make_request("DELETE", f"/inventory_item/{sku}/location/{location_id}")

@mcp.tool()
def get_listing_fees(**kwargs) -> dict:
    """
    Retrieves listing fees.
    """
    return make_request("GET", "/listing_fee", params=kwargs)

# ============================================================================
# FULFILLMENT API
# ============================================================================

@mcp.tool()
def get_order(order_id: str, field_groups: str = None) -> dict:
    """
    Retrieves the contents of an order by its unique identifier.
    """
    params = {}
    if field_groups:
        params["fieldGroups"] = field_groups
    return make_request("GET", f"/order/{order_id}", params=params)

@mcp.tool()
def get_orders(field_groups: str = None, filter: str = None, limit: int = 50, offset: int = 0, order_ids: str = None) -> dict:
    """
    Searches for and retrieves orders based on various filters.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if field_groups:
        params["fieldGroups"] = field_groups
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    return make_request("GET", "/order", params=params)

@mcp.tool()
def create_shipping_fulfillment(order_id: str, lines: list, ship_date: str = None, tracking_number: str = None, **kwargs) -> dict:
    """
    Creates a shipping fulfillment for an order.
    """
    data = {
        "lines": lines,
        **kwargs
    }
    if ship_date:
        data["shipDate"] = ship_date
    if tracking_number:
        data["trackingNumber"] = tracking_number
    return make_request("POST", f"/order/{order_id}/shipping_fulfillment", data=data)

@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """
    Retrieves a specific shipping fulfillment.
    """
    return make_request("GET", f"/order/{order_id}/shipping_fulfillment/{fulfillment_id}")

@mcp.tool()
def get_shipping_fulfillments(order_id: str, limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves shipping fulfillments for an order.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", f"/order/{order_id}/shipping_fulfillment", params=params)

@mcp.tool()
def issue_refund(order_id: str, refund_amount: float, reason: str = "CUSTOMER_CANCEL", **kwargs) -> dict:
    """
    Issues a refund for an order.
    """
    data = {
        "refundAmount": {"value": str(refund_amount), "currency": "USD"},
        "refundReason": reason,
        **kwargs
    }
    return make_request("POST", f"/order/{order_id}/issue_refund", data=data)

@mcp.tool()
def get_payment_dispute(payment_dispute_id: str) -> dict:
    """
    Retrieves detailed information on a specific payment dispute.
    """
    return make_request("GET", f"/payment_dispute/{payment_dispute_id}")

@mcp.tool()
def get_payment_dispute_summaries(limit: int = 200, offset: int = 0, **kwargs) -> dict:
    """
    Retrieves payment disputes with optional filtering.
    """
    params = {"limit": str(limit), "offset": str(offset), **kwargs}
    return make_request("GET", "/payment_dispute_summary", params=params)

@mcp.tool()
def accept_payment_dispute(payment_dispute_id: str, **kwargs) -> dict:
    """
    Accepts a payment dispute.
    """
    return make_request("POST", f"/payment_dispute/{payment_dispute_id}/accept", data=kwargs)

@mcp.tool()
def contest_payment_dispute(payment_dispute_id: str, revision: int, **kwargs) -> dict:
    """
    contests a payment dispute.
    """
    data = {"revision": revision, **kwargs}
    return make_request("POST", f"/payment_dispute/{payment_dispute_id}/contest", data=data)

@mcp.tool()
def add_evidence(payment_dispute_id: str, files: list, evidence_type: str, **kwargs) -> dict:
    """
    Adds evidence files to a payment dispute.
    """
    data = {
        "files": files,
        "evidenceType": evidence_type,
        **kwargs
    }
    return make_request("POST", f"/payment_dispute/{payment_dispute_id}/add_evidence", data=data)

@mcp.tool()
def update_evidence(payment_dispute_id: str, evidence_id: str, **kwargs) -> dict:
    """
    Updates evidence for a payment dispute.
    """
    return make_request("PUT", f"/payment_dispute/{payment_dispute_id}/evidence/{evidence_id}", data=kwargs)

@mcp.tool()
def fetch_evidence_content(payment_dispute_id: str, evidence_id: str) -> dict:
    """
    Fetches evidence content.
    """
    return make_request("GET", f"/payment_dispute/{payment_dispute_id}/evidence/{evidence_id}/content")

@mcp.tool()
def upload_evidence_file(payment_dispute_id: str, **kwargs) -> dict:
    """
    Uploads an evidence file.
    """
    return make_request("POST", f"/payment_dispute/{payment_dispute_id}/evidence/upload", data=kwargs)

@mcp.tool()
def get_activities(limit: int = 50, offset: int = 0, **kwargs) -> dict:
    """
    Retrieves activity records.
    """
    params = {"limit": str(limit), "offset": str(offset), **kwargs}
    return make_request("GET", "/activity", params=params)

# ============================================================================
# ACCOUNT API
# ============================================================================

@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> dict:
    """
    Retrieves a payment policy by its ID.
    """
    return make_request("GET", f"/payment_policy/{payment_policy_id}")

@mcp.tool()
def get_payment_policies(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves all payment policies.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/payment_policy", params=params)

@mcp.tool()
def create_payment_policy(name: str, description: str = None, payment_instructions: str = None, **kwargs) -> dict:
    """
    Creates a new payment policy.
    """
    data = {"name": name, **kwargs}
    if description:
        data["description"] = description
    if payment_instructions:
        data["paymentInstructions"] = payment_instructions
    return make_request("POST", "/payment_policy", data=data)

@mcp.tool()
def update_payment_policy(payment_policy_id: str, **kwargs) -> dict:
    """
    Updates an existing payment policy.
    """
    return make_request("PUT", f"/payment_policy/{payment_policy_id}", data=kwargs)

@mcp.tool()
def delete_payment_policy(payment_policy_id: str) -> dict:
    """
    Deletes a payment policy.
    """
    return make_request("DELETE", f"/payment_policy/{payment_policy_id}")

@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """
    Retrieves a fulfillment policy by its ID.
    """
    return make_request("GET", f"/fulfillment_policy/{fulfillment_policy_id}")

@mcp.tool()
def get_fulfillment_policies(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves all fulfillment policies.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/fulfillment_policy", params=params)

@mcp.tool()
def create_fulfillment_policy(name: str, description: str = None, **kwargs) -> dict:
    """
    Creates a new fulfillment policy.
    """
    data = {"name": name, **kwargs}
    if description:
        data["description"] = description
    return make_request("POST", "/fulfillment_policy", data=data)

@mcp.tool()
def update_fulfillment_policy(fulfillment_policy_id: str, **kwargs) -> dict:
    """
    Updates an existing fulfillment policy.
    """
    return make_request("PUT", f"/fulfillment_policy/{fulfillment_policy_id}", data=kwargs)

@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """
    Deletes a fulfillment policy.
    """
    return make_request("DELETE", f"/fulfillment_policy/{fulfillment_policy_id}")

@mcp.tool()
def get_return_policy(return_policy_id: str) -> dict:
    """
    Retrieves a return policy by its ID.
    """
    return make_request("GET", f"/return_policy/{return_policy_id}")

@mcp.tool()
def get_return_policies(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves all return policies.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/return_policy", params=params)

@mcp.tool()
def create_return_policy(name: str, description: str = None, **kwargs) -> dict:
    """
    Creates a new return policy.
    """
    data = {"name": name, **kwargs}
    if description:
        data["description"] = description
    return make_request("POST", "/return_policy", data=data)

@mcp.tool()
def update_return_policy(return_policy_id: str, **kwargs) -> dict:
    """
    Updates an existing return policy.
    """
    return make_request("PUT", f"/return_policy/{return_policy_id}", data=kwargs)

@mcp.tool()
def delete_return_policy(return_policy_id: str) -> dict:
    """
    Deletes a return policy.
    """
    return make_request("DELETE", f"/return_policy/{return_policy_id}")

@mcp.tool()
def get_sales_tax(sales_tax_id: str) -> dict:
    """
    Retrieves a sales tax by its ID.
    """
    return make_request("GET", f"/sales_tax/{sales_tax_id}")

@mcp.tool()
def get_sales_taxes(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves all sales taxes.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/sales_tax", params=params)

@mcp.tool()
def create_sales_tax(country: str, region: str, rate: float, **kwargs) -> dict:
    """
    Creates a new sales tax.
    """
    data = {
        "country": country,
        "region": region,
        "rate": rate,
        **kwargs
    }
    return make_request("POST", "/sales_tax", data=data)

@mcp.tool()
def update_sales_tax(sales_tax_id: str, **kwargs) -> dict:
    """
    Updates an existing sales tax.
    """
    return make_request("PUT", f"/sales_tax/{sales_tax_id}", data=kwargs)

@mcp.tool()
def delete_sales_tax(sales_tax_id: str) -> dict:
    """
    Deletes a sales tax.
    """
    return make_request("DELETE", f"/sales_tax/{sales_tax_id}")

@mcp.tool()
def get_custom_policy(custom_policy_id: str) -> dict:
    """
    Retrieves a custom policy by its ID.
    """
    return make_request("GET", f"/custom_policy/{custom_policy_id}")

@mcp.tool()
def get_custom_policies(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves all custom policies.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/custom_policy", params=params)

@mcp.tool()
def create_custom_policy(name: str, **kwargs) -> dict:
    """
    Creates a new custom policy.
    """
    data = {"name": name, **kwargs}
    return make_request("POST", "/custom_policy", data=data)

@mcp.tool()
def update_custom_policy(custom_policy_id: str, **kwargs) -> dict:
    """
    Updates an existing custom policy.
    """
    return make_request("PUT", f"/custom_policy/{custom_policy_id}", data=kwargs)

@mcp.tool()
def get_opted_in_programs(**kwargs) -> dict:
    """
    Retrieves all opted-in programs.
    """
    return make_request("GET", "/opted_in_program", params=kwargs)

@mcp.tool()
def get_payments_program(**kwargs) -> dict:
    """
    Retrieves payments program details.
    """
    return make_request("GET", "/payments_program", params=kwargs)

@mcp.tool()
def get_payments_program_onboarding(**kwargs) -> dict:
    """
    Retrieves payments program onboarding details.
    """
    return make_request("GET", "/payments_program_onboarding", params=kwargs)

@mcp.tool()
def get_privileges(**kwargs) -> dict:
    """
    Retrieves seller privileges.
    """
    return make_request("GET", "/privilege", params=kwargs)

@mcp.tool()
def get_rate_tables(**kwargs) -> dict:
    """
    Retrieves rate tables.
    """
    return make_request("GET", "/rate_table", params=kwargs)

@mcp.tool()
def get_subscription(**kwargs) -> dict:
    """
    Retrieves subscription details.
    """
    return make_request("GET", "/subscription", params=kwargs)

@mcp.tool()
def opt_in_to_program(program_id: str, **kwargs) -> dict:
    """
    Opt-in to a program.
    """
    return make_request("POST", f"/program/{program_id}/opt_in", data=kwargs)

@mcp.tool()
def opt_out_of_program(program_id: str, **kwargs) -> dict:
    """
    Opt-out of a program.
    """
    return make_request("POST", f"/program/{program_id}/opt_out", data=kwargs)

@mcp.tool()
def get_fulfillment_policy_by_name(fulfillment_policy_name: str) -> dict:
    """
    Retrieves a fulfillment policy by name.
    """
    return make_request("GET", f"/fulfillment_policy/{fulfillment_policy_name}")

@mcp.tool()
def get_payment_policy_by_name(payment_policy_name: str) -> dict:
    """
    Retrieves a payment policy by name.
    """
    return make_request("GET", f"/payment_policy/{payment_policy_name}")

@mcp.tool()
def get_return_policy_by_name(return_policy_name: str) -> dict:
    """
    Retrieves a return policy by name.
    """
    return make_request("GET", f"/return_policy/{return_policy_name}")

@mcp.tool()
def bulk_create_or_replace_sales_tax(**kwargs) -> dict:
    """
    Bulk creates or replaces sales taxes.
    """
    return make_request("POST", "/sales_tax/bulk_create_or_replace", data=kwargs)

# ============================================================================
# MARKETING API
# ============================================================================

@mcp.tool()
def get_campaign(campaign_id: str) -> dict:
    """
    Retrieves a specific campaign by ID.
    """
    return make_request("GET", f"/ad_campaign/{campaign_id}")

@mcp.tool()
def get_campaign_by_name(campaign_name: str) -> dict:
    """
    Retrieves a campaign by its name.
    """
    return make_request("GET", "/ad_campaign", params={"campaign_name": campaign_name})

@mcp.tool()
def get_campaigns(limit: int = 10, offset: int = 0, **kwargs) -> dict:
    """
    Retrieves all campaigns with optional filtering.
    """
    params = {"limit": str(limit), "offset": str(offset), **kwargs}
    return make_request("GET", "/ad_campaign", params=params)

@mcp.tool()
def create_campaign(name: str, funding_model: str = "CPC", start_date: str = None, end_date: str = None, **kwargs) -> dict:
    """
    Creates a new marketing campaign.
    """
    data = {
        "name": name,
        "fundingModel": funding_model,
        **kwargs
    }
    if start_date:
        data["startDate"] = start_date
    if end_date:
        data["endDate"] = end_date
    return make_request("POST", "/ad_campaign", data=data)

@mcp.tool()
def update_campaign(campaign_id: str, **kwargs) -> dict:
    """
    Updates an existing campaign.
    """
    return make_request("PUT", f"/ad_campaign/{campaign_id}", data=kwargs)

@mcp.tool()
def delete_campaign(campaign_id: str) -> dict:
    """
    Deletes a campaign.
    """
    return make_request("DELETE", f"/ad_campaign/{campaign_id}")

@mcp.tool()
def clone_campaign(campaign_id: str, new_name: str) -> dict:
    """
    Clones an existing campaign.
    """
    data = {"name": new_name}
    return make_request("POST", f"/ad_campaign/{campaign_id}/clone", data=data)

@mcp.tool()
def get_ad(ad_id: str) -> dict:
    """
    Retrieves a specific ad by ID.
    """
    return make_request("GET", f"/ad/{ad_id}")

@mcp.tool()
def get_ads(limit: int = 10, offset: int = 0, **kwargs) -> dict:
    """
    Retrieves all ads with optional filtering.
    """
    params = {"limit": str(limit), "offset": str(offset), **kwargs}
    return make_request("GET", "/ad", params=params)

@mcp.tool()
def create_ad(campaign_id: str, listing_id: str, bid: float = None, **kwargs) -> dict:
    """
    Creates a new ad for a listing.
    """
    data = {
        "campaignId": campaign_id,
        "listingId": listing_id,
        **kwargs
    }
    if bid is not None:
        data["bid"] = bid
    return make_request("POST", "/ad", data=data)

@mcp.tool()
def update_ad(ad_id: str, **kwargs) -> dict:
    """
    Updates an existing ad.
    """
    return make_request("PUT", f"/ad/{ad_id}", data=kwargs)

@mcp.tool()
def delete_ad(ad_id: str) -> dict:
    """
    Deletes an ad.
    """
    return make_request("DELETE", f"/ad/{ad_id}")

@mcp.tool()
def bulk_update_ads_status(campaign_id: str, status: str, listing_ids: list = None, **kwargs) -> dict:
    """
    Bulk updates ad status for a campaign.
    """
    data = {
        "campaignId": campaign_id,
        "status": status,
        **kwargs
    }
    if listing_ids:
        data["listingIds"] = listing_ids
    return make_request("POST", "/ad/bulk_update_status", data=data)

@mcp.tool()
def bulk_update_ads_bid(campaign_id: str, bid: float, **kwargs) -> dict:
    """
    Bulk updates ad bid amounts.
    """
    data = {
        "campaignId": campaign_id,
        "bid": bid,
        **kwargs
    }
    return make_request("POST", "/ad/bulk_update_bid", data=data)

@mcp.tool()
def bulk_create_ads_by_inventory_reference(**kwargs) -> dict:
    """
    Bulk creates ads by inventory reference.
    """
    return make_request("POST", "/ad/bulk_create_by_inventory_reference", data=kwargs)

@mcp.tool()
def bulk_delete_ads_by_inventory_reference(**kwargs) -> dict:
    """
    Bulk deletes ads by inventory reference.
    """
    return make_request("POST", "/ad/bulk_delete_by_inventory_reference", data=kwargs)

@mcp.tool()
def bulk_delete_ads_by_listing_id(**kwargs) -> dict:
    """
    Bulk deletes ads by listing ID.
    """
    return make_request("POST", "/ad/bulk_delete_by_listing_id", data=kwargs)

@mcp.tool()
def get_ads_by_inventory_reference(inventory_reference_id: str) -> dict:
    """
    Retrieves ads by inventory reference.
    """
    return make_request("GET", f"/ad/inventory_reference/{inventory_reference_id}")

@mcp.tool()
def suggest_bids(listing_id: str, **kwargs) -> dict:
    """
    Suggests bid amounts for a listing.
    """
    params = {"listingId": listing_id, **kwargs}
    return make_request("GET", "/ad/suggest_bid", params=params)

@mcp.tool()
def suggest_budget(listing_id: str, **kwargs) -> dict:
    """
    Suggests budget for a listing.
    """
    params = {"listingId": listing_id, **kwargs}
    return make_request("GET", "/ad/suggest_budget", params=params)

@mcp.tool()
def suggest_keywords(listing_id: str, **kwargs) -> dict:
    """
    Suggests keywords for a listing.
    """
    params = {"listingId": listing_id, **kwargs}
    return make_request("GET", "/ad/suggest_keyword", params=params)

@mcp.tool()
def update_bid(ad_id: str, bid: float, **kwargs) -> dict:
    """
    Updates ad bid amount.
    """
    data = {"bid": bid, **kwargs}
    return make_request("PUT", f"/ad/{ad_id}/bid", data=data)

@mcp.tool()
def update_item_price_markdown_promotion(promotion_id: str, **kwargs) -> dict:
    """
    Updates item price markdown promotion.
    """
    return make_request("PUT", f"/promotion/{promotion_id}/price_markdown", data=kwargs)

@mcp.tool()
def update_item_promotion(promotion_id: str, **kwargs) -> dict:
    """
    Updates item promotion.
    """
    return make_request("PUT", f"/promotion/{promotion_id}", data=kwargs)

@mcp.tool()
def update_negative_keyword(ad_id: str, **kwargs) -> dict:
    """
    Updates negative keyword for an ad.
    """
    return make_request("PUT", f"/ad/{ad_id}/negative_keyword", data=kwargs)

@mcp.tool()
def find_campaign_by_ad_reference(ad_reference_id: str) -> dict:
    """
    Finds campaign by ad reference.
    """
    return make_request("GET", f"/campaign/ad_reference/{ad_reference_id}")

@mcp.tool()
def get_ad_group(ad_group_id: str) -> dict:
    """
    Retrieves an ad group by ID.
    """
    return make_request("GET", f"/ad_group/{ad_group_id}")

@mcp.tool()
def get_ad_groups(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves all ad groups.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/ad_group", params=params)

@mcp.tool()
def create_ad_group(campaign_id: str, name: str, **kwargs) -> dict:
    """
    Creates a new ad group.
    """
    data = {
        "campaignId": campaign_id,
        "name": name,
        **kwargs
    }
    return make_request("POST", "/ad_group", data=data)

@mcp.tool()
def update_ad_group(ad_group_id: str, **kwargs) -> dict:
    """
    Updates an existing ad group.
    """
    return make_request("PUT", f"/ad_group/{ad_group_id}", data=kwargs)

@mcp.tool()
def delete_ad_group(ad_group_id: str) -> dict:
    """
    Deletes an ad group.
    """
    return make_request("DELETE", f"/ad_group/{ad_group_id}")

@mcp.tool()
def delete_report_task(task_id: str) -> dict:
    """
    Deletes a report task.
    """
    return make_request("DELETE", f"/report_task/{task_id}")

# ============================================================================
# FINANCES API
# ============================================================================

@mcp.tool()
def get_transactions(filter: str = None, limit: int = 20, offset: int = 0, sort: str = None, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves monetary transactions with optional filtering.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", "/transaction", params=params, headers=headers)

@mcp.tool()
def get_transaction_summary(filter: str = None, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves a summary of monetary transactions.
    """
    params = {}
    if filter:
        params["filter"] = filter
    
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", "/transaction_summary", params=params, headers=headers)

@mcp.tool()
def get_payout(payout_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves a specific payout by ID.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", f"/payout/{payout_id}", headers=headers)

@mcp.tool()
def get_payouts(filter: str = None, limit: int = 10, offset: int = 0, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves payouts with optional filtering.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", "/payout", params=params, headers=headers)

@mcp.tool()
def get_payout_summary(filter: str = None, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves a summary of payouts.
    """
    params = {}
    if filter:
        params["filter"] = filter
    
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", "/payout_summary", params=params, headers=headers)

@mcp.tool()
def get_seller_funds_summary(marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves a summary of seller funds.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", "/seller_funds_summary", headers=headers)

@mcp.tool()
def get_billing_activities(filter: str = None, limit: int = 10, offset: int = 0, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves billing activities.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", "/billing_activity", params=params, headers=headers)

@mcp.tool()
def get_transfer(transfer_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves a specific transfer by ID.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", f"/transfer/{transfer_id}", headers=headers)

# ============================================================================
# FEED API
# ============================================================================

@mcp.tool()
def create_inventory_task(feed_type: str, filters: dict = None) -> dict:
    """
    Creates an inventory-related task.
    """
    data = {"feedType": feed_type}
    if filters:
        data["filters"] = filters
    return make_request("POST", "/inventory_task", data=data)

@mcp.tool()
def get_inventory_task(task_id: str) -> dict:
    """
    Retrieves a specific inventory task by ID.
    """
    return make_request("GET", f"/inventory_task/{task_id}")

@mcp.tool()
def get_inventory_tasks(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves inventory tasks with optional pagination.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/inventory_task", params=params)

@mcp.tool()
def get_inventory_task_input_file(task_id: str) -> dict:
    """
    Retrieves the input file for an inventory task.
    """
    return make_request("GET", f"/inventory_task/{task_id}/input_file")

@mcp.tool()
def get_inventory_task_result_file(task_id: str) -> dict:
    """
    Retrieves the result file for an inventory task.
    """
    return make_request("GET", f"/inventory_task/{task_id}/result_file")

@mcp.tool()
def get_latest_inventory_task_result_file() -> dict:
    """
    Retrieves the latest result file for an inventory task.
    """
    return make_request("GET", "/inventory_task/latest/result_file")

@mcp.tool()
def create_order_task(feed_type: str, filters: dict = None) -> dict:
    """
    Creates an order-related task.
    """
    data = {"feedType": feed_type}
    if filters:
        data["filters"] = filters
    return make_request("POST", "/order_task", data=data)

@mcp.tool()
def get_order_task(task_id: str) -> dict:
    """
    Retrieves a specific order task by ID.
    """
    return make_request("GET", f"/order_task/{task_id}")

@mcp.tool()
def get_order_tasks(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves order tasks with optional pagination.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/order_task", params=params)

@mcp.tool()
def create_customer_service_metric_task(feed_type: str, filters: dict = None) -> dict:
    """
    Creates a customer service metric task.
    """
    data = {"feedType": feed_type}
    if filters:
        data["filters"] = filters
    return make_request("POST", "/customer_service_metric_task", data=data)

@mcp.tool()
def get_customer_service_metric_task(task_id: str) -> dict:
    """
    Retrieves a specific customer service metric task by ID.
    """
    return make_request("GET", f"/customer_service_metric_task/{task_id}")

@mcp.tool()
def get_customer_service_metric_tasks(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves customer service metric tasks with optional pagination.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/customer_service_metric_task", params=params)

@mcp.tool()
def get_schedule(schedule_id: str) -> dict:
    """
    Retrieves a specific feed schedule by ID.
    """
    return make_request("GET", f"/schedule/{schedule_id}")

@mcp.tool()
def get_schedules(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves feed schedules with optional pagination.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/schedule", params=params)

@mcp.tool()
def create_schedule(name: str, feed_type: str, start_time: str, frequency: str, **kwargs) -> dict:
    """
    Creates a new feed schedule.
    """
    data = {
        "name": name,
        "feedType": feed_type,
        "startTime": start_time,
        "frequency": frequency,
        **kwargs
    }
    return make_request("POST", "/schedule", data=data)

@mcp.tool()
def update_schedule(schedule_id: str, **kwargs) -> dict:
    """
    Updates an existing feed schedule.
    """
    return make_request("PUT", f"/schedule/{schedule_id}", data=kwargs)

@mcp.tool()
def delete_schedule(schedule_id: str) -> dict:
    """
    Deletes a feed schedule.
    """
    return make_request("DELETE", f"/schedule/{schedule_id}")

@mcp.tool()
def get_task(task_id: str) -> dict:
    """
    Retrieves a specific task by ID.
    """
    return make_request("GET", f"/task/{task_id}")

@mcp.tool()
def get_tasks(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves tasks with optional pagination.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/task", params=params)

@mcp.tool()
def create_task(task_type: str, **kwargs) -> dict:
    """
    Creates a new task.
    """
    data = {"taskType": task_type, **kwargs}
    return make_request("POST", "/task", data=data)

@mcp.tool()
def upload_file(content_type: str, **kwargs) -> dict:
    """
    Uploads a file.
    """
    headers = {"Content-Type": content_type}
    return make_request("POST", "/file_upload", data=kwargs, headers=headers)

@mcp.tool()
def get_schedule_template(template_id: str) -> dict:
    """
    Retrieves a schedule template by ID.
    """
    return make_request("GET", f"/schedule_template/{template_id}")

@mcp.tool()
def get_schedule_templates(**kwargs) -> dict:
    """
    Retrieves schedule templates.
    """
    return make_request("GET", "/schedule_template", params=kwargs)

# ============================================================================
# LOGISTICS API
# ============================================================================

@mcp.tool()
def get_shipping_quote(order_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves shipping quotes for an order.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", f"/order/{order_id}/shipping_quote", headers=headers)

@mcp.tool()
def create_shipping_quote(order_id: str, **kwargs) -> dict:
    """
    Creates a shipping quote for an order.
    """
    return make_request("POST", f"/order/{order_id}/shipping_quote", data=kwargs)

@mcp.tool()
def create_from_shipping_quote(quote_id: str, **kwargs) -> dict:
    """
    Creates a shipping label from a shipping quote.
    """
    return make_request("POST", f"/shipping_quote/{quote_id}/create_label", data=kwargs)

@mcp.tool()
def get_shipment(shipment_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieves a specific shipment by ID.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("GET", f"/shipment/{shipment_id}", headers=headers)

@mcp.tool()
def cancel_shipment(shipment_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Cancels a shipment.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return make_request("POST", f"/shipment/{shipment_id}/cancel", headers=headers)

@mcp.tool()
def download_label_file(label_id: str) -> dict:
    """
    Downloads a shipping label file.
    """
    return make_request("GET", f"/label_file/{label_id}/download")

# ============================================================================
# COMPLIANCE API
# ============================================================================

@mcp.tool()
def get_listing_violations(filter: str = None, limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves listing violations with optional filtering.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/listing_violation", params=params)

@mcp.tool()
def get_listing_violations_summary() -> dict:
    """
    Retrieves a summary of listing violations.
    """
    return make_request("GET", "/listing_violation_summary")

# ============================================================================
# ANALYTICS API
# ============================================================================

@mcp.tool()
def get_traffic_report(report_type: str, date_range: str, **kwargs) -> dict:
    """
    Retrieves traffic report data.
    """
    params = {"reportType": report_type, "dateRange": date_range, **kwargs}
    return make_request("GET", "/traffic_report", params=params)

@mcp.tool()
def get_seller_standards_profile(profile_id: str) -> dict:
    """
    Retrieves a seller standards profile by ID.
    """
    return make_request("GET", f"/seller_standards_profile/{profile_id}")

@mcp.tool()
def find_seller_standards_profiles(filter: str = None, limit: int = 10, offset: int = 0) -> dict:
    """
    Searches for seller standards profiles.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/seller_standards_profile", params=params)

@mcp.tool()
def get_customer_service_metric(metric_id: str) -> dict:
    """
    Retrieves a customer service metric by ID.
    """
    return make_request("GET", f"/customer_service_metric/{metric_id}")

# ============================================================================
# STORES API
# ============================================================================

@mcp.tool()
def get_store(store_id: str) -> dict:
    """
    Retrieves a store by ID.
    """
    return make_request("GET", f"/store/{store_id}")

@mcp.tool()
def get_store_categories(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves store categories with optional pagination.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/store/category", params=params)

@mcp.tool()
def add_store_category(name: str, parent_category_id: str = None, **kwargs) -> dict:
    """
    Adds a new store category.
    """
    data = {"name": name, **kwargs}
    if parent_category_id:
        data["parentCategoryId"] = parent_category_id
    return make_request("POST", "/store/category", data=data)

@mcp.tool()
def rename_store_category(category_id: str, name: str) -> dict:
    """
    Renames a store category.
    """
    data = {"name": name}
    return make_request("PUT", f"/store/category/{category_id}", data=data)

@mcp.tool()
def move_store_category(category_id: str, new_parent_category_id: str) -> dict:
    """
    Moves a store category to a new parent.
    """
    data = {"parentCategoryId": new_parent_category_id}
    return make_request("PUT", f"/store/category/{category_id}/move", data=data)

@mcp.tool()
def delete_store_category(category_id: str) -> dict:
    """
    Deletes a store category.
    """
    return make_request("DELETE", f"/store/category/{category_id}")

@mcp.tool()
def get_store_task(task_id: str) -> dict:
    """
    Retrieves a specific store task by ID.
    """
    return make_request("GET", f"/store/task/{task_id}")

@mcp.tool()
def get_store_tasks(limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieves store tasks with optional pagination.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    return make_request("GET", "/store/task", params=params)

# ============================================================================
# METADATA API
# ============================================================================

@mcp.tool()
def get_currencies() -> dict:
    """
    Retrieves supported currencies.
    """
    return make_request("GET", "/metadata/currency")

@mcp.tool()
def get_item_condition_policies() -> dict:
    """
    Retrieves item condition policies.
    """
    return make_request("GET", "/metadata/item_condition_policy")

@mcp.tool()
def get_category_policies(category_id: str = None) -> dict:
    """
    Retrieves category policies.
    """
    if category_id:
        return make_request("GET", f"/metadata/category_policy/{category_id}")
    return make_request("GET", "/metadata/category_policy")

@mcp.tool()
def get_listing_structure_policies() -> dict:
    """
    Retrieves listing structure policies.
    """
    return make_request("GET", "/metadata/listing_structure_policy")

@mcp.tool()
def get_automotive_parts_compatibility_policies(**kwargs) -> dict:
    """
    Retrieves automotive parts compatibility policies.
    """
    return make_request("GET", "/metadata/automotive_parts_compatibility_policy", params=kwargs)

@mcp.tool()
def get_classified_ad_policies(**kwargs) -> dict:
    """
    Retrieves classified ad policies.
    """
    return make_request("GET", "/metadata/classified_ad_policy", params=kwargs)

@mcp.tool()
def get_compatibilities_by_specification(**kwargs) -> dict:
    """
    Retrieves compatibilities by specification.
    """
    return make_request("GET", "/metadata/compatibility/by_specification", params=kwargs)

@mcp.tool()
def get_compatibility_property_names(**kwargs) -> dict:
    """
    Retrieves compatibility property names.
    """
    return make_request("GET", "/metadata/compatibility_property_name", params=kwargs)

@mcp.tool()
def get_compatibility_property_values(**kwargs) -> dict:
    """
    Retrieves compatibility property values.
    """
    return make_request("GET", "/metadata/compatibility_property_value", params=kwargs)

@mcp.tool()
def get_extended_producer_responsibility_policies(**kwargs) -> dict:
    """
    Retrieves extended producer responsibility policies.
    """
    return make_request("GET", "/metadata/extended_producer_responsibility_policy", params=kwargs)

@mcp.tool()
def get_hazardous_materials_labels(**kwargs) -> dict:
    """
    Retrieves hazardous materials labels.
    """
    return make_request("GET", "/metadata/hazardous_materials_label", params=kwargs)

@mcp.tool()
def get_listing_type_policies(**kwargs) -> dict:
    """
    Retrieves listing type policies.
    """
    return make_request("GET", "/metadata/listing_type_policy", params=kwargs)

@mcp.tool()
def get_motors_listing_policies(**kwargs) -> dict:
    """
    Retrieves motors listing policies.
    """
    return make_request("GET", "/metadata/motors_listing_policy", params=kwargs)

@mcp.tool()
def get_multi_compatibility_property_values(**kwargs) -> dict:
    """
    Retrieves multi-compatibility property values.
    """
    return make_request("GET", "/metadata/multi_compatibility_property_value", params=kwargs)

@mcp.tool()
def get_product_compatibilities(**kwargs) -> dict:
    """
    Retrieves product compatibilities.
    """
    return make_request("GET", "/metadata/product_compatibility", params=kwargs)

# ============================================================================
# NEGOTIATION API
# ============================================================================

@mcp.tool()
def find_eligible_items(filter: str = None, limit: int = 10, offset: int = 0) -> dict:
    """
    Finds eligible items for negotiation.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/negotiation/eligible_item", params=params)

@mcp.tool()
def send_offer_to_interested_buyers(item_id: str, offer_details: dict) -> dict:
    """
    Sends an offer to interested buyers.
    """
    data = {"itemId": item_id, **offer_details}
    return make_request("POST", "/negotiation/eligible_item/send_offer", data=data)

# ============================================================================
# RECOMMENDATION API
# ============================================================================

@mcp.tool()
def find_listing_recommendations(filter: str = None, limit: int = 10, offset: int = 0) -> dict:
    """
    Finds listing recommendations.
    """
    params = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/recommendation/listing", params=params)

# Run the server
if __name__ == "__main__":
    mcp.run()
