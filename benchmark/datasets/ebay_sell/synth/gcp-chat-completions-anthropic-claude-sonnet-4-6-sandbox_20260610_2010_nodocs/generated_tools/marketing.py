"""
eBay Sell Marketing API tools.
Covers: ad campaigns (Promoted Listings), promotions, item promotions,
        promotion reports, and campaign reports.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post, api_put, api_delete, api_patch

mcp = FastMCP("ebay-marketing")


# ── Ad Campaigns ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_campaigns(campaign_name: str | None = None,
                  campaign_status: str | None = None,
                  end_date_range: str | None = None,
                  start_date_range: str | None = None,
                  limit: int = 10,
                  offset: int = 0) -> dict:
    """
    Retrieve Promoted Listings ad campaigns.

    Args:
        campaign_name: Filter by campaign name (partial match).
        campaign_status: Filter by status (RUNNING, PAUSED, ENDED, etc.).
        end_date_range: Date range filter for campaign end date.
        start_date_range: Date range filter for campaign start date.
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if campaign_name:
        params["campaign_name"] = campaign_name
    if campaign_status:
        params["campaign_status"] = campaign_status
    if end_date_range:
        params["end_date_range"] = end_date_range
    if start_date_range:
        params["start_date_range"] = start_date_range
    return api_get("/sell/marketing/v1/ad_campaign", params=params)


@mcp.tool()
def get_campaign(campaign_id: str) -> dict:
    """Retrieve a single ad campaign by ID."""
    return api_get(f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def get_campaign_by_name(campaign_name: str) -> dict:
    """Retrieve a campaign by its name."""
    return api_get("/sell/marketing/v1/ad_campaign/get_campaign_by_name",
                   params={"campaign_name": campaign_name})


@mcp.tool()
def create_campaign(campaign_name: str, start_date: str,
                    funding_strategy: dict,
                    marketplace_id: str,
                    end_date: str | None = None) -> dict:
    """
    Create a new Promoted Listings ad campaign.

    Args:
        campaign_name: Name for the campaign.
        start_date: ISO 8601 campaign start date.
        funding_strategy: Dict with bidPercentage and fundingModel.
        marketplace_id: eBay marketplace ID (e.g. EBAY_US).
        end_date: Optional ISO 8601 campaign end date.
    """
    body: dict = {
        "campaignName": campaign_name,
        "startDate": start_date,
        "fundingStrategy": funding_strategy,
        "marketplaceId": marketplace_id,
    }
    if end_date:
        body["endDate"] = end_date
    return api_post("/sell/marketing/v1/ad_campaign", body=body)


@mcp.tool()
def update_campaign_identification(campaign_id: str,
                                    campaign_name: str,
                                    start_date: str,
                                    end_date: str | None = None) -> dict:
    """
    Update the name and dates of a campaign.

    Args:
        campaign_id: Campaign ID to update.
        campaign_name: New campaign name.
        start_date: New start date (ISO 8601).
        end_date: New end date (ISO 8601), or None for no end.
    """
    body: dict = {"campaignName": campaign_name, "startDate": start_date}
    if end_date:
        body["endDate"] = end_date
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_identification",
                    body=body)


@mcp.tool()
def update_campaign_budget(campaign_id: str, daily_budget: dict) -> dict:
    """
    Update the daily budget of a campaign.

    Args:
        campaign_id: Campaign ID.
        daily_budget: Dict with value and currency (e.g. {"value": "10.00", "currency": "USD"}).
    """
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_budget",
                    body={"dailyBudget": daily_budget})


@mcp.tool()
def pause_campaign(campaign_id: str) -> dict:
    """Pause a running ad campaign."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/pause")


@mcp.tool()
def resume_campaign(campaign_id: str) -> dict:
    """Resume a paused ad campaign."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/resume")


@mcp.tool()
def end_campaign(campaign_id: str) -> dict:
    """End (permanently stop) an ad campaign."""
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/end")


@mcp.tool()
def delete_campaign(campaign_id: str) -> dict:
    """Delete an ad campaign."""
    return api_delete(f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def clone_campaign(campaign_id: str, campaign_name: str,
                   start_date: str, end_date: str | None = None) -> dict:
    """
    Clone an existing campaign.

    Args:
        campaign_id: Source campaign ID.
        campaign_name: Name for the cloned campaign.
        start_date: Start date for the clone.
        end_date: Optional end date for the clone.
    """
    body: dict = {"campaignName": campaign_name, "startDate": start_date}
    if end_date:
        body["endDate"] = end_date
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/clone", body=body)


# ── Ads (within campaigns) ───────────────────────────────────────────────────

@mcp.tool()
def get_ads(campaign_id: str, limit: int = 25, offset: int = 0,
            listing_ids: str | None = None) -> dict:
    """
    Retrieve ads within a campaign.

    Args:
        campaign_id: Campaign ID.
        limit: Results per page.
        offset: Pagination offset.
        listing_ids: Comma-separated listing IDs to filter.
    """
    params: dict = {"limit": limit, "offset": offset}
    if listing_ids:
        params["listing_ids"] = listing_ids
    return api_get(f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", params=params)


@mcp.tool()
def get_ad(campaign_id: str, ad_id: str) -> dict:
    """Retrieve a single ad by campaign ID and ad ID."""
    return api_get(f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


@mcp.tool()
def create_ads_by_listing_id(campaign_id: str, ads: list[dict]) -> dict:
    """
    Create ads for specific listing IDs within a campaign.

    Args:
        campaign_id: Campaign ID.
        ads: List of ad objects each with listingId and bidPercentage.
    """
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id",
                    body={"requests": ads})


@mcp.tool()
def create_ads_by_inventory_reference(campaign_id: str, ads: list[dict]) -> dict:
    """
    Create ads by inventory reference (SKU/group key) within a campaign.

    Args:
        campaign_id: Campaign ID.
        ads: List of ad objects each with inventoryReferenceId, inventoryReferenceType, bidPercentage.
    """
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference",
                    body={"requests": ads})


@mcp.tool()
def delete_ads(campaign_id: str, ad_ids: list[str]) -> dict:
    """
    Bulk delete ads from a campaign.

    Args:
        campaign_id: Campaign ID.
        ad_ids: List of ad IDs to delete.
    """
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads",
                    body={"requests": [{"adId": aid} for aid in ad_ids]})


@mcp.tool()
def update_bids(campaign_id: str, ads: list[dict]) -> dict:
    """
    Bulk update bid percentages for ads in a campaign.

    Args:
        campaign_id: Campaign ID.
        ads: List of objects each with adId and bidPercentage.
    """
    return api_post(f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id",
                    body={"requests": ads})


# ── Item Promotions ──────────────────────────────────────────────────────────

@mcp.tool()
def get_promotions(marketplace_id: str,
                   promotion_status: str | None = None,
                   promotion_type: str | None = None,
                   limit: int = 200,
                   offset: int = 0,
                   q: str | None = None) -> dict:
    """
    Retrieve item promotions (sales, coupons, etc.).

    Args:
        marketplace_id: eBay marketplace ID.
        promotion_status: Filter by status (ACTIVE, DRAFT, SCHEDULED, ENDED, PAUSED).
        promotion_type: Filter by type (MARKDOWN_SALE, ORDER_DISCOUNT, VOLUME_DISCOUNT, CODED_COUPON).
        limit: Results per page.
        offset: Pagination offset.
        q: Search query string.
    """
    params: dict = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if promotion_status:
        params["promotion_status"] = promotion_status
    if promotion_type:
        params["promotion_type"] = promotion_type
    if q:
        params["q"] = q
    return api_get("/sell/marketing/v1/promotion", params=params)


@mcp.tool()
def get_promotion(promotion_id: str) -> dict:
    """Retrieve a single promotion by ID."""
    return api_get(f"/sell/marketing/v1/promotion/{promotion_id}")


@mcp.tool()
def get_promotion_reports(marketplace_id: str,
                           promotion_status: str | None = None,
                           promotion_type: str | None = None,
                           limit: int = 200,
                           offset: int = 0) -> dict:
    """
    Retrieve promotion performance reports.

    Args:
        marketplace_id: eBay marketplace ID.
        promotion_status: Filter by status.
        promotion_type: Filter by type.
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if promotion_status:
        params["promotion_status"] = promotion_status
    if promotion_type:
        params["promotion_type"] = promotion_type
    return api_get("/sell/marketing/v1/promotion_report", params=params)


@mcp.tool()
def get_promotion_summary_report(marketplace_id: str) -> dict:
    """
    Retrieve a summary report of all promotions for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID.
    """
    return api_get("/sell/marketing/v1/promotion_summary_report",
                   params={"marketplace_id": marketplace_id})


@mcp.tool()
def create_item_price_markdown_promotion(marketplace_id: str,
                                          name: str,
                                          start_date: str,
                                          end_date: str,
                                          selected_inventory_discounts: list[dict],
                                          description: str | None = None,
                                          priority: str | None = None) -> dict:
    """
    Create a markdown (sale price) promotion.

    Args:
        marketplace_id: eBay marketplace ID.
        name: Promotion name.
        start_date: ISO 8601 start date.
        end_date: ISO 8601 end date.
        selected_inventory_discounts: List of discount rule dicts.
        description: Optional description.
        priority: Optional priority (LOWEST_PRIORITY to HIGHEST_PRIORITY).
    """
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "startDate": start_date,
        "endDate": end_date,
        "selectedInventoryDiscounts": selected_inventory_discounts,
    }
    if description:
        body["description"] = description
    if priority:
        body["priority"] = priority
    return api_post("/sell/marketing/v1/item_price_markdown", body=body)


@mcp.tool()
def update_item_price_markdown_promotion(promotion_id: str,
                                          marketplace_id: str,
                                          name: str,
                                          start_date: str,
                                          end_date: str,
                                          selected_inventory_discounts: list[dict],
                                          description: str | None = None) -> dict:
    """Update an existing markdown promotion."""
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "startDate": start_date,
        "endDate": end_date,
        "selectedInventoryDiscounts": selected_inventory_discounts,
    }
    if description:
        body["description"] = description
    return api_put(f"/sell/marketing/v1/item_price_markdown/{promotion_id}", body=body)


@mcp.tool()
def delete_promotion(promotion_id: str) -> dict:
    """Delete a promotion by ID."""
    return api_delete(f"/sell/marketing/v1/promotion/{promotion_id}")


@mcp.tool()
def pause_promotion(promotion_id: str) -> dict:
    """Pause an active promotion."""
    return api_post(f"/sell/marketing/v1/promotion/{promotion_id}/pause")


@mcp.tool()
def resume_promotion(promotion_id: str) -> dict:
    """Resume a paused promotion."""
    return api_post(f"/sell/marketing/v1/promotion/{promotion_id}/resume")


@mcp.tool()
def create_item_promotion(marketplace_id: str, name: str,
                           promotion_type: str,
                           discount_rules: list[dict],
                           inventory_criterion: dict | None = None,
                           start_date: str | None = None,
                           end_date: str | None = None,
                           description: str | None = None,
                           coupon_code: str | None = None) -> dict:
    """
    Create an order-level or volume discount promotion.

    Args:
        marketplace_id: eBay marketplace ID.
        name: Promotion name.
        promotion_type: ORDER_DISCOUNT or VOLUME_DISCOUNT or CODED_COUPON.
        discount_rules: List of discount rule dicts.
        inventory_criterion: Optional inventory selection criteria.
        start_date: Optional ISO 8601 start date.
        end_date: Optional ISO 8601 end date.
        description: Optional description.
        coupon_code: Coupon code (for CODED_COUPON type).
    """
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "promotionType": promotion_type,
        "discountRules": discount_rules,
    }
    if inventory_criterion:
        body["inventoryCriterion"] = inventory_criterion
    if start_date:
        body["startDate"] = start_date
    if end_date:
        body["endDate"] = end_date
    if description:
        body["description"] = description
    if coupon_code:
        body["couponCode"] = coupon_code
    return api_post("/sell/marketing/v1/item_promotion", body=body)


@mcp.tool()
def update_item_promotion(promotion_id: str, marketplace_id: str,
                           name: str, promotion_type: str,
                           discount_rules: list[dict],
                           inventory_criterion: dict | None = None,
                           start_date: str | None = None,
                           end_date: str | None = None,
                           description: str | None = None) -> dict:
    """Update an existing item/order promotion."""
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "promotionType": promotion_type,
        "discountRules": discount_rules,
    }
    if inventory_criterion:
        body["inventoryCriterion"] = inventory_criterion
    if start_date:
        body["startDate"] = start_date
    if end_date:
        body["endDate"] = end_date
    if description:
        body["description"] = description
    return api_put(f"/sell/marketing/v1/item_promotion/{promotion_id}", body=body)


# ── Campaign Reports ─────────────────────────────────────────────────────────

@mcp.tool()
def get_report_tasks(report_types: str | None = None,
                     limit: int = 10,
                     offset: int = 0) -> dict:
    """
    Retrieve ad report tasks.

    Args:
        report_types: Comma-separated report types to filter.
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if report_types:
        params["report_types"] = report_types
    return api_get("/sell/marketing/v1/ad_report_task", params=params)


@mcp.tool()
def create_report_task(report_type: str, marketplace_id: str,
                        date_from: str, date_to: str,
                        campaign_ids: list[str] | None = None,
                        dimensions: list[dict] | None = None,
                        metrics: list[dict] | None = None) -> dict:
    """
    Create an ad performance report task.

    Args:
        report_type: Type of report (e.g. ACCOUNT_PERFORMANCE_REPORT, CAMPAIGN_PERFORMANCE_REPORT).
        marketplace_id: eBay marketplace ID.
        date_from: ISO 8601 start date.
        date_to: ISO 8601 end date.
        campaign_ids: Optional list of campaign IDs to include.
        dimensions: Optional list of dimension dicts.
        metrics: Optional list of metric dicts.
    """
    body: dict = {
        "reportType": report_type,
        "marketplaceId": marketplace_id,
        "dateFrom": date_from,
        "dateTo": date_to,
    }
    if campaign_ids:
        body["campaignIds"] = campaign_ids
    if dimensions:
        body["dimensions"] = dimensions
    if metrics:
        body["metrics"] = metrics
    return api_post("/sell/marketing/v1/ad_report_task", body=body)


@mcp.tool()
def get_report(report_id: str) -> dict:
    """
    Retrieve a completed ad report by report ID.

    Args:
        report_id: The report ID returned from create_report_task.
    """
    return api_get(f"/sell/marketing/v1/ad_report/{report_id}")
