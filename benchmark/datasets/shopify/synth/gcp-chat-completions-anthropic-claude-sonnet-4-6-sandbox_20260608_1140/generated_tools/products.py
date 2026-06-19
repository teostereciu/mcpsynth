"""Shopify Admin REST API — Products tools."""
import os, requests
from mcp.server.fastmcp import FastMCP

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

def _post(path, body):
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


def register_products(mcp: FastMCP):

    @mcp.tool()
    def list_products(
        limit: int = 50,
        ids: str = None,
        since_id: int = None,
        title: str = None,
        vendor: str = None,
        product_type: str = None,
        status: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of products. status: active|archived|draft."""
        params = {"limit": limit}
        if ids: params["ids"] = ids
        if since_id: params["since_id"] = since_id
        if title: params["title"] = title
        if vendor: params["vendor"] = vendor
        if product_type: params["product_type"] = product_type
        if status: params["status"] = status
        if fields: params["fields"] = fields
        return _get("/products.json", params)

    @mcp.tool()
    def get_product(product_id: int, fields: str = None) -> dict:
        """Retrieve a single product by ID."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/products/{product_id}.json", params)

    @mcp.tool()
    def count_products(vendor: str = None, product_type: str = None, status: str = None) -> dict:
        """Retrieve a count of products."""
        params = {}
        if vendor: params["vendor"] = vendor
        if product_type: params["product_type"] = product_type
        if status: params["status"] = status
        return _get("/products/count.json", params)

    @mcp.tool()
    def create_product(
        title: str,
        body_html: str = None,
        vendor: str = None,
        product_type: str = None,
        status: str = "active",
        tags: str = None,
        variants: list = None,
        options: list = None,
        images: list = None,
    ) -> dict:
        """Create a new product. status: active|archived|draft."""
        product = {"title": title, "status": status}
        if body_html: product["body_html"] = body_html
        if vendor: product["vendor"] = vendor
        if product_type: product["product_type"] = product_type
        if tags: product["tags"] = tags
        if variants: product["variants"] = variants
        if options: product["options"] = options
        if images: product["images"] = images
        return _post("/products.json", {"product": product})

    @mcp.tool()
    def update_product(
        product_id: int,
        title: str = None,
        body_html: str = None,
        vendor: str = None,
        product_type: str = None,
        status: str = None,
        tags: str = None,
        published_at: str = None,
    ) -> dict:
        """Update an existing product."""
        product = {}
        if title: product["title"] = title
        if body_html: product["body_html"] = body_html
        if vendor: product["vendor"] = vendor
        if product_type: product["product_type"] = product_type
        if status: product["status"] = status
        if tags: product["tags"] = tags
        if published_at is not None: product["published_at"] = published_at
        return _put(f"/products/{product_id}.json", {"product": product})

    @mcp.tool()
    def delete_product(product_id: int) -> dict:
        """Delete a product by ID."""
        return _delete(f"/products/{product_id}.json")
