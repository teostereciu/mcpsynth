"""
Shopify Admin REST API MCP Server

This server provides tools for interacting with the Shopify Admin REST API.
"""

import os
import requests
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="shopify", include_in_builtin_tools_response=False)

# Base URL for Shopify Admin API
BASE_URL = os.getenv("SHOPIFY_STORE_URL", "").rstrip("/")
if BASE_URL:
    BASE_URL = f"https://{BASE_URL}/admin/api/2026-01"
else:
    BASE_URL = "https://{SHOPIFY_STORE_URL}/admin/api/2026-01"

# Access token
ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")


def _make_request(method, endpoint, params=None, json_body=None):
    """
    Make a request to the Shopify Admin API.
    Returns the JSON response or an error dict.
    """
    if not ACCESS_TOKEN:
        return {"error": "SHOPIFY_ACCESS_TOKEN environment variable is not set"}
    
    if not BASE_URL or BASE_URL.startswith("https://{"):
        return {"error": "SHOPIFY_STORE_URL environment variable is not set or invalid"}
    
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=json_body, params=params, timeout=30)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=json_body, params=params, timeout=30)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        # Handle response
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except ValueError:
                return {"error": "Failed to parse JSON response"}
        else:
            # Return error info from Shopify
            try:
                error_data = response.json()
                return {"error": error_data}
            except ValueError:
                return {"error": f"API request failed with status {response.status_code}: {response.text}"}
                
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection error occurred"}
    except Exception as e:
        return {"error": str(e)}


# ============================================
# PRODUCT MANAGEMENT
# ============================================

@mcp.tool()
def get_products(limit=50, since_id=None, status="active", fields=None):
    """
    Retrieve a list of products from the store.
    
    Args:
        limit (int): Number of products to return (default: 50, max: 250)
        since_id (int): Return products with ID greater than this
        status (str): Product status - 'active', 'archived', 'draft'
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing products list and count
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if status:
        params["status"] = status
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/products.json", params=params)


@mcp.tool()
def get_product(product_id, fields=None):
    """
    Retrieve a single product by ID.
    
    Args:
        product_id (int): The ID of the product to retrieve
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the product
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/products/{product_id}.json", params=params)


@mcp.tool()
def create_product(
    title,
    body_html=None,
    vendor=None,
    product_type=None,
    status="draft",
    tags=None,
    options=None,
    variants=None,
    images=None,
    published=False
):
    """
    Create a new product.
    
    Args:
        title (str): The name of the product (required)
        body_html (str): HTML description of the product
        vendor (str): Product vendor name
        product_type (str): Product category
        status (str): Product status - 'active', 'archived', 'draft'
        tags (str): Comma-separated list of tags
        options (list): List of option names
        variants (list): List of variant data
        images (list): List of image data
        published (bool): Whether to publish the product
    
    Returns:
        dict: Response containing the created product
    """
    product = {"title": title, "status": status}
    
    if body_html:
        product["body_html"] = body_html
    if vendor:
        product["vendor"] = vendor
    if product_type:
        product["product_type"] = product_type
    if tags:
        product["tags"] = tags
    if options:
        product["options"] = options
    if variants:
        product["variants"] = variants
    if images:
        product["images"] = images
    
    if not published:
        product["published"] = False
    
    return _make_request("POST", "/products.json", json_body={"product": product})


@mcp.tool()
def update_product(product_id, **kwargs):
    """
    Update an existing product.
    
    Args:
        product_id (int): The ID of the product to update
        **kwargs: Product fields to update (e.g., title="New Title")
    
    Returns:
        dict: Response containing the updated product
    """
    return _make_request("PUT", f"/products/{product_id}.json", json_body={"product": kwargs})


@mcp.tool()
def delete_product(product_id):
    """
    Delete a product by ID.
    
    Args:
        product_id (int): The ID of the product to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/products/{product_id}.json")


@mcp.tool()
def get_product_count(status="active"):
    """
    Get the count of products.
    
    Args:
        status (str): Filter by status - 'active', 'archived', 'draft'
    
    Returns:
        dict: Response containing count
    """
    params = {"status": status}
    return _make_request("GET", "/products/count.json", params=params)


# ============================================
# PRODUCT VARIANT MANAGEMENT
# ============================================

@mcp.tool()
def get_product_variants(product_id, limit=50, since_id=None, fields=None):
    """
    Retrieve variants for a specific product.
    
    Args:
        product_id (int): The ID of the product
        limit (int): Number of variants to return (default: 50)
        since_id (int): Return variants with ID greater than this
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing variants list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/products/{product_id}/variants.json", params=params)


@mcp.tool()
def update_product_variant(variant_id, **kwargs):
    """
    Update a product variant.
    
    Args:
        variant_id (int): The ID of the variant to update
        **kwargs: Variant fields to update (e.g., price=19.99, inventory_quantity=10)
    
    Returns:
        dict: Response containing the updated variant
    """
    return _make_request("PUT", f"/product_variants/{variant_id}.json", json_body={"variant": kwargs})


@mcp.tool()
def delete_product_variant(variant_id):
    """
    Delete a product variant by ID.
    
    Args:
        variant_id (int): The ID of the variant to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/variants/{variant_id}.json")


# ============================================
# PRODUCT IMAGE MANAGEMENT
# ============================================

@mcp.tool()
def get_product_images(product_id, limit=50, since_id=None):
    """
    Retrieve images for a specific product.
    
    Args:
        product_id (int): The ID of the product
        limit (int): Number of images to return (default: 50)
        since_id (int): Return images with ID greater than this
    
    Returns:
        dict: Response containing images list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    
    return _make_request("GET", f"/products/{product_id}/images.json", params=params)


@mcp.tool()
def create_product_image(product_id, src, position=None, alt=None):
    """
    Add an image to a product.
    
    Args:
        product_id (int): The ID of the product
        src (str): URL of the image to add
        position (int): Position of the image in the gallery
        alt (str): Alt text for the image
    
    Returns:
        dict: Response containing the created image
    """
    image = {"src": src}
    if position:
        image["position"] = position
    if alt:
        image["alt"] = alt
    
    return _make_request("POST", f"/products/{product_id}/images.json", json_body={"image": image})


@mcp.tool()
def delete_product_image(product_id, image_id):
    """
    Delete a product image by ID.
    
    Args:
        product_id (int): The ID of the product
        image_id (int): The ID of the image to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")


# ============================================
# CUSTOMER MANAGEMENT
# ============================================

@mcp.tool()
def get_customers(limit=50, since_id=None, email=None, fields=None):
    """
    Retrieve a list of customers.
    
    Args:
        limit (int): Number of customers to return (default: 50)
        since_id (int): Return customers with ID greater than this
        email (str): Filter by customer email
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing customers list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if email:
        params["email"] = email
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/customers.json", params=params)


@mcp.tool()
def get_customer(customer_id, fields=None):
    """
    Retrieve a single customer by ID.
    
    Args:
        customer_id (int): The ID of the customer to retrieve
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the customer
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/customers/{customer_id}.json", params=params)


@mcp.tool()
def create_customer(
    first_name,
    last_name,
    email,
    phone=None,
    verified_email=True,
    addresses=None,
    password=None,
    password_confirmation=None,
    send_email_welcome=False
):
    """
    Create a new customer.
    
    Args:
        first_name (str): Customer's first name
        last_name (str): Customer's last name
        email (str): Customer's email (required)
        phone (str): Customer's phone number
        verified_email (bool): Whether email is verified
        addresses (list): List of address dictionaries
        password (str): Customer's password (deprecated)
        password_confirmation (str): Password confirmation (deprecated)
        send_email_welcome (bool): Whether to send welcome email
    
    Returns:
        dict: Response containing the created customer
    """
    customer = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "verified_email": verified_email
    }
    
    if phone:
        customer["phone"] = phone
    if addresses:
        customer["addresses"] = addresses
    if password:
        customer["password"] = password
    if password_confirmation:
        customer["password_confirmation"] = password_confirmation
    if send_email_welcome:
        customer["send_email_welcome"] = send_email_welcome
    
    return _make_request("POST", "/customers.json", json_body={"customer": customer})


@mcp.tool()
def update_customer(customer_id, **kwargs):
    """
    Update an existing customer.
    
    Args:
        customer_id (int): The ID of the customer to update
        **kwargs: Customer fields to update
    
    Returns:
        dict: Response containing the updated customer
    """
    return _make_request("PUT", f"/customers/{customer_id}.json", json_body={"customer": kwargs})


@mcp.tool()
def delete_customer(customer_id):
    """
    Delete a customer by ID.
    
    Args:
        customer_id (int): The ID of the customer to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/customers/{customer_id}.json")


@mcp.tool()
def get_customer_count():
    """
    Get the count of customers.
    
    Returns:
        dict: Response containing count
    """
    return _make_request("GET", "/customers/count.json")


@mcp.tool()
def search_customers(query, limit=50):
    """
    Search for customers by query.
    
    Args:
        query (str): Search query (e.g., 'email:customer@example.com')
        limit (int): Number of results to return (default: 50)
    
    Returns:
        dict: Response containing matching customers
    """
    params = {"query": query, "limit": min(limit, 250)}
    return _make_request("GET", "/customers/search.json", params=params)


# ============================================
# ORDER MANAGEMENT
# ============================================

@mcp.tool()
def get_orders(
    status="any",
    limit=50,
    since_id=None,
    created_at_min=None,
    created_at_max=None,
    fields=None
):
    """
    Retrieve a list of orders.
    
    Args:
        status (str): Order status filter - 'any', 'open', 'closed', 'cancelled'
        limit (int): Number of orders to return (default: 50)
        since_id (int): Return orders with ID greater than this
        created_at_min (str): Filter by minimum creation date (ISO 8601)
        created_at_max (str): Filter by maximum creation date (ISO 8601)
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing orders list
    """
    params = {"status": status, "limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/orders.json", params=params)


@mcp.tool()
def get_order(order_id, fields=None):
    """
    Retrieve a single order by ID.
    
    Args:
        order_id (int): The ID of the order to retrieve
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the order
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/orders/{order_id}.json", params=params)


@mcp.tool()
def create_order(
    line_items,
    shipping_address,
    billing_address=None,
    email=None,
    send_receipt=False,
    send_fulfillment_receipt=False,
    inventory_behavior="bypass"
):
    """
    Create a new order.
    
    Args:
        line_items (list): List of line item objects
        shipping_address (dict): Shipping address
        billing_address (dict): Billing address
        email (str): Customer email
        send_receipt (bool): Whether to send order confirmation
        send_fulfillment_receipt (bool): Whether to send fulfillment confirmation
        inventory_behavior (str): 'bypass', 'decrement_ignoring_policy', 'decrement_obeying_policy'
    
    Returns:
        dict: Response containing the created order
    """
    order = {
        "line_items": line_items,
        "shipping_address": shipping_address,
        "send_receipt": send_receipt,
        "send_fulfillment_receipt": send_fulfillment_receipt,
        "inventory_behaviour": inventory_behavior
    }
    
    if billing_address:
        order["billing_address"] = billing_address
    if email:
        order["email"] = email
    
    return _make_request("POST", "/orders.json", json_body={"order": order})


@mcp.tool()
def update_order(order_id, **kwargs):
    """
    Update an existing order.
    
    Args:
        order_id (int): The ID of the order to update
        **kwargs: Order fields to update
    
    Returns:
        dict: Response containing the updated order
    """
    return _make_request("PUT", f"/orders/{order_id}.json", json_body={"order": kwargs})


@mcp.tool()
def cancel_order(order_id, reason=None):
    """
    Cancel an order.
    
    Args:
        order_id (int): The ID of the order to cancel
        reason (str): Reason for cancellation - 'customer', 'fraud', 'inventory', 'declined', 'other'
    
    Returns:
        dict: Response containing the canceled order
    """
    params = {}
    if reason:
        params["reason"] = reason
    
    return _make_request("POST", f"/orders/{order_id}/cancel.json", params=params)


@mcp.tool()
def close_order(order_id):
    """
    Close an order.
    
    Args:
        order_id (int): The ID of the order to close
    
    Returns:
        dict: Response containing the closed order
    """
    return _make_request("POST", f"/orders/{order_id}/close.json")


@mcp.tool()
def open_order(order_id):
    """
    Re-open a closed order.
    
    Args:
        order_id (int): The ID of the order to re-open
    
    Returns:
        dict: Response containing the reopened order
    """
    return _make_request("POST", f"/orders/{order_id}/open.json")


@mcp.tool()
def delete_order(order_id):
    """
    Delete an order by ID.
    
    Args:
        order_id (int): The ID of the order to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/orders/{order_id}.json")


@mcp.tool()
def get_order_count(status="any"):
    """
    Get the count of orders.
    
    Args:
        status (str): Filter by status - 'any', 'open', 'closed', 'cancelled'
    
    Returns:
        dict: Response containing count
    """
    params = {"status": status}
    return _make_request("GET", "/orders/count.json", params=params)


# ============================================
# FULFILLMENT MANAGEMENT
# ============================================

@mcp.tool()
def create_fulfillment(order_id, tracking_number=None, tracking_url=None, tracking_company=None, line_items=None, notify_customer=False):
    """
    Create a fulfillment for an order.
    
    Args:
        order_id (int): The ID of the order to fulfill
        tracking_number (str): Tracking number for the shipment
        tracking_url (str): URL for tracking the shipment
        tracking_company (str): Name of the tracking company
        line_items (list): List of line items to fulfill
        notify_customer (bool): Whether to notify customer
    
    Returns:
        dict: Response containing the created fulfillment
    """
    fulfillment = {"notify_customer": notify_customer}
    
    if tracking_number:
        fulfillment["tracking_number"] = tracking_number
    if tracking_url:
        fulfillment["tracking_url"] = tracking_url
    if tracking_company:
        fulfillment["tracking_company"] = tracking_company
    if line_items:
        fulfillment["line_items"] = line_items
    
    return _make_request("POST", f"/orders/{order_id}/fulfillments.json", json_body={"fulfillment": fulfillment})


@mcp.tool()
def get_fulfillment(order_id, fulfillment_id):
    """
    Retrieve a fulfillment by ID.
    
    Args:
        order_id (int): The ID of the order
        fulfillment_id (int): The ID of the fulfillment
    
    Returns:
        dict: Response containing the fulfillment
    """
    return _make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


@mcp.tool()
def update_fulfillment(order_id, fulfillment_id, **kwargs):
    """
    Update a fulfillment.
    
    Args:
        order_id (int): The ID of the order
        fulfillment_id (int): The ID of the fulfillment
        **kwargs: Fulfillment fields to update
    
    Returns:
        dict: Response containing the updated fulfillment
    """
    return _make_request(
        "PUT",
        f"/orders/{order_id}/fulfillments/{fulfillment_id}.json",
        json_body={"fulfillment": kwargs}
    )


@mcp.tool()
def get_fulfillments(order_id, limit=50, since_id=None, status="pending"):
    """
    Retrieve fulfillments for an order.
    
    Args:
        order_id (int): The ID of the order
        limit (int): Number of fulfillments to return (default: 50)
        since_id (int): Return fulfillments with ID greater than this
        status (str): Filter by status - 'pending', 'success', 'failure', 'cancelled'
    
    Returns:
        dict: Response containing fulfillments list
    """
    params = {"limit": min(limit, 250), "status": status}
    if since_id:
        params["since_id"] = since_id
    
    return _make_request("GET", f"/orders/{order_id}/fulfillments.json", params=params)


# ============================================
# INVENTORY MANAGEMENT
# ============================================

@mcp.tool()
def get_inventory_items(limit=50, since_id=None, fields=None):
    """
    Retrieve a list of inventory items.
    
    Args:
        limit (int): Number of items to return (default: 50)
        since_id (int): Return items with ID greater than this
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing inventory items list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/inventory_items.json", params=params)


@mcp.tool()
def get_inventory_levels(location_id=None, inventory_item_ids=None, limit=50):
    """
    Retrieve inventory levels.
    
    Args:
        location_id (int): Filter by location ID
        inventory_item_ids (list): List of inventory item IDs
        limit (int): Number of levels to return (default: 50)
    
    Returns:
        dict: Response containing inventory levels
    """
    params = {"limit": min(limit, 250)}
    if location_id:
        params["location_id"] = location_id
    if inventory_item_ids:
        params["inventory_item_ids"] = ",".join(map(str, inventory_item_ids))
    
    return _make_request("GET", "/inventory_levels.json", params=params)


@mcp.tool()
def adjust_inventory_level(inventory_item_id, location_id, adjustment):
    """
    Adjust inventory level for an item at a location.
    
    Args:
        inventory_item_id (int): The ID of the inventory item
        location_id (int): The ID of the location
        adjustment (int): Number to adjust by (positive or negative)
    
    Returns:
        dict: Response containing the adjusted inventory level
    """
    payload = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "adjustment": adjustment
    }
    
    return _make_request("POST", "/inventory_levels/adjust.json", json_body=payload)


@mcp.tool()
def set_inventory_level(inventory_item_id, location_id, available):
    """
    Set the available inventory level for an item at a location.
    
    Args:
        inventory_item_id (int): The ID of the inventory item
        location_id (int): The ID of the location
        available (int): The available quantity to set
    
    Returns:
        dict: Response containing the updated inventory level
    """
    payload = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available
    }
    
    return _make_request("POST", "/inventory_levels/set.json", json_body=payload)


# ============================================
# DISCOUNT MANAGEMENT
# ============================================

@mcp.tool()
def get_price_rules(limit=50, status="active", fields=None):
    """
    Retrieve a list of price rules (discounts).
    
    Args:
        limit (int): Number of price rules to return (default: 50)
        status (str): Filter by status - 'active', 'inactive'
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing price rules list
    """
    params = {"limit": min(limit, 250), "status": status}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/price_rules.json", params=params)


@mcp.tool()
def get_price_rule(price_rule_id, fields=None):
    """
    Retrieve a single price rule by ID.
    
    Args:
        price_rule_id (int): The ID of the price rule
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the price rule
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/price_rules/{price_rule_id}.json", params=params)


@mcp.tool()
def create_price_rule(
    title,
    target_type,
    target_selection,
    allocation_method,
    value_type,
    value,
    customer_selection="all",
    starts_at=None,
    ends_at=None,
    once_per_customer=None,
    usage_limit=None,
    conditionals=None
):
    """
    Create a new price rule (discount).
    
    Args:
        title (str): Name of the price rule
        target_type (str): 'line_item' or 'shipping_line'
        target_selection (str): 'all' or 'explicit'
        allocation_method (str): 'across' or 'each'
        value_type (str): 'percentage', 'fixed_amount', or 'shipping'
        value (str or float): Discount value
        customer_selection (str): 'all' or 'specific'
        starts_at (str): Start date in ISO 8601 format
        ends_at (str): End date in ISO 8601 format
        once_per_customer (bool): Whether the rule can only be used once per customer
        usage_limit (int): Maximum number of times the rule can be used
        conditionals (dict): Additional conditions
    
    Returns:
        dict: Response containing the created price rule
    """
    price_rule = {
        "title": title,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "value_type": value_type,
        "value": value,
        "customer_selection": customer_selection
    }
    
    if starts_at:
        price_rule["starts_at"] = starts_at
    if ends_at:
        price_rule["ends_at"] = ends_at
    if once_per_customer is not None:
        price_rule["once_per_customer"] = once_per_customer
    if usage_limit:
        price_rule["usage_limit"] = usage_limit
    if conditionals:
        price_rule["conditional"] = conditionals
    
    return _make_request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


@mcp.tool()
def update_price_rule(price_rule_id, **kwargs):
    """
    Update an existing price rule.
    
    Args:
        price_rule_id (int): The ID of the price rule to update
        **kwargs: Price rule fields to update
    
    Returns:
        dict: Response containing the updated price rule
    """
    return _make_request("PUT", f"/price_rules/{price_rule_id}.json", json_body={"price_rule": kwargs})


@mcp.tool()
def delete_price_rule(price_rule_id):
    """
    Delete a price rule by ID.
    
    Args:
        price_rule_id (int): The ID of the price rule to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/price_rules/{price_rule_id}.json")


@mcp.tool()
def get_discount_codes(price_rule_id, limit=50):
    """
    Retrieve discount codes for a price rule.
    
    Args:
        price_rule_id (int): The ID of the price rule
        limit (int): Number of codes to return (default: 50)
    
    Returns:
        dict: Response containing discount codes list
    """
    params = {"limit": min(limit, 250)}
    
    return _make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


@mcp.tool()
def create_discount_code(price_rule_id, code, usage_limit=None, starts_at=None, ends_at=None):
    """
    Create a discount code for a price rule.
    
    Args:
        price_rule_id (int): The ID of the price rule
        code (str): The discount code
        usage_limit (int): Maximum number of times the code can be used
        starts_at (str): Start date in ISO 8601 format
        ends_at (str): End date in ISO 8601 format
    
    Returns:
        dict: Response containing the created discount code
    """
    discount_code = {"code": code}
    
    if usage_limit:
        discount_code["usage_limit"] = usage_limit
    if starts_at:
        discount_code["starts_at"] = starts_at
    if ends_at:
        discount_code["ends_at"] = ends_at
    
    return _make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json_body={"discount_code": discount_code})


# ============================================
# COLLECTION MANAGEMENT
# ============================================

@mcp.tool()
def get_custom_collections(limit=50, since_id=None, fields=None):
    """
    Retrieve a list of custom collections.
    
    Args:
        limit (int): Number of collections to return (default: 50)
        since_id (int): Return collections with ID greater than this
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing custom collections list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/custom_collections.json", params=params)


@mcp.tool()
def get_custom_collection(collection_id, fields=None):
    """
    Retrieve a single custom collection by ID.
    
    Args:
        collection_id (int): The ID of the collection
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the collection
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/custom_collections/{collection_id}.json", params=params)


@mcp.tool()
def create_custom_collection(
    title,
    body_html=None,
    sort_order=None,
    image=None,
    published=None
):
    """
    Create a new custom collection.
    
    Args:
        title (str): Collection title
        body_html (str): HTML description
        sort_order (str): 'alpha-asc', 'alpha-desc', 'best-selling', 'manual', 'price-asc', 'price-desc'
        image (dict): Collection image data
        published (bool): Whether to publish the collection
    
    Returns:
        dict: Response containing the created collection
    """
    collection = {"title": title}
    
    if body_html:
        collection["body_html"] = body_html
    if sort_order:
        collection["sort_order"] = sort_order
    if image:
        collection["image"] = image
    if published is not None:
        collection["published"] = published
    
    return _make_request("POST", "/custom_collections.json", json_body={"collection": collection})


@mcp.tool()
def update_custom_collection(collection_id, **kwargs):
    """
    Update an existing custom collection.
    
    Args:
        collection_id (int): The ID of the collection to update
        **kwargs: Collection fields to update
    
    Returns:
        dict: Response containing the updated collection
    """
    return _make_request("PUT", f"/custom_collections/{collection_id}.json", json_body={"collection": kwargs})


@mcp.tool()
def delete_custom_collection(collection_id):
    """
    Delete a custom collection by ID.
    
    Args:
        collection_id (int): The ID of the collection to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/custom_collections/{collection_id}.json")


@mcp.tool()
def add_product_to_collection(collection_id, product_id):
    """
    Add a product to a custom collection.
    
    Args:
        collection_id (int): The ID of the collection
        product_id (int): The ID of the product to add
    
    Returns:
        dict: Response containing the created collect
    """
    return _make_request("POST", "/collects.json", json_body={"collect": {"collection_id": collection_id, "product_id": product_id}})


@mcp.tool()
def remove_product_from_collection(collect_id):
    """
    Remove a product from a collection.
    
    Args:
        collect_id (int): The ID of the collect relationship
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/collects/{collect_id}.json")


# ============================================
# SHOP AND STORE INFO
# ============================================

@mcp.tool()
def get_shop():
    """
    Retrieve information about the shop.
    
    Returns:
        dict: Response containing shop information
    """
    return _make_request("GET", "/shop.json")


# ============================================
# METAFIELD MANAGEMENT
# ============================================

@mcp.tool()
def get_metafields(limit=50, since_id=None, namespace=None, key=None, fields=None):
    """
    Retrieve a list of metafields.
    
    Args:
        limit (int): Number of metafields to return (default: 50)
        since_id (int): Return metafields with ID greater than this
        namespace (str): Filter by namespace
        key (str): Filter by key
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing metafields list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if namespace:
        params["namespace"] = namespace
    if key:
        params["key"] = key
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/metafields.json", params=params)


@mcp.tool()
def get_metafield(metafield_id, fields=None):
    """
    Retrieve a single metafield by ID.
    
    Args:
        metafield_id (int): The ID of the metafield
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the metafield
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/metafields/{metafield_id}.json", params=params)


@mcp.tool()
def create_metafield(
    namespace,
    key,
    value,
    type="string",
    description=None
):
    """
    Create a new metafield.
    
    Args:
        namespace (str): Namespace for the metafield
        key (str): Key/identifier for the metafield
        value (str): Value to store
        type (str): Type of value - 'string', 'integer', 'boolean', 'json_string'
        description (str): Description of the metafield
    
    Returns:
        dict: Response containing the created metafield
    """
    metafield = {
        "namespace": namespace,
        "key": key,
        "value": str(value),
        "type": type
    }
    
    if description:
        metafield["description"] = description
    
    return _make_request("POST", "/metafields.json", json_body={"metafield": metafield})


@mcp.tool()
def update_metafield(metafield_id, **kwargs):
    """
    Update an existing metafield.
    
    Args:
        metafield_id (int): The ID of the metafield to update
        **kwargs: Metafield fields to update
    
    Returns:
        dict: Response containing the updated metafield
    """
    return _make_request("PUT", f"/metafields/{metafield_id}.json", json_body={"metafield": kwargs})


@mcp.tool()
def delete_metafield(metafield_id):
    """
    Delete a metafield by ID.
    
    Args:
        metafield_id (int): The ID of the metafield to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/metafields/{metafield_id}.json")


# ============================================
# WEBHOOK MANAGEMENT
# ============================================

@mcp.tool()
def get_webhooks(limit=50, fields=None):
    """
    Retrieve a list of webhooks.
    
    Args:
        limit (int): Number of webhooks to return (default: 50)
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing webhooks list
    """
    params = {"limit": min(limit, 250)}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/webhooks.json", params=params)


@mcp.tool()
def get_webhook(webhook_id, fields=None):
    """
    Retrieve a single webhook by ID.
    
    Args:
        webhook_id (int): The ID of the webhook
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the webhook
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/webhooks/{webhook_id}.json", params=params)


@mcp.tool()
def create_webhook(
    topic,
    address,
    format="json"
):
    """
    Create a new webhook.
    
    Args:
        topic (str): The event topic (e.g., 'products/create', 'orders/create')
        address (str): The URL to send the webhook to
        format (str): Format of the payload - 'json' or 'xml'
    
    Returns:
        dict: Response containing the created webhook
    """
    webhook = {
        "topic": topic,
        "address": address,
        "format": format
    }
    
    return _make_request("POST", "/webhooks.json", json_body={"webhook": webhook})


@mcp.tool()
def update_webhook(webhook_id, **kwargs):
    """
    Update an existing webhook.
    
    Args:
        webhook_id (int): The ID of the webhook to update
        **kwargs: Webhook fields to update
    
    Returns:
        dict: Response containing the updated webhook
    """
    return _make_request("PUT", f"/webhooks/{webhook_id}.json", json_body={"webhook": kwargs})


@mcp.tool()
def delete_webhook(webhook_id):
    """
    Delete a webhook by ID.
    
    Args:
        webhook_id (int): The ID of the webhook to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/webhooks/{webhook_id}.json")


# ============================================
# TRANSACTION AND PAYMENT
# ============================================

@mcp.tool()
def get_transactions(order_id, limit=50, fields=None):
    """
    Retrieve transactions for an order.
    
    Args:
        order_id (int): The ID of the order
        limit (int): Number of transactions to return (default: 50)
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing transactions list
    """
    params = {"limit": min(limit, 250)}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/orders/{order_id}/transactions.json", params=params)


@mcp.tool()
def create_transaction(
    order_id,
    kind,
    amount,
    currency=None,
    receipt=None,
    payment_details=None,
    test=False
):
    """
    Create a transaction for an order.
    
    Args:
        order_id (int): The ID of the order
        kind (str): Transaction kind - 'authorization', 'capture', 'sale', 'refund'
        amount (str or float): Transaction amount
        currency (str): Currency code (default: shop currency)
        receipt (dict): Receipt information
        payment_details (dict): Payment details
        test (bool): Whether this is a test transaction
    
    Returns:
        dict: Response containing the created transaction
    """
    transaction = {
        "kind": kind,
        "amount": str(amount)
    }
    
    if currency:
        transaction["currency"] = currency
    if receipt:
        transaction["receipt"] = receipt
    if payment_details:
        transaction["payment_details"] = payment_details
    transaction["test"] = test
    
    return _make_request("POST", f"/orders/{order_id}/transactions.json", json_body={"transaction": transaction})


# ============================================
# REFUND MANAGEMENT
# ============================================

@mcp.tool()
def create_refund(
    order_id,
    refund_line_items=None,
    shipping=None,
    transactions=None,
    notify=False,
    restock=None
):
    """
    Create a refund for an order.
    
    Args:
        order_id (int): The ID of the order
        refund_line_items (list): List of line items to refund
        shipping (dict): Shipping refund information
        transactions (list): Transactions to refund
        notify (bool): Whether to notify customer
        restock (str): 'restore', 'do_not_restock', or None
    
    Returns:
        dict: Response containing the created refund
    """
    refund = {}
    
    if refund_line_items:
        refund["refund_line_items"] = refund_line_items
    if shipping:
        refund["shipping"] = shipping
    if transactions:
        refund["transactions"] = transactions
    refund["notify"] = notify
    if restock:
        refund["restock"] = restock
    
    return _make_request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


# ============================================
# DRAFT ORDER MANAGEMENT
# ============================================

@mcp.tool()
def get_draft_orders(limit=50, status="open", fields=None):
    """
    Retrieve a list of draft orders.
    
    Args:
        limit (int): Number of draft orders to return (default: 50)
        status (str): Filter by status - 'open', 'completed', 'cancelled'
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing draft orders list
    """
    params = {"limit": min(limit, 250), "status": status}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/draft_orders.json", params=params)


@mcp.tool()
def create_draft_order(
    line_items=None,
    shipping_address=None,
    billing_address=None,
    customer=None,
    note=None,
    tax_exempt=False,
    tax_exemptions=None,
    email=None
):
    """
    Create a new draft order.
    
    Args:
        line_items (list): List of line items
        shipping_address (dict): Shipping address
        billing_address (dict): Billing address
        customer (dict): Customer information
        note (str): Order note
        tax_exempt (bool): Whether order is tax exempt
        tax_exemptions (list): List of tax exemptions
        email (str): Customer email
    
    Returns:
        dict: Response containing the created draft order
    """
    draft_order = {}
    
    if line_items:
        draft_order["line_items"] = line_items
    if shipping_address:
        draft_order["shipping_address"] = shipping_address
    if billing_address:
        draft_order["billing_address"] = billing_address
    if customer:
        draft_order["customer"] = customer
    if note:
        draft_order["note"] = note
    draft_order["tax_exempt"] = tax_exempt
    if tax_exemptions:
        draft_order["tax_exemptions"] = tax_exemptions
    if email:
        draft_order["email"] = email
    
    return _make_request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


@mcp.tool()
def complete_draft_order(draft_order_id, send_receipt=False, send_fulfillment_receipt=False):
    """
    Complete a draft order (convert to order).
    
    Args:
        draft_order_id (int): The ID of the draft order
        send_receipt (bool): Whether to send order confirmation
        send_fulfillment_receipt (bool): Whether to send fulfillment confirmation
    
    Returns:
        dict: Response containing the completed order
    """
    params = {}
    if send_receipt:
        params["send_receipt"] = True
    if send_fulfillment_receipt:
        params["send_fulfillment_receipt"] = True
    
    return _make_request("POST", f"/draft_orders/{draft_order_id}/complete.json", params=params)


# ============================================
# LOCATION MANAGEMENT
# ============================================

@mcp.tool()
def get_locations(limit=50, fields=None):
    """
    Retrieve a list of locations.
    
    Args:
        limit (int): Number of locations to return (default: 50)
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing locations list
    """
    params = {"limit": min(limit, 250)}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/locations.json", params=params)


@mcp.tool()
def get_location(location_id, fields=None):
    """
    Retrieve a single location by ID.
    
    Args:
        location_id (int): The ID of the location
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the location
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/locations/{location_id}.json", params=params)


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
lfillment": fulfillment})


@mcp.tool()
def get_fulfillment(order_id, fulfillment_id):
    """
    Retrieve a fulfillment by ID.
    
    Args:
        order_id (int): The ID of the order
        fulfillment_id (int): The ID of the fulfillment
    
    Returns:
        dict: Response containing the fulfillment
    """
    return _make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


@mcp.tool()
def update_fulfillment(order_id, fulfillment_id, **kwargs):
    """
    Update a fulfillment.
    
    Args:
        order_id (int): The ID of the order
        fulfillment_id (int): The ID of the fulfillment
        **kwargs: Fulfillment fields to update
    
    Returns:
        dict: Response containing the updated fulfillment
    """
    return _make_request(
        "PUT",
        f"/orders/{order_id}/fulfillments/{fulfillment_id}.json",
        json_body={"fulfillment": kwargs}
    )


@mcp.tool()
def get_fulfillments(order_id, limit=50, since_id=None, status="pending"):
    """
    Retrieve fulfillments for an order.
    
    Args:
        order_id (int): The ID of the order
        limit (int): Number of fulfillments to return (default: 50)
        since_id (int): Return fulfillments with ID greater than this
        status (str): Filter by status - 'pending', 'success', 'failure', 'cancelled'
    
    Returns:
        dict: Response containing fulfillments list
    """
    params = {"limit": min(limit, 250), "status": status}
    if since_id:
        params["since_id"] = since_id
    
    return _make_request("GET", f"/orders/{order_id}/fulfillments.json", params=params)


# ============================================
# INVENTORY MANAGEMENT
# ============================================

@mcp.tool()
def get_inventory_items(limit=50, since_id=None, fields=None):
    """
    Retrieve a list of inventory items.
    
    Args:
        limit (int): Number of items to return (default: 50)
        since_id (int): Return items with ID greater than this
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing inventory items list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/inventory_items.json", params=params)


@mcp.tool()
def get_inventory_levels(location_id=None, inventory_item_ids=None, limit=50):
    """
    Retrieve inventory levels.
    
    Args:
        location_id (int): Filter by location ID
        inventory_item_ids (list): List of inventory item IDs
        limit (int): Number of levels to return (default: 50)
    
    Returns:
        dict: Response containing inventory levels
    """
    params = {"limit": min(limit, 250)}
    if location_id:
        params["location_id"] = location_id
    if inventory_item_ids:
        params["inventory_item_ids"] = ",".join(map(str, inventory_item_ids))
    
    return _make_request("GET", "/inventory_levels.json", params=params)


@mcp.tool()
def adjust_inventory_level(inventory_item_id, location_id, adjustment):
    """
    Adjust inventory level for an item at a location.
    
    Args:
        inventory_item_id (int): The ID of the inventory item
        location_id (int): The ID of the location
        adjustment (int): Number to adjust by (positive or negative)
    
    Returns:
        dict: Response containing the adjusted inventory level
    """
    payload = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "adjustment": adjustment
    }
    
    return _make_request("POST", "/inventory_levels/adjust.json", json_body=payload)


@mcp.tool()
def set_inventory_level(inventory_item_id, location_id, available):
    """
    Set the available inventory level for an item at a location.
    
    Args:
        inventory_item_id (int): The ID of the inventory item
        location_id (int): The ID of the location
        available (int): The available quantity to set
    
    Returns:
        dict: Response containing the updated inventory level
    """
    payload = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available
    }
    
    return _make_request("POST", "/inventory_levels/set.json", json_body=payload)


# ============================================
# DISCOUNT MANAGEMENT
# ============================================

@mcp.tool()
def get_price_rules(limit=50, status="active", fields=None):
    """
    Retrieve a list of price rules (discounts).
    
    Args:
        limit (int): Number of price rules to return (default: 50)
        status (str): Filter by status - 'active', 'inactive'
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing price rules list
    """
    params = {"limit": min(limit, 250), "status": status}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/price_rules.json", params=params)


@mcp.tool()
def get_price_rule(price_rule_id, fields=None):
    """
    Retrieve a single price rule by ID.
    
    Args:
        price_rule_id (int): The ID of the price rule
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the price rule
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/price_rules/{price_rule_id}.json", params=params)


@mcp.tool()
def create_price_rule(
    title,
    target_type,
    target_selection,
    allocation_method,
    value_type,
    value,
    customer_selection="all",
    starts_at=None,
    ends_at=None,
    once_per_customer=None,
    usage_limit=None,
    conditionals=None
):
    """
    Create a new price rule (discount).
    
    Args:
        title (str): Name of the price rule
        target_type (str): 'line_item' or 'shipping_line'
        target_selection (str): 'all' or 'explicit'
        allocation_method (str): 'across' or 'each'
        value_type (str): 'percentage', 'fixed_amount', or 'shipping'
        value (str or float): Discount value
        customer_selection (str): 'all' or 'specific'
        starts_at (str): Start date in ISO 8601 format
        ends_at (str): End date in ISO 8601 format
        once_per_customer (bool): Whether the rule can only be used once per customer
        usage_limit (int): Maximum number of times the rule can be used
        conditionals (dict): Additional conditions
    
    Returns:
        dict: Response containing the created price rule
    """
    price_rule = {
        "title": title,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "value_type": value_type,
        "value": value,
        "customer_selection": customer_selection
    }
    
    if starts_at:
        price_rule["starts_at"] = starts_at
    if ends_at:
        price_rule["ends_at"] = ends_at
    if once_per_customer is not None:
        price_rule["once_per_customer"] = once_per_customer
    if usage_limit:
        price_rule["usage_limit"] = usage_limit
    if conditionals:
        price_rule["conditional"] = conditionals
    
    return _make_request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


@mcp.tool()
def update_price_rule(price_rule_id, **kwargs):
    """
    Update an existing price rule.
    
    Args:
        price_rule_id (int): The ID of the price rule to update
        **kwargs: Price rule fields to update
    
    Returns:
        dict: Response containing the updated price rule
    """
    return _make_request("PUT", f"/price_rules/{price_rule_id}.json", json_body={"price_rule": kwargs})


@mcp.tool()
def delete_price_rule(price_rule_id):
    """
    Delete a price rule by ID.
    
    Args:
        price_rule_id (int): The ID of the price rule to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/price_rules/{price_rule_id}.json")


@mcp.tool()
def get_discount_codes(price_rule_id, limit=50):
    """
    Retrieve discount codes for a price rule.
    
    Args:
        price_rule_id (int): The ID of the price rule
        limit (int): Number of codes to return (default: 50)
    
    Returns:
        dict: Response containing discount codes list
    """
    params = {"limit": min(limit, 250)}
    
    return _make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


@mcp.tool()
def create_discount_code(price_rule_id, code, usage_limit=None, starts_at=None, ends_at=None):
    """
    Create a discount code for a price rule.
    
    Args:
        price_rule_id (int): The ID of the price rule
        code (str): The discount code
        usage_limit (int): Maximum number of times the code can be used
        starts_at (str): Start date in ISO 8601 format
        ends_at (str): End date in ISO 8601 format
    
    Returns:
        dict: Response containing the created discount code
    """
    discount_code = {"code": code}
    
    if usage_limit:
        discount_code["usage_limit"] = usage_limit
    if starts_at:
        discount_code["starts_at"] = starts_at
    if ends_at:
        discount_code["ends_at"] = ends_at
    
    return _make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json_body={"discount_code": discount_code})


# ============================================
# COLLECTION MANAGEMENT
# ============================================

@mcp.tool()
def get_custom_collections(limit=50, since_id=None, fields=None):
    """
    Retrieve a list of custom collections.
    
    Args:
        limit (int): Number of collections to return (default: 50)
        since_id (int): Return collections with ID greater than this
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing custom collections list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/custom_collections.json", params=params)


@mcp.tool()
def get_custom_collection(collection_id, fields=None):
    """
    Retrieve a single custom collection by ID.
    
    Args:
        collection_id (int): The ID of the collection
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the collection
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/custom_collections/{collection_id}.json", params=params)


@mcp.tool()
def create_custom_collection(
    title,
    body_html=None,
    sort_order=None,
    image=None,
    published=None
):
    """
    Create a new custom collection.
    
    Args:
        title (str): Collection title
        body_html (str): HTML description
        sort_order (str): 'alpha-asc', 'alpha-desc', 'best-selling', 'manual', 'price-asc', 'price-desc'
        image (dict): Collection image data
        published (bool): Whether to publish the collection
    
    Returns:
        dict: Response containing the created collection
    """
    collection = {"title": title}
    
    if body_html:
        collection["body_html"] = body_html
    if sort_order:
        collection["sort_order"] = sort_order
    if image:
        collection["image"] = image
    if published is not None:
        collection["published"] = published
    
    return _make_request("POST", "/custom_collections.json", json_body={"collection": collection})


@mcp.tool()
def update_custom_collection(collection_id, **kwargs):
    """
    Update an existing custom collection.
    
    Args:
        collection_id (int): The ID of the collection to update
        **kwargs: Collection fields to update
    
    Returns:
        dict: Response containing the updated collection
    """
    return _make_request("PUT", f"/custom_collections/{collection_id}.json", json_body={"collection": kwargs})


@mcp.tool()
def delete_custom_collection(collection_id):
    """
    Delete a custom collection by ID.
    
    Args:
        collection_id (int): The ID of the collection to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/custom_collections/{collection_id}.json")


@mcp.tool()
def add_product_to_collection(collection_id, product_id):
    """
    Add a product to a custom collection.
    
    Args:
        collection_id (int): The ID of the collection
        product_id (int): The ID of the product to add
    
    Returns:
        dict: Response containing the created collect
    """
    return _make_request("POST", "/collects.json", json_body={"collect": {"collection_id": collection_id, "product_id": product_id}})


@mcp.tool()
def remove_product_from_collection(collect_id):
    """
    Remove a product from a collection.
    
    Args:
        collect_id (int): The ID of the collect relationship
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/collects/{collect_id}.json")


# ============================================
# SHOP AND STORE INFO
# ============================================

@mcp.tool()
def get_shop():
    """
    Retrieve information about the shop.
    
    Returns:
        dict: Response containing shop information
    """
    return _make_request("GET", "/shop.json")


# ============================================
# METAFIELD MANAGEMENT
# ============================================

@mcp.tool()
def get_metafields(limit=50, since_id=None, namespace=None, key=None, fields=None):
    """
    Retrieve a list of metafields.
    
    Args:
        limit (int): Number of metafields to return (default: 50)
        since_id (int): Return metafields with ID greater than this
        namespace (str): Filter by namespace
        key (str): Filter by key
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing metafields list
    """
    params = {"limit": min(limit, 250)}
    if since_id:
        params["since_id"] = since_id
    if namespace:
        params["namespace"] = namespace
    if key:
        params["key"] = key
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/metafields.json", params=params)


@mcp.tool()
def get_metafield(metafield_id, fields=None):
    """
    Retrieve a single metafield by ID.
    
    Args:
        metafield_id (int): The ID of the metafield
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the metafield
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/metafields/{metafield_id}.json", params=params)


@mcp.tool()
def create_metafield(
    namespace,
    key,
    value,
    type="string",
    description=None
):
    """
    Create a new metafield.
    
    Args:
        namespace (str): Namespace for the metafield
        key (str): Key/identifier for the metafield
        value (str): Value to store
        type (str): Type of value - 'string', 'integer', 'boolean', 'json_string'
        description (str): Description of the metafield
    
    Returns:
        dict: Response containing the created metafield
    """
    metafield = {
        "namespace": namespace,
        "key": key,
        "value": str(value),
        "type": type
    }
    
    if description:
        metafield["description"] = description
    
    return _make_request("POST", "/metafields.json", json_body={"metafield": metafield})


@mcp.tool()
def update_metafield(metafield_id, **kwargs):
    """
    Update an existing metafield.
    
    Args:
        metafield_id (int): The ID of the metafield to update
        **kwargs: Metafield fields to update
    
    Returns:
        dict: Response containing the updated metafield
    """
    return _make_request("PUT", f"/metafields/{metafield_id}.json", json_body={"metafield": kwargs})


@mcp.tool()
def delete_metafield(metafield_id):
    """
    Delete a metafield by ID.
    
    Args:
        metafield_id (int): The ID of the metafield to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/metafields/{metafield_id}.json")


# ============================================
# WEBHOOK MANAGEMENT
# ============================================

@mcp.tool()
def get_webhooks(limit=50, fields=None):
    """
    Retrieve a list of webhooks.
    
    Args:
        limit (int): Number of webhooks to return (default: 50)
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing webhooks list
    """
    params = {"limit": min(limit, 250)}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/webhooks.json", params=params)


@mcp.tool()
def get_webhook(webhook_id, fields=None):
    """
    Retrieve a single webhook by ID.
    
    Args:
        webhook_id (int): The ID of the webhook
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the webhook
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/webhooks/{webhook_id}.json", params=params)


@mcp.tool()
def create_webhook(
    topic,
    address,
    format="json"
):
    """
    Create a new webhook.
    
    Args:
        topic (str): The event topic (e.g., 'products/create', 'orders/create')
        address (str): The URL to send the webhook to
        format (str): Format of the payload - 'json' or 'xml'
    
    Returns:
        dict: Response containing the created webhook
    """
    webhook = {
        "topic": topic,
        "address": address,
        "format": format
    }
    
    return _make_request("POST", "/webhooks.json", json_body={"webhook": webhook})


@mcp.tool()
def update_webhook(webhook_id, **kwargs):
    """
    Update an existing webhook.
    
    Args:
        webhook_id (int): The ID of the webhook to update
        **kwargs: Webhook fields to update
    
    Returns:
        dict: Response containing the updated webhook
    """
    return _make_request("PUT", f"/webhooks/{webhook_id}.json", json_body={"webhook": kwargs})


@mcp.tool()
def delete_webhook(webhook_id):
    """
    Delete a webhook by ID.
    
    Args:
        webhook_id (int): The ID of the webhook to delete
    
    Returns:
        dict: Response indicating success or error
    """
    return _make_request("DELETE", f"/webhooks/{webhook_id}.json")


# ============================================
# TRANSACTION AND PAYMENT
# ============================================

@mcp.tool()
def get_transactions(order_id, limit=50, fields=None):
    """
    Retrieve transactions for an order.
    
    Args:
        order_id (int): The ID of the order
        limit (int): Number of transactions to return (default: 50)
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing transactions list
    """
    params = {"limit": min(limit, 250)}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/orders/{order_id}/transactions.json", params=params)


@mcp.tool()
def create_transaction(
    order_id,
    kind,
    amount,
    currency=None,
    receipt=None,
    payment_details=None,
    test=False
):
    """
    Create a transaction for an order.
    
    Args:
        order_id (int): The ID of the order
        kind (str): Transaction kind - 'authorization', 'capture', 'sale', 'refund'
        amount (str or float): Transaction amount
        currency (str): Currency code (default: shop currency)
        receipt (dict): Receipt information
        payment_details (dict): Payment details
        test (bool): Whether this is a test transaction
    
    Returns:
        dict: Response containing the created transaction
    """
    transaction = {
        "kind": kind,
        "amount": str(amount)
    }
    
    if currency:
        transaction["currency"] = currency
    if receipt:
        transaction["receipt"] = receipt
    if payment_details:
        transaction["payment_details"] = payment_details
    transaction["test"] = test
    
    return _make_request("POST", f"/orders/{order_id}/transactions.json", json_body={"transaction": transaction})


# ============================================
# REFUND MANAGEMENT
# ============================================

@mcp.tool()
def create_refund(
    order_id,
    refund_line_items=None,
    shipping=None,
    transactions=None,
    notify=False,
    restock=None
):
    """
    Create a refund for an order.
    
    Args:
        order_id (int): The ID of the order
        refund_line_items (list): List of line items to refund
        shipping (dict): Shipping refund information
        transactions (list): Transactions to refund
        notify (bool): Whether to notify customer
        restock (str): 'restore', 'do_not_restock', or None
    
    Returns:
        dict: Response containing the created refund
    """
    refund = {}
    
    if refund_line_items:
        refund["refund_line_items"] = refund_line_items
    if shipping:
        refund["shipping"] = shipping
    if transactions:
        refund["transactions"] = transactions
    refund["notify"] = notify
    if restock:
        refund["restock"] = restock
    
    return _make_request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


# ============================================
# DRAFT ORDER MANAGEMENT
# ============================================

@mcp.tool()
def get_draft_orders(limit=50, status="open", fields=None):
    """
    Retrieve a list of draft orders.
    
    Args:
        limit (int): Number of draft orders to return (default: 50)
        status (str): Filter by status - 'open', 'completed', 'cancelled'
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing draft orders list
    """
    params = {"limit": min(limit, 250), "status": status}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/draft_orders.json", params=params)


@mcp.tool()
def create_draft_order(
    line_items=None,
    shipping_address=None,
    billing_address=None,
    customer=None,
    note=None,
    tax_exempt=False,
    tax_exemptions=None,
    email=None
):
    """
    Create a new draft order.
    
    Args:
        line_items (list): List of line items
        shipping_address (dict): Shipping address
        billing_address (dict): Billing address
        customer (dict): Customer information
        note (str): Order note
        tax_exempt (bool): Whether order is tax exempt
        tax_exemptions (list): List of tax exemptions
        email (str): Customer email
    
    Returns:
        dict: Response containing the created draft order
    """
    draft_order = {}
    
    if line_items:
        draft_order["line_items"] = line_items
    if shipping_address:
        draft_order["shipping_address"] = shipping_address
    if billing_address:
        draft_order["billing_address"] = billing_address
    if customer:
        draft_order["customer"] = customer
    if note:
        draft_order["note"] = note
    draft_order["tax_exempt"] = tax_exempt
    if tax_exemptions:
        draft_order["tax_exemptions"] = tax_exemptions
    if email:
        draft_order["email"] = email
    
    return _make_request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


@mcp.tool()
def complete_draft_order(draft_order_id, send_receipt=False, send_fulfillment_receipt=False):
    """
    Complete a draft order (convert to order).
    
    Args:
        draft_order_id (int): The ID of the draft order
        send_receipt (bool): Whether to send order confirmation
        send_fulfillment_receipt (bool): Whether to send fulfillment confirmation
    
    Returns:
        dict: Response containing the completed order
    """
    params = {}
    if send_receipt:
        params["send_receipt"] = True
    if send_fulfillment_receipt:
        params["send_fulfillment_receipt"] = True
    
    return _make_request("POST", f"/draft_orders/{draft_order_id}/complete.json", params=params)


# ============================================
# LOCATION MANAGEMENT
# ============================================

@mcp.tool()
def get_locations(limit=50, fields=None):
    """
    Retrieve a list of locations.
    
    Args:
        limit (int): Number of locations to return (default: 50)
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing locations list
    """
    params = {"limit": min(limit, 250)}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", "/locations.json", params=params)


@mcp.tool()
def get_location(location_id, fields=None):
    """
    Retrieve a single location by ID.
    
    Args:
        location_id (int): The ID of the location
        fields (str): Comma-separated list of fields to return
    
    Returns:
        dict: Response containing the location
    """
    params = {}
    if fields:
        params["fields"] = fields
    
    return _make_request("GET", f"/locations/{location_id}.json", params=params)


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
