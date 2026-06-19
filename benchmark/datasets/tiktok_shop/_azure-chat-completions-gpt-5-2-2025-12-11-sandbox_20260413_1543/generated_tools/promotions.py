"""Promotions domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .client import TikTokShopClient


def create_activity(
    *,
    title: str,
    activity_type: str,
    product_level: str,
    begin_time: int,
    end_time: int,
    duration_type: Optional[str] = None,
    participation_limit: Optional[list] = None,
    discount: Optional[dict] = None,
    target_user_info: Optional[dict] = None,
    shop_cipher: Optional[str] = None,
    **extra_fields: Any,
) -> Dict[str, Any]:
    """POST /promotion/202309/activities"""

    client = TikTokShopClient.from_env()
    body: Dict[str, Any] = {
        "title": title,
        "activity_type": activity_type,
        "product_level": product_level,
        "begin_time": begin_time,
        "end_time": end_time,
    }
    if duration_type is not None:
        body["duration_type"] = duration_type
    if participation_limit is not None:
        body["participation_limit"] = participation_limit
    if discount is not None:
        body["discount"] = discount
    if target_user_info is not None:
        body["target_user_info"] = target_user_info
    body.update({k: v for k, v in extra_fields.items() if v is not None})

    return client.request(
        "POST",
        "/promotion/202309/activities",
        params={"shop_cipher": shop_cipher},
        body=body,
        use_shop_cipher=True,
    )
