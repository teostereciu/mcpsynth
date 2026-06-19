from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import safe_call


def get_categories(
    locale: Optional[str] = None,
    keyword: Optional[str] = None,
    category_version: Optional[str] = None,
    listing_platform: Optional[str] = None,
    include_prohibited_categories: Optional[bool] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /product/202309/categories"""
    params: Dict[str, Any] = {
        "locale": locale,
        "keyword": keyword,
        "category_version": category_version,
        "listing_platform": listing_platform,
        "include_prohibited_categories": include_prohibited_categories,
    }
    if shop_cipher:
        params["shop_cipher"] = shop_cipher
    return safe_call("GET", "/product/202309/categories", params=params)


def create_product(product: Dict[str, Any], shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """POST /product/202309/products

    Body should follow TikTok create product schema.
    """
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("POST", "/product/202309/products", params=params, body=product)


def get_product(product_id: str, shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """GET /product/202309/products/{product_id}"""
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("GET", f"/product/202309/products/{product_id}", params=params)


def search_products(
    keyword: Optional[str] = None,
    status: Optional[str] = None,
    page_size: int = 20,
    page_token: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /product/202502/products/search

    Uses newer search endpoint; falls back to older if needed.
    """
    body: Dict[str, Any] = {
        "keyword": keyword,
        "status": status,
        "page_size": page_size,
        "page_token": page_token,
    }
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    res = safe_call("POST", "/product/202502/products/search", params=params, body=body)
    if res.get("code") not in (None, 0) and "raw" in res:
        # try legacy search
        res2 = safe_call("POST", "/product/202309/products/search", params=params, body=body)
        return res2
    return res


def update_price(
    product_id: str,
    sku_id: str,
    price: float,
    currency: str = "USD",
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /product/202309/prices/update"""
    body = {
        "product_id": product_id,
        "skus": [{"id": sku_id, "price": {"amount": price, "currency": currency}}],
    }
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("POST", "/product/202309/prices/update", params=params, body=body)


def update_inventory(
    product_id: str,
    sku_id: str,
    quantity: int,
    warehouse_id: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /product/202309/inventory/update"""
    sku: Dict[str, Any] = {"id": sku_id, "quantity": quantity}
    if warehouse_id:
        sku["warehouse_id"] = warehouse_id
    body = {"product_id": product_id, "skus": [sku]}
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("POST", "/product/202309/inventory/update", params=params, body=body)
