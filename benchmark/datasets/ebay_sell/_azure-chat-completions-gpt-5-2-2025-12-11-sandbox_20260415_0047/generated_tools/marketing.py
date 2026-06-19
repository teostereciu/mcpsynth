from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/marketing/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.marketing"


def register(mcp):
    # Campaigns
    @mcp.tool()
    def marketing_get_campaigns(
        *,
        campaign_name: Optional[str] = None,
        campaign_status: Optional[str] = None,
        campaign_targeting_types: Optional[str] = None,
        channels: Optional[str] = None,
        end_date_range: Optional[str] = None,
        funding_strategy: Optional[str] = None,
        start_date_range: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /ad_campaign - Get campaigns."""
        params: Dict[str, Any] = {}
        if campaign_name is not None:
            params["campaign_name"] = campaign_name
        if campaign_status is not None:
            params["campaign_status"] = campaign_status
        if campaign_targeting_types is not None:
            params["campaign_targeting_types"] = campaign_targeting_types
        if channels is not None:
            params["channels"] = channels
        if end_date_range is not None:
            params["end_date_range"] = end_date_range
        if funding_strategy is not None:
            params["funding_strategy"] = funding_strategy
        if start_date_range is not None:
            params["start_date_range"] = start_date_range
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json("GET", API_ROOT, "/ad_campaign", scope=SCOPE, params=params or None)

    @mcp.tool()
    def marketing_get_campaign(campaign_id: str) -> Dict[str, Any]:
        """GET /ad_campaign/{campaign_id} - Get a campaign."""
        return request_json("GET", API_ROOT, f"/ad_campaign/{campaign_id}", scope=SCOPE)

    @mcp.tool()
    def marketing_get_campaign_by_name(campaign_name: str) -> Dict[str, Any]:
        """GET /ad_campaign/get_campaign_by_name - Get campaign by name."""
        return request_json(
            "GET",
            API_ROOT,
            "/ad_campaign/get_campaign_by_name",
            scope=SCOPE,
            params={"campaign_name": campaign_name},
        )

    @mcp.tool()
    def marketing_clone_campaign(campaign_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /ad_campaign/{campaign_id}/clone - Clone a campaign."""
        return request_json(
            "POST",
            API_ROOT,
            f"/ad_campaign/{campaign_id}/clone",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def marketing_delete_campaign(campaign_id: str) -> Dict[str, Any]:
        """DELETE /ad_campaign/{campaign_id} - Delete a campaign."""
        return request_json("DELETE", API_ROOT, f"/ad_campaign/{campaign_id}", scope=SCOPE)

    # Ads
    @mcp.tool()
    def marketing_create_ad_by_listing_id(campaign_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /ad_campaign/{campaign_id}/ad - Create an ad by listing ID."""
        return request_json(
            "POST",
            API_ROOT,
            f"/ad_campaign/{campaign_id}/ad",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def marketing_create_ads_by_inventory_reference(campaign_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /ad_campaign/{campaign_id}/create_ads_by_inventory_reference - Create ads by inventory reference."""
        return request_json(
            "POST",
            API_ROOT,
            f"/ad_campaign/{campaign_id}/create_ads_by_inventory_reference",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def marketing_get_ads(campaign_id: str, *, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """GET /ad_campaign/{campaign_id}/ad - Get ads."""
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json("GET", API_ROOT, f"/ad_campaign/{campaign_id}/ad", scope=SCOPE, params=params or None)

    @mcp.tool()
    def marketing_get_ad(campaign_id: str, ad_id: str) -> Dict[str, Any]:
        """GET /ad_campaign/{campaign_id}/ad/{ad_id} - Get an ad."""
        return request_json("GET", API_ROOT, f"/ad_campaign/{campaign_id}/ad/{ad_id}", scope=SCOPE)

    @mcp.tool()
    def marketing_delete_ad(campaign_id: str, ad_id: str) -> Dict[str, Any]:
        """DELETE /ad_campaign/{campaign_id}/ad/{ad_id} - Delete an ad."""
        return request_json("DELETE", API_ROOT, f"/ad_campaign/{campaign_id}/ad/{ad_id}", scope=SCOPE)

    @mcp.tool()
    def marketing_update_bid(campaign_id: str, ad_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /ad_campaign/{campaign_id}/ad/{ad_id}/update_bid - Update bid."""
        return request_json(
            "POST",
            API_ROOT,
            f"/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    # Bulk ads operations
    @mcp.tool()
    def marketing_bulk_create_ads_by_inventory_reference(campaign_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference"""
        return request_json(
            "POST",
            API_ROOT,
            f"/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def marketing_bulk_delete_ads_by_inventory_reference(campaign_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference"""
        return request_json(
            "POST",
            API_ROOT,
            f"/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def marketing_bulk_update_ads_bid_by_inventory_reference(campaign_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference"""
        return request_json(
            "POST",
            API_ROOT,
            f"/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def marketing_bulk_update_ads_status(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /bulk_update_ads_status - Bulk update ads status."""
        return request_json(
            "POST",
            API_ROOT,
            "/bulk_update_ads_status",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    # Suggestions
    @mcp.tool()
    def marketing_suggest_budget(*, marketplace_id: Optional[str] = None, category_id: Optional[str] = None) -> Dict[str, Any]:
        """GET /ad_campaign/suggest_budget - Suggest budget."""
        params: Dict[str, Any] = {}
        if marketplace_id is not None:
            params["marketplace_id"] = marketplace_id
        if category_id is not None:
            params["category_id"] = category_id
        return request_json("GET", API_ROOT, "/ad_campaign/suggest_budget", scope=SCOPE, params=params or None)
