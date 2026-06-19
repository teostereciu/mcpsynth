"""Shopify Admin REST API — Metafields tools (for products, orders, customers, etc.)."""
import os, requests
from typing import Optional, Any

BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"

# Supported owner resource types and their URL prefixes
RESOURCE_PATHS = {
    "product": "/products",
    "product_image": None,  # handled specially
    "product_variant": "/variants",
    "custom_collection": "/custom_collections",
    "smart_collection": "/smart_collections",
    "customer": "/customers",
    "order": "/orders",
    "draft_order": "/draft_orders",
    "blog": "/blogs",
    "article": None,  # needs blog_id
    "page": "/pages",
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

def _post(path, payload):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, payload):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
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

def _resource_base(resource_type: str, resource_id: Optional[int]) -> str:
    """Build the base path for a resource's metafields endpoint."""
    paths = {
        "product": f"/products/{resource_id}",
        "product_variant": f"/variants/{resource_id}",
        "custom_collection": f"/custom_collections/{resource_id}",
        "smart_collection": f"/smart_collections/{resource_id}",
        "customer": f"/customers/{resource_id}",
        "order": f"/orders/{resource_id}",
        "draft_order": f"/draft_orders/{resource_id}",
        "blog": f"/blogs/{resource_id}",
        "page": f"/pages/{resource_id}",
        "shop": "",
    }
    return paths.get(resource_type, f"/{resource_type}s/{resource_id}")


# ── Metafields ────────────────────────────────────────────────────────────────

def list_metafields(resource_type: str, resource_id: Optional[int] = None,
                    namespace: Optional[str] = None, key: Optional[str] = None,
                    limit: int = 50) -> dict:
    """Retrieve a list of metafields for a resource.
    resource_type: product|product_variant|custom_collection|smart_collection|
                   customer|order|draft_order|blog|page|shop
    resource_id: required for all except 'shop'
    """
    base = _resource_base(resource_type, resource_id)
    params: dict[str, Any] = {"limit": limit}
    if namespace: params["namespace"] = namespace
    if key: params["key"] = key
    return _get(f"{base}/metafields.json", params)

def get_metafield(resource_type: str, resource_id: Optional[int],
                  metafield_id: int) -> dict:
    """Retrieve a specific metafield."""
    base = _resource_base(resource_type, resource_id)
    return _get(f"{base}/metafields/{metafield_id}.json")

def count_metafields(resource_type: str, resource_id: Optional[int] = None) -> dict:
    """Retrieve a count of metafields for a resource."""
    base = _resource_base(resource_type, resource_id)
    return _get(f"{base}/metafields/count.json")

def create_metafield(resource_type: str, resource_id: Optional[int],
                     namespace: str, key: str, value: str, type: str,
                     description: Optional[str] = None) -> dict:
    """Create a metafield for a resource.
    type: single_line_text_field|multi_line_text_field|number_integer|number_decimal|
          json|boolean|date|date_time|url|color|weight|volume|dimension|rating
    """
    base = _resource_base(resource_type, resource_id)
    metafield: dict[str, Any] = {
        "namespace": namespace,
        "key": key,
        "value": value,
        "type": type,
    }
    if description: metafield["description"] = description
    return _post(f"{base}/metafields.json", {"metafield": metafield})

def update_metafield(resource_type: str, resource_id: Optional[int],
                     metafield_id: int, value: str,
                     type: Optional[str] = None) -> dict:
    """Update an existing metafield's value."""
    base = _resource_base(resource_type, resource_id)
    metafield: dict[str, Any] = {"id": metafield_id, "value": value}
    if type: metafield["type"] = type
    return _put(f"{base}/metafields/{metafield_id}.json", {"metafield": metafield})

def delete_metafield(resource_type: str, resource_id: Optional[int],
                     metafield_id: int) -> dict:
    """Delete a metafield by its ID."""
    base = _resource_base(resource_type, resource_id)
    return _delete(f"{base}/metafields/{metafield_id}.json")
