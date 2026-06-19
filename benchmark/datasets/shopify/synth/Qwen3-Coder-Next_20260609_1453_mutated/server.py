#!/usr/bin/env python3
"""
Shopify Admin REST API MCP Server

This server provides tools for interacting with the Shopify Admin REST API.
It supports operations on products, orders, customers, inventory, and more.
"""

import os
import json
from typing import Any
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="shopify-admin-api", version="1.0.0")

# Base URL configuration
BASE_URL = "https://{store_url}/admin/api/2026-01"


def make_request(method: str, endpoint: str, params: dict = None, data: dict = None) -> dict:
    """
    Make an authenticated request to the Shopify Admin REST API.
    
    Args:
        method: HTTP method (GET, POST, PUT, DELETE, PATCH)
        endpoint: API endpoint path (e.g., "/products.json")
        params: Query parameters
        data: Request body for POST/PUT requests
    
    Returns:
        dict: API response as a dictionary
    """
    import requests
    
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    
    if not store_url:
        return {"error": "SHOPIFY_STORE_URL environment variable is required"}
    
    if not access_token:
        return {"error": "SHOPIFY_ACCESS_TOKEN environment variable is required"}
    
    url = f"https://{store_url}/admin/api/2026-01{endpoint}"
    
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            timeout=60
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"raw_response": response.text}
        else:
            return {
                "error": f"API request failed with status {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ==========================================
# PRODUCT ENDPOINTS
# ==========================================

@mcp.tool()
def get_products(limit: int = 50, page: int = 1, ids: str = None, title: str = None) -> dict:
    """
    Retrieve a list of products.
    
    Args:
        limit: Number of results to return (default 50)
        page: Page number for pagination
        ids: Comma-separated list of product IDs to retrieve
        title: Filter products by title
    
    Returns:
        dict: Response containing products array and pagination info
    """
    params = {
        "limit": limit,
        "page": page
    }
    
    if ids:
        params["ids"] = ids
    if title:
        params["title"] = title
    
    return make_request("GET", "/products.json", params)


@mcp.tool()
def get_product(product_id: int) -> dict:
    """
    Retrieve a single product by ID.
    
    Args:
        product_id: The ID of the product to retrieve
    
    Returns:
        dict: Response containing the product details
    """
    return make_request("GET", f"/products/{product_id}.json")


@mcp.tool()
def create_product(
    title: str,
    body_html: str = None,
    vendor: str = None,
    product_type: str = None,
    status: str = "draft",
    published: bool = False,
    tags: str = None,
    variants: list = None
) -> dict:
    """
    Create a new product.
    
    Args:
        title: Product title (required)
        body_html: Product description in HTML format
        vendor: Product vendor name
        product_type: Product type categorization
        status: Product status ('draft', 'active', 'archived')
        published: Whether to publish the product immediately
        tags: Comma-separated list of tags
        variants: List of variant objects with price, sku, etc.
    
    Returns:
        dict: Response containing the created product
    """
    product_data = {
        "title": title
    }
    
    if body_html:
        product_data["body_html"] = body_html
    if vendor:
        product_data["vendor"] = vendor
    if product_type:
        product_data["product_type"] = product_type
    if status:
        product_data["status"] = status
    if published:
        product_data["published_at"] = "2007-12-31T19:00:00-05:00"
    if tags:
        product_data["tags"] = tags
    if variants:
        product_data["variants"] = variants
    
    return make_request("POST", "/products.json", data={"product": product_data})


@mcp.tool()
def update_product(product_id: int, **kwargs) -> dict:
    """
    Update an existing product.
    
    Args:
        product_id: The ID of the product to update
        **kwargs: Fields to update (title, body_html, vendor, etc.)
    
    Returns:
        dict: Response containing the updated product
    """
    return make_request("PUT", f"/products/{product_id}.json", data={"product": kwargs})


@mcp.tool()
def delete_product(product_id: int) -> dict:
    """
    Delete a product by ID.
    
    Args:
        product_id: The ID of the product to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return make_request("DELETE", f"/products/{product_id}.json")


@mcp.tool()
def get_products_count() -> dict:
    """
    Retrieve a count of all products.
    
    Returns:
        dict: Response containing the product count
    """
    return make_request("GET", "/products/count.json")


# ==========================================
# PRODUCT VARIANT ENDPOINTS
# ==========================================

@mcp.tool()
def get_product_variants(product_id: int, limit: int = 50) -> dict:
    """
    Retrieve a list of variants for a product.
    
    Args:
        product_id: The ID of the product
        limit: Number of results to return (default 50)
    
    Returns:
        dict: Response containing variants array
    """
    return make_request("GET", f"/products/{product_id}/variants.json", {"limit": limit})


@mcp.tool()
def get_variant(variant_id: int) -> dict:
    """
    Retrieve a single product variant by ID.
    
    Args:
        variant_id: The ID of the variant to retrieve
    
    Returns:
        dict: Response containing the variant details
    """
    return make_request("GET", f"/variants/{variant_id}.json")


@mcp.tool()
def create_product_variant(
    product_id: int,
    title: str = None,
    price: str = None,
    sku: str = None,
    inventory_policy: str = "deny",
    inventory_quantity: int = None
) -> dict:
    """
    Create a new variant for a product.
    
    Args:
        product_id: The ID of the product
        title: Variant title (e.g., 'Small', 'Large')
        price: Price for the variant
        sku: Stock keeping unit
        inventory_policy: 'deny' or 'continue'
        inventory_quantity: Initial inventory quantity
    
    Returns:
        dict: Response containing the created variant
    """
    variant_data = {}
    
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
    
    return make_request("POST", f"/products/{product_id}/variants.json", data={"variant": variant_data})


@mcp.tool()
def update_variant(variant_id: int, **kwargs) -> dict:
    """
    Update an existing product variant.
    
    Args:
        variant_id: The ID of the variant to update
        **kwargs: Fields to update (price, sku, inventory_quantity, etc.)
    
    Returns:
        dict: Response containing the updated variant
    """
    return make_request("PUT", f"/variants/{variant_id}.json", data={"variant": kwargs})


# ==========================================
# ORDER ENDPOINTS
# ==========================================

@mcp.tool()
def get_orders(
    limit: int = 50,
    status: str = "open",
    created_at_min: str = None,
    created_at_max: str = None
) -> dict:
    """
    Retrieve a list of orders.
    
    Args:
        limit: Number of results to return (default 50)
        status: Order status ('open', 'closed', 'cancelled', 'any')
        created_at_min: Filter orders created after this date
        created_at_max: Filter orders created before this date
    
    Returns:
        dict: Response containing orders array
    """
    params = {
        "limit": limit,
        "status": status
    }
    
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    
    return make_request("GET", "/orders.json", params)


@mcp.tool()
def get_order(order_id: int) -> dict:
    """
    Retrieve a single order by ID.
    
    Args:
        order_id: The ID of the order to retrieve
    
    Returns:
        dict: Response containing the order details
    """
    return make_request("GET", f"/orders/{order_id}.json")


@mcp.tool()
def create_order(
    line_items: list,
    shipping_address: dict = None,
    billing_address: dict = None,
    customer: dict = None,
    send_receipt: bool = False,
    send_fulfillment_receipt: bool = False
) -> dict:
    """
    Create a new order.
    
    Args:
        line_items: List of line item objects with product_id, quantity, price
        shipping_address: Shipping address details
        billing_address: Billing address details
        customer: Customer information
        send_receipt: Whether to send order confirmation
        send_fulfillment_receipt: Whether to send fulfillment confirmation
    
    Returns:
        dict: Response containing the created order
    """
    order_data = {
        "line_items": line_items,
        "send_receipt": send_receipt,
        "send_fulfillment_receipt": send_fulfillment_receipt
    }
    
    if shipping_address:
        order_data["shipping_address"] = shipping_address
    if billing_address:
        order_data["billing_address"] = billing_address
    if customer:
        order_data["customer"] = customer
    
    return make_request("POST", "/orders.json", data={"order": order_data})


@mcp.tool()
def update_order(order_id: int, **kwargs) -> dict:
    """
    Update an existing order.
    
    Args:
        order_id: The ID of the order to update
        **kwargs: Fields to update (shipping_address, billing_address, etc.)
    
    Returns:
        dict: Response containing the updated order
    """
    return make_request("PUT", f"/orders/{order_id}.json", data={"order": kwargs})


@mcp.tool()
def cancel_order(order_id: int, reason: str = "customer") -> dict:
    """
    Cancel an order.
    
    Args:
        order_id: The ID of the order to cancel
        reason: Cancellation reason ('customer', 'fraud', 'inventory', 'declined', 'other')
    
    Returns:
        dict: Response containing the cancelled order
    """
    return make_request("POST", f"/orders/{order_id}/cancel.json", data={"reason": reason})


@mcp.tool()
def close_order(order_id: int) -> dict:
    """
    Close an order.
    
    Args:
        order_id: The ID of the order to close
    
    Returns:
        dict: Response containing the closed order
    """
    return make_request("POST", f"/orders/{order_id}/close.json")


@mcp.tool()
def open_order(order_id: int) -> dict:
    """
    Re-open a closed order.
    
    Args:
        order_id: The ID of the order to re-open
    
    Returns:
        dict: Response containing the reopened order
    """
    return make_request("POST", f"/orders/{order_id}/open.json")


# ==========================================
# CUSTOMER ENDPOINTS
# ==========================================

@mcp.tool()
def get_customers(
    limit: int = 50,
    page: int = 1,
    created_at_min: str = None,
    created_at_max: str = None,
    email: str = None
) -> dict:
    """
    Retrieve a list of customers.
    
    Args:
        limit: Number of results to return (default 50)
        page: Page number for pagination
        created_at_min: Filter customers created after this date
        created_at_max: Filter customers created before this date
        email: Filter by customer email
    
    Returns:
        dict: Response containing customers array
    """
    params = {
        "limit": limit,
        "page": page
    }
    
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if email:
        params["email"] = email
    
    return make_request("GET", "/customers.json", params)


@mcp.tool()
def get_customer(customer_id: int) -> dict:
    """
    Retrieve a single customer by ID.
    
    Args:
        customer_id: The ID of the customer to retrieve
    
    Returns:
        dict: Response containing the customer details
    """
    return make_request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def create_customer(
    first_name: str = None,
    last_name: str = None,
    email: str = None,
    phone: str = None,
    addresses: list = None,
    password: str = None,
    password_confirmation: str = None,
    send_email_welcome: bool = False
) -> dict:
    """
    Create a new customer.
    
    Args:
        first_name: Customer's first name
        last_name: Customer's last name
        email: Customer's email address
        phone: Customer's phone number
        addresses: List of address objects
        password: Customer password
        password_confirmation: Password confirmation
        send_email_welcome: Whether to send welcome email
    
    Returns:
        dict: Response containing the created customer
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
    if send_email_welcome:
        customer_data["send_email_welcome"] = send_email_welcome
    
    return make_request("POST", "/customers.json", data={"customer": customer_data})


@mcp.tool()
def update_customer(customer_id: int, **kwargs) -> dict:
    """
    Update an existing customer.
    
    Args:
        customer_id: The ID of the customer to update
        **kwargs: Fields to update (first_name, last_name, email, etc.)
    
    Returns:
        dict: Response containing the updated customer
    """
    return make_request("PUT", f"/customers/{customer_id}.json", data={"customer": kwargs})


@mcp.tool()
def delete_customer(customer_id: int) -> dict:
    """
    Delete a customer by ID.
    
    Args:
        customer_id: The ID of the customer to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return make_request("DELETE", f"/customers/{customer_id}.json")


@mcp.tool()
def search_customers(query: str) -> dict:
    """
    Search for customers by query.
    
    Args:
        query: Search query (e.g., 'email:test@example.com')
    
    Returns:
        dict: Response containing matching customers
    """
    return make_request("GET", "/customers/search.json", {"query": query})


@mcp.tool()
def get_customer_orders(customer_id: int) -> dict:
    """
    Get all orders for a customer.
    
    Args:
        customer_id: The ID of the customer
    
    Returns:
        dict: Response containing the customer's orders
    """
    return make_request("GET", f"/customers/{customer_id}/orders.json")


@mcp.tool()
def create_account_activation_url(customer_id: int) -> dict:
    """
    Create an account activation URL for a customer.
    
    Args:
        customer_id: The ID of the customer
    
    Returns:
        dict: Response containing the activation URL
    """
    return make_request("POST", f"/customers/{customer_id}/account_activation_url.json")


# ==========================================
# INVENTORY ENDPOINTS
# ==========================================

@mcp.tool()
def get_inventory_items(ids: str, limit: int = 50) -> dict:
    """
    Retrieve inventory items by IDs.
    
    Args:
        ids: Comma-separated list of inventory item IDs
        limit: Number of results to return (default 50)
    
    Returns:
        dict: Response containing inventory items array
    """
    return make_request("GET", "/inventory_items.json", {"ids": ids, "limit": limit})


@mcp.tool()
def get_inventory_item(inventory_item_id: int) -> dict:
    """
    Retrieve a single inventory item by ID.
    
    Args:
        inventory_item_id: The ID of the inventory item
    
    Returns:
        dict: Response containing the inventory item details
    """
    return make_request("GET", f"/inventory_items/{inventory_item_id}.json")


@mcp.tool()
def update_inventory_item(inventory_item_id: int, **kwargs) -> dict:
    """
    Update an inventory item.
    
    Args:
        inventory_item_id: The ID of the inventory item
        **kwargs: Fields to update (sku, cost, tracked, etc.)
    
    Returns:
        dict: Response containing the updated inventory item
    """
    return make_request("PUT", f"/inventory_items/{inventory_item_id}.json", data={"inventory_item": kwargs})


# ==========================================
# INVENTORY LEVEL ENDPOINTS
# ==========================================

@mcp.tool()
def get_inventory_levels(
    location_id: int = None,
    inventory_item_ids: str = None,
    limit: int = 50
) -> dict:
    """
    Retrieve inventory levels.
    
    Args:
        location_id: Filter by location ID
        inventory_item_ids: Comma-separated list of inventory item IDs
        limit: Number of results to return (default 50)
    
    Returns:
        dict: Response containing inventory levels array
    """
    params = {"limit": limit}
    
    if location_id:
        params["location_ids"] = location_id
    if inventory_item_ids:
        params["inventory_item_ids"] = inventory_item_ids
    
    return make_request("GET", "/inventory_levels.json", params)


@mcp.tool()
def adjust_inventory_level(
    inventory_item_id: int,
    location_id: int,
    quantity_adjusted: int,
    reference_id: str = None,
    adjustment_reason: str = "inventory_adjustment"
) -> dict:
    """
    Adjust inventory level at a location.
    
    Args:
        inventory_item_id: The ID of the inventory item
        location_id: The ID of the location
        quantity_adjusted: Quantity to add (positive) or subtract (negative)
        reference_id: Optional reference ID
        adjustment_reason: Reason for adjustment
    
    Returns:
        dict: Response containing the adjusted inventory level
    """
    data = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "quantity_adjusted": quantity_adjusted,
        "reference_id": reference_id,
        "adjustment_reason": adjustment_reason
    }
    
    return make_request("POST", "/inventory_levels/adjust.json", data={"inventory_level": data})


@mcp.tool()
def connect_inventory_level(inventory_item_id: int, location_id: int) -> dict:
    """
    Connect an inventory item to a location.
    
    Args:
        inventory_item_id: The ID of the inventory item
        location_id: The ID of the location
    
    Returns:
        dict: Response confirming the connection
    """
    data = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id
    }
    
    return make_request("POST", "/inventory_levels/connect.json", data={"inventory_level": data})


# ==========================================
# FULFILLMENT ENDPOINTS
# ==========================================

@mcp.tool()
def get_fulfillments(order_id: int) -> dict:
    """
    Get all fulfillments for an order.
    
    Args:
        order_id: The ID of the order
    
    Returns:
        dict: Response containing fulfillments array
    """
    return make_request("GET", f"/orders/{order_id}/fulfillments.json")


@mcp.tool()
def create_fulfillment(order_id: int, tracking_number: str = None, line_items: list = None) -> dict:
    """
    Create a fulfillment for an order.
    
    Args:
        order_id: The ID of the order
        tracking_number: Tracking number for the shipment
        line_items: List of line item IDs to fulfill
    
    Returns:
        dict: Response containing the created fulfillment
    """
    data = {
        "fulfillment": {
            "tracking_number": tracking_number,
            "line_items": line_items
        }
    }
    
    return make_request("POST", f"/orders/{order_id}/fulfillments.json", data=data)


@mcp.tool()
def update_fulfillment_tracking(fulfillment_id: int, tracking_number: str, tracking_url: str = None) -> dict:
    """
    Update fulfillment tracking information.
    
    Args:
        fulfillment_id: The ID of the fulfillment
        tracking_number: Tracking number for the shipment
        tracking_url: Tracking URL for the customer
    
    Returns:
        dict: Response containing the updated fulfillment
    """
    data = {
        "fulfillment": {
            "tracking_number": tracking_number,
            "tracking_url": tracking_url
        }
    }
    
    return make_request("PUT", f"/fulfillments/{fulfillment_id}/update_tracking.json", data=data)


# ==========================================
# DISCOUNT ENDPOINTS
# ==========================================

@mcp.tool()
def get_price_rules(limit: int = 50) -> dict:
    """
    Retrieve a list of price rules (discounts).
    
    Args:
        limit: Number of results to return (default 50)
    
    Returns:
        dict: Response containing price rules array
    """
    return make_request("GET", "/price_rules.json", {"limit": limit})


@mcp.tool()
def get_price_rule(price_rule_id: int) -> dict:
    """
    Retrieve a single price rule by ID.
    
    Args:
        price_rule_id: The ID of the price rule
    
    Returns:
        dict: Response containing the price rule details
    """
    return make_request("GET", f"/price_rules/{price_rule_id}.json")


@mcp.tool()
def create_price_rule(
    title: str,
    target_type: str,
    target_selection: str = "all",
    allocation_method: str = "across",
    value_type: str,
    value: str,
    customer_selection: str = "all",
    starts_at: str = None
) -> dict:
    """
    Create a new price rule (discount).
    
    Args:
        title: Price rule title
        target_type: Target type ('line_item' or 'shipping_line')
        target_selection: Target selection ('all' or 'selected')
        allocation_method: Allocation method ('across' or 'each')
        value_type: Value type ('percentage', 'fixed_amount', 'shipping')
        value: Discount value
        customer_selection: Customer selection ('all' or 'selected')
        starts_at: Start date in ISO 8601 format
    
    Returns:
        dict: Response containing the created price rule
    """
    data = {
        "price_rule": {
            "title": title,
            "target_type": target_type,
            "target_selection": target_selection,
            "allocation_method": allocation_method,
            "value_type": value_type,
            "value": value,
            "customer_selection": customer_selection
        }
    }
    
    if starts_at:
        data["price_rule"]["starts_at"] = starts_at
    
    return make_request("POST", "/price_rules.json", data=data)


@mcp.tool()
def update_price_rule(price_rule_id: int, **kwargs) -> dict:
    """
    Update an existing price rule.
    
    Args:
        price_rule_id: The ID of the price rule
        **kwargs: Fields to update
    
    Returns:
        dict: Response containing the updated price rule
    """
    return make_request("PUT", f"/price_rules/{price_rule_id}.json", data={"price_rule": kwargs})


@mcp.tool()
def delete_price_rule(price_rule_id: int) -> dict:
    """
    Delete a price rule by ID.
    
    Args:
        price_rule_id: The ID of the price rule to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return make_request("DELETE", f"/price_rules/{price_rule_id}.json")


# ==========================================
# METAFIELD ENDPOINTS
# ==========================================

@mcp.tool()
def get_metafields(
    resource_type: str,
    resource_id: int,
    limit: int = 50
) -> dict:
    """
    Retrieve metafields for a resource.
    
    Args:
        resource_type: Resource type ('products', 'variants', 'customers', 'orders', etc.)
        resource_id: The ID of the resource
        limit: Number of results to return (default 50)
    
    Returns:
        dict: Response containing metafields array
    """
    endpoint = f"/{resource_type}/{resource_id}/metafields.json"
    return make_request("GET", endpoint, {"limit": limit})


@mcp.tool()
def get_metafield(metafield_id: int) -> dict:
    """
    Retrieve a single metafield by ID.
    
    Args:
        metafield_id: The ID of the metafield
    
    Returns:
        dict: Response containing the metafield details
    """
    return make_request("GET", f"/metafields/{metafield_id}.json")


@mcp.tool()
def create_metafield(
    resource_type: str,
    resource_id: int,
    key: str,
    value: str,
    type: str,
    namespace: str = "custom"
) -> dict:
    """
    Create a metafield for a resource.
    
    Args:
        resource_type: Resource type ('products', 'variants', 'customers', 'orders', etc.)
        resource_id: The ID of the resource
        key: Metafield key (max 30 characters)
        value: Metafield value
        type: Metafield type (e.g., 'single_line_text_field', 'integer', 'json_string')
        namespace: Metafield namespace (max 20 characters)
    
    Returns:
        dict: Response containing the created metafield
    """
    data = {
        "metafield": {
            "key": key,
            "value": value,
            "type": type,
            "namespace": namespace
        }
    }
    
    endpoint = f"/{resource_type}/{resource_id}/metafields.json"
    return make_request("POST", endpoint, data=data)


@mcp.tool()
def update_metafield(metafield_id: int, **kwargs) -> dict:
    """
    Update an existing metafield.
    
    Args:
        metafield_id: The ID of the metafield
        **kwargs: Fields to update (value, type, etc.)
    
    Returns:
        dict: Response containing the updated metafield
    """
    return make_request("PUT", f"/metafields/{metafield_id}.json", data={"metafield": kwargs})


@mcp.tool()
def delete_metafield(metafield_id: int) -> dict:
    """
    Delete a metafield by ID.
    
    Args:
        metafield_id: The ID of the metafield to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return make_request("DELETE", f"/metafields/{metafield_id}.json")


# ==========================================
# REFUND ENDPOINTS
# ==========================================

@mcp.tool()
def calculate_refund(
    order_id: int,
    line_items: list,
    shipping: dict = None,
    restock_type: str = "return",
    location_id: int = None
) -> dict:
    """
    Calculate a refund.
    
    Args:
        order_id: The ID of the order
        line_items: List of line items to refund with quantity
        shipping: Shipping cost refund amount
        restock_type: How to restock items ('return', 'cancel', 'nothing')
        location_id: Location ID for restocking
    
    Returns:
        dict: Response containing refund calculation
    """
    data = {
        "refund": {
            "line_items": line_items,
            "restock_type": restock_type
        }
    }
    
    if shipping:
        data["refund"]["shipping"] = shipping
    if location_id:
        data["refund"]["location_id"] = location_id
    
    return make_request("POST", f"/orders/{order_id}/refunds/calculate.json", data=data)


@mcp.tool()
def create_refund(
    order_id: int,
    line_items: list,
    shipping: dict = None,
    restock_type: str = "return",
    location_id: int = None,
    send_receipt: bool = False,
    send_fulfillment_receipt: bool = False
) -> dict:
    """
    Create a refund for an order.
    
    Args:
        order_id: The ID of the order
        line_items: List of line items to refund with quantity
        shipping: Shipping cost refund amount
        restock_type: How to restock items ('return', 'cancel', 'nothing')
        location_id: Location ID for restocking
        send_receipt: Whether to send refund receipt
        send_fulfillment_receipt: Whether to send fulfillment receipt
    
    Returns:
        dict: Response containing the created refund
    """
    data = {
        "refund": {
            "line_items": line_items,
            "restock_type": restock_type,
            "send_receipt": send_receipt,
            "send_fulfillment_receipt": send_fulfillment_receipt
        }
    }
    
    if shipping:
        data["refund"]["shipping"] = shipping
    if location_id:
        data["refund"]["location_id"] = location_id
    
    return make_request("POST", f"/orders/{order_id}/refunds.json", data=data)


# ==========================================
# SHOP ENDPOINTS
# ==========================================

@mcp.tool()
def get_shop() -> dict:
    """
    Retrieve shop information.
    
    Returns:
        dict: Response containing shop details
    """
    return make_request("GET", "/shop.json")


# ==========================================
# WEBHOOK ENDPOINTS
# ==========================================

@mcp.tool()
def get_webhooks(limit: int = 50) -> dict:
    """
    Retrieve a list of webhooks.
    
    Args:
        limit: Number of results to return (default 50)
    
    Returns:
        dict: Response containing webhooks array
    """
    return make_request("GET", "/webhooks.json", {"limit": limit})


@mcp.tool()
def get_webhook(webhook_id: int) -> dict:
    """
    Retrieve a single webhook by ID.
    
    Args:
        webhook_id: The ID of the webhook
    
    Returns:
        dict: Response containing the webhook details
    """
    return make_request("GET", f"/webhooks/{webhook_id}.json")


@mcp.tool()
def create_webhook(
    topic: str,
    address: str,
    format: str = "json"
) -> dict:
    """
    Create a new webhook.
    
    Args:
        topic: Webhook topic (e.g., 'orders/create', 'products/update')
        address: Callback URL for the webhook
        format: Data format ('json' or 'xml')
    
    Returns:
        dict: Response containing the created webhook
    """
    data = {
        "webhook": {
            "topic": topic,
            "address": address,
            "format": format
        }
    }
    
    return make_request("POST", "/webhooks.json", data=data)


@mcp.tool()
def update_webhook(webhook_id: int, **kwargs) -> dict:
    """
    Update an existing webhook.
    
    Args:
        webhook_id: The ID of the webhook
        **kwargs: Fields to update (address, topic, etc.)
    
    Returns:
        dict: Response containing the updated webhook
    """
    return make_request("PUT", f"/webhooks/{webhook_id}.json", data={"webhook": kwargs})


@mcp.tool()
def delete_webhook(webhook_id: int) -> dict:
    """
    Delete a webhook by ID.
    
    Args:
        webhook_id: The ID of the webhook to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return make_request("DELETE", f"/webhooks/{webhook_id}.json")


# ==========================================
# BATCH OPERATIONS
# ==========================================

@mcp.tool()
def create_discount_codes_batch(price_rule_id: int, codes: list) -> dict:
    """
    Create multiple discount codes for a price rule.
    
    Args:
        price_rule_id: The ID of the price rule
        codes: List of discount code objects with code property
    
    Returns:
        dict: Response containing discount code creation status
    """
    data = {
        "discount_codes": codes
    }
    
    return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes/batch.json", data=data)


if __name__ == "__main__":
    import asyncio
    asyncio.run(mcp.run_stdio_async())
