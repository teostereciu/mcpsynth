import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

API_VERSION = "2026-01"
BASE_URL = f"https://{{store}}/admin/api/{API_VERSION}"

mcp = FastMCP("shopify-admin-rest")


def _shopify_request(method: str, path: str, params: Optional[dict] = None, json_body: Optional[dict] = None):
    store = os.environ.get("SHOPIFY_STORE_URL")
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    if not store or not token:
        return {"error": "Missing SHOPIFY_STORE_URL or SHOPIFY_ACCESS_TOKEN"}
    url = f"https://{store}/admin/api/{API_VERSION}{path}"
    headers = {"X-Shopify-Access-Token": token, "Content-Type": "application/json"}
    try:
        resp = requests.request(method, url, headers=headers, params=params, json=json_body, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        try:
            return resp.json()
        except Exception:
            return {"result": resp.text}
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": [t.name for t in mcp._tools.values()]}


@mcp.tool()
def get_product(product_id: int):
    return _shopify_request("GET", f"/products/{product_id}.json")


@mcp.tool()
def list_products(ids: Optional[str] = None):
    params = {"ids": ids} if ids else None
    return _shopify_request("GET", "/products.json", params=params)


@mcp.tool()
def create_product(product: dict):
    return _shopify_request("POST", "/products.json", json_body={"product": product})


@mcp.tool()
def update_product(product_id: int, product: dict):
    return _shopify_request("PUT", f"/products/{product_id}.json", json_body={"product": product})


@mcp.tool()
def delete_product(product_id: int):
    return _shopify_request("DELETE", f"/products/{product_id}.json")


@mcp.tool()
def get_order(order_id: int):
    return _shopify_request("GET", f"/orders/{order_id}.json")


@mcp.tool()
def list_orders(status: Optional[str] = None):
    params = {"status": status} if status else None
    return _shopify_request("GET", "/orders.json", params=params)


@mcp.tool()
def create_order(order: dict):
    return _shopify_request("POST", "/orders.json", json_body={"order": order})


@mcp.tool()
def update_order(order_id: int, order: dict):
    return _shopify_request("PUT", f"/orders/{order_id}.json", json_body={"order": order})


@mcp.tool()
def cancel_order(order_id: int):
    return _shopify_request("POST", f"/orders/{order_id}/cancel.json")


@mcp.tool()
def get_customer(customer_id: int):
    return _shopify_request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def list_customers(ids: Optional[str] = None):
    params = {"ids": ids} if ids else None
    return _shopify_request("GET", "/customers.json", params=params)


@mcp.tool()
def create_customer(customer: dict):
    return _shopify_request("POST", "/customers.json", json_body={"customer": customer})


@mcp.tool()
def update_customer(customer_id: int, customer: dict):
    return _shopify_request("PUT", f"/customers/{customer_id}.json", json_body={"customer": customer})


@mcp.tool()
def get_inventory_level(inventory_item_id: int, location_id: int):
    return _shopify_request("GET", "/inventory_levels.json", params={"inventory_item_id": inventory_item_id, "location_id": location_id})


@mcp.tool()
def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int):
    return _shopify_request("POST", "/inventory_levels/adjust.json", json_body={"location_id": location_id, "inventory_item_id": inventory_item_id, "available_adjustment": available_adjustment})


@mcp.tool()
def set_inventory_level(location_id: int, inventory_item_id: int, available: int):
    return _shopify_request("POST", "/inventory_levels/set.json", json_body={"location_id": location_id, "inventory_item_id": inventory_item_id, "available": available})


@mcp.tool()
def get_draft_order(draft_order_id: int):
    return _shopify_request("GET", f"/draft_orders/{draft_order_id}.json")


@mcp.tool()
def list_draft_orders():
    return _shopify_request("GET", "/draft_orders.json")


@mcp.tool()
def create_draft_order(draft_order: dict):
    return _shopify_request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


@mcp.tool()
def complete_draft_order(draft_order_id: int):
    return _shopify_request("PUT", f"/draft_orders/{draft_order_id}/complete.json")


@mcp.tool()
def get_webhook(webhook_id: int):
    return _shopify_request("GET", f"/webhooks/{webhook_id}.json")


@mcp.tool()
def list_webhooks():
    return _shopify_request("GET", "/webhooks.json")


@mcp.tool()
def create_webhook(webhook: dict):
    return _shopify_request("POST", "/webhooks.json", json_body={"webhook": webhook})


@mcp.tool()
def update_webhook(webhook_id: int, webhook: dict):
    return _shopify_request("PUT", f"/webhooks/{webhook_id}.json", json_body={"webhook": webhook})


@mcp.tool()
def delete_webhook(webhook_id: int):
    return _shopify_request("DELETE", f"/webhooks/{webhook_id}.json")


if __name__ == "__main__":
    mcp.run()
