from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


def get_campaigns(
    *,
    campaign_name: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /ad_campaign

    Doc: docs/api_marketing_get-campaigns.md
    """
    c = client or EbayClient()
    params: Dict[str, str] = {}
    if campaign_name is not None:
        params["campaign_name"] = campaign_name
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    status, body, headers = c.request("GET", "/ad_campaign", params=params or None)
    return c.ok_or_error(status, body, headers)


def get_campaign(campaign_id: str, *, client: Optional[EbayClient] = None) -> Any:
    """GET /ad_campaign/{campaign_id}

    Doc: docs/api_marketing_get-campaign.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("GET", f"/ad_campaign/{campaign_id}")
    return c.ok_or_error(status, body, headers)


def create_ad_by_listing_id(
    campaign_id: str,
    ad: Dict[str, Any],
    *,
    client: Optional[EbayClient] = None,
) -> Any:
    """POST /ad_campaign/{campaign_id}/ad

    Doc: docs/api_marketing_create-ad-by-listing-id.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "POST",
        f"/ad_campaign/{campaign_id}/ad",
        json=ad,
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)


def delete_campaign(campaign_id: str, *, client: Optional[EbayClient] = None) -> Any:
    """DELETE /ad_campaign/{campaign_id}

    Doc: docs/api_marketing_delete-campaign.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("DELETE", f"/ad_campaign/{campaign_id}")
    return c.ok_or_error(status, body, headers)
