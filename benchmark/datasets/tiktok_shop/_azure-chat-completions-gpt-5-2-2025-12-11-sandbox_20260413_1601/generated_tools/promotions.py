"""Promotions domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import TikTokRequestOptions, tiktok_request


def create_activity(
    *,
    title: str,
    activity_type: str,
    product_level: str = "PRODUCT",
    begin_time: int,
    end_time: int,
    discount_percentage: Optional[int] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a promotion activity.

    API: POST /promotion/202309/activities

    This tool focuses on DIRECT_DISCOUNT percentage-off activities.
    """

    body: Dict[str, Any] = {
        "title": title,
        "activity_type": activity_type,
        "product_level": product_level,
        "duration_type": "NORMAL",
        "begin_time": int(begin_time),
        "end_time": int(end_time),
        "participation_limit": [{"type": "BUYER_NO_LIMIT"}],
    }

    if activity_type == "DIRECT_DISCOUNT" and discount_percentage is not None:
        body["discount"] = {
            "bmsm_discount": None,
        }
        # The API expects discount config depending on activity_type; for DIRECT_DISCOUNT
        # the discount is configured when adding products/SKUs via Update Activity Product.
        # Some regions allow setting discount here; keep minimal and rely on update_activity_product.

    return tiktok_request(
        "POST",
        "/promotion/202309/activities",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def update_activity_product(
    *,
    activity_id: str,
    product_id: str,
    discount_percentage: int,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Add/update a product in an activity with percentage discount.

    API: POST /promotion/202309/activities/{activity_id}/products

    Note: Endpoint name inferred from docs title "Update Activity Product".
    """

    body = {
        "products": [
            {
                "product_id": product_id,
                "direct_discount": {"percentage": int(discount_percentage)},
            }
        ]
    }

    return tiktok_request(
        "POST",
        f"/promotion/202309/activities/{activity_id}/products",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )
