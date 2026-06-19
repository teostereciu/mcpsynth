#!/usr/bin/env python3
"""
eBay Sell API MCP Server

This server provides tools for interacting with the eBay Sell API,
including inventory management, order fulfillment, account policies,
marketing campaigns, and financial operations.
"""

import os
import json
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("ebay-sell-api")

# ============================================================================
# Authentication & Configuration
# ============================================================================

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
_access_token_cache = {"token": None, "expires_at": 0}


def get_access_token() -> str:
    """Get a valid OAuth 2.0 access token using the refresh token."""
    import time

    # Return cached token if still valid
    if _access_token_cache["token"] and time.time() < _access_token_cache["expires_at"]:
        return _access_token_cache["token"]

    # Request new token
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
        access_token = token_data.get("access_token")
        expires_in = token_data.get("expires_in", 3600)

        # Cache the token
        _access_token_cache["token"] = access_token
        _access_token_cache["expires_at"] = time.time() + expires_in - 60

        return access_token
    except Exception as e:
        return f"Error getting access token: {str(e)}"


def make_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to the eBay API."""
    try:
        access_token = get_access_token()
        if isinstance(access_token, str) and access_token.startswith("Error"):
            return {"error": access_token}

        url = f"{BASE_URL}{path}"

        # Build headers
        request_headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if headers:
            request_headers.update(headers)

        # Make request
        if method.upper() == "GET":
            response = requests.get(url, params=params, headers=request_headers, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(
                url, params=params, json=json_body, headers=request_headers, timeout=30
            )
        elif method.upper() == "PUT":
            response = requests.put(
                url, params=params, json=json_body, headers=request_headers, timeout=30
            )
        elif method.upper() == "DELETE":
            response = requests.delete(url, params=params, headers=request_headers, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        # Handle response
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

    except requests.exceptions.Timeout:
        return {"error": "Request timeout"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# ============================================================================
# Inventory API Tools
# ============================================================================

@mcp.tool()
def create_offer(
    seller_sku: str,
    marketplace_id: str,
    format: str,
    available_quantity: Optional[int] = None,
    price: Optional[float] = None,
    currency_code: Optional[str] = None,
    listing_category: Optional[str] = None,
    fulfillment_policy_id: Optional[str] = None,
    payment_policy_id: Optional[str] = None,
    return_policy_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Create an offer for a specific inventory item."""
    body = {
        "seller_sku": seller_sku,
        "marketplaceId": marketplace_id,
        "format": format,
    }
    if available_quantity is not None:
        body["available_quantity"] = available_quantity
    if price is not None:
        body["price"] = {"value": str(price), "currency": currency_code or "USD"}
    if listing_category:
        body["listing_category"] = listing_category
    if fulfillment_policy_id:
        body["fulfillmentPolicyId"] = fulfillment_policy_id
    if payment_policy_id:
        body["paymentPolicyId"] = payment_policy_id
    if return_policy_id:
        body["returnPolicyId"] = return_policy_id

    return make_request("POST", "/sell/inventory/v1/offer", json_body=body)


@mcp.tool()
def get_offer(offer_id: str) -> Dict[str, Any]:
    """Retrieve a specific offer by ID."""
    return make_request("GET", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def get_offers(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    format: Optional[str] = None,
) -> Dict[str, Any]:
    """Retrieve all offers for the authenticated seller."""
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    if format:
        params["format"] = format

    return make_request("GET", "/sell/inventory/v1/offer", params=params)


@mcp.tool()
def update_offer(
    offer_id: str,
    available_quantity: Optional[int] = None,
    price: Optional[float] = None,
    currency_code: Optional[str] = None,
    listing_category: Optional[str] = None,
) -> Dict[str, Any]:
    """Update an existing offer."""
    body = {}
    if available_quantity is not None:
        body["available_quantity"] = available_quantity
    if price is not None:
        body["price"] = {"value": str(price), "currency": currency_code or "USD"}
    if listing_category:
        body["listing_category"] = listing_category

    return make_request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json_body=body)


@mcp.tool()
def delete_offer(offer_id: str) -> Dict[str, Any]:
    """Delete an offer."""
    return make_request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def publish_offer(offer_id: str) -> Dict[str, Any]:
    """Publish an offer to create an active listing."""
    return make_request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


@mcp.tool()
def withdraw_offer(offer_id: str) -> Dict[str, Any]:
    """Withdraw an active offer/listing."""
    return make_request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


@mcp.tool()
def create_inventory_item(
    sku: str,
    product_type: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    condition: Optional[str] = None,
    brand: Optional[str] = None,
    mpn: Optional[str] = None,
) -> Dict[str, Any]:
    """Create or replace an inventory item."""
    body = {}
    if product_type:
        body["product"] = {"type": product_type}
    if title:
        body["title"] = title
    if description:
        body["description"] = description
    if condition:
        body["condition"] = condition
    if brand:
        body["brand"] = brand
    if mpn:
        body["mpn"] = mpn

    return make_request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json_body=body)


@mcp.tool()
def get_inventory_item(sku: str) -> Dict[str, Any]:
    """Retrieve an inventory item by SKU."""
    return make_request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def get_inventory_items(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve all inventory items for the seller."""
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/inventory/v1/inventory_item", params=params)


@mcp.tool()
def delete_inventory_item(sku: str) -> Dict[str, Any]:
    """Delete an inventory item."""
    return make_request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def create_inventory_location(
    location_name: str,
    merchant_location_status: str,
    address: Dict[str, str],
    phone: Optional[str] = None,
) -> Dict[str, Any]:
    """Create an inventory location."""
    body = {
        "merchantLocationStatus": merchant_location_status,
        "name": location_name,
        "address": address,
    }
    if phone:
        body["phone"] = phone

    return make_request("POST", "/sell/inventory/v1/location", json_body=body)


@mcp.tool()
def get_inventory_location(location_id: str) -> Dict[str, Any]:
    """Retrieve an inventory location by ID."""
    return make_request("GET", f"/sell/inventory/v1/location/{location_id}")


@mcp.tool()
def get_inventory_locations() -> Dict[str, Any]:
    """Retrieve all inventory locations for the seller."""
    return make_request("GET", "/sell/inventory/v1/location")


@mcp.tool()
def update_inventory_location(
    location_id: str,
    merchant_location_status: Optional[str] = None,
    phone: Optional[str] = None,
) -> Dict[str, Any]:
    """Update an inventory location."""
    body = {}
    if merchant_location_status:
        body["merchantLocationStatus"] = merchant_location_status
    if phone:
        body["phone"] = phone

    return make_request("PUT", f"/sell/inventory/v1/location/{location_id}", json_body=body)


@mcp.tool()
def delete_inventory_location(location_id: str) -> Dict[str, Any]:
    """Delete an inventory location."""
    return make_request("DELETE", f"/sell/inventory/v1/location/{location_id}")


@mcp.tool()
def enable_inventory_location(location_id: str) -> Dict[str, Any]:
    """Enable an inventory location."""
    return make_request("POST", f"/sell/inventory/v1/location/{location_id}/enable")


@mcp.tool()
def disable_inventory_location(location_id: str) -> Dict[str, Any]:
    """Disable an inventory location."""
    return make_request("POST", f"/sell/inventory/v1/location/{location_id}/disable")


@mcp.tool()
def get_listing_fees(offers: list) -> Dict[str, Any]:
    """Get estimated listing fees for offers."""
    body = {"offers": offers}
    return make_request("POST", "/sell/inventory/v1/offer/get_listing_fees", json_body=body)


@mcp.tool()
def bulk_create_offer(offers: list) -> Dict[str, Any]:
    """Create multiple offers (up to 25) at once."""
    body = {"requests": offers}
    return make_request("POST", "/sell/inventory/v1/bulk_create_offer", json_body=body)


@mcp.tool()
def bulk_publish_offer(offers: list) -> Dict[str, Any]:
    """Publish multiple offers (up to 25) at once."""
    body = {"requests": offers}
    return make_request("POST", "/sell/inventory/v1/bulk_publish_offer", json_body=body)


@mcp.tool()
def bulk_update_price_quantity(offers: list) -> Dict[str, Any]:
    """Update price and quantity for multiple offers."""
    body = {"requests": offers}
    return make_request("POST", "/sell/inventory/v1/bulk_update_price_quantity", json_body=body)


@mcp.tool()
def create_inventory_item_group(
    inventory_item_group_key: str,
    variants: list,
    title: Optional[str] = None,
) -> Dict[str, Any]:
    """Create an inventory item group for multi-variation listings."""
    body = {
        "inventoryItemGroupKey": inventory_item_group_key,
        "variantSKUs": variants,
    }
    if title:
        body["title"] = title

    return make_request(
        "PUT", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}", json_body=body
    )


@mcp.tool()
def get_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    """Retrieve an inventory item group."""
    return make_request("GET", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


@mcp.tool()
def delete_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    """Delete an inventory item group."""
    return make_request(
        "DELETE", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}"
    )


@mcp.tool()
def publish_offer_by_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    """Publish all offers in an inventory item group."""
    body = {"inventoryItemGroupKey": inventory_item_group_key}
    return make_request(
        "POST", "/sell/inventory/v1/offer/publish_by_inventory_item_group", json_body=body
    )


@mcp.tool()
def withdraw_offer_by_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    """Withdraw all offers in an inventory item group."""
    body = {"inventoryItemGroupKey": inventory_item_group_key}
    return make_request(
        "POST", "/sell/inventory/v1/offer/withdraw_by_inventory_item_group", json_body=body
    )


@mcp.tool()
def create_product_compatibility(
    seller_sku: str,
    compatibility_properties: list,
) -> Dict[str, Any]:
    """Create product compatibility information for an inventory item."""
    body = {"compatibilityProperties": compatibility_properties}
    return make_request(
        "PUT", f"/sell/inventory/v1/inventory_item/{seller_sku}/product_compatibility", json_body=body
    )


@mcp.tool()
def get_product_compatibility(seller_sku: str) -> Dict[str, Any]:
    """Retrieve product compatibility information."""
    return make_request("GET", f"/sell/inventory/v1/inventory_item/{seller_sku}/product_compatibility")


@mcp.tool()
def delete_product_compatibility(seller_sku: str) -> Dict[str, Any]:
    """Delete product compatibility information."""
    return make_request(
        "DELETE", f"/sell/inventory/v1/inventory_item/{seller_sku}/product_compatibility"
    )


@mcp.tool()
def create_sku_location_mapping(
    listing_id: str,
    seller_sku: str,
    location_mappings: list,
) -> Dict[str, Any]:
    """Create SKU to location mappings for a listing."""
    body = {"locationMappings": location_mappings}
    return make_request(
        "PUT",
        f"/sell/inventory/v1/listing/{listing_id}/seller_sku/{seller_sku}/locations",
        json_body=body,
    )


@mcp.tool()
def get_sku_location_mapping(listing_id: str, seller_sku: str) -> Dict[str, Any]:
    """Retrieve SKU to location mappings."""
    return make_request(
        "GET", f"/sell/inventory/v1/listing/{listing_id}/seller_sku/{seller_sku}/locations"
    )


@mcp.tool()
def delete_sku_location_mapping(listing_id: str, seller_sku: str) -> Dict[str, Any]:
    """Delete SKU to location mappings."""
    return make_request(
        "DELETE", f"/sell/inventory/v1/listing/{listing_id}/seller_sku/{seller_sku}/locations"
    )


# ============================================================================
# Fulfillment API Tools
# ============================================================================

@mcp.tool()
def get_order(order_id: str, field_groups: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve order details by order ID."""
    params = {}
    if field_groups:
        params["fieldGroups"] = field_groups

    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}", params=params)


@mcp.tool()
def get_orders(
    order_creation_date_range_from: Optional[str] = None,
    order_creation_date_range_to: Optional[str] = None,
    order_status: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve orders for the seller."""
    params = {}
    if order_creation_date_range_from:
        params["order_creation_date_range_from"] = order_creation_date_range_from
    if order_creation_date_range_to:
        params["order_creation_date_range_to"] = order_creation_date_range_to
    if order_status:
        params["order_status"] = order_status
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/fulfillment/v1/order", params=params)


@mcp.tool()
def create_shipping_fulfillment(
    order_id: str,
    line_items: list,
    carrier_code: Optional[str] = None,
    tracking_number: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a shipping fulfillment for an order."""
    body = {"lineItems": line_items}
    if carrier_code:
        body["shippingCarrierCode"] = carrier_code
    if tracking_number:
        body["trackingNumber"] = tracking_number

    return make_request(
        "POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json_body=body
    )


@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    """Retrieve a shipping fulfillment."""
    return make_request(
        "GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}"
    )


@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    """Retrieve all shipping fulfillments for an order."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


@mcp.tool()
def issue_refund(
    order_id: str,
    line_items: Optional[list] = None,
    refund_reason_code: Optional[str] = None,
    comment: Optional[str] = None,
) -> Dict[str, Any]:
    """Issue a refund for an order or line items."""
    body = {}
    if line_items:
        body["lineItems"] = line_items
    if refund_reason_code:
        body["refundReasonCode"] = refund_reason_code
    if comment:
        body["comment"] = comment

    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/issue_refund", json_body=body)


@mcp.tool()
def get_payment_dispute(dispute_id: str) -> Dict[str, Any]:
    """Retrieve a payment dispute."""
    return make_request("GET", f"/sell/fulfillment/v1/payment_dispute/{dispute_id}")


@mcp.tool()
def get_payment_dispute_summaries(
    order_ids: Optional[list] = None,
    dispute_status: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve payment dispute summaries."""
    params = {}
    if order_ids:
        params["order_ids"] = ",".join(order_ids)
    if dispute_status:
        params["dispute_status"] = dispute_status
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/fulfillment/v1/payment_dispute_summary", params=params)


@mcp.tool()
def accept_payment_dispute(dispute_id: str, note: Optional[str] = None) -> Dict[str, Any]:
    """Accept a payment dispute."""
    body = {}
    if note:
        body["note"] = note

    return make_request(
        "POST", f"/sell/fulfillment/v1/payment_dispute/{dispute_id}/accept", json_body=body
    )


@mcp.tool()
def contest_payment_dispute(dispute_id: str, note: Optional[str] = None) -> Dict[str, Any]:
    """Contest a payment dispute."""
    body = {}
    if note:
        body["note"] = note

    return make_request(
        "POST", f"/sell/fulfillment/v1/payment_dispute/{dispute_id}/contest", json_body=body
    )


@mcp.tool()
def add_evidence(
    dispute_id: str,
    evidence_type: str,
    evidence_documents: Optional[list] = None,
) -> Dict[str, Any]:
    """Add evidence to a payment dispute."""
    body = {"evidenceType": evidence_type}
    if evidence_documents:
        body["evidenceDocuments"] = evidence_documents

    return make_request(
        "POST", f"/sell/fulfillment/v1/payment_dispute/{dispute_id}/add_evidence", json_body=body
    )


@mcp.tool()
def get_activities(dispute_id: str) -> Dict[str, Any]:
    """Get activities for a payment dispute."""
    return make_request("GET", f"/sell/fulfillment/v1/payment_dispute/{dispute_id}/activity")


@mcp.tool()
def fetch_evidence_content(dispute_id: str) -> Dict[str, Any]:
    """Fetch evidence content for a payment dispute."""
    return make_request(
        "GET", f"/sell/fulfillment/v1/payment_dispute/{dispute_id}/fetch_evidence_content"
    )


# ============================================================================
# Account API Tools
# ============================================================================

@mcp.tool()
def create_fulfillment_policy(
    name: str,
    marketplace_id: str,
    fulfillment_type: str,
    shipping_options: list,
    category_types: Optional[list] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a fulfillment policy."""
    body = {
        "name": name,
        "marketplaceId": marketplace_id,
        "fulfillmentType": fulfillment_type,
        "shippingOptions": shipping_options,
    }
    if category_types:
        body["categoryTypes"] = category_types
    if description:
        body["description"] = description

    return make_request("POST", "/sell/account/v1/fulfillment_policy", json_body=body)


@mcp.tool()
def get_fulfillment_policy(policy_id: str) -> Dict[str, Any]:
    """Retrieve a fulfillment policy."""
    return make_request("GET", f"/sell/account/v1/fulfillment_policy/{policy_id}")


@mcp.tool()
def get_fulfillment_policies(marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve all fulfillment policies."""
    params = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id

    return make_request("GET", "/sell/account/v1/fulfillment_policy", params=params)


@mcp.tool()
def get_fulfillment_policy_by_name(
    policy_name: str, marketplace_id: Optional[str] = None
) -> Dict[str, Any]:
    """Retrieve a fulfillment policy by name."""
    params = {"name": policy_name}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id

    return make_request("GET", "/sell/account/v1/fulfillment_policy/get_by_policy_name", params=params)


@mcp.tool()
def update_fulfillment_policy(
    policy_id: str,
    name: Optional[str] = None,
    shipping_options: Optional[list] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a fulfillment policy."""
    body = {}
    if name:
        body["name"] = name
    if shipping_options:
        body["shippingOptions"] = shipping_options
    if description:
        body["description"] = description

    return make_request("PUT", f"/sell/account/v1/fulfillment_policy/{policy_id}", json_body=body)


@mcp.tool()
def delete_fulfillment_policy(policy_id: str) -> Dict[str, Any]:
    """Delete a fulfillment policy."""
    return make_request("DELETE", f"/sell/account/v1/fulfillment_policy/{policy_id}")


@mcp.tool()
def create_payment_policy(
    name: str,
    marketplace_id: str,
    payment_methods: list,
    category_types: Optional[list] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a payment policy."""
    body = {
        "name": name,
        "marketplaceId": marketplace_id,
        "paymentMethods": payment_methods,
    }
    if category_types:
        body["categoryTypes"] = category_types
    if description:
        body["description"] = description

    return make_request("POST", "/sell/account/v1/payment_policy", json_body=body)


@mcp.tool()
def get_payment_policy(policy_id: str) -> Dict[str, Any]:
    """Retrieve a payment policy."""
    return make_request("GET", f"/sell/account/v1/payment_policy/{policy_id}")


@mcp.tool()
def get_payment_policies(marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve all payment policies."""
    params = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id

    return make_request("GET", "/sell/account/v1/payment_policy", params=params)


@mcp.tool()
def get_payment_policy_by_name(
    policy_name: str, marketplace_id: Optional[str] = None
) -> Dict[str, Any]:
    """Retrieve a payment policy by name."""
    params = {"name": policy_name}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id

    return make_request("GET", "/sell/account/v1/payment_policy/get_by_policy_name", params=params)


@mcp.tool()
def update_payment_policy(
    policy_id: str,
    name: Optional[str] = None,
    payment_methods: Optional[list] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a payment policy."""
    body = {}
    if name:
        body["name"] = name
    if payment_methods:
        body["paymentMethods"] = payment_methods
    if description:
        body["description"] = description

    return make_request("PUT", f"/sell/account/v1/payment_policy/{policy_id}", json_body=body)


@mcp.tool()
def delete_payment_policy(policy_id: str) -> Dict[str, Any]:
    """Delete a payment policy."""
    return make_request("DELETE", f"/sell/account/v1/payment_policy/{policy_id}")


@mcp.tool()
def create_return_policy(
    name: str,
    marketplace_id: str,
    returns_accepted: bool,
    return_period: Optional[Dict[str, Any]] = None,
    category_types: Optional[list] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a return policy."""
    body = {
        "name": name,
        "marketplaceId": marketplace_id,
        "returnsAccepted": returns_accepted,
    }
    if return_period:
        body["returnPeriod"] = return_period
    if category_types:
        body["categoryTypes"] = category_types
    if description:
        body["description"] = description

    return make_request("POST", "/sell/account/v1/return_policy", json_body=body)


@mcp.tool()
def get_return_policy(policy_id: str) -> Dict[str, Any]:
    """Retrieve a return policy."""
    return make_request("GET", f"/sell/account/v1/return_policy/{policy_id}")


@mcp.tool()
def get_return_policies(marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve all return policies."""
    params = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id

    return make_request("GET", "/sell/account/v1/return_policy", params=params)


@mcp.tool()
def get_return_policy_by_name(
    policy_name: str, marketplace_id: Optional[str] = None
) -> Dict[str, Any]:
    """Retrieve a return policy by name."""
    params = {"name": policy_name}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id

    return make_request("GET", "/sell/account/v1/return_policy/get_by_policy_name", params=params)


@mcp.tool()
def update_return_policy(
    policy_id: str,
    name: Optional[str] = None,
    returns_accepted: Optional[bool] = None,
    return_period: Optional[Dict[str, Any]] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a return policy."""
    body = {}
    if name:
        body["name"] = name
    if returns_accepted is not None:
        body["returnsAccepted"] = returns_accepted
    if return_period:
        body["returnPeriod"] = return_period
    if description:
        body["description"] = description

    return make_request("PUT", f"/sell/account/v1/return_policy/{policy_id}", json_body=body)


@mcp.tool()
def delete_return_policy(policy_id: str) -> Dict[str, Any]:
    """Delete a return policy."""
    return make_request("DELETE", f"/sell/account/v1/return_policy/{policy_id}")


@mcp.tool()
def get_privileges() -> Dict[str, Any]:
    """Retrieve seller privileges and restrictions."""
    return make_request("GET", "/sell/account/v1/privilege")


@mcp.tool()
def get_opted_in_programs() -> Dict[str, Any]:
    """Retrieve programs the seller is opted into."""
    return make_request("GET", "/sell/account/v1/program/get_opted_in_programs")


@mcp.tool()
def opt_in_to_program(program_name: str) -> Dict[str, Any]:
    """Opt into a seller program."""
    body = {"programName": program_name}
    return make_request("POST", "/sell/account/v1/program/opt_in", json_body=body)


@mcp.tool()
def opt_out_of_program(program_name: str) -> Dict[str, Any]:
    """Opt out of a seller program."""
    body = {"programName": program_name}
    return make_request("POST", "/sell/account/v1/program/opt_out", json_body=body)


@mcp.tool()
def create_custom_policy(
    policy_name: str,
    policy_type: str,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a custom policy."""
    body = {
        "name": policy_name,
        "policyType": policy_type,
    }
    if description:
        body["description"] = description

    return make_request("POST", "/sell/account/v1/custom_policy/", json_body=body)


@mcp.tool()
def get_custom_policy(policy_id: str) -> Dict[str, Any]:
    """Retrieve a custom policy."""
    return make_request("GET", f"/sell/account/v1/custom_policy/{policy_id}")


@mcp.tool()
def get_custom_policies() -> Dict[str, Any]:
    """Retrieve all custom policies."""
    return make_request("GET", "/sell/account/v1/custom_policy/")


@mcp.tool()
def update_custom_policy(
    policy_id: str,
    policy_name: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a custom policy."""
    body = {}
    if policy_name:
        body["name"] = policy_name
    if description:
        body["description"] = description

    return make_request("PUT", f"/sell/account/v1/custom_policy/{policy_id}", json_body=body)


@mcp.tool()
def delete_custom_policy(policy_id: str) -> Dict[str, Any]:
    """Delete a custom policy."""
    return make_request("DELETE", f"/sell/account/v1/custom_policy/{policy_id}")


@mcp.tool()
def create_or_replace_sales_tax(
    country_code: str,
    jurisdiction_id: str,
    sales_tax_percentage: float,
) -> Dict[str, Any]:
    """Create or replace sales tax information."""
    body = {"salesTaxPercentage": sales_tax_percentage}

    return make_request(
        "PUT",
        f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}",
        json_body=body,
    )


@mcp.tool()
def get_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    """Retrieve sales tax information."""
    return make_request("GET", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


@mcp.tool()
def get_sales_taxes() -> Dict[str, Any]:
    """Retrieve all sales tax information."""
    return make_request("GET", "/sell/account/v1/sales_tax")


@mcp.tool()
def delete_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    """Delete sales tax information."""
    return make_request("DELETE", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


@mcp.tool()
def get_rate_tables() -> Dict[str, Any]:
    """Retrieve seller rate tables."""
    return make_request("GET", "/sell/account/v1/rate_table")


@mcp.tool()
def get_subscription() -> Dict[str, Any]:
    """Retrieve seller subscription information."""
    return make_request("GET", "/sell/account/v1/subscription")


@mcp.tool()
def get_payments_program(market_id: str, payments_program_type: str) -> Dict[str, Any]:
    """Get payments program information."""
    return make_request(
        "GET", f"/sell/account/v1/payments_program/{market_id}/{payments_program_type}"
    )


@mcp.tool()
def get_payments_program_onboarding(
    market_id: str, payments_program_type: str
) -> Dict[str, Any]:
    """Get payments program onboarding information."""
    return make_request(
        "GET",
        f"/sell/account/v1/payments_program/{market_id}/{payments_program_type}/onboarding",
    )


# ============================================================================
# Marketing API Tools
# ============================================================================

@mcp.tool()
def create_campaign(
    campaign_name: str,
    marketplace_id: str,
    budget_allocation: float,
    campaign_status: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> Dict[str, Any]:
    """Create an advertising campaign."""
    body = {
        "campaignName": campaign_name,
        "marketplaceId": marketplace_id,
        "budgetAllocation": budget_allocation,
    }
    if campaign_status:
        body["campaignStatus"] = campaign_status
    if start_date:
        body["startDate"] = start_date
    if end_date:
        body["endDate"] = end_date

    return make_request("POST", "/sell/marketing/v1/ad_campaign", json_body=body)


@mcp.tool()
def get_campaign(campaign_id: str) -> Dict[str, Any]:
    """Retrieve a campaign by ID."""
    return make_request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def get_campaigns(
    campaign_status: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve all campaigns."""
    params = {}
    if campaign_status:
        params["campaign_status"] = campaign_status
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/marketing/v1/ad_campaign", params=params)


@mcp.tool()
def update_campaign(
    campaign_id: str,
    campaign_name: Optional[str] = None,
    budget_allocation: Optional[float] = None,
    campaign_status: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a campaign."""
    body = {}
    if campaign_name:
        body["campaignName"] = campaign_name
    if budget_allocation:
        body["budgetAllocation"] = budget_allocation
    if campaign_status:
        body["campaignStatus"] = campaign_status

    return make_request("PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}", json_body=body)


@mcp.tool()
def delete_campaign(campaign_id: str) -> Dict[str, Any]:
    """Delete a campaign."""
    return make_request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def create_ad(
    campaign_id: str,
    listing_id: str,
    bid_amount: float,
) -> Dict[str, Any]:
    """Create an ad for a listing."""
    body = {
        "listingId": listing_id,
        "bidAmount": bid_amount,
    }

    return make_request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", json_body=body)


@mcp.tool()
def get_ad(campaign_id: str, ad_id: str) -> Dict[str, Any]:
    """Retrieve an ad."""
    return make_request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


@mcp.tool()
def get_ads(
    campaign_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve ads for a campaign."""
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", params=params)


@mcp.tool()
def update_ad_bid(
    campaign_id: str,
    ad_id: str,
    bid_amount: float,
) -> Dict[str, Any]:
    """Update an ad's bid amount."""
    body = {"bidAmount": bid_amount}

    return make_request(
        "PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}", json_body=body
    )


@mcp.tool()
def delete_ad(campaign_id: str, ad_id: str) -> Dict[str, Any]:
    """Delete an ad."""
    return make_request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


@mcp.tool()
def clone_campaign(
    campaign_id: str,
    campaign_name: str,
) -> Dict[str, Any]:
    """Clone an existing campaign."""
    body = {"campaignName": campaign_name}

    return make_request(
        "POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/clone", json_body=body
    )


# ============================================================================
# Finances API Tools
# ============================================================================

@mcp.tool()
def get_payout_summary() -> Dict[str, Any]:
    """Retrieve payout summary for the seller."""
    return make_request("GET", "/sell/finances/v1/payout_summary")


@mcp.tool()
def get_payouts(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve all payouts."""
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/finances/v1/payout", params=params)


@mcp.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """Retrieve a specific payout."""
    return make_request("GET", f"/sell/finances/v1/payout/{payout_id}")


@mcp.tool()
def get_transactions(
    transaction_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve financial transactions."""
    params = {}
    if transaction_type:
        params["transaction_type"] = transaction_type
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/finances/v1/transaction", params=params)


@mcp.tool()
def get_transaction_summary() -> Dict[str, Any]:
    """Retrieve a summary of financial transactions."""
    return make_request("GET", "/sell/finances/v1/transaction_summary")


@mcp.tool()
def get_seller_funds_summary() -> Dict[str, Any]:
    """Retrieve seller funds summary."""
    return make_request("GET", "/sell/finances/v1/seller_funds_summary")


# ============================================================================
# Feed API Tools
# ============================================================================

@mcp.tool()
def create_inventory_task(
    feed_type: str,
    file_name: str,
) -> Dict[str, Any]:
    """Create an inventory feed task."""
    body = {
        "feedType": feed_type,
        "fileName": file_name,
    }

    return make_request("POST", "/sell/feed/v1/inventory_task", json_body=body)


@mcp.tool()
def get_inventory_task(task_id: str) -> Dict[str, Any]:
    """Retrieve an inventory task."""
    return make_request("GET", f"/sell/feed/v1/inventory_task/{task_id}")


@mcp.tool()
def get_inventory_tasks(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve all inventory tasks."""
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/feed/v1/inventory_task", params=params)


@mcp.tool()
def create_order_task(
    feed_type: str,
    file_name: str,
) -> Dict[str, Any]:
    """Create an order feed task."""
    body = {
        "feedType": feed_type,
        "fileName": file_name,
    }

    return make_request("POST", "/sell/feed/v1/order_task", json_body=body)


@mcp.tool()
def get_order_task(task_id: str) -> Dict[str, Any]:
    """Retrieve an order task."""
    return make_request("GET", f"/sell/feed/v1/order_task/{task_id}")


@mcp.tool()
def get_order_tasks(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve all order tasks."""
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/feed/v1/order_task", params=params)


@mcp.tool()
def get_task(task_id: str) -> Dict[str, Any]:
    """Retrieve a task."""
    return make_request("GET", f"/sell/feed/v1/task/{task_id}")


@mcp.tool()
def get_tasks(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve all tasks."""
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/feed/v1/task", params=params)


@mcp.tool()
def create_schedule(
    schedule_name: str,
    feed_type: str,
    schedule_template_id: str,
) -> Dict[str, Any]:
    """Create a feed schedule."""
    body = {
        "scheduleName": schedule_name,
        "feedType": feed_type,
        "scheduleTemplateId": schedule_template_id,
    }

    return make_request("POST", "/sell/feed/v1/schedule", json_body=body)


@mcp.tool()
def get_schedule(schedule_id: str) -> Dict[str, Any]:
    """Retrieve a feed schedule."""
    return make_request("GET", f"/sell/feed/v1/schedule/{schedule_id}")


@mcp.tool()
def get_schedules(
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve all feed schedules."""
    params = {}
    if feed_type:
        params["feed_type"] = feed_type
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/feed/v1/schedule", params=params)


@mcp.tool()
def update_schedule(
    schedule_id: str,
    schedule_name: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a feed schedule."""
    body = {}
    if schedule_name:
        body["scheduleName"] = schedule_name

    return make_request("PUT", f"/sell/feed/v1/schedule/{schedule_id}", json_body=body)


@mcp.tool()
def delete_schedule(schedule_id: str) -> Dict[str, Any]:
    """Delete a feed schedule."""
    return make_request("DELETE", f"/sell/feed/v1/schedule/{schedule_id}")


@mcp.tool()
def get_schedule_templates() -> Dict[str, Any]:
    """Retrieve available feed schedule templates."""
    return make_request("GET", "/sell/feed/v1/schedule_template")


@mcp.tool()
def get_schedule_template(schedule_template_id: str) -> Dict[str, Any]:
    """Retrieve a specific feed schedule template."""
    return make_request("GET", f"/sell/feed/v1/schedule_template/{schedule_template_id}")


# ============================================================================
# Metadata API Tools
# ============================================================================

@mcp.tool()
def get_category_policies(
    marketplace_id: str,
    category_id: str,
) -> Dict[str, Any]:
    """Get category policies."""
    params = {
        "marketplace_id": marketplace_id,
        "category_id": category_id,
    }

    return make_request("GET", "/sell/metadata/v1/category_policy", params=params)


@mcp.tool()
def get_currencies(marketplace_id: str) -> Dict[str, Any]:
    """Get supported currencies for a marketplace."""
    params = {"marketplace_id": marketplace_id}

    return make_request("GET", "/sell/metadata/v1/currency", params=params)


@mcp.tool()
def get_item_condition_policies(marketplace_id: str) -> Dict[str, Any]:
    """Get item condition policies for a marketplace."""
    return make_request(
        "GET", f"/sell/metadata/v1/marketplace/{marketplace_id}/get_item_condition_policies"
    )


@mcp.tool()
def get_listing_type_policies(marketplace_id: str) -> Dict[str, Any]:
    """Get listing type policies for a marketplace."""
    return make_request(
        "GET", f"/sell/metadata/v1/marketplace/{marketplace_id}/get_listing_type_policies"
    )


@mcp.tool()
def get_listing_structure_policies(marketplace_id: str) -> Dict[str, Any]:
    """Get listing structure policies for a marketplace."""
    return make_request(
        "GET", f"/sell/metadata/v1/marketplace/{marketplace_id}/get_listing_structure_policies"
    )


@mcp.tool()
def get_hazardous_materials_labels(marketplace_id: str) -> Dict[str, Any]:
    """Get hazardous materials labels for a marketplace."""
    return make_request(
        "GET", f"/sell/metadata/v1/marketplace/{marketplace_id}/get_hazardous_materials_labels"
    )


@mcp.tool()
def get_automotive_parts_compatibility_policies(marketplace_id: str) -> Dict[str, Any]:
    """Get automotive parts compatibility policies."""
    return make_request(
        "GET",
        f"/sell/metadata/v1/marketplace/{marketplace_id}/get_automotive_parts_compatibility_policies",
    )


# ============================================================================
# Compliance API Tools
# ============================================================================

@mcp.tool()
def get_listing_violations_summary() -> Dict[str, Any]:
    """Get a summary of listing violations."""
    return make_request("GET", "/sell/compliance/v1/listing_violations_summary")


@mcp.tool()
def get_listing_violations(
    compliance_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Get listing violations."""
    params = {}
    if compliance_type:
        params["compliance_type"] = compliance_type
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    return make_request("GET", "/sell/compliance/v1/listing_violations", params=params)


# ============================================================================
# Analytics API Tools
# ============================================================================

@mcp.tool()
def get_traffic_report(
    marketplace_id: str,
    date: str,
) -> Dict[str, Any]:
    """Get traffic report for a date."""
    params = {
        "marketplace_id": marketplace_id,
        "date": date,
    }

    return make_request("GET", "/sell/analytics/v1/traffic_report", params=params)


@mcp.tool()
def get_seller_standards_profile() -> Dict[str, Any]:
    """Get seller standards profile."""
    return make_request("GET", "/sell/analytics/v1/seller_standards_profile")


@mcp.tool()
def find_seller_standards_profiles() -> Dict[str, Any]:
    """Find seller standards profiles."""
    return make_request("GET", "/sell/analytics/v1/seller_standards_profile")


@mcp.tool()
def get_customer_service_metric(
    customer_service_metric_type: str,
    evaluation_type: str,
) -> Dict[str, Any]:
    """Get customer service metrics."""
    return make_request(
        "GET",
        f"/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_type}",
    )


# ============================================================================
# Recommendation API Tools
# ============================================================================

@mcp.tool()
def find_listing_recommendations(
    marketplace_id: str,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """Find listing recommendations."""
    params = {"marketplace_id": marketplace_id}
    if limit:
        params["limit"] = limit

    return make_request("GET", "/sell/recommendation/v1/listing_recommendation", params=params)


# ============================================================================
# Negotiation API Tools
# ============================================================================

@mcp.tool()
def find_eligible_items(
    marketplace_id: str,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """Find items eligible for best offer."""
    params = {"marketplace_id": marketplace_id}
    if limit:
        params["limit"] = limit

    return make_request("GET", "/sell/negotiation/v1/find_eligible_items", params=params)


@mcp.tool()
def send_offer_to_interested_buyers(
    item_id: str,
    offer_price: float,
    currency_code: str,
    message: Optional[str] = None,
) -> Dict[str, Any]:
    """Send an offer to interested buyers."""
    body = {
        "itemId": item_id,
        "offerPrice": offer_price,
        "currencyCode": currency_code,
    }
    if message:
        body["message"] = message

    return make_request(
        "POST", "/sell/negotiation/v1/send_offer_to_interested_buyers", json_body=body
    )


# ============================================================================
# Stores API Tools
# ============================================================================

@mcp.tool()
def get_store() -> Dict[str, Any]:
    """Get the seller's store information."""
    return make_request("GET", "/sell/stores/v1/store")


@mcp.tool()
def get_store_categories() -> Dict[str, Any]:
    """Get store categories."""
    return make_request("GET", "/sell/stores/v1/store_category")


@mcp.tool()
def add_store_category(
    category_name: str,
    parent_category_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Add a store category."""
    body = {"name": category_name}
    if parent_category_id:
        body["parentCategoryId"] = parent_category_id

    return make_request("POST", "/sell/stores/v1/store_category", json_body=body)


@mcp.tool()
def delete_store_category(category_id: str) -> Dict[str, Any]:
    """Delete a store category."""
    return make_request("DELETE", f"/sell/stores/v1/store_category/{category_id}")


@mcp.tool()
def rename_store_category(
    category_id: str,
    category_name: str,
) -> Dict[str, Any]:
    """Rename a store category."""
    body = {"name": category_name}

    return make_request(
        "PUT", f"/sell/stores/v1/store_category/{category_id}", json_body=body
    )


# ============================================================================
# Logistics API Tools
# ============================================================================

@mcp.tool()
def create_shipping_quote(
    from_address: Dict[str, str],
    to_address: Dict[str, str],
    shipping_options: list,
) -> Dict[str, Any]:
    """Create a shipping quote."""
    body = {
        "fromAddress": from_address,
        "toAddress": to_address,
        "shippingOptions": shipping_options,
    }

    return make_request("POST", "/sell/logistics/v1/shipping_quote", json_body=body)


@mcp.tool()
def get_shipping_quote(quote_id: str) -> Dict[str, Any]:
    """Get a shipping quote."""
    return make_request("GET", f"/sell/logistics/v1/shipping_quote/{quote_id}")


@mcp.tool()
def create_shipment_from_quote(
    quote_id: str,
    shipping_option_id: str,
) -> Dict[str, Any]:
    """Create a shipment from a shipping quote."""
    body = {"shippingOptionId": shipping_option_id}

    return make_request(
        "POST", f"/sell/logistics/v1/shipping_quote/{quote_id}/create_shipment", json_body=body
    )


@mcp.tool()
def get_shipment(shipment_id: str) -> Dict[str, Any]:
    """Get a shipment."""
    return make_request("GET", f"/sell/logistics/v1/shipment/{shipment_id}")


@mcp.tool()
def cancel_shipment(shipment_id: str) -> Dict[str, Any]:
    """Cancel a shipment."""
    return make_request("POST", f"/sell/logistics/v1/shipment/{shipment_id}/cancel")


@mcp.tool()
def download_label_file(shipment_id: str) -> Dict[str, Any]:
    """Download a shipping label file."""
    return make_request("GET", f"/sell/logistics/v1/shipment/{shipment_id}/download_label_file")


if __name__ == "__main__":
    mcp.run()
