"""Products/Catalog domain tools."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import TikTokRequestOptions, tiktok_request


def get_categories(
    *,
    locale: Optional[str] = None,
    keyword: Optional[str] = None,
    category_version: Optional[str] = None,
    listing_platform: Optional[str] = None,
    include_prohibited_categories: Optional[bool] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get product categories.

    API: GET /product/202309/categories
    """

    params: Dict[str, Any] = {}
    if locale is not None:
        params["locale"] = locale
    if keyword is not None:
        params["keyword"] = keyword
    if category_version is not None:
        params["category_version"] = category_version
    if listing_platform is not None:
        params["listing_platform"] = listing_platform
    if include_prohibited_categories is not None:
        params["include_prohibited_categories"] = str(include_prohibited_categories).lower()

    return tiktok_request(
        "GET",
        "/product/202309/categories",
        params=params,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def recommend_category(
    *,
    product_title: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Recommend categories for a product title.

    API: POST /product/202309/categories/recommend
    """

    body = {"product_title": product_title}
    return tiktok_request(
        "POST",
        "/product/202309/categories/recommend",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def get_brands(
    *,
    category_id: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get brands for a category.

    API: GET /product/202309/brands
    """

    return tiktok_request(
        "GET",
        "/product/202309/brands",
        params={"category_id": category_id},
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def get_attributes(
    *,
    category_id: str,
    locale: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get category attributes.

    API: GET /product/202309/attributes
    """

    params: Dict[str, Any] = {"category_id": category_id}
    if locale is not None:
        params["locale"] = locale

    return tiktok_request(
        "GET",
        "/product/202309/attributes",
        params=params,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def create_product(
    *,
    title: str,
    category_id: str,
    description: Optional[str] = None,
    currency: str = "USD",
    price: Optional[float] = None,
    quantity: Optional[int] = None,
    save_mode: str = "DRAFT",
    main_images: Optional[List[str]] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a product.

    API: POST /product/202309/products

    Note: The full schema is extensive; this tool supports a practical subset.
    """

    body: Dict[str, Any] = {
        "title": title,
        "category_id": category_id,
        "save_mode": save_mode,
    }
    if description is not None:
        body["description"] = description
    if main_images is not None:
        body["main_images"] = main_images

    # Minimal SKU model: single SKU with optional price/inventory.
    if price is not None or quantity is not None:
        sku: Dict[str, Any] = {}
        if price is not None:
            sku["price"] = {"currency": currency, "amount": str(price)}
        if quantity is not None:
            sku["inventory"] = [{"quantity": int(quantity)}]
        body["skus"] = [sku]

    return tiktok_request(
        "POST",
        "/product/202309/products",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def search_products(
    *,
    keyword: Optional[str] = None,
    status: Optional[str] = None,
    page_size: int = 20,
    page_token: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Search products.

    API: POST /product/202502/products/search
    """

    body: Dict[str, Any] = {"page_size": page_size}
    if keyword is not None:
        body["keyword"] = keyword
    if status is not None:
        body["status"] = status
    if page_token is not None:
        body["page_token"] = page_token

    return tiktok_request(
        "POST",
        "/product/202502/products/search",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def get_product(
    *,
    product_id: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get product details.

    API: GET /product/202309/products/{product_id}
    """

    return tiktok_request(
        "GET",
        f"/product/202309/products/{product_id}",
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def update_price(
    *,
    product_id: str,
    sku_id: str,
    currency: str,
    price: float,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Update SKU price.

    API: POST /product/202309/products/{product_id}/prices/update
    """

    body = {
        "skus": [
            {
                "id": sku_id,
                "price": {"currency": currency, "amount": str(price)},
            }
        ]
    }

    return tiktok_request(
        "POST",
        f"/product/202309/products/{product_id}/prices/update",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def update_inventory(
    *,
    product_id: str,
    sku_id: str,
    warehouse_id: str,
    quantity: int,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Update SKU inventory.

    API: POST /product/202309/products/{product_id}/inventory/update
    """

    body = {
        "skus": [
            {
                "id": sku_id,
                "inventory": [
                    {
                        "warehouse_id": warehouse_id,
                        "quantity": int(quantity),
                    }
                ],
            }
        ]
    }

    return tiktok_request(
        "POST",
        f"/product/202309/products/{product_id}/inventory/update",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )
