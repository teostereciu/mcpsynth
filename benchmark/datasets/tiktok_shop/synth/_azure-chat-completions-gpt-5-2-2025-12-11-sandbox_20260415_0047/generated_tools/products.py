from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def products_get_categories(locale: str = "en-US", keyword: Optional[str] = None) -> Dict[str, Any]:
    """Browse product categories.

    API: GET /product/202309/categories
    """

    params: Dict[str, Any] = {"locale": locale}
    if keyword:
        params["keyword"] = keyword
    return tiktok_request("GET", "/product/202309/categories", params=params)


@mcp.tool()
def products_recommend_category(product_title: str, locale: str = "en-US") -> Dict[str, Any]:
    """Recommend categories for a product title.

    API: POST /product/202309/categories/recommend
    """

    body = {"product_title": product_title, "locale": locale}
    return tiktok_request("POST", "/product/202309/categories/recommend", body=body)


@mcp.tool()
def products_get_brands(category_id: str, keyword: Optional[str] = None) -> Dict[str, Any]:
    """Get brand list for a category.

    API: GET /product/202309/brands
    """

    params: Dict[str, Any] = {"category_id": category_id}
    if keyword:
        params["keyword"] = keyword
    return tiktok_request("GET", "/product/202309/brands", params=params)


@mcp.tool()
def products_get_attributes(category_id: str, locale: str = "en-US") -> Dict[str, Any]:
    """Get category attributes.

    API: GET /product/202309/attributes
    """

    params = {"category_id": category_id, "locale": locale}
    return tiktok_request("GET", "/product/202309/attributes", params=params)


@mcp.tool()
def products_create_product(
    title: str,
    category_id: str,
    price: float,
    quantity: int,
    currency: str = "USD",
    save_mode: str = "LISTING",
) -> Dict[str, Any]:
    """Create a product (simple single-SKU helper).

    API: POST /product/202309/products

    Note: TikTok product creation is complex; this helper builds a minimal payload
    that works for many categories but may require additional fields depending on
    category rules.
    """

    body: Dict[str, Any] = {
        "title": title,
        "category_id": category_id,
        "save_mode": save_mode,
        "skus": [
            {
                "seller_sku": "SKU-1",
                "price": {"amount": str(price), "currency": currency},
                "inventory": [{"quantity": quantity}],
            }
        ],
    }
    return tiktok_request("POST", "/product/202309/products", body=body)


@mcp.tool()
def products_search_products(
    keyword: Optional[str] = None,
    status: Optional[str] = None,
    page_size: int = 20,
    page_token: Optional[str] = None,
) -> Dict[str, Any]:
    """Search products.

    API: POST /product/202502/products/search
    """

    body: Dict[str, Any] = {"page_size": page_size}
    if keyword:
        body["keyword"] = keyword
    if status:
        body["status"] = status
    if page_token:
        body["page_token"] = page_token
    return tiktok_request("POST", "/product/202502/products/search", body=body)


@mcp.tool()
def products_get_product(product_id: str) -> Dict[str, Any]:
    """Get product details.

    API: GET /product/202309/products/{product_id}
    """

    return tiktok_request("GET", f"/product/202309/products/{product_id}")


@mcp.tool()
def products_update_price(product_id: str, sku_id: str, price: float, currency: str = "USD") -> Dict[str, Any]:
    """Update SKU price.

    API: POST /product/202309/products/prices/update
    """

    body = {
        "product_id": product_id,
        "skus": [{"id": sku_id, "price": {"amount": str(price), "currency": currency}}],
    }
    return tiktok_request("POST", "/product/202309/products/prices/update", body=body)


@mcp.tool()
def products_update_inventory(
    product_id: str,
    sku_id: str,
    quantity: int,
    warehouse_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Update SKU inventory.

    API: POST /product/202309/products/inventory/update
    """

    inv: Dict[str, Any] = {"quantity": quantity}
    if warehouse_id:
        inv["warehouse_id"] = warehouse_id

    body = {"product_id": product_id, "skus": [{"id": sku_id, "inventory": [inv]}]}
    return tiktok_request("POST", "/product/202309/products/inventory/update", body=body)
