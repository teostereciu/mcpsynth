"""Shopify Admin REST API — Collections (Custom & Smart) tools."""

import os, requests
from mcp.server.fastmcp import FastMCP

def _session():
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    store = os.environ["SHOPIFY_STORE_URL"]
    base  = f"https://{store}/admin/api/2026-01"
    s = requests.Session()
    s.headers.update({"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    return s, base

def register(mcp: FastMCP):

    # ── Custom Collections ────────────────────────────────────────────────────

    @mcp.tool()
    def list_custom_collections(limit: int = 50, page_info: str = "") -> dict:
        """List all custom collections."""
        s, base = _session()
        params = {"limit": limit}
        if page_info:
            params["page_info"] = page_info
        r = s.get(f"{base}/custom_collections.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_custom_collection(collection_id: str) -> dict:
        """Get a custom collection by ID."""
        s, base = _session()
        r = s.get(f"{base}/custom_collections/{collection_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_custom_collection(title: str, body_html: str = "",
                                 published: bool = True) -> dict:
        """Create a custom collection."""
        s, base = _session()
        data: dict = {"title": title, "published": published}
        if body_html:
            data["body_html"] = body_html
        r = s.post(f"{base}/custom_collections.json", json={"custom_collection": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_custom_collection(collection_id: str, title: str = "",
                                 body_html: str = "", published: bool = None) -> dict:
        """Update a custom collection."""
        s, base = _session()
        data: dict = {}
        if title:              data["title"]     = title
        if body_html:          data["body_html"] = body_html
        if published is not None: data["published"] = published
        r = s.put(f"{base}/custom_collections/{collection_id}.json",
                  json={"custom_collection": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_custom_collection(collection_id: str) -> dict:
        """Delete a custom collection."""
        s, base = _session()
        r = s.delete(f"{base}/custom_collections/{collection_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "collection_id": collection_id}

    # ── Smart Collections ─────────────────────────────────────────────────────

    @mcp.tool()
    def list_smart_collections(limit: int = 50, page_info: str = "") -> dict:
        """List all smart (automated) collections."""
        s, base = _session()
        params = {"limit": limit}
        if page_info:
            params["page_info"] = page_info
        r = s.get(f"{base}/smart_collections.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_smart_collection(collection_id: str) -> dict:
        """Get a smart collection by ID."""
        s, base = _session()
        r = s.get(f"{base}/smart_collections/{collection_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_smart_collection(title: str, rules: list, disjunctive: bool = False,
                                body_html: str = "") -> dict:
        """Create a smart collection with automated rules.
        rules: list of {column, relation, condition} dicts."""
        s, base = _session()
        data: dict = {"title": title, "rules": rules, "disjunctive": disjunctive}
        if body_html:
            data["body_html"] = body_html
        r = s.post(f"{base}/smart_collections.json", json={"smart_collection": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_smart_collection(collection_id: str, title: str = "",
                                rules: list = [], body_html: str = "") -> dict:
        """Update a smart collection."""
        s, base = _session()
        data: dict = {}
        if title:     data["title"]     = title
        if rules:     data["rules"]     = rules
        if body_html: data["body_html"] = body_html
        r = s.put(f"{base}/smart_collections/{collection_id}.json",
                  json={"smart_collection": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_smart_collection(collection_id: str) -> dict:
        """Delete a smart collection."""
        s, base = _session()
        r = s.delete(f"{base}/smart_collections/{collection_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "collection_id": collection_id}

    # ── Collects (product↔collection membership) ──────────────────────────────

    @mcp.tool()
    def list_collects(collection_id: str = "", product_id: str = "",
                      limit: int = 50) -> dict:
        """List collect associations between products and custom collections."""
        s, base = _session()
        params: dict = {"limit": limit}
        if collection_id: params["collection_id"] = collection_id
        if product_id:    params["product_id"]    = product_id
        r = s.get(f"{base}/collects.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def add_product_to_collection(product_id: str, collection_id: str) -> dict:
        """Add a product to a custom collection."""
        s, base = _session()
        r = s.post(f"{base}/collects.json",
                   json={"collect": {"product_id": product_id,
                                     "collection_id": collection_id}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def remove_product_from_collection(collect_id: str) -> dict:
        """Remove a product from a custom collection by collect ID."""
        s, base = _session()
        r = s.delete(f"{base}/collects/{collect_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "collect_id": collect_id}
