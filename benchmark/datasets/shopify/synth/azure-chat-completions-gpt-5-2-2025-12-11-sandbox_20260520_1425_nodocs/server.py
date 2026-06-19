import os
import json
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

API_VERSION = "2026-01"


def _env(name: str) -> Optional[str]:
    v = os.getenv(name)
    return v.strip() if isinstance(v, str) and v.strip() else None


def _base_url() -> str:
    store = _env("SHOPIFY_STORE_URL")
    if not store:
        raise RuntimeError("Missing SHOPIFY_STORE_URL")
    store = store.replace("https://", "").replace("http://", "").strip("/")
    return f"https://{store}/admin/api/{API_VERSION}"


def _headers() -> Dict[str, str]:
    token = _env("SHOPIFY_ACCESS_TOKEN")
    if not token:
        raise RuntimeError("Missing SHOPIFY_ACCESS_TOKEN")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def shopify_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    """Low-level request helper.

    Returns JSON-decoded response on success.
    Returns {"error": ..., "status": ..., "details": ...} on expected errors.
    """
    url = _base_url() + path
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json_body, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "details": str(e)}

    content_type = resp.headers.get("Content-Type", "")
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except Exception:
            data = resp.text
    else:
        data = resp.text

    if 200 <= resp.status_code < 300:
        return data

    return {
        "error": "shopify_api_error",
        "status": resp.status_code,
        "details": data,
        "method": method,
        "path": path,
    }


mcp = FastMCP("shopify-admin-rest")

# -------------------- Products --------------------

@mcp.tool()
def list_products(limit: int = 50, page_info: Optional[str] = None, fields: Optional[str] = None, status: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    if fields:
        params["fields"] = fields
    if status:
        params["status"] = status
    return shopify_request("GET", "/products.json", params=params)


@mcp.tool()
def get_product(product_id: int, fields: Optional[str] = None) -> Any:
    params = {"fields": fields} if fields else None
    return shopify_request("GET", f"/products/{product_id}.json", params=params)


@mcp.tool()
def create_product(product: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/products.json", json_body={"product": product})


@mcp.tool()
def update_product(product_id: int, product: Dict[str, Any]) -> Any:
    body = {"product": {**product, "id": product_id}}
    return shopify_request("PUT", f"/products/{product_id}.json", json_body=body)


@mcp.tool()
def delete_product(product_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}.json")


@mcp.tool()
def list_product_variants(product_id: int, limit: int = 50) -> Any:
    return shopify_request("GET", f"/products/{product_id}/variants.json", params={"limit": limit})


@mcp.tool()
def get_variant(variant_id: int) -> Any:
    return shopify_request("GET", f"/variants/{variant_id}.json")


@mcp.tool()
def update_variant(variant_id: int, variant: Dict[str, Any]) -> Any:
    body = {"variant": {**variant, "id": variant_id}}
    return shopify_request("PUT", f"/variants/{variant_id}.json", json_body=body)


@mcp.tool()
def list_product_images(product_id: int, limit: int = 50) -> Any:
    return shopify_request("GET", f"/products/{product_id}/images.json", params={"limit": limit})


@mcp.tool()
def create_product_image(product_id: int, image: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/products/{product_id}/images.json", json_body={"image": image})


@mcp.tool()
def delete_product_image(product_id: int, image_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}/images/{image_id}.json")


# -------------------- Collections --------------------

@mcp.tool()
def list_custom_collections(limit: int = 50) -> Any:
    return shopify_request("GET", "/custom_collections.json", params={"limit": limit})


@mcp.tool()
def list_smart_collections(limit: int = 50) -> Any:
    return shopify_request("GET", "/smart_collections.json", params={"limit": limit})


@mcp.tool()
def create_collect(collection_id: int, product_id: int) -> Any:
    return shopify_request("POST", "/collects.json", json_body={"collect": {"collection_id": collection_id, "product_id": product_id}})


@mcp.tool()
def delete_collect(collect_id: int) -> Any:
    return shopify_request("DELETE", f"/collects/{collect_id}.json")


# -------------------- Orders --------------------

@mcp.tool()
def list_orders(limit: int = 50, status: str = "any", financial_status: Optional[str] = None, fulfillment_status: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit, "status": status}
    if financial_status:
        params["financial_status"] = financial_status
    if fulfillment_status:
        params["fulfillment_status"] = fulfillment_status
    return shopify_request("GET", "/orders.json", params=params)


@mcp.tool()
def get_order(order_id: int, fields: Optional[str] = None) -> Any:
    params = {"fields": fields} if fields else None
    return shopify_request("GET", f"/orders/{order_id}.json", params=params)


@mcp.tool()
def update_order(order_id: int, order: Dict[str, Any]) -> Any:
    body = {"order": {**order, "id": order_id}}
    return shopify_request("PUT", f"/orders/{order_id}.json", json_body=body)


@mcp.tool()
def close_order(order_id: int) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/close.json")


@mcp.tool()
def open_order(order_id: int) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/open.json")


@mcp.tool()
def cancel_order(order_id: int, reason: Optional[str] = None, email: Optional[bool] = None, restock: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {}
    if reason:
        body["reason"] = reason
    if email is not None:
        body["email"] = email
    if restock is not None:
        body["restock"] = restock
    return shopify_request("POST", f"/orders/{order_id}/cancel.json", json_body=body if body else None)


# Draft orders
@mcp.tool()
def list_draft_orders(limit: int = 50) -> Any:
    return shopify_request("GET", "/draft_orders.json", params={"limit": limit})


@mcp.tool()
def create_draft_order(draft_order: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


@mcp.tool()
def complete_draft_order(draft_order_id: int, payment_pending: bool = False) -> Any:
    return shopify_request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params={"payment_pending": str(payment_pending).lower()})


# Refunds / Transactions
@mcp.tool()
def list_transactions(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/transactions.json")


@mcp.tool()
def create_refund(order_id: int, refund: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


# -------------------- Fulfillment --------------------

@mcp.tool()
def list_locations(limit: int = 50) -> Any:
    return shopify_request("GET", "/locations.json", params={"limit": limit})


@mcp.tool()
def list_fulfillment_orders(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/fulfillment_orders.json")


@mcp.tool()
def create_fulfillment(fulfillment: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/fulfillments.json", json_body={"fulfillment": fulfillment})


# -------------------- Customers --------------------

@mcp.tool()
def list_customers(limit: int = 50) -> Any:
    return shopify_request("GET", "/customers.json", params={"limit": limit})


@mcp.tool()
def get_customer(customer_id: int) -> Any:
    return shopify_request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def create_customer(customer: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/customers.json", json_body={"customer": customer})


@mcp.tool()
def update_customer(customer_id: int, customer: Dict[str, Any]) -> Any:
    body = {"customer": {**customer, "id": customer_id}}
    return shopify_request("PUT", f"/customers/{customer_id}.json", json_body=body)


# -------------------- Inventory --------------------

@mcp.tool()
def get_inventory_item(inventory_item_id: int) -> Any:
    return shopify_request("GET", f"/inventory_items/{inventory_item_id}.json")


@mcp.tool()
def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Any:
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return shopify_request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body=body)


@mcp.tool()
def list_inventory_levels(inventory_item_ids: str, location_ids: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"inventory_item_ids": inventory_item_ids}
    if location_ids:
        params["location_ids"] = location_ids
    return shopify_request("GET", "/inventory_levels.json", params=params)


@mcp.tool()
def adjust_inventory_level(inventory_item_id: int, location_id: int, available_adjustment: int) -> Any:
    body = {"inventory_item_id": inventory_item_id, "location_id": location_id, "available_adjustment": available_adjustment}
    return shopify_request("POST", "/inventory_levels/adjust.json", json_body=body)


@mcp.tool()
def set_inventory_level(inventory_item_id: int, location_id: int, available: int) -> Any:
    body = {"inventory_item_id": inventory_item_id, "location_id": location_id, "available": available}
    return shopify_request("POST", "/inventory_levels/set.json", json_body=body)


# -------------------- Discounts --------------------

@mcp.tool()
def list_price_rules(limit: int = 50) -> Any:
    return shopify_request("GET", "/price_rules.json", params={"limit": limit})


@mcp.tool()
def create_price_rule(price_rule: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


@mcp.tool()
def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json_body={"discount_code": discount_code})


# -------------------- Webhooks --------------------

@mcp.tool()
def list_webhooks(limit: int = 50) -> Any:
    return shopify_request("GET", "/webhooks.json", params={"limit": limit})


@mcp.tool()
def create_webhook(webhook: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/webhooks.json", json_body={"webhook": webhook})


@mcp.tool()
def delete_webhook(webhook_id: int) -> Any:
    return shopify_request("DELETE", f"/webhooks/{webhook_id}.json")


# -------------------- Metafields --------------------

@mcp.tool()
def list_metafields(resource: str = "shop", owner_id: Optional[int] = None, limit: int = 50) -> Any:
    """List metafields for a resource.

    resource: one of 'shop', 'products', 'orders', 'customers', etc.
    For shop metafields: GET /metafields.json
    For owner resources: GET /{resource}/{owner_id}/metafields.json
    """
    if resource == "shop":
        return shopify_request("GET", "/metafields.json", params={"limit": limit})
    if not owner_id:
        return {"error": "owner_id_required", "details": "owner_id is required when resource != 'shop'"}
    return shopify_request("GET", f"/{resource}/{owner_id}/metafields.json", params={"limit": limit})


@mcp.tool()
def create_metafield(resource: str, owner_id: int, metafield: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/{resource}/{owner_id}/metafields.json", json_body={"metafield": metafield})


@mcp.tool()
def update_metafield(metafield_id: int, metafield: Dict[str, Any]) -> Any:
    body = {"metafield": {**metafield, "id": metafield_id}}
    return shopify_request("PUT", f"/metafields/{metafield_id}.json", json_body=body)


@mcp.tool()
def delete_metafield(metafield_id: int) -> Any:
    return shopify_request("DELETE", f"/metafields/{metafield_id}.json")


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
