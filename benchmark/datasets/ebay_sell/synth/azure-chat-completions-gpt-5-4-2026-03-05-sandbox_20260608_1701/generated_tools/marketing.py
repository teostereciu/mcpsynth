from typing import Any, Optional

from generated_tools.ebay_common import client


def get_campaigns(
    campaign_name: Optional[str] = None,
    campaign_status: Optional[str] = None,
    campaign_targeting_types: Optional[str] = None,
    channels: Optional[str] = None,
    end_date_range: Optional[str] = None,
    funding_strategy: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
    start_date_range: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/ad_campaign",
        api_group="marketing",
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


def get_campaign(campaign_id: str) -> Any:
    return client.request("GET", f"/ad_campaign/{campaign_id}", api_group="marketing")
