from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def affiliate_get_partner_campaign_list(page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get affiliate partner campaign list.

    API: GET /affiliate_partner/202405/campaigns
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/affiliate_partner/202405/campaigns", params=params)


@mcp.tool()
def affiliate_generate_product_promotion_link(product_id: str) -> Dict[str, Any]:
    """Generate affiliate product promotion link.

    API: POST /affiliate_seller/202405/products/promotion_link/generate
    """

    body = {"product_id": product_id}
    return tiktok_request("POST", "/affiliate_seller/202405/products/promotion_link/generate", body=body)
