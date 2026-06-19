"""Shopify Admin REST API — Products, Variants, Images tools."""
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


# ── Products ──────────────────────────────────────────────────────────────────

def list_products(limit: int = 50, status: Optional[str] = None,
                  vendor: Optional[str] = None, product_type: Optional[str] = None,
                  ids: Optional[str] = None) -> dict:
    """Retrieve a list of products. status: active|archived|draft."""
    params = {"limit": limit}
    if status: params["status"] = status
    if vendor: params["vendor"] = vendor
    if product_type: params["product_type"] = product_type
    if ids: params["ids"] = ids
    return _get("/products.json", params)

def get_product(product_id: int) -> dict:
    """Retrieve a single product by ID."""
    return _get(f"/products/{product_id}.json")

def count_products(status: Optional[str] = None) -> dict:
    """Retrieve a count of products."""
    params = {}
    if status: params["status"] = status
    return _get("/products/count.json", params)

def create_product(title: str, body_html: Optional[str] = None,
                   vendor: Optional[str] = None, product_type: Optional[str] = None,
                   status: Optional[str] = None, tags: Optional[str] = None,
                   variants: Optional[list] = None, images: Optional[list] = None,
                   options: Optional[list] = None) -> dict:
    """Create a new product."""
    product: dict[str, Any] = {"title": title}
    if body_html is not None: product["body_html"] = body_html
    if vendor is not None: product["vendor"] = vendor
    if product_type is not None: product["product_type"] = product_type
    if status is not None: product["status"] = status
    if tags is not None: product["tags"] = tags
    if variants is not None: product["variants"] = variants
    if images is not None: product["images"] = images
    if options is not None: product["options"] = options
    return _post("/products.json", {"product": product})

def update_product(product_id: int, title: Optional[str] = None,
                   body_html: Optional[str] = None, vendor: Optional[str] = None,
                   product_type: Optional[str] = None, status: Optional[str] = None,
                   tags: Optional[str] = None, published_at: Optional[str] = None) -> dict:
    """Update an existing product."""
    product: dict[str, Any] = {"id": product_id}
    if title is not None: product["title"] = title
    if body_html is not None: product["body_html"] = body_html
    if vendor is not None: product["vendor"] = vendor
    if product_type is not None: product["product_type"] = product_type
    if status is not None: product["status"] = status
    if tags is not None: product["tags"] = tags
    if published_at is not None: product["published_at"] = published_at
    return _put(f"/products/{product_id}.json", {"product": product})

def delete_product(product_id: int) -> dict:
    """Delete a product."""
    return _delete(f"/products/{product_id}.json")


# ── Product Variants ──────────────────────────────────────────────────────────

def list_product_variants(product_id: int, limit: int = 50) -> dict:
    """Retrieve a list of product variants for a product."""
    return _get(f"/products/{product_id}/variants.json", {"limit": limit})

def get_product_variant(variant_id: int) -> dict:
    """Retrieve a single product variant by ID."""
    return _get(f"/variants/{variant_id}.json")

def count_product_variants(product_id: int) -> dict:
    """Retrieve a count of product variants for a product."""
    return _get(f"/products/{product_id}/variants/count.json")

def create_product_variant(product_id: int, option1: Optional[str] = None,
                           option2: Optional[str] = None, option3: Optional[str] = None,
                           price: Optional[str] = None, sku: Optional[str] = None,
                           barcode: Optional[str] = None, weight: Optional[float] = None,
                           weight_unit: Optional[str] = None,
                           inventory_policy: Optional[str] = None,
                           compare_at_price: Optional[str] = None,
                           image_id: Optional[int] = None) -> dict:
    """Create a new product variant."""
    variant: dict[str, Any] = {}
    if option1 is not None: variant["option1"] = option1
    if option2 is not None: variant["option2"] = option2
    if option3 is not None: variant["option3"] = option3
    if price is not None: variant["price"] = price
    if sku is not None: variant["sku"] = sku
    if barcode is not None: variant["barcode"] = barcode
    if weight is not None: variant["weight"] = weight
    if weight_unit is not None: variant["weight_unit"] = weight_unit
    if inventory_policy is not None: variant["inventory_policy"] = inventory_policy
    if compare_at_price is not None: variant["compare_at_price"] = compare_at_price
    if image_id is not None: variant["image_id"] = image_id
    return _post(f"/products/{product_id}/variants.json", {"variant": variant})

def update_product_variant(variant_id: int, price: Optional[str] = None,
                           sku: Optional[str] = None, option1: Optional[str] = None,
                           option2: Optional[str] = None, option3: Optional[str] = None,
                           barcode: Optional[str] = None, weight: Optional[float] = None,
                           weight_unit: Optional[str] = None,
                           compare_at_price: Optional[str] = None,
                           inventory_policy: Optional[str] = None,
                           image_id: Optional[int] = None) -> dict:
    """Update an existing product variant."""
    variant: dict[str, Any] = {"id": variant_id}
    if price is not None: variant["price"] = price
    if sku is not None: variant["sku"] = sku
    if option1 is not None: variant["option1"] = option1
    if option2 is not None: variant["option2"] = option2
    if option3 is not None: variant["option3"] = option3
    if barcode is not None: variant["barcode"] = barcode
    if weight is not None: variant["weight"] = weight
    if weight_unit is not None: variant["weight_unit"] = weight_unit
    if compare_at_price is not None: variant["compare_at_price"] = compare_at_price
    if inventory_policy is not None: variant["inventory_policy"] = inventory_policy
    if image_id is not None: variant["image_id"] = image_id
    return _put(f"/variants/{variant_id}.json", {"variant": variant})

def delete_product_variant(product_id: int, variant_id: int) -> dict:
    """Delete a product variant."""
    return _delete(f"/products/{product_id}/variants/{variant_id}.json")


# ── Product Images ────────────────────────────────────────────────────────────

def list_product_images(product_id: int) -> dict:
    """Retrieve a list of product images."""
    return _get(f"/products/{product_id}/images.json")

def get_product_image(product_id: int, image_id: int) -> dict:
    """Retrieve a single product image."""
    return _get(f"/products/{product_id}/images/{image_id}.json")

def count_product_images(product_id: int) -> dict:
    """Retrieve a count of product images."""
    return _get(f"/products/{product_id}/images/count.json")

def create_product_image(product_id: int, src: Optional[str] = None,
                         attachment: Optional[str] = None,
                         filename: Optional[str] = None,
                         position: Optional[int] = None,
                         variant_ids: Optional[list] = None,
                         alt: Optional[str] = None) -> dict:
    """Create a new product image. Provide src (URL) or attachment (base64)."""
    image: dict[str, Any] = {}
    if src is not None: image["src"] = src
    if attachment is not None: image["attachment"] = attachment
    if filename is not None: image["filename"] = filename
    if position is not None: image["position"] = position
    if variant_ids is not None: image["variant_ids"] = variant_ids
    if alt is not None: image["alt"] = alt
    return _post(f"/products/{product_id}/images.json", {"image": image})

def update_product_image(product_id: int, image_id: int,
                         position: Optional[int] = None,
                         alt: Optional[str] = None,
                         variant_ids: Optional[list] = None) -> dict:
    """Update an existing product image."""
    image: dict[str, Any] = {"id": image_id}
    if position is not None: image["position"] = position
    if alt is not None: image["alt"] = alt
    if variant_ids is not None: image["variant_ids"] = variant_ids
    return _put(f"/products/{product_id}/images/{image_id}.json", {"image": image})

def delete_product_image(product_id: int, image_id: int) -> dict:
    """Delete a product image."""
    return _delete(f"/products/{product_id}/images/{image_id}.json")
