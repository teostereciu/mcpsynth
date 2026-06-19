"""
Shopify Admin REST API MCP Server

This server exposes tools for interacting with Shopify Admin REST API (2026-01).
Authentication uses SHOPIFY_ACCESS_TOKEN and SHOPIFY_STORE_URL environment variables.
"""

import os
import json
from typing import Any, Optional
import requests
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="shopify")

# Base URL for Shopify Admin API
BASE_URL = "https://{store_url}/admin/api/2026-01".format(
    store_url=os.getenv("SHOPIFY_STORE_URL", "")
)


def _make_request(method: str, path: str, params: Optional[dict] = None, json_body: Optional[dict] = None) -> dict:
    """Make a request to the Shopify Admin REST API."""
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": os.getenv("SHOPIFY_ACCESS_TOKEN", ""),
    }
    url = f"{BASE_URL}{path}"

    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=json_body,
            timeout=30,
        )

        if response.status_code >= 400:
            error_detail = response.text.strip()
            return {"error": f"API error {response.status_code}: {error_detail}"}

        try:
            return response.json()
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON response"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# =============================================================================
# PRODUCTS
# =============================================================================

@mcp.tool()
def get_product(product_id: int) -> dict:
    """
    Retrieve a single product by ID.
    GET /admin/api/2026-01/products/{product_id}.json
    """
    return _make_request("GET", f"/products/{product_id}.json")


@mcp.tool()
def list_products(limit: int = 50, page_info: Optional[str] = None, product_type: Optional[str] = None) -> dict:
    """
    List products. Supports pagination via page_info and filtering by product_type.
    GET /admin/api/2026-01/products.json
    """
    params = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    if product_type:
        params["product_type"] = product_type
    return _make_request("GET", "/products.json", params=params)


@mcp.tool()
def create_product(
    title: str,
    body_html: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    tags: Optional[str] = None,
    variants: Optional[list] = None,
    images: Optional[list] = None,
) -> dict:
    """
    Create a new product.
    POST /admin/api/2026-01/products.json
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

    return _make_request("POST", "/products.json", json_body={"product": product_data})


@mcp.tool()
def update_product(product_id: int, **kwargs) -> dict:
    """
    Update an existing product. Accepts any updatable product fields as kwargs.
    PUT /admin/api/2026-01/products/{product_id}.json
    """
    return _make_request("PUT", f"/products/{product_id}.json", json_body={"product": kwargs})


@mcp.tool()
def delete_product(product_id: int) -> dict:
    """
    Delete a product.
    DELETE /admin/api/2026-01/products/{product_id}.json
    """
    return _make_request("DELETE", f"/products/{product_id}.json")


# =============================================================================
# PRODUCT VARIANTS
# =============================================================================

@mcp.tool()
def get_variant(variant_id: int) -> dict:
    """
    Retrieve a single variant by ID.
    GET /admin/api/2026-01/variants/{variant_id}.json
    """
    return _make_request("GET", f"/variants/{variant_id}.json")


@mcp.tool()
def list_variants(product_id: int, limit: int = 50) -> dict:
    """
    List variants for a product.
    GET /admin/api/2026-01/products/{product_id}/variants.json
    """
    return _make_request("GET", f"/products/{product_id}/variants.json", params={"limit": limit})


@mcp.tool()
def update_variant(variant_id: int, **kwargs) -> dict:
    """
    Update a variant. Accepts any updatable variant fields as kwargs.
    PUT /admin/api/2026-01/variants/{variant_id}.json
    """
    return _make_request("PUT", f"/variants/{variant_id}.json", json_body={"variant": kwargs})


# =============================================================================
# PRODUCT IMAGES
# =============================================================================

@mcp.tool()
def get_product_image(product_id: int, image_id: int) -> dict:
    """
    Retrieve a product image by ID.
    GET /admin/api/2026-01/products/{product_id}/images/{image_id}.json
    """
    return _make_request("GET", f"/products/{product_id}/images/{image_id}.json")


@mcp.tool()
def list_product_images(product_id: int, limit: int = 50) -> dict:
    """
    List images for a product.
    GET /admin/api/2026-01/products/{product_id}/images.json
    """
    return _make_request("GET", f"/products/{product_id}/images.json", params={"limit": limit})


@mcp.tool()
def create_product_image(product_id: int, src: str, alt: Optional[str] = None) -> dict:
    """
    Create a new image for a product.
    POST /admin/api/2026-01/products/{product_id}/images.json
    """
    image_data = {"src": src}
    if alt:
        image_data["alt"] = alt
    return _make_request("POST", f"/products/{product_id}/images.json", json_body={"image": image_data})


# =============================================================================
# PRODUCT COLLECTIONS
# =============================================================================

@mcp.tool()
def get_collection(collection_id: int) -> dict:
    """
    Retrieve a custom collection by ID.
    GET /admin/api/2026-01/custom_collections/{collection_id}.json
    """
    return _make_request("GET", f"/custom_collections/{collection_id}.json")


@mcp.tool()
def list_collections(limit: int = 50) -> dict:
    """
    List custom collections.
    GET /admin/api/2026-01/custom_collections.json
    """
    return _make_request("GET", "/custom_collections.json", params={"limit": limit})


@mcp.tool()
def create_collection(title: str, body_html: Optional[str] = None, sort_order: Optional[str] = None, template_suffix: Optional[str] = None) -> dict:
    """
    Create a custom collection.
    POST /admin/api/2026-01/custom_collections.json
    """
    data = {"title": title}
    if body_html:
        data["body_html"] = body_html
    if sort_order:
        data["sort_order"] = sort_order
    if template_suffix:
        data["template_suffix"] = template_suffix
    return _make_request("POST", "/custom_collections.json", json_body={"custom_collection": data})


# =============================================================================
# ORDERS
# =============================================================================

@mcp.tool()
def get_order(order_id: int, fields: Optional[str] = None) -> dict:
    """
    Retrieve an order by ID.
    GET /admin/api/2026-01/orders/{order_id}.json
    """
    params = {}
    if fields:
        params["fields"] = fields
    return _make_request("GET", f"/orders/{order_id}.json", params=params)


@mcp.tool()
def list_orders(
    status: str = "open",
    limit: int = 50,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
) -> dict:
    """
    List orders.
    GET /admin/api/2026-01/orders.json
    """
    params = {"status": status, "limit": limit}
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    return _make_request("GET", "/orders.json", params=params)


@mcp.tool()
def create_order(order: dict) -> dict:
    """
    Create a new order.
    POST /admin/api/2026-01/orders.json
    """
    return _make_request("POST", "/orders.json", json_body={"order": order})


# =============================================================================
# DRAFT ORDERS
# =============================================================================

@mcp.tool()
def get_draft_order(draft_order_id: int) -> dict:
    """
    Retrieve a draft order by ID.
    GET /admin/api/2026-01/draft_orders/{draft_order_id}.json
    """
    return _make_request("GET", f"/draft_orders/{draft_order_id}.json")


@mcp.tool()
def list_draft_orders(limit: int = 50) -> dict:
    """
    List draft orders.
    GET /admin/api/2026-01/draft_orders.json
    """
    return _make_request("GET", "/draft_orders.json", params={"limit": limit})


@mcp.tool()
def create_draft_order(order: dict) -> dict:
    """
    Create a new draft order.
    POST /admin/api/2026-01/draft_orders.json
    """
    return _make_request("POST", "/draft_orders.json", json_body={"draft_order": order})


@mcp.tool()
def update_draft_order(draft_order_id: int, order: dict) -> dict:
    """
    Update a draft order.
    PUT /admin/api/2026-01/draft_orders/{draft_order_id}.json
    """
    return _make_request("PUT", f"/draft_orders/{draft_order_id}.json", json_body={"draft_order": order})


# =============================================================================
# REFUNDS
# =============================================================================

@mcp.tool()
def create_refund(order_id: int, refund: dict) -> dict:
    """
    Create a refund for an order.
    POST /admin/api/2026-01/orders/{order_id}/refunds.json
    """
    return _make_request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


# =============================================================================
# TRANSACTIONS
# =============================================================================

@mcp.tool()
def list_transactions(order_id: int, limit: int = 50) -> dict:
    """
    List transactions for an order.
    GET /admin/api/2026-01/orders/{order_id}/transactions.json
    """
    return _make_request("GET", f"/orders/{order_id}/transactions.json", params={"limit": limit})


@mcp.tool()
def create_transaction(order_id: int, transaction: dict) -> dict:
    """
    Create a transaction for an order (e.g., capture, void, refund).
    POST /admin/api/2026-01/orders/{order_id}/transactions.json
    """
    return _make_request("POST", f"/orders/{order_id}/transactions.json", json_body={"transaction": transaction})


# =============================================================================
# CUSTOMERS
# =============================================================================

@mcp.tool()
def get_customer(customer_id: int) -> dict:
    """
    Retrieve a customer by ID.
    GET /admin/api/2026-01/customers/{customer_id}.json
    """
    return _make_request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def list_customers(
    limit: int = 50,
    email: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
) -> dict:
    """
    List customers. Optionally filter by email or date range.
    GET /admin/api/2026-01/customers.json
    """
    params = {"limit": limit}
    if email:
        params["email"] = email
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    return _make_request("GET", "/customers.json", params=params)


@mcp.tool()
def create_customer(customer: dict) -> dict:
    """
    Create a new customer.
    POST /admin/api/2026-01/customers.json
    """
    return _make_request("POST", "/customers.json", json_body={"customer": customer})


@mcp.tool()
def update_customer(customer_id: int, customer: dict) -> dict:
    """
    Update a customer.
    PUT /admin/api/2026-01/customers/{customer_id}.json
    """
    return _make_request("PUT", f"/customers/{customer_id}.json", json_body={"customer": customer})


# =============================================================================
# INVENTORY ITEMS
# =============================================================================

@mcp.tool()
def get_inventory_item(inventory_item_id: int) -> dict:
    """
    Retrieve an inventory item by ID.
    GET /admin/api/2026-01/inventory_items/{inventory_item_id}.json
    """
    return _make_request("GET", f"/inventory_items/{inventory_item_id}.json")


@mcp.tool()
def list_inventory_items(limit: int = 50, cursor: Optional[str] = None) -> dict:
    """
    List inventory items.
    GET /admin/api/2026-01/inventory_items.json
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return _make_request("GET", "/inventory_items.json", params=params)


@mcp.tool()
def update_inventory_item(inventory_item_id: int, cost: Optional[float] = None, tracked: Optional[bool] = None) -> dict:
    """
    Update an inventory item.
    PUT /admin/api/2026-01/inventory_items/{inventory_item_id}.json
    """
    data = {}
    if cost is not None:
        data["cost"] = cost
    if tracked is not None:
        data["tracked"] = tracked
    return _make_request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body={"inventory_item": data})


# =============================================================================
# INVENTORY LEVELS
# =============================================================================

@mcp.tool()
def get_inventory_level(inventory_item_id: int, location_id: int) -> dict:
    """
    Retrieve an inventory level for a specific item and location.
    GET /admin/api/2026-01/inventory_levels.json?inventory_item_id={id}&location_id={id}
    """
    params = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
    }
    return _make_request("GET", "/inventory_levels.json", params=params)


@mcp.tool()
def adjust_inventory_level(location_id: int, inventory_item_id: int, quantity_adjustment: int) -> dict:
    """
    Adjust the inventory level at a specific location.
    POST /admin/api/2026-01/inventory_levels/adjust.json
    """
    data = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "quantity_adjustment": quantity_adjustment,
    }
    return _make_request("POST", "/inventory_levels/adjust.json", json_body=data)


@mcp.tool()
def set_inventory_level(location_id: int, inventory_item_id: int, available: Optional[int] = None, transit: Optional[int] = None) -> dict:
    """
    Set the inventory level for an item at a location.
    POST /admin/api/2026-01/inventory_levels/set.json
    """
    data = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
    }
    if available is not None:
        data["available"] = available
    if transit is not None:
        data["transit"] = transit
    return _make_request("POST", "/inventory_levels/set.json", json_body=data)


# =============================================================================
# FULFILLMENT ORDERS
# =============================================================================

@mcp.tool()
def get_fulfillment_order(fulfillment_order_id: int) -> dict:
    """
    Retrieve a fulfillment order by ID.
    GET /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}.json
    """
    return _make_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


@mcp.tool()
def list_fulfillment_orders(
    fulfillment_order_ids: Optional[str] = None,
    limit: int = 50,
) -> dict:
    """
    List fulfillment orders.
    GET /admin/api/2026-01/fulfillment_orders.json
    """
    params = {"limit": limit}
    if fulfillment_order_ids:
        params["fulfillment_order_ids"] = fulfillment_order_ids
    return _make_request("GET", "/fulfillment_orders.json", params=params)


@mcp.tool()
def cancel_fulfillment_order(fulfillment_order_id: int) -> dict:
    """
    Cancel a fulfillment order.
    POST /admin/api/2026-01/fulfillment_orders/{fulfillment_order_id}/cancel.json
    """
    return _make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


# =============================================================================
# LOCATIONS
# =============================================================================

@mcp.tool()
def get_location(location_id: int) -> dict:
    """
    Retrieve a location by ID.
    GET /admin/api/2026-01/locations/{location_id}.json
    """
    return _make_request("GET", f"/locations/{location_id}.json")


@mcp.tool()
def list_locations(limit: int = 50) -> dict:
    """
    List locations.
    GET /admin/api/2026-01/locations.json
    """
    return _make_request("GET", "/locations.json", params={"limit": limit})


# =============================================================================
# DISCOUNTS - PRICE RULES
# =============================================================================

@mcp.tool()
def get_price_rule(price_rule_id: int) -> dict:
    """
    Retrieve a price rule by ID.
    GET /admin/api/2026-01/price_rules/{price_rule_id}.json
    """
    return _make_request("GET", f"/price_rules/{price_rule_id}.json")


@mcp.tool()
def list_price_rules(limit: int = 50) -> dict:
    """
    List price rules.
    GET /admin/api/2026-01/price_rules.json
    """
    return _make_request("GET", "/price_rules.json", params={"limit": limit})


@mcp.tool()
def create_price_rule(
    title: str,
    target_type: str,
    target_selection: str,
    allocation_method: str,
    value_type: str,
    value: float,
    customer_selection: Optional[str] = None,
    starts_at: Optional[str] = None,
    ends_at: Optional[str] = None,
    once_per_customer: Optional[bool] = None,
    min_quantity_required: Optional[int] = None,
    limit: Optional[int] = None,
    prerequisite_quantity_range: Optional[dict] = None,
    prerequisite_shipping_price_range: Optional[dict] = None,
    prerequisite_to_entitlement_quantity_range: Optional[dict] = None,
) -> dict:
    """
    Create a new price rule (discount).
    POST /admin/api/2026-01/price_rules.json
    """
    data = {
        "title": title,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "value_type": value_type,
        "value": value,
    }
    if customer_selection:
        data["customer_selection"] = customer_selection
    if starts_at:
        data["starts_at"] = starts_at
    if ends_at:
        data["ends_at"] = ends_at
    if once_per_customer is not None:
        data["once_per_customer"] = once_per_customer
    if min_quantity_required is not None:
        data["min_quantity_required"] = min_quantity_required
    if limit is not None:
        data["limit"] = limit
    if prerequisite_quantity_range:
        data["prerequisite_quantity_range"] = prerequisite_quantity_range
    if prerequisite_shipping_price_range:
        data["prerequisite_shipping_price_range"] = prerequisite_shipping_price_range
    if prerequisite_to_entitlement_quantity_range:
        data["prerequisite_to_entitlement_quantity_range"] = prerequisite_to_entitlement_quantity_range

    return _make_request("POST", "/price_rules.json", json_body={"price_rule": data})


@mcp.tool()
def update_price_rule(price_rule_id: int, **kwargs) -> dict:
    """
    Update a price rule.
    PUT /admin/api/2026-01/price_rules/{price_rule_id}.json
    """
    return _make_request("PUT", f"/price_rules/{price_rule_id}.json", json_body={"price_rule": kwargs})


# =============================================================================
# DISCOUNTS - CODES
# =============================================================================

@mcp.tool()
def get_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """
    Retrieve a discount code by ID for a specific price rule.
    GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json
    """
    return _make_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


@mcp.tool()
def list_discount_codes(price_rule_id: int, limit: int = 50) -> dict:
    """
    List discount codes for a price rule.
    GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json
    """
    return _make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params={"limit": limit})


@mcp.tool()
def create_discount_code(price_rule_id: int, code: str) -> dict:
    """
    Create a new discount code for a price rule.
    POST /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json
    """
    return _make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json_body={"discount_code": {"code": code}})


# =============================================================================
# WEBHOOKS
# =============================================================================

@mcp.tool()
def get_webhook(webhook_id: int) -> dict:
    """
    Retrieve a webhook by ID.
    GET /admin/api/2026-01/webhooks/{webhook_id}.json
    """
    return _make_request("GET", f"/webhooks/{webhook_id}.json")


@mcp.tool()
def list_webhooks(limit: int = 50, topic: Optional[str] = None) -> dict:
    """
    List webhooks. Optionally filter by topic.
    GET /admin/api/2026-01/webhooks.json
    """
    params = {"limit": limit}
    if topic:
        params["topic"] = topic
    return _make_request("GET", "/webhooks.json", params=params)


@mcp.tool()
def create_webhook(
    topic: str,
    address: str,
    format: str = "json",
    fields: Optional[str] = None,
    include_fields: Optional[str] = None,
) -> dict:
    """
    Create a new webhook.
    POST /admin/api/2026-01/webhooks.json
    """
    data = {
        "topic": topic,
        "address": address,
        "format": format,
    }
    if fields:
        data["fields"] = fields
    if include_fields:
        data["include_fields"] = include_fields
    return _make_request("POST", "/webhooks.json", json_body={"webhook": data})


@mcp.tool()
def delete_webhook(webhook_id: int) -> dict:
    """
    Delete a webhook.
    DELETE /admin/api/2026-01/webhooks/{webhook_id}.json
    """
    return _make_request("DELETE", f"/webhooks/{webhook_id}.json")


# =============================================================================
# METAFIELDS
# =============================================================================

@mcp.tool()
def get_metafield(metafield_id: int) -> dict:
    """
    Retrieve a metafield by ID.
    GET /admin/api/2026-01/metafields/{metafield_id}.json
    """
    return _make_request("GET", f"/metafields/{metafield_id}.json")


@mcp.tool()
def list_metafields(
    metafieldable_resource: str,
    metafieldable_resource_id: int,
    limit: int = 50,
    key: Optional[str] = None,
    namespace: Optional[str] = None,
) -> dict:
    """
    List metafields for a resource (e.g., product, customer, order).
    GET /admin/api/2026-01/{resource}/{resource_id}/metafields.json
    """
    path = f"/{metafieldable_resource}/{metafieldable_resource_id}/metafields.json"
    params = {"limit": limit}
    if key:
        params["key"] = key
    if namespace:
        params["namespace"] = namespace
    return _make_request("GET", path, params=params)


@mcp.tool()
def create_metafield(
    metafieldable_resource: str,
    metafieldable_resource_id: int,
    namespace: str,
    key: str,
    value: str,
    type: str = "string",
) -> dict:
    """
    Create a metafield for a resource.
    POST /admin/api/2026-01/{resource}/{resource_id}/metafields.json
    """
    path = f"/{metafieldable_resource}/{metafieldable_resource_id}/metafields.json"
    data = {
        "namespace": namespace,
        "key": key,
        "value": value,
        "type": type,
    }
    return _make_request("POST", path, json_body={"metafield": data})


# =============================================================================
# UTILITIES
# =============================================================================

@mcp.tool()
def get_api_usage() -> dict:
    """
    Get current API usage (call count and limit).
    GET /admin/api/2026-01/admin/api_usage.json
    """
    return _make_request("GET", "/admin/api_usage.json")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    mcp.run()
