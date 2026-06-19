

# =============================================================================
# MARKETING API TOOLS
# =============================================================================

@mcp.tool()
def get_campaigns(limit: str = "10", offset: str = "0", campaign_title: str = None,
                  campaign_status: str = None, channels: str = None) -> dict:
    """
    Retrieves marketing campaigns.
    
    Args:
        limit: Maximum campaigns per page (default: 10)
        offset: Page number (default: 0)
        campaign_title: Filter by campaign title
        campaign_status: Filter by status
        channels: Filter by channel
    
    Returns:
        Campaign collection
    """
    params = {"limit": limit, "offset": offset}
    if campaign_title:
        params["campaign_title"] = campaign_title
    if campaign_status:
        params["campaign_status"] = campaign_status
    if channels:
        params["channels"] = channels
    
    return make_request("GET", "/ad_campaign", params=params)


@mcp.tool()
def get_campaign(campaign_id: str) -> dict:
    """
    Retrieves a specific campaign by ID.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
    
    Returns:
        Campaign details
    """
    return make_request("GET", f"/ad_campaign/{campaign_id}")


@mcp.tool()
def create_ad_group(campaign_id: str, default_bid: float) -> dict:
    """
    Creates an ad group for a campaign.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
        default_bid: Default bid amount
    
    Returns:
        Created ad group details
    """
    payload = {
        "defaultBid": default_bid,
    }
    
    return make_request("POST", f"/ad_campaign/{campaign_id}/ad_group", data=payload)


@mcp.tool()
def get_ad_groups(campaign_id: str, limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves ad groups for a campaign.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
        limit: Maximum ad groups per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Ad group collection
    """
    return make_request("GET", f"/ad_campaign/{campaign_id}/ad_group",
                       params={"limit": limit, "offset": offset})


@mcp.tool()
def get_ad_group(campaign_id: str, ad_group_id: str) -> dict:
    """
    Retrieves a specific ad group.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
        ad_group_id: The eBay-assigned ad group ID
    
    Returns:
        Ad group details
    """
    return make_request("GET", f"/ad_campaign/{campaign_id}/ad_group/{ad_group_id}")


@mcp.tool()
def update_ad_group(campaign_id: str, ad_group_id: str, default_bid: float) -> dict:
    """
    Updates an ad group's bid.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
        ad_group_id: The eBay-assigned ad group ID
        default_bid: New default bid amount
    
    Returns:
        Updated ad group details
    """
    payload = {
        "defaultBid": default_bid,
    }
    
    return make_request("PUT", f"/ad_campaign/{campaign_id}/ad_group/{ad_group_id}", data=payload)


@mcp.tool()
def get_ads(campaign_id: str = None, ad_group_id: str = None,
            limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves ads, optionally filtered by campaign or ad group.
    
    Args:
        campaign_id: Filter by campaign ID (optional)
        ad_group_id: Filter by ad group ID (optional)
        limit: Maximum ads per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Ad collection
    """
    base_path = "/ad"
    if campaign_id:
        base_path = f"/ad_campaign/{campaign_id}/ad"
    if ad_group_id:
        base_path = f"/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/ad"
    
    return make_request("GET", base_path, params={"limit": limit, "offset": offset})


@mcp.tool()
def get_ad(ad_id: str) -> dict:
    """
    Retrieves a specific ad by ID.
    
    Args:
        ad_id: The eBay-assigned ad ID
    
    Returns:
        Ad details
    """
    return make_request("GET", f"/ad/{ad_id}")


@mcp.tool()
def create_ad_by_listing_id(campaign_id: str, listing_id: str, bid: float = None) -> dict:
    """
    Creates an ad for a specific listing.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
        listing_id: eBay listing ID
        bid: Optional bid amount
    
    Returns:
        Created ad details
    """
    payload = {
        "listingId": listing_id,
    }
    if bid is not None:
        payload["bid"] = bid
    
    return make_request("POST", f"/ad_campaign/{campaign_id}/ad", data=payload)


@mcp.tool()
def update_bid(ad_id: str, bid: float) -> dict:
    """
    Updates an ad's bid.
    
    Args:
        ad_id: The eBay-assigned ad ID
        bid: New bid amount
    
    Returns:
        Updated ad details
    """
    payload = {
        "bid": bid,
    }
    
    return make_request("PUT", f"/ad/{ad_id}/bid", data=payload)


@mcp.tool()
def delete_ad(ad_id: str) -> dict:
    """
    Deletes an ad.
    
    Args:
        ad_id: The eBay-assigned ad ID
    
    Returns:
        Response with delete status
    """
    return make_request("DELETE", f"/ad/{ad_id}")


@mcp.tool()
def bulk_update_ads_status(campaign_id: str, listing_ids: list, status: str) -> dict:
    """
    Updates status for multiple ads in bulk.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
        listing_ids: List of eBay listing IDs
        status: New status (ACTIVE, INACTIVE)
    
    Returns:
        Bulk update results
    """
    payload = {
        "campaignId": campaign_id,
        "listingIds": listing_ids,
        "status": status,
    }
    
    return make_request("POST", "/bulk_update_ads_status", data=payload)


@mcp.tool()
def bulk_create_ads_by_listing_id(campaign_id: str, listing_ids: list,
                                   bids: list = None) -> dict:
    """
    Creates multiple ads in bulk.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
        listing_ids: List of eBay listing IDs
        bids: Optional list of bid amounts (same order as listing_ids)
    
    Returns:
        Bulk create results
    """
    payload = {
        "campaignId": campaign_id,
        "listingIds": listing_ids,
    }
    if bids:
        payload["bids"] = bids
    
    return make_request("POST", "/bulk_create_ads_by_listing_id", data=payload)


@mcp.tool()
def bulk_delete_ads_by_listing_id(campaign_id: str, listing_ids: list) -> dict:
    """
    Deletes multiple ads in bulk.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
        listing_ids: List of eBay listing IDs
    
    Returns:
        Bulk delete results
    """
    payload = {
        "campaignId": campaign_id,
        "listingIds": listing_ids,
    }
    
    return make_request("POST", "/bulk_delete_ads_by_listing_id", data=payload)


@mcp.tool()
def suggest_keywords(keywords: list, campaign_id: str = None) -> dict:
    """
    Gets keyword suggestions.
    
    Args:
        keywords: List of seed keywords
        campaign_id: Optional campaign ID
    
    Returns:
        Keyword suggestions
    """
    payload = {
        "keywords": keywords,
    }
    if campaign_id:
        payload["campaignId"] = campaign_id
    
    return make_request("POST", "/suggest_keywords", data=payload)


@mcp.tool()
def suggest_budget(campaign_id: str) -> dict:
    """
    Gets budget suggestions for a campaign.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
    
    Returns:
        Budget suggestions
    """
    return make_request("POST", f"/ad_campaign/{campaign_id}/suggest_budget")


@mcp.tool()
def suggest_bids(campaign_id: str) -> dict:
    """
    Gets bid suggestions for a campaign.
    
    Args:
        campaign_id: The eBay-assigned campaign ID
    
    Returns:
        Bid suggestions
    """
    return make_request("POST", f"/ad_campaign/{campaign_id}/suggest_bids")


# =============================================================================
# FINANCES API TOOLS
# =============================================================================

@mcp.tool()
def get_payouts(filter: str = None, limit: str = "20", offset: str = "0",
                marketplace_id: str = None) -> dict:
    """
    Retrieves seller payouts.
    
    Args:
        filter: Filter criteria (payoutDate, payoutStatus, etc.)
        limit: Maximum payouts per page (default: 20)
        offset: Page number (default: 0)
        marketplace_id: eBay marketplace ID
    
    Returns:
        Payout collection
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", "/payout", params=params, headers=headers)


@mcp.tool()
def get_payout(payout_id: str, marketplace_id: str = None) -> dict:
    """
    Retrieves a specific payout by ID.
    
    Args:
        payout_id: The eBay-assigned payout ID
        marketplace_id: eBay marketplace ID
    
    Returns:
        Payout details
    """
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", f"/payout/{payout_id}", headers=headers)


@mcp.tool()
def get_transactions(filter: str = None, limit: str = "50", offset: str = "0",
                     marketplace_id: str = None) -> dict:
    """
    Retrieves seller transactions.
    
    Args:
        filter: Filter criteria
        limit: Maximum transactions per page (default: 50)
        offset: Page number (default: 0)
        marketplace_id: eBay marketplace ID
    
    Returns:
        Transaction collection
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", "/transaction", params=params, headers=headers)


@mcp.tool()
def get_transaction_summary(filter: str = None, marketplace_id: str = None) -> dict:
    """
    Retrieves a summary of seller transactions.
    
    Args:
        filter: Filter criteria
        marketplace_id: eBay marketplace ID
    
    Returns:
        Transaction summary
    """
    params = {}
    if filter:
        params["filter"] = filter
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", "/transaction_summary", params=params, headers=headers)


@mcp.tool()
def get_billing_activities(filter: str = None, limit: str = "50", offset: str = "0",
                           marketplace_id: str = None) -> dict:
    """
    Retrieves billing activities.
    
    Args:
        filter: Filter criteria
        limit: Maximum activities per page (default: 50)
        offset: Page number (default: 0)
        marketplace_id: eBay marketplace ID
    
    Returns:
        Billing activity collection
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", "/billing_activity", params=params, headers=headers)


@mcp.tool()
def get_seller_funds_summary(marketplace_id: str = None) -> dict:
    """
    Retrieves a summary of seller funds.
    
    Args:
        marketplace_id: eBay marketplace ID
    
    Returns:
        Seller funds summary
    """
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", "/seller_funds_summary", headers=headers)


@mcp.tool()
def get_payout_summary(filter: str = None, marketplace_id: str = None) -> dict:
    """
    Retrieves a summary of payouts.
    
    Args:
        filter: Filter criteria
        marketplace_id: eBay marketplace ID
    
    Returns:
        Payout summary
    """
    params = {}
    if filter:
        params["filter"] = filter
    
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", "/payout_summary", params=params, headers=headers)


# =============================================================================
# FEED API TOOLS
# =============================================================================

@mcp.tool()
def get_tasks(feed_type: str = None, schedule_id: str = None,
              limit: str = "10", offset: str = "0") -> dict:
    """
    Retrieves feed tasks.
    
    Args:
        feed_type: Filter by feed type (optional)
        schedule_id: Filter by schedule ID (optional)
        limit: Maximum tasks per page (default: 10)
        offset: Page number (default: 0)
    
    Returns:
        Task collection
    """
    params = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if schedule_id:
        params["schedule_id"] = schedule_id
    
    return make_request("GET", "/task", params=params)


@mcp.tool()
def get_task(task_id: str) -> dict:
    """
    Retrieves a specific task by ID.
    
    Args:
        task_id: The eBay-assigned task ID
    
    Returns:
        Task details
    """
    return make_request("GET", f"/task/{task_id}")


@mcp.tool()
def get_inventory_tasks(feed_type: str = None, limit: str = "10", offset: str = "0") -> dict:
    """
    Retrieves inventory-related tasks.
    
    Args:
        feed_type: Filter by feed type (optional)
        limit: Maximum tasks per page (default: 10)
        offset: Page number (default: 0)
    
    Returns:
        Inventory task collection
    """
    params = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    
    return make_request("GET", "/inventory_task", params=params)


@mcp.tool()
def get_inventory_task(task_id: str) -> dict:
    """
    Retrieves a specific inventory task.
    
    Args:
        task_id: The eBay-assigned task ID
    
    Returns:
        Inventory task details
    """
    return make_request("GET", f"/inventory_task/{task_id}")


@mcp.tool()
def get_order_tasks(limit: str = "10", offset: str = "0") -> dict:
    """
    Retrieves order-related tasks.
    
    Args:
        limit: Maximum tasks per page (default: 10)
        offset: Page number (default: 0)
    
    Returns:
        Order task collection
    """
    params = {"limit": limit, "offset": offset}
    
    return make_request("GET", "/order_task", params=params)


@mcp.tool()
def get_order_task(task_id: str) -> dict:
    """
    Retrieves a specific order task.
    
    Args:
        task_id: The eBay-assigned task ID
    
    Returns:
        Order task details
    """
    return make_request("GET", f"/order_task/{task_id}")


@mcp.tool()
def create_inventory_task(feed_type: str, schema_version: str) -> dict:
    """
    Creates an inventory upload/download task.
    
    Args:
        feed_type: Feed type (e.g., "LMS_INVENTORY")
        schema_version: Schema version
    
    Returns:
        Created task details
    """
    payload = {
        "feedType": feed_type,
        "schemaVersion": schema_version,
    }
    
    return make_request("POST", "/inventory_task", data=payload)


@mcp.tool()
def create_order_task(feed_type: str, schema_version: str,
                      filter_criteria: dict = None) -> dict:
    """
    Creates an order task with filter criteria.
    
    Args:
        feed_type: Feed type (e.g., "LMS_ORDER_REPORT")
        schema_version: Schema version
        filter_criteria: Filter criteria for orders
    
    Returns:
        Created task details
    """
    payload = {
        "feedType": feed_type,
        "schemaVersion": schema_version,
    }
    if filter_criteria:
        payload["filterCriteria"] = filter_criteria
    
    return make_request("POST", "/order_task", data=payload)


@mcp.tool()
def create_schedule(feed_type: str, schedule_template_id: str,
                    start_time: str = None, next_run_time: str = None) -> dict:
    """
    Creates a scheduled task.
    
    Args:
        feed_type: Feed type
        schedule_template_id: Schedule template ID
        start_time: Schedule start time (ISO 8601)
        next_run_time: Next run time (ISO 8601)
    
    Returns:
        Created schedule details
    """
    payload = {
        "feedType": feed_type,
        "scheduleTemplateId": schedule_template_id,
    }
    if start_time:
        payload["startTime"] = start_time
    if next_run_time:
        payload["nextRunTime"] = next_run_time
    
    return make_request("POST", "/schedule", data=payload)


@mcp.tool()
def get_schedules(limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves scheduled tasks.
    
    Args:
        limit: Maximum schedules per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Schedule collection
    """
    params = {"limit": limit, "offset": offset}
    
    return make_request("GET", "/schedule", params=params)


@mcp.tool()
def get_schedule(schedule_id: str) -> dict:
    """
    Retrieves a specific schedule by ID.
    
    Args:
        schedule_id: The eBay-assigned schedule ID
    
    Returns:
        Schedule details
    """
    return make_request("GET", f"/schedule/{schedule_id}")


@mcp.tool()
def update_schedule(schedule_id: str, start_time: str = None,
                    next_run_time: str = None) -> dict:
    """
    Updates a scheduled task.
    
    Args:
        schedule_id: The eBay-assigned schedule ID
        start_time: Updated start time (ISO 8601)
        next_run_time: Updated next run time (ISO 8601)
    
    Returns:
        Updated schedule details
    """
    payload = {}
    if start_time:
        payload["startTime"] = start_time
    if next_run_time:
        payload["nextRunTime"] = next_run_time
    
    return make_request("PUT", f"/schedule/{schedule_id}", data=payload)


@mcp.tool()
def delete_schedule(schedule_id: str) -> dict:
    """
    Deletes a scheduled task.
    
    Args:
        schedule_id: The eBay-assigned schedule ID
    
    Returns:
        Response with delete status
    """
    return make_request("DELETE", f"/schedule/{schedule_id}")


@mcp.tool()
def get_schedule_templates() -> dict:
    """
    Retrieves available schedule templates.
    
    Returns:
        Schedule template collection
    """
    return make_request("GET", "/schedule_template")


@mcp.tool()
def get_schedule_template(schedule_template_id: str) -> dict:
    """
    Retrieves a specific schedule template.
    
    Args:
        schedule_template_id: The schedule template ID
    
    Returns:
        Schedule template details
    """
    return make_request("GET", f"/schedule_template/{schedule_template_id}")


@mcp.tool()
def get_task_input_file(task_id: str) -> dict:
    """
    Downloads the input file for a task.
    
    Args:
        task_id: The eBay-assigned task ID
    
    Returns:
        Input file content
    """
    return make_request("GET", f"/task/{task_id}/download_input_file")


@mcp.tool()
def get_task_result_file(task_id: str) -> dict:
    """
    Downloads the result file for a task.
    
    Args:
        task_id: The eBay-assigned task ID
    
    Returns:
        Result file content
    """
    return make_request("GET", f"/task/{task_id}/download_result_file")


@mcp.tool()
def upload_task_file(task_id: str, file_content: str,
                      content_type: str = "text/csv") -> dict:
    """
    Uploads a file for a task.
    
    Args:
        task_id: The eBay-assigned task ID
        file_content: File content (base64 encoded or raw)
        content_type: MIME type of the file
    
    Returns:
        Upload result
    """
    headers = {
        "Content-Type": content_type,
    }
    
    return make_request("POST", f"/task/{task_id}/upload_file",
                       headers=headers, data=file_content)


# =============================================================================
# LOGISTICS API TOOLS
# =============================================================================

@mcp.tool()
def create_shipping_quote(order_id: str, shipment_details: dict,
                          ship_from_address: dict) -> dict:
    """
    Creates a shipping quote for an order.
    
    Args:
        order_id: The eBay-assigned order ID
        shipment_details: Shipment details including line items
        ship_from_address: Ship-from address
    
    Returns:
        Shipping quote details
    """
    payload = {
        "orderId": order_id,
        "shipmentDetails": shipment_details,
        "shipFromAddress": ship_from_address,
    }
    
    return make_request("POST", "/shipping_quote", data=payload)


@mcp.tool()
def get_shipping_quote(quote_id: str) -> dict:
    """
    Retrieves a specific shipping quote by ID.
    
    Args:
        quote_id: The eBay-assigned quote ID
    
    Returns:
        Shipping quote details
    """
    return make_request("GET", f"/shipping_quote/{quote_id}")


@mcp.tool()
def create_from_shipping_quote(quote_id: str, shipment_details: dict) -> dict:
    """
    Creates a shipment from a shipping quote.
    
    Args:
        quote_id: The eBay-assigned quote ID
        shipment_details: Shipment details
    
    Returns:
        Shipment details
    """
    payload = {
        "shipmentDetails": shipment_details,
    }
    
    return make_request("POST", f"/shipping_quote/{quote_id}/create_shipment", data=payload)


@mcp.tool()
def get_shipment(shipment_id: str) -> dict:
    """
    Retrieves a specific shipment by ID.
    
    Args:
        shipment_id: The eBay-assigned shipment ID
    
    Returns:
        Shipment details
    """
    return make_request("GET", f"/shipment/{shipment_id}")


@mcp.tool()
def cancel_shipment(shipment_id: str) -> dict:
    """
    Cancels a shipment.
    
    Args:
        shipment_id: The eBay-assigned shipment ID
    
    Returns:
        Response with cancel status
    """
    return make_request("POST", f"/shipment/{shipment_id}/cancel")


@mcp.tool()
def download_label_file(label_id: str) -> dict:
    """
    Downloads a shipping label file.
    
    Args:
        label_id: The eBay-assigned label ID
    
    Returns:
        Label file content
    """
    return make_request("GET", f"/label/{label_id}/download")


# =============================================================================
# COMPLIANCE API TOOLS
# =============================================================================

@mcp.tool()
def get_listing_violations(filter: str = None, limit: str = "25",
                           offset: str = "0") -> dict:
    """
    Retrieves listing violations.
    
    Args:
        filter: Filter criteria
        limit: Maximum violations per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Listing violation collection
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    
    return make_request("GET", "/listing_violation", params=params)


@mcp.tool()
def get_listing_violations_summary() -> dict:
    """
    Retrieves a summary of listing violations.
    
    Returns:
        Listing violation summary
    """
    return make_request("GET", "/listing_violation_summary")


# =============================================================================
# ANALYTICS API TOOLS
# =============================================================================

@mcp.tool()
def get_traffic_report(filter: str = None, limit: str = "25",
                       offset: str = "0") -> dict:
    """
    Retrieves traffic reports.
    
    Args:
        filter: Filter criteria
        limit: Maximum reports per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Traffic report collection
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    
    return make_request("GET", "/traffic_report", params=params)


@mcp.tool()
def get_seller_standards_profile(program: str, cycle: str,
                                  marketplace_id: str = None) -> dict:
    """
    Retrieves seller standards profile.
    
    Args:
        program: Program name
        cycle: Cycle identifier
        marketplace_id: eBay marketplace ID
    
    Returns:
        Seller standards profile
    """
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", f"/seller_standards_profile/{program}/{cycle}",
                       headers=headers)


@mcp.tool()
def find_seller_standards_profiles(filter: str = None) -> dict:
    """
    Finds seller standards profiles.
    
    Args:
        filter: Filter criteria
    
    Returns:
        Seller standards profile collection
    """
    params = {}
    if filter:
        params["filter"] = filter
    
    return make_request("GET", "/seller_standards_profile", params=params)


@mcp.tool()
def get_customer_service_metric(metric_type: str, evaluation_type: str,
                                 marketplace_id: str = None) -> dict:
    """
    Retrieves customer service metrics.
    
    Args:
        metric_type: Metric type
        evaluation_type: Evaluation type
        marketplace_id: eBay marketplace ID
    
    Returns:
        Customer service metric details
    """
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", f"/customer_service_metric/{metric_type}/{evaluation_type}",
                       headers=headers)


# =============================================================================
# STORES API TOOLS
# =============================================================================

@mcp.tool()
def get_store() -> dict:
    """
    Retrieves the seller's store information.
    
    Returns:
        Store details
    """
    return make_request("GET", "/store")


@mcp.tool()
def get_store_categories(limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves the seller's store categories.
    
    Args:
        limit: Maximum categories per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Store category collection
    """
    params = {"limit": limit, "offset": offset}
    
    return make_request("GET", "/store/category", params=params)


@mcp.tool()
def add_store_category(name: str, parent_category_id: str = None) -> dict:
    """
    Adds a new store category.
    
    Args:
        name: Category name
        parent_category_id: Parent category ID (optional)
    
    Returns:
        Created store category details
    """
    payload = {
        "name": name,
    }
    if parent_category_id:
        payload["parentCategoryId"] = parent_category_id
    
    return make_request("POST", "/store/category", data=payload)


@mcp.tool()
def update_store_category(category_id: str, name: str = None) -> dict:
    """
    Updates a store category.
    
    Args:
        category_id: The eBay-assigned category ID
        name: Updated category name (optional)
    
    Returns:
        Updated store category details
    """
    payload = {}
    if name:
        payload["name"] = name
    
    return make_request("PUT", f"/store/category/{category_id}", data=payload)


@mcp.tool()
def delete_store_category(category_id: str) -> dict:
    """
    Deletes a store category.
    
    Args:
        category_id: The eBay-assigned category ID
    
    Returns:
        Response with delete status
    """
    return make_request("DELETE", f"/store/category/{category_id}")


@mcp.tool()
def move_store_category(category_id: str, new_parent_id: str,
                         new_position: int = None) -> dict:
    """
    Moves a store category.
    
    Args:
        category_id: The eBay-assigned category ID
        new_parent_id: New parent category ID
        new_position: New position (optional)
    
    Returns:
        Response with move status
    """
    payload = {
        "parentCategoryId": new_parent_id,
    }
    if new_position is not None:
        payload["position"] = new_position
    
    return make_request("POST", f"/store/category/{category_id}/move", data=payload)


@mcp.tool()
def rename_store_category(category_id: str, name: str) -> dict:
    """
    Renames a store category.
    
    Args:
        category_id: The eBay-assigned category ID
        name: New category name
    
    Returns:
        Response with rename status
    """
    payload = {
        "name": name,
    }
    
    return make_request("POST", f"/store/category/{category_id}/rename", data=payload)


@mcp.tool()
def get_store_tasks(limit: str = "25", offset: str = "0") -> dict:
    """
    Retrieves store-related tasks.
    
    Args:
        limit: Maximum tasks per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Store task collection
    """
    params = {"limit": limit, "offset": offset}
    
    return make_request("GET", "/store/task", params=params)


@mcp.tool()
def get_store_task(task_id: str) -> dict:
    """
    Retrieves a specific store task.
    
    Args:
        task_id: The eBay-assigned task ID
    
    Returns:
        Store task details
    """
    return make_request("GET", f"/store/task/{task_id}")


# =============================================================================
# PAYMENT DISPUTE TOOLS
# =============================================================================

@mcp.tool()
def get_payment_disputes(filter: str = None, limit: str = "25",
                         offset: str = "0") -> dict:
    """
    Retrieves payment disputes.
    
    Args:
        filter: Filter criteria
        limit: Maximum disputes per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Payment dispute collection
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    
    return make_request("GET", "/payment_dispute_summary", params=params)


@mcp.tool()
def get_payment_dispute(dispute_id: str) -> dict:
    """
    Retrieves a specific payment dispute.
    
    Args:
        dispute_id: The eBay-assigned dispute ID
    
    Returns:
        Payment dispute details
    """
    return make_request("GET", f"/payment_dispute/{dispute_id}")


@mcp.tool()
def accept_payment_dispute(dispute_id: str) -> dict:
    """
    Accepts a payment dispute.
    
    Args:
        dispute_id: The eBay-assigned dispute ID
    
    Returns:
        Response with acceptance status
    """
    return make_request("POST", f"/payment_dispute/{dispute_id}/accept")


@mcp.tool()
def contest_payment_dispute(dispute_id: str, evidence_ids: list,
                             resolution: str = None) -> dict:
    """
    Contests a payment dispute.
    
    Args:
        dispute_id: The eBay-assigned dispute ID
        evidence_ids: List of evidence IDs
        resolution: Resolution amount (optional)
    
    Returns:
        Response with contest status
    """
    payload = {
        "evidenceIds": evidence_ids,
    }
    if resolution:
        payload["resolution"] = resolution
    
    return make_request("POST", f"/payment_dispute/{dispute_id}/contest", data=payload)


@mcp.tool()
def add_evidence(dispute_id: str, evidence_type: str,
                 evidence_content: dict) -> dict:
    """
    Adds evidence to a payment dispute.
    
    Args:
        dispute_id: The eBay-assigned dispute ID
        evidence_type: Type of evidence
        evidence_content: Evidence content
    
    Returns:
        Added evidence details
    """
    payload = {
        "evidenceType": evidence_type,
        "evidenceContent": evidence_content,
    }
    
    return make_request("POST", f"/payment_dispute/{dispute_id}/add_evidence", data=payload)


@mcp.tool()
def update_evidence(dispute_id: str, evidence_id: str,
                     evidence_content: dict) -> dict:
    """
    Updates evidence for a payment dispute.
    
    Args:
        dispute_id: The eBay-assigned dispute ID
        evidence_id: The evidence ID
        evidence_content: Updated evidence content
    
    Returns:
        Updated evidence details
    """
    payload = {
        "evidenceContent": evidence_content,
    }
    
    return make_request("POST", f"/payment_dispute/{dispute_id}/update_evidence/{evidence_id}",
                       data=payload)


@mcp.tool()
def get_evidence_content(dispute_id: str, evidence_id: str) -> dict:
    """
    Fetches evidence content for a payment dispute.
    
    Args:
        dispute_id: The eBay-assigned dispute ID
        evidence_id: The evidence ID
    
    Returns:
        Evidence content
    """
    return make_request("GET", f"/payment_dispute/{dispute_id}/fetch_evidence_content/{evidence_id}")


@mcp.tool()
def upload_evidence_file(dispute_id: str, file_content: str,
                          content_type: str = "application/pdf") -> dict:
    """
    Uploads a file as evidence for a payment dispute.
    
    Args:
        dispute_id: The eBay-assigned dispute ID
        file_content: File content
        content_type: MIME type of the file
    
    Returns:
        Upload result
    """
    headers = {
        "Content-Type": content_type,
    }
    
    return make_request("POST", f"/payment_dispute/{dispute_id}/upload_evidence_file",
                       headers=headers, data=file_content)


@mcp.tool()
def get_dispute_activities(dispute_id: str) -> dict:
    """
    Retrieves activities for a payment dispute.
    
    Args:
        dispute_id: The eBay-assigned dispute ID
    
    Returns:
        Dispute activity collection
    """
    return make_request("GET", f"/payment_dispute/{dispute_id}/activity")


# =============================================================================
# TRANSFER TOOLS
# =============================================================================

@mcp.tool()
def get_transfer(transfer_id: str, marketplace_id: str = None) -> dict:
    """
    Retrieves a specific transfer by ID.
    
    Args:
        transfer_id: The eBay-assigned transfer ID
        marketplace_id: eBay marketplace ID
    
    Returns:
        Transfer details
    """
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    
    return make_request("GET", f"/transfer/{transfer_id}", headers=headers)


# =============================================================================
# NEGOTIATION TOOLS
# =============================================================================

@mcp.tool()
def find_eligible_items(filter: str = None, limit: str = "25",
                        offset: str = "0") -> dict:
    """
    Finds items eligible for offers.
    
    Args:
        filter: Filter criteria
        limit: Maximum items per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Eligible items collection
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    
    return make_request("GET", "/eligible_items", params=params)


@mcp.tool()
def send_offer_to_interested_buyers(item_id: str, offer_details: dict) -> dict:
    """
    Sends an offer to interested buyers.
    
    Args:
        item_id: eBay listing ID
        offer_details: Offer details including price and quantity
    
    Returns:
        Offer send results
    """
    return make_request("POST", f"/item/{item_id}/send_offer", data=offer_details)


# =============================================================================
# RECOMMENDATION TOOLS
# =============================================================================

@mcp.tool()
def find_listing_recommendations(filter: str = None, limit: str = "25",
                                  offset: str = "0") -> dict:
    """
    Finds listing recommendations.
    
    Args:
        filter: Filter criteria
        limit: Maximum recommendations per page (default: 25)
        offset: Page number (default: 0)
    
    Returns:
        Listing recommendation collection
    """
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    
    return make_request("GET", "/listing_recommendations", params=params)


# =============================================================================
# METADATA TOOLS
# =============================================================================

@mcp.tool()
def get_currencies() -> dict:
    """
    Retrieves available currencies.
    
    Returns:
        Currency list
    """
    return make_request("GET", "/currency")


@mcp.tool()
def get_category_policies(category_id: str = None, filter: str = None) -> dict:
    """
    Retrieves category policies.
    
    Args:
        category_id: Specific category ID (optional)
        filter: Filter criteria
    
    Returns:
        Category policy collection
    """
    params = {}
    if filter:
        params["filter"] = filter
    
    path = "/category_policy"
    if category_id:
        path = f"/category_policy/{category_id}"
    
    return make_request("GET", path, params=params)


@mcp.tool()
def get_listing_structure_policies(category_id: str = None) -> dict:
    """
    Retrieves listing structure policies.
    
    Args:
        category_id: Specific category ID (optional)
    
    Returns:
        Listing structure policy collection
    """
    path = "/listing_structure_policy"
    if category_id:
        path = f"/listing_structure_policy/{category_id}"
    
    return make_request("GET", path)


@mcp.tool()
def get_item_condition_policies(category_id: str = None, filter: str = None) -> dict:
    """
    Retrieves item condition policies.
    
    Args:
        category_id: Specific category ID (optional)
        filter: Filter criteria
    
    Returns:
        Item condition policy collection
    """
    params = {}
    if filter:
        params["filter"] = filter
    
    path = "/item_condition_policy"
    if category_id:
        path = f"/item_condition_policy/{category_id}"
    
    return make_request("GET", path, params=params)


@mcp.tool()
def get_product_compatibilities(seller_sku: str) -> dict:
    """
    Retrieves product compatibilities for an inventory item.
    
    Args:
        seller_sku: Seller-defined SKU
    
    Returns:
        Product compatibility collection
    """
    return make_request("GET", f"/inventory_item/{seller_sku}/product_compatibility")


@mcp.tool()
def create_or_replace_product_compatibility(seller_sku: str,
                                             compatibilities: list) -> dict:
    """
    Creates or replaces product compatibilities.
    
    Args:
        seller_sku: Seller-defined SKU
        compatibilities: List of compatibility definitions
    
    Returns:
        Response with operation status
    """
    payload = {
        "compatibilities": compatibilities,
    }
    
    return make_request("PUT", f"/inventory_item/{seller_sku}/product_compatibility",
                       data=payload)


@mcp.tool()
def delete_product_compatibility(seller_sku: str, compatibility_id: str) -> dict:
    """
    Deletes a product compatibility.
    
    Args:
        seller_sku: Seller-defined SKU
        compatibility_id: Compatibility ID
    
    Returns:
        Response with delete status
    """
    return make_request("DELETE", f"/inventory_item/{seller_sku}/product_compatibility/{compatibility_id}")


@mcp.tool()
def get_automotive_parts_compatibility_policies() -> dict:
    """
    Retrieves automotive parts compatibility policies.
    
    Returns:
        Automotive parts compatibility policy collection
    """
    return make_request("GET", "/automotive_parts_compatibility_policy")


@mcp.tool()
def get_compatibilities_by_specification(specifications: dict) -> dict:
    """
    Gets compatibilities by specification.
    
    Args:
        specifications: Specification criteria
    
    Returns:
        Compatibility list
    """
    return make_request("POST", "/compatibilities_by_specification",
                       data={"specifications": specifications})


@mcp.tool()
def get_compatibility_property_names(category_id: str) -> dict:
    """
    Gets compatibility property names for a category.
    
    Args:
        category_id: eBay category ID
    
    Returns:
        Compatibility property names
    """
    return make_request("GET", f"/compatibility_property_names/{category_id}")


@mcp.tool()
def get_compatibility_property_values(category_id: str, property_name: str) -> dict:
    """
    Gets compatibility property values for a category.
    
    Args:
        category_id: eBay category ID
        property_name: Property name
    
    Returns:
        Compatibility property values
    """
    return make_request("GET", f"/compatibility_property_values/{category_id}/{property_name}")


@mcp.tool()
def get_multi_compatibility_property_values(category_id: str,
                                            property_names: list) -> dict:
    """
    Gets multiple compatibility property values.
    
    Args:
        category_id: eBay category ID
        property_names: List of property names
    
    Returns:
        Multi-compatibility property values
    """
    payload = {
        "propertyNames": property_names,
    }
    
    return make_request("POST", f"/multi_compatibility_property_values/{category_id}",
                       data=payload)


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    # Validate environment variables
    required_vars = ["EBAY_APP_ID", "EBAY_CERT_ID", "EBAY_REFRESH_TOKEN"]
    missing = [var for var in required_vars if not os.environ.get(var)]
    if missing:
        print(f"Warning: Missing required environment variables: {', '.join(missing)}")
    
    print(f"Running eBay Sell API MCP Server (Environment: {EBAY_ENVIRONMENT})")
    
    # Run the server over stdio
    mcp.run()
