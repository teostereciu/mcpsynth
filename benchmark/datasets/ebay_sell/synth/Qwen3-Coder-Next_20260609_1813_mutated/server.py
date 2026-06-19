#!/usr/bin/env python3
"""
eBay Sell API MCP Server

This server provides tools for interacting with the eBay Sell API through the
Model Context Protocol (MCP).
"""

import os
import requests
from typing import Optional, Dict, Any, List

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("ebay-sell")

# Configuration from environment variables
EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_REFRESH_TOKEN = os.environ.get("EBAY_REFRESH_TOKEN")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com"
}

BASE_URL = BASE_URLS.get(EBAY_ENVIRONMENT, BASE_URLS["SANDBOX"])

# OAuth token storage
oauth_token = None
token_expiry = None


def get_oauth_token() -> str:
    """Get or refresh OAuth token using refresh token flow."""
    global oauth_token, token_expiry
    
    # Check if we have a valid token
    if oauth_token and token_expiry and token_expiry > 0:
        import time
        if time.time() < token_expiry - 60:  # Refresh 60 seconds before expiry
            return oauth_token
    
    # Refresh token endpoint
    token_url = f"{BASE_URL}/identity/v1/oauth2/token"
    
    # Get access token from refresh token
    response = requests.post(
        token_url,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {requests.auth._basic_auth_str(EBAY_APP_ID, EBAY_CERT_ID)}"
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": EBAY_REFRESH_TOKEN,
            "scope": "https://api.ebay.com/oauth/api_scope"
        }
    )
    
    if response.status_code != 200:
        raise Exception(f"Failed to get OAuth token: {response.status_code} - {response.text}")
    
    data = response.json()
    oauth_token = data.get("access_token")
    
    # Set expiry (tokens typically last 2 hours)
    import time
    token_expiry = time.time() + data.get("expires_in", 7200)
    
    return oauth_token


def make_request(method: str, path: str, params: Optional[Dict] = None, 
                 data: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict[str, Any]:
    """Make an authenticated request to the eBay API."""
    token = get_oauth_token()
    
    url = f"{BASE_URL}{path}"
    
    request_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    if headers:
        request_headers.update(headers)
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=data,
            headers=request_headers
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            if response.status_code == 204:  # No content
                return {"status": "success", "status_code": 204}
            return response.json()
        else:
            # Return error info as dict
            error_text = response.text
            try:
                error_data = response.json()
                return {"error": error_data}
            except:
                return {"error": error_text}
                
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ============================================================================
# INVENTORY API TOOLS
# ============================================================================

@mcp.tool()
def create_inventory_location(
    merchant_location_key: str,
    location_name: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    location_types: Optional[List[str]] = None,
    hangup_address: Optional[Dict[str, Any]] = None,
    geo_coordinates: Optional[Dict[str, Any]] = None,
    merchant_location_status: Optional[str] = None,
    special_hours: Optional[Dict[str, Any]] = None,
    fulfillment_center_specs: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create a new inventory location.
    
    Use this call to create a new inventory location. In order to create and 
    publish an offer (and create an eBay listing), a seller must have at least 
    one location, as every offer must be associated with at least one location.
    
    Args:
        merchant_location_key: Unique seller-defined key for the inventory location (required)
        location_name: Name of the location
        address: Physical address of the location
        location_types: Types of location (Fulfillment center, Warehouse, Store)
        hangup_address: Alternate address for hangup
        geo_coordinates: Geographic coordinates
        merchant_location_status: Status of the location (ENABLED or DISABLED)
        special_hours: Special operating hours
        fulfillment_center_specs: Specifications for fulfillment center
        
    Returns:
        Success response with status 204
    """
    path = f"/location/{merchant_location_key}"
    
    # Build request body
    body = {}
    if location_name:
        body["locationName"] = location_name
    if address:
        body["address"] = address
    if location_types:
        body["locationTypes"] = location_types
    if hangup_address:
        body["hangupAddress"] = hangup_address
    if geo_coordinates:
        body["geoCoordinates"] = geo_coordinates
    if merchant_location_status:
        body["merchantLocationStatus"] = merchant_location_status
    if special_hours:
        body["specialHours"] = special_hours
    if fulfillment_center_specs:
        body["fulfillmentCenterSpecifications"] = fulfillment_center_specs
    
    return make_request("POST", path, data=body)


@mcp.tool()
def get_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """
    Get an inventory location by key.
    
    Args:
        merchant_location_key: The unique seller-defined key for the inventory location
        
    Returns:
        Inventory location details
    """
    path = f"/location/{merchant_location_key}"
    return make_request("GET", path)


@mcp.tool()
def list_inventory_locations() -> Dict[str, Any]:
    """
    List all inventory locations for the seller.
    
    Returns:
        Collection of inventory locations
    """
    path = "/location"
    return make_request("GET", path)


@mcp.tool()
def update_inventory_location(
    merchant_location_key: str,
    location_name: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    location_types: Optional[List[str]] = None,
    hangup_address: Optional[Dict[str, Any]] = None,
    geo_coordinates: Optional[Dict[str, Any]] = None,
    merchant_location_status: Optional[str] = None,
    special_hours: Optional[Dict[str, Any]] = None,
    fulfillment_center_specs: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Update an existing inventory location.
    
    Args:
        merchant_location_key: The unique seller-defined key for the inventory location
        location_name: Name of the location
        address: Physical address of the location
        location_types: Types of location
        hangup_address: Alternate address for hangup
        geo_coordinates: Geographic coordinates
        merchant_location_status: Status of the location
        special_hours: Special operating hours
        fulfillment_center_specs: Specifications for fulfillment center
        
    Returns:
        Success response with status 204
    """
    path = f"/location/{merchant_location_key}"
    
    # Build request body
    body = {}
    if location_name:
        body["locationName"] = location_name
    if address:
        body["address"] = address
    if location_types:
        body["locationTypes"] = location_types
    if hangup_address:
        body["hangupAddress"] = hangup_address
    if geo_coordinates:
        body["geoCoordinates"] = geo_coordinates
    if merchant_location_status:
        body["merchantLocationStatus"] = merchant_location_status
    if special_hours:
        body["specialHours"] = special_hours
    if fulfillment_center_specs:
        body["fulfillmentCenterSpecifications"] = fulfillment_center_specs
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def disable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """
    Disable an inventory location.
    
    Args:
        merchant_location_key: The unique seller-defined key for the inventory location
        
    Returns:
        Success response with status 204
    """
    return update_inventory_location(merchant_location_key, merchant_location_status="DISABLED")


@mcp.tool()
def enable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """
    Enable an inventory location.
    
    Args:
        merchant_location_key: The unique seller-defined key for the inventory location
        
    Returns:
        Success response with status 204
    """
    return update_inventory_location(merchant_location_key, merchant_location_status="ENABLED")


@mcp.tool()
def delete_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """
    Delete an inventory location.
    
    Args:
        merchant_location_key: The unique seller-defined key for the inventory location
        
    Returns:
        Success response with status 204
    """
    path = f"/location/{merchant_location_key}"
    return make_request("DELETE", path)


@mcp.tool()
def create_or_replace_inventory_item(
    seller_sku: str,
    condition: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    product_id: Optional[str] = None,
    brand: Optional[str] = None,
    mpn: Optional[str] = None,
    isbn: Optional[str] = None,
    ean: Optional[str] = None,
    upc: Optional[str] = None,
    image_urls: Optional[List[str]] = None,
    product_aspects: Optional[Dict[str, Any]] = None,
    package_weight: Optional[float] = None,
    package_dimensions: Optional[Dict[str, Any]] = None,
    availability: Optional[Dict[str, Any]] = None,
    price: Optional[float] = None,
    quantity: Optional[int] = None,
    marketplace_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create or replace an inventory item.
    
    This call creates a new inventory item record or replaces an existing one.
    
    Args:
        seller_sku: Seller-defined SKU value for the inventory item (required)
        condition: Item condition (NEW, USED, REPAIRABLE, etc.)
        title: Item title
        description: Item description
        product_id: eBay Product ID (ePID)
        brand: Brand name
        mpn: Manufacturer Part Number
        isbn: ISBN identifier
        ean: EAN identifier
        upc: UPC identifier
        image_urls: URLs to product images
        product_aspects: Product aspects (category-specific attributes)
        package_weight: Package weight
        package_dimensions: Package dimensions
        availability: Availability details
        price: Item price
        quantity: Available quantity
        marketplace_id: eBay marketplace ID
        
    Returns:
        Inventory item details
    """
    path = f"/inventory_item/{seller_sku}"
    
    # Build request body
    body = {}
    if condition:
        body["condition"] = condition
    if title:
        body["title"] = title
    if description:
        body["description"] = description
    if product_id:
        body["productId"] = product_id
    if brand:
        body["brand"] = brand
    if mpn:
        body["mpn"] = mpn
    if isbn:
        body["isbn"] = isbn
    if ean:
        body["ean"] = ean
    if upc:
        body["upc"] = upc
    if image_urls:
        body["imageUrls"] = image_urls
    if product_aspects:
        body["productAspects"] = product_aspects
    if package_weight:
        body["packageWeight"] = package_weight
    if package_dimensions:
        body["packageDimensions"] = package_dimensions
    if availability:
        body["availability"] = availability
    if price:
        body["price"] = price
    if quantity:
        body["quantity"] = quantity
    if marketplace_id:
        body["marketplaceId"] = marketplace_id
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def get_inventory_item(seller_sku: str) -> Dict[str, Any]:
    """
    Get an inventory item by SKU.
    
    Args:
        seller_sku: Seller-defined SKU value for the inventory item
        
    Returns:
        Inventory item details
    """
    path = f"/inventory_item/{seller_sku}"
    return make_request("GET", path)


@mcp.tool()
def list_inventory_items() -> Dict[str, Any]:
    """
    List all inventory items for the seller.
    
    Returns:
        Collection of inventory items
    """
    path = "/inventory_item"
    return make_request("GET", path)


@mcp.tool()
def delete_inventory_item(seller_sku: str) -> Dict[str, Any]:
    """
    Delete an inventory item.
    
    Args:
        seller_sku: Seller-defined SKU value for the inventory item
        
    Returns:
        Success response with status 204
    """
    path = f"/inventory_item/{seller_sku}"
    return make_request("DELETE", path)


@mcp.tool()
def bulk_create_or_replace_inventory_items(
    inventory_items: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Bulk create or replace inventory items (up to 25 at a time).
    
    Args:
        inventory_items: List of inventory item objects to create or replace
        
    Returns:
        Bulk operation response
    """
    path = "/inventory_item/bulk"
    return make_request("POST", path, data={"requests": inventory_items})


@mcp.tool()
def create_offer(
    seller_sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    price: Optional[Dict[str, Any]] = None,
    availability: Optional[Dict[str, Any]] = None,
    listing_description: Optional[str] = None,
    category_id: Optional[str] = None,
    payment_instructions: Optional[str] = None,
    listing_policies: Optional[Dict[str, Any]] = None,
    catalog_product_details: Optional[bool] = True
) -> Dict[str, Any]:
    """
    Create an offer for a specific inventory item.
    
    This call creates an offer for a specific inventory item on a specific 
    eBay marketplace. The offer can be published later to create an active listing.
    
    Args:
        seller_sku: Seller SKU for the inventory item
        marketplace_id: eBay marketplace ID
        format: Listing format (FIXED_PRICE, AUCTION, etc.)
        price: Price information
        availability: Availability details
        listing_description: Listing description
        category_id: eBay category ID
        payment_instructions: Payment instructions
        listing_policies: Listing policy references
        catalog_product_details: Whether to include catalog product details
        
    Returns:
        Created offer details with offerId
    """
    path = "/offer"
    
    # Build request body
    body = {}
    if seller_sku:
        body["sellerSku"] = seller_sku
    if marketplace_id:
        body["marketplaceId"] = marketplace_id
    if format:
        body["format"] = format
    if price:
        body["price"] = price
    if availability:
        body["availability"] = availability
    if listing_description:
        body["listingDescription"] = listing_description
    if category_id:
        body["categoryId"] = category_id
    if payment_instructions:
        body["paymentInstructions"] = payment_instructions
    if listing_policies:
        body["listingPolicies"] = listing_policies
    body["includeCatalogProductDetails"] = catalog_product_details
    
    return make_request("POST", path, data=body)


@mcp.tool()
def get_offer(offer_id: str) -> Dict[str, Any]:
    """
    Get an offer by ID.
    
    Args:
        offer_id: Unique identifier of the offer
        
    Returns:
        Offer details
    """
    path = f"/offer/{offer_id}"
    return make_request("GET", path)


@mcp.tool()
def list_offers() -> Dict[str, Any]:
    """
    List all offers for the seller.
    
    Returns:
        Collection of offers
    """
    path = "/offer"
    return make_request("GET", path)


@mcp.tool()
def update_offer(
    offer_id: str,
    seller_sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    price: Optional[Dict[str, Any]] = None,
    availability: Optional[Dict[str, Any]] = None,
    listing_description: Optional[str] = None,
    category_id: Optional[str] = None,
    payment_instructions: Optional[str] = None,
    listing_policies: Optional[Dict[str, Any]] = None,
    status: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update an existing offer.
    
    Args:
        offer_id: Unique identifier of the offer
        seller_sku: Seller SKU for the inventory item
        marketplace_id: eBay marketplace ID
        format: Listing format
        price: Price information
        availability: Availability details
        listing_description: Listing description
        category_id: eBay category ID
        payment_instructions: Payment instructions
        listing_policies: Listing policy references
        status: Offer status
        
    Returns:
        Updated offer details
    """
    path = f"/offer/{offer_id}"
    
    # Build request body
    body = {}
    if seller_sku:
        body["sellerSku"] = seller_sku
    if marketplace_id:
        body["marketplaceId"] = marketplace_id
    if format:
        body["format"] = format
    if price:
        body["price"] = price
    if availability:
        body["availability"] = availability
    if listing_description:
        body["listingDescription"] = listing_description
    if category_id:
        body["categoryId"] = category_id
    if payment_instructions:
        body["paymentInstructions"] = payment_instructions
    if listing_policies:
        body["listingPolicies"] = listing_policies
    if status:
        body["status"] = status
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def publish_offer(offer_id: str) -> Dict[str, Any]:
    """
    Publish an offer to create an eBay listing.
    
    Args:
        offer_id: Unique identifier of the offer to publish
        
    Returns:
        Publish response with listing details
    """
    path = f"/offer/{offer_id}/publish"
    return make_request("POST", path)


@mcp.tool()
def bulk_publish_offers(offer_ids: List[str]) -> Dict[str, Any]:
    """
    Bulk publish offers (up to 25 at a time).
    
    Args:
        offer_ids: List of offer IDs to publish
        
    Returns:
        Bulk publish response
    """
    path = "/offer/bulk/publish"
    return make_request("POST", path, data={"offerIds": offer_ids})


@mcp.tool()
def withdraw_offer(offer_id: str) -> Dict[str, Any]:
    """
    Withdraw (unpublish) an offer.
    
    Args:
        offer_id: Unique identifier of the offer to withdraw
        
    Returns:
        Withdraw response
    """
    path = f"/offer/{offer_id}/withdraw"
    return make_request("POST", path)


@mcp.tool()
def delete_offer(offer_id: str) -> Dict[str, Any]:
    """
    Delete an offer.
    
    Args:
        offer_id: Unique identifier of the offer to delete
        
    Returns:
        Success response with status 204
    """
    path = f"/offer/{offer_id}"
    return make_request("DELETE", path)


@mcp.tool()
def bulk_create_offers(offers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Bulk create offers (up to 25 at a time).
    
    Args:
        offers: List of offer objects to create
        
    Returns:
        Bulk create response
    """
    path = "/offer/bulk"
    return make_request("POST", path, data={"requests": offers})


@mcp.tool()
def get_inventory_item_group(inventory_item_group_id: str) -> Dict[str, Any]:
    """
    Get an inventory item group by ID.
    
    Args:
        inventory_item_group_id: Unique identifier of the inventory item group
        
    Returns:
        Inventory item group details
    """
    path = f"/inventory_item_group/{inventory_item_group_id}"
    return make_request("GET", path)


@mcp.tool()
def create_or_replace_inventory_item_group(
    inventory_item_group_id: str,
    items: List[Dict[str, Any]],
    group_by: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create or replace an inventory item group.
    
    Args:
        inventory_item_group_id: Unique identifier for the inventory item group
        items: List of inventory items in the group
        group_by: Attribute to group by (e.g., "color", "size")
        
    Returns:
        Inventory item group details
    """
    path = f"/inventory_item_group/{inventory_item_group_id}"
    
    body = {"items": items}
    if group_by:
        body["groupBy"] = group_by
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def delete_inventory_item_group(inventory_item_group_id: str) -> Dict[str, Any]:
    """
    Delete an inventory item group.
    
    Args:
        inventory_item_group_id: Unique identifier of the inventory item group
        
    Returns:
        Success response with status 204
    """
    path = f"/inventory_item_group/{inventory_item_group_id}"
    return make_request("DELETE", path)


@mcp.tool()
def publish_offer_by_inventory_item_group(inventory_item_group_id: str) -> Dict[str, Any]:
    """
    Publish all offers in an inventory item group (for multiple-variation listings).
    
    Args:
        inventory_item_group_id: Unique identifier of the inventory item group
        
    Returns:
        Publish response
    """
    path = f"/inventory_item_group/{inventory_item_group_id}/publish"
    return make_request("POST", path)


@mcp.tool()
def withdraw_offer_by_inventory_item_group(inventory_item_group_id: str) -> Dict[str, Any]:
    """
    Withdraw (unpublish) all offers in an inventory item group.
    
    Args:
        inventory_item_group_id: Unique identifier of the inventory item group
        
    Returns:
        Withdraw response
    """
    path = f"/inventory_item_group/{inventory_item_group_id}/withdraw"
    return make_request("POST", path)


# ============================================================================
# ACCOUNT API TOOLS
# ============================================================================

@mcp.tool()
def create_fulfillment_policy(
    name: str,
    description: Optional[str] = None,
    orderDispatchTime: Optional[Dict[str, Any]] = None,
    shippingCarrierCodes: Optional[List[str]] = None,
    shippingOption: Optional[List[Dict[str, Any]]] = None,
    domesticRateTable: Optional[str] = None,
    internationalRateTable: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new fulfillment policy.
    
    Args:
        name: Name of the fulfillment policy (required)
        description: Description of the policy
        orderDispatchTime: Order dispatch time settings
        shippingCarrierCodes: Shipping carrier codes
        shippingOption: Shipping option details
        domesticRateTable: Domestic rate table name
        internationalRateTable: International rate table name
        
    Returns:
        Created fulfillment policy details
    """
    path = "/fulfillment_policy"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if orderDispatchTime:
        body["orderDispatchTime"] = orderDispatchTime
    if shippingCarrierCodes:
        body["shippingCarrierCodes"] = shippingCarrierCodes
    if shippingOption:
        body["shippingOption"] = shippingOption
    if domesticRateTable:
        body["domesticRateTable"] = domesticRateTable
    if internationalRateTable:
        body["internationalRateTable"] = internationalRateTable
    
    return make_request("POST", path, data=body)


@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    """
    Get a fulfillment policy by ID.
    
    Args:
        fulfillment_policy_id: Unique identifier of the fulfillment policy
        
    Returns:
        Fulfillment policy details
    """
    path = f"/fulfillment_policy/{fulfillment_policy_id}"
    return make_request("GET", path)


@mcp.tool()
def list_fulfillment_policies() -> Dict[str, Any]:
    """
    List all fulfillment policies for the seller.
    
    Returns:
        Collection of fulfillment policies
    """
    path = "/fulfillment_policy"
    return make_request("GET", path)


@mcp.tool()
def update_fulfillment_policy(
    fulfillment_policy_id: str,
    name: str,
    description: Optional[str] = None,
    orderDispatchTime: Optional[Dict[str, Any]] = None,
    shippingCarrierCodes: Optional[List[str]] = None,
    shippingOption: Optional[List[Dict[str, Any]]] = None,
    domesticRateTable: Optional[str] = None,
    internationalRateTable: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update an existing fulfillment policy.
    
    Args:
        fulfillment_policy_id: Unique identifier of the fulfillment policy
        name: Name of the fulfillment policy
        description: Description of the policy
        orderDispatchTime: Order dispatch time settings
        shippingCarrierCodes: Shipping carrier codes
        shippingOption: Shipping option details
        domesticRateTable: Domestic rate table name
        internationalRateTable: International rate table name
        
    Returns:
        Updated fulfillment policy details
    """
    path = f"/fulfillment_policy/{fulfillment_policy_id}"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if orderDispatchTime:
        body["orderDispatchTime"] = orderDispatchTime
    if shippingCarrierCodes:
        body["shippingCarrierCodes"] = shippingCarrierCodes
    if shippingOption:
        body["shippingOption"] = shippingOption
    if domesticRateTable:
        body["domesticRateTable"] = domesticRateTable
    if internationalRateTable:
        body["internationalRateTable"] = internationalRateTable
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    """
    Delete a fulfillment policy.
    
    Args:
        fulfillment_policy_id: Unique identifier of the fulfillment policy
        
    Returns:
        Success response with status 204
    """
    path = f"/fulfillment_policy/{fulfillment_policy_id}"
    return make_request("DELETE", path)


@mcp.tool()
def get_fulfillment_policy_by_name(name: str) -> Dict[str, Any]:
    """
    Get a fulfillment policy by name.
    
    Args:
        name: Name of the fulfillment policy
        
    Returns:
        Fulfillment policy details
    """
    path = f"/fulfillment_policy/get_by_name?name={name}"
    return make_request("GET", path)


@mcp.tool()
def create_payment_policy(
    name: str,
    description: Optional[str] = None,
    payment_instructions: Optional[str] = None,
    payment_methods: Optional[List[str]] = None,
    accept_paypal: Optional[bool] = None,
    immediate_payment_required: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Create a new payment policy.
    
    Args:
        name: Name of the payment policy (required)
        description: Description of the policy
        payment_instructions: Payment instructions
        payment_methods: Accepted payment methods
        accept_paypal: Whether to accept PayPal
        immediate_payment_required: Whether immediate payment is required
        
    Returns:
        Created payment policy details
    """
    path = "/payment_policy"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if payment_instructions:
        body["paymentInstructions"] = payment_instructions
    if payment_methods:
        body["paymentMethods"] = payment_methods
    if accept_paypal is not None:
        body["acceptPayPal"] = accept_paypal
    if immediate_payment_required is not None:
        body["immediatePaymentRequired"] = immediate_payment_required
    
    return make_request("POST", path, data=body)


@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    """
    Get a payment policy by ID.
    
    Args:
        payment_policy_id: Unique identifier of the payment policy
        
    Returns:
        Payment policy details
    """
    path = f"/payment_policy/{payment_policy_id}"
    return make_request("GET", path)


@mcp.tool()
def list_payment_policies() -> Dict[str, Any]:
    """
    List all payment policies for the seller.
    
    Returns:
        Collection of payment policies
    """
    path = "/payment_policy"
    return make_request("GET", path)


@mcp.tool()
def update_payment_policy(
    payment_policy_id: str,
    name: str,
    description: Optional[str] = None,
    payment_instructions: Optional[str] = None,
    payment_methods: Optional[List[str]] = None,
    accept_paypal: Optional[bool] = None,
    immediate_payment_required: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Update an existing payment policy.
    
    Args:
        payment_policy_id: Unique identifier of the payment policy
        name: Name of the payment policy
        description: Description of the policy
        payment_instructions: Payment instructions
        payment_methods: Accepted payment methods
        accept_paypal: Whether to accept PayPal
        immediate_payment_required: Whether immediate payment is required
        
    Returns:
        Updated payment policy details
    """
    path = f"/payment_policy/{payment_policy_id}"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if payment_instructions:
        body["paymentInstructions"] = payment_instructions
    if payment_methods:
        body["paymentMethods"] = payment_methods
    if accept_paypal is not None:
        body["acceptPayPal"] = accept_paypal
    if immediate_payment_required is not None:
        body["immediatePaymentRequired"] = immediate_payment_required
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    """
    Delete a payment policy.
    
    Args:
        payment_policy_id: Unique identifier of the payment policy
        
    Returns:
        Success response with status 204
    """
    path = f"/payment_policy/{payment_policy_id}"
    return make_request("DELETE", path)


@mcp.tool()
def get_payment_policy_by_name(name: str) -> Dict[str, Any]:
    """
    Get a payment policy by name.
    
    Args:
        name: Name of the payment policy
        
    Returns:
        Payment policy details
    """
    path = f"/payment_policy/get_by_name?name={name}"
    return make_request("GET", path)


@mcp.tool()
def create_return_policy(
    name: str,
    description: Optional[str] = None,
    return_instructions: Optional[str] = None,
    return_type: Optional[str] = None,
    return_shipping_cost_payer: Optional[str] = None,
    refund_method: Optional[str] = None,
    refund_timing: Optional[str] = None,
    restocking_fee: Optional[Dict[str, Any]] = None,
    return_period: Optional[Dict[str, Any]] = None,
    return_condition: Optional[Dict[str, Any]] = None,
    return_item_required: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Create a new return policy.
    
    Args:
        name: Name of the return policy (required)
        description: Description of the policy
        return_instructions: Return instructions
        return_type: Type of return (MONEY_BACK, EXCHANGE, NO_RETURN)
        return_shipping_cost_payer: Who pays for return shipping
        refund_method: Refund method
        refund_timing: Refund timing
        restocking_fee: Restocking fee details
        return_period: Return period
        return_condition: Return condition requirements
        return_item_required: Whether return item is required
        
    Returns:
        Created return policy details
    """
    path = "/return_policy"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if return_instructions:
        body["returnInstructions"] = return_instructions
    if return_type:
        body["returnType"] = return_type
    if return_shipping_cost_payer:
        body["returnShippingCostPayer"] = return_shipping_cost_payer
    if refund_method:
        body["refundMethod"] = refund_method
    if refund_timing:
        body["refundTiming"] = refund_timing
    if restocking_fee:
        body["restockingFee"] = restocking_fee
    if return_period:
        body["returnPeriod"] = return_period
    if return_condition:
        body["returnCondition"] = return_condition
    if return_item_required is not None:
        body["returnItemRequired"] = return_item_required
    
    return make_request("POST", path, data=body)


@mcp.tool()
def get_return_policy(return_policy_id: str) -> Dict[str, Any]:
    """
    Get a return policy by ID.
    
    Args:
        return_policy_id: Unique identifier of the return policy
        
    Returns:
        Return policy details
    """
    path = f"/return_policy/{return_policy_id}"
    return make_request("GET", path)


@mcp.tool()
def list_return_policies() -> Dict[str, Any]:
    """
    List all return policies for the seller.
    
    Returns:
        Collection of return policies
    """
    path = "/return_policy"
    return make_request("GET", path)


@mcp.tool()
def update_return_policy(
    return_policy_id: str,
    name: str,
    description: Optional[str] = None,
    return_instructions: Optional[str] = None,
    return_type: Optional[str] = None,
    return_shipping_cost_payer: Optional[str] = None,
    refund_method: Optional[str] = None,
    refund_timing: Optional[str] = None,
    restocking_fee: Optional[Dict[str, Any]] = None,
    return_period: Optional[Dict[str, Any]] = None,
    return_condition: Optional[Dict[str, Any]] = None,
    return_item_required: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Update an existing return policy.
    
    Args:
        return_policy_id: Unique identifier of the return policy
        name: Name of the return policy
        description: Description of the policy
        return_instructions: Return instructions
        return_type: Type of return
        return_shipping_cost_payer: Who pays for return shipping
        refund_method: Refund method
        refund_timing: Refund timing
        restocking_fee: Restocking fee details
        return_period: Return period
        return_condition: Return condition requirements
        return_item_required: Whether return item is required
        
    Returns:
        Updated return policy details
    """
    path = f"/return_policy/{return_policy_id}"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if return_instructions:
        body["returnInstructions"] = return_instructions
    if return_type:
        body["returnType"] = return_type
    if return_shipping_cost_payer:
        body["returnShippingCostPayer"] = return_shipping_cost_payer
    if refund_method:
        body["refundMethod"] = refund_method
    if refund_timing:
        body["refundTiming"] = refund_timing
    if restocking_fee:
        body["restockingFee"] = restocking_fee
    if return_period:
        body["returnPeriod"] = return_period
    if return_condition:
        body["returnCondition"] = return_condition
    if return_item_required is not None:
        body["returnItemRequired"] = return_item_required
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def delete_return_policy(return_policy_id: str) -> Dict[str, Any]:
    """
    Delete a return policy.
    
    Args:
        return_policy_id: Unique identifier of the return policy
        
    Returns:
        Success response with status 204
    """
    path = f"/return_policy/{return_policy_id}"
    return make_request("DELETE", path)


@mcp.tool()
def get_return_policy_by_name(name: str) -> Dict[str, Any]:
    """
    Get a return policy by name.
    
    Args:
        name: Name of the return policy
        
    Returns:
        Return policy details
    """
    path = f"/return_policy/get_by_name?name={name}"
    return make_request("GET", path)


@mcp.tool()
def get_sales_tax(sales_tax_id: str) -> Dict[str, Any]:
    """
    Get a sales tax by ID.
    
    Args:
        sales_tax_id: Unique identifier of the sales tax
        
    Returns:
        Sales tax details
    """
    path = f"/sales_tax/{sales_tax_id}"
    return make_request("GET", path)


@mcp.tool()
def list_sales_taxes() -> Dict[str, Any]:
    """
    List all sales taxes for the seller.
    
    Returns:
        Collection of sales taxes
    """
    path = "/sales_tax"
    return make_request("GET", path)


@mcp.tool()
def create_or_replace_sales_tax(
    state_or_province: str,
    postal_code: Optional[str] = None,
    country_code: Optional[str] = None,
    tax_percentage: Optional[float] = None,
    tax_shipping: Optional[bool] = None,
    tax_on_subtotal: Optional[bool] = None,
    tax_on_shipping: Optional[bool] = None,
    tax_on_handling: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Create or replace a sales tax.
    
    Args:
        state_or_province: State or province name (required)
        postal_code: Postal code
        country_code: Country code
        tax_percentage: Tax percentage
        tax_shipping: Whether to tax shipping
        tax_on_subtotal: Whether to tax subtotal
        tax_on_shipping: Whether to tax shipping
        tax_on_handling: Whether to tax handling
        
    Returns:
        Sales tax details
    """
    path = "/sales_tax"
    
    body = {"stateOrProvince": state_or_province}
    if postal_code:
        body["postalCode"] = postal_code
    if country_code:
        body["countryCode"] = country_code
    if tax_percentage:
        body["taxPercentage"] = tax_percentage
    if tax_shipping is not None:
        body["taxShipping"] = tax_shipping
    if tax_on_subtotal is not None:
        body["taxOnSubtotal"] = tax_on_subtotal
    if tax_on_shipping is not None:
        body["taxOnShipping"] = tax_on_shipping
    if tax_on_handling is not None:
        body["taxOnHandling"] = tax_on_handling
    
    return make_request("POST", path, data=body)


@mcp.tool()
def delete_sales_tax(sales_tax_id: str) -> Dict[str, Any]:
    """
    Delete a sales tax.
    
    Args:
        sales_tax_id: Unique identifier of the sales tax
        
    Returns:
        Success response with status 204
    """
    path = f"/sales_tax/{sales_tax_id}"
    return make_request("DELETE", path)


@mcp.tool()
def create_custom_policy(
    policy_type: str,
    name: str,
    description: Optional[str] = None,
    custom_policy_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create a custom policy.
    
    Args:
        policy_type: Type of custom policy
        name: Name of the custom policy (required)
        description: Description of the policy
        custom_policy_data: Custom policy data
        
    Returns:
        Created custom policy details
    """
    path = f"/custom_policy/{policy_type}"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if custom_policy_data:
        body.update(custom_policy_data)
    
    return make_request("POST", path, data=body)


@mcp.tool()
def get_custom_policy(policy_type: str, custom_policy_id: str) -> Dict[str, Any]:
    """
    Get a custom policy by ID.
    
    Args:
        policy_type: Type of custom policy
        custom_policy_id: Unique identifier of the custom policy
        
    Returns:
        Custom policy details
    """
    path = f"/custom_policy/{policy_type}/{custom_policy_id}"
    return make_request("GET", path)


@mcp.tool()
def list_custom_policies(policy_type: str) -> Dict[str, Any]:
    """
    List custom policies by type.
    
    Args:
        policy_type: Type of custom policy
        
    Returns:
        Collection of custom policies
    """
    path = f"/custom_policy/{policy_type}"
    return make_request("GET", path)


@mcp.tool()
def update_custom_policy(
    policy_type: str,
    custom_policy_id: str,
    name: str,
    description: Optional[str] = None,
    custom_policy_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Update a custom policy.
    
    Args:
        policy_type: Type of custom policy
        custom_policy_id: Unique identifier of the custom policy
        name: Name of the custom policy
        description: Description of the policy
        custom_policy_data: Custom policy data
        
    Returns:
        Updated custom policy details
    """
    path = f"/custom_policy/{policy_type}/{custom_policy_id}"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if custom_policy_data:
        body.update(custom_policy_data)
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def get_opted_in_programs() -> Dict[str, Any]:
    """
    List programs the seller is opted into.
    
    Returns:
        Collection of opted-in programs
    """
    path = "/opted_in_program"
    return make_request("GET", path)


@mcp.tool()
def opt_in_to_program(program_name: str) -> Dict[str, Any]:
    """
    Opt into a program.
    
    Args:
        program_name: Name of the program to opt into
        
    Returns:
        Opt-in result
    """
    path = f"/opted_in_program/{program_name}"
    return make_request("POST", path)


@mcp.tool()
def opt_out_of_program(program_name: str) -> Dict[str, Any]:
    """
    Opt out of a program.
    
    Args:
        program_name: Name of the program to opt out of
        
    Returns:
        Opt-out result
    """
    path = f"/opted_in_program/{program_name}"
    return make_request("DELETE", path)


@mcp.tool()
def get_privileges() -> Dict[str, Any]:
    """
    Get seller privileges.
    
    Returns:
        Seller privileges details
    """
    path = "/privilege"
    return make_request("GET", path)


@mcp.tool()
def get_rate_tables() -> Dict[str, Any]:
    """
    Get available rate tables.
    
    Returns:
        Collection of rate tables
    """
    path = "/rate_table"
    return make_request("GET", path)


@mcp.tool()
def get_subscription() -> Dict[str, Any]:
    """
    Get seller subscription details.
    
    Returns:
        Subscription details
    """
    path = "/subscription"
    return make_request("GET", path)


# ============================================================================
# FULFILLMENT API TOOLS
# ============================================================================

@mcp.tool()
def get_order(order_id: str, field_groups: Optional[str] = None) -> Dict[str, Any]:
    """
    Get an order by ID.
    
    Args:
        order_id: Unique identifier of the order
        field_groups: Field groups to include (e.g., "TAX_BREAKDOWN")
        
    Returns:
        Order details
    """
    path = f"/order/{order_id}"
    params = {}
    if field_groups:
        params["fieldGroups"] = field_groups
    return make_request("GET", path, params=params)


@mcp.tool()
def list_orders(
    filter: Optional[str] = None,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    List orders with optional filters.
    
    Args:
        filter: Filter criteria (e.g., "creationdate:[2024-01-01T00:00:00.000Z..]")
        order_ids: Comma-separated list of order IDs
        field_groups: Field groups to include (e.g., "TAX_BREAKDOWN")
        limit: Maximum number of orders per page (max 200)
        offset: Number of orders to skip for pagination
        
    Returns:
        Collection of orders
    """
    path = "/order"
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    if field_groups:
        params["fieldGroups"] = field_groups
    return make_request("GET", path, params=params)


@mcp.tool()
def create_shipping_fulfillment(
    order_id: str,
    line_items: List[Dict[str, Any]],
    shipment_date: Optional[str] = None,
    shipping_note: Optional[str] = None,
    shipping_carrier_code: Optional[str] = None,
    tracking_number: Optional[str] = None,
    shipping_method: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a shipping fulfillment for an order.
    
    Args:
        order_id: Unique identifier of the order
        line_items: Line items to fulfill
        shipment_date: Date of shipment (ISO 8601 format)
        shipping_note: Shipping note
        shipping_carrier_code: Shipping carrier code
        tracking_number: Tracking number
        shipping_method: Shipping method
        
    Returns:
        Shipping fulfillment details
    """
    path = f"/order/{order_id}/shipping_fulfillment"
    
    body = {"lineItems": line_items}
    if shipment_date:
        body["shipmentDate"] = shipment_date
    if shipping_note:
        body["shippingNote"] = shipping_note
    if shipping_carrier_code:
        body["shippingCarrierCode"] = shipping_carrier_code
    if tracking_number:
        body["trackingNumber"] = tracking_number
    if shipping_method:
        body["shippingMethod"] = shipping_method
    
    return make_request("POST", path, data=body)


@mcp.tool()
def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    """
    Get a shipping fulfillment by order and fulfillment ID.
    
    Args:
        order_id: Unique identifier of the order
        fulfillment_id: Unique identifier of the fulfillment
        
    Returns:
        Shipping fulfillment details
    """
    path = f"/order/{order_id}/shipping_fulfillment/{fulfillment_id}"
    return make_request("GET", path)


@mcp.tool()
def list_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    """
    List shipping fulfillments for an order.
    
    Args:
        order_id: Unique identifier of the order
        
    Returns:
        Collection of shipping fulfillments
    """
    path = f"/order/{order_id}/shipping_fulfillment"
    return make_request("GET", path)


@mcp.tool()
def get_payment_dispute(dispute_id: str) -> Dict[str, Any]:
    """
    Get a payment dispute by ID.
    
    Args:
        dispute_id: Unique identifier of the payment dispute
        
    Returns:
        Payment dispute details
    """
    path = f"/payment_dispute/{dispute_id}"
    return make_request("GET", path)


@mcp.tool()
def list_payment_disputes() -> Dict[str, Any]:
    """
    List payment disputes for the seller.
    
    Returns:
        Collection of payment disputes
    """
    path = "/payment_dispute"
    return make_request("GET", path)


@mcp.tool()
def accept_payment_dispute(dispute_id: str, resolution: str) -> Dict[str, Any]:
    """
    Accept a payment dispute with a resolution.
    
    Args:
        dispute_id: Unique identifier of the payment dispute
        resolution: Resolution details
        
    Returns:
        Acceptance result
    """
    path = f"/payment_dispute/{dispute_id}/accept"
    return make_request("POST", path, data={"resolution": resolution})


@mcp.tool()
def contest_payment_dispute(
    dispute_id: str,
    dispute_evidence: List[Dict[str, Any]],
    response_to_buyer: Optional[str] = None
) -> Dict[str, Any]:
    """
    Contest a payment dispute.
    
    Args:
        dispute_id: Unique identifier of the payment dispute
        dispute_evidence: Evidence for the dispute
        response_to_buyer: Response to the buyer
        
    Returns:
        Contest result
    """
    path = f"/payment_dispute/{dispute_id}/contest"
    
    body = {"disputeEvidence": dispute_evidence}
    if response_to_buyer:
        body["responseToBuyer"] = response_to_buyer
    
    return make_request("POST", path, data=body)


@mcp.tool()
def add_evidence(dispute_id: str, evidence_type: str, evidence_value: str) -> Dict[str, Any]:
    """
    Add evidence to a payment dispute.
    
    Args:
        dispute_id: Unique identifier of the payment dispute
        evidence_type: Type of evidence
        evidence_value: Evidence value
        
    Returns:
        Evidence addition result
    """
    path = f"/payment_dispute/{dispute_id}/evidence"
    return make_request("POST", path, data={
        "evidenceType": evidence_type,
        "evidenceValue": evidence_value
    })


@mcp.tool()
def update_evidence(dispute_id: str, evidence_id: str, evidence_value: str) -> Dict[str, Any]:
    """
    Update evidence for a payment dispute.
    
    Args:
        dispute_id: Unique identifier of the payment dispute
        evidence_id: Unique identifier of the evidence
        evidence_value: Updated evidence value
        
    Returns:
        Evidence update result
    """
    path = f"/payment_dispute/{dispute_id}/evidence/{evidence_id}"
    return make_request("PUT", path, data={"evidenceValue": evidence_value})


@mcp.tool()
def fetch_evidence_content(dispute_id: str, evidence_id: str) -> Dict[str, Any]:
    """
    Fetch content of evidence for a payment dispute.
    
    Args:
        dispute_id: Unique identifier of the payment dispute
        evidence_id: Unique identifier of the evidence
        
    Returns:
        Evidence content
    """
    path = f"/payment_dispute/{dispute_id}/evidence/{evidence_id}/content"
    return make_request("GET", path)


@mcp.tool()
def upload_evidence_file(
    dispute_id: str,
    evidence_id: str,
    file_content: str,
    file_content_type: str
) -> Dict[str, Any]:
    """
    Upload evidence file for a payment dispute.
    
    Args:
        dispute_id: Unique identifier of the payment dispute
        evidence_id: Unique identifier of the evidence
        file_content: Base64-encoded file content
        file_content_type: MIME type of the file
        
    Returns:
        Upload result
    """
    path = f"/payment_dispute/{dispute_id}/evidence/{evidence_id}/upload"
    
    headers = {
        "Content-Type": file_content_type
    }
    
    return make_request("POST", path, data=file_content, headers=headers)


@mcp.tool()
def get_activities(order_id: str) -> Dict[str, Any]:
    """
    Get activities for an order.
    
    Args:
        order_id: Unique identifier of the order
        
    Returns:
        Collection of activities
    """
    path = f"/order/{order_id}/activity"
    return make_request("GET", path)


@mcp.tool()
def issue_refund(order_id: str, refund_details: Dict[str, Any]) -> Dict[str, Any]:
    """
    Issue a refund for an order.
    
    Args:
        order_id: Unique identifier of the order
        refund_details: Refund details (amount, reason, etc.)
        
    Returns:
        Refund result
    """
    path = f"/order/{order_id}/issue_refund"
    return make_request("POST", path, data=refund_details)


# ============================================================================
# FINANCES API TOOLS
# ============================================================================

@mcp.tool()
def get_payout(payout_id: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a payout by ID.
    
    Args:
        payout_id: Unique identifier of the payout
        marketplace_id: eBay marketplace ID
        
    Returns:
        Payout details
    """
    path = f"/payout/{payout_id}"
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", path, headers=headers)


@mcp.tool()
def list_payouts(
    creation_date_start: Optional[str] = None,
    creation_date_end: Optional[str] = None,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
    marketplace_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    List payouts with optional date filters.
    
    Args:
        creation_date_start: Start date for filtering (ISO 8601)
        creation_date_end: End date for filtering (ISO 8601)
        limit: Maximum number of payouts per page
        offset: Number of payouts to skip for pagination
        marketplace_id: eBay marketplace ID
        
    Returns:
        Collection of payouts
    """
    path = "/payout"
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    if creation_date_start:
        params["creationDate.start"] = creation_date_start
    if creation_date_end:
        params["creationDate.end"] = creation_date_end
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", path, params=params, headers=headers)


@mcp.tool()
def get_payout_summary(marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Get payout summary.
    
    Args:
        marketplace_id: eBay marketplace ID
        
    Returns:
        Payout summary
    """
    path = "/payout_summary"
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", path, headers=headers)


@mcp.tool()
def get_transaction_summary() -> Dict[str, Any]:
    """
    Get transaction summary.
    
    Returns:
        Transaction summary
    """
    path = "/transaction_summary"
    return make_request("GET", path)


@mcp.tool()
def list_transactions(
    creation_date_start: Optional[str] = None,
    creation_date_end: Optional[str] = None,
    transaction_type: Optional[str] = None,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    List transactions with optional filters.
    
    Args:
        creation_date_start: Start date for filtering (ISO 8601)
        creation_date_end: End date for filtering (ISO 8601)
        transaction_type: Type of transaction
        limit: Maximum number of transactions per page
        offset: Number of transactions to skip for pagination
        
    Returns:
        Collection of transactions
    """
    path = "/transaction"
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    if creation_date_start:
        params["creationDate.start"] = creation_date_start
    if creation_date_end:
        params["creationDate.end"] = creation_date_end
    if transaction_type:
        params["transactionType"] = transaction_type
    
    return make_request("GET", path, params=params)


@mcp.tool()
def get_seller_funds_summary() -> Dict[str, Any]:
    """
    Get seller funds summary.
    
    Returns:
        Seller funds summary
    """
    path = "/seller_funds_summary"
    return make_request("GET", path)


@mcp.tool()
def get_billing_activities() -> Dict[str, Any]:
    """
    Get billing activities.
    
    Returns:
        Collection of billing activities
    """
    path = "/billing_activity"
    return make_request("GET", path)


@mcp.tool()
def get_transfer(transfer_id: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a transfer by ID.
    
    Args:
        transfer_id: Unique identifier of the transfer
        marketplace_id: eBay marketplace ID
        
    Returns:
        Transfer details
    """
    path = f"/transfer/{transfer_id}"
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", path, headers=headers)


# ============================================================================
# MARKETING API TOOLS
# ============================================================================

@mcp.tool()
def get_campaign(campaign_id: str) -> Dict[str, Any]:
    """
    Get a campaign by ID.
    
    Args:
        campaign_id: Unique identifier of the campaign
        
    Returns:
        Campaign details
    """
    path = f"/ad_campaign/{campaign_id}"
    return make_request("GET", path)


@mcp.tool()
def list_campaigns() -> Dict[str, Any]:
    """
    List all campaigns for the seller.
    
    Returns:
        Collection of campaigns
    """
    path = "/ad_campaign"
    return make_request("GET", path)


@mcp.tool()
def create_campaign(
    name: str,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    daily_budget: Optional[Dict[str, Any]] = None,
    campaign_status: Optional[str] = None,
    campaign_type: Optional[str] = None,
    selection_rules: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create a new campaign.
    
    Args:
        name: Name of the campaign (required)
        start_time: Start time for the campaign (ISO 8601)
        end_time: End time for the campaign (ISO 8601)
        daily_budget: Daily budget details
        campaign_status: Status of the campaign
        campaign_type: Type of campaign
        selection_rules: Selection rules for the campaign
        
    Returns:
        Created campaign details
    """
    path = "/ad_campaign"
    
    body = {"name": name}
    if start_time:
        body["startTime"] = start_time
    if end_time:
        body["endTime"] = end_time
    if daily_budget:
        body["dailyBudget"] = daily_budget
    if campaign_status:
        body["campaignStatus"] = campaign_status
    if campaign_type:
        body["campaignType"] = campaign_type
    if selection_rules:
        body["selectionRules"] = selection_rules
    
    return make_request("POST", path, data=body)


@mcp.tool()
def update_campaign(
    campaign_id: str,
    name: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    daily_budget: Optional[Dict[str, Any]] = None,
    campaign_status: Optional[str] = None,
    selection_rules: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Update an existing campaign.
    
    Args:
        campaign_id: Unique identifier of the campaign
        name: Name of the campaign
        start_time: Start time for the campaign
        end_time: End time for the campaign
        daily_budget: Daily budget details
        campaign_status: Status of the campaign
        selection_rules: Selection rules for the campaign
        
    Returns:
        Updated campaign details
    """
    path = f"/ad_campaign/{campaign_id}"
    
    body = {}
    if name:
        body["name"] = name
    if start_time:
        body["startTime"] = start_time
    if end_time:
        body["endTime"] = end_time
    if daily_budget:
        body["dailyBudget"] = daily_budget
    if campaign_status:
        body["campaignStatus"] = campaign_status
    if selection_rules:
        body["selectionRules"] = selection_rules
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def delete_campaign(campaign_id: str) -> Dict[str, Any]:
    """
    Delete a campaign.
    
    Args:
        campaign_id: Unique identifier of the campaign
        
    Returns:
        Success response with status 204
    """
    path = f"/ad_campaign/{campaign_id}"
    return make_request("DELETE", path)


@mcp.tool()
def get_campaign_by_name(name: str) -> Dict[str, Any]:
    """
    Get a campaign by name.
    
    Args:
        name: Name of the campaign
        
    Returns:
        Campaign details
    """
    path = f"/ad_campaign/get_by_name?name={name}"
    return make_request("GET", path)


@mcp.tool()
def clone_campaign(campaign_id: str, new_name: str) -> Dict[str, Any]:
    """
    Clone a campaign.
    
    Args:
        campaign_id: Unique identifier of the campaign to clone
        new_name: Name for the cloned campaign
        
    Returns:
        Cloned campaign details
    """
    path = f"/ad_campaign/{campaign_id}/clone"
    return make_request("POST", path, data={"name": new_name})


@mcp.tool()
def get_ad(ad_id: str) -> Dict[str, Any]:
    """
    Get an ad by ID.
    
    Args:
        ad_id: Unique identifier of the ad
        
    Returns:
        Ad details
    """
    path = f"/ad/{ad_id}"
    return make_request("GET", path)


@mcp.tool()
def list_ads(
    campaign_id: Optional[str] = None,
    listing_id: Optional[str] = None,
    inventory_reference_id: Optional[str] = None,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    List ads with optional filters.
    
    Args:
        campaign_id: Filter by campaign ID
        listing_id: Filter by listing ID
        inventory_reference_id: Filter by inventory reference ID
        limit: Maximum number of ads per page
        offset: Number of ads to skip for pagination
        
    Returns:
        Collection of ads
    """
    path = "/ad"
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    if campaign_id:
        params["campaignId"] = campaign_id
    if listing_id:
        params["listingId"] = listing_id
    if inventory_reference_id:
        params["inventoryReferenceId"] = inventory_reference_id
    
    return make_request("GET", path, params=params)


@mcp.tool()
def get_ads_by_inventory_reference(
    inventory_reference_id: str,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    Get ads by inventory reference ID.
    
    Args:
        inventory_reference_id: Inventory reference ID
        limit: Maximum number of ads per page
        offset: Number of ads to skip for pagination
        
    Returns:
        Collection of ads
    """
    path = f"/ad/inventory_reference/{inventory_reference_id}"
    params = {
        "limit": str(limit),
        "offset": str(offset)
    }
    return make_request("GET", path, params=params)


@mcp.tool()
def create_ad_by_listing_id(
    campaign_id: str,
    listing_id: str,
    bid: Optional[float] = None
) -> Dict[str, Any]:
    """
    Create an ad by listing ID.
    
    Args:
        campaign_id: Unique identifier of the campaign
        listing_id: eBay listing ID
        bid: Bid amount for the ad
        
    Returns:
        Created ad details
    """
    path = "/ad"
    return make_request("POST", path, data={
        "campaignId": campaign_id,
        "listingId": listing_id,
        "bid": bid
    })


@mcp.tool()
def create_ads_by_inventory_reference(
    campaign_id: str,
    inventory_references: List[Dict[str, Any]],
    bid: Optional[float] = None
) -> Dict[str, Any]:
    """
    Create ads by inventory reference (up to 50 at a time).
    
    Args:
        campaign_id: Unique identifier of the campaign
        inventory_references: List of inventory reference objects
        bid: Bid amount for the ads
        
    Returns:
        Created ads details
    """
    path = "/ad/bulk"
    return make_request("POST", path, data={
        "campaignId": campaign_id,
        "inventoryReferences": inventory_references,
        "bid": bid
    })


@mcp.tool()
def update_ad_bid(ad_id: str, bid: float) -> Dict[str, Any]:
    """
    Update the bid for an ad.
    
    Args:
        ad_id: Unique identifier of the ad
        bid: New bid amount
        
    Returns:
        Updated ad details
    """
    path = f"/ad/{ad_id}/bid"
    return make_request("PUT", path, data={"bid": bid})


@mcp.tool()
def update_ads_bid_by_listing_id(
    campaign_id: str,
    listing_ids: List[str],
    bid: float
) -> Dict[str, Any]:
    """
    Update bids for multiple ads by listing ID.
    
    Args:
        campaign_id: Unique identifier of the campaign
        listing_ids: List of listing IDs
        bid: New bid amount
        
    Returns:
        Updated ads details
    """
    path = "/ad/bulk/bid"
    return make_request("PUT", path, data={
        "campaignId": campaign_id,
        "listingIds": listing_ids,
        "bid": bid
    })


@mcp.tool()
def update_ads_bid_by_inventory_reference(
    campaign_id: str,
    inventory_reference_ids: List[str],
    bid: float
) -> Dict[str, Any]:
    """
    Update bids for multiple ads by inventory reference.
    
    Args:
        campaign_id: Unique identifier of the campaign
        inventory_reference_ids: List of inventory reference IDs
        bid: New bid amount
        
    Returns:
        Updated ads details
    """
    path = "/ad/bulk/bid/inventory_reference"
    return make_request("PUT", path, data={
        "campaignId": campaign_id,
        "inventoryReferenceIds": inventory_reference_ids,
        "bid": bid
    })


@mcp.tool()
def update_ad_status(ad_id: str, status: str) -> Dict[str, Any]:
    """
    Update the status of an ad.
    
    Args:
        ad_id: Unique identifier of the ad
        status: New status for the ad
        
    Returns:
        Updated ad details
    """
    path = f"/ad/{ad_id}/status"
    return make_request("PUT", path, data={"status": status})


@mcp.tool()
def update_ads_status_by_listing_id(
    campaign_id: str,
    listing_ids: List[str],
    status: str
) -> Dict[str, Any]:
    """
    Update statuses for multiple ads by listing ID.
    
    Args:
        campaign_id: Unique identifier of the campaign
        listing_ids: List of listing IDs
        status: New status for the ads
        
    Returns:
        Updated ads details
    """
    path = "/ad/bulk/status"
    return make_request("PUT", path, data={
        "campaignId": campaign_id,
        "listingIds": listing_ids,
        "status": status
    })


@mcp.tool()
def delete_ad(ad_id: str) -> Dict[str, Any]:
    """
    Delete an ad.
    
    Args:
        ad_id: Unique identifier of the ad
        
    Returns:
        Success response with status 204
    """
    path = f"/ad/{ad_id}"
    return make_request("DELETE", path)


@mcp.tool()
def delete_ads_by_listing_id(
    campaign_id: str,
    listing_ids: List[str]
) -> Dict[str, Any]:
    """
    Delete multiple ads by listing ID.
    
    Args:
        campaign_id: Unique identifier of the campaign
        listing_ids: List of listing IDs
        
    Returns:
        Deletion result
    """
    path = "/ad/bulk"
    return make_request("DELETE", path, data={
        "campaignId": campaign_id,
        "listingIds": listing_ids
    })


@mcp.tool()
def delete_ads_by_inventory_reference(
    campaign_id: str,
    inventory_reference_ids: List[str]
) -> Dict[str, Any]:
    """
    Delete multiple ads by inventory reference.
    
    Args:
        campaign_id: Unique identifier of the campaign
        inventory_reference_ids: List of inventory reference IDs
        
    Returns:
        Deletion result
    """
    path = "/ad/bulk/inventory_reference"
    return make_request("DELETE", path, data={
        "campaignId": campaign_id,
        "inventoryReferenceIds": inventory_reference_ids
    })


@mcp.tool()
def update_ad_group(ad_group_id: str, name: Optional[str] = None, 
                   description: Optional[str] = None) -> Dict[str, Any]:
    """
    Update an ad group.
    
    Args:
        ad_group_id: Unique identifier of the ad group
        name: New name for the ad group
        description: New description for the ad group
        
    Returns:
        Updated ad group details
    """
    path = f"/ad_group/{ad_group_id}"
    
    body = {}
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    
    return make_request("PUT", path, data=body)


@mcp.tool()
def get_ad_group(ad_group_id: str) -> Dict[str, Any]:
    """
    Get an ad group by ID.
    
    Args:
        ad_group_id: Unique identifier of the ad group
        
    Returns:
        Ad group details
    """
    path = f"/ad_group/{ad_group_id}"
    return make_request("GET", path)


@mcp.tool()
def list_ad_groups() -> Dict[str, Any]:
    """
    List all ad groups for the seller.
    
    Returns:
        Collection of ad groups
    """
    path = "/ad_group"
    return make_request("GET", path)


@mcp.tool()
def create_ad_group(
    name: str,
    description: Optional[str] = None,
    campaign_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new ad group.
    
    Args:
        name: Name of the ad group (required)
        description: Description of the ad group
        campaign_id: ID of the campaign to add the ad group to
        
    Returns:
        Created ad group details
    """
    path = "/ad_group"
    
    body = {"name": name}
    if description:
        body["description"] = description
    if campaign_id:
        body["campaignId"] = campaign_id
    
    return make_request("POST", path, data=body)


@mcp.tool()
def suggest_budget() -> Dict[str, Any]:
    """
    Suggest a campaign budget.
    
    Returns:
        Budget suggestion
    """
    path = "/marketing/suggest_budget"
    return make_request("GET", path)


@mcp.tool()
def suggest_bids(campaign_id: str) -> Dict[str, Any]:
    """
    Suggest bid amounts for a campaign.
    
    Args:
        campaign_id: Unique identifier of the campaign
        
    Returns:
        Bid suggestions
    """
    path = f"/marketing/suggest_bid?campaignId={campaign_id}"
    return make_request("GET", path)


@mcp.tool()
def suggest_keywords(campaign_id: str) -> Dict[str, Any]:
    """
    Suggest keywords for a campaign.
    
    Args:
        campaign_id: Unique identifier of the campaign
        
    Returns:
        Keyword suggestions
    """
    path = f"/marketing/suggest_keyword?campaignId={campaign_id}"
    return make_request("GET", path)


@mcp.tool()
def update_item_promotion(
    item_promotion_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    promotion_type: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    discount: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Update an item promotion.
    
    Args:
        item_promotion_id: Unique identifier of the item promotion
        name: Name of the item promotion
        description: Description of the promotion
        promotion_type