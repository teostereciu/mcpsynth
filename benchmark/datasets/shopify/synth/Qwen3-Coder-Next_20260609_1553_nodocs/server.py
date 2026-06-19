#!/usr/bin/env python3
"""
MCP Server for Shopify Admin REST API
Provides tools for managing products, orders, customers, inventory, discounts, and more.
"""

import os
import json
import requests
from typing import Any, Dict, Optional, List
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(name="shopify-admin")

# Base URL for Shopify Admin API
def get_base_url() -> str:
    """Get the base URL from environment variables."""
    store_url = os.getenv("SHOPIFY_STORE_URL")
    if not store_url:
        raise ValueError("SHOPIFY_STORE_URL environment variable is required")
    # Ensure proper format
    if not store_url.startswith("https://"):
        store_url = f"https://{store_url}"
    return f"{store_url}/admin/api/2026-01"

def get_access_token() -> str:
    """Get the access token from environment variables."""
    token = os.getenv("SHOPIFY_ACCESS_TOKEN")
    if not token:
        raise ValueError("SHOPIFY_ACCESS_TOKEN environment variable is required")
    return token

def make_request(method: str, endpoint: str, params: Optional[Dict] = None, 
                 json_data: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Make a request to the Shopify Admin API.
    
    Args:
        method: HTTP method (GET, POST, PUT, DELETE)
        endpoint: API endpoint path (e.g., /products)
        params: Query parameters
        json_data: Request body for POST/PUT
        
    Returns:
        JSON response as dict
    """
    base_url = get_base_url()
    url = f"{base_url}{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": get_access_token()
    }
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_data,
            timeout=60
        )
        
        if response.status_code >= 400:
            error_msg = f"API Error {response.status_code}: {response.text}"
            return {"error": error_msg}
        
        # Return JSON response or success status
        if response.text:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"data": response.text}
        else:
            return {"success": True, "status_code": response.status_code}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# ============================================================================
# PRODUCTS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_products(limit: int = 50, page: int = 1, fields: Optional[str] = None) -> Dict[str, Any]:
    """
    List all products in the store.
    
    Args:
        limit: Number of products to return (default 50, max 250)
        page: Page number for pagination
        fields: Comma-separated list of fields to return
        
    Returns:
        List of products
    """
    params = {"limit": limit, "page": page}
    if fields:
        params["fields"] = fields
    return make_request("GET", "/products.json", params=params)

@mcp.tool()
def get_product(product_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a single product by ID.
    
    Args:
        product_id: The product ID
        fields: Comma-separated list of fields to return
        
    Returns:
        Product details
    """
    params = {}
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/products/{product_id}.json", params=params)

@mcp.tool()
def create_product(title: str, body_html: Optional[str] = None, 
                   vendor: Optional[str] = None, product_type: Optional[str] = None,
                   tags: Optional[str] = None, variants: Optional[List[Dict]] = None,
                   images: Optional[List[Dict]] = None) -> Dict[str, Any]:
    """
    Create a new product.
    
    Args:
        title: Product title (required)
        body_html: Product description HTML
        vendor: Product vendor
        product_type: Product type
        tags: Comma-separated tags
        variants: List of variant configurations
        images: List of image configurations
        
    Returns:
        Created product
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
        
    return make_request("POST", "/products.json", json_data={"product": product_data})

@mcp.tool()
def update_product(product_id: int, title: Optional[str] = None,
                   body_html: Optional[str] = None, vendor: Optional[str] = None,
                   product_type: Optional[str] = None, tags: Optional[str] = None,
                   variants: Optional[List[Dict]] = None) -> Dict[str, Any]:
    """
    Update an existing product.
    
    Args:
        product_id: The product ID
        title: New product title
        body_html: New product description HTML
        vendor: New vendor
        product_type: New product type
        tags: New tags
        variants: List of variant configurations with id
        
    Returns:
        Updated product
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
    if variants:
        product_data["variants"] = variants
        
    return make_request("PUT", f"/products/{product_id}.json", 
                       json_data={"product": product_data})

@mcp.tool()
def delete_product(product_id: int) -> Dict[str, Any]:
    """
    Delete a product.
    
    Args:
        product_id: The product ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/products/{product_id}.json")

# ============================================================================
# PRODUCT VARIANTS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_product_variants(product_id: int, limit: int = 50, page: int = 1) -> Dict[str, Any]:
    """
    List variants for a product.
    
    Args:
        product_id: The product ID
        limit: Number of variants to return
        page: Page number for pagination
        
    Returns:
        List of variants
    """
    params = {"limit": limit, "page": page}
    return make_request("GET", f"/products/{product_id}/variants.json", params=params)

@mcp.tool()
def get_product_variant(variant_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a single variant by ID.
    
    Args:
        variant_id: The variant ID
        fields: Comma-separated list of fields to return
        
    Returns:
        Variant details
    """
    params = {}
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/variants/{variant_id}.json", params=params)

@mcp.tool()
def create_product_variant(product_id: int, price: float, 
                           inventory_quantity: int = 0,
                           sku: Optional[str] = None,
                           weight: Optional[float] = None,
                           weight_unit: str = "kg") -> Dict[str, Any]:
    """
    Create a new variant for a product.
    
    Args:
        product_id: The product ID
        price: Variant price (required)
        inventory_quantity: Initial inventory quantity
        sku: Stock keeping unit
        weight: Variant weight
        weight_unit: Weight unit (kg, g, lb, oz)
        
    Returns:
        Created variant
    """
    variant_data = {
        "product_id": product_id,
        "price": price,
        "inventory_quantity": inventory_quantity
    }
    if sku:
        variant_data["sku"] = sku
    if weight:
        variant_data["weight"] = weight
    variant_data["weight_unit"] = weight_unit
    
    return make_request("POST", f"/products/{product_id}/variants.json", 
                       json_data={"variant": variant_data})

@mcp.tool()
def update_product_variant(variant_id: int, price: Optional[float] = None,
                           inventory_quantity: Optional[int] = None,
                           sku: Optional[str] = None,
                           weight: Optional[float] = None) -> Dict[str, Any]:
    """
    Update a variant.
    
    Args:
        variant_id: The variant ID
        price: New price
        inventory_quantity: New inventory quantity
        sku: New SKU
        weight: New weight
        
    Returns:
        Updated variant
    """
    variant_data = {}
    if price is not None:
        variant_data["price"] = price
    if inventory_quantity is not None:
        variant_data["inventory_quantity"] = inventory_quantity
    if sku:
        variant_data["sku"] = sku
    if weight is not None:
        variant_data["weight"] = weight
        
    return make_request("PUT", f"/variants/{variant_id}.json",
                       json_data={"variant": variant_data})

@mcp.tool()
def delete_product_variant(variant_id: int) -> Dict[str, Any]:
    """
    Delete a variant.
    
    Args:
        variant_id: The variant ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/variants/{variant_id}.json")

# ============================================================================
# PRODUCT IMAGES ENDPOINTS
# ============================================================================

@mcp.tool()
def get_product_images(product_id: int, limit: int = 50) -> Dict[str, Any]:
    """
    List images for a product.
    
    Args:
        product_id: The product ID
        limit: Number of images to return
        
    Returns:
        List of images
    """
    params = {"limit": limit}
    return make_request("GET", f"/products/{product_id}/images.json", params=params)

@mcp.tool()
def create_product_image(product_id: int, src: str,
                         alt: Optional[str] = None,
                         position: Optional[int] = None) -> Dict[str, Any]:
    """
    Add an image to a product.
    
    Args:
        product_id: The product ID
        src: Image URL (required)
        alt: Image alt text
        position: Image position
        
    Returns:
        Created image
    """
    image_data = {"src": src}
    if alt:
        image_data["alt"] = alt
    if position:
        image_data["position"] = position
        
    return make_request("POST", f"/products/{product_id}/images.json",
                       json_data={"image": image_data})

@mcp.tool()
def update_product_image(product_id: int, image_id: int,
                         alt: Optional[str] = None,
                         position: Optional[int] = None) -> Dict[str, Any]:
    """
    Update a product image.
    
    Args:
        product_id: The product ID
        image_id: The image ID
        alt: New alt text
        position: New position
        
    Returns:
        Updated image
    """
    image_data = {}
    if alt:
        image_data["alt"] = alt
    if position:
        image_data["position"] = position
        
    return make_request("PUT", f"/products/{product_id}/images/{image_id}.json",
                       json_data={"image": image_data})

@mcp.tool()
def delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    """
    Delete a product image.
    
    Args:
        product_id: The product ID
        image_id: The image ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")

# ============================================================================
# PRODUCT COLLECTIONS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_collections(limit: int = 50, page: int = 1) -> Dict[str, Any]:
    """
    List all collections.
    
    Args:
        limit: Number of collections to return
        page: Page number for pagination
        
    Returns:
        List of collections
    """
    params = {"limit": limit, "page": page}
    return make_request("GET", "/collections.json", params=params)

@mcp.tool()
def get_collection(collection_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a single collection by ID.
    
    Args:
        collection_id: The collection ID
        fields: Comma-separated list of fields to return
        
    Returns:
        Collection details
    """
    params = {}
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/collections/{collection_id}.json", params=params)

@mcp.tool()
def create_collection(title: str, body_html: Optional[str] = None,
                      rules: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Create a new collection.
    
    Args:
        title: Collection title (required)
        body_html: Collection description HTML
        rules: Automated collection rules
        
    Returns:
        Created collection
    """
    collection_data = {"title": title}
    if body_html:
        collection_data["body_html"] = body_html
    if rules:
        collection_data["rules"] = rules
        
    return make_request("POST", "/collections.json",
                       json_data={"collection": collection_data})

@mcp.tool()
def update_collection(collection_id: int, title: Optional[str] = None,
                      body_html: Optional[str] = None) -> Dict[str, Any]:
    """
    Update a collection.
    
    Args:
        collection_id: The collection ID
        title: New title
        body_html: New body HTML
        
    Returns:
        Updated collection
    """
    collection_data = {}
    if title:
        collection_data["title"] = title
    if body_html:
        collection_data["body_html"] = body_html
        
    return make_request("PUT", f"/collections/{collection_id}.json",
                       json_data={"collection": collection_data})

@mcp.tool()
def delete_collection(collection_id: int) -> Dict[str, Any]:
    """
    Delete a collection.
    
    Args:
        collection_id: The collection ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/collections/{collection_id}.json")

@mcp.tool()
def add_product_to_collection(collection_id: int, product_id: int) -> Dict[str, Any]:
    """
    Add a product to a collection.
    
    Args:
        collection_id: The collection ID
        product_id: The product ID
        
    Returns:
        Collection details with product
    """
    return make_request("POST", f"/collections/{collection_id}/product_entries.json",
                       json_data={"product_entry": {"product_id": product_id}})

@mcp.tool()
def remove_product_from_collection(collection_id: int, product_id: int) -> Dict[str, Any]:
    """
    Remove a product from a collection.
    
    Args:
        collection_id: The collection ID
        product_id: The product ID
        
    Returns:
        Deletion status
    """
    # Need to find the collection product ID first
    collection = get_collection(collection_id)
    if "error" in collection:
        return collection
    
    products = collection.get("collection", {}).get("products", [])
    for product in products:
        if product["id"] == product_id:
            return make_request("DELETE", 
                              f"/collections/{collection_id}/products/{product['id']}.json")
    
    return {"error": f"Product {product_id} not found in collection {collection_id}"}

# ============================================================================
# ORDERS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_orders(status: str = "any", limit: int = 50, page: int = 1,
               fields: Optional[str] = None) -> Dict[str, Any]:
    """
    List all orders.
    
    Args:
        status: Order status (open, closed, cancelled, any)
        limit: Number of orders to return
        page: Page number for pagination
        fields: Comma-separated list of fields to return
        
    Returns:
        List of orders
    """
    params = {"status": status, "limit": limit, "page": page}
    if fields:
        params["fields"] = fields
    return make_request("GET", "/orders.json", params=params)

@mcp.tool()
def get_order(order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a single order by ID.
    
    Args:
        order_id: The order ID
        fields: Comma-separated list of fields to return
        
    Returns:
        Order details
    """
    params = {}
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/orders/{order_id}.json", params=params)

@mcp.tool()
def create_order(customer_id: Optional[int] = None, line_items: Optional[List[Dict]] = None,
                 shipping_address: Optional[Dict] = None, 
                 billing_address: Optional[Dict] = None,
                 email: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new order.
    
    Args:
        customer_id: Customer ID
        line_items: List of line items with product_id, variant_id, quantity
        shipping_address: Shipping address
        billing_address: Billing address
        email: Customer email
        
    Returns:
        Created order
    """
    order_data = {}
    if customer_id:
        order_data["customer_id"] = customer_id
    if line_items:
        order_data["line_items"] = line_items
    if shipping_address:
        order_data["shipping_address"] = shipping_address
    if billing_address:
        order_data["billing_address"] = billing_address
    if email:
        order_data["email"] = email
        
    return make_request("POST", "/orders.json", json_data={"order": order_data})

@mcp.tool()
def update_order(order_id: int, financial_status: Optional[str] = None,
                 fulfill_status: Optional[str] = None, 
                 email: Optional[str] = None) -> Dict[str, Any]:
    """
    Update an order.
    
    Args:
        order_id: The order ID
        financial_status: Payment status (pending, authorized, paid, refunded)
        fulfill_status: Fulfillment status (fulfilled, partial, unfulfilled, unknown)
        email: New email
        
    Returns:
        Updated order
    """
    order_data = {}
    if financial_status:
        order_data["financial_status"] = financial_status
    if fulfill_status:
        order_data["fulfill_status"] = fulfill_status
    if email:
        order_data["email"] = email
        
    return make_request("PUT", f"/orders/{order_id}.json", 
                       json_data={"order": order_data})

@mcp.tool()
def cancel_order(order_id: int) -> Dict[str, Any]:
    """
    Cancel an order.
    
    Args:
        order_id: The order ID
        
    Returns:
        Cancelled order
    """
    return make_request("POST", f"/orders/{order_id}/cancel.json")

@mcp.tool()
def close_order(order_id: int) -> Dict[str, Any]:
    """
    Close an order.
    
    Args:
        order_id: The order ID
        
    Returns:
        Closed order
    """
    return make_request("POST", f"/orders/{order_id}/close.json")

@mcp.tool()
def open_order(order_id: int) -> Dict[str, Any]:
    """
    Open a closed order.
    
    Args:
        order_id: The order ID
        
    Returns:
        Opened order
    """
    return make_request("POST", f"/orders/{order_id}/open.json")

@mcp.tool()
def delete_order(order_id: int) -> Dict[str, Any]:
    """
    Delete an order (requires specific permissions).
    
    Args:
        order_id: The order ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/orders/{order_id}.json")

# ============================================================================
# DRAFT ORDERS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_draft_orders(limit: int = 50, page: int = 1) -> Dict[str, Any]:
    """
    List all draft orders.
    
    Args:
        limit: Number of draft orders to return
        page: Page number for pagination
        
    Returns:
        List of draft orders
    """
    params = {"limit": limit, "page": page}
    return make_request("GET", "/draft_orders.json", params=params)

@mcp.tool()
def get_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """
    Get a single draft order by ID.
    
    Args:
        draft_order_id: The draft order ID
        
    Returns:
        Draft order details
    """
    return make_request("GET", f"/draft_orders/{draft_order_id}.json")

@mcp.tool()
def create_draft_order(customer_id: Optional[int] = None, line_items: Optional[List[Dict]] = None,
                       shipping_address: Optional[Dict] = None,
                       email: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new draft order.
    
    Args:
        customer_id: Customer ID
        line_items: List of line items
        shipping_address: Shipping address
        email: Customer email
        
    Returns:
        Created draft order
    """
    order_data = {}
    if customer_id:
        order_data["customer_id"] = customer_id
    if line_items:
        order_data["line_items"] = line_items
    if shipping_address:
        order_data["shipping_address"] = shipping_address
    if email:
        order_data["email"] = email
        
    return make_request("POST", "/draft_orders.json", 
                       json_data={"draft_order": order_data})

@mcp.tool()
def update_draft_order(draft_order_id: int, line_items: Optional[List[Dict]] = None,
                       shipping_address: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Update a draft order.
    
    Args:
        draft_order_id: The draft order ID
        line_items: Updated line items
        shipping_address: Updated shipping address
        
    Returns:
        Updated draft order
    """
    order_data = {}
    if line_items:
        order_data["line_items"] = line_items
    if shipping_address:
        order_data["shipping_address"] = shipping_address
        
    return make_request("PUT", f"/draft_orders/{draft_order_id}.json",
                       json_data={"draft_order": order_data})

@mcp.tool()
def delete_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """
    Delete a draft order.
    
    Args:
        draft_order_id: The draft order ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/draft_orders/{draft_order_id}.json")

@mcp.tool()
def complete_draft_order(draft_order_id: int, send_invoice_email: bool = False) -> Dict[str, Any]:
    """
    Complete a draft order, converting it to a paid order.
    
    Args:
        draft_order_id: The draft order ID
        send_invoice_email: Whether to send invoice email
        
    Returns:
        Completed order
    """
    params = {"send_invoice_email": send_invoice_email}
    return make_request("POST", f"/draft_orders/{draft_order_id}/complete.json", 
                       params=params)

# ============================================================================
# CUSTOMERS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_customers(limit: int = 50, page: int = 1, fields: Optional[str] = None) -> Dict[str, Any]:
    """
    List all customers.
    
    Args:
        limit: Number of customers to return
        page: Page number for pagination
        fields: Comma-separated list of fields to return
        
    Returns:
        List of customers
    """
    params = {"limit": limit, "page": page}
    if fields:
        params["fields"] = fields
    return make_request("GET", "/customers.json", params=params)

@mcp.tool()
def get_customer(customer_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a single customer by ID.
    
    Args:
        customer_id: The customer ID
        fields: Comma-separated list of fields to return
        
    Returns:
        Customer details
    """
    params = {}
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/customers/{customer_id}.json", params=params)

@mcp.tool()
def create_customer(first_name: Optional[str] = None, last_name: Optional[str] = None,
                    email: Optional[str] = None, phone: Optional[str] = None,
                    address: Optional[Dict] = None, tags: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new customer.
    
    Args:
        first_name: Customer's first name
        last_name: Customer's last name
        email: Customer's email
        phone: Customer's phone
        address: Customer's address
        tags: Comma-separated tags
        
    Returns:
        Created customer
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
    if address:
        customer_data["addresses"] = [address]
    if tags:
        customer_data["tags"] = tags
        
    return make_request("POST", "/customers.json", 
                       json_data={"customer": customer_data})

@mcp.tool()
def update_customer(customer_id: int, first_name: Optional[str] = None,
                    last_name: Optional[str] = None, email: Optional[str] = None,
                    phone: Optional[str] = None) -> Dict[str, Any]:
    """
    Update a customer.
    
    Args:
        customer_id: The customer ID
        first_name: New first name
        last_name: New last name
        email: New email
        phone: New phone
        
    Returns:
        Updated customer
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
        
    return make_request("PUT", f"/customers/{customer_id}.json",
                       json_data={"customer": customer_data})

@mcp.tool()
def delete_customer(customer_id: int) -> Dict[str, Any]:
    """
    Delete a customer.
    
    Args:
        customer_id: The customer ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/customers/{customer_id}.json")

# ============================================================================
# INVENTORY ENDPOINTS
# ============================================================================

@mcp.tool()
def get_inventory_items(limit: int = 50, page: int = 1) -> Dict[str, Any]:
    """
    List all inventory items.
    
    Args:
        limit: Number of items to return
        page: Page number for pagination
        
    Returns:
        List of inventory items
    """
    params = {"limit": limit, "page": page}
    return make_request("GET", "/inventory_items.json", params=params)

@mcp.tool()
def update_inventory_item(inventory_item_id: int, cost: Optional[float] = None,
                          tracked: bool = True) -> Dict[str, Any]:
    """
    Update an inventory item.
    
    Args:
        inventory_item_id: The inventory item ID
        cost: New cost
        tracked: Whether inventory is tracked
        
    Returns:
        Updated inventory item
    """
    item_data = {"tracked": tracked}
    if cost is not None:
        item_data["cost"] = cost
        
    return make_request("PUT", f"/inventory_items/{inventory_item_id}.json",
                       json_data={"inventory_item": item_data})

@mcp.tool()
def get_inventory_levels(inventory_item_ids: List[int], limit: int = 50) -> Dict[str, Any]:
    """
    Get inventory levels for items.
    
    Args:
        inventory_item_ids: List of inventory item IDs
        limit: Number of levels to return
        
    Returns:
        List of inventory levels
    """
    # Inventory levels endpoint uses POST with item_ids
    params = {"limit": limit}
    data = {"inventory_item_ids": ",".join(str(id) for id in inventory_item_ids)}
    return make_request("GET", "/inventory_levels.json", params=params, json_data=data)

@mcp.tool()
def adjust_inventory_level(inventory_item_id: int, location_id: int, 
                           adjustment: int) -> Dict[str, Any]:
    """
    Adjust inventory level at a location.
    
    Args:
        inventory_item_id: The inventory item ID
        location_id: The location ID
        adjustment: Amount to adjust (positive or negative)
        
    Returns:
        Updated inventory level
    """
    return make_request("POST", "/inventory_levels/adjust.json",
                       json_data={
                           "inventory_item_id": inventory_item_id,
                           "location_id": location_id,
                           "adjustment": adjustment
                       })

@mcp.tool()
def set_inventory_level(inventory_item_id: int, location_id: int, 
                        available: int) -> Dict[str, Any]:
    """
    Set inventory level at a location.
    
    Args:
        inventory_item_id: The inventory item ID
        location_id: The location ID
        available: New available quantity
        
    Returns:
        Updated inventory level
    """
    return make_request("POST", "/inventory_levels/set.json",
                       json_data={
                           "inventory_item_id": inventory_item_id,
                           "location_id": location_id,
                           "available": available
                       })

# ============================================================================
# LOCATIONS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_locations() -> Dict[str, Any]:
    """
    List all locations.
    
    Returns:
        List of locations
    """
    return make_request("GET", "/locations.json")

@mcp.tool()
def get_location(location_id: int) -> Dict[str, Any]:
    """
    Get a single location by ID.
    
    Args:
        location_id: The location ID
        
    Returns:
        Location details
    """
    return make_request("GET", f"/locations/{location_id}.json")

# ============================================================================
# FULFILLMENT ENDPOINTS
# ============================================================================

@mcp.tool()
def get_fulfillments(order_id: int, limit: int = 50) -> Dict[str, Any]:
    """
    List fulfillments for an order.
    
    Args:
        order_id: The order ID
        limit: Number of fulfillments to return
        
    Returns:
        List of fulfillments
    """
    params = {"limit": limit}
    return make_request("GET", f"/orders/{order_id}/fulfillments.json", params=params)

@mcp.tool()
def create_fulfillment(order_id: int, location_id: int, line_items: List[Dict],
                       tracking_number: Optional[str] = None,
                       tracking_url: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a fulfillment for an order.
    
    Args:
        order_id: The order ID
        location_id: The fulfillment location ID
        line_items: List of line items to fulfill with id and quantity
        tracking_number: Tracking number
        tracking_url: Tracking URL
        
    Returns:
        Created fulfillment
    """
    fulfillment_data = {
        "location_id": location_id,
        "line_items": line_items
    }
    if tracking_number:
        fulfillment_data["tracking_number"] = tracking_number
    if tracking_url:
        fulfillment_data["tracking_url"] = tracking_url
        
    return make_request("POST", f"/orders/{order_id}/fulfillments.json",
                       json_data={"fulfillment": fulfillment_data})

@mcp.tool()
def get_fulfillment(order_id: int, fulfillment_id: int) -> Dict[str, Any]:
    """
    Get a single fulfillment.
    
    Args:
        order_id: The order ID
        fulfillment_id: The fulfillment ID
        
    Returns:
        Fulfillment details
    """
    return make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")

# ============================================================================
# REFUNDS ENDPOINTS
# ============================================================================

@mcp.tool()
def create_refund(order_id: int, shipping: Optional[Dict] = None,
                  refund_line_items: Optional[List[Dict]] = None,
                  note: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a refund for an order.
    
    Args:
        order_id: The order ID
        shipping: Shipping refund amount
        refund_line_items: List of line items to refund
        note: Refund note
        
    Returns:
        Created refund
    """
    refund_data = {}
    if shipping:
        refund_data["shipping"] = shipping
    if refund_line_items:
        refund_data["refund_line_items"] = refund_line_items
    if note:
        refund_data["note"] = note
        
    return make_request("POST", f"/orders/{order_id}/refunds.json",
                       json_data={"refund": refund_data})

# ============================================================================
# TRANSACTIONS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_transactions(order_id: int) -> Dict[str, Any]:
    """
    List transactions for an order.
    
    Args:
        order_id: The order ID
        
    Returns:
        List of transactions
    """
    return make_request("GET", f"/orders/{order_id}/transactions.json")

@mcp.tool()
def create_transaction(order_id: int, amount: float, kind: str,
                       gateway: Optional[str] = None, 
                       status: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a transaction for an order.
    
    Args:
        order_id: The order ID
        amount: Transaction amount
        kind: Transaction kind (authorization, capture, sale, void, refund)
        gateway: Payment gateway
        status: Transaction status
        
    Returns:
        Created transaction
    """
    transaction_data = {
        "amount": amount,
        "kind": kind
    }
    if gateway:
        transaction_data["gateway"] = gateway
    if status:
        transaction_data["status"] = status
        
    return make_request("POST", f"/orders/{order_id}/transactions.json",
                       json_data={"transaction": transaction_data})

# ============================================================================
# DISCOUNTS ENDPOINTS (Price Rules)
# ============================================================================

@mcp.tool()
def get_price_rules(limit: int = 50, page: int = 1) -> Dict[str, Any]:
    """
    List all price rules (discounts).
    
    Args:
        limit: Number of price rules to return
        page: Page number for pagination
        
    Returns:
        List of price rules
    """
    params = {"limit": limit, "page": page}
    return make_request("GET", "/price_rules.json", params=params)

@mcp.tool()
def get_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """
    Get a single price rule by ID.
    
    Args:
        price_rule_id: The price rule ID
        
    Returns:
        Price rule details
    """
    return make_request("GET", f"/price_rules/{price_rule_id}.json")

@mcp.tool()
def create_price_rule(title: str, value_type: str, value: float,
                      customer_selection: str = "all",
                      target_type: str = "line_item",
                      target_selection: str = "all",
                      allocation_limit: Optional[int] = None,
                      starts_at: Optional[str] = None,
                      ends_at: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new price rule (discount).
    
    Args:
        title: Price rule title
        value_type: Type of value (fixed_amount, percentage)
        value: Discount value
        customer_selection: Customer selection (all, pricelist, specific)
        target_type: What the discount applies to (line_item, shipping_line)
        target_selection: Target selection (all,priced_items,specific)
        allocation_limit: Maximum number of times discount can be used
        starts_at: Start date (ISO 8601)
        ends_at: End date (ISO 8601)
        
    Returns:
        Created price rule
    """
    rule_data = {
        "title": title,
        "value_type": value_type,
        "value": value,
        "customer_selection": customer_selection,
        "target_type": target_type,
        "target_selection": target_selection
    }
    if allocation_limit:
        rule_data["allocation_limit"] = allocation_limit
    if starts_at:
        rule_data["starts_at"] = starts_at
    if ends_at:
        rule_data["ends_at"] = ends_at
        
    return make_request("POST", "/price_rules.json",
                       json_data={"price_rule": rule_data})

@mcp.tool()
def update_price_rule(price_rule_id: int, title: Optional[str] = None,
                      value: Optional[float] = None,
                      starts_at: Optional[str] = None,
                      ends_at: Optional[str] = None) -> Dict[str, Any]:
    """
    Update a price rule.
    
    Args:
        price_rule_id: The price rule ID
        title: New title
        value: New value
        starts_at: New start date
        ends_at: New end date
        
    Returns:
        Updated price rule
    """
    rule_data = {}
    if title:
        rule_data["title"] = title
    if value is not None:
        rule_data["value"] = value
    if starts_at:
        rule_data["starts_at"] = starts_at
    if ends_at:
        rule_data["ends_at"] = ends_at
        
    return make_request("PUT", f"/price_rules/{price_rule_id}.json",
                       json_data={"price_rule": rule_data})

@mcp.tool()
def delete_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """
    Delete a price rule.
    
    Args:
        price_rule_id: The price rule ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/price_rules/{price_rule_id}.json")

@mcp.tool()
def get_price_rule_codes(price_rule_id: int, limit: int = 50) -> Dict[str, Any]:
    """
    Get discount codes for a price rule.
    
    Args:
        price_rule_id: The price rule ID
        limit: Number of codes to return
        
    Returns:
        List of discount codes
    """
    params = {"limit": limit}
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json",
                       params=params)

# ============================================================================
# METAFIELDS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_metafields(namespace: Optional[str] = None, key: Optional[str] = None,
                   limit: int = 50, page: int = 1) -> Dict[str, Any]:
    """
    List metafields.
    
    Args:
        namespace: Filter by namespace
        key: Filter by key
        limit: Number of metafields to return
        page: Page number for pagination
        
    Returns:
        List of metafields
    """
    params = {"limit": limit, "page": page}
    if namespace:
        params["namespace"] = namespace
    if key:
        params["key"] = key
    return make_request("GET", "/metafields.json", params=params)

@mcp.tool()
def create_metafield(namespace: str, key: str, value: str, type: str,
                     owner_id: int, owner_resource: str) -> Dict[str, Any]:
    """
    Create a new metafield.
    
    Args:
        namespace: Metafield namespace
        key: Metafield key
        value: Metafield value
        type: Value type (string, integer, json_string, etc.)
        owner_id: Owner resource ID
        owner_resource: Owner resource type (product, customer, order, etc.)
        
    Returns:
        Created metafield
    """
    metafield_data = {
        "namespace": namespace,
        "key": key,
        "value": value,
        "type": type,
        f"{owner_resource}_id": owner_id
    }
    
    return make_request("POST", "/metafields.json",
                       json_data={"metafield": metafield_data})

@mcp.tool()
def get_metafield(metafield_id: int) -> Dict[str, Any]:
    """
    Get a single metafield by ID.
    
    Args:
        metafield_id: The metafield ID
        
    Returns:
        Metafield details
    """
    return make_request("GET", f"/metafields/{metafield_id}.json")

@mcp.tool()
def update_metafield(metafield_id: int, value: Optional[str] = None,
                     type: Optional[str] = None) -> Dict[str, Any]:
    """
    Update a metafield.
    
    Args:
        metafield_id: The metafield ID
        value: New value
        type: New type
        
    Returns:
        Updated metafield
    """
    metafield_data = {}
    if value is not None:
        metafield_data["value"] = value
    if type:
        metafield_data["type"] = type
        
    return make_request("PUT", f"/metafields/{metafield_id}.json",
                       json_data={"metafield": metafield_data})

@mcp.tool()
def delete_metafield(metafield_id: int) -> Dict[str, Any]:
    """
    Delete a metafield.
    
    Args:
        metafield_id: The metafield ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/metafields/{metafield_id}.json")

# ============================================================================
# WEBHOOKS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_webhooks(limit: int = 50, page: int = 1) -> Dict[str, Any]:
    """
    List all webhooks.
    
    Args:
        limit: Number of webhooks to return
        page: Page number for pagination
        
    Returns:
        List of webhooks
    """
    params = {"limit": limit, "page": page}
    return make_request("GET", "/webhooks.json", params=params)

@mcp.tool()
def get_webhook(webhook_id: int) -> Dict[str, Any]:
    """
    Get a single webhook by ID.
    
    Args:
        webhook_id: The webhook ID
        
    Returns:
        Webhook details
    """
    return make_request("GET", f"/webhooks/{webhook_id}.json")

@mcp.tool()
def create_webhook(topic: str, address: str, format: str = "json",
                   fields: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Create a new webhook.
    
    Args:
        topic: Webhook topic (orders/create, products/update, etc.)
        address: Webhook URL address
        format: Data format (json, xml)
        fields: Fields to include in webhook payload
        
    Returns:
        Created webhook
    """
    webhook_data = {
        "topic": topic,
        "address": address,
        "format": format
    }
    if fields:
        webhook_data["fields"] = fields
        
    return make_request("POST", "/webhooks.json",
                       json_data={"webhook": webhook_data})

@mcp.tool()
def update_webhook(webhook_id: int, address: Optional[str] = None,
                   fields: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Update a webhook.
    
    Args:
        webhook_id: The webhook ID
        address: New webhook URL
        fields: Updated fields list
        
    Returns:
        Updated webhook
    """
    webhook_data = {}
    if address:
        webhook_data["address"] = address
    if fields:
        webhook_data["fields"] = fields
        
    return make_request("PUT", f"/webhooks/{webhook_id}.json",
                       json_data={"webhook": webhook_data})

@mcp.tool()
def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """
    Delete a webhook.
    
    Args:
        webhook_id: The webhook ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/webhooks/{webhook_id}.json")

# ============================================================================
# SHOP ENDPOINTS
# ============================================================================

@mcp.tool()
def get_shop() -> Dict[str, Any]:
    """
    Get shop information.
    
    Returns:
        Shop details
    """
    return make_request("GET", "/shop.json")

# ============================================================================
# ORDER TRANSPORT ENDPOINTS
# ============================================================================

@mcp.tool()
def get_order_transports(order_id: int) -> Dict[str, Any]:
    """
    List transports for an order (delivery tracking).
    
    Args:
        order_id: The order ID
        
    Returns:
        List of transports
    """
    return make_request("GET", f"/orders/{order_id}/transports.json")

@mcp.tool()
def create_order_transport(order_id: int, tracking_number: str,
                           tracking_url: str, carrier: str,
                           service: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a transport (delivery tracking) for an order.
    
    Args:
        order_id: The order ID
        tracking_number: Tracking number
        tracking_url: Tracking URL
        carrier: Carrier name
        service: Service name
        
    Returns:
        Created transport
    """
    transport_data = {
        "tracking_number": tracking_number,
        "tracking_url": tracking_url,
        "carrier": carrier
    }
    if service:
        transport_data["service"] = service
        
    return make_request("POST", f"/orders/{order_id}/transports.json",
                       json_data={"transport": transport_data})

# ============================================================================
# CUSTOMER ADDRESSES ENDPOINTS
# ============================================================================

@mcp.tool()
def get_customer_addresses(customer_id: int) -> Dict[str, Any]:
    """
    List addresses for a customer.
    
    Args:
        customer_id: The customer ID
        
    Returns:
        List of addresses
    """
    return make_request("GET", f"/customers/{customer_id}/addresses.json")

@mcp.tool()
def get_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    """
    Get a single customer address.
    
    Args:
        customer_id: The customer ID
        address_id: The address ID
        
    Returns:
        Address details
    """
    return make_request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")

@mcp.tool()
def create_customer_address(customer_id: int, address1: str, city: str,
                            province: str, country: str, zip_code: str,
                            first_name: Optional[str] = None,
                            last_name: Optional[str] = None,
                            phone: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a customer address.
    
    Args:
        customer_id: The customer ID
        address1: Street address
        city: City
        province: Province/state
        country: Country
        zip_code: Postal code
        first_name: First name
        last_name: Last name
        phone: Phone number
        
    Returns:
        Created address
    """
    address_data = {
        "address1": address1,
        "city": city,
        "province": province,
        "country": country,
        "zip": zip_code
    }
    if first_name:
        address_data["first_name"] = first_name
    if last_name:
        address_data["last_name"] = last_name
    if phone:
        address_data["phone"] = phone
        
    return make_request("POST", f"/customers/{customer_id}/addresses.json",
                       json_data={"address": address_data})

@mcp.tool()
def update_customer_address(customer_id: int, address_id: int,
                            address1: Optional[str] = None,
                            city: Optional[str] = None,
                            phone: Optional[str] = None) -> Dict[str, Any]:
    """
    Update a customer address.
    
    Args:
        customer_id: The customer ID
        address_id: The address ID
        address1: New address1
        city: New city
        phone: New phone
        
    Returns:
        Updated address
    """
    address_data = {}
    if address1:
        address_data["address1"] = address1
    if city:
        address_data["city"] = city
    if phone:
        address_data["phone"] = phone
        
    return make_request("PUT", f"/customers/{customer_id}/addresses/{address_id}.json",
                       json_data={"address": address_data})

@mcp.tool()
def delete_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    """
    Delete a customer address.
    
    Args:
        customer_id: The customer ID
        address_id: The address ID
        
    Returns:
        Deletion status
    """
    return make_request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")

# ============================================================================
# FULFILLMENT ORDERS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_fulfillment_orders(limit: int = 50, status: str = "unfulfilled") -> Dict[str, Any]:
    """
    List fulfillment orders.
    
    Args:
        limit: Number of orders to return
        status: Filter by status (unfulfilled, fulfilled, partial, canceled)
        
    Returns:
        List of fulfillment orders
    """
    params = {"limit": limit, "status": status}
    return make_request("GET", "/fulfillment_orders.json", params=params)

@mcp.tool()
def get_fulfillment_order(fulfillment_order_id: int) -> Dict[str, Any]:
    """
    Get a single fulfillment order.
    
    Args:
        fulfillment_order_id: The fulfillment order ID
        
    Returns:
        Fulfillment order details
    """
    return make_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")

@mcp.tool()
def fulfill_fulfillment_order(fulfillment_order_id: int, location_id: int,
                               line_items: List[Dict]) -> Dict[str, Any]:
    """
    Create a fulfillment for a fulfillment order.
    
    Args:
        fulfillment_order_id: The fulfillment order ID
        location_id: The fulfillment location ID
        line_items: List of line items to fulfill
        
    Returns:
        Created fulfillment
    """
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/fulfillment.json",
                       json_data={
                           "location_id": location_id,
                           "line_items": line_items
                       })

# ============================================================================
# INVENTORY SETS ENDPOINTS
# ============================================================================

@mcp.tool()
def get_inventory_sets(limit: int = 50) -> Dict[str, Any]:
    """
    List inventory sets.
    
    Args:
        limit: Number of sets to return
        
    Returns:
        List of inventory sets
    """
    params = {"limit": limit}
    return make_request("GET", "/inventory_sets.json", params=params)

@mcp.tool()
def create_inventory_set(inventory_item_id: int, available: int,
                          reserved: int = 0) -> Dict[str, Any]:
    """
    Create an inventory set.
    
    Args:
        inventory_item_id: The inventory item ID
        available: Available quantity
        reserved: Reserved quantity
        
    Returns:
        Created inventory set
    """
    return make_request("POST", "/inventory_sets.json",
                       json_data={
                           "inventory_set": {
                               "inventory_item_id": inventory_item_id,
                               "available": available,
                               "reserved": reserved
                           }
                       })

if __name__ == "__main__":
    # Run the server
    mcp.run()
