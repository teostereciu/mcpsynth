from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def marketing_get_campaigns(
    marketplace_id: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /sell/marketing/v1/ad_campaign"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if marketplace_id is not None:
        params["marketplace_id"] = marketplace_id
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return c.request("GET", "/sell/marketing/v1/ad_campaign", params=params)


def marketing_get_campaign(campaign_id: str) -> Dict[str, Any]:
    """GET /sell/marketing/v1/ad_campaign/{campaignId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def marketing_create_campaign(campaign: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/marketing/v1/ad_campaign"""
    c = EbayClient()
    return c.request("POST", "/sell/marketing/v1/ad_campaign", json=campaign)


def marketing_update_campaign(campaign_id: str, campaign: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/marketing/v1/ad_campaign/{campaignId}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}", json=campaign)


def marketing_delete_campaign(campaign_id: str) -> Dict[str, Any]:
    """DELETE /sell/marketing/v1/ad_campaign/{campaignId}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def marketing_get_promotions(
    marketplace_id: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /sell/marketing/v1/promotion"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if marketplace_id is not None:
        params["marketplace_id"] = marketplace_id
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return c.request("GET", "/sell/marketing/v1/promotion", params=params)


def marketing_get_promotion(promotion_id: str) -> Dict[str, Any]:
    """GET /sell/marketing/v1/promotion/{promotionId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/marketing/v1/promotion/{promotion_id}")


def marketing_create_promotion(promotion: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/marketing/v1/promotion"""
    c = EbayClient()
    return c.request("POST", "/sell/marketing/v1/promotion", json=promotion)


def marketing_update_promotion(promotion_id: str, promotion: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/marketing/v1/promotion/{promotionId}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/marketing/v1/promotion/{promotion_id}", json=promotion)


def marketing_delete_promotion(promotion_id: str) -> Dict[str, Any]:
    """DELETE /sell/marketing/v1/promotion/{promotionId}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/marketing/v1/promotion/{promotion_id}")
