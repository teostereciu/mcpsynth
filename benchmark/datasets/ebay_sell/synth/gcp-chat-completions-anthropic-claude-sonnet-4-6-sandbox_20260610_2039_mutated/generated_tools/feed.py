"""eBay Sell Feed API tools."""
from typing import Any, Optional
from .client import get_client


# --- Tasks ---

def create_task(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Create an upload or download task without filter criteria."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/feed/v1/task", json=body, headers=headers)


def get_tasks(
    feed_type: Optional[str] = None,
    schedule_id: Optional[str] = None,
    date_range: Optional[str] = None,
    look_back_days: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve details and status for tasks based on feed type or schedule ID."""
    client = get_client()
    params = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if schedule_id is not None:
        params["schedule_id"] = schedule_id
    if date_range is not None:
        params["date_range"] = date_range
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/task", params=params)


def get_task(task_id: str) -> dict:
    """Retrieve the details and status of a specific task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/task/{task_id}")


def get_result_file(task_id: str) -> dict:
    """Retrieve the generated result file associated with a completed task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/task/{task_id}/download_result_file")


def get_input_file(task_id: str) -> dict:
    """Retrieve the input file associated with a task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/task/{task_id}/download_input_file")


def upload_file(task_id: str, file_data: bytes, filename: str = "upload.xml") -> dict:
    """Upload a file and associate it with the specified task ID."""
    client = get_client()
    files = {"file": (filename, file_data, "application/octet-stream")}
    return client.request("POST", f"/sell/feed/v1/task/{task_id}/upload_file", files=files)


# --- Order Tasks ---

def create_order_task(body: dict) -> dict:
    """Create an order download task with filter criteria for the order report."""
    client = get_client()
    return client.request("POST", "/sell/feed/v1/order_task", json=body)


def get_order_tasks(
    feed_type: Optional[str] = None,
    schedule_id: Optional[str] = None,
    date_range: Optional[str] = None,
    look_back_days: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve details and status for order tasks."""
    client = get_client()
    params = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if schedule_id is not None:
        params["schedule_id"] = schedule_id
    if date_range is not None:
        params["date_range"] = date_range
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/order_task", params=params)


def get_order_task(task_id: str) -> dict:
    """Retrieve the details and status of a specific order task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/order_task/{task_id}")


# --- Inventory Tasks ---

def create_inventory_task(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Create an inventory-related download task."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/feed/v1/inventory_task", json=body, headers=headers)


def get_inventory_tasks(
    feed_type: Optional[str] = None,
    schedule_id: Optional[str] = None,
    date_range: Optional[str] = None,
    look_back_days: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve details and status for inventory tasks."""
    client = get_client()
    params = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if schedule_id is not None:
        params["schedule_id"] = schedule_id
    if date_range is not None:
        params["date_range"] = date_range
    if look_back_days is not None:
        params["look_back_days"] = look_back_days
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/inventory_task", params=params)


def get_inventory_task(task_id: str) -> dict:
    """Retrieve the details and status of a specific inventory task."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/inventory_task/{task_id}")


# --- Schedules ---

def create_schedule(body: dict) -> dict:
    """Create a schedule (subscription to a schedule template) for periodic reports."""
    client = get_client()
    return client.request("POST", "/sell/feed/v1/schedule", json=body)


def get_schedules(
    feed_type: str,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve all schedules for a specified feed type."""
    client = get_client()
    params = {"feed_type": feed_type}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/schedule", params=params)


def get_schedule(schedule_id: str) -> dict:
    """Retrieve schedule details and status for a specific schedule."""
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


def get_schedule_template(schedule_template_id: str) -> dict:
    """Retrieve details of a specific schedule template."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/schedule_template/{schedule_template_id}")


def get_schedule_templates(
    feed_type: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve all schedule templates."""
    client = get_client()
    params = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/schedule_template", params=params)


def get_latest_result_file(schedule_id: str) -> dict:
    """Retrieve the latest result file for a schedule."""
    client = get_client()
    return client.request("GET", f"/sell/feed/v1/schedule/{schedule_id}/download_result_file")
