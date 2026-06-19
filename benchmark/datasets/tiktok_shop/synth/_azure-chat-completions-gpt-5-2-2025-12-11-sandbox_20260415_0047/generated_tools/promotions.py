from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .http import tiktok_request


@mcp.tool()
def promotions_create_activity_direct_discount(
    title: str,
    start_time: int,
    end_time: int,
    discount_percentage: int,
    product_ids: list[str],
) -> Dict[str, Any]:
    """Create a DIRECT_DISCOUNT activity.

    API: POST /promotion/202309/activities
    """

    body: Dict[str, Any] = {
        "activity_type": "DIRECT_DISCOUNT",
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "discount_percentage": discount_percentage,
        "product_ids": product_ids,
    }
    return tiktok_request("POST", "/promotion/202309/activities", body=body)


@mcp.tool()
def promotions_get_activity(activity_id: str) -> Dict[str, Any]:
    """Get activity detail.

    API: GET /promotion/202309/activities/{activity_id}
    """

    return tiktok_request("GET", f"/promotion/202309/activities/{activity_id}")


@mcp.tool()
def promotions_search_activities(page_size: int = 20, page_token: str | None = None) -> Dict[str, Any]:
    """Search promotion activities.

    API: GET /promotion/202309/activities
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/promotion/202309/activities", params=params)
