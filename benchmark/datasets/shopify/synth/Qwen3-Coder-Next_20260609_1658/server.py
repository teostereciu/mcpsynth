#!/usr/bin/env python3
"""
Shopify Admin REST API MCP Server

This server provides tools for interacting with the Shopify Admin REST API
using the Model Context Protocol (MCP).
"""

import os
import json
import requests
from typing import Any, Dict, Optional, List

# Initialize FastMCP server
from fastmcp import FastMCP

app = FastMCP(
    name="shopify-admin",
    version="1.0.0",
    description="Shopify Admin REST API server for managing products, orders, customers, inventory, and more"
)

# Base URL for Shopify Admin API
SHOPIFY_BASE_URL = os.environ.get(
    "SHOPIFY_BASE_URL",
    "https://{store_url}/admin/api/2026-01"
)

def get_auth_headers() -> Dict[str, str]:
    """Get authentication headers for Shopify API."""
    access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": access_token
    }
    
    return headers, store_url

def build_url(path: str, store_url: str) -> str:
    """Build a Shopify API URL."""
    base = f"https://{store_url}/admin/api/2026-01"
    if not path.startswith("/"):
        path = "/" + path
    return base + path

def make_request(method: str, endpoint: str, data: Optional[Dict] = None, 
                 params: Optional[Dict] = None) -> Dict:
    """Make a request to the Shopify API."""
    headers, store_url = get_auth_headers()
    
    if not store_url:
        return {"error": "SHOPIFY_STORE_URL environment variable is not set"}
    if not headers.get("X-Shopify-Access-Token"):
        return {"error": "SHOPIFY_ACCESS_TOKEN environment variable is not set"}
    
    url = build_url(endpoint, store_url)
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=data, params=params, timeout=30)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=data, params=params, timeout=30)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        
        # Try to parse JSON response
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"raw_response": response.text}
            
    except requests.exceptions.HTTPError as e:
        error_msg = {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
        try:
            error_data = e.response.json()
            error_msg["details"] = error_data
        except json.JSONDecodeError:
            pass
        return error_msg
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# =============================================================================
# Product Operations
# =============================================================================

@app.tool()
def create_product(
    title: str,
    body_html: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    tags: Optional[str] = None,
    status: Optional[str] = "draft",
    published_at: Optional[str] = None,
    variants: Optional[List[Dict]] = None,
    images: Optional[List[Dict]] = None
) -> Dict:
    """
    Create a new product in Shopify.
    
    Args:
        title: The name of the product (required)
        body_html: A description of the product with HTML formatting
        vendor: The name of the product's vendor
        product_type: A categorization for the product
        tags: Comma-separated tags for filtering and search
        status: Product status ('active', 'draft', 'archived')
        published_at: ISO 8601 date when the product should be published
        variants: Array of product variant objects
        images: Array of product image objects
        
    Returns:
        Dict containing the created product or error information
    """
    product_data = {"title": title}
    
    if body_html:
        product_data["body_html"] = body_html
    if vendor:
        product_data["vendor"] = vendor
    if product_type:
        product_data["product_type"] = product_type
    if tags:
        product_data["tags"] = tags
    if status:
        product_data["status"] = status
    if published_at:
        product_data["published_at"] = published_at
    if variants:
        product_data["variants"] = variants
    if images:
        product_data["images"] = images
    
    return make_request("POST", "/products.json", {"product": product_data})

@app.tool()
def list_products(
    limit: int = 50,
    page: int = 1,
    ids: Optional[str] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
    status: Optional[str] = "active",
    published_status: Optional[str] = "published"
) -> Dict:
    """
    Retrieve a list of products.
    
    Args:
        limit: Number of products to retrieve (max 250)
        page: Page number for pagination
        ids: Comma-separated list of product IDs
        title: Filter by product title
        vendor: Filter by vendor
        product_type: Filter by product type
        created_at_min: Filter products created after this date
        created_at_max: Filter products created before this date
        updated_at_min: Filter products updated after this date
        updated_at_max: Filter products updated before this date
        published_at_min: Filter products published after this date
        published_at_max: Filter products published before this date
        status: Filter by status ('active', 'draft', 'archived')
        published_status: Filter by published status ('published', 'unpublished')
        
    Returns:
        Dict containing the list of products or error information
    """
    params = {"limit": limit, "page": page}
    
    if ids:
        params["ids"] = ids
    if title:
        params["title"] = title
    if vendor:
        params["vendor"] = vendor
    if product_type:
        params["product_type"] = product_type
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    if published_at_min:
        params["published_at_min"] = published_at_min
    if published_at_max:
        params["published_at_max"] = published_at_max
    if status:
        params["status"] = status
    if published_status:
        params["published_status"] = published_status
    
    return make_request("GET", "/products.json", params=params)

@app.tool()
def get_product(product_id: int) -> Dict:
    """
    Retrieve a single product by its ID.
    
    Args:
        product_id: The ID of the product to retrieve
        
    Returns:
        Dict containing the product or error information
    """
    return make_request("GET", f"/products/{product_id}.json")

@app.tool()
def update_product(
    product_id: int,
    title: Optional[str] = None,
    body_html: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    tags: Optional[str] = None,
    status: Optional[str] = None,
    published_at: Optional[str] = None
) -> Dict:
    """
    Update an existing product.
    
    Args:
        product_id: The ID of the product to update
        title: Updated product name
        body_html: Updated description with HTML formatting
        vendor: Updated vendor name
        product_type: Updated product type
        tags: Updated comma-separated tags
        status: Updated status ('active', 'draft', 'archived')
        published_at: Updated ISO 8601 publication date
        
    Returns:
        Dict containing the updated product or error information
    """
    product_data = {}
    
    if title:
        product_data["title"] = title
    if body_html:
        product_data["body_html"] = body_html
    if vendor:
        product_data["vendor"] = vendor
    if product_type:
        product_data["product_type"] = product_type
    if tags:
        product_data["tags"] = tags
    if status:
        product_data["status"] = status
    if published_at:
        product_data["published_at"] = published_at
    
    return make_request("PUT", f"/products/{product_id}.json", {"product": product_data})

@app.tool()
def delete_product(product_id: int) -> Dict:
    """
    Delete a product by its ID.
    
    Args:
        product_id: The ID of the product to delete
        
    Returns:
        Dict containing the deletion result or error information
    """
    return make_request("DELETE", f"/products/{product_id}.json")

@app.tool()
def create_product_variant(
    product_id: int,
    title: str,
    price: Optional[str] = None,
    sku: Optional[str] = None,
    position: Optional[int] = None,
    inventory_policy: Optional[str] = None,
    compare_at_price: Optional[str] = None,
    fulfillment_service: Optional[str] = None,
    inventory_management: Optional[str] = None,
    option1: Optional[str] = None,
    option2: Optional[str] = None,
    option3: Optional[str] = None,
    tax_code: Optional[str] = None,
    requires_shipping: Optional[bool] = None,
    grams: Optional[int] = None,
    weight: Optional[float] = None,
    weight_unit: Optional[str] = None,
    barcode: Optional[str] = None,
    ean: Optional[str] = None,
    isbn: Optional[str] = None,
    upc: Optional[str] = None,
    image_id: Optional[int] = None,
    inventory_item_id: Optional[int] = None,
    inventory_quantity: Optional[int] = None,
    old_inventory_quantity: Optional[int] = None
) -> Dict:
    """
    Create a new product variant.
    
    Args:
        product_id: The ID of the product to add the variant to
        title: The variant name
        price: The price of the variant
        sku: The SKU (stock keeping unit) for the variant
        position: The position of the variant in the list
        inventory_policy: Whether to continue selling when out of stock ('deny' or 'continue')
        compare_at_price: The original price before discount
        fulfillment_service: The fulfillment service handling this variant
        inventory_management: Which service tracks inventory ('shopify', 'null', or fulfillment service handle)
        option1: First option value (e.g., 'Small', 'Red')
        option2: Second option value
        option3: Third option value
        tax_code: Tax code for the variant
        requires_shipping: Whether the item requires shipping
        grams: Weight in grams
        weight: Weight value
        weight_unit: Unit of weight ('g', 'kg', 'oz', 'lb')
        barcode: Barcode, UPC, or ISBN number
        ean: EAN number
        isbn: ISBN number
        upc: UPC number
        image_id: ID of the associated product image
        inventory_item_id: ID of the inventory item
        inventory_quantity: Current inventory quantity
        old_inventory_quantity: Previous inventory quantity
        
    Returns:
        Dict containing the created variant or error information
    """
    variant_data = {"product_id": product_id, "title": title}
    
    if price:
        variant_data["price"] = price
    if sku:
        variant_data["sku"] = sku
    if position:
        variant_data["position"] = position
    if inventory_policy:
        variant_data["inventory_policy"] = inventory_policy
    if compare_at_price:
        variant_data["compare_at_price"] = compare_at_price
    if fulfillment_service:
        variant_data["fulfillment_service"] = fulfillment_service
    if inventory_management:
        variant_data["inventory_management"] = inventory_management
    if option1:
        variant_data["option1"] = option1
    if option2:
        variant_data["option2"] = option2
    if option3:
        variant_data["option3"] = option3
    if tax_code:
        variant_data["tax_code"] = tax_code
    if requires_shipping is not None:
        variant_data["requires_shipping"] = requires_shipping
    if grams:
        variant_data["grams"] = grams
    if weight:
        variant_data["weight"] = weight
    if weight_unit:
        variant_data["weight_unit"] = weight_unit
    if barcode:
        variant_data["barcode"] = barcode
    if ean:
        variant_data["ean"] = ean
    if isbn:
        variant_data["isbn"] = isbn
    if upc:
        variant_data["upc"] = upc
    if image_id:
        variant_data["image_id"] = image_id
    if inventory_item_id:
        variant_data["inventory_item_id"] = inventory_item_id
    if inventory_quantity is not None:
        variant_data["inventory_quantity"] = inventory_quantity
    if old_inventory_quantity is not None:
        variant_data["old_inventory_quantity"] = old_inventory_quantity
    
    return make_request("POST", f"/products/{product_id}/variants.json", {"variant": variant_data})

@app.tool()
def list_product_variants(product_id: int) -> Dict:
    """
    Retrieve a list of variants for a product.
    
    Args:
        product_id: The ID of the product
        
    Returns:
        Dict containing the list of variants or error information
    """
    return make_request("GET", f"/products/{product_id}/variants.json")

@app.tool()
def get_product_variant(variant_id: int) -> Dict:
    """
    Retrieve a single product variant by its ID.
    
    Args:
        variant_id: The ID of the variant to retrieve
        
    Returns:
        Dict containing the variant or error information
    """
    return make_request("GET", f"/variants/{variant_id}.json")

@app.tool()
def update_product_variant(
    variant_id: int,
    title: Optional[str] = None,
    price: Optional[str] = None,
    sku: Optional[str] = None,
    position: Optional[int] = None,
    inventory_policy: Optional[str] = None,
    compare_at_price: Optional[str] = None,
    fulfillment_service: Optional[str] = None,
    inventory_management: Optional[str] = None,
    option1: Optional[str] = None,
    option2: Optional[str] = None,
    option3: Optional[str] = None,
    tax_code: Optional[str] = None,
    requires_shipping: Optional[bool] = None,
    grams: Optional[int] = None,
    weight: Optional[float] = None,
    weight_unit: Optional[str] = None,
    barcode: Optional[str] = None,
    image_id: Optional[int] = None
) -> Dict:
    """
    Update an existing product variant.
    
    Args:
        variant_id: The ID of the variant to update
        title: Updated variant name
        price: Updated price
        sku: Updated SKU
        position: Updated position
        inventory_policy: Updated inventory policy
        compare_at_price: Updated compare-at price
        fulfillment_service: Updated fulfillment service
        inventory_management: Updated inventory management
        option1: Updated first option value
        option2: Updated second option value
        option3: Updated third option value
        tax_code: Updated tax code
        requires_shipping: Updated shipping requirement
        grams: Updated weight in grams
        weight: Updated weight
        weight_unit: Updated weight unit
        barcode: Updated barcode
        image_id: Updated image ID
        
    Returns:
        Dict containing the updated variant or error information
    """
    variant_data = {}
    
    if title:
        variant_data["title"] = title
    if price:
        variant_data["price"] = price
    if sku:
        variant_data["sku"] = sku
    if position:
        variant_data["position"] = position
    if inventory_policy:
        variant_data["inventory_policy"] = inventory_policy
    if compare_at_price:
        variant_data["compare_at_price"] = compare_at_price
    if fulfillment_service:
        variant_data["fulfillment_service"] = fulfillment_service
    if inventory_management:
        variant_data["inventory_management"] = inventory_management
    if option1:
        variant_data["option1"] = option1
    if option2:
        variant_data["option2"] = option2
    if option3:
        variant_data["option3"] = option3
    if tax_code:
        variant_data["tax_code"] = tax_code
    if requires_shipping is not None:
        variant_data["requires_shipping"] = requires_shipping
    if grams:
        variant_data["grams"] = grams
    if weight:
        variant_data["weight"] = weight
    if weight_unit:
        variant_data["weight_unit"] = weight_unit
    if barcode:
        variant_data["barcode"] = barcode
    if image_id:
        variant_data["image_id"] = image_id
    
    return make_request("PUT", f"/variants/{variant_id}.json", {"variant": variant_data})

@app.tool()
def delete_product_variant(product_id: int, variant_id: int) -> Dict:
    """
    Delete a product variant.
    
    Args:
        product_id: The ID of the product
        variant_id: The ID of the variant to delete
        
    Returns:
        Dict containing the deletion result or error information
    """
    return make_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")

# =============================================================================
# Order Operations
# =============================================================================

@app.tool()
def create_order(
    line_items: List[Dict],
    shipping_address: Optional[Dict] = None,
    billing_address: Optional[Dict] = None,
    email: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    note: Optional[str] = None,
    note_attributes: Optional[List[Dict]] = None,
    customer: Optional[Dict] = None,
    metafields: Optional[List[Dict]] = None
) -> Dict:
    """
    Create a new order.
    
    Args:
        line_items: Array of line item objects (required)
        shipping_address: Shipping address object
        billing_address: Billing address object
        email: Customer email address
        financial_status: Payment status ('pending', 'authorized', 'paid', 'refunded', 'voided')
        fulfillment_status: Fulfillment status ('fulfilled', 'partial', 'unfulfilled', 'unknown', 'restocked')
        note: Order note
        note_attributes: Custom order attributes as key-value pairs
        customer: Customer information
        metafields: Metafield objects to attach to the order
        
    Returns:
        Dict containing the created order or error information
    """
    order_data = {"line_items": line_items}
    
    if shipping_address:
        order_data["shipping_address"] = shipping_address
    if billing_address:
        order_data["billing_address"] = billing_address
    if email:
        order_data["email"] = email
    if financial_status:
        order_data["financial_status"] = financial_status
    if fulfillment_status:
        order_data["fulfillment_status"] = fulfillment_status
    if note:
        order_data["note"] = note
    if note_attributes:
        order_data["note_attributes"] = note_attributes
    if customer:
        order_data["customer"] = customer
    if metafields:
        order_data["metafields"] = metafields
    
    return make_request("POST", "/orders.json", {"order": order_data})

@app.tool()
def list_orders(
    limit: int = 50,
    page: int = 1,
    status: str = "any",
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    name: Optional[str] = None,
    customer_id: Optional[int] = None
) -> Dict:
    """
    Retrieve a list of orders.
    
    Args:
        limit: Number of orders to retrieve (max 250)
        page: Page number for pagination
        status: Order status ('open', 'closed', 'cancelled', 'any')
        financial_status: Payment status ('pending', 'authorized', 'paid', 'refunded', 'voided', 'any')
        fulfillment_status: Fulfillment status ('fulfilled', 'partial', 'unfulfilled', 'unknown', 'restocked', 'any')
        created_at_min: Filter orders created after this date
        created_at_max: Filter orders created before this date
        updated_at_min: Filter orders updated after this date
        updated_at_max: Filter orders updated before this date
        processed_at_min: Filter orders processed after this date
        processed_at_max: Filter orders processed before this date
        name: Filter by order name
        customer_id: Filter by customer ID
        
    Returns:
        Dict containing the list of orders or error information
    """
    params = {"limit": limit, "page": page, "status": status}
    
    if financial_status:
        params["financial_status"] = financial_status
    if fulfillment_status:
        params["fulfillment_status"] = fulfillment_status
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    if processed_at_min:
        params["processed_at_min"] = processed_at_min
    if processed_at_max:
        params["processed_at_max"] = processed_at_max
    if name:
        params["name"] = name
    if customer_id:
        params["customer_id"] = customer_id
    
    return make_request("GET", "/orders.json", params=params)

@app.tool()
def get_order(order_id: int) -> Dict:
    """
    Retrieve a single order by its ID.
    
    Args:
        order_id: The ID of the order to retrieve
        
    Returns:
        Dict containing the order or error information
    """
    return make_request("GET", f"/orders/{order_id}.json")

@app.tool()
def update_order(
    order_id: int,
    shipping_address: Optional[Dict] = None,
    billing_address: Optional[Dict] = None,
    email: Optional[str] = None,
    note: Optional[str] = None,
    customer: Optional[Dict] = None,
    line_items: Optional[List[Dict]] = None
) -> Dict:
    """
    Update an existing order.
    
    Args:
        order_id: The ID of the order to update
        shipping_address: Updated shipping address
        billing_address: Updated billing address
        email: Updated email address
        note: Updated order note
        customer: Updated customer information
        line_items: Updated line items
        
    Returns:
        Dict containing the updated order or error information
    """
    order_data = {}
    
    if shipping_address:
        order_data["shipping_address"] = shipping_address
    if billing_address:
        order_data["billing_address"] = billing_address
    if email:
        order_data["email"] = email
    if note:
        order_data["note"] = note
    if customer:
        order_data["customer"] = customer
    if line_items:
        order_data["line_items"] = line_items
    
    return make_request("PUT", f"/orders/{order_id}.json", {"order": order_data})

@app.tool()
def cancel_order(order_id: int, reason: Optional[str] = None) -> Dict:
    """
    Cancel an order.
    
    Args:
        order_id: The ID of the order to cancel
        reason: Reason for cancellation ('customer', 'fraud', 'inventory', 'declined', 'other')
        
    Returns:
        Dict containing the cancelled order or error information
    """
    data = {}
    if reason:
        data["reason"] = reason
    
    return make_request("POST", f"/orders/{order_id}/cancel.json", data)

@app.tool()
def close_order(order_id: int) -> Dict:
    """
    Close an order.
    
    Args:
        order_id: The ID of the order to close
        
    Returns:
        Dict containing the closed order or error information
    """
    return make_request("POST", f"/orders/{order_id}/close.json")

@app.tool()
def open_order(order_id: int) -> Dict:
    """
    Re-open a closed order.
    
    Args:
        order_id: The ID of the order to re-open
        
    Returns:
        Dict containing the reopened order or error information
    """
    return make_request("POST", f"/orders/{order_id}/open.json")

# =============================================================================
# Customer Operations
# =============================================================================

@app.tool()
def create_customer(
    first_name: str,
    last_name: str,
    email: str,
    phone: Optional[str] = None,
    addresses: Optional[List[Dict]] = None,
    note: Optional[str] = None,
    verified_email: Optional[bool] = None,
    metafields: Optional[List[Dict]] = None
) -> Dict:
    """
    Create a new customer.
    
    Args:
        first_name: Customer's first name
        last_name: Customer's last name
        email: Customer's email address (required, unique)
        phone: Customer's phone number
        addresses: Array of customer address objects
        note: Customer note
        verified_email: Whether the email is verified
        metafields: Metafield objects to attach to the customer
        
    Returns:
        Dict containing the created customer or error information
    """
    customer_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    
    if phone:
        customer_data["phone"] = phone
    if addresses:
        customer_data["addresses"] = addresses
    if note:
        customer_data["note"] = note
    if verified_email is not None:
        customer_data["verified_email"] = verified_email
    if metafields:
        customer_data["metafields"] = metafields
    
    return make_request("POST", "/customers.json", {"customer": customer_data})

@app.tool()
def list_customers(
    limit: int = 50,
    page: int = 1,
    ids: Optional[str] = None,
    since_id: Optional[int] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    name: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None
) -> Dict:
    """
    Retrieve a list of customers.
    
    Args:
        limit: Number of customers to retrieve (max 250)
        page: Page number for pagination
        ids: Comma-separated list of customer IDs
        since_id: Filter customers with ID greater than this value
        email: Filter by email address
        phone: Filter by phone number
        name: Filter by customer name
        created_at_min: Filter customers created after this date
        created_at_max: Filter customers created before this date
        updated_at_min: Filter customers updated after this date
        updated_at_max: Filter customers updated before this date
        
    Returns:
        Dict containing the list of customers or error information
    """
    params = {"limit": limit, "page": page}
    
    if ids:
        params["ids"] = ids
    if since_id:
        params["since_id"] = since_id
    if email:
        params["email"] = email
    if phone:
        params["phone"] = phone
    if name:
        params["name"] = name
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    
    return make_request("GET", "/customers.json", params=params)

@app.tool()
def get_customer(customer_id: int) -> Dict:
    """
    Retrieve a single customer by its ID.
    
    Args:
        customer_id: The ID of the customer to retrieve
        
    Returns:
        Dict containing the customer or error information
    """
    return make_request("GET", f"/customers/{customer_id}.json")

@app.tool()
def update_customer(
    customer_id: int,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    note: Optional[str] = None,
    addresses: Optional[List[Dict]] = None
) -> Dict:
    """
    Update an existing customer.
    
    Args:
        customer_id: The ID of the customer to update
        first_name: Updated first name
        last_name: Updated last name
        email: Updated email address
        phone: Updated phone number
        note: Updated note
        addresses: Updated addresses array
        
    Returns:
        Dict containing the updated customer or error information
    """
    customer_data = {}
    
    if first_name:
        customer_data["first_name"] = first_name
    if last_name:
        customer_data["last_name"] = last_name
    if email:
        customer_data["email"] = email
    if phone:
        customer_data["phone"] = phone
    if note:
        customer_data["note"] = note
    if addresses:
        customer_data["addresses"] = addresses
    
    return make_request("PUT", f"/customers/{customer_id}.json", {"customer": customer_data})

@app.tool()
def search_customers(
    query: str,
    limit: int = 50,
    page: int = 1
) -> Dict:
    """
    Search for customers by query.
    
    Args:
        query: Search query (e.g., 'email:customer@example.com', 'phone:+1234567890', 'name:John')
        limit: Number of results to retrieve (max 250)
        page: Page number for pagination
        
    Returns:
        Dict containing the search results or error information
    """
    params = {"query": query, "limit": limit, "page": page}
    
    return make_request("GET", "/customers/search.json", params=params)

@app.tool()
def create_customer_address(
    customer_id: int,
    address1: str,
    city: str,
    province: str,
    country: str,
    zip: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    company: Optional[str] = None,
    default: Optional[bool] = None
) -> Dict:
    """
    Create a new customer address.
    
    Args:
        customer_id: The ID of the customer
        address1: First line of the address
        city: City name
        province: Province/state
        country: Country name
        zip: ZIP/postal code
        first_name: First name for the address
        last_name: Last name for the address
        phone: Phone number
        company: Company name
        default: Whether this is the default address
        
    Returns:
        Dict containing the created address or error information
    """
    address_data = {
        "address1": address1,
        "city": city,
        "province": province,
        "country": country,
        "zip": zip
    }
    
    if first_name:
        address_data["first_name"] = first_name
    if last_name:
        address_data["last_name"] = last_name
    if phone:
        address_data["phone"] = phone
    if company:
        address_data["company"] = company
    if default is not None:
        address_data["default"] = default
    
    return make_request("POST", f"/customers/{customer_id}/addresses.json", {"address": address_data})

@app.tool()
def list_customer_addresses(customer_id: int) -> Dict:
    """
    List addresses for a customer.
    
    Args:
        customer_id: The ID of the customer
        
    Returns:
        Dict containing the list of addresses or error information
    """
    return make_request("GET", f"/customers/{customer_id}/addresses.json")

@app.tool()
def get_customer_address(customer_id: int, address_id: int) -> Dict:
    """
    Get a specific customer address.
    
    Args:
        customer_id: The ID of the customer
        address_id: The ID of the address
        
    Returns:
        Dict containing the address or error information
    """
    return make_request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")

@app.tool()
def update_customer_address(
    customer_id: int,
    address_id: int,
    address1: Optional[str] = None,
    city: Optional[str] = None,
    province: Optional[str] = None,
    country: Optional[str] = None,
    zip: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    company: Optional[str] = None,
    default: Optional[bool] = None
) -> Dict:
    """
    Update a customer address.
    
    Args:
        customer_id: The ID of the customer
        address_id: The ID of the address
        address1: Updated first line of the address
        city: Updated city
        province: Updated province/state
        country: Updated country
        zip: Updated ZIP/postal code
        first_name: Updated first name
        last_name: Updated last name
        phone: Updated phone number
        company: Updated company name
        default: Updated default address flag
        
    Returns:
        Dict containing the updated address or error information
    """
    address_data = {}
    
    if address1:
        address_data["address1"] = address1
    if city:
        address_data["city"] = city
    if province:
        address_data["province"] = province
    if country:
        address_data["country"] = country
    if zip:
        address_data["zip"] = zip
    if first_name:
        address_data["first_name"] = first_name
    if last_name:
        address_data["last_name"] = last_name
    if phone:
        address_data["phone"] = phone
    if company:
        address_data["company"] = company
    if default is not None:
        address_data["default"] = default
    
    return make_request("PUT", f"/customers/{customer_id}/addresses/{address_id}.json", {"address": address_data})

@app.tool()
def delete_customer_address(customer_id: int, address_id: int) -> Dict:
    """
    Delete a customer address.
    
    Args:
        customer_id: The ID of the customer
        address_id: The ID of the address to delete
        
    Returns:
        Dict containing the deletion result or error information
    """
    return make_request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")

# =============================================================================
# Inventory Operations
# =============================================================================

@app.tool()
def get_inventory_item(inventory_item_id: int) -> Dict:
    """
    Retrieve a single inventory item by its ID.
    
    Args:
        inventory_item_id: The ID of the inventory item to retrieve
        
    Returns:
        Dict containing the inventory item or error information
    """
    return make_request("GET", f"/inventory_items/{inventory_item_id}.json")

@app.tool()
def list_inventory_items(
    limit: int = 50,
    page: int = 1,
    ids: Optional[str] = None,
    sku: Optional[str] = None,
    tracked: Optional[bool] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None
) -> Dict:
    """
    Retrieve a list of inventory items.
    
    Args:
        limit: Number of items to retrieve (max 250)
        page: Page number for pagination
        ids: Comma-separated list of inventory item IDs (max 100)
        sku: Filter by SKU
        tracked: Filter by whether inventory is tracked
        created_at_min: Filter items created after this date
        created_at_max: Filter items created before this date
        updated_at_min: Filter items updated after this date
        updated_at_max: Filter items updated before this date
        
    Returns:
        Dict containing the list of inventory items or error information
    """
    params = {"limit": limit, "page": page}
    
    if ids:
        params["ids"] = ids
    if sku:
        params["sku"] = sku
    if tracked is not None:
        params["tracked"] = tracked
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    
    return make_request("GET", "/inventory_items.json", params=params)

@app.tool()
def update_inventory_item(
    inventory_item_id: int,
    sku: Optional[str] = None,
    cost: Optional[str] = None,
    tracked: Optional[bool] = None,
    country_code_of_origin: Optional[str] = None,
    province_code_of_origin: Optional[str] = None,
    harmonized_system_code: Optional[str] = None
) -> Dict:
    """
    Update an inventory item.
    
    Args:
        inventory_item_id: The ID of the inventory item to update
        sku: Updated SKU
        cost: Updated cost
        tracked: Whether inventory is tracked
        country_code_of_origin: Updated country of origin code
        province_code_of_origin: Updated province of origin code
        harmonized_system_code: Updated HS code
        
    Returns:
        Dict containing the updated inventory item or error information
    """
    inventory_item_data = {}
    
    if sku:
        inventory_item_data["sku"] = sku
    if cost:
        inventory_item_data["cost"] = cost
    if tracked is not None:
        inventory_item_data["tracked"] = tracked
    if country_code_of_origin:
        inventory_item_data["country_code_of_origin"] = country_code_of_origin
    if province_code_of_origin:
        inventory_item_data["province_code_of_origin"] = province_code_of_origin
    if harmonized_system_code:
        inventory_item_data["harmonized_system_code"] = harmonized_system_code
    
    return make_request("PUT", f"/inventory_items/{inventory_item_id}.json", {"inventory_item": inventory_item_data})

@app.tool()
def get_inventory_level(
    inventory_item_id: int,
    location_id: int
) -> Dict:
    """
    Get inventory level for a specific item at a location.
    
    Args:
        inventory_item_id: The ID of the inventory item
        location_id: The ID of the location
        
    Returns:
        Dict containing the inventory level or error information
    """
    params = {
        "inventory_item_ids": inventory_item_id,
        "location_ids": location_id
    }
    
    return make_request("GET", "/inventory_levels.json", params=params)

@app.tool()
def list_inventory_levels(
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    since_id: Optional[int] = None
) -> Dict:
    """
    List inventory levels.
    
    Args:
        location_ids: Comma-separated list of location IDs
        inventory_item_ids: Comma-separated list of inventory item IDs
        since_id: Filter levels with ID greater than this value
        
    Returns:
        Dict containing the list of inventory levels or error information
    """
    params = {}
    
    if location_ids:
        params["location_ids"] = location_ids
    if inventory_item_ids:
        params["inventory_item_ids"] = inventory_item_ids
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/inventory_levels.json", params=params)

@app.tool()
def adjust_inventory_level(
    inventory_item_id: int,
    location_id: int,
    available_adjustment: int
) -> Dict:
    """
    Adjust inventory level at a location.
    
    Args:
        inventory_item_id: The ID of the inventory item
        location_id: The ID of the location
        available_adjustment: Amount to adjust (positive to add, negative to subtract)
        
    Returns:
        Dict containing the updated inventory level or error information
    """
    data = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available_adjustment": available_adjustment
    }
    
    return make_request("POST", "/inventory_levels/adjust.json", data)

@app.tool()
def connect_inventory_item_to_location(
    inventory_item_id: int,
    location_id: int,
    relocate_if_necessary: bool = False
) -> Dict:
    """
    Connect an inventory item to a location.
    
    Args:
        inventory_item_id: The ID of the inventory item
        location_id: The ID of the location
        relocate_if_necessary: Whether to relocate inventory if necessary
        
    Returns:
        Dict containing the connection result or error information
    """
    data = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "relocate_if_necessary": relocate_if_necessary
    }
    
    return make_request("POST", "/inventory_levels/connect.json", data)

@app.tool()
def set_inventory_level(
    inventory_item_id: int,
    location_id: int,
    available: int,
    disconnect_if_necessary: bool = False
) -> Dict:
    """
    Set inventory level for an item at a location.
    
    Args:
        inventory_item_id: The ID of the inventory item
        location_id: The ID of the location
        available: The available quantity to set
        disconnect_if_necessary: Whether to disconnect from other locations if necessary
        
    Returns:
        Dict containing the set result or error information
    """
    data = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available,
        "disconnect_if_necessary": disconnect_if_necessary
    }
    
    return make_request("POST", "/inventory_levels/set.json", data)

# =============================================================================
# Metafield Operations
# =============================================================================

@app.tool()
def get_metafield(
    resource_type: str,
    resource_id: int,
    metafield_id: int
) -> Dict:
    """
    Get a specific metafield.
    
    Args:
        resource_type: The type of resource ('product', 'variant', 'customer', 'order', 'collection', 'blog', 'article', 'page', 'shop', 'location')
        resource_id: The ID of the resource
        metafield_id: The ID of the metafield
        
    Returns:
        Dict containing the metafield or error information
    """
    return make_request("GET", f"/{resource_type}s/{resource_id}/metafields/{metafield_id}.json")

@app.tool()
def list_metafields(
    resource_type: str,
    resource_id: int,
    limit: int = 50,
    page: int = 1,
    metafield_ids: Optional[str] = None,
    key: Optional[str] = None,
    namespace: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None
) -> Dict:
    """
    List metafields for a resource.
    
    Args:
        resource_type: The type of resource ('product', 'variant', 'customer', 'order', 'collection', 'blog', 'article', 'page', 'shop', 'location')
        resource_id: The ID of the resource
        limit: Number of results to retrieve (max 250)
        page: Page number for pagination
        metafield_ids: Comma-separated list of metafield IDs
        key: Filter by key
        namespace: Filter by namespace
        created_at_min: Filter metafields created after this date
        created_at_max: Filter metafields created before this date
        updated_at_min: Filter metafields updated after this date
        updated_at_max: Filter metafields updated before this date
        
    Returns:
        Dict containing the list of metafields or error information
    """
    params = {"limit": limit, "page": page}
    
    if metafield_ids:
        params["metafield_ids"] = metafield_ids
    if key:
        params["key"] = key
    if namespace:
        params["namespace"] = namespace
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    
    return make_request("GET", f"/{resource_type}s/{resource_id}/metafields.json", params=params)

@app.tool()
def create_metafield(
    resource_type: str,
    resource_id: int,
    key: str,
    namespace: str,
    value: str,
    type: str
) -> Dict:
    """
    Create a metafield.
    
    Args:
        resource_type: The type of resource ('product', 'variant', 'customer', 'order', 'collection', 'blog', 'article', 'page', 'shop', 'location')
        resource_id: The ID of the resource
        key: The unique identifier for the metafield (3-64 chars)
        namespace: The container for the metafield (3-255 chars)
        value: The value to store (stored as string)
        type: The data type ('single_line_text_field', 'multi_line_text_field', 'number_integer', 'number_decimal', 'json_string', 'boolean', 'date', 'datetime', 'url', 'file', 'phone', 'weight', 'dimension', 'volume', 'mass', 'rating', 'video', 'map', 'external_reference', 'external_video', 'external_image', 'external_file')
        
    Returns:
        Dict containing the created metafield or error information
    """
    metafield_data = {
        "key": key,
        "namespace": namespace,
        "value": value,
        "type": type
    }
    
    return make_request("POST", f"/{resource_type}s/{resource_id}/metafields.json", {"metafield": metafield_data})

@app.tool()
def update_metafield(
    resource_type: str,
    resource_id: int,
    metafield_id: int,
    key: Optional[str] = None,
    namespace: Optional[str] = None,
    value: Optional[str] = None,
    type: Optional[str] = None
) -> Dict:
    """
    Update a metafield.
    
    Args:
        resource_type: The type of resource ('product', 'variant', 'customer', 'order', 'collection', 'blog', 'article', 'page', 'shop', 'location')
        resource_id: The ID of the resource
        metafield_id: The ID of the metafield to update
        key: Updated key
        namespace: Updated namespace
        value: Updated value
        type: Updated data type
        
    Returns:
        Dict containing the updated metafield or error information
    """
    metafield_data = {}
    
    if key:
        metafield_data["key"] = key
    if namespace:
        metafield_data["namespace"] = namespace
    if value:
        metafield_data["value"] = value
    if type:
        metafield_data["type"] = type
    
    return make_request("PUT", f"/{resource_type}s/{resource_id}/metafields/{metafield_id}.json", {"metafield": metafield_data})

@app.tool()
def delete_metafield(
    resource_type: str,
    resource_id: int,
    metafield_id: int
) -> Dict:
    """
    Delete a metafield.
    
    Args:
        resource_type: The type of resource ('product', 'variant', 'customer', 'order', 'collection', 'blog', 'article', 'page', 'shop', 'location')
        resource_id: The ID of the resource
        metafield_id: The ID of the metafield to delete
        
    Returns:
        Dict containing the deletion result or error information
    """
    return make_request("DELETE", f"/{resource_type}s/{resource_id}/metafields/{metafield_id}.json")

# =============================================================================
# Discount Code Operations
# =============================================================================

@app.tool()
def create_discount_code(
    price_rule_id: int,
    code: str
) -> Dict:
    """
    Create a discount code.
    
    Args:
        price_rule_id: The ID of the price rule the discount code belongs to
        code: The discount code (max 255 chars)
        
    Returns:
        Dict containing the created discount code or error information
    """
    discount_code_data = {"code": code}
    
    return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", {"discount_code": discount_code_data})

@app.tool()
def list_discount_codes(price_rule_id: int) -> Dict:
    """
    List discount codes for a price rule.
    
    Args:
        price_rule_id: The ID of the price rule
        
    Returns:
        Dict containing the list of discount codes or error information
    """
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json")

@app.tool()
def get_discount_code(price_rule_id: int, discount_code_id: int) -> Dict:
    """
    Get a specific discount code.
    
    Args:
        price_rule_id: The ID of the price rule
        discount_code_id: The ID of the discount code
        
    Returns:
        Dict containing the discount code or error information
    """
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")

@app.tool()
def update_discount_code(
    price_rule_id: int,
    discount_code_id: int,
    code: str
) -> Dict:
    """
    Update a discount code.
    
    Args:
        price_rule_id: The ID of the price rule
        discount_code_id: The ID of the discount code
        code: Updated discount code
        
    Returns:
        Dict containing the updated discount code or error information
    """
    discount_code_data = {"code": code}
    
    return make_request("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", {"discount_code": discount_code_data})

@app.tool()
def delete_discount_code(
    price_rule_id: int,
    discount_code_id: int
) -> Dict:
    """
    Delete a discount code.
    
    Args:
        price_rule_id: The ID of the price rule
        discount_code_id: The ID of the discount code to delete
        
    Returns:
        Dict containing the deletion result or error information
    """
    return make_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")

# =============================================================================
# Refund Operations
# =============================================================================

@app.tool()
def calculate_refund(
    order_id: int,
    refund_line_items: List[Dict],
    shipping: Optional[Dict] = None,
    transactions: Optional[List[Dict]] = None,
    duties: Optional[List[Dict]] = None
) -> Dict:
    """
    Calculate a refund.
    
    Args:
        order_id: The ID of the order
        refund_line_items: Array of line items to refund with quantities and restock type
        shipping: Shipping refund information
        transactions: Array of transactions to refund
        duties: Array of duties to refund
        
    Returns:
        Dict containing the refund calculation or error information
    """
    refund_data = {"refund_line_items": refund_line_items}
    
    if shipping:
        refund_data["shipping"] = shipping
    if transactions:
        refund_data["transactions"] = transactions
    if duties:
        refund_data["duties"] = duties
    
    return make_request("POST", f"/orders/{order_id}/refunds/calculate.json", {"refund": refund_data})

@app.tool()
def create_refund(
    order_id: int,
    refund_line_items: List[Dict],
    transactions: List[Dict],
    shipping: Optional[Dict] = None,
    duties: Optional[List[Dict]] = None,
    note: Optional[str] = None,
    notify: Optional[bool] = None,
    discrepancy_reason: Optional[str] = None
) -> Dict:
    """
    Create a refund.
    
    Args:
        order_id: The ID of the order
        refund_line_items: Array of line items to refund with quantities and restock type
        transactions: Array of transactions to process as refunds
        shipping: Shipping refund information
        duties: Array of duties to refund
        note: Optional refund note
        notify: Whether to notify the customer
        discrepancy_reason: Reason for discrepancies (restock, damage, customer, other)
        
    Returns:
        Dict containing the created refund or error information
    """
    refund_data = {
        "refund_line_items": refund_line_items,
        "transactions": transactions
    }
    
    if shipping:
        refund_data["shipping"] = shipping
    if duties:
        refund_data["duties"] = duties
    if note:
        refund_data["note"] = note
    if notify is not None:
        refund_data["notify"] = notify
    if discrepancy_reason:
        refund_data["discrepancy_reason"] = discrepancy_reason
    
    return make_request("POST", f"/orders/{order_id}/refunds.json", {"refund": refund_data})

@app.tool()
def list_refunds(order_id: int) -> Dict:
    """
    List refunds for an order.
    
    Args:
        order_id: The ID of the order
        
    Returns:
        Dict containing the list of refunds or error information
    """
    return make_request("GET", f"/orders/{order_id}/refunds.json")

@app.tool()
def get_refund(order_id: int, refund_id: int) -> Dict:
    """
    Get a specific refund.
    
    Args:
        order_id: The ID of the order
        refund_id: The ID of the refund
        
    Returns:
        Dict containing the refund or error information
    """
    return make_request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")

# =============================================================================
# Location Operations
# =============================================================================

@app.tool()
def get_location(location_id: int) -> Dict:
    """
    Get a specific location.
    
    Args:
        location_id: The ID of the location
        
    Returns:
        Dict containing the location or error information
    """
    return make_request("GET", f"/locations/{location_id}.json")

@app.tool()
def list_locations() -> Dict:
    """
    List all locations.
    
    Returns:
        Dict containing the list of locations or error information
    """
    return make_request("GET", "/locations.json")

@app.tool()
def get_location_inventory_levels(location_id: int) -> Dict:
    """
    Get inventory levels for a location.
    
    Args:
        location_id: The ID of the location
        
    Returns:
        Dict containing the inventory levels or error information
    """
    return make_request("GET", f"/locations/{location_id}/inventory_levels.json")

# =============================================================================
# Fulfillment Operations
# =============================================================================

@app.tool()
def create_fulfillment(
    order_id: int,
    location_id: int,
    line_items_by_fulfillment_order: Optional[List[Dict]] = None,
    tracking_info: Optional[Dict] = None,
    notify_customer: bool = False
) -> Dict:
    """
    Create a fulfillment.
    
    Args:
        order_id: The ID of the order
        location_id: The ID of the fulfillment location
        line_items_by_fulfillment_order: Array of fulfillment orders with line items
        tracking_info: Tracking information object
        notify_customer: Whether to notify the customer
        
    Returns:
        Dict containing the created fulfillment or error information
    """
    fulfillment_data = {
        "location_id": location_id,
        "notify_customer": notify_customer
    }
    
    if line_items_by_fulfillment_order:
        fulfillment_data["line_items_by_fulfillment_order"] = line_items_by_fulfillment_order
    if tracking_info:
        fulfillment_data["tracking_info"] = tracking_info
    
    return make_request("POST", f"/orders/{order_id}/fulfillments.json", {"fulfillment": fulfillment_data})

@app.tool()
def list_fulfillments(order_id: int) -> Dict:
    """
    List fulfillments for an order.
    
    Args:
        order_id: The ID of the order
        
    Returns:
        Dict containing the list of fulfillments or error information
    """
    return make_request("GET", f"/orders/{order_id}/fulfillments.json")

@app.tool()
def get_fulfillment(order_id: int, fulfillment_id: int) -> Dict:
    """
    Get a specific fulfillment.
    
    Args:
        order_id: The ID of the order
        fulfillment_id: The ID of the fulfillment
        
    Returns:
        Dict containing the fulfillment or error information
    """
    return make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")

@app.tool()
def update_fulfillment(
    order_id: int,
    fulfillment_id: int,
    tracking_info: Dict
) -> Dict:
    """
    Update a fulfillment with tracking information.
    
    Args:
        order_id: The ID of the order
        fulfillment_id: The ID of the fulfillment
        tracking_info: Tracking information object
        
    Returns:
        Dict containing the updated fulfillment or error information
    """
    return make_request("PUT", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json", {"fulfillment": {"tracking_info": tracking_info}})

@app.tool()
def get_fulfillment_order(fulfillment_order_id: int) -> Dict:
    """
    Get a specific fulfillment order.
    
    Args:
        fulfillment_order_id: The ID of the fulfillment order
        
    Returns:
        Dict containing the fulfillment order or error information
    """
    return make_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")

@app.tool()
def list_fulfillment_orders(order_id: int) -> Dict:
    """
    List fulfillment orders for an order.
    
    Args:
        order_id: The ID of the order
        
    Returns:
        Dict containing the list of fulfillment orders or error information
    """
    return make_request("GET", f"/orders/{order_id}/fulfillment_orders.json")

@app.tool()
def cancel_fulfillment_order(fulfillment_order_id: int) -> Dict:
    """
    Cancel a fulfillment order.
    
    Args:
        fulfillment_order_id: The ID of the fulfillment order
        
    Returns:
        Dict containing the cancellation result or error information
    """
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")

@app.tool()
def release_hold_fulfillment_order(fulfillment_order_id: int) -> Dict:
    """
    Release hold on a fulfillment order.
    
    Args:
        fulfillment_order_id: The ID of the fulfillment order
        
    Returns:
        Dict containing the release result or error information
    """
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")

# =============================================================================
# Webhook Operations
# =============================================================================

@app.tool()
def create_webhook(
    topic: str,
    address: str,
    format: str = "json",
    fields: Optional[List[str]] = None,
    metafield_namespaces: Optional[List[str]] = None
) -> Dict:
    """
    Create a webhook subscription.
    
    Args:
        topic: The event topic to subscribe to (e.g., 'orders/create', 'customers/update')
        address: The URL where the webhook should send POST requests
        format: The format for webhook data ('json' or 'xml')
        fields: Array of specific fields to include in the webhook
        metafield_namespaces: Array of metafield namespaces to include
        
    Returns:
        Dict containing the created webhook or error information
    """
    webhook_data = {
        "topic": topic,
        "address": address,
        "format": format
    }
    
    if fields:
        webhook_data["fields"] = fields
    if metafield_namespaces:
        webhook_data["metafield_namespaces"] = metafield_namespaces
    
    return make_request("POST", "/webhooks.json", {"webhook": webhook_data})

@app.tool()
def list_webhooks() -> Dict:
    """
    List webhook subscriptions.
    
    Returns:
        Dict containing the list of webhooks or error information
    """
    return make_request("GET", "/webhooks.json")

@app.tool()
def get_webhook(webhook_id: int) -> Dict:
    """
    Get a specific webhook subscription.
    
    Args:
        webhook_id: The ID of the webhook
        
    Returns:
        Dict containing the webhook or error information
    """
    return make_request("GET", f"/webhooks/{webhook_id}.json")

@app.tool()
def update_webhook(
    webhook_id: int,
    address: Optional[str] = None,
    topic: Optional[str] = None,
    format: Optional[str] = None,
    fields: Optional[List[str]] = None,
    metafield_namespaces: Optional[List[str]] = None
) -> Dict:
    """
    Update a webhook subscription.
    
    Args:
        webhook_id: The ID of the webhook to update
        address: Updated webhook address
        topic: Updated topic
        format: Updated format
        fields: Updated fields array
        metafield_namespaces: Updated metafield namespaces
        
    Returns:
        Dict containing the updated webhook or error information
    """
    webhook_data = {}
    
    if address:
        webhook_data["address"] = address
    if topic:
        webhook_data["topic"] = topic
    if format:
        webhook_data["format"] = format
    if fields:
        webhook_data["fields"] = fields
    if metafield_namespaces:
        webhook_data["metafield_namespaces"] = metafield_namespaces
    
    return make_request("PUT", f"/webhooks/{webhook_id}.json", {"webhook": webhook_data})

@app.tool()
def delete_webhook(webhook_id: int) -> Dict:
    """
    Delete a webhook subscription.
    
    Args:
        webhook_id: The ID of the webhook to delete
        
    Returns:
        Dict containing the deletion result or error information
    """
    return make_request("DELETE", f"/webhooks/{webhook_id}.json")

# =============================================================================
# Shop Operations
# =============================================================================

@app.tool()
def get_shop() -> Dict:
    """
    Get shop information.
    
    Returns:
        Dict containing shop information or error information
    """
    return make_request("GET", "/shop.json")

# =============================================================================
# Collection Operations
# =============================================================================

@app.tool()
def get_collection(collection_id: int) -> Dict:
    """
    Get a specific collection.
    
    Args:
        collection_id: The ID of the collection
        
    Returns:
        Dict containing the collection or error information
    """
    return make_request("GET", f"/collections/{collection_id}.json")

@app.tool()
def get_collection_products(collection_id: int) -> Dict:
    """
    Get products in a collection.
    
    Args:
        collection_id: The ID of the collection
        
    Returns:
        Dict containing the list of products or error information
    """
    return make_request("GET", f"/collections/{collection_id}/products.json")

# =============================================================================
# Product Image Operations
# =============================================================================

@app.tool()
def create_product_image(
    product_id: int,
    src: str,
    alt: Optional[str] = None
) -> Dict:
    """
    Create a product image.
    
    Args:
        product_id: The ID of the product
        src: The URL of the image
        alt: Alternative text for the image
        
    Returns:
        Dict containing the created image or error information
    """
    image_data = {"src": src}
    
    if alt:
        image_data["alt"] = alt
    
    return make_request("POST", f"/products/{product_id}/images.json", {"image": image_data})

@app.tool()
def list_product_images(product_id: int) -> Dict:
    """
    List images for a product.
    
    Args:
        product_id: The ID of the product
        
    Returns:
        Dict containing the list of images or error information
    """
    return make_request("GET", f"/products/{product_id}/images.json")

@app.tool()
def get_product_image(product_id: int, image_id: int) -> Dict:
    """
    Get a specific product image.
    
    Args:
        product_id: The ID of the product
        image_id: The ID of the image
        
    Returns:
        Dict containing the image or error information
    """
    return make_request("GET", f"/products/{product_id}/images/{image_id}.json")

@app.tool()
def update_product_image(
    product_id: int,
    image_id: int,
    src: Optional[str] = None,
    alt: Optional[str] = None,
    position: Optional[int] = None
) -> Dict:
    """
    Update a product image.
    
    Args:
        product_id: The ID of the product
        image_id: The ID of the image
        src: Updated image URL
        alt: Updated alternative text
        position: Updated position in the image list
        
    Returns:
        Dict containing the updated image or error information
    """
    image_data = {}
    
    if src:
        image_data["src"] = src
    if alt:
        image_data["alt"] = alt
    if position:
        image_data["position"] = position
    
    return make_request("PUT", f"/products/{product_id}/images/{image_id}.json", {"image": image_data})

@app.tool()
def delete_product_image(product_id: int, image_id: int) -> Dict:
    """
    Delete a product image.
    
    Args:
        product_id: The ID of the product
        image_id: The ID of the image to delete
        
    Returns:
        Dict containing the deletion result or error information
    """
    return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")

# =============================================================================
# Country Operations
# =============================================================================

@app.tool()
def get_country(country_id: int) -> Dict:
    """
    Get a specific country.
    
    Args:
        country_id: The ID of the country
        
    Returns:
        Dict containing the country or error information
    """
    return make_request("GET", f"/countries/{country_id}.json")

@app.tool()
def list_countries() -> Dict:
    """
    List all countries.
    
    Returns:
        Dict containing the list of countries or error information
    """
    return make_request("GET", "/countries.json")

@app.tool()
def create_country(
    name: str,
    code: str,
    tax: Optional[float] = None,
    province_count: Optional[int] = None
) -> Dict:
    """
    Create a country.
    
    Args:
        name: The name of the country
        code: The two-letter country code
        tax: Tax rate for the country
        province_count: Number of provinces/states
        
    Returns:
        Dict containing the created country or error information
    """
    country_data = {
        "name": name,
        "code": code
    }
    
    if tax is not None:
        country_data["tax"] = tax
    if province_count is not None:
        country_data["province_count"] = province_count
    
    return make_request("POST", "/countries.json", {"country": country_data})

@app.tool()
def update_country(
    country_id: int,
    name: Optional[str] = None,
    code: Optional[str] = None,
    tax: Optional[float] = None,
    province_count: Optional[int] = None
) -> Dict:
    """
    Update a country.
    
    Args:
        country_id: The ID of the country to update
        name: Updated country name
        code: Updated country code
        tax: Updated tax rate
        province_count: Updated province count
        
    Returns:
        Dict containing the updated country or error information
    """
    country_data = {}
    
    if name:
        country_data["name"] = name
    if code:
        country_data["code"] = code
    if tax is not None:
        country_data["tax"] = tax
    if province_count is not None:
        country_data["province_count"] = province_count
    
    return make_request("PUT", f"/countries/{country_id}.json", {"country": country_data})

@app.tool()
def delete_country(country_id: int) -> Dict:
    """
    Delete a country.
    
    Args:
        country_id: The ID of the country to delete
        
    Returns:
        Dict containing the deletion result or error information
    """
    return make_request("DELETE", f"/countries/{country_id}.json")

# =============================================================================
# Draft Order Operations
# =============================================================================

@app.tool()
def create_draft_order(
    line_items: List[Dict],
    shipping_address: Optional[Dict] = None,
    billing_address: Optional[Dict] = None,
    note: Optional[str] = None,
    customer: Optional[Dict] = None
) -> Dict:
    """
    Create a draft order.
    
    Args:
        line_items: Array of line item objects
        shipping_address: Shipping address object
        billing_address: Billing address object
        note: Draft order note
        customer: Customer information
        
    Returns:
        Dict containing the created draft order or error information
    """
    draft_order_data = {"line_items": line_items}
    
    if shipping_address:
        draft_order_data["shipping_address"] = shipping_address
    if billing_address:
        draft_order_data["billing_address"] = billing_address
    if note:
        draft_order_data["note"] = note
    if customer:
        draft_order_data["customer"] = customer
    
    return make_request("POST", "/draft_orders.json", {"draft_order": draft_order_data})

@app.tool()
def list_draft_orders(
    limit: int = 50,
    page: int = 1,
    status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None
) -> Dict:
    """
    List draft orders.
    
    Args:
        limit: Number of draft orders to retrieve (max 250)
        page: Page number for pagination
        status: Filter by status
        created_at_min: Filter by creation date (min)
        created_at_max: Filter by creation date (max)
        updated_at_min: Filter by update date (min)
        updated_at_max: Filter by update date (max)
        
    Returns:
        Dict containing the list of draft orders or error information
    """
    params = {"limit": limit, "page": page}
    
    if status:
        params["status"] = status
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    
    return make_request("GET", "/draft_orders.json", params=params)

@app.tool()
def get_draft_order(draft_order_id: int) -> Dict:
    """
    Get a specific draft order.
    
    Args:
        draft_order_id: The ID of the draft order
        
    Returns:
        Dict containing the draft order or error information
    """
    return make_request("GET", f"/draft_orders/{draft_order_id}.json")

@app.tool()
def update_draft_order(
    draft_order_id: int,
    line_items: Optional[List[Dict]] = None,
    shipping_address: Optional[Dict] = None,
    billing_address: Optional[Dict] = None,
    note: Optional[str] = None,
    customer: Optional[Dict] = None,
    email: Optional[str] = None
) -> Dict:
    """
    Update a draft order.
    
    Args:
        draft_order_id: The ID of the draft order to update
        line_items: Updated line items
        shipping_address: Updated shipping address
        billing_address: Updated billing address
        note: Updated note
        customer: Updated customer information
        email: Updated email address
        
    Returns:
        Dict containing the updated draft order or error information
    """
    draft_order_data = {}
    
    if line_items:
        draft_order_data["line_items"] = line_items
    if shipping_address:
        draft_order_data["shipping_address"] = shipping_address
    if billing_address:
        draft_order_data["billing_address"] = billing_address
    if note:
        draft_order_data["note"] = note
    if customer:
        draft_order_data["customer"] = customer
    if email:
        draft_order_data["email"] = email
    
    return make_request("PUT", f"/draft_orders/{draft_order_id}.json", {"draft_order": draft_order_data})

@app.tool()
def send_draft_order(draft_order_id: int, email: Optional[str] = None) -> Dict:
    """
    Send a draft order invoice to a customer.
    
    Args:
        draft_order_id: The ID of the draft order
        email: Optional email address to send the invoice to
        
    Returns:
        Dict containing the send result or error information
    """
    data = {}
    if email:
        data["email"] = email
    
    return make_request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", data)

# =============================================================================
# Run the server
# =============================================================================

if __name__ == "__main__":
    app.run()