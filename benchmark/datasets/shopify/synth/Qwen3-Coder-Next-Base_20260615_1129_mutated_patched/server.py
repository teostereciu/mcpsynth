#!/usr/bin/env python3
"""
Shopify Admin REST API MCP Server
Runs over stdio using FastMCP
"""

from fastmcp import FastMCP
from fastmcp.server.stdio import stdio_server
import os
import requests
import logging

logger = logging.getLogger(__name__)
mcp = FastMCP("shopify-admin")

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_headers() -> dict:
    """Construct Shopify API headers with authentication."""
    access_token = os.getenv("SHOPIFY_ACCESS_TOKEN")
    store_url = os.getenv("SHOPIFY_STORE_URL")
    
    if not access_token:
        raise ValueError("SHOPIFY_ACCESS_TOKEN environment variable is required")
    if not store_url:
        raise ValueError("SHOPIFY_STORE_URL environment variable is required")
    
    return {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json",
        "User-Agent": "ShopifyAdminMCP/1.0"
    }

def get_base_url() -> str:
    """Construct the Shopify API base URL."""
    store_url = os.getenv("SHOPIFY_STORE_URL")
    if not store_url:
        raise ValueError("SHOPIFY_STORE_URL environment variable is required")
    return f"https://{store_url}/admin/api/2026-01"

def make_request(method: str, path: str, params: dict = None, 
                 json: dict = None) -> dict:
    """Make a request to the Shopify API and return parsed JSON response."""
    base_url = get_base_url()
    url = f"{base_url}{path}"
    headers = get_headers()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_data = response.json()
            error_msg = error_data.get("errors", str(e))
        except:
            error_msg = str(e)
        return {"error": error_msg}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# ============================================================================
# API ENDPOINT TOOLS
# ============================================================================

# ---------- SHOP ----------
@mcp.tool()
def get_shop(fields: str = None) -> dict:
    """Retrieve the shop's configuration
    
    Documentation: docs/api_shop.md
    Endpoint: GET /admin/api/2026-01/shop.json
    """
    params = {}
    if fields:
        params["fields"] = fields
    result = make_request("GET", "/shop.json", params=params)
    return result.get("shop", result)

# ---------- CUSTOMER ----------
@mcp.tool()
def create_customer(customer: dict) -> dict:
    """Create a customer
    
    Documentation: docs/api_customer.md
    Endpoint: POST /admin/api/2026-01/customers.json
    """
    payload = {"customer": customer}
    result = make_request("POST", "/customers.json", json=payload)
    return result.get("customer", result)

@mcp.tool()
def get_customers(ids: str = None, limit: int = 50, page: int = 1) -> dict:
    """Retrieve a list of customers
    
    Documentation: docs/api_customer.md
    Endpoint: GET /admin/api/2026-01/customers.json
    """
    params = {"limit": limit, "page": page}
    if ids:
        params["ids"] = ids
    result = make_request("GET", "/customers.json", params=params)
    return result.get("customers", result)

@mcp.tool()
def get_customer(customer_id: int) -> dict:
    """Retrieve a specific customer
    
    Documentation: docs/api_customer.md
    Endpoint: GET /admin/api/2026-01/customers/{customer_id}.json
    """
    result = make_request("GET", f"/customers/{customer_id}.json")
    return result.get("customer", result)

@mcp.tool()
def update_customer(customer_id: int, customer: dict) -> dict:
    """Update a customer
    
    Documentation: docs/api_customer.md
    Endpoint: PUT /admin/api/2026-01/customers/{customer_id}.json
    """
    payload = {"customer": customer}
    result = make_request("PUT", f"/customers/{customer_id}.json", json=payload)
    return result.get("customer", result)

@mcp.tool()
def delete_customer(customer_id: int) -> dict:
    """Delete a customer (cannot be undone)
    
    Documentation: docs/api_customer.md
    Endpoint: DELETE /admin/api/2026-01/customers/{customer_id}.json
    """
    result = make_request("DELETE", f"/customers/{customer_id}.json")
    return result

@mcp.tool()
def search_customers(query: str, page: int = 1, limit: int = 50) -> dict:
    """Search for customers that match a query
    
    Documentation: docs/api_customer.md
    Endpoint: GET /admin/api/2026-01/customers/search.json
    """
    params = {"query": query, "page": page, "limit": limit}
    result = make_request("GET", "/customers/search.json", params=params)
    return result.get("customers", result)

@mcp.tool()
def get_customer_orders(customer_id: int, status: str = "any", 
                       limit: int = 50) -> dict:
    """Retrieve all orders for a customer
    
    Documentation: docs/api_customer.md
    Endpoint: GET /admin/api/2026-01/customers/{customer_id}/orders.json
    """
    params = {"status": status, "limit": limit}
    result = make_request("GET", f"/customers/{customer_id}/orders.json", 
                         params=params)
    return result.get("orders", result)

@mcp.tool()
def get_customer_count(query: str = None) -> dict:
    """Retrieve a count of customers
    
    Documentation: docs/api_customer.md
    Endpoint: GET /admin/api/2026-01/customers/count.json
    """
    params = {}
    if query:
        params["query"] = query
    result = make_request("GET", "/customers/count.json", params=params)
    return result.get("count", result)

# ---------- ORDER ----------
@mcp.tool()
def create_order(order: dict) -> dict:
    """Create an order
    
    Documentation: docs/api_order.md
    Endpoint: POST /admin/api/2026-01/orders.json
    """
    payload = {"order": order}
    result = make_request("POST", "/orders.json", json=payload)
    return result.get("order", result)

@mcp.tool()
def get_orders(status: str = "any", limit: int = 50, page: int = 1) -> dict:
    """Retrieve a list of orders
    
    Documentation: docs/api_order.md
    Endpoint: GET /admin/api/2026-01/orders.json
    """
    params = {"status": status, "limit": limit, "page": page}
    result = make_request("GET", "/orders.json", params=params)
    return result.get("orders", result)

@mcp.tool()
def get_order(order_id: int) -> dict:
    """Retrieve a specific order
    
    Documentation: docs/api_order.md
    Endpoint: GET /admin/api/2026-01/orders/{order_id}.json
    """
    result = make_request("GET", f"/orders/{order_id}.json")
    return result.get("order", result)

@mcp.tool()
def get_order_count(status: str = "any") -> dict:
    """Retrieve an order count
    
    Documentation: docs/api_order.md
    Endpoint: GET /admin/api/2026-01/orders/count.json
    """
    params = {"status": status}
    result = make_request("GET", "/orders/count.json", params=params)
    return result.get("count", result)

@mcp.tool()
def update_order(order_id: int, order: dict) -> dict:
    """Update an order
    
    Documentation: docs/api_order.md
    Endpoint: PUT /admin/api/2026-01/orders/{order_id}.json
    """
    payload = {"order": order}
    result = make_request("PUT", f"/orders/{order_id}.json", json=payload)
    return result.get("order", result)

@mcp.tool()
def delete_order(order_id: int) -> dict:
    """Delete an order
    
    Documentation: docs/api_order.md
    Endpoint: DELETE /admin/api/2026-01/orders/{order_id}.json
    """
    result = make_request("DELETE", f"/orders/{order_id}.json")
    return result

@mcp.tool()
def cancel_order(order_id: int, 
                 refund: dict = None,
                 note: str = None) -> dict:
    """Cancel an order
    
    Documentation: docs/api_order.md
    Endpoint: POST /admin/api/2026-01/orders/{order_id}/cancel.json
    """
    payload = {}
    if refund:
        payload["refund"] = refund
    if note:
        payload["note"] = note
    result = make_request("POST", f"/orders/{order_id}/cancel.json", json=payload)
    return result.get("order", result)

@mcp.tool()
def close_order(order_id: int) -> dict:
    """Close an order
    
    Documentation: docs/api_order.md
    Endpoint: POST /admin/api/2026-01/orders/{order_id}/close.json
    """
    result = make_request("POST", f"/orders/{order_id}/close.json")
    return result.get("order", result)

@mcp.tool()
def open_order(order_id: int) -> dict:
    """Re-open a closed order
    
    Documentation: docs/api_order.md
    Endpoint: POST /admin/api/2026-01/orders/{order_id}/open.json
    """
    result = make_request("POST", f"/orders/{order_id}/open.json")
    return result.get("order", result)

# ---------- PRODUCT ----------
@mcp.tool()
def create_product(product: dict) -> dict:
    """Create a new product
    
    Documentation: docs/api_product.md
    Endpoint: POST /admin/api/2026-01/products.json
    """
    payload = {"product": product}
    result = make_request("POST", "/products.json", json=payload)
    return result.get("product", result)

@mcp.tool()
def get_products(ids: str = None, limit: int = 50, page: int = 1) -> dict:
    """Retrieve a list of products
    
    Documentation: docs/api_product.md
    Endpoint: GET /admin/api/2026-01/products.json
    """
    params = {"limit": limit, "page": page}
    if ids:
        params["ids"] = ids
    result = make_request("GET", "/products.json", params=params)
    return result.get("products", result)

@mcp.tool()
def get_product(product_id: int) -> dict:
    """Retrieve a single product
    
    Documentation: docs/api_product.md
    Endpoint: GET /admin/api/2026-01/products/{product_id}.json
    """
    result = make_request("GET", f"/products/{product_id}.json")
    return result.get("product", result)

@mcp.tool()
def get_product_count() -> dict:
    """Retrieve a count of products
    
    Documentation: docs/api_product.md
    Endpoint: GET /admin/api/2026-01/products/count.json
    """
    result = make_request("GET", "/products/count.json")
    return result.get("count", result)

@mcp.tool()
def update_product(product_id: int, product: dict) -> dict:
    """Update a product
    
    Documentation: docs/api_product.md
    Endpoint: PUT /admin/api/2026-01/products/{product_id}.json
    """
    payload = {"product": product}
    result = make_request("PUT", f"/products/{product_id}.json", json=payload)
    return result.get("product", result)

@mcp.tool()
def delete_product(product_id: int) -> dict:
    """Delete a product
    
    Documentation: docs/api_product.md
    Endpoint: DELETE /admin/api/2026-01/products/{product_id}.json
    """
    result = make_request("DELETE", f"/products/{product_id}.json")
    return result

# ---------- VARIANT ----------
@mcp.tool()
def create_variant(variant: dict) -> dict:
    """Create a product variant
    
    Documentation: docs/api_product-variant.md
    Endpoint: POST /admin/api/2026-01/variants.json
    """
    payload = {"variant": variant}
    result = make_request("POST", "/variants.json", json=payload)
    return result.get("variant", result)

@mcp.tool()
def get_variants(product_id: int = None, ids: str = None, 
                limit: int = 50) -> dict:
    """Retrieve a list of product variants
    
    Documentation: docs/api_product-variant.md
    Endpoint: GET /admin/api/2026-01/variants.json
    """
    params = {"limit": limit}
    if product_id:
        params["product_id"] = product_id
    if ids:
        params["ids"] = ids
    result = make_request("GET", "/variants.json", params=params)
    return result.get("variants", result)

@mcp.tool()
def get_variant(variant_id: int) -> dict:
    """Retrieve a specific product variant
    
    Documentation: docs/api_product-variant.md
    Endpoint: GET /admin/api/2026-01/variants/{variant_id}.json
    """
    result = make_request("GET", f"/variants/{variant_id}.json")
    return result.get("variant", result)

@mcp.tool()
def update_variant(variant_id: int, variant: dict) -> dict:
    """Update a product variant
    
    Documentation: docs/api_product-variant.md
    Endpoint: PUT /admin/api/2026-01/variants/{variant_id}.json
    """
    payload = {"variant": variant}
    result = make_request("PUT", f"/variants/{variant_id}.json", json=payload)
    return result.get("variant", result)

@mcp.tool()
def delete_variant(variant_id: int) -> dict:
    """Delete a product variant
    
    Documentation: docs/api_product-variant.md
    Endpoint: DELETE /admin/api/2026-01/variants/{variant_id}.json
    """
    result = make_request("DELETE", f"/variants/{variant_id}.json")
    return result

# ---------- INVENTORY ----------
@mcp.tool()
def get_inventory_items(ids: str = None, limit: int = 50) -> dict:
    """Retrieve inventory items
    
    Documentation: docs/api_inventoryitem.md
    Endpoint: GET /admin/api/2026-01/inventory_items.json
    """
    params = {"limit": limit}
    if ids:
        params["ids"] = ids
    result = make_request("GET", "/inventory_items.json", params=params)
    return result.get("inventory_items", result)

@mcp.tool()
def update_inventory_item(id: int, cost: str = None, tracked: bool = None) -> dict:
    """Update an inventory item
    
    Documentation: docs/api_inventoryitem.md
    Endpoint: PUT /admin/api/2026-01/inventory_items/{id}.json
    """
    payload = {"inventory_item": {}}
    if cost is not None:
        payload["inventory_item"]["cost"] = cost
    if tracked is not None:
        payload["inventory_item"]["tracked"] = tracked
    result = make_request("PUT", f"/inventory_items/{id}.json", json=payload)
    return result.get("inventory_item", result)

@mcp.tool()
def create_location(name: str, address1: str, city: str, country: str,
                   province: str = None, zip: str = None) -> dict:
    """Create a location
    
    Documentation: docs/api_location.md
    Endpoint: POST /admin/api/2026-01/locations.json
    """
    payload = {"location": {
        "name": name,
        "address1": address1,
        "city": city,
        "country": country
    }}
    if province:
        payload["location"]["province"] = province
    if zip:
        payload["location"]["zip"] = zip
    result = make_request("POST", "/locations.json", json=payload)
    return result.get("location", result)

@mcp.tool()
def get_locations(ids: str = None, limit: int = 50) -> dict:
    """Retrieve a list of locations
    
    Documentation: docs/api_location.md
    Endpoint: GET /admin/api/2026-01/locations.json
    """
    params = {"limit": limit}
    if ids:
        params["ids"] = ids
    result = make_request("GET", "/locations.json", params=params)
    return result.get("locations", result)

@mcp.tool()
def get_inventory_levels(ids: str = None, location_ids: str = None,
                        sku: str = None, limit: int = 50) -> dict:
    """Retrieve inventory levels
    
    Documentation: docs/api_inventorylevel.md
    Endpoint: GET /admin/api/2026-01/inventory_levels.json
    """
    params = {"limit": limit}
    if ids:
        params["ids"] = ids
    if location_ids:
        params["location_ids"] = location_ids
    if sku:
        params["sku"] = sku
    result = make_request("GET", "/inventory_levels.json", params=params)
    return result.get("inventory_levels", result)

# ---------- COLLECTION ----------
@mcp.tool()
def create_custom_collection(title: str, body_html: str = None,
                            sort_order: str = "manual") -> dict:
    """Create a custom collection
    
    Documentation: docs/api_customcollection.md
    Endpoint: POST /admin/api/2026-01/custom_collections.json
    """
    payload = {
        "custom_collection": {
            "title": title,
            "sort_order": sort_order
        }
    }
    if body_html:
        payload["custom_collection"]["body_html"] = body_html
    result = make_request("POST", "/custom_collections.json", json=payload)
    return result.get("custom_collection", result)

@mcp.tool()
def get_custom_collections(ids: str = None, limit: int = 50) -> dict:
    """Retrieve a list of custom collections
    
    Documentation: docs/api_customcollection.md
    Endpoint: GET /admin/api/2026-01/custom_collections.json
    """
    params = {"limit": limit}
    if ids:
        params["ids"] = ids
    result = make_request("GET", "/custom_collections.json", params=params)
    return result.get("custom_collections", result)

@mcp.tool()
def get_custom_collection(collection_id: int) -> dict:
    """Retrieve a specific custom collection
    
    Documentation: docs/api_customcollection.md
    Endpoint: GET /admin/api/2026-01/custom_collections/{collection_id}.json
    """
    result = make_request("GET", f"/custom_collections/{collection_id}.json")
    return result.get("custom_collection", result)

@mcp.tool()
def update_custom_collection(collection_id: int, collection: dict) -> dict:
    """Update a custom collection
    
    Documentation: docs/api_customcollection.md
    Endpoint: PUT /admin/api/2026-01/custom_collections/{collection_id}.json
    """
    payload = {"custom_collection": collection}
    result = make_request("PUT", f"/custom_collections/{collection_id}.json",
                         json=payload)
    return result.get("custom_collection", result)

@mcp.tool()
def delete_custom_collection(collection_id: int) -> dict:
    """Delete a custom collection
    
    Documentation: docs/api_customcollection.md
    Endpoint: DELETE /admin/api/2026-01/custom_collections/{collection_id}.json
    """
    result = make_request("DELETE", f"/custom_collections/{collection_id}.json")
    return result

# ---------- DISCOUNT ----------
@mcp.tool()
def create_pricerule(name: str, value_type: str, value: str,
                    target_type: str, target_selection: str,
                    allocation_method: str) -> dict:
    """Create a price rule
    
    Documentation: docs/api_pricerule.md
    Endpoint: POST /admin/api/2026-01/price_rules.json
    """
    payload = {
        "price_rule": {
            "title": name,
            "target_type": target_type,
            "target_selection": target_selection,
            "allocation_method": allocation_method,
            "value_type": value_type,
            "value": value
        }
    }
    result = make_request("POST", "/price_rules.json", json=payload)
    return result.get("price_rule", result)

@mcp.tool()
def get_price_rules(limit: int = 50) -> dict:
    """Retrieve a list of price rules
    
    Documentation: docs/api_pricerule.md
    Endpoint: GET /admin/api/2026-01/price_rules.json
    """
    params = {"limit": limit}
    result = make_request("GET", "/price_rules.json", params=params)
    return result.get("price_rules", result)

@mcp.tool()
def get_price_rule(rule_id: int) -> dict:
    """Retrieve a specific price rule
    
    Documentation: docs/api_pricerule.md
    Endpoint: GET /admin/api/2026-01/price_rules/{rule_id}.json
    """
    result = make_request("GET", f"/price_rules/{rule_id}.json")
    return result.get("price_rule", result)

@mcp.tool()
def update_price_rule(rule_id: int, price_rule: dict) -> dict:
    """Update a price rule
    
    Documentation: docs/api_pricerule.md
    Endpoint: PUT /admin/api/2026-01/price_rules/{rule_id}.json
    """
    payload = {"price_rule": price_rule}
    result = make_request("PUT", f"/price_rules/{rule_id}.json", json=payload)
    return result.get("price_rule", result)

@mcp.tool()
def delete_price_rule(rule_id: int) -> dict:
    """Delete a price rule
    
    Documentation: docs/api_pricerule.md
    Endpoint: DELETE /admin/api/2026-01/price_rules/{rule_id}.json
    """
    result = make_request("DELETE", f"/price_rules/{rule_id}.json")
    return result

@mcp.tool()
def create_discount_code(code: str, price_rule_id: int,
                        usage_limit: int = None) -> dict:
    """Create a discount code
    
    Documentation: docs/api_discountcode.md
    Endpoint: POST /admin/api/2026-01/discount_codes.json
    """
    payload = {
        "discount_code": {
            "code": code,
            "price_rule_id": price_rule_id
        }
    }
    if usage_limit:
        payload["discount_code"]["usage_limit"] = usage_limit
    result = make_request("POST", "/discount_codes.json", json=payload)
    return result.get("discount_code", result)

# ---------- WEBHOOK ----------
@mcp.tool()
def create_webhook(topic: str, address: str, format: str = "json",
                  fields: list = None, metafield_namespaces: list = None) -> dict:
    """Create a new webhook subscription
    
    Documentation: docs/api_webhook.md
    Endpoint: POST /admin/api/2026-01/webhooks.json
    """
    payload = {
        "webhook": {
            "topic": topic,
            "address": address,
            "format": format
        }
    }
    if fields:
        payload["webhook"]["fields"] = fields
    if metafield_namespaces:
        payload["webhook"]["metafield_namespaces"] = metafield_namespaces
    result = make_request("POST", "/webhooks.json", json=payload)
    return result.get("webhook", result)

@mcp.tool()
def get_webhooks(topic: str = None, limit: int = 50) -> dict:
    """Retrieve a list of webhooks
    
    Documentation: docs/api_webhook.md
    Endpoint: GET /admin/api/2026-01/webhooks.json
    """
    params = {"limit": limit}
    if topic:
        params["topic"] = topic
    result = make_request("GET", "/webhooks.json", params=params)
    return result.get("webhooks", result)

@mcp.tool()
def get_webhook(webhook_id: int) -> dict:
    """Receive a specific webhook subscription
    
    Documentation: docs/api_webhook.md
    Endpoint: GET /admin/api/2026-01/webhooks/{webhook_id}.json
    """
    result = make_request("GET", f"/webhooks/{webhook_id}.json")
    return result.get("webhook", result)

@mcp.tool()
def get_webhook_count(topic: str = None) -> dict:
    """Receive a count of all webhooks
    
    Documentation: docs/api_webhook.md
    Endpoint: GET /admin/api/2026-01/webhooks/count.json
    """
    params = {}
    if topic:
        params["topic"] = topic
    result = make_request("GET", "/webhooks/count.json", params=params)
    return result.get("count", result)

@mcp.tool()
def update_webhook(webhook_id: int, webhook: dict) -> dict:
    """Modify an existing webhook subscription
    
    Documentation: docs/api_webhook.md
    Endpoint: PUT /admin/api/2026-01/webhooks/{webhook_id}.json
    """
    payload = {"webhook": webhook}
    result = make_request("PUT", f"/webhooks/{webhook_id}.json", json=payload)
    return result.get("webhook", result)

@mcp.tool()
def delete_webhook(webhook_id: int) -> dict:
    """Remove an existing webhook subscription
    
    Documentation: docs/api_webhook.md
    Endpoint: DELETE /admin/api/2026-01/webhooks/{webhook_id}.json
    """
    result = make_request("DELETE", f"/webhooks/{webhook_id}.json")
    return result

# ---------- METAFIELD ----------
@mcp.tool()
def create_metafield(owner_id: int, owner_resource: str, key: str,
                    namespace: str, value: str, type: str) -> dict:
    """Create a metafield
    
    Documentation: docs/api_metafield.md
    Endpoint: POST /admin/api/2026-01/metafields.json
    """
    payload = {
        "metafield": {
            "owner_id": owner_id,
            "owner_resource": owner_resource,
            "key": key,
            "namespace": namespace,
            "value": value,
            "type": type
        }
    }
    result = make_request("POST", "/metafields.json", json=payload)
    return result.get("metafield", result)

@mcp.tool()
def get_metafields(owner_id: int, owner_resource: str,
                  limit: int = 50) -> dict:
    """Retrieve metafields
    
    Documentation: docs/api_metafield.md
    Endpoint: GET /admin/api/2026-01/metafields.json
    """
    params = {
        "owner_id": owner_id,
        "owner_resource": owner_resource,
        "limit": limit
    }
    result = make_request("GET", "/metafields.json", params=params)
    return result.get("metafields", result)

@mcp.tool()
def get_metafield(metafield_id: int) -> dict:
    """Retrieve a specific metafield
    
    Documentation: docs/api_metafield.md
    Endpoint: GET /admin/api/2026-01/metafields/{metafield_id}.json
    """
    result = make_request("GET", f"/metafields/{metafield_id}.json")
    return result.get("metafield", result)

# ---------- REFUND ----------
@mcp.tool()
def create_refund(order_id: int, transaction_id: int = None,
                 refund_line_items: list = None,
                 restock: str = "return") -> dict:
    """Create a refund
    
    Documentation: docs/api_refund.md
    Endpoint: POST /admin/api/2026-01/orders/{order_id}/refunds.json
    """
    payload = {
        "refund": {
            "restock": restock
        }
    }
    if transaction_id:
        payload["refund"]["transaction_id"] = transaction_id
    if refund_line_items:
        payload["refund"]["refund_line_items"] = refund_line_items
    result = make_request("POST", f"/orders/{order_id}/refunds.json",
                         json=payload)
    return result.get("refund", result)

# ============================================================================
# GROUNDING DEFINITION
# ============================================================================

GROUNDING = {
    # SHOP
    "get_shop": {
        "doc": "docs/api_shop.md",
        "endpoint": "GET /admin/api/2026-01/shop.json"
    },
    
    # CUSTOMER
    "create_customer": {
        "doc": "docs/api_customer.md",
        "endpoint": "POST /admin/api/2026-01/customers.json"
    },
    "get_customers": {
        "doc": "docs/api_customer.md",
        "endpoint": "GET /admin/api/2026-01/customers.json"
    },
    "get_customer": {
        "doc": "docs/api_customer.md",
        "endpoint": "GET /admin/api/2026-01/customers/{customer_id}.json"
    },
    "update_customer": {
        "doc": "docs/api_customer.md",
        "endpoint": "PUT /admin/api/2026-01/customers/{customer_id}.json"
    },
    "delete_customer": {
        "doc": "docs/api_customer.md",
        "endpoint": "DELETE /admin/api/2026-01/customers/{customer_id}.json"
    },
    "search_customers": {
        "doc": "docs/api_customer.md",
        "endpoint": "GET /admin/api/2026-01/customers/search.json"
    },
    "get_customer_orders": {
        "doc": "docs/api_customer.md",
        "endpoint": "GET /admin/api/2026-01/customers/{customer_id}/orders.json"
    },
    "get_customer_count": {
        "doc": "docs/api_customer.md",
        "endpoint": "GET /admin/api/2026-01/customers/count.json"
    },
    
    # ORDER
    "create_order": {
        "doc": "docs/api_order.md",
        "endpoint": "POST /admin/api/2026-01/orders.json"
    },
    "get_orders": {
        "doc": "docs/api_order.md",
        "endpoint": "GET /admin/api/2026-01/orders.json"
    },
    "get_order": {
        "doc": "docs/api_order.md",
        "endpoint": "GET /admin/api/2026-01/orders/{order_id}.json"
    },
    "get_order_count": {
        "doc": "docs/api_order.md",
        "endpoint": "GET /admin/api/2026-01/orders/count.json"
    },
    "update_order": {
        "doc": "docs/api_order.md",
        "endpoint": "PUT /admin/api/2026-01/orders/{order_id}.json"
    },
    "delete_order": {
        "doc": "docs/api_order.md",
        "endpoint": "DELETE /admin/api/2026-01/orders/{order_id}.json"
    },
    "cancel_order": {
        "doc": "docs/api_order.md",
        "endpoint": "POST /admin/api/2026-01/orders/{order_id}/cancel.json"
    },
    "close_order": {
        "doc": "docs/api_order.md",
        "endpoint": "POST /admin/api/2026-01/orders/{order_id}/close.json"
    },
    "open_order": {
        "doc": "docs/api_order.md",
        "endpoint": "POST /admin/api/2026-01/orders/{order_id}/open.json"
    },
    
    # PRODUCT
    "create_product": {
        "doc": "docs/api_product.md",
        "endpoint": "POST /admin/api/2026-01/products.json"
    },
    "get_products": {
        "doc": "docs/api_product.md",
        "endpoint": "GET /admin/api/2026-01/products.json"
    },
    "get_product": {
        "doc": "docs/api_product.md",
        "endpoint": "GET /admin/api/2026-01/products/{product_id}.json"
    },
    "get_product_count": {
        "doc": "docs/api_product.md",
        "endpoint": "GET /admin/api/2026-01/products/count.json"
    },
    "update_product": {
        "doc": "docs/api_product.md",
        "endpoint": "PUT /admin/api/2026-01/products/{product_id}.json"
    },
    "delete_product": {
        "doc": "docs/api_product.md",
        "endpoint": "DELETE /admin/api/2026-01/products/{product_id}.json"
    },
    
    # VARIANT
    "create_variant": {
        "doc": "docs/api_product-variant.md",
        "endpoint": "POST /admin/api/2026-01/variants.json"
    },
    "get_variants": {
        "doc": "docs/api_product-variant.md",
        "endpoint": "GET /admin/api/2026-01/variants.json"
    },
    "get_variant": {
        "doc": "docs/api_product-variant.md",
        "endpoint": "GET /admin/api/2026-01/variants/{variant_id}.json"
    },
    "update_variant": {
        "doc": "docs/api_product-variant.md",
        "endpoint": "PUT /admin/api/2026-01/variants/{variant_id}.json"
    },
    "delete_variant": {
        "doc": "docs/api_product-variant.md",
        "endpoint": "DELETE /admin/api/2026-01/variants/{variant_id}.json"
    },
    
    # INVENTORY
    "get_inventory_items": {
        "doc": "docs/api_inventoryitem.md",
        "endpoint": "GET /admin/api/2026-01/inventory_items.json"
    },
    "update_inventory_item": {
        "doc": "docs/api_inventoryitem.md",
        "endpoint": "PUT /admin/api/2026-01/inventory_items/{id}.json"
    },
    "create_location": {
        "doc": "docs/api_location.md",
        "endpoint": "POST /admin/api/2026-01/locations.json"
    },
    "get_locations": {
        "doc": "docs/api_location.md",
        "endpoint": "GET /admin/api/2026-01/locations.json"
    },
    "get_inventory_levels": {
        "doc": "docs/api_inventorylevel.md",
        "endpoint": "GET /admin/api/2026-01/inventory_levels.json"
    },
    
    # COLLECTION
    "create_custom_collection": {
        "doc": "docs/api_customcollection.md",
        "endpoint": "POST /admin/api/2026-01/custom_collections.json"
    },
    "get_custom_collections": {
        "doc": "docs/api_customcollection.md",
        "endpoint": "GET /admin/api/2026-01/custom_collections.json"
    },
    "get_custom_collection": {
        "doc": "docs/api_customcollection.md",
        "endpoint": "GET /admin/api/2026-01/custom_collections/{collection_id}.json"
    },
    "update_custom_collection": {
        "doc": "docs/api_customcollection.md",
        "endpoint": "PUT /admin/api/2026-01/custom_collections/{collection_id}.json"
    },
    "delete_custom_collection": {
        "doc": "docs/api_customcollection.md",
        "endpoint": "DELETE /admin/api/2026-01/custom_collections/{collection_id}.json"
    },
    
    # DISCOUNT
    "create_pricerule": {
        "doc": "docs/api_pricerule.md",
        "endpoint": "POST /admin/api/2026-01/price_rules.json"
    },
    "get_price_rules": {
        "doc": "docs/api_pricerule.md",
        "endpoint": "GET /admin/api/2026-01/price_rules.json"
    },
    "get_price_rule": {
        "doc": "docs/api_pricerule.md",
        "endpoint": "GET /admin/api/2026-01/price_rules/{rule_id}.json"
    },
    "update_price_rule": {
        "doc": "docs/api_pricerule.md",
        "endpoint": "PUT /admin/api/2026-01/price_rules/{rule_id}.json"
    },
    "delete_price_rule": {
        "doc": "docs/api_pricerule.md",
        "endpoint": "DELETE /admin/api/2026-01/price_rules/{rule_id}.json"
    },
    "create_discount_code": {
        "doc": "docs/api_discountcode.md",
        "endpoint": "POST /admin/api/2026-01/discount_codes.json"
    },
    
    # WEBHOOK
    "create_webhook": {
        "doc": "docs/api_webhook.md",
        "endpoint": "POST /admin/api/2026-01/webhooks.json"
    },
    "get_webhooks": {
        "doc": "docs/api_webhook.md",
        "endpoint": "GET /admin/api/2026-01/webhooks.json"
    },
    "get_webhook": {
        "doc": "docs/api_webhook.md",
        "endpoint": "GET /admin/api/2026-01/webhooks/{webhook_id}.json"
    },
    "get_webhook_count": {
        "doc": "docs/api_webhook.md",
        "endpoint": "GET /admin/api/2026-01/webhooks/count.json"
    },
    "update_webhook": {
        "doc": "docs/api_webhook.md",
        "endpoint": "PUT /admin/api/2026-01/webhooks/{webhook_id}.json"
    },
    "delete_webhook": {
        "doc": "docs/api_webhook.md",
        "endpoint": "DELETE /admin/api/2026-01/webhooks/{webhook_id}.json"
    },
    
    # METAFIELD
    "create_metafield": {
        "doc": "docs/api_metafield.md",
        "endpoint": "POST /admin/api/2026-01/metafields.json"
    },
    "get_metafields": {
        "doc": "docs/api_metafield.md",
        "endpoint": "GET /admin/api/2026-01/metafields.json"
    },
    "get_metafield": {
        "doc": "docs/api_metafield.md",
        "endpoint": "GET /admin/api/2026-01/metafields/{metafield_id}.json"
    },
    
    # REFUND
    "create_refund": {
        "doc": "docs/api_refund.md",
        "endpoint": "POST /admin/api/2026-01/orders/{order_id}/refunds.json"
    }
}

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Shopify Admin MCP Server")
    parser.add_argument("--stdio", action="store_true", help="Run over stdio")
    args = parser.parse_args()
    
    if args.stdio:
        # Run over stdio
        with stdio_server() as (read, write):
            async def reader():
                while True:
                    await read()
                    write("")
            
            import asyncio
            asyncio.run(reader())
    else:
        # Run with MCP server
        print("Shopify Admin MCP Server is ready!")
        print("Usage: mcp-server --stdio")
        print("For more information, use --help")
