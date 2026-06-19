"""Products domain tools (catalog, categories, attributes, pricing, inventory)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .client import TikTokShopClient


def create_product(
    *,
    save_mode: str = "LISTING",
    title: str,
    description: str,
    category_id: str,
    main_images: List[Dict[str, Any]],
    skus: List[Dict[str, Any]],
    brand_id: Optional[str] = None,
    shop_cipher: Optional[str] = None,
    **extra_fields: Any,
) -> Dict[str, Any]:
    """POST /product/202309/products

    This tool is a thin wrapper; pass fields as documented by TikTok.
    """

    client = TikTokShopClient.from_env()
    body: Dict[str, Any] = {
        "save_mode": save_mode,
        "title": title,
        "description": description,
        "category_id": category_id,
        "main_images": main_images,
        "skus": skus,
    }
    if brand_id is not None:
        body["brand_id"] = brand_id
    body.update({k: v for k, v in extra_fields.items() if v is not None})

    return client.request(
        "POST",
        "/product/202309/products",
        params={"shop_cipher": shop_cipher},
        body=body,
        use_shop_cipher=True,
    )


def update_price(
    *,
    product_id: str,
    skus: List[Dict[str, Any]],
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /product/202309/products/{product_id}/prices/update"""

    client = TikTokShopClient.from_env()
    body = {"skus": skus}
    return client.request(
        "POST",
        f"/product/202309/products/{product_id}/prices/update",
        params={"shop_cipher": shop_cipher},
        body=body,
        use_shop_cipher=True,
    )


def update_inventory(
    *,
    product_id: str,
    skus: List[Dict[str, Any]],
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /product/202309/products/{product_id}/inventory/update"""

    client = TikTokShopClient.from_env()
    body = {"skus": skus}
    return client.request(
        "POST",
        f"/product/202309/products/{product_id}/inventory/update",
        params={"shop_cipher": shop_cipher},
        body=body,
        use_shop_cipher=True,
    )


def get_product(
    *,
    product_id: str,
    return_under_review_version: Optional[bool] = None,
    return_draft_version: Optional[bool] = None,
    locale: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /product/202309/products/{product_id}"""

    client = TikTokShopClient.from_env()
    params: Dict[str, Any] = {
        "return_under_review_version": return_under_review_version,
        "return_draft_version": return_draft_version,
        "locale": locale,
        "shop_cipher": shop_cipher,
    }
    return client.request(
        "GET",
        f"/product/202309/products/{product_id}",
        params=params,
        use_shop_cipher=True,
    )


def search_products(
    *,
    page_size: int = 20,
    page_token: Optional[str] = None,
    status: Optional[str] = None,
    seller_skus: Optional[List[str]] = None,
    category_version: Optional[str] = None,
    audit_status: Optional[List[str]] = None,
    sku_ids: Optional[List[str]] = None,
    return_draft_version: Optional[bool] = None,
    shop_cipher: Optional[str] = None,
    **extra_filters: Any,
) -> Dict[str, Any]:
    """POST /product/202502/products/search"""

    client = TikTokShopClient.from_env()
    params: Dict[str, Any] = {"page_size": page_size, "page_token": page_token, "shop_cipher": shop_cipher}
    body: Dict[str, Any] = {}
    if status is not None:
        body["status"] = status
    if seller_skus is not None:
        body["seller_skus"] = seller_skus
    if category_version is not None:
        body["category_version"] = category_version
    if audit_status is not None:
        body["audit_status"] = audit_status
    if sku_ids is not None:
        body["sku_ids"] = sku_ids
    if return_draft_version is not None:
        body["return_draft_version"] = return_draft_version
    body.update({k: v for k, v in extra_filters.items() if v is not None})

    return client.request(
        "POST",
        "/product/202502/products/search",
        params=params,
        body=body,
        use_shop_cipher=True,
    )


def get_categories(
    *,
    locale: Optional[str] = None,
    keyword: Optional[str] = None,
    category_version: Optional[str] = None,
    listing_platform: Optional[str] = None,
    include_prohibited_categories: Optional[bool] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /product/202309/categories"""

    client = TikTokShopClient.from_env()
    params: Dict[str, Any] = {
        "locale": locale,
        "keyword": keyword,
        "category_version": category_version,
        "listing_platform": listing_platform,
        "include_prohibited_categories": include_prohibited_categories,
        "shop_cipher": shop_cipher,
    }
    return client.request("GET", "/product/202309/categories", params=params, use_shop_cipher=True)
