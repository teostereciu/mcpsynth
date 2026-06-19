#!/usr/bin/env python3
"""
MCP Server for Shopify Admin REST API
Provides tools for managing products, orders, customers, inventory, and more.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
server = FastMCP("shopify-admin-api")

# Configuration from environment
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN", "")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL", "")
BASE_URL = f"https://{SHOPIFY_STORE_URL}/admin/api/2026-01"

# Headers for API requests
HEADERS = {
    "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
    "Content-Type": "application/json",
}


def make_request(
    method: str, endpoint: str, data: Optional[dict] = None, params: Optional[dict] = None
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
            try:
                return {"error": response.json()}
            except:
                return {"error": "Unprocessable entity"}
        else:
            return {"error": f"API error: {response.status_code}", "details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# PRODUCTS
# ============================================================================


@server.tool()
def list_products(
    limit: int = 50,
    status: str = "active",
    fields: Optional[str] = None,
) -> dict:
    """List all products in the store."""
    params = {"limit": limit, "status": status}
    if fields:
        params["fields"] = fields
    return make_request("GET", "/products.json", params=params)


@server.tool()
def get_product(product_id: int, fields: Optional[str] = None) -> dict:
    """Get a specific product by ID."""
    params = {}
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/products/{product_id}.json", params=params)


@server.tool()
def create_product(
    title: str,
    product_type: str = "",
    vendor: str = "",
    body_html: str = "",
    tags: str = "",
    handle: Optional[str] = None,
) -> dict:
    """Create a new product."""
    data = {
        "product": {
            "title": title,
            "product_type": product_type,
            "vendor": vendor,
            "body_html": body_html,
            "tags": tags,
        }
    }
    if handle:
        data["product"]["handle"] = handle
    return make_request("POST", "/products.json", data=data)


@server.tool()
def update_product(
    product_id: int,
    title: Optional[str] = None,
    body_html: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    tags: Optional[str] = None,
) -> dict:
    """Update an existing product."""
    data = {"product": {}}
    if title is not None:
        data["product"]["title"] = title
    if body_html is not None:
        data["product"]["body_html"] = body_html
    if vendor is not None:
        data["product"]["vendor"] = vendor
    if product_type is not None:
        data["product"]["product_type"] = product_type
    if tags is not None:
        data["product"]["tags"] = tags
    return make_request("PUT", f"/products/{product_id}.json", data=data)


@server.tool()
def delete_product(product_id: int) -> dict:
    """Delete a product."""
    return make_request("DELETE", f"/products/{product_id}.json")


# ============================================================================
# PRODUCT VARIANTS
# ============================================================================


@server.tool()
def list_product_variants(product_id: int, limit: int = 50) -> dict:
    """List all variants for a product."""
    return make_request("GET", f"/products/{product_id}/variants.json", params={"limit": limit})


@server.tool()
def get_product_variant(variant_id: int) -> dict:
    """Get a specific product variant by ID."""
    return make_request("GET", f"/variants/{variant_id}.json")


@server.tool()
def create_product_variant(
    product_id: int,
    title: str,
    price: str,
    sku: Optional[str] = None,
    barcode: Optional[str] = None,
    weight: Optional[float] = None,
    weight_unit: str = "kg",
    option1_value: Optional[str] = None,
) -> dict:
    """Create a new variant for a product."""
    data = {
        "variant": {
            "title": title,
            "price": price,
        }
    }
    if sku:
        data["variant"]["sku"] = sku
    if barcode:
        data["variant"]["barcode"] = barcode
    if weight is not None:
        data["variant"]["weight"] = weight
        data["variant"]["weight_unit"] = weight_unit
    if option1_value:
        data["variant"]["option1"] = option1_value
    return make_request("POST", f"/products/{product_id}/variants.json", data=data)


@server.tool()
def update_product_variant(
    variant_id: int,
    title: Optional[str] = None,
    price: Optional[str] = None,
    sku: Optional[str] = None,
    barcode: Optional[str] = None,
) -> dict:
    """Update a product variant."""
    data = {"variant": {}}
    if title is not None:
        data["variant"]["title"] = title
    if price is not None:
        data["variant"]["price"] = price
    if sku is not None:
        data["variant"]["sku"] = sku
    if barcode is not None:
        data["variant"]["barcode"] = barcode
    return make_request("PUT", f"/variants/{variant_id}.json", data=data)


@server.tool()
def delete_product_variant(product_id: int, variant_id: int) -> dict:
    """Delete a product variant."""
    return make_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


# ============================================================================
# PRODUCT IMAGES
# ============================================================================


@server.tool()
def list_product_images(product_id: int) -> dict:
    """List all images for a product."""
    return make_request("GET", f"/products/{product_id}/images.json")


@server.tool()
def get_product_image(product_id: int, image_id: int) -> dict:
    """Get a specific product image."""
    return make_request("GET", f"/products/{product_id}/images/{image_id}.json")


@server.tool()
def create_product_image(
    product_id: int,
    src: str,
    alt: Optional[str] = None,
    position: Optional[int] = None,
) -> dict:
    """Create a new product image."""
    data = {
        "image": {
            "src": src,
        }
    }
    if alt:
        data["image"]["alt"] = alt
    if position is not None:
        data["image"]["position"] = position
    return make_request("POST", f"/products/{product_id}/images.json", data=data)


@server.tool()
def update_product_image(
    product_id: int,
    image_id: int,
    alt: Optional[str] = None,
    position: Optional[int] = None,
) -> dict:
    """Update a product image."""
    data = {"image": {}}
    if alt is not None:
        data["image"]["alt"] = alt
    if position is not None:
        data["image"]["position"] = position
    return make_request("PUT", f"/products/{product_id}/images/{image_id}.json", data=data)


@server.tool()
def delete_product_image(product_id: int, image_id: int) -> dict:
    """Delete a product image."""
    return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")


# ============================================================================
# COLLECTIONS
# ============================================================================


@server.tool()
def list_collections(limit: int = 50) -> dict:
    """List all collections."""
    return make_request("GET", "/collections.json", params={"limit": limit})


@server.tool()
def get_collection(collection_id: int) -> dict:
    """Get a specific collection by ID."""
    return make_request("GET", f"/collections/{collection_id}.json")


@server.tool()
def create_collection(
    title: str,
    body_html: str = "",
    handle: Optional[str] = None,
) -> dict:
    """Create a new collection."""
    data = {
        "collection": {
            "title": title,
            "body_html": body_html,
        }
    }
    if handle:
        data["collection"]["handle"] = handle
    return make_request("POST", "/collections.json", data=data)


@server.tool()
def update_collection(
    collection_id: int,
    title: Optional[str] = None,
    body_html: Optional[str] = None,
) -> dict:
    """Update a collection."""
    data = {"collection": {}}
    if title is not None:
        data["collection"]["title"] = title
    if body_html is not None:
        data["collection"]["body_html"] = body_html
    return make_request("PUT", f"/collections/{collection_id}.json", data=data)


@server.tool()
def delete_collection(collection_id: int) -> dict:
    """Delete a collection."""
    return make_request("DELETE", f"/collections/{collection_id}.json")


# ============================================================================
# ORDERS
# ============================================================================


@server.tool()
def list_orders(
    limit: int = 50,
    status: str = "any",
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
) -> dict:
    """List all orders."""
    params = {"limit": limit, "status": status}
    if financial_status:
        params["financial_status"] = financial_status
    if fulfillment_status:
        params["fulfillment_status"] = fulfillment_status
    return make_request("GET", "/orders.json", params=params)


@server.tool()
def get_order(order_id: int) -> dict:
    """Get a specific order by ID."""
    return make_request("GET", f"/orders/{order_id}.json")


@server.tool()
def update_order(
    order_id: int,
    email: Optional[str] = None,
    note: Optional[str] = None,
    tags: Optional[str] = None,
) -> dict:
    """Update an order."""
    data = {"order": {}}
    if email is not None:
        data["order"]["email"] = email
    if note is not None:
        data["order"]["note"] = note
    if tags is not None:
        data["order"]["tags"] = tags
    return make_request("PUT", f"/orders/{order_id}.json", data=data)


@server.tool()
def close_order(order_id: int) -> dict:
    """Close an order."""
    return make_request("POST", f"/orders/{order_id}/close.json")


@server.tool()
def reopen_order(order_id: int) -> dict:
    """Reopen a closed order."""
    return make_request("POST", f"/orders/{order_id}/open.json")


@server.tool()
def cancel_order(order_id: int, reason: str = "customer") -> dict:
    """Cancel an order."""
    data = {"order": {"cancel_reason": reason}}
    return make_request("POST", f"/orders/{order_id}/cancel.json", data=data)


# ============================================================================
# DRAFT ORDERS
# ============================================================================


@server.tool()
def list_draft_orders(limit: int = 50, status: str = "open") -> dict:
    """List all draft orders."""
    return make_request("GET", "/draft_orders.json", params={"limit": limit, "status": status})


@server.tool()
def get_draft_order(draft_order_id: int) -> dict:
    """Get a specific draft order by ID."""
    return make_request("GET", f"/draft_orders/{draft_order_id}.json")


@server.tool()
def create_draft_order(
    customer_id: Optional[int] = None,
    email: Optional[str] = None,
    line_items: Optional[list] = None,
    note: str = "",
) -> dict:
    """Create a new draft order."""
    data = {
        "draft_order": {
            "note": note,
        }
    }
    if customer_id:
        data["draft_order"]["customer_id"] = customer_id
    if email:
        data["draft_order"]["email"] = email
    if line_items:
        data["draft_order"]["line_items"] = line_items
    return make_request("POST", "/draft_orders.json", data=data)


@server.tool()
def update_draft_order(
    draft_order_id: int,
    note: Optional[str] = None,
    line_items: Optional[list] = None,
) -> dict:
    """Update a draft order."""
    data = {"draft_order": {}}
    if note is not None:
        data["draft_order"]["note"] = note
    if line_items is not None:
        data["draft_order"]["line_items"] = line_items
    return make_request("PUT", f"/draft_orders/{draft_order_id}.json", data=data)


@server.tool()
def delete_draft_order(draft_order_id: int) -> dict:
    """Delete a draft order."""
    return make_request("DELETE", f"/draft_orders/{draft_order_id}.json")


@server.tool()
def complete_draft_order(draft_order_id: int, payment_pending: bool = False) -> dict:
    """Complete a draft order and convert it to an order."""
    data = {"draft_order": {"payment_pending": payment_pending}}
    return make_request("PUT", f"/draft_orders/{draft_order_id}/complete.json", data=data)


# ============================================================================
# REFUNDS
# ============================================================================


@server.tool()
def list_refunds(order_id: int) -> dict:
    """List all refunds for an order."""
    return make_request("GET", f"/orders/{order_id}/refunds.json")


@server.tool()
def get_refund(order_id: int, refund_id: int) -> dict:
    """Get a specific refund."""
    return make_request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")


@server.tool()
def create_refund(
    order_id: int,
    note: str = "",
    notify: bool = True,
    line_items: Optional[list] = None,
) -> dict:
    """Create a refund for an order."""
    data = {
        "refund": {
            "note": note,
            "notify": notify,
        }
    }
    if line_items:
        data["refund"]["refund_line_items"] = line_items
    return make_request("POST", f"/orders/{order_id}/refunds.json", data=data)


# ============================================================================
# TRANSACTIONS
# ============================================================================


@server.tool()
def list_transactions(order_id: int) -> dict:
    """List all transactions for an order."""
    return make_request("GET", f"/orders/{order_id}/transactions.json")


@server.tool()
def get_transaction(order_id: int, transaction_id: int) -> dict:
    """Get a specific transaction."""
    return make_request("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")


@server.tool()
def create_transaction(
    order_id: int,
    kind: str,
    amount: str,
    currency: str = "USD",
) -> dict:
    """Create a transaction for an order."""
    data = {
        "transaction": {
            "kind": kind,
            "amount": amount,
            "currency": currency,
        }
    }
    return make_request("POST", f"/orders/{order_id}/transactions.json", data=data)


# ============================================================================
# CUSTOMERS
# ============================================================================


@server.tool()
def list_customers(limit: int = 50) -> dict:
    """List all customers."""
    return make_request("GET", "/customers.json", params={"limit": limit})


@server.tool()
def get_customer(customer_id: int) -> dict:
    """Get a specific customer by ID."""
    return make_request("GET", f"/customers/{customer_id}.json")


@server.tool()
def create_customer(
    email: str,
    first_name: str = "",
    last_name: str = "",
    phone: str = "",
    tags: str = "",
) -> dict:
    """Create a new customer."""
    data = {
        "customer": {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "tags": tags,
        }
    }
    return make_request("POST", "/customers.json", data=data)


@server.tool()
def update_customer(
    customer_id: int,
    email: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    tags: Optional[str] = None,
) -> dict:
    """Update a customer."""
    data = {"customer": {}}
    if email is not None:
        data["customer"]["email"] = email
    if first_name is not None:
        data["customer"]["first_name"] = first_name
    if last_name is not None:
        data["customer"]["last_name"] = last_name
    if phone is not None:
        data["customer"]["phone"] = phone
    if tags is not None:
        data["customer"]["tags"] = tags
    return make_request("PUT", f"/customers/{customer_id}.json", data=data)


@server.tool()
def delete_customer(customer_id: int) -> dict:
    """Delete a customer."""
    return make_request("DELETE", f"/customers/{customer_id}.json")


# ============================================================================
# CUSTOMER ADDRESSES
# ============================================================================


@server.tool()
def list_customer_addresses(customer_id: int) -> dict:
    """List all addresses for a customer."""
    return make_request("GET", f"/customers/{customer_id}/addresses.json")


@server.tool()
def get_customer_address(customer_id: int, address_id: int) -> dict:
    """Get a specific customer address."""
    return make_request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


@server.tool()
def create_customer_address(
    customer_id: int,
    address1: str,
    city: str,
    province: str,
    zip: str,
    country: str,
    address2: str = "",
    phone: str = "",
    default: bool = False,
) -> dict:
    """Create a new address for a customer."""
    data = {
        "address": {
            "address1": address1,
            "city": city,
            "province": province,
            "zip": zip,
            "country": country,
            "address2": address2,
            "phone": phone,
            "default": default,
        }
    }
    return make_request("POST", f"/customers/{customer_id}/addresses.json", data=data)


@server.tool()
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
    data = {"address": {}}
    if address1 is not None:
        data["address"]["address1"] = address1
    if city is not None:
        data["address"]["city"] = city
    if province is not None:
        data["address"]["province"] = province
    if zip is not None:
        data["address"]["zip"] = zip
    if country is not None:
        data["address"]["country"] = country
    return make_request("PUT", f"/customers/{customer_id}/addresses/{address_id}.json", data=data)


@server.tool()
def delete_customer_address(customer_id: int, address_id: int) -> dict:
    """Delete a customer address."""
    return make_request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")


@server.tool()
def set_default_customer_address(customer_id: int, address_id: int) -> dict:
    """Set a customer address as the default."""
    return make_request("PUT", f"/customers/{customer_id}/addresses/{address_id}/default.json")


# ============================================================================
# FULFILLMENT ORDERS
# ============================================================================


@server.tool()
def list_fulfillment_orders(order_id: int, status: str = "scheduled") -> dict:
    """List fulfillment orders for an order."""
    return make_request(
        "GET", f"/orders/{order_id}/fulfillment_orders.json", params={"status": status}
    )


@server.tool()
def get_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Get a specific fulfillment order."""
    return make_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


@server.tool()
def create_fulfillment(
    fulfillment_order_id: int,
    line_items: list,
    tracking_info: Optional[dict] = None,
) -> dict:
    """Create a fulfillment for a fulfillment order."""
    data = {
        "fulfillment": {
            "line_items_by_fulfillment_order": [
                {
                    "fulfillment_order_id": fulfillment_order_id,
                    "fulfillment_order_line_items": line_items,
                }
            ]
        }
    }
    if tracking_info:
        data["fulfillment"]["tracking_info"] = tracking_info
    return make_request("POST", "/fulfillments.json", data=data)


@server.tool()
def cancel_fulfillment(fulfillment_id: int) -> dict:
    """Cancel a fulfillment."""
    return make_request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")


# ============================================================================
# LOCATIONS
# ============================================================================


@server.tool()
def list_locations() -> dict:
    """List all locations."""
    return make_request("GET", "/locations.json")


@server.tool()
def get_location(location_id: int) -> dict:
    """Get a specific location."""
    return make_request("GET", f"/locations/{location_id}.json")


# ============================================================================
# INVENTORY
# ============================================================================


@server.tool()
def list_inventory_items(limit: int = 50) -> dict:
    """List all inventory items."""
    return make_request("GET", "/inventory_items.json", params={"limit": limit})


@server.tool()
def get_inventory_item(inventory_item_id: int) -> dict:
    """Get a specific inventory item."""
    return make_request("GET", f"/inventory_items/{inventory_item_id}.json")


@server.tool()
def update_inventory_item(
    inventory_item_id: int,
    sku: Optional[str] = None,
    tracked: Optional[bool] = None,
) -> dict:
    """Update an inventory item."""
    data = {"inventory_item": {}}
    if sku is not None:
        data["inventory_item"]["sku"] = sku
    if tracked is not None:
        data["inventory_item"]["tracked"] = tracked
    return make_request("PUT", f"/inventory_items/{inventory_item_id}.json", data=data)


@server.tool()
def list_inventory_levels(inventory_item_id: Optional[int] = None) -> dict:
    """List inventory levels."""
    params = {}
    if inventory_item_id:
        params["inventory_item_ids"] = inventory_item_id
    return make_request("GET", "/inventory_levels.json", params=params)


@server.tool()
def adjust_inventory_level(
    inventory_item_id: int,
    location_id: int,
    available_adjustment: int,
) -> dict:
    """Adjust inventory level for an item at a location."""
    data = {
        "inventory_adjustment": {
            "inventory_item_id": inventory_item_id,
            "location_id": location_id,
            "available_adjustment": available_adjustment,
        }
    }
    return make_request("POST", "/inventory_adjustments.json", data=data)


# ============================================================================
# PRICE RULES & DISCOUNTS
# ============================================================================


@server.tool()
def list_price_rules(limit: int = 50) -> dict:
    """List all price rules."""
    return make_request("GET", "/price_rules.json", params={"limit": limit})


@server.tool()
def get_price_rule(price_rule_id: int) -> dict:
    """Get a specific price rule."""
    return make_request("GET", f"/price_rules/{price_rule_id}.json")


@server.tool()
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
    """Create a new price rule."""
    data = {
        "price_rule": {
            "title": title,
            "target_type": target_type,
            "target_selection": target_selection,
            "allocation_method": allocation_method,
            "value": value,
            "value_type": value_type,
            "starts_at": starts_at,
        }
    }
    if ends_at:
        data["price_rule"]["ends_at"] = ends_at
    return make_request("POST", "/price_rules.json", data=data)


@server.tool()
def update_price_rule(
    price_rule_id: int,
    title: Optional[str] = None,
    value: Optional[str] = None,
) -> dict:
    """Update a price rule."""
    data = {"price_rule": {}}
    if title is not None:
        data["price_rule"]["title"] = title
    if value is not None:
        data["price_rule"]["value"] = value
    return make_request("PUT", f"/price_rules/{price_rule_id}.json", data=data)


@server.tool()
def delete_price_rule(price_rule_id: int) -> dict:
    """Delete a price rule."""
    return make_request("DELETE", f"/price_rules/{price_rule_id}.json")


@server.tool()
def list_discount_codes(price_rule_id: int) -> dict:
    """List all discount codes for a price rule."""
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json")


@server.tool()
def get_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """Get a specific discount code."""
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


@server.tool()
def create_discount_code(
    price_rule_id: int,
    code: str,
) -> dict:
    """Create a new discount code for a price rule."""
    data = {
        "discount_code": {
            "code": code,
        }
    }
    return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", data=data)


@server.tool()
def update_discount_code(
    price_rule_id: int,
    discount_code_id: int,
    code: Optional[str] = None,
) -> dict:
    """Update a discount code."""
    data = {"discount_code": {}}
    if code is not None:
        data["discount_code"]["code"] = code
    return make_request(
        "PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", data=data
    )


@server.tool()
def delete_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """Delete a discount code."""
    return make_request(
        "DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
    )


# ============================================================================
# WEBHOOKS
# ============================================================================


@server.tool()
def list_webhooks() -> dict:
    """List all webhooks."""
    return make_request("GET", "/webhooks.json")


@server.tool()
def get_webhook(webhook_id: int) -> dict:
    """Get a specific webhook."""
    return make_request("GET", f"/webhooks/{webhook_id}.json")


@server.tool()
def create_webhook(
    topic: str,
    address: str,
    format: str = "json",
) -> dict:
    """Create a new webhook."""
    data = {
        "webhook": {
            "topic": topic,
            "address": address,
            "format": format,
        }
    }
    return make_request("POST", "/webhooks.json", data=data)


@server.tool()
def update_webhook(
    webhook_id: int,
    address: Optional[str] = None,
    topic: Optional[str] = None,
) -> dict:
    """Update a webhook."""
    data = {"webhook": {}}
    if address is not None:
        data["webhook"]["address"] = address
    if topic is not None:
        data["webhook"]["topic"] = topic
    return make_request("PUT", f"/webhooks/{webhook_id}.json", data=data)


@server.tool()
def delete_webhook(webhook_id: int) -> dict:
    """Delete a webhook."""
    return make_request("DELETE", f"/webhooks/{webhook_id}.json")


# ============================================================================
# METAFIELDS
# ============================================================================


@server.tool()
def list_metafields(resource_type: str, resource_id: int) -> dict:
    """List metafields for a resource."""
    return make_request("GET", f"/{resource_type}/{resource_id}/metafields.json")


@server.tool()
def get_metafield(metafield_id: int) -> dict:
    """Get a specific metafield."""
    return make_request("GET", f"/metafields/{metafield_id}.json")


@server.tool()
def create_metafield(
    resource_type: str,
    resource_id: int,
    namespace: str,
    key: str,
    value: str,
    value_type: str = "string",
) -> dict:
    """Create a new metafield."""
    data = {
        "metafield": {
            "namespace": namespace,
            "key": key,
            "value": value,
            "value_type": value_type,
        }
    }
    return make_request("POST", f"/{resource_type}/{resource_id}/metafields.json", data=data)


@server.tool()
def update_metafield(
    metafield_id: int,
    value: Optional[str] = None,
) -> dict:
    """Update a metafield."""
    data = {"metafield": {}}
    if value is not None:
        data["metafield"]["value"] = value
    return make_request("PUT", f"/metafields/{metafield_id}.json", data=data)


@server.tool()
def delete_metafield(metafield_id: int) -> dict:
    """Delete a metafield."""
    return make_request("DELETE", f"/metafields/{metafield_id}.json")


# ============================================================================
# SHOP INFO
# ============================================================================


@server.tool()
def get_shop() -> dict:
    """Get shop information."""
    return make_request("GET", "/shop.json")


if __name__ == "__main__":
    server.run()
