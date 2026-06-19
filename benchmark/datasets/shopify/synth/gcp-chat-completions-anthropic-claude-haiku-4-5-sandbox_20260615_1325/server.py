#!/usr/bin/env python3
"""
Shopify Admin REST API MCP Server

This server provides tools for interacting with the Shopify Admin REST API.
It supports operations on products, orders, customers, fulfillments, and more.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("shopify-admin-api")

# Configuration from environment variables
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")
API_VERSION = "2026-01"
BASE_URL = f"https://{SHOPIFY_STORE_URL}/admin/api/{API_VERSION}"

# Headers for API requests
HEADERS = {
    "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
    "Content-Type": "application/json",
}


def make_request(
    method: str,
    endpoint: str,
    data: Optional[dict] = None,
    params: Optional[dict] = None,
) -> dict:
    """Make an HTTP request to the Shopify API."""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, headers=HEADERS, params=params, timeout=30)
        elif method == "POST":
            response = requests.post(url, headers=HEADERS, json=data, params=params, timeout=30)
        elif method == "PUT":
            response = requests.put(url, headers=HEADERS, json=data, params=params, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=HEADERS, params=params, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        if response.status_code in [200, 201]:
            return response.json()
        elif response.status_code == 204:
            return {"success": True}
        elif response.status_code == 404:
            return {"error": "Resource not found"}
        elif response.status_code == 422:
            return {"error": "Unprocessable entity", "details": response.json()}
        else:
            return {"error": f"API error: {response.status_code}", "details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# PRODUCTS
# ============================================================================


@mcp.tool()
def list_products(
    limit: int = 50,
    status: str = "active",
    ids: Optional[str] = None,
) -> dict:
    """
    Retrieve a list of products.
    
    Args:
        limit: Number of products to return (max 250)
        status: Filter by status (active, draft, archived)
        ids: Comma-separated product IDs to retrieve
    """
    params = {"limit": min(limit, 250), "status": status}
    if ids:
        params["ids"] = ids
    return make_request("GET", "/products.json", params=params)


@mcp.tool()
def get_product(product_id: int) -> dict:
    """Retrieve a single product by ID."""
    return make_request("GET", f"/products/{product_id}.json")


@mcp.tool()
def create_product(
    title: str,
    body_html: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    status: str = "draft",
    tags: Optional[str] = None,
) -> dict:
    """
    Create a new product.
    
    Args:
        title: The name of the product
        body_html: A description of the product (HTML supported)
        vendor: The name of the product's vendor
        product_type: A categorization for the product
        status: The status of the product (draft, active, archived)
        tags: Comma-separated tags for filtering and search
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
    return make_request("POST", "/products.json", data={"product": product})


@mcp.tool()
def update_product(
    product_id: int,
    title: Optional[str] = None,
    body_html: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    tags: Optional[str] = None,
) -> dict:
    """Update an existing product."""
    product = {}
    if title is not None:
        product["title"] = title
    if body_html is not None:
        product["body_html"] = body_html
    if vendor is not None:
        product["vendor"] = vendor
    if product_type is not None:
        product["product_type"] = product_type
    if status is not None:
        product["status"] = status
    if tags is not None:
        product["tags"] = tags
    return make_request("PUT", f"/products/{product_id}.json", data={"product": product})


@mcp.tool()
def delete_product(product_id: int) -> dict:
    """Delete a product."""
    return make_request("DELETE", f"/products/{product_id}.json")


@mcp.tool()
def get_product_count() -> dict:
    """Retrieve a count of products."""
    return make_request("GET", "/products/count.json")


# ============================================================================
# PRODUCT VARIANTS
# ============================================================================


@mcp.tool()
def list_product_variants(product_id: int, limit: int = 50) -> dict:
    """Retrieve a list of product variants for a product."""
    return make_request("GET", f"/products/{product_id}/variants.json", params={"limit": limit})


@mcp.tool()
def get_product_variant(product_id: int, variant_id: int) -> dict:
    """Retrieve a single product variant."""
    return make_request("GET", f"/products/{product_id}/variants/{variant_id}.json")


@mcp.tool()
def create_product_variant(
    product_id: int,
    price: str,
    sku: Optional[str] = None,
    option1: Optional[str] = None,
    option2: Optional[str] = None,
    option3: Optional[str] = None,
    weight: Optional[float] = None,
    weight_unit: str = "kg",
) -> dict:
    """
    Create a product variant.
    
    Args:
        product_id: The product ID
        price: The price of the variant
        sku: The SKU (stock keeping unit)
        option1: The first option value
        option2: The second option value
        option3: The third option value
        weight: The weight of the variant
        weight_unit: The unit of weight (kg, g, lb, oz)
    """
    variant = {"price": price}
    if sku:
        variant["sku"] = sku
    if option1:
        variant["option1"] = option1
    if option2:
        variant["option2"] = option2
    if option3:
        variant["option3"] = option3
    if weight is not None:
        variant["weight"] = weight
        variant["weight_unit"] = weight_unit
    return make_request("POST", f"/products/{product_id}/variants.json", data={"variant": variant})


@mcp.tool()
def update_product_variant(
    product_id: int,
    variant_id: int,
    price: Optional[str] = None,
    sku: Optional[str] = None,
    option1: Optional[str] = None,
    option2: Optional[str] = None,
    option3: Optional[str] = None,
) -> dict:
    """Update a product variant."""
    variant = {}
    if price is not None:
        variant["price"] = price
    if sku is not None:
        variant["sku"] = sku
    if option1 is not None:
        variant["option1"] = option1
    if option2 is not None:
        variant["option2"] = option2
    if option3 is not None:
        variant["option3"] = option3
    return make_request("PUT", f"/products/{product_id}/variants/{variant_id}.json", data={"variant": variant})


@mcp.tool()
def delete_product_variant(product_id: int, variant_id: int) -> dict:
    """Delete a product variant."""
    return make_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


# ============================================================================
# PRODUCT IMAGES
# ============================================================================


@mcp.tool()
def list_product_images(product_id: int) -> dict:
    """Retrieve a list of product images."""
    return make_request("GET", f"/products/{product_id}/images.json")


@mcp.tool()
def get_product_image(product_id: int, image_id: int) -> dict:
    """Retrieve a single product image."""
    return make_request("GET", f"/products/{product_id}/images/{image_id}.json")


@mcp.tool()
def create_product_image(
    product_id: int,
    src: Optional[str] = None,
    attachment: Optional[str] = None,
    alt: Optional[str] = None,
) -> dict:
    """
    Create a product image.
    
    Args:
        product_id: The product ID
        src: The URL of the image
        attachment: Base64 encoded image data
        alt: Alt text for the image
    """
    image = {}
    if src:
        image["src"] = src
    if attachment:
        image["attachment"] = attachment
    if alt:
        image["alt"] = alt
    return make_request("POST", f"/products/{product_id}/images.json", data={"image": image})


@mcp.tool()
def update_product_image(
    product_id: int,
    image_id: int,
    alt: Optional[str] = None,
) -> dict:
    """Update a product image."""
    image = {}
    if alt is not None:
        image["alt"] = alt
    return make_request("PUT", f"/products/{product_id}/images/{image_id}.json", data={"image": image})


@mcp.tool()
def delete_product_image(product_id: int, image_id: int) -> dict:
    """Delete a product image."""
    return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")


# ============================================================================
# ORDERS
# ============================================================================


@mcp.tool()
def list_orders(
    limit: int = 50,
    status: str = "any",
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
) -> dict:
    """
    Retrieve a list of orders.
    
    Args:
        limit: Number of orders to return (max 250)
        status: Filter by status (any, cancelled, fulfilled, pending, refunded, partial, unshipped, unfullfilled, processing)
        financial_status: Filter by financial status (authorized, pending, paid, refunded, voided)
        fulfillment_status: Filter by fulfillment status (fulfilled, partial, unshipped, unfullfilled, restocked, cancelled)
    """
    params = {"limit": min(limit, 250), "status": status}
    if financial_status:
        params["financial_status"] = financial_status
    if fulfillment_status:
        params["fulfillment_status"] = fulfillment_status
    return make_request("GET", "/orders.json", params=params)


@mcp.tool()
def get_order(order_id: int) -> dict:
    """Retrieve a single order by ID."""
    return make_request("GET", f"/orders/{order_id}.json")


@mcp.tool()
def create_order(
    line_items: list,
    customer: Optional[dict] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    billing_address: Optional[dict] = None,
    shipping_address: Optional[dict] = None,
    send_receipt: bool = False,
    send_fulfillment_receipt: bool = False,
) -> dict:
    """
    Create an order.
    
    Args:
        line_items: List of line items (each with title, price, quantity, etc.)
        customer: Customer object or customer ID
        email: Customer email
        phone: Customer phone
        billing_address: Billing address object
        shipping_address: Shipping address object
        send_receipt: Whether to send order confirmation
        send_fulfillment_receipt: Whether to send fulfillment confirmation
    """
    order = {
        "line_items": line_items,
        "send_receipt": send_receipt,
        "send_fulfillment_receipt": send_fulfillment_receipt,
    }
    if customer:
        order["customer"] = customer
    if email:
        order["email"] = email
    if phone:
        order["phone"] = phone
    if billing_address:
        order["billing_address"] = billing_address
    if shipping_address:
        order["shipping_address"] = shipping_address
    return make_request("POST", "/orders.json", data={"order": order})


@mcp.tool()
def update_order(
    order_id: int,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    note: Optional[str] = None,
    tags: Optional[str] = None,
) -> dict:
    """Update an order."""
    order = {}
    if email is not None:
        order["email"] = email
    if phone is not None:
        order["phone"] = phone
    if note is not None:
        order["note"] = note
    if tags is not None:
        order["tags"] = tags
    return make_request("PUT", f"/orders/{order_id}.json", data={"order": order})


@mcp.tool()
def cancel_order(order_id: int, reason: Optional[str] = None) -> dict:
    """
    Cancel an order.
    
    Args:
        order_id: The order ID
        reason: The reason for cancellation (customer, fraud, inventory, declined, other)
    """
    data = {}
    if reason:
        data["reason"] = reason
    return make_request("POST", f"/orders/{order_id}/cancel.json", data=data)


@mcp.tool()
def close_order(order_id: int) -> dict:
    """Close an order."""
    return make_request("POST", f"/orders/{order_id}/close.json")


@mcp.tool()
def open_order(order_id: int) -> dict:
    """Re-open a closed order."""
    return make_request("POST", f"/orders/{order_id}/open.json")


@mcp.tool()
def delete_order(order_id: int) -> dict:
    """Delete an order."""
    return make_request("DELETE", f"/orders/{order_id}.json")


@mcp.tool()
def get_order_count(status: str = "any") -> dict:
    """Retrieve a count of orders."""
    return make_request("GET", "/orders/count.json", params={"status": status})


# ============================================================================
# CUSTOMERS
# ============================================================================


@mcp.tool()
def list_customers(limit: int = 50) -> dict:
    """Retrieve a list of customers."""
    return make_request("GET", "/customers.json", params={"limit": min(limit, 250)})


@mcp.tool()
def get_customer(customer_id: int) -> dict:
    """Retrieve a single customer by ID."""
    return make_request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def create_customer(
    email: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    note: Optional[str] = None,
    tags: Optional[str] = None,
    tax_exempt: bool = False,
) -> dict:
    """
    Create a customer.
    
    Args:
        email: The customer's email address
        first_name: The customer's first name
        last_name: The customer's last name
        phone: The customer's phone number
        note: A note about the customer
        tags: Tags for the customer
        tax_exempt: Whether the customer is tax exempt
    """
    customer = {"email": email, "tax_exempt": tax_exempt}
    if first_name:
        customer["first_name"] = first_name
    if last_name:
        customer["last_name"] = last_name
    if phone:
        customer["phone"] = phone
    if note:
        customer["note"] = note
    if tags:
        customer["tags"] = tags
    return make_request("POST", "/customers.json", data={"customer": customer})


@mcp.tool()
def update_customer(
    customer_id: int,
    email: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    note: Optional[str] = None,
    tags: Optional[str] = None,
) -> dict:
    """Update a customer."""
    customer = {}
    if email is not None:
        customer["email"] = email
    if first_name is not None:
        customer["first_name"] = first_name
    if last_name is not None:
        customer["last_name"] = last_name
    if phone is not None:
        customer["phone"] = phone
    if note is not None:
        customer["note"] = note
    if tags is not None:
        customer["tags"] = tags
    return make_request("PUT", f"/customers/{customer_id}.json", data={"customer": customer})


@mcp.tool()
def search_customers(query: str) -> dict:
    """
    Search for customers.
    
    Args:
        query: Search query (e.g., "email:bob@example.com" or "name:Bob")
    """
    return make_request("GET", "/customers/search.json", params={"query": query})


@mcp.tool()
def get_customer_orders(customer_id: int) -> dict:
    """Retrieve all orders for a customer."""
    return make_request("GET", f"/customers/{customer_id}/orders.json")


@mcp.tool()
def get_customer_count() -> dict:
    """Retrieve a count of customers."""
    return make_request("GET", "/customers/count.json")


# ============================================================================
# CUSTOMER ADDRESSES
# ============================================================================


@mcp.tool()
def list_customer_addresses(customer_id: int) -> dict:
    """Retrieve a list of addresses for a customer."""
    return make_request("GET", f"/customers/{customer_id}/addresses.json")


@mcp.tool()
def get_customer_address(customer_id: int, address_id: int) -> dict:
    """Retrieve a single customer address."""
    return make_request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


@mcp.tool()
def create_customer_address(
    customer_id: int,
    address1: str,
    city: str,
    province: str,
    zip: str,
    country: str,
    address2: Optional[str] = None,
    company: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
) -> dict:
    """Create a customer address."""
    address = {
        "address1": address1,
        "city": city,
        "province": province,
        "zip": zip,
        "country": country,
    }
    if address2:
        address["address2"] = address2
    if company:
        address["company"] = company
    if first_name:
        address["first_name"] = first_name
    if last_name:
        address["last_name"] = last_name
    if phone:
        address["phone"] = phone
    return make_request("POST", f"/customers/{customer_id}/addresses.json", data={"address": address})


@mcp.tool()
def update_customer_address(
    customer_id: int,
    address_id: int,
    address1: Optional[str] = None,
    city: Optional[str] = None,
    province: Optional[str] = None,
    zip: Optional[str] = None,
    country: Optional[str] = None,
) -> dict:
    """Update a customer address."""
    address = {}
    if address1 is not None:
        address["address1"] = address1
    if city is not None:
        address["city"] = city
    if province is not None:
        address["province"] = province
    if zip is not None:
        address["zip"] = zip
    if country is not None:
        address["country"] = country
    return make_request("PUT", f"/customers/{customer_id}/addresses/{address_id}.json", data={"address": address})


@mcp.tool()
def delete_customer_address(customer_id: int, address_id: int) -> dict:
    """Delete a customer address."""
    return make_request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")


# ============================================================================
# FULFILLMENT ORDERS
# ============================================================================


@mcp.tool()
def list_fulfillment_orders(order_id: int) -> dict:
    """Retrieve fulfillment orders for an order."""
    return make_request("GET", f"/orders/{order_id}/fulfillment_orders.json")


@mcp.tool()
def get_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Retrieve a single fulfillment order."""
    return make_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


@mcp.tool()
def cancel_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Cancel a fulfillment order."""
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


@mcp.tool()
def close_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Mark a fulfillment order as incomplete."""
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json")


@mcp.tool()
def open_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Mark a fulfillment order as open."""
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")


@mcp.tool()
def hold_fulfillment_order(
    fulfillment_order_id: int,
    reason: Optional[str] = None,
    reason_notes: Optional[str] = None,
) -> dict:
    """
    Hold fulfillment of a fulfillment order.
    
    Args:
        fulfillment_order_id: The fulfillment order ID
        reason: The reason for the hold
        reason_notes: Additional notes about the hold
    """
    data = {}
    if reason:
        data["reason"] = reason
    if reason_notes:
        data["reason_notes"] = reason_notes
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", data=data)


@mcp.tool()
def release_fulfillment_order_hold(fulfillment_order_id: int) -> dict:
    """Release all holds on a fulfillment order."""
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")


@mcp.tool()
def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int) -> dict:
    """Move a fulfillment order to a new location."""
    return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/move.json", data={"new_location_id": new_location_id})


# ============================================================================
# FULFILLMENTS
# ============================================================================


@mcp.tool()
def list_fulfillments(order_id: int) -> dict:
    """Retrieve fulfillments for an order."""
    return make_request("GET", f"/orders/{order_id}/fulfillments.json")


@mcp.tool()
def get_fulfillment(order_id: int, fulfillment_id: int) -> dict:
    """Retrieve a single fulfillment."""
    return make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


@mcp.tool()
def create_fulfillment(
    order_id: int,
    line_items_by_fulfillment_order: list,
    tracking_info: Optional[dict] = None,
) -> dict:
    """
    Create a fulfillment.
    
    Args:
        order_id: The order ID
        line_items_by_fulfillment_order: List of fulfillment order line items
        tracking_info: Tracking information (number, company, url)
    """
    fulfillment = {"line_items_by_fulfillment_order": line_items_by_fulfillment_order}
    if tracking_info:
        fulfillment["tracking_info"] = tracking_info
    return make_request("POST", f"/orders/{order_id}/fulfillments.json", data={"fulfillment": fulfillment})


@mcp.tool()
def update_fulfillment_tracking(
    order_id: int,
    fulfillment_id: int,
    tracking_number: Optional[str] = None,
    tracking_company: Optional[str] = None,
    tracking_url: Optional[str] = None,
) -> dict:
    """Update tracking information for a fulfillment."""
    tracking_info = {}
    if tracking_number:
        tracking_info["number"] = tracking_number
    if tracking_company:
        tracking_info["company"] = tracking_company
    if tracking_url:
        tracking_info["url"] = tracking_url
    return make_request("POST", f"/orders/{order_id}/fulfillments/{fulfillment_id}/update_tracking.json", data={"tracking_info": tracking_info})


# ============================================================================
# REFUNDS
# ============================================================================


@mcp.tool()
def list_refunds(order_id: int) -> dict:
    """Retrieve refunds for an order."""
    return make_request("GET", f"/orders/{order_id}/refunds.json")


@mcp.tool()
def get_refund(order_id: int, refund_id: int) -> dict:
    """Retrieve a single refund."""
    return make_request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")


@mcp.tool()
def create_refund(
    order_id: int,
    note: Optional[str] = None,
    notify: bool = True,
    refund_line_items: Optional[list] = None,
) -> dict:
    """
    Create a refund.
    
    Args:
        order_id: The order ID
        note: A note about the refund
        notify: Whether to notify the customer
        refund_line_items: List of line items to refund
    """
    refund = {"notify": notify}
    if note:
        refund["note"] = note
    if refund_line_items:
        refund["refund_line_items"] = refund_line_items
    return make_request("POST", f"/orders/{order_id}/refunds.json", data={"refund": refund})


# ============================================================================
# COLLECTIONS
# ============================================================================


@mcp.tool()
def list_collections(limit: int = 50) -> dict:
    """Retrieve a list of collections."""
    return make_request("GET", "/collections.json", params={"limit": min(limit, 250)})


@mcp.tool()
def get_collection(collection_id: int) -> dict:
    """Retrieve a single collection."""
    return make_request("GET", f"/collections/{collection_id}.json")


@mcp.tool()
def get_collection_products(collection_id: int, limit: int = 50) -> dict:
    """Retrieve products in a collection."""
    return make_request("GET", f"/collections/{collection_id}/products.json", params={"limit": min(limit, 250)})


# ============================================================================
# CUSTOM COLLECTIONS
# ============================================================================


@mcp.tool()
def list_custom_collections(limit: int = 50) -> dict:
    """Retrieve a list of custom collections."""
    return make_request("GET", "/custom_collections.json", params={"limit": min(limit, 250)})


@mcp.tool()
def get_custom_collection(collection_id: int) -> dict:
    """Retrieve a single custom collection."""
    return make_request("GET", f"/custom_collections/{collection_id}.json")


@mcp.tool()
def create_custom_collection(
    title: str,
    body_html: Optional[str] = None,
    published: bool = True,
) -> dict:
    """
    Create a custom collection.
    
    Args:
        title: The name of the collection
        body_html: The description of the collection
        published: Whether the collection is published
    """
    collection = {"title": title, "published": published}
    if body_html:
        collection["body_html"] = body_html
    return make_request("POST", "/custom_collections.json", data={"custom_collection": collection})


@mcp.tool()
def update_custom_collection(
    collection_id: int,
    title: Optional[str] = None,
    body_html: Optional[str] = None,
    published: Optional[bool] = None,
) -> dict:
    """Update a custom collection."""
    collection = {}
    if title is not None:
        collection["title"] = title
    if body_html is not None:
        collection["body_html"] = body_html
    if published is not None:
        collection["published"] = published
    return make_request("PUT", f"/custom_collections/{collection_id}.json", data={"custom_collection": collection})


@mcp.tool()
def delete_custom_collection(collection_id: int) -> dict:
    """Delete a custom collection."""
    return make_request("DELETE", f"/custom_collections/{collection_id}.json")


# ============================================================================
# COLLECTS (Collection membership)
# ============================================================================


@mcp.tool()
def list_collects(collection_id: Optional[int] = None, product_id: Optional[int] = None) -> dict:
    """
    Retrieve collects (collection memberships).
    
    Args:
        collection_id: Filter by collection ID
        product_id: Filter by product ID
    """
    params = {}
    if collection_id:
        params["collection_id"] = collection_id
    if product_id:
        params["product_id"] = product_id
    return make_request("GET", "/collects.json", params=params)


@mcp.tool()
def create_collect(collection_id: int, product_id: int) -> dict:
    """Add a product to a collection."""
    return make_request("POST", "/collects.json", data={"collect": {"collection_id": collection_id, "product_id": product_id}})


@mcp.tool()
def delete_collect(collect_id: int) -> dict:
    """Remove a product from a collection."""
    return make_request("DELETE", f"/collects/{collect_id}.json")


# ============================================================================
# INVENTORY ITEMS
# ============================================================================


@mcp.tool()
def list_inventory_items(ids: Optional[str] = None, limit: int = 50) -> dict:
    """
    Retrieve inventory items.
    
    Args:
        ids: Comma-separated inventory item IDs
        limit: Number of items to return
    """
    params = {"limit": min(limit, 250)}
    if ids:
        params["ids"] = ids
    return make_request("GET", "/inventory_items.json", params=params)


@mcp.tool()
def get_inventory_item(inventory_item_id: int) -> dict:
    """Retrieve a single inventory item."""
    return make_request("GET", f"/inventory_items/{inventory_item_id}.json")


@mcp.tool()
def update_inventory_item(
    inventory_item_id: int,
    sku: Optional[str] = None,
    tracked: Optional[bool] = None,
) -> dict:
    """Update an inventory item."""
    item = {}
    if sku is not None:
        item["sku"] = sku
    if tracked is not None:
        item["tracked"] = tracked
    return make_request("PUT", f"/inventory_items/{inventory_item_id}.json", data={"inventory_item": item})


# ============================================================================
# INVENTORY LEVELS
# ============================================================================


@mcp.tool()
def list_inventory_levels(inventory_item_ids: Optional[str] = None) -> dict:
    """
    Retrieve inventory levels.
    
    Args:
        inventory_item_ids: Comma-separated inventory item IDs
    """
    params = {}
    if inventory_item_ids:
        params["inventory_item_ids"] = inventory_item_ids
    return make_request("GET", "/inventory_levels.json", params=params)


@mcp.tool()
def adjust_inventory_level(
    inventory_item_id: int,
    location_id: int,
    available_adjustment: int,
) -> dict:
    """
    Adjust inventory level.
    
    Args:
        inventory_item_id: The inventory item ID
        location_id: The location ID
        available_adjustment: The quantity adjustment
    """
    return make_request("POST", "/inventory_levels/adjust.json", data={
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available_adjustment": available_adjustment,
    })


# ============================================================================
# LOCATIONS
# ============================================================================


@mcp.tool()
def list_locations() -> dict:
    """Retrieve a list of locations."""
    return make_request("GET", "/locations.json")


@mcp.tool()
def get_location(location_id: int) -> dict:
    """Retrieve a single location."""
    return make_request("GET", f"/locations/{location_id}.json")


# ============================================================================
# DRAFT ORDERS
# ============================================================================


@mcp.tool()
def list_draft_orders(status: str = "open", limit: int = 50) -> dict:
    """
    Retrieve draft orders.
    
    Args:
        status: Filter by status (open, invoice_sent, completed, cancelled, expired)
        limit: Number of draft orders to return
    """
    return make_request("GET", "/draft_orders.json", params={"status": status, "limit": min(limit, 250)})


@mcp.tool()
def get_draft_order(draft_order_id: int) -> dict:
    """Retrieve a single draft order."""
    return make_request("GET", f"/draft_orders/{draft_order_id}.json")


@mcp.tool()
def create_draft_order(
    line_items: list,
    customer: Optional[dict] = None,
    email: Optional[str] = None,
    note: Optional[str] = None,
) -> dict:
    """
    Create a draft order.
    
    Args:
        line_items: List of line items
        customer: Customer object
        email: Customer email
        note: A note about the draft order
    """
    draft_order = {"line_items": line_items}
    if customer:
        draft_order["customer"] = customer
    if email:
        draft_order["email"] = email
    if note:
        draft_order["note"] = note
    return make_request("POST", "/draft_orders.json", data={"draft_order": draft_order})


@mcp.tool()
def update_draft_order(
    draft_order_id: int,
    note: Optional[str] = None,
) -> dict:
    """Update a draft order."""
    draft_order = {}
    if note is not None:
        draft_order["note"] = note
    return make_request("PUT", f"/draft_orders/{draft_order_id}.json", data={"draft_order": draft_order})


@mcp.tool()
def delete_draft_order(draft_order_id: int) -> dict:
    """Delete a draft order."""
    return make_request("DELETE", f"/draft_orders/{draft_order_id}.json")


@mcp.tool()
def send_draft_order_invoice(draft_order_id: int) -> dict:
    """Send an invoice for a draft order."""
    return make_request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json")


@mcp.tool()
def complete_draft_order(draft_order_id: int, payment_pending: bool = False) -> dict:
    """
    Complete a draft order.
    
    Args:
        draft_order_id: The draft order ID
        payment_pending: Whether payment is pending
    """
    return make_request("PUT", f"/draft_orders/{draft_order_id}/complete.json", data={"payment_pending": payment_pending})


# ============================================================================
# PRICE RULES
# ============================================================================


@mcp.tool()
def list_price_rules(limit: int = 50) -> dict:
    """Retrieve a list of price rules."""
    return make_request("GET", "/price_rules.json", params={"limit": min(limit, 250)})


@mcp.tool()
def get_price_rule(price_rule_id: int) -> dict:
    """Retrieve a single price rule."""
    return make_request("GET", f"/price_rules/{price_rule_id}.json")


@mcp.tool()
def create_price_rule(
    title: str,
    target_type: str,
    target_selection: str,
    allocation_method: str,
    value: str,
    value_type: str,
    starts_at: str,
    ends_at: Optional[str] = None,
) -> dict:
    """
    Create a price rule.
    
    Args:
        title: The name of the price rule
        target_type: The type of target (line_item, shipping_line)
        target_selection: The selection type (all, entitled)
        allocation_method: How the discount is allocated (across, each)
        value: The discount value
        value_type: The type of value (fixed_amount, percentage)
        starts_at: When the rule starts (ISO 8601)
        ends_at: When the rule ends (ISO 8601)
    """
    rule = {
        "title": title,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "value": value,
        "value_type": value_type,
        "starts_at": starts_at,
    }
    if ends_at:
        rule["ends_at"] = ends_at
    return make_request("POST", "/price_rules.json", data={"price_rule": rule})


@mcp.tool()
def update_price_rule(
    price_rule_id: int,
    title: Optional[str] = None,
    value: Optional[str] = None,
    ends_at: Optional[str] = None,
) -> dict:
    """Update a price rule."""
    rule = {}
    if title is not None:
        rule["title"] = title
    if value is not None:
        rule["value"] = value
    if ends_at is not None:
        rule["ends_at"] = ends_at
    return make_request("PUT", f"/price_rules/{price_rule_id}.json", data={"price_rule": rule})


@mcp.tool()
def delete_price_rule(price_rule_id: int) -> dict:
    """Delete a price rule."""
    return make_request("DELETE", f"/price_rules/{price_rule_id}.json")


# ============================================================================
# DISCOUNT CODES
# ============================================================================


@mcp.tool()
def list_discount_codes(price_rule_id: int) -> dict:
    """Retrieve discount codes for a price rule."""
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json")


@mcp.tool()
def get_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """Retrieve a single discount code."""
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


@mcp.tool()
def create_discount_code(
    price_rule_id: int,
    code: str,
    usage_limit: Optional[int] = None,
) -> dict:
    """
    Create a discount code.
    
    Args:
        price_rule_id: The price rule ID
        code: The discount code
        usage_limit: Maximum number of uses
    """
    discount_code = {"code": code}
    if usage_limit is not None:
        discount_code["usage_limit"] = usage_limit
    return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", data={"discount_code": discount_code})


@mcp.tool()
def update_discount_code(
    price_rule_id: int,
    discount_code_id: int,
    code: Optional[str] = None,
    usage_limit: Optional[int] = None,
) -> dict:
    """Update a discount code."""
    discount_code = {}
    if code is not None:
        discount_code["code"] = code
    if usage_limit is not None:
        discount_code["usage_limit"] = usage_limit
    return make_request("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", data={"discount_code": discount_code})


@mcp.tool()
def delete_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """Delete a discount code."""
    return make_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


# ============================================================================
# WEBHOOKS
# ============================================================================


@mcp.tool()
def list_webhooks() -> dict:
    """Retrieve a list of webhooks."""
    return make_request("GET", "/webhooks.json")


@mcp.tool()
def get_webhook(webhook_id: int) -> dict:
    """Retrieve a single webhook."""
    return make_request("GET", f"/webhooks/{webhook_id}.json")


@mcp.tool()
def create_webhook(
    topic: str,
    address: str,
    format: str = "json",
) -> dict:
    """
    Create a webhook.
    
    Args:
        topic: The webhook topic (e.g., orders/create, products/update)
        address: The URL to send webhook data to
        format: The format of the webhook (json, xml)
    """
    webhook = {"topic": topic, "address": address, "format": format}
    return make_request("POST", "/webhooks.json", data={"webhook": webhook})


@mcp.tool()
def update_webhook(
    webhook_id: int,
    address: Optional[str] = None,
) -> dict:
    """Update a webhook."""
    webhook = {}
    if address is not None:
        webhook["address"] = address
    return make_request("PUT", f"/webhooks/{webhook_id}.json", data={"webhook": webhook})


@mcp.tool()
def delete_webhook(webhook_id: int) -> dict:
    """Delete a webhook."""
    return make_request("DELETE", f"/webhooks/{webhook_id}.json")


# ============================================================================
# METAFIELDS
# ============================================================================


@mcp.tool()
def list_metafields(
    owner_resource: str,
    owner_id: int,
) -> dict:
    """
    Retrieve metafields for a resource.
    
    Args:
        owner_resource: The resource type (product, order, customer, etc.)
        owner_id: The resource ID
    """
    return make_request("GET", f"/{owner_resource}s/{owner_id}/metafields.json")


@mcp.tool()
def get_metafield(
    owner_resource: str,
    owner_id: int,
    metafield_id: int,
) -> dict:
    """Retrieve a single metafield."""
    return make_request("GET", f"/{owner_resource}s/{owner_id}/metafields/{metafield_id}.json")


@mcp.tool()
def create_metafield(
    owner_resource: str,
    owner_id: int,
    namespace: str,
    key: str,
    value: str,
    type: str,
    description: Optional[str] = None,
) -> dict:
    """
    Create a metafield.
    
    Args:
        owner_resource: The resource type (product, order, customer, etc.)
        owner_id: The resource ID
        namespace: The namespace for the metafield
        key: The key for the metafield
        value: The value of the metafield
        type: The type of the metafield
        description: A description of the metafield
    """
    metafield = {
        "namespace": namespace,
        "key": key,
        "value": value,
        "type": type,
    }
    if description:
        metafield["description"] = description
    return make_request("POST", f"/{owner_resource}s/{owner_id}/metafields.json", data={"metafield": metafield})


@mcp.tool()
def update_metafield(
    owner_resource: str,
    owner_id: int,
    metafield_id: int,
    value: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a metafield."""
    metafield = {}
    if value is not None:
        metafield["value"] = value
    if description is not None:
        metafield["description"] = description
    return make_request("PUT", f"/{owner_resource}s/{owner_id}/metafields/{metafield_id}.json", data={"metafield": metafield})


@mcp.tool()
def delete_metafield(
    owner_resource: str,
    owner_id: int,
    metafield_id: int,
) -> dict:
    """Delete a metafield."""
    return make_request("DELETE", f"/{owner_resource}s/{owner_id}/metafields/{metafield_id}.json")


# ============================================================================
# SHOP
# ============================================================================


@mcp.tool()
def get_shop() -> dict:
    """Retrieve shop information."""
    return make_request("GET", "/shop.json")


# ============================================================================
# TRANSACTIONS
# ============================================================================


@mcp.tool()
def list_transactions(order_id: int) -> dict:
    """Retrieve transactions for an order."""
    return make_request("GET", f"/orders/{order_id}/transactions.json")


@mcp.tool()
def get_transaction(order_id: int, transaction_id: int) -> dict:
    """Retrieve a single transaction."""
    return make_request("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")


@mcp.tool()
def create_transaction(
    order_id: int,
    amount: str,
    kind: str,
    gateway: Optional[str] = None,
) -> dict:
    """
    Create a transaction.
    
    Args:
        order_id: The order ID
        amount: The transaction amount
        kind: The transaction kind (sale, capture, void, refund, authorization)
        gateway: The payment gateway
    """
    transaction = {"amount": amount, "kind": kind}
    if gateway:
        transaction["gateway"] = gateway
    return make_request("POST", f"/orders/{order_id}/transactions.json", data={"transaction": transaction})


if __name__ == "__main__":
    mcp.run()
