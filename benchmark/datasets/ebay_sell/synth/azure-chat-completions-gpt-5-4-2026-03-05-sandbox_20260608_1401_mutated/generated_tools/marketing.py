from typing import Any, Dict, Optional
from urllib.parse import quote

from generated_tools.common import clean_params, client


def get_campaigns(
    campaign_title: Optional[str] = None,
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
        "GET",
        "/sell/marketing/v1/ad_campaign",
        params=clean_params(
            campaign_title=campaign_title,
            campaign_status=campaign_status,
            campaign_targeting_types=campaign_targeting_types,
            channels=channels,
            end_date_range=end_date_range,
            funding_strategy=funding_strategy,
            limit=limit,
            offset=offset,
            start_date_range=start_date_range,
        ),
    )


def get_campaign(campaign_id: str) -> Any:
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{quote(campaign_id, safe='')}")


def clone_campaign(campaign_id: str, body: Dict[str, Any]) -> Any:
    return client.request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{quote(campaign_id, safe='')}/clone",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )
