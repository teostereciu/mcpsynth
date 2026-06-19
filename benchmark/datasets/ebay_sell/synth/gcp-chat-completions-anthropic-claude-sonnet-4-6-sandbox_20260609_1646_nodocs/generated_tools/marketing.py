"""
eBay Sell Marketing API tools.
Covers: ad campaigns (Promoted Listings), promotions, item promotions,
        promotion reports, ad reports.
"""

from typing import Optional
from auth import api_get, api_post, api_put, api_delete


# ---------------------------------------------------------------------------
# Ad Campaigns (Promoted Listings)
# ---------------------------------------------------------------------------

def get_campaigns(
    campaign_name: Optional[str] = None,
    campaign_status: Optional[str] = None,
    end_date_range: Optional[str] = None,
    start_date_range: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """Get all Promoted Listings ad campaigns."""
    params: dict = {"limit": limit, "offset": offset}
    if campaign_name:
        params["campaign_name"] = campaign_name
    if campaign_status:
        params["campaign_status"] = campaign_status
    if end_date_range:
        params["end_date_range"] = end_date_range
    if start_date_range:
        params["start_date_range"] = start_date_range
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    return api_get("/sell/marketing/v1/ad_campaign", params=params)


def get_campaign(campaign_id: str) -> dict:
    """Get a Promoted Listings campaign by ID."""
    return api_get(f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def get_campaign_by_name(campaign_name: str) -> dict:
    """Get a campaign by name."""
    return api_get("/sell/marketing/v1/ad_campaign/get_campaign_by_name",
                   params={"campaign_name": campaign_name})


def create_campaign(body: dict) -> dict:
    """
    Create a Promoted Listings campaign.

    body fields:
      campaignName: str
      marketplaceId: str
      startDate: ISO 8601 str
      endDate: ISO 8601 str (optional)
      fundingStrategy: dict with bidPercentage and fundingModel
      campaignCriterion: dict (optional, for smart targeting)
    """
    return api_post("/sell/marketing/v1/ad_campaign", body=body)


def update_campaign_identification(campaign_id: str, body: dict) -> dict:
    """Update the name and/or start/end dates of a campaign."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_identification",
                    body=body)


def update_campaign_budget(campaign_id: str, body: dict) -> dict:
    """Update the budget of a campaign."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_budget",
                    body=body)


def pause_campaign(campaign_id: str) -> dict:
    """Pause an active campaign."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/pause")


def resume_campaign(campaign_id: str) -> dict:
    """Resume a paused campaign."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/resume")


def end_campaign(campaign_id: str) -> dict:
    """End (permanently stop) a campaign."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/end")


def delete_campaign(campaign_id: str) -> dict:
    """Delete a campaign."""
    return api_delete(f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def clone_campaign(campaign_id: str, body: dict) -> dict:
    """
    Clone an existing campaign.

    body fields:
      campaignName: str
      startDate: str
      endDate: str (optional)
    """
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/clone", body=body)


# ---------------------------------------------------------------------------
# Ads (within campaigns)
# ---------------------------------------------------------------------------

def get_ads(campaign_id: str, limit: int = 25, offset: int = 0,
            listing_ids: Optional[str] = None) -> dict:
    """Get all ads in a campaign."""
    params: dict = {"limit": limit, "offset": offset}
    if listing_ids:
        params["listing_ids"] = listing_ids
    return api_get(f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", params=params)


def get_ad(campaign_id: str, ad_id: str) -> dict:
    """Get a specific ad within a campaign."""
    return api_get(f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


def create_ads_by_listing_id(campaign_id: str, body: dict) -> dict:
    """
    Create ads for specific listing IDs within a campaign.

    body fields:
      listingIds: list of str
      bidPercentage: str (e.g. "5.0")
    """
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/create_ads_by_listing_id",
                    body=body)


def create_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Create ads by inventory reference (SKU/group key)."""
    return api_post(
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/create_ads_by_inventory_reference",
        body=body,
    )


def update_bid(campaign_id: str, ad_id: str, body: dict) -> dict:
    """Update the bid percentage for an ad."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid",
                    body=body)


def delete_ad(campaign_id: str, ad_id: str) -> dict:
    """Delete an ad from a campaign."""
    return api_delete(f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


def bulk_create_ads_by_listing_id(campaign_id: str, requests_list: list) -> dict:
    """Bulk create ads by listing IDs."""
    return api_post(
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id",
        body={"requests": requests_list},
    )


def bulk_delete_ads_by_listing_id(campaign_id: str, requests_list: list) -> dict:
    """Bulk delete ads by listing IDs."""
    return api_post(
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id",
        body={"requests": requests_list},
    )


def bulk_update_ads_bid_by_listing_id(campaign_id: str, requests_list: list) -> dict:
    """Bulk update ad bids by listing IDs."""
    return api_post(
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id",
        body={"requests": requests_list},
    )


# ---------------------------------------------------------------------------
# Promotions
# ---------------------------------------------------------------------------

def get_promotions(
    marketplace_id: str,
    promotion_status: Optional[str] = None,
    promotion_type: Optional[str] = None,
    q: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = 200,
    offset: int = 0,
) -> dict:
    """Get all promotions for a marketplace."""
    params: dict = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if promotion_status:
        params["promotion_status"] = promotion_status
    if promotion_type:
        params["promotion_type"] = promotion_type
    if q:
        params["q"] = q
    if sort:
        params["sort"] = sort
    return api_get("/sell/marketing/v1/promotion", params=params)


def get_promotion(promotion_id: str) -> dict:
    """Get a promotion by ID."""
    return api_get(f"/sell/marketing/v1/promotion/{promotion_id}")


def get_promotion_reports(
    marketplace_id: str,
    promotion_status: Optional[str] = None,
    promotion_type: Optional[str] = None,
    limit: int = 200,
    offset: int = 0,
) -> dict:
    """Get promotion performance reports."""
    params: dict = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if promotion_status:
        params["promotion_status"] = promotion_status
    if promotion_type:
        params["promotion_type"] = promotion_type
    return api_get("/sell/marketing/v1/promotion_report", params=params)


def get_promotion_summary_report(marketplace_id: str) -> dict:
    """Get a summary report of all promotions for a marketplace."""
    return api_get("/sell/marketing/v1/promotion_summary_report",
                   params={"marketplace_id": marketplace_id})


# ---------------------------------------------------------------------------
# Item Promotions (Threshold / Order-level)
# ---------------------------------------------------------------------------

def create_item_promotion(body: dict) -> dict:
    """
    Create an item promotion (e.g. CODED_COUPON, MARKDOWN_SALE, ORDER_DISCOUNT,
    VOLUME_DISCOUNT).

    body fields:
      marketplaceId: str
      name: str
      promotionType: str
      startDate: str
      endDate: str
      status: str ("DRAFT" or "SCHEDULED")
      description: str
      discountRules: list of dicts
      inventoryCriterion: dict
      couponCode: str (for CODED_COUPON)
    """
    return api_post("/sell/marketing/v1/item_promotion", body=body)


def update_item_promotion(promotion_id: str, body: dict) -> dict:
    """Update an item promotion."""
    return api_put(f"/sell/marketing/v1/item_promotion/{promotion_id}", body=body)


def delete_item_promotion(promotion_id: str) -> dict:
    """Delete an item promotion."""
    return api_delete(f"/sell/marketing/v1/item_promotion/{promotion_id}")


def get_item_promotion(promotion_id: str) -> dict:
    """Get an item promotion by ID."""
    return api_get(f"/sell/marketing/v1/item_promotion/{promotion_id}")


def pause_promotion(promotion_id: str) -> dict:
    """Pause an active promotion."""
    return api_post(f"/sell/marketing/v1/promotion/{promotion_id}/pause")


def resume_promotion(promotion_id: str) -> dict:
    """Resume a paused promotion."""
    return api_post(f"/sell/marketing/v1/promotion/{promotion_id}/resume")


# ---------------------------------------------------------------------------
# Ad Reports
# ---------------------------------------------------------------------------

def get_ad_report_tasks(
    report_task_statuses: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """Get all ad report tasks."""
    params: dict = {"limit": limit, "offset": offset}
    if report_task_statuses:
        params["report_task_statuses"] = report_task_statuses
    return api_get("/sell/marketing/v1/ad_report_task", params=params)


def get_ad_report_task(report_task_id: str) -> dict:
    """Get a specific ad report task."""
    return api_get(f"/sell/marketing/v1/ad_report_task/{report_task_id}")


def create_ad_report_task(body: dict) -> dict:
    """
    Create an ad report task.

    body fields:
      reportType: str (e.g. "ACCOUNT_PERFORMANCE_REPORT", "CAMPAIGN_PERFORMANCE_REPORT")
      campaignIds: list of str
      dateFrom: str
      dateTo: str
      dimensions: list of dicts with dimensionKey
      metrics: list of dicts with key
      marketplaceId: str
    """
    return api_post("/sell/marketing/v1/ad_report_task", body=body)


def delete_ad_report_task(report_task_id: str) -> dict:
    """Delete an ad report task."""
    return api_delete(f"/sell/marketing/v1/ad_report_task/{report_task_id}")


def get_ad_report(report_id: str) -> dict:
    """Download a completed ad report by report ID."""
    return api_get(f"/sell/marketing/v1/ad_report/{report_id}")


def get_ad_report_metadata() -> dict:
    """Get metadata about available ad report types and their dimensions/metrics."""
    return api_get("/sell/marketing/v1/ad_report_metadata")
