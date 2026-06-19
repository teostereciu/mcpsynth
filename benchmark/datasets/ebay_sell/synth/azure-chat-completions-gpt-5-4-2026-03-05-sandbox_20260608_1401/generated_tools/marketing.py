from typing import Any, Optional

from .common import client

API_PATH = "/sell/marketing/v1"


def get_campaigns(
    campaign_name: Optional[str] = None,
    campaign_status: Optional[str] = None,
    campaign_targeting_types: Optional[str] = None,
    channels: Optional[str] = None,
    end_date_range: Optional[str] = None,
    funding_strategy: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    start_date_range: Optional[str] = None,
) -> Any:
    return client.request(
        API_PATH,
        "GET",
        "/ad_campaign",
        params={
            "campaign_name": campaign_name,
            "campaign_status": campaign_status,
            "campaign_targeting_types": campaign_targeting_types,
            "channels": channels,
            "end_date_range": end_date_range,
            "funding_strategy": funding_strategy,
            "limit": limit,
            "offset": offset,
            "start_date_range": start_date_range,
        },
    )


def create_ad_by_listing_id(campaign_id: str, body: dict) -> Any:
    return client.request(
        API_PATH,
        "POST",
        f"/ad_campaign/{campaign_id}/ad",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )


def bulk_create_ads_by_listing_id(campaign_id: str, body: dict) -> Any:
    return client.request(
        API_PATH,
        "POST",
        f"/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )
