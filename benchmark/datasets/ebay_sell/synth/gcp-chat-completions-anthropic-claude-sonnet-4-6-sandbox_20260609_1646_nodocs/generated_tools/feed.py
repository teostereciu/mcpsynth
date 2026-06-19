"""
eBay Sell Feed API tools.
Covers: feed tasks (upload/download), feed types, schedules, customer service metrics.
"""

from typing import Optional
from auth import api_get, api_post, api_delete


# ---------------------------------------------------------------------------
# Feed Tasks
# ---------------------------------------------------------------------------

def get_feed_tasks(
    feed_type: Optional[str] = None,
    schedule_id: Optional[str] = None,
    look_back_days: Optional[int] = None,
    date_range: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Get a list of feed tasks.

    feed_type: e.g. "LMS_ORDER_REPORT", "LMS_ACTIVE_INVENTORY_REPORT",
               "LMS_ADD_ITEM", "LMS_REVISE_ITEM"
    look_back_days: number of days to look back (1-90)
    date_range: ISO 8601 date range filter
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if schedule_id:
        params["schedule_id"] = schedule_id
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    if date_range:
        params["date_range"] = date_range
    return api_get("/sell/feed/v1/task", params=params)


def get_feed_task(task_id: str) -> dict:
    """Get a specific feed task by ID."""
    return api_get(f"/sell/feed/v1/task/{task_id}")


def create_feed_task(body: dict) -> dict:
    """
    Create a feed task (upload or download).

    body fields:
      feedType: str (e.g. "LMS_ORDER_REPORT", "LMS_ADD_ITEM")
      marketplaceIds: list of str
      schemaVersion: str (optional)
      filterCriteria: dict (optional, for download tasks)
        - dateRange: dict with from and to
        - listingFormat: str
        - listingStatus: str
    """
    return api_post("/sell/feed/v1/task", body=body)


def delete_feed_task(task_id: str) -> dict:
    """Delete a feed task."""
    return api_delete(f"/sell/feed/v1/task/{task_id}")


def get_input_file_for_task(task_id: str) -> dict:
    """Get the input file associated with an upload task."""
    return api_get(f"/sell/feed/v1/task/{task_id}/download_input_file")


def get_result_file_for_task(task_id: str) -> dict:
    """Get the result/output file for a completed task."""
    return api_get(f"/sell/feed/v1/task/{task_id}/download_result_file")


# ---------------------------------------------------------------------------
# Feed Types
# ---------------------------------------------------------------------------

def get_feed_types(
    feed_scope: Optional[str] = None,
    marketplace_ids: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Get available feed types.

    feed_scope: "SELLER" or "BUYER"
    marketplace_ids: comma-separated marketplace IDs
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_scope:
        params["feed_scope"] = feed_scope
    if marketplace_ids:
        params["marketplace_ids"] = marketplace_ids
    return api_get("/sell/feed/v1/feed_type", params=params)


def get_feed_type(feed_type: str) -> dict:
    """Get details about a specific feed type."""
    return api_get(f"/sell/feed/v1/feed_type/{feed_type}")


# ---------------------------------------------------------------------------
# Schedules
# ---------------------------------------------------------------------------

def get_schedules(
    feed_type: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """Get all feed schedules, optionally filtered by feed type."""
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    return api_get("/sell/feed/v1/schedule", params=params)


def get_schedule(schedule_id: str) -> dict:
    """Get a specific feed schedule by ID."""
    return api_get(f"/sell/feed/v1/schedule/{schedule_id}")


def create_schedule(body: dict) -> dict:
    """
    Create a feed schedule.

    body fields:
      feedType: str
      marketplaceIds: list of str
      preferredTriggerDayOfMonth: int (optional)
      preferredTriggerDayOfWeek: str (optional)
      preferredTriggerHour: str (optional, "HH:MM:SS" format)
      scheduleStartDate: str (ISO 8601)
      scheduleEndDate: str (ISO 8601, optional)
      scheduleName: str
      schemaVersion: str (optional)
    """
    return api_post("/sell/feed/v1/schedule", body=body)


def update_schedule(schedule_id: str, body: dict) -> dict:
    """Update an existing feed schedule."""
    from auth import api_put
    return api_put(f"/sell/feed/v1/schedule/{schedule_id}", body=body)


def delete_schedule(schedule_id: str) -> dict:
    """Delete a feed schedule."""
    return api_delete(f"/sell/feed/v1/schedule/{schedule_id}")


def get_latest_result_file_for_schedule(schedule_id: str) -> dict:
    """Get the most recent result file for a scheduled feed."""
    return api_get(f"/sell/feed/v1/schedule/{schedule_id}/download_result_file")


# ---------------------------------------------------------------------------
# Customer Service Metrics (via Feed)
# ---------------------------------------------------------------------------

def get_customer_service_metric_tasks(
    feed_type: Optional[str] = None,
    look_back_days: Optional[int] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """Get customer service metric tasks."""
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    return api_get("/sell/feed/v1/customer_service_metric_task", params=params)


def get_customer_service_metric_task(task_id: str) -> dict:
    """Get a specific customer service metric task."""
    return api_get(f"/sell/feed/v1/customer_service_metric_task/{task_id}")


def create_customer_service_metric_task(body: dict) -> dict:
    """
    Create a customer service metric task.

    body fields:
      feedType: str (e.g. "CUSTOMER_SERVICE_METRICS_REPORT")
      filterCriteria: dict with evaluationMarketplaceId, customerServiceMetricType,
                      evaluationCycleType
      schemaVersion: str
    """
    return api_post("/sell/feed/v1/customer_service_metric_task", body=body)


# ---------------------------------------------------------------------------
# Inventory Upload Tasks (Large Merchant Services)
# ---------------------------------------------------------------------------

def get_inventory_tasks(
    feed_type: Optional[str] = None,
    look_back_days: Optional[int] = None,
    date_range: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """Get inventory upload/download tasks."""
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    if date_range:
        params["date_range"] = date_range
    return api_get("/sell/feed/v1/inventory_task", params=params)


def get_inventory_task(task_id: str) -> dict:
    """Get a specific inventory task."""
    return api_get(f"/sell/feed/v1/inventory_task/{task_id}")


def create_inventory_task(body: dict) -> dict:
    """
    Create an inventory task.

    body fields:
      feedType: str (e.g. "LMS_ACTIVE_INVENTORY_REPORT")
      marketplaceIds: list of str
      schemaVersion: str (optional)
      filterCriteria: dict (optional)
    """
    return api_post("/sell/feed/v1/inventory_task", body=body)


# ---------------------------------------------------------------------------
# Order Tasks
# ---------------------------------------------------------------------------

def get_order_tasks(
    order_ids: Optional[str] = None,
    feed_type: Optional[str] = None,
    look_back_days: Optional[int] = None,
    date_range: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """Get order download tasks."""
    params: dict = {"limit": limit, "offset": offset}
    if order_ids:
        params["order_ids"] = order_ids
    if feed_type:
        params["feed_type"] = feed_type
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    if date_range:
        params["date_range"] = date_range
    return api_get("/sell/feed/v1/order_task", params=params)


def get_order_task(task_id: str) -> dict:
    """Get a specific order task."""
    return api_get(f"/sell/feed/v1/order_task/{task_id}")


def create_order_task(body: dict) -> dict:
    """
    Create an order download task.

    body fields:
      feedType: str (e.g. "LMS_ORDER_REPORT")
      marketplaceIds: list of str
      schemaVersion: str (optional)
      filterCriteria: dict with dateRange, listingFormat, listingStatus
    """
    return api_post("/sell/feed/v1/order_task", body=body)
