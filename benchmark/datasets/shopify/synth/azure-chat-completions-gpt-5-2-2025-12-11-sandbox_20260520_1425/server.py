import os
import re
import json
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

DEFAULT_API_VERSION = os.getenv("SHOPIFY_API_VERSION", "2026-01")


def _require_env(name: str) -> str:
    v = os.getenv(name)
    if not v:
        raise ValueError(
            f"Missing required environment variable {name}. "
            f"Set it before starting the server."
        )
    return v


def _normalize_shop_domain(shop: str) -> str:
    shop = shop.strip()
    shop = re.sub(r"^https?://", "", shop)
    shop = shop.rstrip("/")
    if shop.endswith(".myshopify.com"):
        return shop
    # allow passing just the subdomain
    if "." not in shop:
        return f"{shop}.myshopify.com"
    return shop


class ShopifyAdminClient:
    def __init__(self, shop: str, access_token: str, api_version: str = DEFAULT_API_VERSION, timeout_s: float = 60.0):
        self.shop = _normalize_shop_domain(shop)
        self.access_token = access_token
        self.api_version = api_version
        self.base_url = f"https://{self.shop}/admin/api/{self.api_version}"
        self._client = httpx.Client(timeout=timeout_s, headers={
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def close(self):
        self._client.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        if not path.startswith("/"):
            path = "/" + path
        url = self.base_url + path
        headers = dict(self._client.headers)
        if extra_headers:
            headers.update(extra_headers)

        resp = self._client.request(method.upper(), url, params=query, json=body, headers=headers)

        # Shopify pagination uses Link header
        link = resp.headers.get("Link")
        retry_after = resp.headers.get("Retry-After")
        location = resp.headers.get("Location")

        content_type = resp.headers.get("Content-Type", "")
        data: Any
        if "application/json" in content_type:
            try:
                data = resp.json()
            except Exception:
                data = {"raw": resp.text}
        else:
            data = {"raw": resp.text}

        if resp.status_code >= 400:
            raise RuntimeError(
                json.dumps(
                    {
                        "error": True,
                        "status_code": resp.status_code,
                        "reason": resp.reason_phrase,
                        "data": data,
                        "headers": {
                            "x-request-id": resp.headers.get("X-Request-Id"),
                            "x-shopify-shop-api-call-limit": resp.headers.get("X-Shopify-Shop-Api-Call-Limit"),
                        },
                    },
                    ensure_ascii=False,
                )
            )

        return {
            "status_code": resp.status_code,
            "data": data,
            "headers": {
                "link": link,
                "retry_after": retry_after,
                "location": location,
                "x-request-id": resp.headers.get("X-Request-Id"),
                "x-shopify-shop-api-call-limit": resp.headers.get("X-Shopify-Shop-Api-Call-Limit"),
            },
        }


mcp = FastMCP("shopify-admin-rest")


def _client_from_env() -> ShopifyAdminClient:
    shop = _require_env("SHOPIFY_SHOP")
    token = _require_env("SHOPIFY_ACCESS_TOKEN")
    api_version = os.getenv("SHOPIFY_API_VERSION", DEFAULT_API_VERSION)
    return ShopifyAdminClient(shop=shop, access_token=token, api_version=api_version)


@mcp.tool()
def shopify_admin_request(
    method: str,
    path: str,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """Generic Shopify Admin REST request.

    Args:
      method: HTTP method (GET, POST, PUT, DELETE).
      path: Admin REST path under /admin/api/{version}, e.g. "/orders.json".
      query: Query parameters dict.
      body: JSON body dict.
      api_version: Override API version (default SHOPIFY_API_VERSION or 2026-01).

    Returns:
      Dict with status_code, data, and selected headers (Link, Retry-After, Location).
    """
    client = _client_from_env()
    try:
        if api_version:
            client.api_version = api_version
            client.base_url = f"https://{client.shop}/admin/api/{client.api_version}"
        return client.request(method, path, query=query, body=body)
    finally:
        client.close()


# Convenience tools for common domains (orders, customers, products, inventory, webhooks)

@mcp.tool()
def orders_list(status: str = "any", limit: int = 50, **query) -> Dict[str, Any]:
    """Retrieve a list of orders (GET /orders.json?status=any)."""
    q = {"status": status, "limit": limit}
    q.update(query)
    return shopify_admin_request("GET", "/orders.json", query=q)


@mcp.tool()
def orders_get(order_id: str, fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a specific order (GET /orders/{order_id}.json)."""
    q = {"fields": fields} if fields else None
    return shopify_admin_request("GET", f"/orders/{order_id}.json", query=q)


@mcp.tool()
def orders_create(order: Dict[str, Any]) -> Dict[str, Any]:
    """Create an order (POST /orders.json). Body wrapper key is 'order'."""
    return shopify_admin_request("POST", "/orders.json", body={"order": order})


@mcp.tool()
def orders_update(order_id: str, order: Dict[str, Any]) -> Dict[str, Any]:
    """Update an order (PUT /orders/{order_id}.json). Body wrapper key is 'order'."""
    return shopify_admin_request("PUT", f"/orders/{order_id}.json", body={"order": order})


@mcp.tool()
def orders_cancel(order_id: str, **body) -> Dict[str, Any]:
    """Cancel an order (POST /orders/{order_id}/cancel.json)."""
    return shopify_admin_request("POST", f"/orders/{order_id}/cancel.json", body=body or None)


@mcp.tool()
def customers_list(limit: int = 50, **query) -> Dict[str, Any]:
    """Retrieve a list of customers (GET /customers.json)."""
    q = {"limit": limit}
    q.update(query)
    return shopify_admin_request("GET", "/customers.json", query=q)


@mcp.tool()
def customers_get(customer_id: str, fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a specific customer (GET /customers/{customer_id}.json)."""
    q = {"fields": fields} if fields else None
    return shopify_admin_request("GET", f"/customers/{customer_id}.json", query=q)


@mcp.tool()
def customers_create(customer: Dict[str, Any]) -> Dict[str, Any]:
    """Create a customer (POST /customers.json). Body wrapper key is 'customer'."""
    return shopify_admin_request("POST", "/customers.json", body={"customer": customer})


@mcp.tool()
def products_list(limit: int = 50, **query) -> Dict[str, Any]:
    """Retrieve a list of products (GET /products.json)."""
    q = {"limit": limit}
    q.update(query)
    return shopify_admin_request("GET", "/products.json", query=q)


@mcp.tool()
def products_get(product_id: str, fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a specific product (GET /products/{product_id}.json)."""
    q = {"fields": fields} if fields else None
    return shopify_admin_request("GET", f"/products/{product_id}.json", query=q)


@mcp.tool()
def inventory_levels_list(location_id: Optional[str] = None, inventory_item_ids: Optional[str] = None, limit: int = 50, **query) -> Dict[str, Any]:
    """List inventory levels (GET /inventory_levels.json).

    Common query params:
      - location_ids (comma-separated)
      - inventory_item_ids (comma-separated)
    """
    q: Dict[str, Any] = {"limit": limit}
    if location_id:
        q["location_ids"] = location_id
    if inventory_item_ids:
        q["inventory_item_ids"] = inventory_item_ids
    q.update(query)
    return shopify_admin_request("GET", "/inventory_levels.json", query=q)


@mcp.tool()
def locations_list(limit: int = 50) -> Dict[str, Any]:
    """Retrieve a list of locations (GET /locations.json)."""
    return shopify_admin_request("GET", "/locations.json", query={"limit": limit})


@mcp.tool()
def webhooks_list(address: Optional[str] = None, topic: Optional[str] = None, limit: int = 50, **query) -> Dict[str, Any]:
    """Retrieve a list of webhooks (GET /webhooks.json)."""
    q: Dict[str, Any] = {"limit": limit}
    if address:
        q["address"] = address
    if topic:
        q["topic"] = topic
    q.update(query)
    return shopify_admin_request("GET", "/webhooks.json", query=q)


@mcp.tool()
def webhooks_create(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """Create a webhook (POST /webhooks.json). Body wrapper key is 'webhook'."""
    return shopify_admin_request("POST", "/webhooks.json", body={"webhook": webhook})


@mcp.tool()
def webhooks_delete(webhook_id: str) -> Dict[str, Any]:
    """Delete a webhook (DELETE /webhooks/{webhook_id}.json)."""
    return shopify_admin_request("DELETE", f"/webhooks/{webhook_id}.json")


if __name__ == "__main__":
    mcp.run()
