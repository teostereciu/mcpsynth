"""Shopify Admin REST API — Products, Variants, Images tools."""

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

    @mcp.tool()
    def list_products(limit: int = 50, page_info: str = "", status: str = "") -> dict:
        """List products in the store. Supports pagination via page_info cursor."""
        s, base = _session()
        params = {"limit": limit}
        if page_info:
            params["page_info"] = page_info
        if status:
            params["status"] = status
        r = s.get(f"{base}/products.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_product(product_id: str) -> dict:
        """Get a single product by ID."""
        s, base = _session()
        r = s.get(f"{base}/products/{product_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_product(title: str, body_html: str = "", vendor: str = "",
                       product_type: str = "", status: str = "draft",
                       tags: str = "") -> dict:
        """Create a new product."""
        s, base = _session()
        payload: dict = {"product": {"title": title, "status": status}}
        if body_html:    payload["product"]["body_html"]    = body_html
        if vendor:       payload["product"]["vendor"]       = vendor
        if product_type: payload["product"]["product_type"] = product_type
        if tags:         payload["product"]["tags"]         = tags
        r = s.post(f"{base}/products.json", json=payload)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_product(product_id: str, title: str = "", body_html: str = "",
                       vendor: str = "", product_type: str = "",
                       status: str = "", tags: str = "") -> dict:
        """Update an existing product."""
        s, base = _session()
        data: dict = {}
        if title:        data["title"]        = title
        if body_html:    data["body_html"]    = body_html
        if vendor:       data["vendor"]       = vendor
        if product_type: data["product_type"] = product_type
        if status:       data["status"]       = status
        if tags:         data["tags"]         = tags
        r = s.put(f"{base}/products/{product_id}.json", json={"product": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_product(product_id: str) -> dict:
        """Delete a product by ID."""
        s, base = _session()
        r = s.delete(f"{base}/products/{product_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "product_id": product_id}

    @mcp.tool()
    def count_products(status: str = "") -> dict:
        """Count products in the store."""
        s, base = _session()
        params = {}
        if status:
            params["status"] = status
        r = s.get(f"{base}/products/count.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Variants ──────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_product_variants(product_id: str, limit: int = 50) -> dict:
        """List all variants for a product."""
        s, base = _session()
        r = s.get(f"{base}/products/{product_id}/variants.json", params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_product_variant(variant_id: str) -> dict:
        """Get a single product variant by ID."""
        s, base = _session()
        r = s.get(f"{base}/variants/{variant_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_product_variant(product_id: str, price: str, option1: str = "",
                               sku: str = "", inventory_quantity: int = 0,
                               weight: float = 0.0, weight_unit: str = "kg") -> dict:
        """Create a new variant for a product."""
        s, base = _session()
        data: dict = {"price": price}
        if option1:             data["option1"]             = option1
        if sku:                 data["sku"]                 = sku
        if inventory_quantity:  data["inventory_quantity"]  = inventory_quantity
        if weight:              data["weight"]              = weight
        if weight_unit:         data["weight_unit"]         = weight_unit
        r = s.post(f"{base}/products/{product_id}/variants.json", json={"variant": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_product_variant(variant_id: str, price: str = "", sku: str = "",
                               option1: str = "", inventory_quantity: int = -1,
                               weight: float = -1.0, weight_unit: str = "") -> dict:
        """Update an existing product variant."""
        s, base = _session()
        data: dict = {}
        if price:                       data["price"]               = price
        if sku:                         data["sku"]                 = sku
        if option1:                     data["option1"]             = option1
        if inventory_quantity >= 0:     data["inventory_quantity"]  = inventory_quantity
        if weight >= 0:                 data["weight"]              = weight
        if weight_unit:                 data["weight_unit"]         = weight_unit
        r = s.put(f"{base}/variants/{variant_id}.json", json={"variant": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_product_variant(product_id: str, variant_id: str) -> dict:
        """Delete a product variant."""
        s, base = _session()
        r = s.delete(f"{base}/products/{product_id}/variants/{variant_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "variant_id": variant_id}

    # ── Images ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_product_images(product_id: str) -> dict:
        """List all images for a product."""
        s, base = _session()
        r = s.get(f"{base}/products/{product_id}/images.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_product_image(product_id: str, src: str, alt: str = "",
                             variant_ids: list = []) -> dict:
        """Add an image to a product by URL."""
        s, base = _session()
        data: dict = {"src": src}
        if alt:          data["alt"]         = alt
        if variant_ids:  data["variant_ids"] = variant_ids
        r = s.post(f"{base}/products/{product_id}/images.json", json={"image": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_product_image(product_id: str, image_id: str) -> dict:
        """Delete a product image."""
        s, base = _session()
        r = s.delete(f"{base}/products/{product_id}/images/{image_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "image_id": image_id}
