#!/usr/bin/env python3
"""
Shopify Admin REST API MCP Server

An MCP server that exposes tools for interacting with Shopify's Admin REST API.
"""

import os
import json
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("shopify-admin")

# Base URL for Shopify Admin API
SHOPIFY_BASE_URL = "https://{store_url}/admin/api/2026-01"

def get_shopify_headers() -> Dict[str, str]:
    """Get Shopify API headers for authentication."""
    access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    
    if not access_token:
        raise ValueError("SHOPIFY_ACCESS_TOKEN environment variable is not set")
    if not store_url:
        raise ValueError("SHOPIFY_STORE_URL environment variable is not set")
    
    return {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json",
        "User-Agent": "Shopify-MCP-Server/1.0"
    }

def make_request(method: str, endpoint: str, params: Optional[Dict] = None, 
                 data: Optional[Dict] = None) -> Dict[str, Any]:
    """Make a request to the Shopify Admin API."""
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    if not store_url:
        return {"error": "SHOPIFY_STORE_URL environment variable is not set"}
    
    url = f"https://{store_url}{endpoint}"
    headers = get_shopify_headers()
    
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
        
        # Handle response
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"data": response.text}
        else:
            # Return error details
            try:
                error_data = response.json()
                return {"error": error_data}
            except json.JSONDecodeError:
                return {"error": {"message": response.text, "status_code": response.status_code}}
    except requests.exceptions.RequestException as e:
        return {"error": {"message": str(e)}}

# ==================== Product-related endpoints ====================

@mcp.tool()
def get_product(product_id: int) -> Dict[str, Any]:
    """Retrieve a single product by ID.
    
    Args:
        product_id: The ID of the product to retrieve
        
    Returns:
        Product data or error information
    """
    result = make_request("GET", f"/products/{product_id}.json")
    return result.get("product", result)

@mcp.tool()
def list_products(limit: int = 50, cursor: Optional[str] = None, 
                  status: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of products.
    
    Args:
        limit: Maximum number of products to return (default: 50)
        cursor: Pagination cursor for the next page
        status: Filter by product status (active, draft, archived)
        
    Returns:
        List of products and pagination info
    """
    params = {"limit": limit}
    if cursor:
        params["page_info"] = cursor
    if status:
        params["status"] = status
    
    result = make_request("GET", "/products.json", params=params)
    return result

@mcp.tool()
def create_product(title: str, body_html: Optional[str] = None, 
                   vendor: Optional[str] = None,
                   product_type: Optional[str] = None,
                   tags: Optional[str] = None,
                   variants: Optional[list] = None,
                   images: Optional[list] = None,
                   options: Optional[list] = None) -> Dict[str, Any]:
    """Create a new product.
    
    Args:
        title: Product title (required)
        body_html: Product description in HTML format
        vendor: Product vendor name
        product_type: Product category
        tags: Comma-separated list of tags
        variants: List of variant configurations
        images: List of image configurations
        options: List of option names (e.g., ["Color", "Size"])
        
    Returns:
        Created product data or error information
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
    if variants:
        product_data["variants"] = variants
    if images:
        product_data["images"] = images
    if options:
        product_data["options"] = options
    
    result = make_request("POST", "/products.json", data={"product": product_data})
    return result.get("product", result)

@mcp.tool()
def update_product(product_id: int, title: Optional[str] = None,
                   body_html: Optional[str] = None,
                   vendor: Optional[str] = None,
                   product_type: Optional[str] = None,
                   tags: Optional[str] = None,
                   status: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing product.
    
    Args:
        product_id: The ID of the product to update
        title: Updated product title
        body_html: Updated product description in HTML format
        vendor: Updated vendor name
        product_type: Updated product category
        tags: Updated comma-separated list of tags
        status: Updated product status (active, draft, archived)
        
    Returns:
        Updated product data or error information
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
    
    result = make_request("PUT", f"/products/{product_id}.json", data={"product": product_data})
    return result.get("product", result)

@mcp.tool()
def delete_product(product_id: int) -> Dict[str, Any]:
    """Delete a product.
    
    Args:
        product_id: The ID of the product to delete
        
    Returns:
        Deletion confirmation or error information
    """
    result = make_request("DELETE", f"/products/{product_id}.json")
    # Delete returns empty body on success
    if "product" not in result:
        return {"success": True, "message": f"Product {product_id} deleted successfully"}
    return result

@mcp.tool()
def get_product_count(status: Optional[str] = None) -> Dict[str, Any]:
    """Get the count of products.
    
    Args:
        status: Filter by product status (active, draft, archived)
        
    Returns:
        Product count
    """
    params = {}
    if status:
        params["status"] = status
    
    result = make_request("GET", "/products/count.json", params=params)
    return result

# ==================== Product Variant-related endpoints ====================

@mcp.tool()
def get_product_variant(variant_id: int) -> Dict[str, Any]:
    """Retrieve a single product variant by ID.
    
    Args:
        variant_id: The ID of the variant to retrieve
        
    Returns:
        Variant data or error information
    """
    result = make_request("GET", f"/variants/{variant_id}.json")
    return result.get("variant", result)

@mcp.tool()
def list_product_variants(product_id: int, limit: int = 50) -> Dict[str, Any]:
    """Retrieve a list of variants for a product.
    
    Args:
        product_id: The ID of the product
        limit: Maximum number of variants to return (default: 50)
        
    Returns:
        List of variants and pagination info
    """
    params = {"limit": limit}
    result = make_request("GET", f"/products/{product_id}/variants.json", params=params)
    return result

@mcp.tool()
def create_product_variant(product_id: int, title: Optional[str] = None,
                           price: Optional[str] = None,
                           sku: Optional[str] = None,
                           inventory_policy: Optional[str] = None,
                           inventory_quantity: Optional[int] = None,
                           weight: Optional[float] = None,
                           weight_unit: Optional[str] = None,
                           requires_shipping: Optional[bool] = None,
                           taxable: Optional[bool] = None,
                           barcode: Optional[str] = None,
                           cost: Optional[str] = None) -> Dict[str, Any]:
    """Create a new product variant.
    
    Args:
        product_id: The ID of the product to add the variant to
        title: Variant title (e.g., "Small", "Red")
        price: Price for the variant
        sku: Stock keeping unit
        inventory_policy: "deny" or "continue"
        inventory_quantity: Initial inventory quantity (deprecated, use inventory level API)
        weight: Weight of the variant
        weight_unit: Unit of weight ("g", "kg", "oz", "lb")
        requires_shipping: Whether the variant requires shipping
        taxable: Whether the variant is taxable
        barcode: Barcode/UPC/ISBN
        cost: Cost of the variant
        
    Returns:
        Created variant data or error information
    """
    variant_data = {"product_id": product_id}
    
    if title:
        variant_data["title"] = title
    if price:
        variant_data["price"] = price
    if sku:
        variant_data["sku"] = sku
    if inventory_policy:
        variant_data["inventory_policy"] = inventory_policy
    if inventory_quantity is not None:
        variant_data["inventory_quantity"] = inventory_quantity
    if weight is not None:
        variant_data["weight"] = weight
    if weight_unit:
        variant_data["weight_unit"] = weight_unit
    if requires_shipping is not None:
        variant_data["requires_shipping"] = requires_shipping
    if taxable is not None:
        variant_data["taxable"] = taxable
    if barcode:
        variant_data["barcode"] = barcode
    if cost:
        variant_data["cost"] = cost
    
    result = make_request("POST", f"/products/{product_id}/variants.json", 
                         data={"variant": variant_data})
    return result.get("variant", result)

@mcp.tool()
def update_product_variant(variant_id: int, price: Optional[str] = None,
                           sku: Optional[str] = None,
                           inventory_policy: Optional[str] = None,
                           weight: Optional[float] = None,
                           weight_unit: Optional[str] = None,
                           requires_shipping: Optional[bool] = None,
                           taxable: Optional[bool] = None,
                           barcode: Optional[str] = None,
                           cost: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing product variant.
    
    Args:
        variant_id: The ID of the variant to update
        price: Updated price
        sku: Updated SKU
        inventory_policy: Updated inventory policy
        weight: Updated weight
        weight_unit: Updated weight unit
        requires_shipping: Updated shipping requirement
        taxable: Updated taxable status
        barcode: Updated barcode
        cost: Updated cost
        
    Returns:
        Updated variant data or error information
    """
    variant_data = {}
    
    if price:
        variant_data["price"] = price
    if sku:
        variant_data["sku"] = sku
    if inventory_policy:
        variant_data["inventory_policy"] = inventory_policy
    if weight is not None:
        variant_data["weight"] = weight
    if weight_unit:
        variant_data["weight_unit"] = weight_unit
    if requires_shipping is not None:
        variant_data["requires_shipping"] = requires_shipping
    if taxable is not None:
        variant_data["taxable"] = taxable
    if barcode:
        variant_data["barcode"] = barcode
    if cost:
        variant_data["cost"] = cost
    
    result = make_request("PUT", f"/variants/{variant_id}.json", 
                         data={"variant": variant_data})
    return result.get("variant", result)

# ==================== Customer-related endpoints ====================

@mcp.tool()
def get_customer(customer_id: int) -> Dict[str, Any]:
    """Retrieve a single customer by ID.
    
    Args:
        customer_id: The ID of the customer to retrieve
        
    Returns:
        Customer data or error information
    """
    result = make_request("GET", f"/customers/{customer_id}.json")
    return result.get("customer", result)

@mcp.tool()
def list_customers(limit: int = 50, cursor: Optional[str] = None,
                   since_id: Optional[int] = None) -> Dict[str, Any]:
    """Retrieve a list of customers.
    
    Args:
        limit: Maximum number of customers to return (default: 50)
        cursor: Pagination cursor for the next page
        since_id: Return customers with ID greater than since_id
        
    Returns:
        List of customers and pagination info
    """
    params = {"limit": limit}
    if cursor:
        params["page_info"] = cursor
    if since_id:
        params["since_id"] = since_id
    
    result = make_request("GET", "/customers.json", params=params)
    return result

@mcp.tool()
def create_customer(first_name: Optional[str] = None, last_name: Optional[str] = None,
                    email: Optional[str] = None, phone: Optional[str] = None,
                    addresses: Optional[list] = None, 
                    password: Optional[str] = None,
                    password_confirmation: Optional[str] = None,
                    verified_email: Optional[bool] = None,
                    tags: Optional[str] = None,
                    note: Optional[str] = None) -> Dict[str, Any]:
    """Create a new customer.
    
    Args:
        first_name: Customer's first name
        last_name: Customer's last name
        email: Customer's email address (required if creating account)
        phone: Customer's phone number
        addresses: List of address objects
        password: Customer's password (for account creation)
        password_confirmation: Customer's password confirmation
        verified_email: Whether email is verified
        tags: Comma-separated list of tags
        note: Internal note about the customer
        
    Returns:
        Created customer data or error information
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
    if addresses:
        customer_data["addresses"] = addresses
    if password:
        customer_data["password"] = password
    if password_confirmation:
        customer_data["password_confirmation"] = password_confirmation
    if verified_email is not None:
        customer_data["verified_email"] = verified_email
    if tags:
        customer_data["tags"] = tags
    if note:
        customer_data["note"] = note
    
    result = make_request("POST", "/customers.json", data={"customer": customer_data})
    return result.get("customer", result)

@mcp.tool()
def update_customer(customer_id: int, first_name: Optional[str] = None,
                    last_name: Optional[str] = None, email: Optional[str] = None,
                    phone: Optional[str] = None, addresses: Optional[list] = None,
                    tags: Optional[str] = None, note: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing customer.
    
    Args:
        customer_id: The ID of the customer to update
        first_name: Updated first name
        last_name: Updated last name
        email: Updated email address
        phone: Updated phone number
        addresses: Updated addresses
        tags: Updated tags
        note: Updated note
        
    Returns:
        Updated customer data or error information
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
    if addresses:
        customer_data["addresses"] = addresses
    if tags:
        customer_data["tags"] = tags
    if note:
        customer_data["note"] = note
    
    result = make_request("PUT", f"/customers/{customer_id}.json",
                         data={"customer": customer_data})
    return result.get("customer", result)

# ==================== Order-related endpoints ====================

@mcp.tool()
def get_order(order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a single order by ID.
    
    Args:
        order_id: The ID of the order to retrieve
        fields: Comma-separated list of fields to return
        
    Returns:
        Order data or error information
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    result = make_request("GET", f"/orders/{order_id}.json", params=params)
    return result.get("order", result)

@mcp.tool()
def list_orders(limit: int = 50, cursor: Optional[str] = None,
                status: Optional[str] = None, 
                created_at_min: Optional[str] = None,
                created_at_max: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of orders.
    
    Args:
        limit: Maximum number of orders to return (default: 50)
        cursor: Pagination cursor for the next page
        status: Filter by status (open, closed, cancelled, any)
        created_at_min: Return orders created after this date (ISO 8601)
        created_at_max: Return orders created before this date (ISO 8601)
        
    Returns:
        List of orders and pagination info
    """
    params = {"limit": limit}
    if cursor:
        params["page_info"] = cursor
    if status:
        params["status"] = status
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    
    result = make_request("GET", "/orders.json", params=params)
    return result

@mcp.tool()
def create_order(customer_id: int, line_items: list, shipping_address: dict,
                 billing_address: dict, email: str,
                 financial_status: Optional[str] = None,
                 fulfillment_status: Optional[str] = None,
                 send_receipt: Optional[bool] = None,
                 send_fulfillment_receipt: Optional[bool] = None,
                 inventory_behavior: Optional[str] = None) -> Dict[str, Any]:
    """Create a new order.
    
    Args:
        customer_id: The ID of the customer
        line_items: List of line item objects with product details
        shipping_address: Shipping address object
        billing_address: Billing address object
        email: Customer email address
        financial_status: Payment status (authorized, paid)
        fulfillment_status: Fulfillment status (fulfilled, partial, unfulfilled, any)
        send_receipt: Whether to send order confirmation email
        send_fulfillment_receipt: Whether to send fulfillment confirmation email
        inventory_behavior: How to handle inventory (bypass, decrement_ignoring_policy, decrement_obeying_policy)
        
    Returns:
        Created order data or error information
    """
    order_data = {
        "customer_id": customer_id,
        "line_items": line_items,
        "shipping_address": shipping_address,
        "billing_address": billing_address,
        "email": email
    }
    
    if financial_status:
        order_data["financial_status"] = financial_status
    if fulfillment_status:
        order_data["fulfillment_status"] = fulfillment_status
    if send_receipt is not None:
        order_data["send_receipt"] = send_receipt
    if send_fulfillment_receipt is not None:
        order_data["send_fulfillment_receipt"] = send_fulfillment_receipt
    if inventory_behavior:
        order_data["inventory_behavior"] = inventory_behavior
    
    result = make_request("POST", "/orders.json", data={"order": order_data})
    return result.get("order", result)

@mcp.tool()
def update_order(order_id: int, note: Optional[str] = None,
                 financial_status: Optional[str] = None,
                 fulfillment_status: Optional[str] = None,
                 send_receipt: Optional[bool] = None) -> Dict[str, Any]:
    """Update an existing order.
    
    Args:
        order_id: The ID of the order to update
        note: Updated order note
        financial_status: Updated financial status
        fulfillment_status: Updated fulfillment status
        send_receipt: Whether to send a new order confirmation
        
    Returns:
        Updated order data or error information
    """
    order_data = {}
    
    if note:
        order_data["note"] = note
    if financial_status:
        order_data["financial_status"] = financial_status
    if fulfillment_status:
        order_data["fulfillment_status"] = fulfillment_status
    if send_receipt is not None:
        order_data["send_receipt"] = send_receipt
    
    result = make_request("PUT", f"/orders/{order_id}.json",
                         data={"order": order_data})
    return result.get("order", result)

@mcp.tool()
def cancel_order(order_id: int, reason: Optional[str] = None) -> Dict[str, Any]:
    """Cancel an order.
    
    Args:
        order_id: The ID of the order to cancel
        reason: Reason for cancellation (customer, fraud, inventory, declined, other)
        
    Returns:
        Cancellation confirmation or error information
    """
    params = {}
    if reason:
        params["reason"] = reason
    
    result = make_request("POST", f"/orders/{order_id}/cancel.json", params=params)
    return result.get("order", result)

@mcp.tool()
def close_order(order_id: int) -> Dict[str, Any]:
    """Close an order.
    
    Args:
        order_id: The ID of the order to close
        
    Returns:
        Closure confirmation or error information
    """
    result = make_request("POST", f"/orders/{order_id}/close.json")
    return result.get("order", result)

@mcp.tool()
def open_order(order_id: int) -> Dict[str, Any]:
    """Re-open a closed order.
    
    Args:
        order_id: The ID of the order to re-open
        
    Returns:
        Re-opening confirmation or error information
    """
    result = make_request("POST", f"/orders/{order_id}/open.json")
    return result.get("order", result)

# ==================== Inventory-related endpoints ====================

@mcp.tool()
def get_inventory_item(inventory_item_id: int) -> Dict[str, Any]:
    """Retrieve a single inventory item by ID.
    
    Args:
        inventory_item_id: The ID of the inventory item to retrieve
        
    Returns:
        Inventory item data or error information
    """
    result = make_request("GET", f"/inventory_items/{inventory_item_id}.json")
    return result.get("inventory_item", result)

@mcp.tool()
def list_inventory_items(ids: str, limit: int = 50) -> Dict[str, Any]:
    """Retrieve a list of inventory items by IDs.
    
    Args:
        ids: Comma-separated list of inventory item IDs (max 100)
        limit: Maximum number of items to return (default: 50, max 250)
        
    Returns:
        List of inventory items and pagination info
    """
    params = {"ids": ids, "limit": limit}
    result = make_request("GET", "/inventory_items.json", params=params)
    return result

@mcp.tool()
def update_inventory_item(inventory_item_id: int, sku: Optional[str] = None,
                          cost: Optional[str] = None,
                          country_code_of_origin: Optional[str] = None,
                          province_code_of_origin: Optional[str] = None,
                          harmonized_system_code: Optional[str] = None,
                          requires_shipping: Optional[bool] = None) -> Dict[str, Any]:
    """Update an existing inventory item.
    
    Args:
        inventory_item_id: The ID of the inventory item to update
        sku: Updated SKU
        cost: Updated cost
        country_code_of_origin: Updated country of origin (ISO 3166-1 alpha-2)
        province_code_of_origin: Updated province code (ISO 3166-2 alpha-2)
        harmonized_system_code: Updated HS code
        requires_shipping: Updated shipping requirement
        
    Returns:
        Updated inventory item data or error information
    """
    inventory_item_data = {}
    
    if sku:
        inventory_item_data["sku"] = sku
    if cost:
        inventory_item_data["cost"] = cost
    if country_code_of_origin:
        inventory_item_data["country_code_of_origin"] = country_code_of_origin
    if province_code_of_origin:
        inventory_item_data["province_code_of_origin"] = province_code_of_origin
    if harmonized_system_code:
        inventory_item_data["harmonized_system_code"] = harmonized_system_code
    if requires_shipping is not None:
        inventory_item_data["requires_shipping"] = requires_shipping
    
    result = make_request("PUT", f"/inventory_items/{inventory_item_id}.json",
                         data={"inventory_item": inventory_item_data})
    return result.get("inventory_item", result)

@mcp.tool()
def get_inventory_level(location_id: int, inventory_item_id: int) -> Dict[str, Any]:
    """Retrieve inventory level for a specific location and item.
    
    Args:
        location_id: The ID of the location
        inventory_item_id: The ID of the inventory item
        
    Returns:
        Inventory level data or error information
    """
    params = {"location_ids": location_id, "inventory_item_ids": inventory_item_id}
    result = make_request("GET", "/inventory_levels.json", params=params)
    # The API returns a list of inventory levels
    return result.get("inventory_levels", [])[0] if result.get("inventory_levels", []) else result

@mcp.tool()
def adjust_inventory_level(inventory_item_id: int, location_id: int, 
                           available_adjustment: int,
                           adjustment_reason: Optional[str] = None,
                           reference_id: Optional[str] = None) -> Dict[str, Any]:
    """Adjust inventory level for an item at a specific location.
    
    Args:
        inventory_item_id: The ID of the inventory item
        location_id: The ID of the location
        available_adjustment: The amount to adjust inventory by (positive or negative)
        adjustment_reason: Reason for adjustment (e.g., "damaged", "theft", "misplaced")
        reference_id: Optional reference ID (e.g., inventory count ID)
        
    Returns:
        Adjustment confirmation or error information
    """
    data = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available_adjustment": available_adjustment
    }
    
    if adjustment_reason:
        data["adjustment_reason"] = adjustment_reason
    if reference_id:
        data["reference_id"] = reference_id
    
    result = make_request("POST", "/inventory_levels/adjust.json", data=data)
    return result.get("inventory_level", result)

@mcp.tool()
def connect_inventory_level(inventory_item_id: int, location_id: int,
                            available: int = 0) -> Dict[str, Any]:
    """Connect an inventory item to a location with a specific available quantity.
    
    Args:
        inventory_item_id: The ID of the inventory item
        location_id: The ID of the location
        available: Available quantity (default: 0)
        
    Returns:
        Connection confirmation or error information
    """
    data = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available
    }
    
    result = make_request("POST", "/inventory_levels/connect.json", data=data)
    return result.get("inventory_level", result)

# ==================== Location-related endpoints ====================

@mcp.tool()
def list_locations(active: Optional[bool] = None) -> Dict[str, Any]:
    """Retrieve a list of locations.
    
    Args:
        active: Filter by active status
        
    Returns:
        List of locations
    """
    params = {}
    if active is not None:
        params["active"] = active
    
    result = make_request("GET", "/locations.json", params=params)
    return result

@mcp.tool()
def get_location(location_id: int) -> Dict[str, Any]:
    """Retrieve a single location by ID.
    
    Args:
        location_id: The ID of the location to retrieve
        
    Returns:
        Location data or error information
    """
    result = make_request("GET", f"/locations/{location_id}.json")
    return result.get("location", result)

# ==================== Fulfillment-related endpoints ====================

@mcp.tool()
def create_fulfillment(order_id: int, tracking_number: Optional[str] = None,
                       tracking_url: Optional[str] = None,
                       tracking_company: Optional[str] = None,
                       line_items: Optional[list] = None,
                       notify_customer: Optional[bool] = None,
                       location_id: Optional[int] = None) -> Dict[str, Any]:
    """Create a fulfillment for an order.
    
    Args:
        order_id: The ID of the order to fulfill
        tracking_number: Tracking number for the shipment
        tracking_url: Tracking URL for the shipment
        tracking_company: Name of the tracking company
        line_items: List of line items to fulfill with quantities
        notify_customer: Whether to send fulfillment notification email
        location_id: ID of the location to fulfill from
        
    Returns:
        Created fulfillment data or error information
    """
    fulfillment_data = {"order_id": order_id}
    
    if tracking_number:
        fulfillment_data["tracking_number"] = tracking_number
    if tracking_url:
        fulfillment_data["tracking_url"] = tracking_url
    if tracking_company:
        fulfillment_data["tracking_company"] = tracking_company
    if line_items:
        fulfillment_data["line_items"] = line_items
    if notify_customer is not None:
        fulfillment_data["notify_customer"] = notify_customer
    if location_id:
        fulfillment_data["location_id"] = location_id
    
    result = make_request("POST", "/fulfillments.json", data={"fulfillment": fulfillment_data})
    return result.get("fulfillment", result)

@mcp.tool()
def get_fulfillment(fulfillment_id: int) -> Dict[str, Any]:
    """Retrieve a single fulfillment by ID.
    
    Args:
        fulfillment_id: The ID of the fulfillment to retrieve
        
    Returns:
        Fulfillment data or error information
    """
    result = make_request("GET", f"/fulfillments/{fulfillment_id}.json")
    return result.get("fulfillment", result)

@mcp.tool()
def update_fulfillment(fulfillment_id: int, tracking_number: Optional[str] = None,
                       tracking_url: Optional[str] = None,
                       tracking_company: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing fulfillment.
    
    Args:
        fulfillment_id: The ID of the fulfillment to update
        tracking_number: Updated tracking number
        tracking_url: Updated tracking URL
        tracking_company: Updated tracking company
        
    Returns:
        Updated fulfillment data or error information
    """
    fulfillment_data = {}
    
    if tracking_number:
        fulfillment_data["tracking_number"] = tracking_number
    if tracking_url:
        fulfillment_data["tracking_url"] = tracking_url
    if tracking_company:
        fulfillment_data["tracking_company"] = tracking_company
    
    result = make_request("PUT", f"/fulfillments/{fulfillment_id}.json",
                         data={"fulfillment": fulfillment_data})
    return result.get("fulfillment", result)

# ==================== Refund-related endpoints ====================

@mcp.tool()
def create_refund(order_id: int, refund_line_items: list,
                  shipping: Optional[dict] = None,
                  transactions: Optional[list] = None,
                  notify_customer: Optional[bool] = None,
                  order_adjustment: Optional[dict] = None) -> Dict[str, Any]:
    """Create a refund for an order.
    
    Args:
        order_id: The ID of the order to refund
        refund_line_items: List of line items to refund with quantities
        shipping: Shipping refund details
        transactions: List of transactions to refund
        notify_customer: Whether to send refund notification email
        order_adjustment: Refund adjustment details
        
    Returns:
        Created refund data or error information
    """
    refund_data = {"order_id": order_id, "refund_line_items": refund_line_items}
    
    if shipping:
        refund_data["shipping"] = shipping
    if transactions:
        refund_data["transactions"] = transactions
    if notify_customer is not None:
        refund_data["notify_customer"] = notify_customer
    if order_adjustment:
        refund_data["order_adjustment"] = order_adjustment
    
    result = make_request("POST", f"/orders/{order_id}/refunds.json",
                         data={"refund": refund_data})
    return result.get("refund", result)

# ==================== Discount-related endpoints ====================

@mcp.tool()
def get_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """Retrieve a single price rule by ID.
    
    Args:
        price_rule_id: The ID of the price rule to retrieve
        
    Returns:
        Price rule data or error information
    """
    result = make_request("GET", f"/price_rules/{price_rule_id}.json")
    return result.get("price_rule", result)

@mcp.tool()
def list_price_rules(limit: int = 50, cursor: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of price rules.
    
    Args:
        limit: Maximum number of price rules to return (default: 50)
        cursor: Pagination cursor for the next page
        
    Returns:
        List of price rules and pagination info
    """
    params = {"limit": limit}
    if cursor:
        params["page_info"] = cursor
    
    result = make_request("GET", "/price_rules.json", params=params)
    return result

@mcp.tool()
def create_price_rule(title: str, target_type: str, target_selection: str,
                      allocation_method: str, value_type: str, value: str,
                      customer_selection: Optional[str] = None,
                      repeats: Optional[int] = None,
                      once_per_customer: Optional[bool] = None,
                      starts_at: Optional[str] = None,
                      ends_at: Optional[str] = None,
                      min_cart_amount: Optional[str] = None,
                      min_quantity: Optional[int] = None) -> Dict[str, Any]:
    """Create a new price rule (discount).
    
    Args:
        title: Price rule title (required)
        target_type: Target type (line_item or shipping_line)
        target_selection: Target selection (all or explicit)
        allocation_method: Allocation method (across, each, or maximum)
        value_type: Value type (percentage, fixed_amount, or free_shipping)
        value: Discount value (e.g., "10" for 10%, "$5.00" for $5)
        customer_selection: Customer selection (all or specific)
        repeats: Number of times the rule can be repeated
        once_per_customer: Whether the rule can only be used once per customer
        starts_at: Start date (ISO 8601)
        ends_at: End date (ISO 8601)
        min_cart_amount: Minimum cart amount required
        min_quantity: Minimum quantity required
        
    Returns:
        Created price rule data or error information
    """
    price_rule_data = {
        "title": title,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "value_type": value_type,
        "value": value
    }
    
    if customer_selection:
        price_rule_data["customer_selection"] = customer_selection
    if repeats is not None:
        price_rule_data["repeats"] = repeats
    if once_per_customer is not None:
        price_rule_data["once_per_customer"] = once_per_customer
    if starts_at:
        price_rule_data["starts_at"] = starts_at
    if ends_at:
        price_rule_data["ends_at"] = ends_at
    if min_cart_amount:
        price_rule_data["min_cart_amount"] = min_cart_amount
    if min_quantity is not None:
        price_rule_data["min_quantity"] = min_quantity
    
    result = make_request("POST", "/price_rules.json",
                         data={"price_rule": price_rule_data})
    return result.get("price_rule", result)

@mcp.tool()
def update_price_rule(price_rule_id: int, title: Optional[str] = None,
                      target_type: Optional[str] = None,
                      target_selection: Optional[str] = None,
                      allocation_method: Optional[str] = None,
                      value_type: Optional[str] = None,
                      value: Optional[str] = None,
                      starts_at: Optional[str] = None,
                      ends_at: Optional[str] = None,
                      min_cart_amount: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing price rule.
    
    Args:
        price_rule_id: The ID of the price rule to update
        title: Updated title
        target_type: Updated target type
        target_selection: Updated target selection
        allocation_method: Updated allocation method
        value_type: Updated value type
        value: Updated value
        starts_at: Updated start date
        ends_at: Updated end date
        min_cart_amount: Updated minimum cart amount
        
    Returns:
        Updated price rule data or error information
    """
    price_rule_data = {}
    
    if title:
        price_rule_data["title"] = title
    if target_type:
        price_rule_data["target_type"] = target_type
    if target_selection:
        price_rule_data["target_selection"] = target_selection
    if allocation_method:
        price_rule_data["allocation_method"] = allocation_method
    if value_type:
        price_rule_data["value_type"] = value_type
    if value:
        price_rule_data["value"] = value
    if starts_at:
        price_rule_data["starts_at"] = starts_at
    if ends_at:
        price_rule_data["ends_at"] = ends_at
    if min_cart_amount:
        price_rule_data["min_cart_amount"] = min_cart_amount
    
    result = make_request("PUT", f"/price_rules/{price_rule_id}.json",
                         data={"price_rule": price_rule_data})
    return result.get("price_rule", result)

@mcp.tool()
def create_discount_code(price_rule_id: int, code: str) -> Dict[str, Any]:
    """Create a discount code for a price rule.
    
    Args:
        price_rule_id: The ID of the price rule
        code: Discount code (e.g., "SUMMER10OFF")
        
    Returns:
        Created discount code data or error information
    """
    data = {"discount_code": {"code": code}}
    
    result = make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json",
                         data=data)
    return result.get("discount_code", result)

# ==================== Metafield-related endpoints ====================

@mcp.tool()
def get_metafield(metafield_id: int) -> Dict[str, Any]:
    """Retrieve a single metafield by ID.
    
    Args:
        metafield_id: The ID of the metafield to retrieve
        
    Returns:
        Metafield data or error information
    """
    result = make_request("GET", f"/metafields/{metafield_id}.json")
    return result.get("metafield", result)

@mcp.tool()
def list_metafields(resource_type: str, resource_id: int,
                    limit: int = 50, cursor: Optional[str] = None,
                    fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of metafields for a resource.
    
    Args:
        resource_type: Type of resource (product, variant, customer, order, etc.)
        resource_id: ID of the resource
        limit: Maximum number of metafields to return (default: 50)
        cursor: Pagination cursor for the next page
        fields: Comma-separated list of fields to return
        
    Returns:
        List of metafields and pagination info
    """
    params = {"limit": limit}
    if cursor:
        params["page_info"] = cursor
    if fields:
        params["fields"] = fields
    
    result = make_request("GET", f"/{resource_type}s/{resource_id}/metafields.json", 
                         params=params)
    return result

@mcp.tool()
def create_metafield(resource_type: str, resource_id: int,
                     namespace: str, key: str, value: str,
                     type: str = "string") -> Dict[str, Any]:
    """Create a new metafield.
    
    Args:
        resource_type: Type of resource (product, variant, customer, order, etc.)
        resource_id: ID of the resource
        namespace: Namespace for the metafield (max 20 characters)
        key: Key/identifier for the metafield (max 30 characters)
        value: Value to store (max 64KB)
        type: Type of value (string, integer, json_string, etc.)
        
    Returns:
        Created metafield data or error information
    """
    metafield_data = {
        "namespace": namespace,
        "key": key,
        "value": value,
        "type": type
    }
    
    result = make_request("POST", f"/{resource_type}s/{resource_id}/metafields.json",
                         data={"metafield": metafield_data})
    return result.get("metafield", result)

@mcp.tool()
def update_metafield(metafield_id: int, value: str,
                     type: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing metafield.
    
    Args:
        metafield_id: The ID of the metafield to update
        value: Updated value
        type: Updated type (if changing)
        
    Returns:
        Updated metafield data or error information
    """
    metafield_data = {"value": value}
    
    if type:
        metafield_data["type"] = type
    
    result = make_request("PUT", f"/metafields/{metafield_id}.json",
                         data={"metafield": metafield_data})
    return result.get("metafield", result)

# ==================== Shop-related endpoints ====================

@mcp.tool()
def get_shop() -> Dict[str, Any]:
    """Retrieve shop information.
    
    Returns:
        Shop data including name, address, currency, etc.
    """
    result = make_request("GET", "/shop.json")
    return result.get("shop", result)

# ==================== Webhook-related endpoints ====================

@mcp.tool()
def list_webhooks(limit: int = 50, cursor: Optional[str] = None,
                  topic: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of webhooks.
    
    Args:
        limit: Maximum number of webhooks to return (default: 50)
        cursor: Pagination cursor for the next page
        topic: Filter by webhook topic
        
    Returns:
        List of webhooks and pagination info
    """
    params = {"limit": limit}
    if cursor:
        params["page_info"] = cursor
    if topic:
        params["topic"] = topic
    
    result = make_request("GET", "/webhooks.json", params=params)
    return result

@mcp.tool()
def create_webhook(topic: str, address: str, 
                   format: Optional[str] = None,
                   fields: Optional[str] = None,
                   metafield_namespaces: Optional[list] = None) -> Dict[str, Any]:
    """Create a new webhook.
    
    Args:
        topic: Webhook topic (e.g., "orders/create", "products/update")
        address: URL where webhook notifications will be sent
        format: Format of the webhook data (json, xml)
        fields: Comma-separated list of fields to include
        metafield_namespaces: List of metafield namespaces to include
        
    Returns:
        Created webhook data or error information
    """
    webhook_data = {
        "topic": topic,
        "address": address
    }
    
    if format:
        webhook_data["format"] = format
    if fields:
        webhook_data["fields"] = fields
    if metafield_namespaces:
        webhook_data["metafield_namespaces"] = metafield_namespaces
    
    result = make_request("POST", "/webhooks.json", data={"webhook": webhook_data})
    return result.get("webhook", result)

@mcp.tool()
def get_webhook(webhook_id: int) -> Dict[str, Any]:
    """Retrieve a single webhook by ID.
    
    Args:
        webhook_id: The ID of the webhook to retrieve
        
    Returns:
        Webhook data or error information
    """
    result = make_request("GET", f"/webhooks/{webhook_id}.json")
    return result.get("webhook", result)

@mcp.tool()
def update_webhook(webhook_id: int, address: Optional[str] = None,
                   topic: Optional[str] = None,
                   fields: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing webhook.
    
    Args:
        webhook_id: The ID of the webhook to update
        address: Updated webhook URL
        topic: Updated webhook topic
        fields: Updated fields list
        
    Returns:
        Updated webhook data or error information
    """
    webhook_data = {}
    
    if address:
        webhook_data["address"] = address
    if topic:
        webhook_data["topic"] = topic
    if fields:
        webhook_data["fields"] = fields
    
    result = make_request("PUT", f"/webhooks/{webhook_id}.json",
                         data={"webhook": webhook_data})
    return result.get("webhook", result)

@mcp.tool()
def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """Delete a webhook.
    
    Args:
        webhook_id: The ID of the webhook to delete
        
    Returns:
        Deletion confirmation or error information
    """
    result = make_request("DELETE", f"/webhooks/{webhook_id}.json")
    return {"success": True, "message": f"Webhook {webhook_id} deleted successfully"}

# ==================== Collection-related endpoints ====================

@mcp.tool()
def get_custom_collection(collection_id: int) -> Dict[str, Any]:
    """Retrieve a single custom collection by ID.
    
    Args:
        collection_id: The ID of the custom collection to retrieve
        
    Returns:
        Collection data or error information
    """
    result = make_request("GET", f"/custom_collections/{collection_id}.json")
    return result.get("custom_collection", result)

@mcp.tool()
def list_custom_collections(limit: int = 50, cursor: Optional[str] = None,
                            status: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of custom collections.
    
    Args:
        limit: Maximum number of collections to return (default: 50)
        cursor: Pagination cursor for the next page
        status: Filter by collection status (active, archived, draft)
        
    Returns:
        List of collections and pagination info
    """
    params = {"limit": limit}
    if cursor:
        params["page_info"] = cursor
    if status:
        params["status"] = status
    
    result = make_request("GET", "/custom_collections.json", params=params)
    return result

@mcp.tool()
def create_custom_collection(title: str, body_html: Optional[str] = None,
                             handle: Optional[str] = None,
                             image: Optional[dict] = None,
                             sort_order: Optional[str] = None,
                             published: Optional[bool] = None) -> Dict[str, Any]:
    """Create a new custom collection.
    
    Args:
        title: Collection title (required)
        body_html: Collection description in HTML
        handle: URL-friendly identifier (auto-generated if not provided)
        image: Collection image object
        sort_order: Sort order for products (alpha, manual, best-selling)
        published: Whether the collection is published
        
    Returns:
        Created collection data or error information
    """
    collection_data = {"title": title}
    
    if body_html:
        collection_data["body_html"] = body_html
    if handle:
        collection_data["handle"] = handle
    if image:
        collection_data["image"] = image
    if sort_order:
        collection_data["sort_order"] = sort_order
    if published is not None:
        collection_data["published"] = published
    
    result = make_request("POST", "/custom_collections.json",
                         data={"custom_collection": collection_data})
    return result.get("custom_collection", result)

@mcp.tool()
def update_custom_collection(collection_id: int, title: Optional[str] = None,
                             body_html: Optional[str] = None,
                             handle: Optional[str] = None,
                             sort_order: Optional[str] = None,
                             published: Optional[bool] = None) -> Dict[str, Any]:
    """Update an existing custom collection.
    
    Args:
        collection_id: The ID of the collection to update
        title: Updated title
        body_html: Updated description
        handle: Updated handle
        sort_order: Updated sort order
        published: Updated published status
        
    Returns:
        Updated collection data or error information
    """
    collection_data = {}
    
    if title:
        collection_data["title"] = title
    if body_html:
        collection_data["body_html"] = body_html
    if handle:
        collection_data["handle"] = handle
    if sort_order:
        collection_data["sort_order"] = sort_order
    if published is not None:
        collection_data["published"] = published
    
    result = make_request("PUT", f"/custom_collections/{collection_id}.json",
                         data={"custom_collection": collection_data})
    return result.get("custom_collection", result)

# ==================== Product Image-related endpoints ====================

@mcp.tool()
def get_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    """Retrieve a single product image by ID.
    
    Args:
        product_id: The ID of the product
        image_id: The ID of the image to retrieve
        
    Returns:
        Image data or error information
    """
    result = make_request("GET", f"/products/{product_id}/images/{image_id}.json")
    return result.get("image", result)

@mcp.tool()
def list_product_images(product_id: int, limit: int = 50) -> Dict[str, Any]:
    """Retrieve a list of images for a product.
    
    Args:
        product_id: The ID of the product
        limit: Maximum number of images to return (default: 50)
        
    Returns:
        List of images and pagination info
    """
    params = {"limit": limit}
    result = make_request("GET", f"/products/{product_id}/images.json", params=params)
    return result

@mcp.tool()
def create_product_image(product_id: int, src: Optional[str] = None,
                         attachment: Optional[str] = None,
                         filename: Optional[str] = None,
                         alt: Optional[str] = None) -> Dict[str, Any]:
    """Create a new product image.
    
    Args:
        product_id: The ID of the product to add the image to
        src: URL of the image to download (if not using attachment)
        attachment: Base64-encoded image data (if not using src)
        filename: Filename for the image (required if using attachment)
        alt: Alternative text for the image
        
    Returns:
        Created image data or error information
    """
    image_data = {}
    
    if src:
        image_data["src"] = src
    elif attachment:
        image_data["attachment"] = attachment
        if filename:
            image_data["filename"] = filename
    else:
        return {"error": "Either src or attachment (with filename) is required"}
    
    if alt:
        image_data["alt"] = alt
    
    result = make_request("POST", f"/products/{product_id}/images.json",
                         data={"image": image_data})
    return result.get("image", result)

@mcp.tool()
def update_product_image(product_id: int, image_id: int,
                         src: Optional[str] = None,
                         alt: Optional[str] = None,
                         position: Optional[int] = None) -> Dict[str, Any]:
    """Update an existing product image.
    
    Args:
        product_id: The ID of the product
        image_id: The ID of the image to update
        src: Updated image URL
        alt: Updated alternative text
        position: Updated position (1-based index)
        
    Returns:
        Updated image data or error information
    """
    image_data = {}
    
    if src:
        image_data["src"] = src
    if alt:
        image_data["alt"] = alt
    if position is not None:
        image_data["position"] = position
    
    result = make_request("PUT", f"/products/{product_id}/images/{image_id}.json",
                         data={"image": image_data})
    return result.get("image", result)

# ==================== Address-related endpoints ====================

@mcp.tool()
def get_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    """Retrieve a single customer address by ID.
    
    Args:
        customer_id: The ID of the customer
        address_id: The ID of the address to retrieve
        
    Returns:
        Address data or error information
    """
    result = make_request("GET", 
                         f"/customers/{customer_id}/addresses/{address_id}.json")
    return result.get("address", result)

@mcp.tool()
def list_customer_addresses(customer_id: int) -> Dict[str, Any]:
    """Retrieve a list of customer addresses.
    
    Args:
        customer_id: The ID of the customer
        
    Returns:
        List of addresses
    """
    result = make_request("GET", f"/customers/{customer_id}/addresses.json")
    return result

@mcp.tool()
def create_customer_address(customer_id: int, first_name: Optional[str] = None,
                            last_name: Optional[str] = None,
                            address1: Optional[str] = None,
                            address2: Optional[str] = None,
                            city: Optional[str] = None,
                            province: Optional[str] = None,
                            country: Optional[str] = None,
                            zip: Optional[str] = None,
                            phone: Optional[str] = None,
                            default: Optional[bool] = None) -> Dict[str, Any]:
    """Create a new customer address.
    
    Args:
        customer_id: The ID of the customer
        first_name: Address first name
        last_name: Address last name
        address1: First line of address
        address2: Second line of address
        city: City name
        province: Province/state name
        country: Country name
        zip: ZIP/postal code
        phone: Phone number
        default: Whether this is the default address
        
    Returns:
        Created address data or error information
    """
    address_data = {}
    
    if first_name:
        address_data["first_name"] = first_name
    if last_name:
        address_data["last_name"] = last_name
    if address1:
        address_data["address1"] = address1
    if address2:
        address_data["address2"] = address2
    if city:
        address_data["city"] = city
    if province:
        address_data["province"] = province
    if country:
        address_data["country"] = country
    if zip:
        address_data["zip"] = zip
    if phone:
        address_data["phone"] = phone
    if default is not None:
        address_data["default"] = default
    
    result = make_request("POST", f"/customers/{customer_id}/addresses.json",
                         data={"address": address_data})
    return result.get("address", result)

@mcp.tool()
def update_customer_address(customer_id: int, address_id: int,
                            first_name: Optional[str] = None,
                            last_name: Optional[str] = None,
                            address1: Optional[str] = None,
                            city: Optional[str] = None,
                            province: Optional[str] = None,
                            country: Optional[str] = None,
                            zip: Optional[str] = None,
                            phone: Optional[str] = None,
                            default: Optional[bool] = None) -> Dict[str, Any]:
    """Update an existing customer address.
    
    Args:
        customer_id: The ID of the customer
        address_id: The ID of the address to update
        first_name: Updated first name
        last_name: Updated last name
        address1: Updated first line of address
        city: Updated city
        province: Updated province
        country: Updated country
        zip: Updated ZIP code
        phone: Updated phone number
        default: Whether this is the default address
        
    Returns:
        Updated address data or error information
    """
    address_data = {}
    
    if first_name:
        address_data["first_name"] = first_name
    if last_name:
        address_data["last_name"] = last_name
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
    if phone:
        address_data["phone"] = phone
    if default is not None:
        address_data["default"] = default
    
    result = make_request("PUT", 
                         f"/customers/{customer_id}/addresses/{address_id}.json",
                         data={"address": address_data})
    return result.get("address", result)

# ==================== Draft Order-related endpoints ====================

@mcp.tool()
def get_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """Retrieve a single draft order by ID.
    
    Args:
        draft_order_id: The ID of the draft order to retrieve
        
    Returns:
        Draft order data or error information
    """
    result = make_request("GET", f"/draft_orders/{draft_order_id}.json")
    return result.get("draft_order", result)

@mcp.tool()
def list_draft_orders(limit: int = 50, cursor: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a list of draft orders.
    
    Args:
        limit: Maximum number of draft orders to return (default: 50)
        cursor: Pagination cursor for the next page
        
    Returns:
        List of draft orders and pagination info
    """
    params = {"limit": limit}
    if cursor:
        params["page_info"] = cursor
    
    result = make_request("GET", "/draft_orders.json", params=params)
    return result

@mcp.tool()
def create_draft_order(customer_id: int, line_items: list,
                       shipping_address: Optional[dict] = None,
                       billing_address: Optional[dict] = None,
                       note: Optional[str] = None,
                       tax_exempt: Optional[bool] = None,
                       tags: Optional[str] = None) -> Dict[str, Any]:
    """Create a new draft order.
    
    Args:
        customer_id: The ID of the customer
        line_items: List of line item objects
        shipping_address: Shipping address object
        billing_address: Billing address object
        note: Draft order note
        tax_exempt: Whether the order is tax exempt
        tags: Comma-separated list of tags
        
    Returns:
        Created draft order data or error information
    """
    draft_order_data = {
        "customer_id": customer_id,
        "line_items": line_items
    }
    
    if shipping_address:
        draft_order_data["shipping_address"] = shipping_address
    if billing_address:
        draft_order_data["billing_address"] = billing_address
    if note:
        draft_order_data["note"] = note
    if tax_exempt is not None:
        draft_order_data["tax_exempt"] = tax_exempt
    if tags:
        draft_order_data["tags"] = tags
    
    result = make_request("POST", "/draft_orders.json",
                         data={"draft_order": draft_order_data})
    return result.get("draft_order", result)

@mcp.tool()
def update_draft_order(draft_order_id: int, line_items: Optional[list] = None,
                       shipping_address: Optional[dict] = None,
                       billing_address: Optional[dict] = None,
                       note: Optional[str] = None,
                       tags: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing draft order.
    
    Args:
        draft_order_id: The ID of the draft order to update
        line_items: Updated line items
        shipping_address: Updated shipping address
        billing_address: Updated billing address
        note: Updated note
        tags: Updated tags
        
    Returns:
        Updated draft order data or error information
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
    if tags:
        draft_order_data["tags"] = tags
    
    result = make_request("PUT", f"/draft_orders/{draft_order_id}.json",
                         data={"draft_order": draft_order_data})
    return result.get("draft_order", result)

# ==================== Transaction-related endpoints ====================

@mcp.tool()
def list_transactions(order_id: int) -> Dict[str, Any]:
    """Retrieve a list of transactions for an order.
    
    Args:
        order_id: The ID of the order
        
    Returns:
        List of transactions
    """
    result = make_request("GET", f"/orders/{order_id}/transactions.json")
    return result

@mcp.tool()
def create_transaction(order_id: int, kind: str, amount: str,
                       currency: Optional[str] = None,
                       payment_details: Optional[dict] = None,
                       receipt: Optional[dict] = None,
                       test: Optional[bool] = None) -> Dict[str, Any]:
    """Create a new transaction for an order.
    
    Args:
        order_id: The ID of the order
        kind: Transaction kind (authorization, capture, sale, refund, void)
        amount: Transaction amount
        currency: Currency code (default: shop currency)
        payment_details: Payment details object
        receipt: Receipt data from payment provider
        test: Whether this is a test transaction
        
    Returns:
        Created transaction data or error information
    """
    transaction_data = {
        "order_id": order_id,
        "kind": kind,
        "amount": amount
    }
    
    if currency:
        transaction_data["currency"] = currency
    if payment_details:
        transaction_data["payment_details"] = payment_details
    if receipt:
        transaction_data["receipt"] = receipt
    if test is not None:
        transaction_data["test"] = test
    
    result = make_request("POST", f"/orders/{order_id}/transactions.json",
                         data={"transaction": transaction_data})
    return result.get("transaction", result)

# ==================== Country-related endpoints ====================

@mcp.tool()
def list_countries() -> Dict[str, Any]:
    """Retrieve a list of countries.
    
    Returns:
        List of countries
    """
    result = make_request("GET", "/countries.json")
    return result

@mcp.tool()
def get_country(country_id: int) -> Dict[str, Any]:
    """Retrieve a single country by ID.
    
    Args:
        country_id: The ID of the country to retrieve
        
    Returns:
        Country data or error information
    """
    result = make_request("GET", f"/countries/{country_id}.json")
    return result.get("country", result)

# ==================== Currency-related endpoints ====================

@mcp.tool()
def list_currencies() -> Dict[str, Any]:
    """Retrieve a list of currencies.
    
    Returns:
        List of currencies
    """
    result = make_request("GET", "/currencies.json")
    return result

# ==================== Run server ====================

if __name__ == "__main__":
    mcp.run()
