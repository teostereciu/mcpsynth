"""Shopify Admin REST API — Metafields tools (generic resource-based endpoints)."""
import os, requests
from mcp.server.fastmcp import FastMCP

BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"

# Supported owner_resource values and their URL path segments
RESOURCE_PATHS = {
    "product": "products",
    "product_image": None,  # handled specially
    "product_variant": "variants",
    "collection": "collections",
    "custom_collection": "custom_collections",
    "smart_collection": "smart_collections",
    "customer": "customers",
    "order": "orders",
    "draft_order": "draft_orders",
    "blog": "blogs",
    "article": None,  # handled specially
    "page": "pages",
    "shop": None,  # shop-level
}

def _headers():
    return {
        "X-Shopify-Access-Token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
        "Content-Type": "application/json",
    }

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, body=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, body):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), timeout=30)
        if r.status_code == 200:
            return r.json()
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)}

def _resource_base(owner_resource: str, owner_id: int) -> str:
    """Build the base URL path for a resource's metafields."""
    paths = {
        "product": f"/products/{owner_id}",
        "product_variant": f"/variants/{owner_id}",
        "collection": f"/collections/{owner_id}",
        "custom_collection": f"/custom_collections/{owner_id}",
        "smart_collection": f"/smart_collections/{owner_id}",
        "customer": f"/customers/{owner_id}",
        "order": f"/orders/{owner_id}",
        "draft_order": f"/draft_orders/{owner_id}",
        "blog": f"/blogs/{owner_id}",
        "page": f"/pages/{owner_id}",
        "shop": "/shop",
    }
    return paths.get(owner_resource, f"/{owner_resource}s/{owner_id}")


def register_metafields(mcp: FastMCP):

    @mcp.tool()
    def list_metafields(
        owner_resource: str,
        owner_id: int = None,
        namespace: str = None,
        key: str = None,
        fields: str = None,
        limit: int = 50,
    ) -> dict:
        """Retrieve metafields for a resource.
        owner_resource: product|product_variant|collection|customer|order|draft_order|blog|page|shop.
        owner_id: required for all except shop."""
        if owner_resource == "shop":
            base = "/shop"
        else:
            base = _resource_base(owner_resource, owner_id)
        params = {"limit": limit}
        if namespace: params["namespace"] = namespace
        if key: params["key"] = key
        if fields: params["fields"] = fields
        return _get(f"{base}/metafields.json", params)

    @mcp.tool()
    def get_metafield(
        owner_resource: str,
        metafield_id: int,
        owner_id: int = None,
    ) -> dict:
        """Retrieve a specific metafield.
        owner_resource: product|product_variant|collection|customer|order|draft_order|blog|page|shop."""
        if owner_resource == "shop":
            base = "/shop"
        else:
            base = _resource_base(owner_resource, owner_id)
        return _get(f"{base}/metafields/{metafield_id}.json")

    @mcp.tool()
    def count_metafields(
        owner_resource: str,
        owner_id: int = None,
    ) -> dict:
        """Retrieve a count of metafields for a resource."""
        if owner_resource == "shop":
            base = "/shop"
        else:
            base = _resource_base(owner_resource, owner_id)
        return _get(f"{base}/metafields/count.json")

    @mcp.tool()
    def create_metafield(
        owner_resource: str,
        namespace: str,
        key: str,
        value: str,
        type: str,
        owner_id: int = None,
        description: str = None,
    ) -> dict:
        """Create a metafield for a resource.
        owner_resource: product|product_variant|collection|customer|order|draft_order|blog|page|shop.
        type: single_line_text_field|multi_line_text_field|number_integer|number_decimal|json|boolean|date|date_time|url|color|weight|volume|dimension|rating."""
        if owner_resource == "shop":
            base = "/shop"
        else:
            base = _resource_base(owner_resource, owner_id)
        mf = {"namespace": namespace, "key": key, "value": value, "type": type}
        if description: mf["description"] = description
        return _post(f"{base}/metafields.json", {"metafield": mf})

    @mcp.tool()
    def update_metafield(
        owner_resource: str,
        metafield_id: int,
        value: str,
        type: str = None,
        owner_id: int = None,
    ) -> dict:
        """Update an existing metafield's value."""
        if owner_resource == "shop":
            base = "/shop"
        else:
            base = _resource_base(owner_resource, owner_id)
        mf = {"value": value}
        if type: mf["type"] = type
        return _put(f"{base}/metafields/{metafield_id}.json", {"metafield": mf})

    @mcp.tool()
    def delete_metafield(
        owner_resource: str,
        metafield_id: int,
        owner_id: int = None,
    ) -> dict:
        """Delete a metafield by its ID."""
        if owner_resource == "shop":
            base = "/shop"
        else:
            base = _resource_base(owner_resource, owner_id)
        return _delete(f"{base}/metafields/{metafield_id}.json")
