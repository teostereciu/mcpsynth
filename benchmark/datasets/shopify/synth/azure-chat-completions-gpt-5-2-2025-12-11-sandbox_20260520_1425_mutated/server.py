import os
import re
import json
import asyncio
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

APP_NAME = "shopify-admin-rest"


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


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


class ShopifyClient:
    def __init__(
        self,
        shop: str,
        access_token: str,
        api_version: str = "2026-01",
        timeout_s: float = 60.0,
    ):
        self.shop = _normalize_shop_domain(shop)
        self.access_token = access_token
        self.api_version = api_version
        self.timeout_s = timeout_s

    @property
    def base_url(self) -> str:
        return f"https://{self.shop}/admin/api/{self.api_version}"

    def _headers(self) -> Dict[str, str]:
        return {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def request(
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

        headers = self._headers()
        if extra_headers:
            headers.update({k: str(v) for k, v in extra_headers.items()})

        async with httpx.AsyncClient(timeout=self.timeout_s, follow_redirects=False) as client:
            resp = await client.request(method.upper(), url, params=query, json=body, headers=headers)

        # Shopify returns useful pagination in Link header
        link = resp.headers.get("Link")
        request_id = resp.headers.get("X-Request-Id")

        content_type = resp.headers.get("Content-Type", "")
        text = resp.text
        data: Any
        if "application/json" in content_type:
            try:
                data = resp.json()
            except Exception:
                data = {"_raw": text}
        else:
            data = {"_raw": text}

        if resp.status_code >= 400:
            raise RuntimeError(
                json.dumps(
                    {
                        "error": "Shopify API error",
                        "status": resp.status_code,
                        "request_id": request_id,
                        "body": data,
                    },
                    ensure_ascii=False,
                )
            )

        return {
            "status": resp.status_code,
            "request_id": request_id,
            "link": link,
            "headers": {
                "X-Shopify-Shop-Api-Call-Limit": resp.headers.get("X-Shopify-Shop-Api-Call-Limit"),
                "Retry-After": resp.headers.get("Retry-After"),
            },
            "data": data,
        }


def _get_client(
    shop: Optional[str],
    access_token: Optional[str],
    api_version: Optional[str],
) -> ShopifyClient:
    shop = shop or _env("SHOPIFY_SHOP")
    access_token = access_token or _env("SHOPIFY_ACCESS_TOKEN")
    api_version = api_version or _env("SHOPIFY_API_VERSION", "2026-01")

    if not shop:
        raise ValueError("Missing shop. Provide 'shop' or set SHOPIFY_SHOP.")
    if not access_token:
        raise ValueError("Missing access token. Provide 'access_token' or set SHOPIFY_ACCESS_TOKEN.")

    return ShopifyClient(shop=shop, access_token=access_token, api_version=api_version)


mcp = FastMCP(APP_NAME)


@mcp.tool()
async def shopify_request(
    method: str,
    path: str,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Generic Shopify Admin REST request.

    Args:
      method: HTTP method (GET, POST, PUT, DELETE).
      path: Path under /admin/api/{version}, e.g. "/orders.json".
      query: Query parameters dict.
      body: JSON body dict.
      shop: Optional shop domain or subdomain (defaults to SHOPIFY_SHOP).
      access_token: Optional Admin API access token (defaults to SHOPIFY_ACCESS_TOKEN).
      api_version: Optional API version (defaults to SHOPIFY_API_VERSION or 2026-01).
      extra_headers: Optional additional headers.

    Returns:
      Dict with status, request_id, link (pagination), headers (rate limit), and data.
    """
    client = _get_client(shop, access_token, api_version)
    return await client.request(method, path, query=query, body=body, extra_headers=extra_headers)


# Convenience tools for common resources (based on docs patterns)

@mcp.tool()
async def orders_list(
    query: Optional[Dict[str, Any]] = None,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """List orders: GET /orders.json (pagination via Link header)."""
    client = _get_client(shop, access_token, api_version)
    return await client.request("GET", "/orders.json", query=query)


@mcp.tool()
async def orders_get(
    order_id: str,
    query: Optional[Dict[str, Any]] = None,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """Get an order: GET /orders/{order_id}.json"""
    client = _get_client(shop, access_token, api_version)
    return await client.request("GET", f"/orders/{order_id}.json", query=query)


@mcp.tool()
async def customers_list(
    query: Optional[Dict[str, Any]] = None,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """List customers: GET /customers.json (pagination via Link header)."""
    client = _get_client(shop, access_token, api_version)
    return await client.request("GET", "/customers.json", query=query)


@mcp.tool()
async def customers_get(
    customer_id: str,
    query: Optional[Dict[str, Any]] = None,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """Get a customer: GET /customers/{customer_id}.json"""
    client = _get_client(shop, access_token, api_version)
    return await client.request("GET", f"/customers/{customer_id}.json", query=query)


@mcp.tool()
async def products_list(
    query: Optional[Dict[str, Any]] = None,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """List products: GET /products.json (deprecated in newer versions but still available)."""
    client = _get_client(shop, access_token, api_version)
    return await client.request("GET", "/products.json", query=query)


@mcp.tool()
async def inventory_levels_set(
    inventory_item_id: str,
    location_id: str,
    available: int,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """Set inventory level: POST /inventory_levels/set.json

    Body: {"location_id":..., "inventory_item_id":..., "available":...}
    """
    client = _get_client(shop, access_token, api_version)
    body = {
        "location_id": int(location_id),
        "inventory_item_id": int(inventory_item_id),
        "available": int(available),
    }
    return await client.request("POST", "/inventory_levels/set.json", body=body)


@mcp.tool()
async def webhooks_list(
    query: Optional[Dict[str, Any]] = None,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """List webhooks: GET /webhooks.json"""
    client = _get_client(shop, access_token, api_version)
    return await client.request("GET", "/webhooks.json", query=query)


@mcp.tool()
async def webhooks_create(
    topic: str,
    address: str,
    format: str = "json",
    fields: Optional[list[str]] = None,
    metafield_namespaces: Optional[list[str]] = None,
    shop: Optional[str] = None,
    access_token: Optional[str] = None,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """Create webhook: POST /webhooks.json

    Body: {"webhook": {"topic":..., "address":..., "format":..., ...}}
    """
    client = _get_client(shop, access_token, api_version)
    webhook: Dict[str, Any] = {"topic": topic, "address": address, "format": format}
    if fields is not None:
        webhook["fields"] = fields
    if metafield_namespaces is not None:
        webhook["metafield_namespaces"] = metafield_namespaces
    return await client.request("POST", "/webhooks.json", body={"webhook": webhook})


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
