"""Shopify Admin REST API — Product Variants, Images, Collections tools."""
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


def register_collections(mcp: FastMCP):

    # ── Product Variants ──────────────────────────────────────────────────────

    @mcp.tool()
    def list_product_variants(product_id: int, limit: int = 50, fields: str = None) -> dict:
        """Retrieve a list of variants for a product."""
        params = {"limit": limit}
        if fields: params["fields"] = fields
        return _get(f"/products/{product_id}/variants.json", params)

    @mcp.tool()
    def get_product_variant(variant_id: int, fields: str = None) -> dict:
        """Retrieve a single product variant by ID."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/variants/{variant_id}.json", params)

    @mcp.tool()
    def count_product_variants(product_id: int) -> dict:
        """Retrieve a count of variants for a product."""
        return _get(f"/products/{product_id}/variants/count.json")

    @mcp.tool()
    def create_product_variant(
        product_id: int,
        option1: str = None,
        option2: str = None,
        option3: str = None,
        price: str = None,
        sku: str = None,
        barcode: str = None,
        compare_at_price: str = None,
        weight: float = None,
        weight_unit: str = None,
        inventory_management: str = None,
        inventory_policy: str = None,
        requires_shipping: bool = None,
        taxable: bool = None,
        image_id: int = None,
    ) -> dict:
        """Create a new product variant."""
        variant = {}
        if option1 is not None: variant["option1"] = option1
        if option2 is not None: variant["option2"] = option2
        if option3 is not None: variant["option3"] = option3
        if price is not None: variant["price"] = price
        if sku is not None: variant["sku"] = sku
        if barcode is not None: variant["barcode"] = barcode
        if compare_at_price is not None: variant["compare_at_price"] = compare_at_price
        if weight is not None: variant["weight"] = weight
        if weight_unit is not None: variant["weight_unit"] = weight_unit
        if inventory_management is not None: variant["inventory_management"] = inventory_management
        if inventory_policy is not None: variant["inventory_policy"] = inventory_policy
        if requires_shipping is not None: variant["requires_shipping"] = requires_shipping
        if taxable is not None: variant["taxable"] = taxable
        if image_id is not None: variant["image_id"] = image_id
        return _post(f"/products/{product_id}/variants.json", {"variant": variant})

    @mcp.tool()
    def update_product_variant(
        variant_id: int,
        price: str = None,
        sku: str = None,
        barcode: str = None,
        compare_at_price: str = None,
        option1: str = None,
        option2: str = None,
        option3: str = None,
        weight: float = None,
        weight_unit: str = None,
        inventory_policy: str = None,
        image_id: int = None,
    ) -> dict:
        """Update an existing product variant."""
        variant = {}
        if price is not None: variant["price"] = price
        if sku is not None: variant["sku"] = sku
        if barcode is not None: variant["barcode"] = barcode
        if compare_at_price is not None: variant["compare_at_price"] = compare_at_price
        if option1 is not None: variant["option1"] = option1
        if option2 is not None: variant["option2"] = option2
        if option3 is not None: variant["option3"] = option3
        if weight is not None: variant["weight"] = weight
        if weight_unit is not None: variant["weight_unit"] = weight_unit
        if inventory_policy is not None: variant["inventory_policy"] = inventory_policy
        if image_id is not None: variant["image_id"] = image_id
        return _put(f"/variants/{variant_id}.json", {"variant": variant})

    @mcp.tool()
    def delete_product_variant(product_id: int, variant_id: int) -> dict:
        """Delete a product variant."""
        return _delete(f"/products/{product_id}/variants/{variant_id}.json")

    # ── Product Images ────────────────────────────────────────────────────────

    @mcp.tool()
    def list_product_images(product_id: int, fields: str = None) -> dict:
        """Retrieve a list of images for a product."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/products/{product_id}/images.json", params)

    @mcp.tool()
    def get_product_image(product_id: int, image_id: int, fields: str = None) -> dict:
        """Retrieve a single product image."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/products/{product_id}/images/{image_id}.json", params)

    @mcp.tool()
    def count_product_images(product_id: int) -> dict:
        """Retrieve a count of images for a product."""
        return _get(f"/products/{product_id}/images/count.json")

    @mcp.tool()
    def create_product_image(
        product_id: int,
        src: str = None,
        attachment: str = None,
        filename: str = None,
        alt: str = None,
        position: int = None,
        variant_ids: list = None,
    ) -> dict:
        """Create a new product image. Provide src (URL) or attachment (base64)."""
        image = {}
        if src: image["src"] = src
        if attachment: image["attachment"] = attachment
        if filename: image["filename"] = filename
        if alt: image["alt"] = alt
        if position: image["position"] = position
        if variant_ids: image["variant_ids"] = variant_ids
        return _post(f"/products/{product_id}/images.json", {"image": image})

    @mcp.tool()
    def update_product_image(
        product_id: int,
        image_id: int,
        alt: str = None,
        position: int = None,
        variant_ids: list = None,
    ) -> dict:
        """Update an existing product image."""
        image = {}
        if alt is not None: image["alt"] = alt
        if position is not None: image["position"] = position
        if variant_ids is not None: image["variant_ids"] = variant_ids
        return _put(f"/products/{product_id}/images/{image_id}.json", {"image": image})

    @mcp.tool()
    def delete_product_image(product_id: int, image_id: int) -> dict:
        """Delete a product image."""
        return _delete(f"/products/{product_id}/images/{image_id}.json")

    # ── Custom Collections ────────────────────────────────────────────────────

    @mcp.tool()
    def list_custom_collections(
        limit: int = 50,
        ids: str = None,
        since_id: int = None,
        title: str = None,
        product_id: int = None,
        published_status: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of custom collections."""
        params = {"limit": limit}
        if ids: params["ids"] = ids
        if since_id: params["since_id"] = since_id
        if title: params["title"] = title
        if product_id: params["product_id"] = product_id
        if published_status: params["published_status"] = published_status
        if fields: params["fields"] = fields
        return _get("/custom_collections.json", params)

    @mcp.tool()
    def get_custom_collection(custom_collection_id: int, fields: str = None) -> dict:
        """Retrieve a single custom collection."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/custom_collections/{custom_collection_id}.json", params)

    @mcp.tool()
    def count_custom_collections(title: str = None, product_id: int = None) -> dict:
        """Retrieve a count of custom collections."""
        params = {}
        if title: params["title"] = title
        if product_id: params["product_id"] = product_id
        return _get("/custom_collections/count.json", params)

    @mcp.tool()
    def create_custom_collection(
        title: str,
        body_html: str = None,
        published: bool = True,
        sort_order: str = None,
        image_src: str = None,
        collects: list = None,
    ) -> dict:
        """Create a custom collection. collects: list of {product_id} dicts."""
        cc = {"title": title, "published": published}
        if body_html: cc["body_html"] = body_html
        if sort_order: cc["sort_order"] = sort_order
        if image_src: cc["image"] = {"src": image_src}
        if collects: cc["collects"] = collects
        return _post("/custom_collections.json", {"custom_collection": cc})

    @mcp.tool()
    def update_custom_collection(
        custom_collection_id: int,
        title: str = None,
        body_html: str = None,
        published: bool = None,
        sort_order: str = None,
    ) -> dict:
        """Update an existing custom collection."""
        cc = {}
        if title: cc["title"] = title
        if body_html: cc["body_html"] = body_html
        if published is not None: cc["published"] = published
        if sort_order: cc["sort_order"] = sort_order
        return _put(f"/custom_collections/{custom_collection_id}.json", {"custom_collection": cc})

    @mcp.tool()
    def delete_custom_collection(custom_collection_id: int) -> dict:
        """Delete a custom collection."""
        return _delete(f"/custom_collections/{custom_collection_id}.json")

    # ── Collects (product↔collection links) ──────────────────────────────────

    @mcp.tool()
    def list_collects(
        limit: int = 50,
        product_id: int = None,
        collection_id: int = None,
    ) -> dict:
        """Retrieve a list of collects (product-collection associations)."""
        params = {"limit": limit}
        if product_id: params["product_id"] = product_id
        if collection_id: params["collection_id"] = collection_id
        return _get("/collects.json", params)

    @mcp.tool()
    def create_collect(product_id: int, collection_id: int) -> dict:
        """Add a product to a custom collection."""
        return _post("/collects.json", {"collect": {"product_id": product_id, "collection_id": collection_id}})

    @mcp.tool()
    def delete_collect(collect_id: int) -> dict:
        """Remove a product from a custom collection."""
        return _delete(f"/collects/{collect_id}.json")

    @mcp.tool()
    def get_collection(collection_id: int, fields: str = None) -> dict:
        """Retrieve a single collection (works for both custom and smart)."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/collections/{collection_id}.json", params)

    @mcp.tool()
    def list_collection_products(collection_id: int, limit: int = 50) -> dict:
        """Retrieve products belonging to a collection."""
        return _get(f"/collections/{collection_id}/products.json", {"limit": limit})

    # ── Smart Collections ─────────────────────────────────────────────────────

    @mcp.tool()
    def list_smart_collections(
        limit: int = 50,
        since_id: int = None,
        title: str = None,
        product_id: int = None,
        published_status: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of smart collections."""
        params = {"limit": limit}
        if since_id: params["since_id"] = since_id
        if title: params["title"] = title
        if product_id: params["product_id"] = product_id
        if published_status: params["published_status"] = published_status
        if fields: params["fields"] = fields
        return _get("/smart_collections.json", params)

    @mcp.tool()
    def get_smart_collection(smart_collection_id: int, fields: str = None) -> dict:
        """Retrieve a single smart collection."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/smart_collections/{smart_collection_id}.json", params)

    @mcp.tool()
    def count_smart_collections(title: str = None, product_id: int = None) -> dict:
        """Retrieve a count of smart collections."""
        params = {}
        if title: params["title"] = title
        if product_id: params["product_id"] = product_id
        return _get("/smart_collections/count.json", params)

    @mcp.tool()
    def create_smart_collection(
        title: str,
        rules: list,
        disjunctive: bool = False,
        body_html: str = None,
        published: bool = True,
        sort_order: str = None,
    ) -> dict:
        """Create a smart collection with rules.
        rules: list of {column, relation, condition} dicts.
        disjunctive: True = match any rule, False = match all rules."""
        sc = {"title": title, "rules": rules, "disjunctive": disjunctive, "published": published}
        if body_html: sc["body_html"] = body_html
        if sort_order: sc["sort_order"] = sort_order
        return _post("/smart_collections.json", {"smart_collection": sc})

    @mcp.tool()
    def update_smart_collection(
        smart_collection_id: int,
        title: str = None,
        rules: list = None,
        disjunctive: bool = None,
        body_html: str = None,
        published: bool = None,
        sort_order: str = None,
    ) -> dict:
        """Update an existing smart collection."""
        sc = {}
        if title: sc["title"] = title
        if rules is not None: sc["rules"] = rules
        if disjunctive is not None: sc["disjunctive"] = disjunctive
        if body_html: sc["body_html"] = body_html
        if published is not None: sc["published"] = published
        if sort_order: sc["sort_order"] = sort_order
        return _put(f"/smart_collections/{smart_collection_id}.json", {"smart_collection": sc})

    @mcp.tool()
    def delete_smart_collection(smart_collection_id: int) -> dict:
        """Delete a smart collection."""
        return _delete(f"/smart_collections/{smart_collection_id}.json")
