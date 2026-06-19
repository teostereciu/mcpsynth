import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

API_VERSION = "2026-01"
BASE_URL = f"https://{{store}}/admin/api/{API_VERSION}"

mcp = FastMCP("shopify-admin-rest")


def _headers() -> Dict[str, str]:
    return {
        "X-Shopify-Access-Token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def _request(method: str, path: str, params: Dict[str, Any] | None = None, json: Dict[str, Any] | None = None):
    store = os.environ.get("SHOPIFY_STORE_URL")
    if not store:
        return {"error": "SHOPIFY_STORE_URL is not set"}
    if not os.environ.get("SHOPIFY_ACCESS_TOKEN"):
        return {"error": "SHOPIFY_ACCESS_TOKEN is not set"}
    url = BASE_URL.format(store=store) + path
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.text:
            return resp.json()
        return {}
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": sorted([name for name in globals() if name.startswith(("list_", "get_", "create_", "update_", "delete_", "cancel_", "close_", "open_", "hold_", "release_", "adjust_", "connect_", "set_", "lookup_", "complete_")])}


@mcp.tool()
def list_products(limit: int = 50, page_info: str | None = None):
    params = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    return _request("GET", "/products.json", params=params)


@mcp.tool()
def get_product(product_id: int):
    return _request("GET", f"/products/{product_id}.json")


@mcp.tool()
def create_product(product: Dict[str, Any]):
    return _request("POST", "/products.json", json={"product": product})


@mcp.tool()
def update_product(product_id: int, product: Dict[str, Any]):
    return _request("PUT", f"/products/{product_id}.json", json={"product": product})


@mcp.tool()
def delete_product(product_id: int):
    return _request("DELETE", f"/products/{product_id}.json")


@mcp.tool()
def list_customers(limit: int = 50, page_info: str | None = None):
    params = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    return _request("GET", "/customers.json", params=params)


@mcp.tool()
def get_customer(customer_id: int):
    return _request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def create_customer(customer: Dict[str, Any]):
    return _request("POST", "/customers.json", json={"customer": customer})


@mcp.tool()
def update_customer(customer_id: int, customer: Dict[str, Any]):
    return _request("PUT", f"/customers/{customer_id}.json", json={"customer": customer})


@mcp.tool()
def list_orders(limit: int = 50, status: str | None = None):
    params = {"limit": limit}
    if status:
        params["status"] = status
    return _request("GET", "/orders.json", params=params)


@mcp.tool()
def get_order(order_id: int):
    return _request("GET", f"/orders/{order_id}.json")


@mcp.tool()
def cancel_order(order_id: int, body: Dict[str, Any] | None = None):
    return _request("POST", f"/orders/{order_id}/cancel.json", json=body or {})


@mcp.tool()
def close_order(order_id: int):
    return _request("POST", f"/orders/{order_id}/close.json")


@mcp.tool()
def open_order(order_id: int):
    return _request("POST", f"/orders/{order_id}/open.json")


if __name__ == "__main__":
    mcp.run()
