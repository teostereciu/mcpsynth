import os
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("shopify_admin")

def get_api_base() -> str:
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    if not store_url:
        raise ValueError("SHOPIFY_STORE_URL environment variable is required")
    return f"https://{store_url}/admin/api/2026-01"

def get_headers() -> Dict[str, str]:
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    if not token:
        raise ValueError("SHOPIFY_ACCESS_TOKEN environment variable is required")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

def make_request(method: str, endpoint: str, params: Optional[Dict] = None, json: Optional[Dict] = None) -> Any:
    url = f"{get_api_base()}{endpoint}"
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=get_headers(),
            params=params,
            json=json
        )
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_msg = e.response.json()
            except ValueError:
                error_msg = e.response.text
        return {"error": error_msg}

# Products
@mcp.tool()
def get_products(limit: int = 50, status: str = "active", title: Optional[str] = None) -> Any:
    """Retrieve a list of products."""
    params = {"limit": limit, "status": status}
    if title:
        params["title"] = title
    return make_request("GET", "/products.json", params=params)

@mcp.tool()
def get_product(product_id: int) -> Any:
    """Retrieve a single product by ID."""
    return make_request("GET", f"/products/{product_id}.json")

@mcp.tool()
def create_product(title: str, body_html: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None, tags: Optional[str] = None) -> Any:
    """Create a new product."""
    product = {"title": title}
    if body_html: product["body_html"] = body_html
    if vendor: product["vendor"] = vendor
    if product_type: product["product_type"] = product_type
    if tags: product["tags"] = tags
    return make_request("POST", "/products.json", json={"product": product})

@mcp.tool()
def update_product(product_id: int, title: Optional[str] = None, body_html: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None, tags: Optional[str] = None) -> Any:
    """Update an existing product."""
    product = {"id": product_id}
    if title: product["title"] = title
    if body_html: product["body_html"] = body_html
    if vendor: product["vendor"] = vendor
    if product_type: product["product_type"] = product_type
    if tags: product["tags"] = tags
    return make_request("PUT", f"/products/{product_id}.json", json={"product": product})

@mcp.tool()
def delete_product(product_id: int) -> Any:
    """Delete a product."""
    return make_request("DELETE", f"/products/{product_id}.json")

# Product Variants
@mcp.tool()
def get_product_variants(product_id: int) -> Any:
    """Retrieve a list of product variants."""
    return make_request("GET", f"/products/{product_id}/variants.json")

@mcp.tool()
def create_product_variant(product_id: int, price: str, option1: str, sku: Optional[str] = None) -> Any:
    """Create a new product variant."""
    variant = {"price": price, "option1": option1}
    if sku: variant["sku"] = sku
    return make_request("POST", f"/products/{product_id}/variants.json", json={"variant": variant})

# Product Images
@mcp.tool()
def get_product_images(product_id: int) -> Any:
    """Retrieve a list of product images."""
    return make_request("GET", f"/products/{product_id}/images.json")

@mcp.tool()
def create_product_image(product_id: int, src: str) -> Any:
    """Create a new product image."""
    return make_request("POST", f"/products/{product_id}/images.json", json={"image": {"src": src}})

# Orders
@mcp.tool()
def get_orders(limit: int = 50, status: str = "any", financial_status: Optional[str] = None, fulfillment_status: Optional[str] = None) -> Any:
    """Retrieve a list of orders."""
    params = {"limit": limit, "status": status}
    if financial_status: params["financial_status"] = financial_status
    if fulfillment_status: params["fulfillment_status"] = fulfillment_status
    return make_request("GET", "/orders.json", params=params)

@mcp.tool()
def get_order(order_id: int) -> Any:
    """Retrieve a single order by ID."""
    return make_request("GET", f"/orders/{order_id}.json")

@mcp.tool()
def create_order(line_items: List[Dict[str, Any]], email: Optional[str] = None, financial_status: Optional[str] = None) -> Any:
    """Create a new order. line_items should be a list of dicts with variant_id and quantity."""
    order = {"line_items": line_items}
    if email: order["email"] = email
    if financial_status: order["financial_status"] = financial_status
    return make_request("POST", "/orders.json", json={"order": order})

@mcp.tool()
def update_order(order_id: int, note: Optional[str] = None, email: Optional[str] = None, tags: Optional[str] = None) -> Any:
    """Update an existing order."""
    order = {"id": order_id}
    if note: order["note"] = note
    if email: order["email"] = email
    if tags: order["tags"] = tags
    return make_request("PUT", f"/orders/{order_id}.json", json={"order": order})

@mcp.tool()
def delete_order(order_id: int) -> Any:
    """Delete an order."""
    return make_request("DELETE", f"/orders/{order_id}.json")

# Draft Orders
@mcp.tool()
def get_draft_orders(limit: int = 50) -> Any:
    """Retrieve a list of draft orders."""
    return make_request("GET", "/draft_orders.json", params={"limit": limit})

@mcp.tool()
def create_draft_order(line_items: List[Dict[str, Any]]) -> Any:
    """Create a new draft order."""
    return make_request("POST", "/draft_orders.json", json={"draft_order": {"line_items": line_items}})

# Refunds
@mcp.tool()
def calculate_refund(order_id: int, refund_line_items: List[Dict[str, Any]]) -> Any:
    """Calculate a refund."""
    return make_request("POST", f"/orders/{order_id}/refunds/calculate.json", json={"refund": {"refund_line_items": refund_line_items}})

@mcp.tool()
def create_refund(order_id: int, refund_line_items: List[Dict[str, Any]], notify: bool = False) -> Any:
    """Create a refund."""
    return make_request("POST", f"/orders/{order_id}/refunds.json", json={"refund": {"refund_line_items": refund_line_items, "notify": notify}})

# Transactions
@mcp.tool()
def get_transactions(order_id: int) -> Any:
    """Retrieve a list of transactions for an order."""
    return make_request("GET", f"/orders/{order_id}/transactions.json")

@mcp.tool()
def create_transaction(order_id: int, kind: str, amount: str) -> Any:
    """Create a transaction for an order."""
    return make_request("POST", f"/orders/{order_id}/transactions.json", json={"transaction": {"kind": kind, "amount": amount}})

# Fulfillment
@mcp.tool()
def get_fulfillment_orders(order_id: int) -> Any:
    """Retrieve fulfillment orders for an order."""
    return make_request("GET", f"/orders/{order_id}/fulfillment_orders.json")

@mcp.tool()
def create_fulfillment(fulfillment_order_id: int, message: Optional[str] = None) -> Any:
    """Create a fulfillment for a fulfillment order."""
    data = {"fulfillment": {"line_items_by_fulfillment_order": [{"fulfillment_order_id": fulfillment_order_id}]}}
    if message: data["fulfillment"]["message"] = message
    return make_request("POST", "/fulfillments.json", json=data)

# Customers
@mcp.tool()
def get_customers(limit: int = 50) -> Any:
    """Retrieve a list of customers."""
    return make_request("GET", "/customers.json", params={"limit": limit})

@mcp.tool()
def get_customer(customer_id: int) -> Any:
    """Retrieve a single customer by ID."""
    return make_request("GET", f"/customers/{customer_id}.json")

@mcp.tool()
def create_customer(first_name: str, last_name: str, email: str, phone: Optional[str] = None) -> Any:
    """Create a new customer."""
    customer = {"first_name": first_name, "last_name": last_name, "email": email}
    if phone: customer["phone"] = phone
    return make_request("POST", "/customers.json", json={"customer": customer})

@mcp.tool()
def update_customer(customer_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None, email: Optional[str] = None, phone: Optional[str] = None) -> Any:
    """Update an existing customer."""
    customer = {"id": customer_id}
    if first_name: customer["first_name"] = first_name
    if last_name: customer["last_name"] = last_name
    if email: customer["email"] = email
    if phone: customer["phone"] = phone
    return make_request("PUT", f"/customers/{customer_id}.json", json={"customer": customer})

@mcp.tool()
def delete_customer(customer_id: int) -> Any:
    """Delete a customer."""
    return make_request("DELETE", f"/customers/{customer_id}.json")

# Inventory
@mcp.tool()
def get_inventory_items(ids: str) -> Any:
    """Retrieve a list of inventory items."""
    return make_request("GET", "/inventory_items.json", params={"ids": ids})

@mcp.tool()
def get_inventory_levels(inventory_item_ids: str, location_ids: Optional[str] = None) -> Any:
    """Retrieve a list of inventory levels. inventory_item_ids is a comma-separated list of IDs."""
    params = {"inventory_item_ids": inventory_item_ids}
    if location_ids: params["location_ids"] = location_ids
    return make_request("GET", "/inventory_levels.json", params=params)

@mcp.tool()
def set_inventory_level(location_id: int, inventory_item_id: int, available: int) -> Any:
    """Set the inventory level for an inventory item at a location."""
    data = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available": available
    }
    return make_request("POST", "/inventory_levels/set.json", json=data)

# Locations
@mcp.tool()
def get_locations() -> Any:
    """Retrieve a list of locations."""
    return make_request("GET", "/locations.json")

# Collections
@mcp.tool()
def get_custom_collections(limit: int = 50) -> Any:
    """Retrieve a list of custom collections."""
    return make_request("GET", "/custom_collections.json", params={"limit": limit})

@mcp.tool()
def get_smart_collections(limit: int = 50) -> Any:
    """Retrieve a list of smart collections."""
    return make_request("GET", "/smart_collections.json", params={"limit": limit})

# Discounts
@mcp.tool()
def get_price_rules() -> Any:
    """Retrieve a list of price rules."""
    return make_request("GET", "/price_rules.json")

@mcp.tool()
def create_price_rule(title: str, target_type: str, target_selection: str, allocation_method: str, value_type: str, value: str, customer_selection: str, starts_at: str) -> Any:
    """Create a price rule."""
    rule = {
        "title": title,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "value_type": value_type,
        "value": value,
        "customer_selection": customer_selection,
        "starts_at": starts_at
    }
    return make_request("POST", "/price_rules.json", json={"price_rule": rule})

@mcp.tool()
def get_discount_codes(price_rule_id: int) -> Any:
    """Retrieve a list of discount codes for a price rule."""
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json")

@mcp.tool()
def create_discount_code(price_rule_id: int, code: str) -> Any:
    """Create a discount code for a price rule."""
    return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json={"discount_code": {"code": code}})

# Webhooks
@mcp.tool()
def get_webhooks() -> Any:
    """Retrieve a list of webhooks."""
    return make_request("GET", "/webhooks.json")

@mcp.tool()
def create_webhook(topic: str, address: str, format: str = "json") -> Any:
    """Create a webhook."""
    return make_request("POST", "/webhooks.json", json={"webhook": {"topic": topic, "address": address, "format": format}})

# Metafields
@mcp.tool()
def get_metafields(metafield_id: Optional[int] = None) -> Any:
    """Retrieve a list of metafields or a specific metafield."""
    if metafield_id:
        return make_request("GET", f"/metafields/{metafield_id}.json")
    return make_request("GET", "/metafields.json")

@mcp.tool()
def create_metafield(namespace: str, key: str, value: str, type: str) -> Any:
    """Create a metafield."""
    metafield = {"namespace": namespace, "key": key, "value": value, "type": type}
    return make_request("POST", "/metafields.json", json={"metafield": metafield})

if __name__ == "__main__":
    mcp.run()
