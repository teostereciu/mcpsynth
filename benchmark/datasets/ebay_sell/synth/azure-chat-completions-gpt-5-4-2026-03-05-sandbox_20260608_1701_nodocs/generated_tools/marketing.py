from typing import Any, Dict, Optional

from .common import client


def list_campaigns(marketplace_id: str = "EBAY_US", limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", "/sell/marketing/v1/ad_campaign", params={"marketplace_id": marketplace_id, "limit": limit, "offset": offset})


def create_campaign(data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/marketing/v1/ad_campaign", json_body=data)


def get_campaign(campaign_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def update_campaign(campaign_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}", json_body=data)


def delete_campaign(campaign_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def list_promoted_listings(campaign_id: str, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", params={"limit": limit, "offset": offset})


def create_promoted_listing(campaign_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", json_body=data)
