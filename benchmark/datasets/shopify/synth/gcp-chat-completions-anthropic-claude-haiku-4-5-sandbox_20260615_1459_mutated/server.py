#!/usr/bin/env python3
"""
Shopify Admin REST API MCP Server

This server provides tools for interacting with the Shopify Admin REST API.
It uses FastMCP to expose tools over the MCP protocol.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("shopify-admin-api")

# Configuration from environment variables
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN", "")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL", "")
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
            try:
                return {"error": response.json()}
            except:
                return {"error": "Unprocessable entity"}
        elif response.status_code >= 400:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
        else:
            return response.json()
    except requests.exceptions.Timeout:
        return {"error": "Request timeout"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}


# PRODUCTS
@mcp.tool()
def list_products(limit: int = 50, status: str = "active", fields: Optional[str] = None) -> dict:
    """Retrieve a list of products."""
    params = {"limit": min(limit, 250), "status": status}
    if fields:
        params["fields"] = fields
    return make_request("GET", "/products.json", params=params)


@mcp.tool()
def get_product(product_id: int, fields: Optional[str] = None) -> dict:
    """Retrieve a single product by ID."""
    params = {}
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/products/{product_id}.json", params=params)


@mcp.tool()
def create_product(title: str, body_html: Optional[str] = None, vendor: Optional[str] = None,
                   product_type: Optional[str] = None, tags: Optional[str] = None, status: str = "draft") -> dict:
    """Create a new product."""
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
def update_product(product_id: int, title: Optional[str] = None, body_html: Optional[str] = None,
                   vendor: Optional[str] = None, product_type: Optional[str] = None,
                   tags: Optional[str] = None, status: Optional[str] = None) -> dict:
    """Update a product."""
    product = {"id": product_id}
    if title is not None:
        product["title"] = title
    if body_html is not None:
        product["body_html"] = body_html
    if vendor is not None:
        product["vendor"] = vendor
    if product_type is not None:
        product["product_type"] = product_type
    if tags is not None:
        product["tags"] = tags
    if status is not None:
        product["status"] = status
    return make_request("PUT", f"/products/{product_id}.json", data={"product": product})


@mcp.tool()
def delete_product(product_id: int) -> dict:
    """Delete a product."""
    return make_request("DELETE", f"/products/{product_id}.json")


@mcp.tool()
def count_products(status: str = "active") -> dict:
    """Get a count of products."""
    return make_request("GET", "/products/count.json", params={"status": status})


# PRODUCT VARIANTS
@mcp.tool()
def list_product_variants(product_id: int, limit: int = 50) -> dict:
    """Retrieve variants for a product."""
    return make_request("GET", f"/products/{product_id}/variants.json", params={"limit": min(limit, 250)})


@mcp.tool()
def get_product_variant(variant_id: int) -> dict:
    """Retrieve a single product variant."""
    return make_request("GET", f"/variants/{variant_id}.json")


@mcp.tool()
def create_product_variant(product_id: int, title: Optional[str] = None, price: Optional[str] = None,
                           sku: Optional[str] = None, option1: Optional[str] = None,
                           option2: Optional[str] = None, option3: Optional[str] = None) -> dict:
    """Create a product variant."""
    variant = {}
    if title:
        variant["title"] = title
    if price:
        variant["price"] = price
    if sku:
        variant["sku"] = sku
    if option1:
        variant["option1"] = option1
    if option2:
        variant["option2"] = option2
    if option3:
        variant["option3"] = option3
    return make_request("POST", f"/products/{product_id}/variants.json", data={"variant": variant})


@mcp.tool()
def update_product_variant(variant_id: int, title: Optional[str] = None, price: Optional[str] = None,
                           sku: Optional[str] = None) -> dict:
    """Update a product variant."""
    variant = {"id": variant_id}
    if title is not None:
        variant["title"] = title
    if price is not None:
        variant["price"] = price
    if sku is not None:
        variant["sku"] = sku
    return make_request("PUT", f"/variants/{variant_id}.json", data={"variant": variant})


@mcp.tool()
def delete_product_variant(product_id: int, variant_id: int) -> dict:
    """Delete a product variant."""
    return make_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


# PRODUCT IMAGES
@mcp.tool()
def list_product_images(product_id: int) -> dict:
    """Retrieve images for a product."""
    return make_request("GET", f"/products/{product_id}/images.json")


@mcp.tool()
def get_product_image(product_id: int, image_id: int) -> dict:
    """Retrieve a single product image."""
    return make_request("GET", f"/products/{product_id}/images/{image_id}.json")


@mcp.tool()
def create_product_image(product_id: int, src: Optional[str] = None, attachment: Optional[str] = None,
                         alt: Optional[str] = None) -> dict:
    """Create a product image."""
    image = {}
    if src:
        image["src"] = src
    if attachment:
        image["attachment"] = attachment
    if alt:
        image["alt"] = alt
    return make_request("POST", f"/products/{product_id}/images.json", data={"image": image})


@mcp.tool()
def delete_product_image(product_id: int, image_id: int) -> dict:
    """Delete a product image."""
    return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")


# ORDERS
@mcp.tool()
def list_orders(limit: int = 50, status: str = "any", financial_status: Optional[str] = None,
                fulfillment_status: Optional[str] = None) -> dict:
    """Retrieve a list of orders."""
    params = {"limit": min(limit, 250), "status": status}
    if financial_status:
        params["financial_status"] = financial_status
    if fulfillment_status:
        params["fulfillment_status"] = fulfillment_status
    return make_request("GET", "/orders.json", params=params)


@mcp.tool()
def get_order(order_id: int, fields: Optional[str] = None) -> dict:
    """Retrieve a single order."""
    params = {}
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/orders/{order_id}.json", params=params)


@mcp.tool()
def create_order(line_items: list, customer: Optional[dict] = None, email: Optional[str] = None,
                 phone: Optional[str] = None, send_receipt: bool = False) -> dict:
    """Create an order."""
    order = {"line_items": line_items, "send_receipt": send_receipt}
    if customer:
        order["customer"] = customer
    if email:
        order["email"] = email
    if phone:
        order["phone"] = phone
    return make_request("POST", "/orders.json", data={"order": order})


@mcp.tool()
def update_order(order_id: int, email: Optional[str] = None, phone: Optional[str] = None,
                 note: Optional[str] = None, tags: Optional[str] = None) -> dict:
    """Update an order."""
    order = {"id": order_id}
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
def cancel_order(order_id: int, reason: str = "other") -> dict:
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


@mcp.tool()
def delete_order(order_id: int) -> dict:
    """Delete an order."""
    return make_request("DELETE", f"/orders/{order_id}.json")


@mcp.tool()
def count_orders(status: str = "any") -> dict:
    """Get a count of orders."""
    return make_request("GET", "/orders/count.json", params={"status": status})


# CUSTOMERS
@mcp.tool()
def list_customers(limit: int = 50) -> dict:
    """Retrieve a list of customers."""
    return make_request("GET", "/customers.json", params={"limit": min(limit, 250)})


@mcp.tool()
def get_customer(customer_id: int) -> dict:
    """Retrieve a single customer."""
    return make_request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def search_customers(query: str) -> dict:
    """Search for customers."""
    return make_request("GET", "/customers/search.json", params={"query": query})


@mcp.tool()
def create_customer(email: str, first_name: Optional[str] = None, last_name: Optional[str] = None,
                    phone: Optional[str] = None, tags: Optional[str] = None) -> dict:
    """Create a customer."""
    customer = {"email": email}
    if first_name:
        customer["first_name"] = first_name
    if last_name:
        customer["last_name"] = last_name
    if phone:
        customer["phone"] = phone
    if tags:
        customer["tags"] = tags
    return make_request("POST", "/customers.json", data={"customer": customer})


@mcp.tool()
def update_customer(customer_id: int, email: Optional[str] = None, first_name: Optional[str] = None,
                    last_name: Optional[str] = None, phone: Optional[str] = None,
                    tags: Optional[str] = None) -> dict:
    """Update a customer."""
    customer = {"id": customer_id}
    if email is not None:
        customer["email"] = email
    if first_name is not None:
        customer["first_name"] = first_name
    if last_name is not None:
        customer["last_name"] = last_name
    if phone is not None:
        customer["phone"] = phone
    if tags is not None:
        customer["tags"] = tags
    return make_request("PUT", f"/customers/{customer_id}.json", data={"customer": customer})


@mcp.tool()
def count_customers() -> dict:
    """Get a count of customers."""
    return make_request("GET", "/customers/count.json")


@mcp.tool()
def get_customer_orders(customer_id: int) -> dict:
    """Get all orders for a customer."""
    return make_request("GET", f"/customers/{customer_id}/orders.json")


# CUSTOMER ADDRESSES
@mcp.tool()
def list_customer_addresses(customer_id: int) -> dict:
    """Retrieve addresses for a customer."""
    return make_request("GET", f"/customers/{customer_id}/addresses.json")


@mcp.tool()
def get_customer_address(customer_id: int, address_id: int) -> dict:
    """Retrieve a single customer address."""
    return make_request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


@mcp.tool()
def create_customer_address(customer_id: int, address1: str, city: str, province: str, zip: str,
                            country: str, address2: Optional[str] = None, company: Optional[str] = None,
                            first_name: Optional[str] = None, last_name: Optional[str] = None,
                            phone: Optional[str] = None) -> dict:
    """Create a customer address."""
    address = {"address1": address1, "city": city, "province": province, "zip": zip, "country": country}
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
def update_customer_address(customer_id: int, address_id: int, address1: Optional[str] = None,
                            city: Optional[str] = None, province: Optional[str] = None,
                            zip: Optional[str] = None, country: Optional[str] = None) -> dict:
    """Update a customer address."""
    address = {"id": address_id}
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


# FULFILLMENTS
@mcp.tool()
def list_fulfillments(order_id: int) -> dict:
    """Retrieve fulfillments for an order."""
    return make_request("GET", f"/orders/{order_id}/fulfillments.json")


@mcp.tool()
def get_fulfillment(order_id: int, fulfillment_id: int) -> dict:
    """Retrieve a single fulfillment."""
    return make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


@mcp.tool()
def create_fulfillment(order_id: int, line_items: list, tracking_info: Optional[dict] = None) -> dict:
    """Create a fulfillment for an order."""
    fulfillment = {"line_items": line_items}
    if tracking_info:
        fulfillment["tracking_info"] = tracking_info
    return make_request("POST", f"/orders/{order_id}/fulfillments.json", data={"fulfillment": fulfillment})


@mcp.tool()
def update_fulfillment(order_id: int, fulfillment_id: int, tracking_info: Optional[dict] = None) -> dict:
    """Update a fulfillment."""
    fulfillment = {}
    if tracking_info:
        fulfillment["tracking_info"] = tracking_info
    return make_request("PUT", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json", data={"fulfillment": fulfillment})


# FULFILLMENT ORDERS
@mcp.tool()
def list_fulfillment_orders(order_id: int, status: Optional[str] = None) -> dict:
    """Retrieve fulfillment orders for an order."""
    params = {}
    if status:
        params["status"] = status
    return make_request("GET", f"/orders/{order_id}/fulfillment_orders.json", params=params)


@mcp.tool()
def get_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Retrieve a single fulfillment order."""
    return make_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


# REFUNDS
@mcp.tool()
def list_refunds(order_id: int) -> dict:
    """Retrieve refunds for an order."""
    return make_request("GET", f"/orders/{order_id}/refunds.json")


@mcp.tool()
def get_refund(order_id: int, refund_id: int) -> dict:
    """Retrieve a single refund."""
    return make_request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")


@mcp.tool()
def create_refund(order_id: int, line_items: Optional[list] = None, shipping: Optional[dict] = None,
                  note: Optional[str] = None) -> dict:
    """Create a refund for an order."""
    refund = {}
    if line_items:
        refund["line_items"] = line_items
    if shipping:
        refund["shipping"] = shipping
    if note:
        refund["note"] = note
    return make_request("POST", f"/orders/{order_id}/refunds.json", data={"refund": refund})


# TRANSACTIONS
@mcp.tool()
def list_transactions(order_id: int) -> dict:
    """Retrieve transactions for an order."""
    return make_request("GET", f"/orders/{order_id}/transactions.json")


@mcp.tool()
def get_transaction(order_id: int, transaction_id: int) -> dict:
    """Retrieve a single transaction."""
    return make_request("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")


# INVENTORY
@mcp.tool()
def list_inventory_items(limit: int = 50) -> dict:
    """Retrieve a list of inventory items."""
    return make_request("GET", "/inventory_items.json", params={"limit": min(limit, 250)})


@mcp.tool()
def get_inventory_item(inventory_item_id: int) -> dict:
    """Retrieve a single inventory item."""
    return make_request("GET", f"/inventory_items/{inventory_item_id}.json")


@mcp.tool()
def update_inventory_item(inventory_item_id: int, sku: Optional[str] = None,
                          tracked: Optional[bool] = None) -> dict:
    """Update an inventory item."""
    item = {"id": inventory_item_id}
    if sku is not None:
        item["sku"] = sku
    if tracked is not None:
        item["tracked"] = tracked
    return make_request("PUT", f"/inventory_items/{inventory_item_id}.json", data={"inventory_item": item})


@mcp.tool()
def list_inventory_levels(inventory_item_id: Optional[int] = None) -> dict:
    """Retrieve inventory levels."""
    params = {}
    if inventory_item_id:
        params["inventory_item_ids"] = str(inventory_item_id)
    return make_request("GET", "/inventory_levels.json", params=params)


@mcp.tool()
def adjust_inventory_level(inventory_item_id: int, location_id: int, available_adjustment: int) -> dict:
    """Adjust inventory level at a location."""
    return make_request("POST", "/inventory_levels/adjust.json",
                       data={"inventory_item_id": inventory_item_id, "location_id": location_id,
                             "available_adjustment": available_adjustment})


# LOCATIONS
@mcp.tool()
def list_locations() -> dict:
    """Retrieve a list of locations."""
    return make_request("GET", "/locations.json")


@mcp.tool()
def get_location(location_id: int) -> dict:
    """Retrieve a single location."""
    return make_request("GET", f"/locations/{location_id}.json")


# COLLECTIONS
@mcp.tool()
def list_custom_collections(limit: int = 50, status: str = "active") -> dict:
    """Retrieve a list of custom collections."""
    return make_request("GET", "/custom_collections.json", params={"limit": min(limit, 250), "status": status})


@mcp.tool()
def get_custom_collection(collection_id: int) -> dict:
    """Retrieve a single custom collection."""
    return make_request("GET", f"/custom_collections/{collection_id}.json")


@mcp.tool()
def create_custom_collection(title: str, body_html: Optional[str] = None,
                             image_src: Optional[str] = None) -> dict:
    """Create a custom collection."""
    collection = {"title": title}
    if body_html:
        collection["body_html"] = body_html
    if image_src:
        collection["image"] = {"src": image_src}
    return make_request("POST", "/custom_collections.json", data={"custom_collection": collection})


@mcp.tool()
def update_custom_collection(collection_id: int, title: Optional[str] = None,
                             body_html: Optional[str] = None) -> dict:
    """Update a custom collection."""
    collection = {"id": collection_id}
    if title is not None:
        collection["title"] = title
    if body_html is not None:
        collection["body_html"] = body_html
    return make_request("PUT", f"/custom_collections/{collection_id}.json", data={"custom_collection": collection})


@mcp.tool()
def delete_custom_collection(collection_id: int) -> dict:
    """Delete a custom collection."""
    return make_request("DELETE", f"/custom_collections/{collection_id}.json")


# COLLECTS
@mcp.tool()
def list_collects(collection_id: Optional[int] = None, product_id: Optional[int] = None) -> dict:
    """Retrieve collects (products in collections)."""
    params = {}
    if collection_id:
        params["collection_id"] = collection_id
    if product_id:
        params["product_id"] = product_id
    return make_request("GET", "/collects.json", params=params)


@mcp.tool()
def create_collect(collection_id: int, product_id: int) -> dict:
    """Add a product to a collection."""
    return make_request("POST", "/collects.json",
                       data={"collect": {"collection_id": collection_id, "product_id": product_id}})


@mcp.tool()
def delete_collect(collect_id: int) -> dict:
    """Remove a product from a collection."""
    return make_request("DELETE", f"/collects/{collect_id}.json")


# METAFIELDS
@mcp.tool()
def list_metafields(resource_type: str, resource_id: int) -> dict:
    """Retrieve metafields for a resource."""
    return make_request("GET", f"/{resource_type}/{resource_id}/metafields.json")


@mcp.tool()
def create_metafield(resource_type: str, resource_id: int, namespace: str, key: str, value: str,
                     type: str = "string") -> dict:
    """Create a metafield for a resource."""
    metafield = {"namespace": namespace, "key": key, "value": value, "type": type}
    return make_request("POST", f"/{resource_type}/{resource_id}/metafields.json", data={"metafield": metafield})


@mcp.tool()
def update_metafield(resource_type: str, resource_id: int, metafield_id: int,
                     value: Optional[str] = None) -> dict:
    """Update a metafield."""
    metafield = {"id": metafield_id}
    if value is not None:
        metafield["value"] = value
    return make_request("PUT", f"/{resource_type}/{resource_id}/metafields/{metafield_id}.json",
                       data={"metafield": metafield})


@mcp.tool()
def delete_metafield(resource_type: str, resource_id: int, metafield_id: int) -> dict:
    """Delete a metafield."""
    return make_request("DELETE", f"/{resource_type}/{resource_id}/metafields/{metafield_id}.json")


# WEBHOOKS
@mcp.tool()
def list_webhooks() -> dict:
    """Retrieve a list of webhooks."""
    return make_request("GET", "/webhooks.json")


@mcp.tool()
def get_webhook(webhook_id: int) -> dict:
    """Retrieve a single webhook."""
    return make_request("GET", f"/webhooks/{webhook_id}.json")


@mcp.tool()
def create_webhook(topic: str, address: str, format: str = "json") -> dict:
    """Create a webhook."""
    webhook = {"topic": topic, "address": address, "format": format}
    return make_request("POST", "/webhooks.json", data={"webhook": webhook})


@mcp.tool()
def update_webhook(webhook_id: int, address: Optional[str] = None, topic: Optional[str] = None) -> dict:
    """Update a webhook."""
    webhook = {"id": webhook_id}
    if address is not None:
        webhook["address"] = address
    if topic is not None:
        webhook["topic"] = topic
    return make_request("PUT", f"/webhooks/{webhook_id}.json", data={"webhook": webhook})


@mcp.tool()
def delete_webhook(webhook_id: int) -> dict:
    """Delete a webhook."""
    return make_request("DELETE", f"/webhooks/{webhook_id}.json")


# DRAFT ORDERS
@mcp.tool()
def list_draft_orders(status: str = "open") -> dict:
    """Retrieve a list of draft orders."""
    return make_request("GET", "/draft_orders.json", params={"status": status})


@mcp.tool()
def get_draft_order(draft_order_id: int) -> dict:
    """Retrieve a single draft order."""
    return make_request("GET", f"/draft_orders/{draft_order_id}.json")


@mcp.tool()
def create_draft_order(line_items: list, customer: Optional[dict] = None,
                       email: Optional[str] = None) -> dict:
    """Create a draft order."""
    draft_order = {"line_items": line_items}
    if customer:
        draft_order["customer"] = customer
    if email:
        draft_order["email"] = email
    return make_request("POST", "/draft_orders.json", data={"draft_order": draft_order})


@mcp.tool()
def update_draft_order(draft_order_id: int, line_items: Optional[list] = None,
                       email: Optional[str] = None) -> dict:
    """Update a draft order."""
    draft_order = {"id": draft_order_id}
    if line_items is not None:
        draft_order["line_items"] = line_items
    if email is not None:
        draft_order["email"] = email
    return make_request("PUT", f"/draft_orders/{draft_order_id}.json", data={"draft_order": draft_order})


@mcp.tool()
def delete_draft_order(draft_order_id: int) -> dict:
    """Delete a draft order."""
    return make_request("DELETE", f"/draft_orders/{draft_order_id}.json")


@mcp.tool()
def send_draft_order_invoice(draft_order_id: int, email: Optional[str] = None) -> dict:
    """Send an invoice for a draft order."""
    data = {}
    if email:
        data["email"] = email
    return make_request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json",
                       data=data if data else None)


# PRICE RULES
@mcp.tool()
def list_price_rules() -> dict:
    """Retrieve a list of price rules."""
    return make_request("GET", "/price_rules.json")


@mcp.tool()
def get_price_rule(price_rule_id: int) -> dict:
    """Retrieve a single price rule."""
    return make_request("GET", f"/price_rules/{price_rule_id}.json")


@mcp.tool()
def create_price_rule(title: str, target_type: str, target_selection: str, allocation_method: str,
                      value: str, value_type: str) -> dict:
    """Create a price rule."""
    price_rule = {"title": title, "target_type": target_type, "target_selection": target_selection,
                  "allocation_method": allocation_method, "value": value, "value_type": value_type}
    return make_request("POST", "/price_rules.json", data={"price_rule": price_rule})


@mcp.tool()
def update_price_rule(price_rule_id: int, title: Optional[str] = None,
                      value: Optional[str] = None) -> dict:
    """Update a price rule."""
    price_rule = {"id": price_rule_id}
    if title is not None:
        price_rule["title"] = title
    if value is not None:
        price_rule["value"] = value
    return make_request("PUT", f"/price_rules/{price_rule_id}.json", data={"price_rule": price_rule})


@mcp.tool()
def delete_price_rule(price_rule_id: int) -> dict:
    """Delete a price rule."""
    return make_request("DELETE", f"/price_rules/{price_rule_id}.json")


# DISCOUNT CODES
@mcp.tool()
def list_discount_codes(price_rule_id: int) -> dict:
    """Retrieve discount codes for a price rule."""
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json")


@mcp.tool()
def get_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """Retrieve a single discount code."""
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


@mcp.tool()
def create_discount_code(price_rule_id: int, code: str) -> dict:
    """Create a discount code."""
    discount_code = {"code": code}
    return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json",
                       data={"discount_code": discount_code})


@mcp.tool()
def update_discount_code(price_rule_id: int, discount_code_id: int, code: Optional[str] = None) -> dict:
    """Update a discount code."""
    discount_code = {"id": discount_code_id}
    if code is not None:
        discount_code["code"] = code
    return make_request("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
                       data={"discount_code": discount_code})


@mcp.tool()
def delete_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """Delete a discount code."""
    return make_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


# SHOP
@mcp.tool()
def get_shop() -> dict:
    """Retrieve shop information."""
    return make_request("GET", "/shop.json")


if __name__ == "__main__":
    mcp.run()
