"""eBay Sell Feed API tools."""
from typing import Optional
from .client import get_client


def create_task(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Create an upload or download task for a specified feed type."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/feed/v1/task", json=body, extra_headers=headers)


def get_tasks(feed_type: Optional[str] = None, schedule_id: Optional[str] = None,
              date_range: Optional[str] = None, look_back_days: Optional[str] = None,
              limit: Optional[str] = None, offset: Optional[str] = None) -> dict:
    """Retrieve details and status for tasks based on feed type or schedule ID."""
    client = get_client()
    params = {}
    if feed_type:
        params["feed_type"] = feed_type
    if schedule_id:
        params["schedule_id"] = schedule_id
    if date_range:
        params["date_range"] = date_range
    if look_back_days:
        params["look_back_days"] = look_back_days
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/task", params=params)


def get_task(task_id: str) -> dict:
    """Retrieve the details and status of a specific task by task ID."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/task/{task_id}")


def get_result_file(task_id: str) -> dict:
    """Download the result file associated with a completed task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/task/{task_id}/download_result_file")


def get_input_file(task_id: str) -> dict:
    """Download the input file previously uploaded for a task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/task/{task_id}/download_input_file")


def create_order_task(body: dict) -> dict:
    """Create an order download task with filter criteria for the order report."""
    client = get_client()
    return client.request("POST", "/sell/feed/v1/order_task", json=body)


def get_order_tasks(feed_type: Optional[str] = None, schedule_id: Optional[str] = None,
                    date_range: Optional[str] = None, look_back_days: Optional[str] = None,
                    limit: Optional[str] = None, offset: Optional[str] = None) -> dict:
    """Retrieve details and status for order tasks based on feed type or schedule ID."""
    client = get_client()
    params = {}
    if feed_type:
        params["feed_type"] = feed_type
    if schedule_id:
        params["schedule_id"] = schedule_id
    if date_range:
        params["date_range"] = date_range
    if look_back_days:
        params["look_back_days"] = look_back_days
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/order_task", params=params)


def get_order_task(task_id: str) -> dict:
    """Retrieve details and status of a specific order task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/order_task/{task_id}")


def create_inventory_task(body: dict) -> dict:
    """Create an inventory-related download task for a specified feed type."""
    client = get_client()
    return client.request("POST", "/sell/feed/v1/inventory_task", json=body)


def get_inventory_tasks(feed_type: Optional[str] = None, date_range: Optional[str] = None,
                        look_back_days: Optional[str] = None, limit: Optional[str] = None,
                        offset: Optional[str] = None) -> dict:
    """Retrieve inventory tasks based on feed type and date filters."""
    client = get_client()
    params = {}
    if feed_type:
        params["feed_type"] = feed_type
    if date_range:
        params["date_range"] = date_range
    if look_back_days:
        params["look_back_days"] = look_back_days
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/inventory_task", params=params)


def get_inventory_task(task_id: str) -> dict:
    """Retrieve details and status of a specific inventory task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/inventory_task/{task_id}")


def create_schedule(body: dict) -> dict:
    """Create a schedule (subscription) to a schedule template for periodic report generation."""
    client = get_client()
    return client.request("POST", "/sell/feed/v1/schedule", json=body)


def get_schedules(feed_type: str, limit: Optional[str] = None, offset: Optional[str] = None) -> dict:
    """Retrieve all schedules for a specified feed type."""
    client = get_client()
    params = {"feed_type": feed_type}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/schedule", params=params)


def get_schedule(schedule_id: str) -> dict:
    """Retrieve schedule details and status for a specific schedule ID."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/schedule/{schedule_id}")


def update_schedule(schedule_id: str, body: dict) -> dict:
    """Update an existing schedule."""
    client = get_client()
    return client.request("PUT", f"/sell/feed/v1/schedule/{schedule_id}", json=body)


def delete_schedule(schedule_id: str) -> dict:
    """Delete an existing schedule."""
    client = get_client()
    return client.request("DELETE", f"/sell/feed/v1/schedule/{schedule_id}")


def get_latest_result_file(schedule_id: str) -> dict:
    """Download the latest result file for a schedule."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/schedule/{schedule_id}/download_result_file")


def get_schedule_template(schedule_template_id: str) -> dict:
    """Retrieve details of a specific schedule template."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/schedule_template/{schedule_template_id}")


def get_schedule_templates(feed_type: Optional[str] = None, limit: Optional[str] = None,
                           offset: Optional[str] = None) -> dict:
    """Retrieve all schedule templates, optionally filtered by feed type."""
    client = get_client()
    params = {}
    if feed_type:
        params["feed_type"] = feed_type
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/schedule_template", params=params)


def create_customer_service_metric_task(body: dict) -> dict:
    """Create a customer service metric task."""
    client = get_client()
    return client.request("POST", "/sell/feed/v1/customer_service_metric_task", json=body)


def get_customer_service_metric_tasks(feed_type: Optional[str] = None, date_range: Optional[str] = None,
                                       look_back_days: Optional[str] = None, limit: Optional[str] = None,
                                       offset: Optional[str] = None) -> dict:
    """Retrieve customer service metric tasks."""
    client = get_client()
    params = {}
    if feed_type:
        params["feed_type"] = feed_type
    if date_range:
        params["date_range"] = date_range
    if look_back_days:
        params["look_back_days"] = look_back_days
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/customer_service_metric_task", params=params)


def get_customer_service_metric_task(task_id: str) -> dict:
    """Retrieve a specific customer service metric task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/customer_service_metric_task/{task_id}")
