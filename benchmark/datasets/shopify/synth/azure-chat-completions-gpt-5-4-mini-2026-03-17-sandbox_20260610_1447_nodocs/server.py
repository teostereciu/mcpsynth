import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

API_VERSION = "2026-01"
BASE_URL = f"https://{{store}}/admin/api/{API_VERSION}"

mcp = FastMCP("shopify-admin-rest")


def _headers() -> Dict[str, str]:
    token = os.getenv("SHOPIFY_ACCESS_TOKEN")
    if not token:
        return {}
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def _store_url() -> str:
    store = os.getenv("SHOPIFY_STORE_URL")
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    return f"https://{store}/admin/api/{API_VERSION}"


def _request(method: str, path: str, params: Dict[str, Any] | None = None, json_body: Dict[str, Any] | None = None):
    try:
        resp = requests.request(
            method,
            _store_url() + path,
            headers=_headers(),
            params=params,
            json=json_body,
            timeout=30,
        )
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text, "status": resp.status_code}
        if not resp.text:
            return {}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": sorted([name for name in globals() if name.startswith(("get_", "list_", "create_", "update_", "delete_"))])}


@mcp.tool()
def get_shop() -> Dict[str, Any]:
    return _request("GET", "/shop.json")


@mcp.tool()
def list_products(limit: int = 50) -> Dict[str, Any]:
    return _request("GET", "/products.json", params={"limit": limit})


@mcp.tool()
def get_product(product_id: int) -> Dict[str, Any]:
    return _request("GET", f"/products/{product_id}.json")


@mcp.tool()
def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    return _request("POST", "/products.json", json_body={"product": product})


@mcp.tool()
def update_product(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    return _request("PUT", f"/products/{product_id}.json", json_body={"product": product})


@mcp.tool()
def delete_product(product_id: int) -> Dict[str, Any]:
    return _request("DELETE", f"/products/{product_id}.json")


@mcp.tool()
def list_customers(limit: int = 50) -> Dict[str, Any]:
    return _request("GET", "/customers.json", params={"limit": limit})


@mcp.tool()
def get_customer(customer_id: int) -> Dict[str, Any]:
    return _request("GET", f"/customers/{customer_id}.json")


@mcp.tool()
def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    return _request("POST", "/customers.json", json_body={"customer": customer})


@mcp.tool()
def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    return _request("PUT", f"/customers/{customer_id}.json", json_body={"customer": customer})


@mcp.tool()
def delete_customer(customer_id: int) -> Dict[str, Any]:
    return _request("DELETE", f"/customers/{customer_id}.json")


@mcp.tool()
def list_orders(limit: int = 50) -> Dict[str, Any]:
    return _request("GET", "/orders.json", params={"limit": limit})


@mcp.tool()
def get_order(order_id: int) -> Dict[str, Any]:
    return _request("GET", f"/orders/{order_id}.json")


@mcp.tool()
def create_order(order: Dict[str, Any]) -> Dict[str, Any]:
    return _request("POST", "/orders.json", json_body={"order": order})


@mcp.tool()
def update_order(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    return _request("PUT", f"/orders/{order_id}.json", json_body={"order": order})


@mcp.tool()
def delete_order(order_id: int) -> Dict[str, Any]:
    return _request("DELETE", f"/orders/{order_id}.json")


if __name__ == "__main__":
    mcp.run()
