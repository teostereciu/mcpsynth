from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_MARKETING
from . import mcp

API = "/sell/marketing/v1"


@mcp.tool()
def marketing_get_campaigns(
    *,
    campaign_name: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /ad_campaign"""
    params: Dict[str, Any] = {}
    if campaign_name is not None:
        params["campaign_name"] = campaign_name
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/ad_campaign",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        params=params or None,
    )


@mcp.tool()
def marketing_get_campaign(campaign_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /ad_campaign/{campaign_id}"""
    return _shared.client.request(
        "GET",
        API,
        f"/ad_campaign/{campaign_id}",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def marketing_get_campaign_by_name(
    campaign_name: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /ad_campaign/get_campaign_by_name"""
    return _shared.client.request(
        "GET",
        API,
        "/ad_campaign/get_campaign_by_name",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        params={"campaign_name": campaign_name},
    )


@mcp.tool()
def marketing_create_campaign(
    campaign: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /ad_campaign"""
    return _shared.client.request(
        "POST",
        API,
        "/ad_campaign",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        json=campaign,
    )


@mcp.tool()
def marketing_delete_campaign(campaign_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """DELETE /ad_campaign/{campaign_id}"""
    return _shared.client.request(
        "DELETE",
        API,
        f"/ad_campaign/{campaign_id}",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def marketing_clone_campaign(
    campaign_id: str,
    clone_request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /ad_campaign/{campaign_id}/clone"""
    return _shared.client.request(
        "POST",
        API,
        f"/ad_campaign/{campaign_id}/clone",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        json=clone_request,
    )


@mcp.tool()
def marketing_create_ads_by_inventory_reference(
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference

    campaign_id should be included in request payload per docs in this repo.
    """
    # Some docs use /ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference
    campaign_id = request.get("campaign_id") or request.get("campaignId")
    if not campaign_id:
        return {"error": "campaign_id is required in request"}
    return _shared.client.request(
        "POST",
        API,
        f"/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        json=request,
    )


@mcp.tool()
def marketing_bulk_create_ads_by_inventory_reference(
    campaign_id: str,
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference"""
    return _shared.client.request(
        "POST",
        API,
        f"/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        json=request,
    )


@mcp.tool()
def marketing_bulk_update_ads_bid_by_inventory_reference(
    campaign_id: str,
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference"""
    return _shared.client.request(
        "POST",
        API,
        f"/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        json=request,
    )


@mcp.tool()
def marketing_get_ads_by_inventory_reference(
    campaign_id: str,
    inventory_reference_id: str,
    inventory_reference_type: str = "INVENTORY_ITEM",
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /ad_campaign/{campaign_id}/get_ads_by_inventory_reference"""
    params = {
        "inventory_reference_id": inventory_reference_id,
        "inventory_reference_type": inventory_reference_type,
    }
    return _shared.client.request(
        "GET",
        API,
        f"/ad_campaign/{campaign_id}/get_ads_by_inventory_reference",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        params=params,
    )


@mcp.tool()
def marketing_create_ad_group(
    campaign_id: str,
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /ad_campaign/{campaign_id}/ad_group"""
    return _shared.client.request(
        "POST",
        API,
        f"/ad_campaign/{campaign_id}/ad_group",
        scope=SCOPE_MARKETING,
        marketplace_id=marketplace_id,
        json=request,
    )
