from typing import Any, Dict, Optional

from .ebay_client import EbayClient, omit_none


client = EbayClient()


def marketing_get_campaigns(
    marketplace_id: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params = omit_none({"marketplace_id": marketplace_id, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/marketing/v1/ad_campaign", params=params)


def marketing_get_campaign(campaign_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def marketing_create_campaign(campaign: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/marketing/v1/ad_campaign", json_body=campaign)


def marketing_update_campaign(campaign_id: str, campaign: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}", json_body=campaign)


def marketing_delete_campaign(campaign_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def marketing_get_promotions(
    marketplace_id: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params = omit_none({"marketplace_id": marketplace_id, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/marketing/v1/promotion", params=params)


def marketing_get_promotion(promotion_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/marketing/v1/promotion/{promotion_id}")


def marketing_create_promotion(promotion: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/marketing/v1/promotion", json_body=promotion)


def marketing_update_promotion(promotion_id: str, promotion: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/marketing/v1/promotion/{promotion_id}", json_body=promotion)


def marketing_delete_promotion(promotion_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/marketing/v1/promotion/{promotion_id}")
