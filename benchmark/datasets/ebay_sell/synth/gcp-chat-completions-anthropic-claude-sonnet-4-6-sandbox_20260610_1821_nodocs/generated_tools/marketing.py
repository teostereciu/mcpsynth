"""
eBay Sell Marketing API tools.
Covers: ad campaigns, promoted listings, promotions, item promotions,
        keyword management, and reports.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-marketing")

# ---------------------------------------------------------------------------
# Ad Campaigns (Promoted Listings)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_campaigns(
    campaign_name: str | None = None,
    campaign_status: str | None = None,
    end_date_range: str | None = None,
    start_date_range: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve ad campaigns for the seller.

    Args:
        campaign_name: Filter by campaign name (optional).
        campaign_status: Filter by status: RUNNING, PAUSED, ENDED (optional).
        end_date_range: Date range filter for campaign end date (optional).
        start_date_range: Date range filter for campaign start date (optional).
        limit: Number of campaigns to return (default 10).
        offset: Pagination offset (default 0).
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
    return ebay_request("GET", "/sell/marketing/v1/ad_campaign", params=params)


@mcp.tool()
def get_campaign(campaign_id: str) -> dict:
    """
    Retrieve a specific ad campaign by its ID.

    Args:
        campaign_id: The unique identifier of the campaign.
    """
    return ebay_request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def get_campaign_by_name(campaign_name: str) -> dict:
    """
    Retrieve an ad campaign by its name.

    Args:
        campaign_name: The name of the campaign.
    """
    return ebay_request(
        "GET",
        "/sell/marketing/v1/ad_campaign/get_campaign_by_name",
        params={"campaign_name": campaign_name},
    )


@mcp.tool()
def create_campaign(campaign: dict) -> dict:
    """
    Create a new Promoted Listings ad campaign.

    Args:
        campaign: Campaign object with campaignName, startDate, endDate,
                  marketplaceId, fundingStrategy (bidPercentage), and
                  promotedListingType fields.
                  Example: {
                    "campaignName": "Summer Sale",
                    "startDate": "2024-06-01T00:00:00Z",
                    "endDate": "2024-08-31T23:59:59Z",
                    "marketplaceId": "EBAY_US",
                    "fundingStrategy": {
                      "bidPercentage": "5.0",
                      "fundingModel": "COST_PER_SALE"
                    }
                  }
    """
    return ebay_request("POST", "/sell/marketing/v1/ad_campaign", json=campaign)


@mcp.tool()
def update_campaign_identification(
    campaign_id: str, campaign_name: str, start_date: str, end_date: str | None = None
) -> dict:
    """
    Update the name and dates of an existing campaign.

    Args:
        campaign_id: The unique identifier of the campaign.
        campaign_name: New name for the campaign.
        start_date: New start date in ISO 8601 format.
        end_date: New end date in ISO 8601 format (optional).
    """
    body: dict = {"campaignName": campaign_name, "startDate": start_date}
    if end_date:
        body["endDate"] = end_date
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_identification",
        json=body,
    )


@mcp.tool()
def update_campaign_budget(campaign_id: str, budget: dict) -> dict:
    """
    Update the budget for a campaign.

    Args:
        campaign_id: The unique identifier of the campaign.
        budget: Budget object with 'dailyBudget' (value and currency).
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_budget",
        json=budget,
    )


@mcp.tool()
def pause_campaign(campaign_id: str) -> dict:
    """
    Pause a running ad campaign.

    Args:
        campaign_id: The unique identifier of the campaign to pause.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/pause",
    )


@mcp.tool()
def resume_campaign(campaign_id: str) -> dict:
    """
    Resume a paused ad campaign.

    Args:
        campaign_id: The unique identifier of the campaign to resume.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/resume",
    )


@mcp.tool()
def end_campaign(campaign_id: str) -> dict:
    """
    End (permanently stop) an ad campaign.

    Args:
        campaign_id: The unique identifier of the campaign to end.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/end",
    )


@mcp.tool()
def delete_campaign(campaign_id: str) -> dict:
    """
    Delete an ended ad campaign.

    Args:
        campaign_id: The unique identifier of the campaign to delete.
    """
    return ebay_request(
        "DELETE",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}",
    )


@mcp.tool()
def clone_campaign(campaign_id: str, campaign_name: str, start_date: str, end_date: str | None = None) -> dict:
    """
    Clone an existing campaign to create a new one.

    Args:
        campaign_id: The unique identifier of the campaign to clone.
        campaign_name: Name for the new cloned campaign.
        start_date: Start date for the new campaign in ISO 8601 format.
        end_date: End date for the new campaign in ISO 8601 format (optional).
    """
    body: dict = {"campaignName": campaign_name, "startDate": start_date}
    if end_date:
        body["endDate"] = end_date
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/clone",
        json=body,
    )


# ---------------------------------------------------------------------------
# Ads (individual ad items within a campaign)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_ads(
    campaign_id: str,
    limit: int = 10,
    offset: int = 0,
    listing_ids: str | None = None,
) -> dict:
    """
    Retrieve ads within a campaign.

    Args:
        campaign_id: The unique identifier of the campaign.
        limit: Number of ads to return (default 10).
        offset: Pagination offset (default 0).
        listing_ids: Comma-separated listing IDs to filter by (optional).
    """
    params: dict = {"limit": limit, "offset": offset}
    if listing_ids:
        params["listing_ids"] = listing_ids
    return ebay_request(
        "GET",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad",
        params=params,
    )


@mcp.tool()
def get_ad(campaign_id: str, ad_id: str) -> dict:
    """
    Retrieve a specific ad within a campaign.

    Args:
        campaign_id: The unique identifier of the campaign.
        ad_id: The unique identifier of the ad.
    """
    return ebay_request(
        "GET",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}",
    )


@mcp.tool()
def create_ads_by_listing_id(campaign_id: str, ads: list) -> dict:
    """
    Add listings to a campaign as ads using listing IDs.

    Args:
        campaign_id: The unique identifier of the campaign.
        ads: List of ad objects, each with 'listingId' and 'bidPercentage'.
             Example: [{"listingId": "123456789", "bidPercentage": "5.0"}]
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id",
        json={"requests": ads},
    )


@mcp.tool()
def create_ads_by_inventory_reference(campaign_id: str, ads: list) -> dict:
    """
    Add inventory items to a campaign as ads using inventory references.

    Args:
        campaign_id: The unique identifier of the campaign.
        ads: List of ad objects with 'inventoryReferenceId', 'inventoryReferenceType',
             and 'bidPercentage'.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference",
        json={"requests": ads},
    )


@mcp.tool()
def delete_ads_by_listing_id(campaign_id: str, listing_ids: list) -> dict:
    """
    Remove ads from a campaign by listing IDs.

    Args:
        campaign_id: The unique identifier of the campaign.
        listing_ids: List of listing ID strings to remove.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id",
        json={"requests": [{"listingId": lid} for lid in listing_ids]},
    )


@mcp.tool()
def update_bids_by_listing_id(campaign_id: str, bids: list) -> dict:
    """
    Update bid percentages for ads in a campaign by listing ID.

    Args:
        campaign_id: The unique identifier of the campaign.
        bids: List of objects with 'listingId' and 'bidPercentage'.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id",
        json={"requests": bids},
    )


# ---------------------------------------------------------------------------
# Keywords (Promoted Listings Advanced)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_keywords(campaign_id: str, limit: int = 10, offset: int = 0) -> dict:
    """
    Retrieve keywords for a Promoted Listings Advanced campaign.

    Args:
        campaign_id: The unique identifier of the campaign.
        limit: Number of keywords to return (default 10).
        offset: Pagination offset (default 0).
    """
    return ebay_request(
        "GET",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/keyword",
        params={"limit": limit, "offset": offset},
    )


@mcp.tool()
def get_keyword(campaign_id: str, keyword_id: str) -> dict:
    """
    Retrieve a specific keyword from a campaign.

    Args:
        campaign_id: The unique identifier of the campaign.
        keyword_id: The unique identifier of the keyword.
    """
    return ebay_request(
        "GET",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/keyword/{keyword_id}",
    )


@mcp.tool()
def create_keywords(campaign_id: str, keywords: list) -> dict:
    """
    Add keywords to a Promoted Listings Advanced campaign.

    Args:
        campaign_id: The unique identifier of the campaign.
        keywords: List of keyword objects with 'keywordText', 'matchType',
                  and 'bid' (value and currency).
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_keywords",
        json={"requests": keywords},
    )


@mcp.tool()
def update_keywords(campaign_id: str, keywords: list) -> dict:
    """
    Update keywords in a Promoted Listings Advanced campaign.

    Args:
        campaign_id: The unique identifier of the campaign.
        keywords: List of keyword update objects with 'keywordId' and 'bid'.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_keywords",
        json={"requests": keywords},
    )


# ---------------------------------------------------------------------------
# Item Promotions (Markdown, Order Discount, etc.)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_promotions(
    marketplace_id: str,
    promotion_status: str | None = None,
    promotion_type: str | None = None,
    limit: int = 10,
    offset: int = 0,
    q: str | None = None,
    sort: str | None = None,
) -> dict:
    """
    Retrieve promotions for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        promotion_status: Filter by status: ACTIVE, DRAFT, SCHEDULED, ENDED (optional).
        promotion_type: Filter by type: MARKDOWN_SALE, ORDER_DISCOUNT,
                        VOLUME_DISCOUNT, CODED_COUPON (optional).
        limit: Number of promotions to return (default 10).
        offset: Pagination offset (default 0).
        q: Search query string (optional).
        sort: Sort order, e.g. 'START_DATE' (optional).
    """
    params: dict = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if promotion_status:
        params["promotion_status"] = promotion_status
    if promotion_type:
        params["promotion_type"] = promotion_type
    if q:
        params["q"] = q
    if sort:
        params["sort"] = sort
    return ebay_request("GET", "/sell/marketing/v1/promotion", params=params)


@mcp.tool()
def get_promotion(promotion_id: str) -> dict:
    """
    Retrieve a specific promotion by its ID.

    Args:
        promotion_id: The unique identifier of the promotion.
    """
    return ebay_request("GET", f"/sell/marketing/v1/promotion/{promotion_id}")


@mcp.tool()
def get_promotion_reports(
    marketplace_id: str,
    promotion_type: str | None = None,
    promotion_status: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve performance reports for promotions.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        promotion_type: Filter by promotion type (optional).
        promotion_status: Filter by promotion status (optional).
        limit: Number of reports to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if promotion_type:
        params["promotion_type"] = promotion_type
    if promotion_status:
        params["promotion_status"] = promotion_status
    return ebay_request(
        "GET", "/sell/marketing/v1/promotion_report", params=params
    )


@mcp.tool()
def get_promotion_summary_report(marketplace_id: str) -> dict:
    """
    Retrieve a summary report of all promotions for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        "/sell/marketing/v1/promotion_summary_report",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def create_item_price_markdown_promotion(promotion: dict) -> dict:
    """
    Create a markdown (sale price) promotion.

    Args:
        promotion: Promotion object with name, marketplaceId, startDate,
                   endDate, selectedInventoryDiscounts (list of discount rules
                   with inventoryItems and discountRules).
    """
    return ebay_request(
        "POST",
        "/sell/marketing/v1/item_price_markdown",
        json=promotion,
    )


@mcp.tool()
def update_item_price_markdown_promotion(promotion_id: str, promotion: dict) -> dict:
    """
    Update an existing markdown promotion.

    Args:
        promotion_id: The unique identifier of the promotion.
        promotion: Updated promotion object.
    """
    return ebay_request(
        "PUT",
        f"/sell/marketing/v1/item_price_markdown/{promotion_id}",
        json=promotion,
    )


@mcp.tool()
def delete_item_price_markdown_promotion(promotion_id: str) -> dict:
    """
    Delete a markdown promotion.

    Args:
        promotion_id: The unique identifier of the promotion to delete.
    """
    return ebay_request(
        "DELETE",
        f"/sell/marketing/v1/item_price_markdown/{promotion_id}",
    )


@mcp.tool()
def create_item_promotion(promotion: dict) -> dict:
    """
    Create an order-level or volume discount promotion.

    Args:
        promotion: Promotion object with name, marketplaceId, promotionType,
                   startDate, endDate, discountRules, and inventoryItems.
    """
    return ebay_request(
        "POST",
        "/sell/marketing/v1/item_promotion",
        json=promotion,
    )


@mcp.tool()
def update_item_promotion(promotion_id: str, promotion: dict) -> dict:
    """
    Update an existing order-level or volume discount promotion.

    Args:
        promotion_id: The unique identifier of the promotion.
        promotion: Updated promotion object.
    """
    return ebay_request(
        "PUT",
        f"/sell/marketing/v1/item_promotion/{promotion_id}",
        json=promotion,
    )


@mcp.tool()
def delete_item_promotion(promotion_id: str) -> dict:
    """
    Delete an order-level or volume discount promotion.

    Args:
        promotion_id: The unique identifier of the promotion to delete.
    """
    return ebay_request(
        "DELETE",
        f"/sell/marketing/v1/item_promotion/{promotion_id}",
    )


@mcp.tool()
def pause_promotion(promotion_id: str) -> dict:
    """
    Pause an active promotion.

    Args:
        promotion_id: The unique identifier of the promotion to pause.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/promotion/{promotion_id}/pause",
    )


@mcp.tool()
def resume_promotion(promotion_id: str) -> dict:
    """
    Resume a paused promotion.

    Args:
        promotion_id: The unique identifier of the promotion to resume.
    """
    return ebay_request(
        "POST",
        f"/sell/marketing/v1/promotion/{promotion_id}/resume",
    )


@mcp.tool()
def get_listing_set(promotion_id: str, limit: int = 200, offset: int = 0) -> dict:
    """
    Retrieve the set of listings included in a promotion.

    Args:
        promotion_id: The unique identifier of the promotion.
        limit: Number of listings to return (default 200).
        offset: Pagination offset (default 0).
    """
    return ebay_request(
        "GET",
        f"/sell/marketing/v1/promotion/{promotion_id}/get_listing_set",
        params={"limit": limit, "offset": offset},
    )


# ---------------------------------------------------------------------------
# Campaign Reports
# ---------------------------------------------------------------------------

@mcp.tool()
def get_report_tasks(
    report_types: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve report tasks for marketing analytics.

    Args:
        report_types: Comma-separated report types to filter by (optional).
        limit: Number of tasks to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if report_types:
        params["report_types"] = report_types
    return ebay_request("GET", "/sell/marketing/v1/ad_report_task", params=params)


@mcp.tool()
def create_report_task(report_task: dict) -> dict:
    """
    Create a new marketing analytics report task.

    Args:
        report_task: Report task object with reportType, campaignIds,
                     dateFrom, dateTo, dimensions, and metrics.
                     Example: {
                       "reportType": "CAMPAIGN_PERFORMANCE_REPORT",
                       "campaignIds": ["campaign-id-1"],
                       "dateFrom": "2024-01-01",
                       "dateTo": "2024-01-31",
                       "dimensions": [{"dimensionKey": "CAMPAIGN_ID"}],
                       "metrics": [{"metricKey": "TOTAL_SPEND"}]
                     }
    """
    return ebay_request("POST", "/sell/marketing/v1/ad_report_task", json=report_task)


@mcp.tool()
def get_report(report_id: str) -> dict:
    """
    Retrieve a completed marketing analytics report.

    Args:
        report_id: The unique identifier of the report.
    """
    return ebay_request("GET", f"/sell/marketing/v1/ad_report/{report_id}")


@mcp.tool()
def delete_report_task(report_task_id: str) -> dict:
    """
    Delete a marketing analytics report task.

    Args:
        report_task_id: The unique identifier of the report task.
    """
    return ebay_request(
        "DELETE",
        f"/sell/marketing/v1/ad_report_task/{report_task_id}",
    )
