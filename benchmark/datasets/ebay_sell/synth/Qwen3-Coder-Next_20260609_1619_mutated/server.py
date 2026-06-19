#!/usr/bin/env python3
"""
MCP Server for eBay Sell API
Provides comprehensive coverage of the eBay Sell API for autonomous agents.
"""

import os
import requests
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(name="ebay-sell", version="1.0.0")

# Configuration
EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_REFRESH_TOKEN = os.environ.get("EBAY_REFRESH_TOKEN")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

# OAuth token cache
_oauth_token = None
_oauth_token_expiry = 0


def get_base_url() -> str:
    """Get the appropriate base URL based on environment."""
    return BASE_URLS.get(EBAY_ENVIRONMENT.upper(), BASE_URLS["SANDBOX"])


def get_oauth_token() -> str:
    """Get or refresh OAuth token."""
    global _oauth_token, _oauth_token_expiry
    
    # Check if we have a valid token
    if _oauth_token and _oauth_token_expiry > 0:
        import time
        if _oauth_token_expiry > time.time() + 60:  # 1 minute buffer
            return _oauth_token
    
    # Refresh token
    token_url = "https://api.ebay.com/oauth2/token"
    auth = (EBAY_APP_ID, EBAY_CERT_ID)
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN,
        "scope": "https://api.ebay.com/oauth/api_scope",
    }
    
    response = requests.post(token_url, auth=auth, data=data)
    response.raise_for_status()
    
    result = response.json()
    _oauth_token = result["access_token"]
    
    # Set expiry (tokens typically last 2 hours)
    import time
    _oauth_token_expiry = time.time() + result.get("expires_in", 7200)
    
    return _oauth_token


def make_request(method: str, path: str, params: Optional[dict] = None, 
                 headers: Optional[dict] = None, data: Optional[dict] = None) -> dict:
    """Make an eBay API request."""
    base_url = get_base_url()
    url = f"{base_url}{path}"
    
    auth_token = get_oauth_token()
    
    request_headers = {
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    
    if headers:
        request_headers.update(headers)
    
    response = requests.request(
        method=method,
        url=url,
        params=params,
        headers=request_headers,
        json=data,
    )
    
    # Handle errors gracefully
    if not response.ok:
        try:
            error_data = response.json()
            error_msg = error_data.get("errors", [{}])[0].get("message", f"HTTP {response.status_code}: {response.text}")
            return {"error": error_msg}
        except:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
    
    try:
        return response.json()
    except:
        return {"raw_response": response.text}


# =============================================================================
# INVENTORY API TOOLS
# =============================================================================

@mcp.tool()
def get_inventory_items(limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves all inventory item records defined for the seller's account.
    
    Args:
        limit: Maximum number of records per page (1-200, default: 25)
        offset: Page number to retrieve (default: 0)
    
    Returns:
        Inventory items collection
    """
    return make_request("GET", "/inventory_item", params={"limit": limit, "offset": offset})


@mcp.tool()
def get_inventory_item(seller_sku: str) -> dict:
    """
    Retrieves a specific inventory item by seller SKU.
    
    Args:
        seller_sku: The seller-defined SKU value for the inventory item
    
    Returns:
        Inventory item details
    """
    return make_request("GET", f"/inventory_item/{seller_sku}")


@mcp.tool()
def create_or_replace_inventory_item(seller_sku: str, condition: str, 
                                      quantity: int, price: dict,
                                      title: str = None, description: str = None,
                                      category_ids: list = None,
                                      brand: str = None, mpn: str = None,
                                      gtin: str = None, images: list = None) -> dict:
    """
    Creates a new inventory item record or replaces an existing one.
    
    Args:
        seller_sku: Seller-defined SKU (required, path parameter)
        condition: Item condition (e.g., "NEW", "USED", "REFURBISHED")
        quantity: Available quantity
        price: Price object with value and currency
        title: Item title
        description: Item description
        category_ids: List of eBay category IDs
        brand: Brand name
        mpn: Manufacturer part number
        gtin: Global trade item number (UPC, ISBN, EAN)
        images: List of image URLs
    
    Returns:
        BaseResponse with operation status
    """
    payload = {
        "condition": condition,
        "inventoryItem": {
            "name": title,
            "description": description,
            "imageUrls": images or [],
            "product": {
                "title": title,
                "description": description,
                "brand": brand,
                "mpn": mpn,
                "gtin": gtin,
                "categoryIds": category_ids or [],
            }
        },
        "quantity": quantity,
        "price": price,
    }
    
    return make_request("PUT", f"/inventory_item/{seller_sku}", data=payload)


@mcp.tool()
def bulk_update_price_quantity(seller_sku: str, offers: list) -> dict:
    """
    Updates the price and/or quantity of offers associated with an inventory item.
    
    Args:
        seller_sku: The seller-defined SKU for the inventory item
        offers: List of offer updates with offerId, quantity, and/or price
    
    Returns:
        BulkPriceQuantityResponse with update results
    """
    payload = {
        "seller_sku": seller_sku,
        "offers": offers,
    }
    
    return make_request("POST", "/bulk_update_price_quantity", data=payload)


@mcp.tool()
def get_offers(seller_sku: str = None, limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves offers associated with a seller SKU or all offers for the seller.
    
    Args:
        seller_sku: Optional seller SKU to filter offers
        limit: Maximum number of offers per page (default: 25)
        offset: Page number to retrieve (default: 0)
    
    Returns:
        Offer collection
    """
    params = {"limit": limit, "offset": offset}
    if seller_sku:
        params["seller_sku"] = seller_sku
    
    return make_request("GET", "/offer", params=params)


@mcp.tool()
def create_offer(seller_sku: str, marketplace_id: str, format: str,
                 price: dict, quantity: int, category_id: str = None,
                 listing_description: str = None, listing_policy_id: str = None,
                 payment_policy_id: str = None, return_policy_id: str = None) -> dict:
    """
    Creates an offer for a specific inventory item.
    
    Args:
        seller_sku: Seller-defined SKU for the inventory item
        marketplace_id: eBay marketplace ID (e.g., "EBAY_US")
        format: Listing format (e.g., "FIXED_PRICE")
        price: Price object with value and currency
        quantity: Available quantity
        category_id: eBay category ID
        listing_description: Listing description
        listing_policy_id: Listing policy ID
        payment_policy_id: Payment policy ID
        return_policy_id: Return policy ID
    
    Returns:
        OfferResponse with created offer details
    """
    payload = {
        "seller_sku": seller_sku,
        "marketplaceId": marketplace_id,
        "format": format,
        "price": price,
        "quantity": quantity,
    }
    
    if category_id:
        payload["category_id"] = category_id
    if listing_description:
        payload["listing_description"] = listing_description
    if listing_policy_id:
        payload["listing_policy_id"] = listing_policy_id
    if payment_policy_id:
        payload["payment_policy_id"] = payment_policy_id
    if return_policy_id:
        payload["return_policy_id"] = return_policy_id
    
    return make_request("POST", "/offer", data=payload)


@mcp.tool()
def update_offer(offer_id: str, price: dict = None, quantity: int = None,
                 condition: str = None, category_id: str = None) -> dict:
    """
    Updates an existing offer.
    
    Args:
        offer_id: The eBay-assigned offer ID
        price: Updated price object (optional)
        quantity: Updated quantity (optional)
        condition: Updated condition (optional)
        category_id: Updated category ID (optional)
    
    Returns:
        OfferResponse with updated offer details
    """
    payload = {}
    if price is not None:
        payload["price"] = price
    if quantity is not None:
        payload["quantity"] = quantity
    if condition is not None:
        payload["condition"] = condition
    if category_id is not None:
        payload["category_id"] = category_id
    
    return make_request("PUT", f"/offer/{offer_id}", data=payload)


@mcp.tool()
def publish_offer(offer_id: str) -> dict:
    """
    Publishes (activates) a staged offer to create an eBay listing.
    
    Args:
        offer_id: The eBay-assigned offer ID
    
    Returns:
        Response with listing details
    """
    return make_request("POST", f"/offer/{offer_id}/publish")


@mcp.tool()
def withdraw_offer(offer_id: str) -> dict:
    """
    Withdraws (deactivates) a published offer from eBay.
    
    Args:
        offer_id: The eBay-assigned offer ID
    
    Returns:
        Response with withdrawal status
    """
    return make_request("POST", f"/offer/{offer_id}/withdraw")


@mcp.tool()
def get_inventory_locations(limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves all inventory locations for the seller.
    
    Args:
        limit: Maximum number of locations per page (default: 25)
        offset: Page number to retrieve (default: 0)
    
    Returns:
        Inventory location collection
    """
    return make_request("GET", "/location", params={"limit": limit, "offset": offset})


@mcp.tool()
def get_inventory_location(merchant_location_key: str) -> dict:
    """
    Retrieves a specific inventory location by merchant location key.
    
    Args:
        merchant_location_key: The merchant-defined location key
    
    Returns:
        Inventory location details
    """
    return make_request("GET", f"/location/{merchant_location_key}")


@mcp.tool()
def create_inventory_location(merchant_location_key: str, name: str,
                               address: dict = None, store_hours: dict = None) -> dict:
    """
    Creates a new inventory location.
    
    Args:
        merchant_location_key: Unique key for the location
        name: Location name
        address: Location address
        store_hours: Store operating hours
    
    Returns:
        Inventory location details
    """
    payload = {
        "merchantLocationKey": merchant_location_key,
        "name": name,
    }
    if address:
        payload["address"] = address
    if store_hours:
        payload["storeHours"] = store_hours
    
    return make_request("POST", f"/location/{merchant_location_key}", data=payload)


@mcp.tool()
def update_inventory_location(merchant_location_key: str, name: str = None,
                               address: dict = None, store_hours: dict = None) -> dict:
    """
    Updates an existing inventory location.
    
    Args:
        merchant_location_key: The merchant-defined location key
        name: Updated location name (optional)
        address: Updated address (optional)
        store_hours: Updated store hours (optional)
    
    Returns:
        Updated inventory location details
    """
    payload = {}
    if name:
        payload["name"] = name
    if address:
        payload["address"] = address
    if store_hours:
        payload["storeHours"] = store_hours
    
    return make_request("PUT", f"/location/{merchant_location_key}", data=payload)


@mcp.tool()
def disable_inventory_location(merchant_location_key: str) -> dict:
    """
    Disables an inventory location.
    
    Args:
        merchant_location_key: The merchant-defined location key
    
    Returns:
        Response with disable status
    """
    return make_request("POST", f"/location/{merchant_location_key}/disable")


@mcp.tool()
def enable_inventory_location(merchant_location_key: str) -> dict:
    """
    Enables a previously disabled inventory location.
    
    Args:
        merchant_location_key: The merchant-defined location key
    
    Returns:
        Response with enable status
    """
    return make_request("POST", f"/location/{merchant_location_key}/enable")


@mcp.tool()
def delete_inventory_location(merchant_location_key: str) -> dict:
    """
    Deletes an inventory location.
    
    Args:
        merchant_location_key: The merchant-defined location key
    
    Returns:
        Response with delete status
    """
    return make_request("DELETE", f"/location/{merchant_location_key}")


# =============================================================================
# FULFILLMENT API TOOLS
# =============================================================================

@mcp.tool()
def get_orders(filter: str = None, limit: str = "50", offset: str = "0",
               order_ids: str = None, field_groups: str = None) -> dict:
    """
    Searches for and retrieves orders based on various criteria.
    
    Args:
        filter: Filter criteria (creationdate, lastmodifieddate, orderfulfillmentstatus)
        limit: Maximum orders per page (default: 50)
        offset: Page number (default: 0)
        order_ids: Comma-separated list of specific order IDs to retrieve
        field_groups: Extra fields to include (e.g., "TAX_BREAKDOWN")
    
    Returns:
        Order search results
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    if field_groups:
        params["fieldGroups"] = field_groups
    
    return make_request("GET", "/order", params=params)


@mcp.tool()
def get_order(order_id: str, field_groups: str = None) -> dict:
    """
    Retrieves a specific order by order ID.
    
    Args:
        order_id: The eBay-assigned order ID
        field_groups: Extra fields to include (e.g., "TAX_BREAKDOWN")
    
    Returns:
        Order details
    """
    params = {}
    if field_groups:
        params["fieldGroups"] = field_groups
    
    return make_request("GET", f"/order/{order_id}", params=params)


@mcp.tool()
def create_shipping_fulfillment(order_id: str, line_items: list,
                                 shipment_date: str = None,
                                 shipping_note: str = None) -> dict:
    """
    Creates a shipping fulfillment for an order.
    
    Args:
        order_id: The eBay-assigned order ID
        line_items: List of line item IDs to fulfill
        shipment_date: Shipment date (ISO 8601 format, defaults to now)
        shipping_note: Optional shipping note
    
    Returns:
        Shipping fulfillment details
    """
    payload = {
        "lineItems": line_items,
    }
    if shipment_date:
        payload["shipmentDate"] = shipment_date
    if shipping_note:
        payload["shippingNote"] = shipping_note
    
    return make_request("POST", f"/order/{order_id}/shipping_fulfillment", data=payload)


@mcp.tool()
def get_shipping_fulfillments(order_id: str, limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves all shipping fulfillments for an order.
    
    Args:
        order_id: The eBay-assigned order ID
        limit: Maximum fulfillments per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Shipping fulfillment collection
    """
    return make_request("GET", f"/order/{order_id}/shipping_fulfillment",
                       params={"limit": limit, "offset": offset})


@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> dict:
    """
    Retrieves a specific shipping fulfillment.
    
    Args:
        order_id: The eBay-assigned order ID
        fulfillment_id: The shipping fulfillment ID
    
    Returns:
        Shipping fulfillment details
    """
    return make_request("GET", f"/order/{order_id}/shipping_fulfillment/{fulfillment_id}")


@mcp.tool()
def issue_refund(order_id: str, refund_amount: dict,
                 refund_type: str = "FULL", reason: str = None) -> dict:
    """
    Issues a refund for an order.
    
    Args:
        order_id: The eBay-assigned order ID
        refund_amount: Refund amount object with value and currency
        refund_type: Type of refund (FULL, PARTIAL, etc.)
        reason: Reason for the refund
    
    Returns:
        Refund details
    """
    payload = {
        "refundAmount": refund_amount,
        "refundType": refund_type,
    }
    if reason:
        payload["reason"] = reason
    
    return make_request("POST", f"/order/{order_id}/issue_refund", data=payload)


# =============================================================================
# ACCOUNT API TOOLS (Policies, Programs)
# =============================================================================

@mcp.tool()
def get_fulfillment_policies(market_id: str, limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves all fulfillment policies for a marketplace.
    
    Args:
        market_id: eBay marketplace ID (required)
        limit: Maximum policies per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Fulfillment policy collection
    """
    return make_request("GET", "/fulfillment_policy",
                       params={"market_id": market_id, "limit": limit, "offset": offset})


@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """
    Retrieves a specific fulfillment policy by ID.
    
    Args:
        fulfillment_policy_id: The eBay-assigned policy ID
    
    Returns:
        Fulfillment policy details
    """
    return make_request("GET", f"/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def create_fulfillment_policy(name: str, market_id: str, description: str = None,
                               handling_time: dict = None, template: dict = None) -> dict:
    """
    Creates a new fulfillment policy.
    
    Args:
        name: Policy name
        market_id: eBay marketplace ID
        description: Policy description
        handling_time: Handling time definition
        template: Shipping template definition
    
    Returns:
        Created fulfillment policy details
    """
    payload = {
        "name": name,
        "marketId": market_id,
    }
    if description:
        payload["description"] = description
    if handling_time:
        payload["handlingTime"] = handling_time
    if template:
        payload["template"] = template
    
    return make_request("POST", "/fulfillment_policy", data=payload)


@mcp.tool()
def update_fulfillment_policy(fulfillment_policy_id: str, name: str = None,
                               description: str = None, handling_time: dict = None) -> dict:
    """
    Updates an existing fulfillment policy.
    
    Args:
        fulfillment_policy_id: The eBay-assigned policy ID
        name: Updated policy name (optional)
        description: Updated description (optional)
        handling_time: Updated handling time (optional)
    
    Returns:
        Updated fulfillment policy details
    """
    payload = {}
    if name:
        payload["name"] = name
    if description:
        payload["description"] = description
    if handling_time:
        payload["handlingTime"] = handling_time
    
    return make_request("PUT", f"/fulfillment_policy/{fulfillment_policy_id}", data=payload)


@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """
    Deletes a fulfillment policy.
    
    Args:
        fulfillment_policy_id: The eBay-assigned policy ID
    
    Returns:
        Response with delete status
    """
    return make_request("DELETE", f"/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def get_payment_policies(market_id: str, limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves all payment policies for a marketplace.
    
    Args:
        market_id: eBay marketplace ID (required)
        limit: Maximum policies per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Payment policy collection
    """
    return make_request("GET", "/payment_policy",
                       params={"market_id": market_id, "limit": limit, "offset": offset})


@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> dict:
    """
    Retrieves a specific payment policy by ID.
    
    Args:
        payment_policy_id: The eBay-assigned policy ID
    
    Returns:
        Payment policy details
    """
    return make_request("GET", f"/payment_policy/{payment_policy_id}")


@mcp.tool()
def create_payment_policy(name: str, market_id: str, payment_instructions: str = None,
                          payment_methods: list = None) -> dict:
    """
    Creates a new payment policy.
    
    Args:
        name: Policy name
        market_id: eBay marketplace ID
        payment_instructions: Payment instructions for buyers
        payment_methods: List of accepted payment methods
    
    Returns:
        Created payment policy details
    """
    payload = {
        "name": name,
        "marketId": market_id,
        "paymentInstructions": payment_instructions or "",
        "paymentMethods": payment_methods or [],
    }
    
    return make_request("POST", "/payment_policy", data=payload)


@mcp.tool()
def update_payment_policy(payment_policy_id: str, name: str = None,
                          payment_instructions: str = None) -> dict:
    """
    Updates an existing payment policy.
    
    Args:
        payment_policy_id: The eBay-assigned policy ID
        name: Updated policy name (optional)
        payment_instructions: Updated payment instructions (optional)
    
    Returns:
        Updated payment policy details
    """
    payload = {}
    if name:
        payload["name"] = name
    if payment_instructions:
        payload["paymentInstructions"] = payment_instructions
    
    return make_request("PUT", f"/payment_policy/{payment_policy_id}", data=payload)


@mcp.tool()
def delete_payment_policy(payment_policy_id: str) -> dict:
    """
    Deletes a payment policy.
    
    Args:
        payment_policy_id: The eBay-assigned policy ID
    
    Returns:
        Response with delete status
    """
    return make_request("DELETE", f"/payment_policy/{payment_policy_id}")


@mcp.tool()
def get_return_policies(market_id: str, limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves all return policies for a marketplace.
    
    Args:
        market_id: eBay marketplace ID (required)
        limit: Maximum policies per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Return policy collection
    """
    return make_request("GET", "/return_policy",
                       params={"market_id": market_id, "limit": limit, "offset": offset})


@mcp.tool()
def get_return_policy(return_policy_id: str) -> dict:
    """
    Retrieves a specific return policy by ID.
    
    Args:
        return_policy_id: The eBay-assigned policy ID
    
    Returns:
        Return policy details
    """
    return make_request("GET", f"/return_policy/{return_policy_id}")


@mcp.tool()
def create_return_policy(name: str, market_id: str, description: str = None,
                         return_method: str = None, refund_method: str = None,
                         restocking_fee: str = None, return_shipping_payer: str = None) -> dict:
    """
    Creates a new return policy.
    
    Args:
        name: Policy name
        market_id: eBay marketplace ID
        description: Policy description
        return_method: Return method (EXCHANGE, RETURN)
        refund_method: Refund method (MONEY_BACK, EXCHANGE)
        restocking_fee: Restocking fee value
        return_shipping_payer: Who pays for return shipping (BUYER, SELLER)
    
    Returns:
        Created return policy details
    """
    payload = {
        "name": name,
        "marketId": market_id,
    }
    if description:
        payload["description"] = description
    if return_method:
        payload["returnMethod"] = return_method
    if refund_method:
        payload["refundMethod"] = refund_method
    if restocking_fee:
        payload["restockingFee"] = restocking_fee
    if return_shipping_payer:
        payload["returnShippingPayer"] = return_shipping_payer
    
    return make_request("POST", "/return_policy", data=payload)


@mcp.tool()
def update_return_policy(return_policy_id: str, name: str = None,
                          description: str = None) -> dict:
    """
    Updates an existing return policy.
    
    Args:
        return_policy_id: The eBay-assigned policy ID
        name: Updated policy name (optional)
        description: Updated description (optional)
    
    Returns:
        Updated return policy details
    """
    payload = {}
    if name:
        payload["name"] = name
    if description:
        payload["description"] = description
    
    return make_request("PUT", f"/return_policy/{return_policy_id}", data=payload)


@mcp.tool()
def delete_return_policy(return_policy_id: str) -> dict:
    """
    Deletes a return policy.
    
    Args:
        return_policy_id: The eBay-assigned policy ID
    
    Returns:
        Response with delete status
    """
    return make_request("DELETE", f"/return_policy/{return_policy_id}")


@mcp.tool()
def get_opted_in_programs() -> dict:
    """
    Retrieves all programs the seller has opted into.
    
    Returns:
        Opted-in programs collection
    """
    return make_request("GET", "/program/get_opted_in_programs")


@mcp.tool()
def opt_in_to_program(program_id: str, marketplace_id: str) -> dict:
    """
    Optes the seller into a program.
    
    Args:
        program_id: Program ID
        marketplace_id: eBay marketplace ID
    
    Returns:
        Response with opt-in status
    """
    return make_request("POST", "/program/opt_in",
                       data={"programId": program_id, "marketplaceId": marketplace_id})


@mcp.tool()
def opt_out_of_program(program_id: str, marketplace_id: str) -> dict:
    """
    Optes the seller out of a program.
    
    Args:
        program_id: Program ID
        marketplace_id: eBay marketplace ID
    
    Returns:
        Response with opt-out status
    """
    return make_request("POST", "/program/opt_out",
                       data={"programId": program_id, "marketplaceId": marketplace_id})


@mcp.tool()
def get_privileges() -> dict:
    """
    Retrieves the seller's account privileges.
    
    Returns:
        Account privileges
    """
    return make_request("GET", "/privilege")
