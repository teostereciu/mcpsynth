from typing import Any, Dict, Optional

from .client import TikTokShopClient


def create_product_202309(
    client: TikTokShopClient,
    *,
    product: Dict[str, Any],
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Create Product (202309).

    Path: /product/202309/products
    Method: POST

    Args:
      product: Full request body per docs (save_mode, description, category_id, brand_id, main_images, skus, ...)
      shop_cipher: Override shop cipher.
    """
    return client.request(
        "POST",
        "/product/202309/products",
        body=product,
        shop_cipher=shop_cipher,
    )


def get_product_202309(
    client: TikTokShopClient,
    *,
    product_id: str,
    return_under_review_version: Optional[bool] = None,
    return_draft_version: Optional[bool] = None,
    locale: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get Product (202309).

    Path: /product/202309/products/{product_id}
    Method: GET
    """
    query: Dict[str, Any] = {}
    if return_under_review_version is not None:
        query["return_under_review_version"] = str(return_under_review_version).lower()
    if return_draft_version is not None:
        query["return_draft_version"] = str(return_draft_version).lower()
    if locale is not None:
        query["locale"] = locale

    return client.request(
        "GET",
        f"/product/202309/products/{product_id}",
        query=query,
        body=None,
        shop_cipher=shop_cipher,
    )
