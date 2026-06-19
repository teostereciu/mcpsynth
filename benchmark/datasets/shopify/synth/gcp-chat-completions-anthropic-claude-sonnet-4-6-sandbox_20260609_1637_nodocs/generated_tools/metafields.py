"""Shopify Admin REST API — Metafields tools."""

import os, requests
from mcp.server.fastmcp import FastMCP

def _session():
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    store = os.environ["SHOPIFY_STORE_URL"]
    base  = f"https://{store}/admin/api/2026-01"
    s = requests.Session()
    s.headers.update({"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    return s, base

# Supported owner resources for metafields
OWNER_RESOURCES = [
    "products", "variants", "customers", "orders", "draft_orders",
    "collections", "pages", "blogs", "articles", "shops",
]

def register(mcp: FastMCP):

    @mcp.tool()
    def list_metafields(owner_resource: str, owner_id: str = "",
                        namespace: str = "", limit: int = 50) -> dict:
        """List metafields for a resource.
        owner_resource: products|variants|customers|orders|draft_orders|
                        collections|pages|blogs|articles|shops.
        owner_id: omit for shop-level metafields."""
        s, base = _session()
        params: dict = {"limit": limit}
        if namespace:
            params["namespace"] = namespace
        if owner_id:
            url = f"{base}/{owner_resource}/{owner_id}/metafields.json"
        else:
            url = f"{base}/metafields.json"
            params["metafield[owner_resource]"] = owner_resource
        r = s.get(url, params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_metafield(metafield_id: str) -> dict:
        """Get a metafield by its ID."""
        s, base = _session()
        r = s.get(f"{base}/metafields/{metafield_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_metafield(owner_resource: str, owner_id: str,
                         namespace: str, key: str, value: str,
                         type: str = "single_line_text_field") -> dict:
        """Create a metafield on a resource.
        type: single_line_text_field|multi_line_text_field|integer|decimal|
              json|boolean|date|date_time|url|color|weight|volume|dimension."""
        s, base = _session()
        data: dict = {"namespace": namespace, "key": key,
                      "value": value, "type": type}
        r = s.post(f"{base}/{owner_resource}/{owner_id}/metafields.json",
                   json={"metafield": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_metafield(metafield_id: str, value: str,
                         type: str = "") -> dict:
        """Update a metafield's value."""
        s, base = _session()
        data: dict = {"value": value}
        if type:
            data["type"] = type
        r = s.put(f"{base}/metafields/{metafield_id}.json",
                  json={"metafield": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_metafield(metafield_id: str) -> dict:
        """Delete a metafield by ID."""
        s, base = _session()
        r = s.delete(f"{base}/metafields/{metafield_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "metafield_id": metafield_id}

    @mcp.tool()
    def count_metafields(owner_resource: str, owner_id: str) -> dict:
        """Count metafields for a resource."""
        s, base = _session()
        r = s.get(f"{base}/{owner_resource}/{owner_id}/metafields/count.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
