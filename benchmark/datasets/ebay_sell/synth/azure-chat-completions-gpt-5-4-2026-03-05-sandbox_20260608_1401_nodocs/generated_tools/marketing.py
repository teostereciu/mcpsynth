from typing import Any, Dict, Optional

from generated_tools.common import client


def get_campaigns(marketplace_id: str, campaign_status: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    params: Dict[str, Any] = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if campaign_status is not None:
        params["campaign_status"] = campaign_status
    return client.request("GET", "/sell/marketing/v1/ad_campaign", params=params)


def create_campaign(campaign_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/marketing/v1/ad_campaign", json_body=campaign_payload)


def get_campaign(campaign_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def update_campaign(campaign_id: str, campaign_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}", json_body=campaign_payload)


def delete_campaign(campaign_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def get_ads(campaign_id: str, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", params={"limit": limit, "offset": offset})


def create_ads(campaign_id: str, ads_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id", json_body=ads_payload)


def update_bids(campaign_id: str, bids_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid", json_body=bids_payload)
