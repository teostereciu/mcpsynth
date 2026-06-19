"""Shopify Admin REST API — Custom Collections, Smart Collections, Collects tools."""
import os, requests
from typing import Optional, Any

BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"

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


# ── Custom Collections ────────────────────────────────────────────────────────

def list_custom_collections(limit: int = 50, ids: Optional[str] = None,
                            product_id: Optional[int] = None,
                            title: Optional[str] = None) -> dict:
    """Retrieve a list of custom collections."""
    params: dict[str, Any] = {"limit": limit}
    if ids: params["ids"] = ids
    if product_id: params["product_id"] = product_id
    if title: params["title"] = title
    return _get("/custom_collections.json", params)

def get_custom_collection(custom_collection_id: int) -> dict:
    """Retrieve a single custom collection."""
    return _get(f"/custom_collections/{custom_collection_id}.json")

def count_custom_collections() -> dict:
    """Retrieve a count of custom collections."""
    return _get("/custom_collections/count.json")

def create_custom_collection(title: str, body_html: Optional[str] = None,
                             published: bool = True,
                             sort_order: Optional[str] = None,
                             image: Optional[dict] = None,
                             collects: Optional[list] = None) -> dict:
    """Create a custom collection.
    sort_order: alpha-asc|alpha-desc|best-selling|created|created-desc|manual|price-asc|price-desc
    collects: list of {"product_id": id} to add products
    """
    collection: dict[str, Any] = {"title": title, "published": published}
    if body_html: collection["body_html"] = body_html
    if sort_order: collection["sort_order"] = sort_order
    if image: collection["image"] = image
    if collects: collection["collects"] = collects
    return _post("/custom_collections.json", {"custom_collection": collection})

def update_custom_collection(custom_collection_id: int, title: Optional[str] = None,
                             body_html: Optional[str] = None,
                             published: Optional[bool] = None,
                             sort_order: Optional[str] = None,
                             image: Optional[dict] = None) -> dict:
    """Update an existing custom collection."""
    collection: dict[str, Any] = {"id": custom_collection_id}
    if title is not None: collection["title"] = title
    if body_html is not None: collection["body_html"] = body_html
    if published is not None: collection["published"] = published
    if sort_order is not None: collection["sort_order"] = sort_order
    if image is not None: collection["image"] = image
    return _put(f"/custom_collections/{custom_collection_id}.json",
                {"custom_collection": collection})

def delete_custom_collection(custom_collection_id: int) -> dict:
    """Delete a custom collection."""
    return _delete(f"/custom_collections/{custom_collection_id}.json")


# ── Smart Collections ─────────────────────────────────────────────────────────

def list_smart_collections(limit: int = 50, title: Optional[str] = None,
                           product_id: Optional[int] = None) -> dict:
    """Retrieve a list of smart collections."""
    params: dict[str, Any] = {"limit": limit}
    if title: params["title"] = title
    if product_id: params["product_id"] = product_id
    return _get("/smart_collections.json", params)

def get_smart_collection(smart_collection_id: int) -> dict:
    """Retrieve a single smart collection."""
    return _get(f"/smart_collections/{smart_collection_id}.json")

def count_smart_collections() -> dict:
    """Retrieve a count of smart collections."""
    return _get("/smart_collections/count.json")

def create_smart_collection(title: str, rules: list,
                            body_html: Optional[str] = None,
                            disjunctive: bool = False,
                            published: bool = True,
                            sort_order: Optional[str] = None,
                            image: Optional[dict] = None) -> dict:
    """Create a smart collection.
    rules: list of {column, relation, condition} dicts
    disjunctive: if True, products match ANY rule; if False, ALL rules
    """
    collection: dict[str, Any] = {
        "title": title,
        "rules": rules,
        "disjunctive": disjunctive,
        "published": published,
    }
    if body_html: collection["body_html"] = body_html
    if sort_order: collection["sort_order"] = sort_order
    if image: collection["image"] = image
    return _post("/smart_collections.json", {"smart_collection": collection})

def update_smart_collection(smart_collection_id: int, title: Optional[str] = None,
                            rules: Optional[list] = None,
                            body_html: Optional[str] = None,
                            disjunctive: Optional[bool] = None,
                            sort_order: Optional[str] = None) -> dict:
    """Update an existing smart collection."""
    collection: dict[str, Any] = {"id": smart_collection_id}
    if title is not None: collection["title"] = title
    if rules is not None: collection["rules"] = rules
    if body_html is not None: collection["body_html"] = body_html
    if disjunctive is not None: collection["disjunctive"] = disjunctive
    if sort_order is not None: collection["sort_order"] = sort_order
    return _put(f"/smart_collections/{smart_collection_id}.json",
                {"smart_collection": collection})

def delete_smart_collection(smart_collection_id: int) -> dict:
    """Delete a smart collection."""
    return _delete(f"/smart_collections/{smart_collection_id}.json")
