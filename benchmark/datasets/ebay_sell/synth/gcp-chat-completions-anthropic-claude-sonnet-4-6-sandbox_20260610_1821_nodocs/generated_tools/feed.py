"""
eBay Sell Feed API tools.
Covers: feed types, tasks (upload/download), schedules, and file management.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-feed")

# ---------------------------------------------------------------------------
# Feed Types
# ---------------------------------------------------------------------------

@mcp.tool()
def get_feed_types(
    feed_scope: str | None = None,
    marketplace_ids: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve available feed types for the seller.

    Args:
        feed_scope: Filter by scope: ALL_ACTIVE, NEWLY_LISTED (optional).
        marketplace_ids: Comma-separated marketplace IDs to filter by (optional).
        limit: Number of feed types to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_scope:
        params["feed_scope"] = feed_scope
    if marketplace_ids:
        params["marketplace_ids"] = marketplace_ids
    return ebay_request("GET", "/sell/feed/v1/feed_type", params=params)


@mcp.tool()
def get_feed_type(feed_type: str) -> dict:
    """
    Retrieve details about a specific feed type.

    Args:
        feed_type: The feed type identifier, e.g. 'LMS_ACTIVE_INVENTORY_REPORT'.
    """
    return ebay_request("GET", f"/sell/feed/v1/feed_type/{feed_type}")


# ---------------------------------------------------------------------------
# Tasks (Upload / Download)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_tasks(
    feed_type: str | None = None,
    date_range: str | None = None,
    look_back_days: int | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve feed tasks for the seller.

    Args:
        feed_type: Filter by feed type, e.g. 'LMS_ORDER_ACK' (optional).
        date_range: Date range filter in format 'YYYY-MM-DDTHH:MM:SS.000Z..' (optional).
        look_back_days: Number of past days to include (optional).
        limit: Number of tasks to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if date_range:
        params["date_range"] = date_range
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    return ebay_request("GET", "/sell/feed/v1/task", params=params)


@mcp.tool()
def get_task(task_id: str) -> dict:
    """
    Retrieve a specific feed task by its ID.

    Args:
        task_id: The unique identifier of the feed task.
    """
    return ebay_request("GET", f"/sell/feed/v1/task/{task_id}")


@mcp.tool()
def create_task(task: dict) -> dict:
    """
    Create a new feed task (upload or download).

    Args:
        task: Task object with feedType, marketplaceId, and optional
              schemaVersion and filterCriteria fields.
              Example: {
                "feedType": "LMS_ACTIVE_INVENTORY_REPORT",
                "marketplaceId": "EBAY_US",
                "schemaVersion": "1.0"
              }
    """
    return ebay_request("POST", "/sell/feed/v1/task", json=task)


@mcp.tool()
def delete_task(task_id: str) -> dict:
    """
    Delete a feed task.

    Args:
        task_id: The unique identifier of the feed task to delete.
    """
    return ebay_request("DELETE", f"/sell/feed/v1/task/{task_id}")


@mcp.tool()
def get_input_file(task_id: str) -> dict:
    """
    Download the input file associated with an upload task.

    Args:
        task_id: The unique identifier of the feed task.
    """
    return ebay_request("GET", f"/sell/feed/v1/task/{task_id}/download_file")


@mcp.tool()
def get_result_file(task_id: str) -> dict:
    """
    Download the result/output file for a completed feed task.

    Args:
        task_id: The unique identifier of the completed feed task.
    """
    return ebay_request(
        "GET",
        f"/sell/feed/v1/task/{task_id}/download_file",
        params={"fileType": "RESULT"},
    )


# ---------------------------------------------------------------------------
# Schedules
# ---------------------------------------------------------------------------

@mcp.tool()
def get_schedules(
    feed_type: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve feed schedules for the seller.

    Args:
        feed_type: Filter by feed type (optional).
        limit: Number of schedules to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    return ebay_request("GET", "/sell/feed/v1/schedule", params=params)


@mcp.tool()
def get_schedule(schedule_id: str) -> dict:
    """
    Retrieve a specific feed schedule by its ID.

    Args:
        schedule_id: The unique identifier of the schedule.
    """
    return ebay_request("GET", f"/sell/feed/v1/schedule/{schedule_id}")


@mcp.tool()
def create_schedule(schedule: dict) -> dict:
    """
    Create a new feed schedule for automated recurring feed generation.

    Args:
        schedule: Schedule object with feedType, marketplaceId, scheduleTemplateId,
                  scheduleName, preferredTriggerHour, and optional schemaVersion.
                  Example: {
                    "feedType": "LMS_ACTIVE_INVENTORY_REPORT",
                    "marketplaceId": "EBAY_US",
                    "scheduleTemplateId": "template-id",
                    "scheduleName": "Daily Inventory Report",
                    "preferredTriggerHour": "02"
                  }
    """
    return ebay_request("POST", "/sell/feed/v1/schedule", json=schedule)


@mcp.tool()
def update_schedule(schedule_id: str, schedule: dict) -> dict:
    """
    Update an existing feed schedule.

    Args:
        schedule_id: The unique identifier of the schedule to update.
        schedule: Updated schedule object.
    """
    return ebay_request(
        "PUT",
        f"/sell/feed/v1/schedule/{schedule_id}",
        json=schedule,
    )


@mcp.tool()
def delete_schedule(schedule_id: str) -> dict:
    """
    Delete a feed schedule.

    Args:
        schedule_id: The unique identifier of the schedule to delete.
    """
    return ebay_request("DELETE", f"/sell/feed/v1/schedule/{schedule_id}")


@mcp.tool()
def get_schedule_templates(
    feed_type: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve available schedule templates for feed scheduling.

    Args:
        feed_type: Filter by feed type (optional).
        limit: Number of templates to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    return ebay_request("GET", "/sell/feed/v1/schedule_template", params=params)


@mcp.tool()
def get_schedule_template(schedule_template_id: str) -> dict:
    """
    Retrieve a specific schedule template by its ID.

    Args:
        schedule_template_id: The unique identifier of the schedule template.
    """
    return ebay_request(
        "GET",
        f"/sell/feed/v1/schedule_template/{schedule_template_id}",
    )


# ---------------------------------------------------------------------------
# Customer Service Metric Tasks
# ---------------------------------------------------------------------------

@mcp.tool()
def get_customer_service_metric_tasks(
    feed_type: str | None = None,
    look_back_days: int | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve customer service metric feed tasks.

    Args:
        feed_type: Filter by feed type (optional).
        look_back_days: Number of past days to include (optional).
        limit: Number of tasks to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    return ebay_request(
        "GET",
        "/sell/feed/v1/customer_service_metric_task",
        params=params,
    )


@mcp.tool()
def create_customer_service_metric_task(task: dict) -> dict:
    """
    Create a customer service metric feed task.

    Args:
        task: Task object with feedType, marketplaceId, and filterCriteria.
    """
    return ebay_request(
        "POST",
        "/sell/feed/v1/customer_service_metric_task",
        json=task,
    )


@mcp.tool()
def get_customer_service_metric_task(task_id: str) -> dict:
    """
    Retrieve a specific customer service metric task.

    Args:
        task_id: The unique identifier of the task.
    """
    return ebay_request(
        "GET",
        f"/sell/feed/v1/customer_service_metric_task/{task_id}",
    )


# ---------------------------------------------------------------------------
# Inventory Tasks (Large Merchant Services)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_inventory_tasks(
    feed_type: str | None = None,
    look_back_days: int | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve inventory feed tasks (LMS-style bulk inventory operations).

    Args:
        feed_type: Filter by feed type, e.g. 'LMS_ADD_ITEM' (optional).
        look_back_days: Number of past days to include (optional).
        limit: Number of tasks to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    return ebay_request("GET", "/sell/feed/v1/inventory_task", params=params)


@mcp.tool()
def create_inventory_task(task: dict) -> dict:
    """
    Create an inventory feed task for bulk listing operations.

    Args:
        task: Task object with feedType, marketplaceId, and optional
              schemaVersion and filterCriteria.
              Common feedTypes: LMS_ADD_ITEM, LMS_REVISE_ITEM,
              LMS_RELIST_ITEM, LMS_END_ITEM, LMS_ACTIVE_INVENTORY_REPORT.
    """
    return ebay_request("POST", "/sell/feed/v1/inventory_task", json=task)


@mcp.tool()
def get_inventory_task(task_id: str) -> dict:
    """
    Retrieve a specific inventory feed task.

    Args:
        task_id: The unique identifier of the inventory task.
    """
    return ebay_request("GET", f"/sell/feed/v1/inventory_task/{task_id}")


# ---------------------------------------------------------------------------
# Order Tasks
# ---------------------------------------------------------------------------

@mcp.tool()
def get_order_tasks(
    feed_type: str | None = None,
    look_back_days: int | None = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve order feed tasks (e.g. order acknowledgement, shipping updates).

    Args:
        feed_type: Filter by feed type, e.g. 'LMS_ORDER_ACK' (optional).
        look_back_days: Number of past days to include (optional).
        limit: Number of tasks to return (default 10).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    return ebay_request("GET", "/sell/feed/v1/order_task", params=params)


@mcp.tool()
def create_order_task(task: dict) -> dict:
    """
    Create an order feed task for bulk order processing.

    Args:
        task: Task object with feedType, marketplaceId, and optional
              schemaVersion and filterCriteria.
              Common feedTypes: LMS_ORDER_ACK, LMS_SHIP_TO_HOME_SHIPMENT.
    """
    return ebay_request("POST", "/sell/feed/v1/order_task", json=task)


@mcp.tool()
def get_order_task(task_id: str) -> dict:
    """
    Retrieve a specific order feed task.

    Args:
        task_id: The unique identifier of the order task.
    """
    return ebay_request("GET", f"/sell/feed/v1/order_task/{task_id}")
