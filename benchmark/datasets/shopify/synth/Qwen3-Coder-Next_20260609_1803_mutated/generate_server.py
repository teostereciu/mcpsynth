#!/usr/bin/env python3
"""
Generate the Shopify Admin REST API MCP Server.
This script creates a comprehensive server with all endpoints.
"""

import textwrap

SERVER_CODE = '''#!/usr/bin/env python3
"""
Shopify Admin REST API MCP Server

An MCP server for interacting with Shopify Admin REST API endpoints.
"""

import os
import json
from typing import Any
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("shopify-admin")

# Base URL for Shopify Admin API
BASE_URL = "https://{store_url}/admin/api/2026-01"


def get_access_token() -> str:
    """Get Shopify access token from environment."""
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    if not token:
        raise ValueError("SHOPIFY_ACCESS_TOKEN environment variable is not set")
    return token


def get_store_url() -> str:
    """Get Shopify store URL from environment."""
    url = os.environ.get("SHOPIFY_STORE_URL")
    if not url:
        raise ValueError("SHOPIFY_STORE_URL environment variable is not set")
    return url


def build_url(path: str) -> str:
    """Build full Shopify API URL."""
    store_url = get_store_url()
    base = BASE_URL.replace("{store_url}", store_url)
    return f"{base}{path}"


def make_request(method: str, path: str, data: dict | None = None, params: dict | None = None) -> dict:
    """Make authenticated request to Shopify API."""
    import requests
    
    url = build_url(path)
    headers = {
        "X-Shopify-Access-Token": get_access_token(),
        "Content-Type": "application/json",
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data, params=params)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data, params=params)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        
        # Try to parse JSON response
        try:
            return response.json()
        except ValueError:
            return {"message": response.text}
            
    except requests.exceptions.HTTPError as e:
        try:
            error_response = e.response.json()
            return {"error": str(error_response)}
        except (ValueError, AttributeError):
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ==================== PRODUCT ENDPOINTS ====================

@mcp.tool()
def get_product(product_id: int) -> dict:
    """Retrieve a single product by ID."""
    return make_request("GET", f"/products/{product_id}.json")


@mcp.tool()
def list_products(limit: int = 50, page: int = 1, ids: str | None = None) -> dict:
    """Retrieve a list of products."""
    params = {"limit": limit, "page": page}
    if ids:
        params["ids"] = ids
    return make_request("GET", "/products.json", params=params)


@mcp.tool()
def create_product(
    title: str,
    body_html: str | None = None,
    vendor: str | None = None,
    product_type: str | None = None,
    status: str = "draft",
    tags: str | None = None,
    variants: list[dict] | None = None,
    options: list[dict] | None = None,
    images: list[dict] | None = None,
) -> dict:
    """Create a new product."""
    product = {"title": title}
    if body_html:
        product["body_html"] = body_html
    if vendor:
        product["vendor"] = vendor
    if product_type:
        product["product_type"] = product_type
    if status:
        product["status"] = status
    if tags:
        product["tags"] = tags
    if variants:
        product["variants"] = variants
    if options:
        product["options"] = options
    if images:
        product["images"] = images
    return make_request("POST", "/products.json", data={"product": product})


@mcp.tool()
def update_product(
    product_id: int,
    title: str | None = None,
    body_html: str | None = None,
    vendor: str | None = None,
    product_type: str | None = None,
    status: str | None = None,
    tags: str | None = None,
    variants: list[dict] | None = None,
) -> dict:
    """Update an existing product."""
    product = {}
    if title:
        product["title"] = title
    if body_html:
        product["body_html"] = body_html
    if vendor:
        product["vendor"] = vendor
    if product_type:
        product["product_type"] = product_type
    if status:
        product["status"] = status
    if tags:
        product["tags"] = tags
    if variants:
        product["variants"] = variants
    return make_request("PUT", f"/products/{product_id}.json", data={"product": product})


@mcp.tool()
def delete_product(product_id: int) -> dict:
    """Delete a product."""
    return make_request("DELETE", f"/products/{product_id}.json")


# ==================== PRODUCT VARIANT ENDPOINTS ====================

@mcp.tool()
def list_product_variants(product_id: int, limit: int = 50) -> dict:
    """Retrieve a list of product variants."""
    params = {"limit": limit}
    return make_request("GET", f"/products/{product_id}/variants.json", params=params)


@mcp.tool()
def get_product_variant(variant_id: int) -> dict:
    """Retrieve a single product variant by ID."""
    return make_request("GET", f"/product_variants/{variant_id}.json")


@mcp.tool()
def update_product_variant(
    variant_id: int,
    price: float | None = None,
    inventory_quantity: int | None = None,
    sku: str | None = None,
    weight: float | None = None,
    weight_unit: str = "kg",
) -> dict:
    """Update a product variant."""
    variant = {}
    if price is not None:
        variant["price"] = str(price)
    if inventory_quantity is not None:
        variant["inventory_quantity"] = inventory_quantity
    if sku:
        variant["sku"] = sku
    if weight is not None:
        variant["weight"] = weight
    variant["weight_unit"] = weight_unit
    return make_request("PUT", f"/product_variants/{variant_id}.json", data={"variant": variant})


# ==================== PRODUCT IMAGE ENDPOINTS ====================

@mcp.tool()
def list_product_images(product_id: int) -> dict:
    """Retrieve a list of product images."""
    return make_request("GET", f"/products/{product_id}/images.json")


@mcp.tool()
def create_product_image(product_id: int, src: str, filename: str | None = None) -> dict:
    """Create a new product image."""
    image = {"src": src}
    if filename:
        image["filename"] = filename
    return make_request("POST", f"/products/{product_id}/images.json", data={"image": image})


@mcp.tool()
def delete_product_image(product_id: int, image_id: int) -> dict:
    """Delete a product image."""
    return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")


# ==================== COLLECTION ENDPOINTS ====================

@mcp.tool()
def list_custom_collections() -> dict:
    """Retrieve a list of custom collections."""
    return make_request("GET", "/custom_collections.json")


@mcp.tool()
def create_custom_collection(
    title: str,
    body_html: str | None = None,
    handle: str | None = None,
    image: dict | None = None,
) -> dict:
    """Create a new custom collection."""
    collection = {"title": title}
    if body_html:
        collection["body_html"] = body_html
    if handle:
        collection["handle"] = handle
    if image:
        collection["image"] = image
    return make_request("POST", "/custom_collections.json", data={"collection": collection})


@mcp.tool()
def update_custom_collection(
    collection_id: int,
    title: str | None = None,
    body_html: str | None = None,
    handle: str | None = None,
) -> dict:
    """Update a custom collection."""
    collection = {}
    if title:
        collection["title"] = title
    if body_html:
        collection["body_html"] = body_html
    if handle:
        collection["handle"] = handle
    return make_request("PUT", f"/custom_collections/{collection_id}.json", data={"collection": collection})


@mcp.tool()
def delete_custom_collection(collection_id: int) -> dict:
    """Delete a custom collection."""
    return make_request("DELETE", f"/custom_collections/{collection_id}.json")


# ==================== CUSTOMER ENDPOINTS ====================

@mcp.tool()
def get_customer(customer_id: int) -> dict:
    """Retrieve a single customer by ID."""
    return make_request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def list_customers(limit: int = 50, page: int = 1, email: str | None = None) -> dict:
    """Retrieve a list of customers."""
    params = {"limit": limit, "page": page}
    if email:
        params["email"] = email
    return make_request("GET", "/customers.json", params=params)


@mcp.tool()
def search_customers(query: str, limit: int = 50) -> dict:
    """Search for customers."""
    params = {"query": query, "limit": limit}
    return make_request("GET", "/customers/search.json", params=params)


@mcp.tool()
def create_customer(
    first_name: str,
    last_name: str,
    email: str,
    phone: str | None = None,
    password: str | None = None,
    password_confirmation: str | None = None,
    addresses: list[dict] | None = None,
    send_email_welcome: bool = True,
) -> dict:
    """Create a new customer."""
    customer = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "send_email_welcome": str(send_email_welcome).lower(),
    }
    if phone:
        customer["phone"] = phone
    if password:
        customer["password"] = password
        customer["password_confirmation"] = password or password_confirmation
    if addresses:
        customer["addresses"] = addresses
    return make_request("POST", "/customers.json", data={"customer": customer})


@mcp.tool()
def update_customer(
    customer_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    email: str | None = None,
    phone: str | None = None,
    note: str | None = None,
    tags: str | None = None,
) -> dict:
    """Update an existing customer."""
    customer = {}
    if first_name:
        customer["first_name"] = first_name
    if last_name:
        customer["last_name"] = last_name
    if email:
        customer["email"] = email
    if phone:
        customer["phone"] = phone
    if note:
        customer["note"] = note
    if tags:
        customer["tags"] = tags
    return make_request("PUT", f"/customers/{customer_id}.json", data={"customer": customer})


@mcp.tool()
def delete_customer(customer_id: int) -> dict:
    """Delete a customer."""
    return make_request("DELETE", f"/customers/{customer_id}.json")


# ==================== ORDER ENDPOINTS ====================

@mcp.tool()
def get_order(order_id: int) -> dict:
    """Retrieve a single order by ID."""
    return make_request("GET", f"/orders/{order_id}.json")


@mcp.tool()
def list_orders(
    limit: int = 50,
    page: int = 1,
    status: str = "any",
    created_at_min: str | None = None,
    created_at_max: str | None = None,
) -> dict:
    """Retrieve a list of orders."""
    params = {"limit": limit, "page": page, "status": status}
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    return make_request("GET", "/orders.json", params=params)


@mcp.tool()
def create_order(
    line_items: list[dict],
    shipping_address: dict | None = None,
    billing_address: dict | None = None,
    email: str | None = None,
    send_receipt: bool = False,
    send_fulfillment_receipt: bool = False,
    inventory_behavior: str = "bypass",
) -> dict:
    """Create a new order."""
    order = {
        "line_items": line_items,
        "send_receipt": str(send_receipt).lower(),
        "send_fulfillment_receipt": str(send_fulfillment_receipt).lower(),
        "inventory_behavior": inventory_behavior,
    }
    if shipping_address:
        order["shipping_address"] = shipping_address
    if billing_address:
        order["billing_address"] = billing_address
    if email:
        order["email"] = email
    return make_request("POST", "/orders.json", data={"order": order})


@mcp.tool()
def update_order(
    order_id: int,
    shipping_address: dict | None = None,
    billing_address: dict | None = None,
    note: str | None = None,
    email: str | None = None,
) -> dict:
    """Update an existing order."""
    order = {}
    if shipping_address:
        order["shipping_address"] = shipping_address
    if billing_address:
        order["billing_address"] = billing_address
    if note:
        order["note"] = note
    if email:
        order["email"] = email
    return make_request("PUT", f"/orders/{order_id}.json", data={"order": order})


@mcp.tool()
def cancel_order(order_id: int, reason: str = "customer") -> dict:
    """Cancel an order."""
    return make_request("POST", f"/orders/{order_id}/cancel.json", data={"reason": reason})


@mcp.tool()
def close_order(order_id: int) -> dict:
    """Close an order."""
    return make_request("POST", f"/orders/{order_id}/close.json")


@mcp.tool()
def open_order(order_id: int) -> dict:
    """Re-open a closed order."""
    return make_request("POST", f"/orders/{order_id}/open.json")


# ==================== INVENTORY ENDPOINTS ====================

@mcp.tool()
def get_inventory_item(inventory_item_id: int) -> dict:
    """Retrieve a single inventory item by ID."""
    return make_request("GET", f"/inventory_items/{inventory_item_id}.json")


@mcp.tool()
def list_inventory_items(ids: str) -> dict:
    """Retrieve inventory items by IDs."""
    params = {"ids": ids}
    return make_request("GET", "/inventory_items.json", params=params)


@mcp.tool()
def update_inventory_item(inventory_item_id: int, sku: str | None = None, cost: float | None = None) -> dict:
    """Update an inventory item."""
    inventory_item = {}
    if sku:
        inventory_item["sku"] = sku
    if cost is not None:
        inventory_item["cost"] = str(cost)
    return make_request("PUT", f"/inventory_items/{inventory_item_id}.json", data={"inventory_item": inventory_item})


@mcp.tool()
def adjust_inventory(inventory_item_id: int, location_id: int, available_adjustment: int) -> dict:
    """Adjust inventory level at a location."""
    data = {"inventory_item_id": inventory_item_id, "location_id": location_id, "available_adjustment": available_adjustment}
    return make_request("POST", "/inventory_levels/adjust.json", data=data)


@mcp.tool()
def set_inventory(inventory_item_id: int, location_id: int, available: int) -> dict:
    """Set inventory level at a location."""
    data = {"inventory_item_id": inventory_item_id, "location_id": location_id, "available": available}
    return make_request("POST", "/inventory_levels/set.json", data=data)


@mcp.tool()
def connect_inventory_item(inventory_item_id: int, location_id: int, relocate_if_necessary: bool = True) -> dict:
    """Connect an inventory item to a location."""
    data = {"inventory_item_id": inventory_item_id, "location_id": location_id, "relocate_if_necessary": str(relocate_if_necessary).lower()}
    return make_request("POST", "/inventory_levels/connect.json", data=data)


@mcp.tool()
def delete_inventory_level(inventory_item_id: int, location_id: int) -> dict:
    """Delete an inventory level from a location."""
    params = {"inventory_item_id": inventory_item_id, "location_id": location_id}
    return make_request("DELETE", "/inventory_levels.json", params=params)


# ==================== FULFILLMENT ENDPOINTS ====================

@mcp.tool()
def create_fulfillment(
    order_id: int,
    tracking_numbers: list[str],
    tracking_urls: list[str],
    tracking_company: str,
    shipped_date: str | None = None,
    send_customer_notification: bool = False,
) -> dict:
    """Create a new fulfillment."""
    fulfillment = {
        "tracking_numbers": tracking_numbers,
        "tracking_urls": tracking_urls,
        "tracking_company": tracking_company,
        "send_customer_notification": str(send_customer_notification).lower(),
    }
    if shipped_date:
        fulfillment["shipped_at"] = shipped_date
    return make_request("POST", f"/orders/{order_id}/fulfillments.json", data={"fulfillment": fulfillment})


@mcp.tool()
def get_fulfillment(order_id: int, fulfillment_id: int) -> dict:
    """Retrieve a fulfillment by order and fulfillment ID."""
    return make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


@mcp.tool()
def list_fulfillments(order_id: int, limit: int = 50) -> dict:
    """Retrieve a list of fulfillments for an order."""
    params = {"limit": limit}
    return make_request("GET", f"/orders/{order_id}/fulfillments.json", params=params)


# ==================== DISCOUNT/PRICE RULE ENDPOINTS ====================

@mcp.tool()
def list_price_rules(limit: int = 50) -> dict:
    """Retrieve a list of price rules."""
    params = {"limit": limit}
    return make_request("GET", "/price_rules.json", params=params)


@mcp.tool()
def create_price_rule(
    title: str,
    target_type: str,
    target_selection: str,
    allocation_method: str,
    value_type: str,
    value: float,
    customer_selection: str = "all",
    starts_at: str | None = None,
    ends_at: str | None = None,
    once_per_customer: bool = False,
    usage_limit: int | None = None,
    condition: dict | None = None,
) -> dict:
    """Create a new price rule (discount)."""
    price_rule = {
        "title": title,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "value_type": value_type,
        "value": str(value),
        "customer_selection": customer_selection,
    }
    if starts_at:
        price_rule["starts_at"] = starts_at
    if ends_at:
        price_rule["ends_at"] = ends_at
    price_rule["once_per_customer"] = once_per_customer
    if usage_limit:
        price_rule["usage_limit"] = usage_limit
    if condition:
        price_rule["condition"] = condition
    return make_request("POST", "/price_rules.json", data={"price_rule": price_rule})


@mcp.tool()
def update_price_rule(
    price_rule_id: int,
    title: str | None = None,
    value: float | None = None,
    usage_limit: int | None = None,
    ends_at: str | None = None,
) -> dict:
    """Update a price rule."""
    price_rule = {}
    if title:
        price_rule["title"] = title
    if value is not None:
        price_rule["value"] = str(value)
    if usage_limit:
        price_rule["usage_limit"] = usage_limit
    if ends_at:
        price_rule["ends_at"] = ends_at
    return make_request("PUT", f"/price_rules/{price_rule_id}.json", data={"price_rule": price_rule})


@mcp.tool()
def delete_price_rule(price_rule_id: int) -> dict:
    """Delete a price rule."""
    return make_request("DELETE", f"/price_rules/{price_rule_id}.json")


@mcp.tool()
def create_discount_code(price_rule_id: int, code: str) -> dict:
    """Create a discount code for a price rule."""
    data = {"discount_code": {"code": code}}
    return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", data=data)


@mcp.tool()
def list_discount_codes(price_rule_id: int, limit: int = 50) -> dict:
    """Retrieve discount codes for a price rule."""
    params = {"limit": limit}
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


# ==================== WEBHOOK ENDPOINTS ====================

@mcp.tool()
def create_webhook(
    topic: str,
    address: str,
    format: str = "json",
    fields: list[str] | None = None,
    metafield_namespaces: list[str] | None = None,
) -> dict:
    """Create a new webhook subscription."""
    webhook = {"topic": topic, "address": address, "format": format}
    if fields:
        webhook["fields"] = fields
    if metafield_namespaces:
        webhook["metafield_namespaces"] = metafield_namespaces
    return make_request("POST", "/webhooks.json", data={"webhook": webhook})


@mcp.tool()
def list_webhooks() -> dict:
    """Retrieve a list of webhook subscriptions."""
    return make_request("GET", "/webhooks.json")


@mcp.tool()
def get_webhook(webhook_id: int) -> dict:
    """Retrieve a single webhook subscription."""
    return make_request("GET", f"/webhooks/{webhook_id}.json")


@mcp.tool()
def update_webhook(
    webhook_id: int,
    address: str | None = None,
    topic: str | None = None,
    format: str | None = None,
    fields: list[str] | None = None,
) -> dict:
    """Update a webhook subscription."""
    webhook = {}
    if address:
        webhook["address"] = address
    if topic:
        webhook["topic"] = topic
    if format:
        webhook["format"] = format
    if fields:
        webhook["fields"] = fields
    return make_request("PUT", f"/webhooks/{webhook_id}.json", data={"webhook": webhook})


@mcp.tool()
def delete_webhook(webhook_id: int) -> dict:
    """Delete a webhook subscription."""
    return make_request("DELETE", f"/webhooks/{webhook_id}.json")


# ==================== METAFIELD ENDPOINTS ====================

@mcp.tool()
def create_metafield(
    owner_id: int,
    owner_resource: str,
    namespace: str,
    key: str,
    value: str,
    type: str = "single_line_text_field",
    description: str | None = None,
) -> dict:
    """Create a metafield on a resource."""
    metafield = {"namespace": namespace, "key": key, "value": value, "type": type}
    if description:
        metafield["description"] = description
    return make_request("POST", f"/{owner_resource}s/{owner_id}/metafields.json", data={"metafield": metafield})


@mcp.tool()
def list_metafields(owner_id: int, owner_resource: str, limit: int = 50) -> dict:
    """Retrieve metafields for a resource."""
    params = {"limit": limit}
    return make_request("GET", f"/{owner_resource}s/{owner_id}/metafields.json", params=params)


@mcp.tool()
def get_metafield(owner_id: int, owner_resource: str, metafield_id: int) -> dict:
    """Retrieve a specific metafield."""
    return make_request("GET", f"/{owner_resource}s/{owner_id}/metafields/{metafield_id}.json")


@mcp.tool()
def update_metafield(metafield_id: int, value: str | None = None, type: str | None = None, description: str | None = None) -> dict:
    """Update a metafield."""
    metafield = {}
    if value:
        metafield["value"] = value
    if type:
        metafield["type"] = type
    if description:
        metafield["description"] = description
    return make_request("PUT", f"/metafields/{metafield_id}.json", data={"metafield": metafield})


@mcp.tool()
def delete_metafield(metafield_id: int) -> dict:
    """Delete a metafield."""
    return make_request("DELETE", f"/metafields/{metafield_id}.json")


# ==================== LOCATION ENDPOINTS ====================

@mcp.tool()
def get_location(location_id: int) -> dict:
    """Retrieve a single location by ID."""
    return make_request("GET", f"/locations/{location_id}.json")


@mcp.tool()
def list_locations() -> dict:
    """Retrieve a list of locations."""
    return make_request("GET", "/locations.json")


# ==================== DRAFT ORDER ENDPOINTS ====================

@mcp.tool()
def create_draft_order(
    line_items: list[dict],
    customer_id: int | None = None,
    shipping_address: dict | None = None,
    billing_address: dict | None = None,
    note: str | None = None,
) -> dict:
    """Create a new draft order."""
    order = {"line_items": line_items}
    if customer_id:
        order["customer_id"] = customer_id
    if shipping_address:
        order["shipping_address"] = shipping_address
    if billing_address:
        order["billing_address"] = billing_address
    if note:
        order["note"] = note
    return make_request("POST", "/draft_orders.json", data={"draft_order": order})


@mcp.tool()
def update_draft_order(
    draft_order_id: int,
    line_items: list[dict] | None = None,
    shipping_address: dict | None = None,
    billing_address: dict | None = None,
    note: str | None = None,
) -> dict:
    """Update a draft order."""
    order = {}
    if line_items:
        order["line_items"] = line_items
    if shipping_address:
        order["shipping_address"] = shipping_address
    if billing_address:
        order["billing_address"] = billing_address
    if note:
        order["note"] = note
    return make_request("PUT", f"/draft_orders/{draft_order_id}.json", data={"draft_order": order})


@mcp.tool()
def complete_draft_order(draft_order_id: int, send_invoice_email: bool = False) -> dict:
    """Complete a draft order (convert to order)."""
    data = {"send_invoice_email": str(send_invoice_email).lower()}
    return make_request("POST", f"/draft_orders/{draft_order_id}/order.json", data=data)


# ==================== REFUND ENDPOINTS ====================

@mcp.tool()
def create_refund(
    order_id: int,
    refund_line_items: list[dict],
    shipping: dict | None = None,
    notes: str | None = None,
) -> dict:
    """Create a refund for an order."""
    refund = {"refund_line_items": refund_line_items}
    if shipping:
        refund["shipping"] = shipping
    if notes:
        refund["notes"] = notes
    return make_request("POST", f"/orders/{order_id}/refunds.json", data={"refund": refund})


# ==================== TRANSACTION ENDPOINTS ====================

@mcp.tool()
def list_transactions(order_id: int, limit: int = 50) -> dict:
    """Retrieve transactions for an order."""
    params = {"limit": limit}
    return make_request("GET", f"/orders/{order_id}/transactions.json", params=params)


# ==================== SHOP ENDPOINTS ====================

@mcp.tool()
def get_shop() -> dict:
    """Retrieve shop information."""
    return make_request("GET", "/shop.json")


if __name__ == "__main__":
    mcp.run()
'''

# Write the server code to a file
with open("server.py", "w") as f:
    f.write(SERVER_CODE)

print("server.py generated successfully!")
