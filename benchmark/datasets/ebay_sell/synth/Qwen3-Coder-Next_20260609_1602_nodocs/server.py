#!/usr/bin/env python3
"""
eBay Sell API MCP Server

An MCP server with comprehensive coverage of the eBay Sell API for autonomous agents.
"""

import os
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("ebay-sell", inherit_from=["mcp-1"])

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

# OAuth token endpoint
OAUTH_TOKEN_URL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"


def get_base_url() -> str:
    """Get the correct base URL based on environment."""
    return BASE_URLS.get(EBAY_ENVIRONMENT, BASE_URLS["SANDBOX"])


def get_access_token() -> Optional[str]:
    """Get access token using refresh token flow."""
    if not EBAY_APP_ID or not EBAY_CERT_ID or not EBAY_REFRESH_TOKEN:
        return None

    auth = requests.auth.HTTPBasicAuth(EBAY_APP_ID, EBAY_CERT_ID)
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN,
        "scope": " ".join([
            "https://api.ebay.com/oauth/api_scope",
            "https://api.ebay.com/oauth/api_scope/sell.account",
            "https://api.ebay.com/oauth/api_scope/sell.marketing",
            "https://api.ebay.com/oauth/api_scope/sell.inventory",
            "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
            "https://api.ebay.com/oauth/api_scope/sell.analytics",
            "https://api.ebay.com/oauth/api_scope/sell.finances",
        ]),
    }

    try:
        response = requests.post(OAUTH_TOKEN_URL, auth=auth, data=data)
        response.raise_for_status()
        return response.json().get("access_token")
    except Exception:
        return None


def make_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to eBay API."""
    access_token = get_access_token()
    if not access_token:
        return {"error": "Authentication failed. Please check EBAY_APP_ID, EBAY_CERT_ID, and EBAY_REFRESH_TOKEN."}

    base_url = get_base_url()
    url = f"{base_url}{path}"
    
    request_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if headers:
        request_headers.update(headers)

    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json,
            headers=request_headers,
        )
        
        # Parse response
        try:
            data = response.json()
        except ValueError:
            data = {"raw_response": response.text}
        
        if response.status_code >= 400:
            return {"error": f"API Error: {response.status_code}", "details": data}
        
        return data
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# INVENTORY API - Items
# ============================================================================

@mcp.tool()
def get_item(item_id: str) -> Dict[str, Any]:
    """
    Get details of a specific item by ID.
    
    Args:
        item_id: The unique identifier of the item
    
    Returns:
        Item details including title, price, quantity, and status
    """
    return make_request("GET", f"/sell/inventory/v1/inventory_item/{item_id}")


@mcp.tool()
def list_items(
    limit: int = 10,
    offset: int = 0,
    seller_collection: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List inventory items with optional filtering.
    
    Args:
        limit: Maximum number of items to return (max 100)
        offset: Pagination offset
        seller_collection: Filter by seller collection
    
    Returns:
        List of inventory items with pagination info
    """
    params = {"limit": limit, "offset": offset}
    if seller_collection:
        params["seller_collection"] = seller_collection
    return make_request("GET", "/sell/inventory/v1/inventory_item", params=params)


@mcp.tool()
def create_item(
    sku: str,
    title: str,
    price: Dict[str, Any],
    quantity: int = 0,
    description: Optional[str] = None,
    category_id: Optional[str] = None,
    brand: Optional[str] = None,
    image_urls: Optional[list[str]] = None,
    condition: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new inventory item.
    
    Args:
        sku: Stock Keeping Unit - unique identifier for the item
        title: Item title
        price: Price object with value and currency
        quantity: Available quantity (default: 0)
        description: Item description
        category_id: eBay category ID
        brand: Brand name
        image_urls: List of image URLs
        condition: Item condition (e.g., "NEW", "USED_EXCELLENT")
        **kwargs: Additional item properties
    
    Returns:
        Created item details
    """
    payload = {
        "sku": sku,
        "title": title,
        "price": price,
        "quantity": quantity,
    }
    if description:
        payload["description"] = description
    if category_id:
        payload["categoryID"] = category_id
    if brand:
        payload["brand"] = brand
    if image_urls:
        payload["imageUrls"] = image_urls
    if condition:
        payload["condition"] = condition
    
    payload.update(kwargs)
    return make_request("POST", "/sell/inventory/v1/inventory_item", json=payload)


@mcp.tool()
def update_item(
    item_id: str,
    title: Optional[str] = None,
    price: Optional[Dict[str, Any]] = None,
    quantity: Optional[int] = None,
    description: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Update an existing inventory item.
    
    Args:
        item_id: The unique identifier of the item to update
        title: New title (optional)
        price: New price object (optional)
        quantity: New quantity (optional)
        description: New description (optional)
        **kwargs: Additional properties to update
    
    Returns:
        Updated item details
    """
    # First get the current item to preserve existing values
    current_item = get_item(item_id)
    if "error" in current_item:
        return current_item
    
    payload = {"sku": current_item.get("sku", item_id)}
    
    if title:
        payload["title"] = title
    if price:
        payload["price"] = price
    if quantity is not None:
        payload["quantity"] = quantity
    if description:
        payload["description"] = description
    
    payload.update(kwargs)
    
    return make_request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{item_id}",
        json=payload,
    )


@mcp.tool()
def delete_item(item_id: str) -> Dict[str, Any]:
    """
    Delete an inventory item.
    
    Args:
        item_id: The unique identifier of the item to delete
    
    Returns:
        Deletion confirmation
    """
    return make_request(
        "DELETE",
        f"/sell/inventory/v1/inventory_item/{item_id}",
    )


@mcp.tool()
def add_item_image(item_id: str, image_url: str) -> Dict[str, Any]:
    """
    Add an image to an existing inventory item.
    
    Args:
        item_id: The unique identifier of the item
        image_url: URL of the image to add
    
    Returns:
        Updated item with new image
    """
    return make_request(
        "POST",
        f"/sell/inventory/v1/inventory_item/{item_id}/image",
        json={"imageUrl": image_url},
    )


@mcp.tool()
def get_item_price(item_id: str) -> Dict[str, Any]:
    """
    Get price information for an item.
    
    Args:
        item_id: The unique identifier of the item
    
    Returns:
        Price details
    """
    return make_request("GET", f"/sell/inventory/v1/inventory_item/{item_id}/price")


@mcp.tool()
def update_item_price(
    item_id: str,
    price: Dict[str, Any],
    discount_percentage: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Update the price of an inventory item.
    
    Args:
        item_id: The unique identifier of the item
        price: Price object with value and currency
        discount_percentage: Optional discount percentage
    
    Returns:
        Updated price information
    """
    payload = {"price": price}
    if discount_percentage is not None:
        payload["discountPercentage"] = discount_percentage
    
    return make_request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{item_id}/price",
        json=payload,
    )


@mcp.tool()
def get_item_quantity(item_id: str) -> Dict[str, Any]:
    """
    Get quantity information for an item.
    
    Args:
        item_id: The unique identifier of the item
    
    Returns:
        Quantity details
    """
    return make_request("GET", f"/sell/inventory/v1/inventory_item/{item_id}/quantity")


@mcp.tool()
def update_item_quantity(
    item_id: str,
    available: int,
    sold: int = 0,
    on_order: int = 0,
    reserved: int = 0,
) -> Dict[str, Any]:
    """
    Update the quantity of an inventory item.
    
    Args:
        item_id: The unique identifier of the item
        available: Available quantity
        sold: Quantity sold (default: 0)
        on_order: Quantity on order (default: 0)
        reserved: Quantity reserved (default: 0)
    
    Returns:
        Updated quantity information
    """
    payload = {
        "available": available,
        "sold": sold,
        "onOrder": on_order,
        "reserved": reserved,
    }
    return make_request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{item_id}/quantity",
        json=payload,
    )


# ============================================================================
# INVENTORY API - Offers (Listing Offers)
# ============================================================================

@mcp.tool()
def get_listing_offer(offer_id: str) -> Dict[str, Any]:
    """
    Get a specific listing offer by ID.
    
    Args:
        offer_id: The unique identifier of the listing offer
    
    Returns:
        Listing offer details
    """
    return make_request("GET", f"/sell/inventory/v1/offers/{offer_id}")


@mcp.tool()
def list_listing_offers(
    limit: int = 10,
    offset: int = 0,
    sku: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List listing offers with optional filtering.
    
    Args:
        limit: Maximum number of offers to return (max 100)
        offset: Pagination offset
        sku: Filter by SKU
    
    Returns:
        List of listing offers with pagination info
    """
    params = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    return make_request("GET", "/sell/inventory/v1/offers", params=params)


@mcp.tool()
def create_listing_offer(
    sku: str,
    listing_title: str,
    price: Dict[str, Any],
    quantity: int = 0,
    category_id: Optional[str] = None,
    description: Optional[str] = None,
    condition: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new listing offer.
    
    Args:
        sku: Stock Keeping Unit
        listing_title: Title for the listing
        price: Price object with value and currency
        quantity: Available quantity (default: 0)
        category_id: eBay category ID
        description: Listing description
        condition: Item condition
        **kwargs: Additional offer properties
    
    Returns:
        Created listing offer details
    """
    payload = {
        "sku": sku,
        "listingTitle": listing_title,
        "price": price,
        "quantity": quantity,
    }
    if category_id:
        payload["categoryId"] = category_id
    if description:
        payload["description"] = description
    if condition:
        payload["condition"] = condition
    
    payload.update(kwargs)
    return make_request("POST", "/sell/inventory/v1/offers", json=payload)


@mcp.tool()
def update_listing_offer(
    offer_id: str,
    listing_title: Optional[str] = None,
    price: Optional[Dict[str, Any]] = None,
    quantity: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Update an existing listing offer.
    
    Args:
        offer_id: The unique identifier of the listing offer
        listing_title: New title (optional)
        price: New price object (optional)
        quantity: New quantity (optional)
        **kwargs: Additional properties to update
    
    Returns:
        Updated listing offer details
    """
    payload = {}
    if listing_title:
        payload["listingTitle"] = listing_title
    if price:
        payload["price"] = price
    if quantity is not None:
        payload["quantity"] = quantity
    
    payload.update(kwargs)
    return make_request(
        "PUT",
        f"/sell/inventory/v1/offers/{offer_id}",
        json=payload,
    )


@mcp.tool()
def delete_listing_offer(offer_id: str) -> Dict[str, Any]:
    """
    Delete a listing offer.
    
    Args:
        offer_id: The unique identifier of the listing offer to delete
    
    Returns:
        Deletion confirmation
    """
    return make_request(
        "DELETE",
        f"/sell/inventory/v1/offers/{offer_id}",
    )


@mcp.tool()
def activate_listing_offer(offer_id: str) -> Dict[str, Any]:
    """
    Activate a listing offer (publish it to eBay).
    
    Args:
        offer_id: The unique identifier of the listing offer
    
    Returns:
        Activation confirmation
    """
    return make_request(
        "POST",
        f"/sell/inventory/v1/offers/{offer_id}/activate",
    )


@mcp.tool()
def deactivate_listing_offer(offer_id: str) -> Dict[str, Any]:
    """
    Deactivate a listing offer (remove it from eBay).
    
    Args:
        offer_id: The unique identifier of the listing offer
    
    Returns:
        Deactivation confirmation
    """
    return make_request(
        "POST",
        f"/sell/inventory/v1/offers/{offer_id}/deactivate",
    )


# ============================================================================
# INVENTORY API - Inventory Locations
# ============================================================================

@mcp.tool()
def get_inventory_location(location_id: str) -> Dict[str, Any]:
    """
    Get details of a specific inventory location.
    
    Args:
        location_id: The unique identifier of the inventory location
    
    Returns:
        Location details including address and operating hours
    """
    return make_request("GET", f"/sell/inventory/v1/location/{location_id}")


@mcp.tool()
def list_inventory_locations(
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    List inventory locations.
    
    Args:
        limit: Maximum number of locations to return (max 100)
        offset: Pagination offset
    
    Returns:
        List of inventory locations with pagination info
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/sell/inventory/v1/location", params=params)


@mcp.tool()
def create_inventory_location(
    location_id: str,
    location_name: str,
    address: Dict[str, Any],
    location_instructions: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new inventory location.
    
    Args:
        location_id: Unique identifier for the location
        location_name: Display name for the location
        address: Address object with street, city, state, postalCode, country
        location_instructions: Special instructions for the location
        **kwargs: Additional location properties
    
    Returns:
        Created location details
    """
    payload = {
        "locationId": location_id,
        "locationName": location_name,
        "address": address,
    }
    if location_instructions:
        payload["locationInstructions"] = location_instructions
    
    payload.update(kwargs)
    return make_request("POST", "/sell/inventory/v1/location", json=payload)


@mcp.tool()
def update_inventory_location(
    location_id: str,
    location_name: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Update an existing inventory location.
    
    Args:
        location_id: The unique identifier of the location
        location_name: New name (optional)
        address: New address object (optional)
        **kwargs: Additional properties to update
    
    Returns:
        Updated location details
    """
    payload = {}
    if location_name:
        payload["locationName"] = location_name
    if address:
        payload["address"] = address
    
    payload.update(kwargs)
    return make_request(
        "PUT",
        f"/sell/inventory/v1/location/{location_id}",
        json=payload,
    )


@mcp.tool()
def delete_inventory_location(location_id: str) -> Dict[str, Any]:
    """
    Delete an inventory location.
    
    Args:
        location_id: The unique identifier of the location to delete
    
    Returns:
        Deletion confirmation
    """
    return make_request(
        "DELETE",
        f"/sell/inventory/v1/location/{location_id}",
    )


@mcp.tool()
def get_location_inventory(location_id: str) -> Dict[str, Any]:
    """
    Get inventory items at a specific location.
    
    Args:
        location_id: The unique identifier of the location
    
    Returns:
        Inventory items at the location
    """
    return make_request("GET", f"/sell/inventory/v1/location/{location_id}/inventory")


@mcp.tool()
def add_inventory_to_location(
    location_id: str,
    sku: str,
    quantity: int,
) -> Dict[str, Any]:
    """
    Add inventory to a specific location.
    
    Args:
        location_id: The unique identifier of the location
        sku: Stock Keeping Unit
        quantity: Quantity to add
    
    Returns:
        Updated location inventory
    """
    return make_request(
        "POST",
        f"/sell/inventory/v1/location/{location_id}/inventory/{sku}",
        json={"quantity": quantity},
    )


@mcp.tool()
def remove_inventory_from_location(
    location_id: str,
    sku: str,
    quantity: int,
) -> Dict[str, Any]:
    """
    Remove inventory from a specific location.
    
    Args:
        location_id: The unique identifier of the location
        sku: Stock Keeping Unit
        quantity: Quantity to remove
    
    Returns:
        Updated location inventory
    """
    return make_request(
        "DELETE",
        f"/sell/inventory/v1/location/{location_id}/inventory/{sku}",
        params={"quantity": quantity},
    )


# ============================================================================
# FULFILLMENT API - Orders
# ============================================================================

@mcp.tool()
def get_order(order_id: str) -> Dict[str, Any]:
    """
    Get details of a specific order.
    
    Args:
        order_id: The unique identifier of the order
    
    Returns:
        Order details including buyer, items, shipping, and payment
    """
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}")


@mcp.tool()
def list_orders(
    limit: int = 10,
    offset: int = 0,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    order_status: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List orders with optional filtering.
    
    Args:
        limit: Maximum number of orders to return (max 100)
        offset: Pagination offset
        date_from: Filter orders from this date (ISO 8601)
        date_to: Filter orders until this date (ISO 8601)
        order_status: Filter by status (e.g., "COMPLETED", "SHIPPED", "PAUSED")
    
    Returns:
        List of orders with pagination info
    """
    params = {"limit": limit, "offset": offset}
    if date_from:
        params["dateFrom"] = date_from
    if date_to:
        params["dateTo"] = date_to
    if order_status:
        params["orderStatus"] = order_status
    return make_request("GET", "/sell/fulfillment/v1/order", params=params)


@mcp.tool()
def update_order(
    order_id: str,
    shipping_tracking_number: Optional[str] = None,
    shipping carrier: Optional[str] = None,
    shipping_method: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update order fulfillment information.
    
    Args:
        order_id: The unique identifier of the order
        shipping_tracking_number: Shipping tracking number
        shipping_carrier: Shipping carrier name
        shipping_method: Shipping method (e.g., "StandardShipping")
    
    Returns:
        Updated order details
    """
    payload = {}
    if shipping_tracking_number:
        payload["shippingTrackingNumber"] = shipping_tracking_number
    if shipping_carrier:
        payload["shippingCarrier"] = shipping_carrier
    if shipping_method:
        payload["shippingMethod"] = shipping_method
    return make_request(
        "PUT",
        f"/sell/fulfillment/v1/order/{order_id}",
        json=payload,
    )


@mcp.tool()
def ship_order(
    order_id: str,
    tracking_number: str,
    carrier: str,
    notify_buyer: bool = True,
) -> Dict[str, Any]:
    """
    Mark an order as shipped.
    
    Args:
        order_id: The unique identifier of the order
        tracking_number: Shipping tracking number
        carrier: Shipping carrier name
        notify_buyer: Whether to notify the buyer (default: True)
    
    Returns:
        Shipment confirmation
    """
    payload = {
        "shippingTrackingNumber": tracking_number,
        "shippingCarrier": carrier,
        "notifyBuyer": notify_buyer,
    }
    return make_request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/ship",
        json=payload,
    )


@mcp.tool()
def cancel_order(order_id: str, reason: str = "Buyer Canceled") -> Dict[str, Any]:
    """
    Cancel an order.
    
    Args:
        order_id: The unique identifier of the order
        reason: Reason for cancellation (default: "Buyer Canceled")
    
    Returns:
        Cancellation confirmation
    """
    return make_request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/cancel",
        json={"cancellation": {"reason": reason}},
    )


# ============================================================================
# FULFILLMENT API - Orders (Alternative endpoint)
# ============================================================================

@mcp.tool()
def get_order_transactions(order_id: str) -> Dict[str, Any]:
    """
    Get transaction details for an order.
    
    Args:
        order_id: The unique identifier of the order
    
    Returns:
        Transaction details
    """
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}/transaction")


# ============================================================================
# ACCOUNT API - Policies
# ============================================================================

@mcp.tool()
def get_policy(policy_id: str) -> Dict[str, Any]:
    """
    Get details of a specific policy.
    
    Args:
        policy_id: The unique identifier of the policy
    
    Returns:
        Policy details including name, description, and terms
    """
    return make_request("GET", f"/sell/account/v1/policy/{policy_id}")


@mcp.tool()
def list_policies(
    limit: int = 10,
    offset: int = 0,
    policy_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List policies with optional filtering.
    
    Args:
        limit: Maximum number of policies to return (max 100)
        offset: Pagination offset
        policy_type: Filter by policy type (e.g., "SHIPPING", "PAYMENT", "RETURN")
    
    Returns:
        List of policies with pagination info
    """
    params = {"limit": limit, "offset": offset}
    if policy_type:
        params["policyType"] = policy_type
    return make_request("GET", "/sell/account/v1/policy", params=params)


@mcp.tool()
def create_policy(
    policy_type: str,
    name: str,
    description: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new policy.
    
    Args:
        policy_type: Type of policy (e.g., "SHIPPING", "PAYMENT", "RETURN")
        name: Policy name
        description: Policy description
        **kwargs: Policy-specific parameters
    
    Returns:
        Created policy details
    """
    payload = {
        "policyType": policy_type,
        "name": name,
    }
    if description:
        payload["description"] = description
    
    payload.update(kwargs)
    return make_request("POST", "/sell/account/v1/policy", json=payload)


@mcp.tool()
def update_policy(
    policy_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Update an existing policy.
    
    Args:
        policy_id: The unique identifier of the policy
        name: New name (optional)
        description: New description (optional)
        **kwargs: Policy-specific parameters to update
    
    Returns:
        Updated policy details
    """
    payload = {}
    if name:
        payload["name"] = name
    if description:
        payload["description"] = description
    
    payload.update(kwargs)
    return make_request(
        "PUT",
        f"/sell/account/v1/policy/{policy_id}",
        json=payload,
    )


@mcp.tool()
def delete_policy(policy_id: str) -> Dict[str, Any]:
    """
    Delete a policy.
    
    Args:
        policy_id: The unique identifier of the policy to delete
    
    Returns:
        Deletion confirmation
    """
    return make_request(
        "DELETE",
        f"/sell/account/v1/policy/{policy_id}",
    )


# ============================================================================
# ACCOUNT API - Payment Policies
# ============================================================================

@mcp.tool()
def get_payment_policy(policy_id: str) -> Dict[str, Any]:
    """
    Get details of a specific payment policy.
    
    Args:
        policy_id: The unique identifier of the the payment policy
    
    Returns:
        Payment policy details
    """
    return get_policy(policy_id)


@mcp.tool()
def list_payment_policies(
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    List payment policies.
    
    Args:
        limit: Maximum number of policies to return (max 100)
        offset: Pagination offset
    
    Returns:
        List of payment policies
    """
    return list_policies(limit=limit, offset=offset, policy_type="PAYMENT")


@mcp.tool()
def create_payment_policy(
    name: str,
    payment_instructions: Optional[str] = None,
    payment_methods: Optional[list] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new payment policy.
    
    Args:
        name: Policy name
        payment_instructions: Payment instructions for buyers
        payment_methods: List of accepted payment methods
        **kwargs: Additional payment policy parameters
    
    Returns:
        Created payment policy details
    """
    payload = {
        "name": name,
        "paymentInstructions": payment_instructions,
    }
    if payment_methods:
        payload["paymentMethods"] = payment_methods
    
    payload.update(kwargs)
    return create_policy("PAYMENT", name, **payload)


# ============================================================================
# ACCOUNT API - Shipping Policies
# ============================================================================

@mcp.tool()
def get_shipping_policy(policy_id: str) -> Dict[str, Any]:
    """
    Get details of a specific shipping policy.
    
    Args:
        policy_id: The unique identifier of the shipping policy
    
    Returns:
        Shipping policy details
    """
    return get_policy(policy_id)


@mcp.tool()
def list_shipping_policies(
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    List shipping policies.
    
    Args:
        limit: Maximum number of policies to return (max 100)
        offset: Pagination offset
    
    Returns:
        List of shipping policies
    """
    return list_policies(limit=limit, offset=offset, policy_type="SHIPPING")


@mcp.tool()
def create_shipping_policy(
    name: str,
    description: Optional[str] = None,
    shipping_details: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new shipping policy.
    
    Args:
        name: Policy name
        description: Policy description
        shipping_details: Shipping rate table and service details
        **kwargs: Additional shipping policy parameters
    
    Returns:
        Created shipping policy details
    """
    payload = {
        "name": name,
    }
    if description:
        payload["description"] = description
    if shipping_details:
        payload["shippingDetails"] = shipping_details
    
    payload.update(kwargs)
    return create_policy("SHIPPING", name, description, **payload)


# ============================================================================
# ACCOUNT API - Return Policies
# ============================================================================

@mcp.tool()
def get_return_policy(policy_id: str) -> Dict[str, Any]:
    """
    Get details of a specific return policy.
    
    Args:
        policy_id: The unique identifier of the return policy
    
    Returns:
        Return policy details
    """
    return get_policy(policy_id)


@mcp.tool()
def list_return_policies(
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    List return policies.
    
    Args:
        limit: Maximum number of policies to return (max 100)
        offset: Pagination offset
    
    Returns:
        List of return policies
    """
    return list_policies(limit=limit, offset=offset, policy_type="RETURN")


@mcp.tool()
def create_return_policy(
    name: str,
    description: Optional[str] = None,
    return_method: Optional[str] = None,
    refund_method: Optional[str] = None,
    return_period: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new return policy.
    
    Args:
        name: Policy name
        description: Policy description
        return_method: Return method (e.g., "PRE_PAID_LABEL", "CUSTOM_CONTACT")
        refund_method: Refund method (e.g., "MONEY_BACK", "EXCHANGE")
        return_period: Return period object with days
        **kwargs: Additional return policy parameters
    
    Returns:
        Created return policy details
    """
    payload = {
        "name": name,
    }
    if description:
        payload["description"] = description
    if return_method:
        payload["returnMethod"] = return_method
    if refund_method:
        payload["refundMethod"] = refund_method
    if return_period:
        payload["returnPeriod"] = return_period
    
    payload.update(kwargs)
    return create_policy("RETURN", name, description, **payload)


# ============================================================================
# ACCOUNT API - Programs
# ============================================================================

@mcp.tool()
def get_program(program_id: str) -> Dict[str, Any]:
    """
    Get details of a specific program.
    
    Args:
        program_id: The unique identifier of the program
    
    Returns:
        Program details
    """
    return make_request("GET", f"/sell/account/v1/program/{program_id}")


@mcp.tool()
def list_programs(
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    List account programs.
    
    Args:
        limit: Maximum number of programs to return (max 100)
        offset: Pagination offset
    
    Returns:
        List of programs
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/sell/account/v1/program", params=params)


@mcp.tool()
def create_program(program_type: str, **kwargs: Any) -> Dict[str, Any]:
    """
    Create a new program.
    
    Args:
        program_type: Type of program (e.g., "BULK_LIST", "REPRICING")
        **kwargs: Program-specific parameters
    
    Returns:
        Created program details
    """
    payload = {"programType": program_type}
    payload.update(kwargs)
    return make_request("POST", "/sell/account/v1/program", json=payload)


@mcp.tool()
def update_program(
    program_id: str,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Update an existing program.
    
    Args:
        program_id: The unique identifier of the program
        **kwargs: Program-specific parameters to update
    
    Returns:
        Updated program details
    """
    return make_request(
        "PUT",
        f"/sell/account/v1/program/{program_id}",
        json=kwargs,
    )


@mcp.tool()
def delete_program(program_id: str) -> Dict[str, Any]:
    """
    Delete a program.
    
    Args:
        program_id: The unique identifier of the program to delete
    
    Returns:
        Deletion confirmation
    """
    return make_request(
        "DELETE",
        f"/sell/account/v1/program/{program_id}",
    )


# ============================================================================
# MARKETING API - Promotions
# ============================================================================

@mcp.tool()
def get_promotion(promotion_id: str) -> Dict[str, Any]:
    """
    Get details of a specific promotion.
    
    Args:
        promotion_id: The unique identifier of the promotion
    
    Returns:
        Promotion details
    """
    return make_request("GET", f"/sell/marketing/v1/promotion/{promotion_id}")


@mcp.tool()
def list_promotions(
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    List promotions.
    
    Args:
        limit: Maximum number of promotions to return (max 100)
        offset: Pagination offset
    
    Returns:
        List of promotions with pagination info
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/sell/marketing/v1/promotion", params=params)


@mcp.tool()
def create_promotion(
    promotion_type: str,
    title: str,
    description: Optional[str] = None,
    discount: Dict[str, Any] = None,
    applicable_items: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new promotion.
    
    Args:
        promotion_type: Type of promotion (e.g., "DISCOUNT", "BUY_ONE_GET_ONE")
        title: Promotion title
        description: Promotion description
        discount: Discount object with type and value
        applicable_items: Object defining which items are applicable
        **kwargs: Additional promotion parameters
    
    Returns:
        Created promotion details
    """
    payload = {
        "promotionType": promotion_type,
        "title": title,
    }
    if description:
        payload["description"] = description
    if discount:
        payload["discount"] = discount
    if applicable_items:
        payload["applicableItems"] = applicable_items
    
    payload.update(kwargs)
    return make_request("POST", "/sell/marketing/v1/promotion", json=payload)


@mcp.tool()
def update_promotion(
    promotion_id: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
    discount: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Update an existing promotion.
    
    Args:
        promotion_id: The unique identifier of the promotion
        title: New title (optional)
        description: New description (optional)
        discount: New discount object (optional)
        **kwargs: Additional properties to update
    
    Returns:
        Updated promotion details
    """
    payload = {}
    if title:
        payload["title"] = title
    if description:
        payload["description"] = description
    if discount:
        payload["discount"] = discount
    
    payload.update(kwargs)
    return make_request(
        "PUT",
        f"/sell/marketing/v1/promotion/{promotion_id}",
        json=payload,
    )


@mcp.tool()
def delete_promotion(promotion_id: str) -> Dict[str, Any]:
    """
    Delete a promotion.
    
    Args:
        promotion_id: The unique identifier of the promotion to delete
    
    Returns:
        Deletion confirmation
    """
    return make_request(
        "DELETE",
        f"/sell/marketing/v1/promotion/{promotion_id}",
    )


@mcp.tool()
def activate_promotion(promotion_id: str) -> Dict[str, Any]:
    """
    Activate a promotion.
    
    Args:
        promotion_id: The unique identifier of the promotion
    
    Returns:
        Activation confirmation
    """
    return make_request(
        "POST",
        f"/sell/marketing/v1/promotion/{promotion_id}/activate",
    )


@mcp.tool()
def deactivate_promotion(promotion_id: str) -> Dict[str, Any]:
    """
    Deactivate a promotion.
    
    Args:
        promotion_id: The unique identifier of the promotion
    
    Returns:
        Deactivation confirmation
    """
    return make_request(
        "POST",
        f"/sell/marketing/v1/promotion/{promotion_id}/deactivate",
    )


# ============================================================================
# MARKETING API - Promotional Sale
# ============================================================================

@mcp.tool()
def get_promotional_sale(sale_id: str) -> Dict[str, Any]:
    """
    Get details of a specific promotional sale.
    
    Args:
        sale_id: The unique identifier of the promotional sale
    
    Returns:
        Promotional sale details
    """
    return make_request("GET", f"/sell/marketing/v1/promotional_sale/{sale_id}")


@mcp.tool()
def list_promotional_sales(
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    List promotional sales.
    
    Args:
        limit: Maximum number of sales to return (max 100)
        offset: Pagination offset
    
    Returns:
        List of promotional sales with pagination info
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/sell/marketing/v1/promotional_sale", params=params)


@mcp.tool()
def create_promotional_sale(
    title: str,
    description: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    discount: Dict[str, Any] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new promotional sale.
    
    Args:
        title: Sale title
        description: Sale description
        start_time: Start time in ISO 8601 format
        end_time: End time in ISO 8601 format
        discount: Discount object
        **kwargs: Additional sale parameters
    
    Returns:
        Created promotional sale details
    """
    payload = {
        "title": title,
        "startTime": start_time,
        "endTime": end_time,
        "discount": discount,
    }
    if description:
        payload["description"] = description
    
    payload.update(kwargs)
    return make_request("POST", "/sell/marketing/v1/promotional_sale", json=payload)


@mcp.tool()
def update_promotional_sale(
    sale_id: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Update an existing promotional sale.
    
    Args:
        sale_id: The unique identifier of the promotional sale
        title: New title (optional)
        description: New description (optional)
        start_time: New start time (optional)
        end_time: New end time (optional)
        **kwargs: Additional properties to update
    
    Returns:
        Updated promotional sale details
    """
    payload = {}
    if title:
        payload["title"] = title
    if description:
        payload["description"] = description
    if start_time:
        payload["startTime"] = start_time
    if end_time:
        payload["endTime"] = end_time
    
    payload.update(kwargs)
    return make_request(
        "PUT",
        f"/sell/marketing/v1/promotional_sale/{sale_id}",
        json=payload,
    )


@mcp.tool()
def delete_promotional_sale(sale_id: str) -> Dict[str, Any]:
    """
    Delete a promotional sale.
    
    Args:
        sale_id: The unique identifier of the promotional sale to delete
    
    Returns:
        Deletion confirmation
    """
    return make_request(
        "DELETE",
        f"/sell/marketing/v1/promotional_sale/{sale_id}",
    )


# ============================================================================
# FINANCES API - Transactions
# ============================================================================

@mcp.tool()
def get_transaction(transaction_id: str) -> Dict[str, Any]:
    """
    Get details of a specific transaction.
    
    Args:
        transaction_id: The unique identifier of the transaction
    
    Returns:
        Transaction details
    """
    return make_request("GET", f"/sell/finances/v1/transaction/{transaction_id}")


@mcp.tool()
def list_transactions(
    limit: int = 10,
    offset: int = 0,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    transaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List transactions with optional filtering.
    
    Args:
        limit: Maximum number of transactions to return (max 100)
        offset: Pagination offset
        date_from: Filter transactions from this date (ISO 8601)
        date_to: Filter transactions until this date (ISO 8601)
        transaction_type: Filter by transaction type
    
    Returns:
        List of transactions with pagination info
    """
    params = {"limit": limit, "offset": offset}
    if date_from:
        params["dateFrom"] = date_from
    if date_to:
        params["dateTo"] = date_to
    if transaction_type:
        params["transactionType"] = transaction_type
    return make_request("GET", "/sell/finances/v1/transaction", params=params)


# ============================================================================
# FINANCES API - Payouts
# ============================================================================

@mcp.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """
    Get details of a specific payout.
    
    Args:
        payout_id: The unique identifier of the payout
    
    Returns:
        Payout details including amount and date
    """
    return make_request("GET", f"/sell/finances/v1/payout/{payout_id}")


@mcp.tool()
def list_payouts(
    limit: int = 10,
    offset: int = 0,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List payouts with optional filtering.
    
    Args:
        limit: Maximum number of payouts to return (max 100)
        offset: Pagination offset
        date_from: Filter payouts from this date (ISO 8601)
        date_to: Filter payouts until this date (ISO 8601)
    
    Returns:
        List of payouts with pagination info
    """
    params = {"limit": limit, "offset": offset}
    if date_from:
        params["dateFrom"] = date_from
    if date_to:
        params["dateTo"] = date_to
    return make_request("GET", "/sell/finances/v1/payout", params=params)


# ============================================================================
# FEED API
# ============================================================================

@mcp.tool()
def create_feed(
    feed_type: str,
    payload_file_name: str,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Create a new feed for bulk upload/download.
    
    Args:
        feed_type: Type of feed (e.g., "CREATE_INVENTORY_ITEM", "UPDATE_INVENTORY_ITEM")
        payload_file_name: Name of the payload file
        **kwargs: Additional feed parameters
    
    Returns:
        Feed creation details including feed ID
    """
    payload = {
        "feedType": feed_type,
        "payloadFileName": payload_file_name,
    }
    payload.update(kwargs)
    return make_request("POST", "/sell/feed/v1/feed", json=payload)


@mcp.tool()
def get_feed(feed_id: str) -> Dict[str, Any]:
    """
    Get details of a specific feed.
    
    Args:
        feed_id: The unique identifier of the feed
    
    Returns:
        Feed details including status and results
    """
    return make_request("GET", f"/sell/feed/v1/feed/{feed_id}")


@mcp.tool()
def list_feeds(
    limit: int = 10,
    offset: int = 0,
    feed_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List feeds with optional filtering.
    
    Args:
        limit: Maximum number of feeds to return (max 100)
        offset: Pagination offset
        feed_type: Filter by feed type
    
    Returns:
        List of feeds with pagination info
    """
    params = {"limit": limit, "offset": offset}
    if feed_type:
        params["feedType"] = feed_type
    return make_request("GET", "/sell/feed/v1/feed", params=params)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

@mcp.tool()
def get_user_account() -> Dict[str, Any]:
    """
    Get the authenticated user's account information.
    
    Returns:
        Account details including user ID and profile information
    """
    return make_request("GET", "/sell/account/v1/user")


@mcp.tool()
def get_category_tree(category_id: str = "0") -> Dict[str, Any]:
    """
    Get the eBay category tree.
    
    Args:
        category_id: Root category ID (default: "0" for complete tree)
    
    Returns:
        Category tree structure
    """
    return make_request("GET", f"/sell/account/v1/category_tree/{category_id}")


@mcp.tool()
def get_selling_limits() -> Dict[str, Any]:
    """
    Get the seller's selling limits and requirements.
    
    Returns:
        Selling limits information
    """
    return make_request("GET", "/sell/account/v1/selling_limit")


@mcp.tool()
def get_feedback_received(
    limit: int = 10,
    offset: int = 0,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get feedback received by the seller.
    
    Args:
        limit: Maximum number of feedback items to return (max 100)
        offset: Pagination offset
        date_from: Filter feedback from this date (ISO 8601)
        date_to: Filter feedback until this date (ISO 8601)
    
    Returns:
        List of feedback items with pagination info
    """
    params = {"limit": limit, "offset": offset}
    if date_from:
        params["dateFrom"] = date_from
    if date_to:
        params["dateTo"] = date_to
    return make_request("GET", "/sell/fulfillment/v1/feedback_received", params=params)


# Run the server
if __name__ == "__main__":
    mcp.run()
