import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("shopify-admin-rest")
BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"
HEADERS = {
    "X-Shopify-Access-Token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def _request(method: str, path: str, params: Dict[str, Any] | None = None, body: Dict[str, Any] | None = None):
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=HEADERS, params=params, json=body, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        return resp.json() if resp.text else {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": sorted([n for n in globals() if n.startswith(("list_", "get_", "create_", "update_", "delete_", "cancel_", "close_", "open_"))])}


@mcp.tool()
def list_products(limit: int | None = None, ids: str | None = None): return _request("GET", "/products.json", {k: v for k, v in {"limit": limit, "ids": ids}.items() if v is not None})
@mcp.tool()
def get_product(product_id: int): return _request("GET", f"/products/{product_id}.json")
@mcp.tool()
def create_product(product: Dict[str, Any]): return _request("POST", "/products.json", body={"product": product})
@mcp.tool()
def update_product(product_id: int, product: Dict[str, Any]): return _request("PUT", f"/products/{product_id}.json", body={"product": product})
@mcp.tool()
def delete_product(product_id: int): return _request("DELETE", f"/products/{product_id}.json")

@mcp.tool()
def list_orders(status: str | None = None, limit: int | None = None): return _request("GET", "/orders.json", {k: v for k, v in {"status": status, "limit": limit}.items() if v is not None})
@mcp.tool()
def get_order(order_id: int): return _request("GET", f"/orders/{order_id}.json")
@mcp.tool()
def create_order(order: Dict[str, Any]): return _request("POST", "/orders.json", body={"order": order})
@mcp.tool()
def update_order(order_id: int, order: Dict[str, Any]): return _request("PUT", f"/orders/{order_id}.json", body={"order": order})
@mcp.tool()
def delete_order(order_id: int): return _request("DELETE", f"/orders/{order_id}.json")
@mcp.tool()
def cancel_order(order_id: int, body: Dict[str, Any] | None = None): return _request("POST", f"/orders/{order_id}/cancel.json", body=body or {})
@mcp.tool()
def close_order(order_id: int): return _request("POST", f"/orders/{order_id}/close.json")
@mcp.tool()
def open_order(order_id: int): return _request("POST", f"/orders/{order_id}/open.json")

@mcp.tool()
def list_customers(limit: int | None = None): return _request("GET", "/customers.json", {k: v for k, v in {"limit": limit}.items() if v is not None})
@mcp.tool()
def get_customer(customer_id: int): return _request("GET", f"/customers/{customer_id}.json")
@mcp.tool()
def create_customer(customer: Dict[str, Any]): return _request("POST", "/customers.json", body={"customer": customer})
@mcp.tool()
def update_customer(customer_id: int, customer: Dict[str, Any]): return _request("PUT", f"/customers/{customer_id}.json", body={"customer": customer})
@mcp.tool()
def delete_customer(customer_id: int): return _request("DELETE", f"/customers/{customer_id}.json")

@mcp.tool()
def list_inventory_items(ids: str | None = None): return _request("GET", "/inventory_items.json", {k: v for k, v in {"ids": ids}.items() if v is not None})
@mcp.tool()
def get_inventory_item(inventory_item_id: int): return _request("GET", f"/inventory_items/{inventory_item_id}.json")
@mcp.tool()
def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]): return _request("PUT", f"/inventory_items/{inventory_item_id}.json", body={"inventory_item": inventory_item})

@mcp.tool()
def list_price_rules(limit: int | None = None): return _request("GET", "/price_rules.json", {k: v for k, v in {"limit": limit}.items() if v is not None})
@mcp.tool()
def get_price_rule(price_rule_id: int): return _request("GET", f"/price_rules/{price_rule_id}.json")
@mcp.tool()
def create_price_rule(price_rule: Dict[str, Any]): return _request("POST", "/price_rules.json", body={"price_rule": price_rule})
@mcp.tool()
def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]): return _request("PUT", f"/price_rules/{price_rule_id}.json", body={"price_rule": price_rule})
@mcp.tool()
def delete_price_rule(price_rule_id: int): return _request("DELETE", f"/price_rules/{price_rule_id}.json")

@mcp.tool()
def list_webhooks(limit: int | None = None): return _request("GET", "/webhooks.json", {k: v for k, v in {"limit": limit}.items() if v is not None})
@mcp.tool()
def get_webhook(webhook_id: int): return _request("GET", f"/webhooks/{webhook_id}.json")
@mcp.tool()
def create_webhook(webhook: Dict[str, Any]): return _request("POST", "/webhooks.json", body={"webhook": webhook})
@mcp.tool()
def update_webhook(webhook_id: int, webhook: Dict[str, Any]): return _request("PUT", f"/webhooks/{webhook_id}.json", body={"webhook": webhook})
@mcp.tool()
def delete_webhook(webhook_id: int): return _request("DELETE", f"/webhooks/{webhook_id}.json")


if __name__ == "__main__":
    mcp.run()
