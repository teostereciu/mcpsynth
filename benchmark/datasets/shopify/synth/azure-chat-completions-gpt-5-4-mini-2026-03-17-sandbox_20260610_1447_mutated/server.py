import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("shopify-admin-rest")
BASE_URL = "https://{store}/admin/api/2026-01"
TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN", "")
STORE = os.getenv("SHOPIFY_STORE_URL", "")
HEADERS = {
    "X-Shopify-Access-Token": TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def _request(method: str, path: str, params: Dict[str, Any] | None = None, json_body: Dict[str, Any] | None = None):
    if not STORE or not TOKEN:
        return {"error": "Missing SHOPIFY_ACCESS_TOKEN or SHOPIFY_STORE_URL"}
    url = BASE_URL.format(store=STORE) + path
    try:
        resp = requests.request(method, url, headers=HEADERS, params=params, json=json_body, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if not resp.text:
            return {}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> list[dict[str, Any]]:
    return [
        {"name": name, "description": fn.__doc__ or ""}
        for name, fn in mcp._tools.items()
    ]


@mcp.tool()
def get_product(product_id: int) -> Any:
    """Retrieve a single product."""
    return _request("GET", f"/products/{product_id}.json")


@mcp.tool()
def list_products(ids: str | None = None) -> Any:
    """Retrieve a list of products."""
    params = {"ids": ids} if ids else None
    return _request("GET", "/products.json", params=params)


@mcp.tool()
def create_product(product: Dict[str, Any]) -> Any:
    """Create a new product."""
    return _request("POST", "/products.json", json_body={"product": product})


@mcp.tool()
def update_product(product_id: int, product: Dict[str, Any]) -> Any:
    """Update a product."""
    return _request("PUT", f"/products/{product_id}.json", json_body={"product": product})


@mcp.tool()
def delete_product(product_id: int) -> Any:
    """Delete a product."""
    return _request("DELETE", f"/products/{product_id}.json")


if __name__ == "__main__":
    mcp.run()
