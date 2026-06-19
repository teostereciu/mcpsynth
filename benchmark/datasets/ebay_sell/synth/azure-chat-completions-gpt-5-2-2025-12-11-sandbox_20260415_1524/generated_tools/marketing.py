from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_campaigns(
    *,
    campaign_name: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /ad_campaign"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if campaign_name is not None:
        params["campaign_name"] = campaign_name
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    return client.request("GET", "/sell/marketing/v1/ad_campaign", params=params or None)


def get_campaign(campaign_id: str) -> Dict[str, Any]:
    """GET /ad_campaign/{campaign_id}"""
    client = EbayClient()
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def create_ad_group(campaign_id: str, ad_group: Dict[str, Any]) -> Dict[str, Any]:
    """POST /ad_campaign/{campaign_id}/ad_group"""
    client = EbayClient()
    return client.request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group",
        json=ad_group,
        content_type="application/json",
    )


def get_ad_groups(campaign_id: str, *, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /ad_campaign/{campaign_id}/ad_group"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    return client.request(
        "GET",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group",
        params=params or None,
    )
