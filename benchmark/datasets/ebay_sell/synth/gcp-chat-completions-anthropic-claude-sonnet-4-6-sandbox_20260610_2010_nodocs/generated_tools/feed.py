"""
eBay Sell Feed API tools.
Covers: feed types, tasks (upload/download), schedules, and file upload.
"""

import os
import requests
from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post, api_delete, get_base_url, auth_headers

mcp = FastMCP("ebay-feed")


# ── Feed Types ───────────────────────────────────────────────────────────────

@mcp.tool()
def get_feed_types(feed_scope: str | None = None,
                   marketplace_ids: str | None = None,
                   limit: int = 10,
                   offset: int = 0) -> dict:
    """
    Retrieve available feed types.

    Args:
        feed_scope: Filter by scope (e.g. SELLER).
        marketplace_ids: Comma-separated marketplace IDs.
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_scope:
        params["feed_scope"] = feed_scope
    if marketplace_ids:
        params["marketplace_ids"] = marketplace_ids
    return api_get("/sell/feed/v1/feed_type", params=params)


@mcp.tool()
def get_feed_type(feed_type_name: str) -> dict:
    """
    Retrieve details for a specific feed type.

    Args:
        feed_type_name: The feed type name (e.g. LMS_ACTIVE_INVENTORY_REPORT).
    """
    return api_get(f"/sell/feed/v1/feed_type/{feed_type_name}")


# ── Tasks ────────────────────────────────────────────────────────────────────

@mcp.tool()
def get_tasks(feed_type: str | None = None,
              schedule_id: str | None = None,
              look_back_days: int | None = None,
              date_range: str | None = None,
              limit: int = 10,
              offset: int = 0) -> dict:
    """
    Retrieve feed tasks.

    Args:
        feed_type: Filter by feed type name.
        schedule_id: Filter by schedule ID.
        look_back_days: Number of days to look back for tasks.
        date_range: Date range filter string.
        limit: Results per page.
        offset: Pagination offset.
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


@mcp.tool()
def get_task(task_id: str) -> dict:
    """
    Retrieve a single feed task by ID.

    Args:
        task_id: The task ID.
    """
    return api_get(f"/sell/feed/v1/task/{task_id}")


@mcp.tool()
def create_task(feed_type: str, marketplace_id: str,
                schema_version: str | None = None,
                filter_criteria: dict | None = None) -> dict:
    """
    Create a new feed task (e.g. to generate a report or upload data).

    Args:
        feed_type: Feed type name (e.g. LMS_ACTIVE_INVENTORY_REPORT).
        marketplace_id: eBay marketplace ID.
        schema_version: Optional schema version string.
        filter_criteria: Optional filter criteria dict.
    """
    body: dict = {
        "feedType": feed_type,
        "marketplaceIds": [marketplace_id],
    }
    if schema_version:
        body["schemaVersion"] = schema_version
    if filter_criteria:
        body["filterCriteria"] = filter_criteria
    return api_post("/sell/feed/v1/task", body=body)


@mcp.tool()
def delete_task(task_id: str) -> dict:
    """
    Delete a feed task.

    Args:
        task_id: The task ID to delete.
    """
    return api_delete(f"/sell/feed/v1/task/{task_id}")


@mcp.tool()
def get_task_input_file(task_id: str) -> dict:
    """
    Retrieve the input file associated with a feed task.

    Args:
        task_id: The task ID.
    """
    url = get_base_url() + f"/sell/feed/v1/task/{task_id}/download_input_file"
    try:
        r = requests.get(url, headers=auth_headers(), timeout=60)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"content_type": r.headers.get("Content-Type"), "size_bytes": len(r.content),
                "content_preview": r.text[:500] if r.text else None}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_task_result_file(task_id: str) -> dict:
    """
    Retrieve the result file for a completed feed task.

    Args:
        task_id: The task ID.
    """
    url = get_base_url() + f"/sell/feed/v1/task/{task_id}/download_result_file"
    try:
        r = requests.get(url, headers=auth_headers(), timeout=60)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"content_type": r.headers.get("Content-Type"), "size_bytes": len(r.content),
                "content_preview": r.text[:2000] if r.text else None}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def upload_task_input_file(task_id: str, file_path: str,
                            content_type: str = "text/xml") -> dict:
    """
    Upload an input file for a feed task from the local filesystem.

    Args:
        task_id: The task ID.
        file_path: Absolute or relative path to the file to upload.
        content_type: MIME type of the file (default text/xml).
    """
    url = get_base_url() + f"/sell/feed/v1/task/{task_id}/upload_file"
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
        headers = auth_headers()
        headers.pop("Content-Type", None)
        r = requests.post(
            url,
            headers=headers,
            files={"file": (os.path.basename(file_path), file_data, content_type)},
            timeout=120,
        )
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json() if r.text else {"status": "uploaded"}
    except Exception as e:
        return {"error": str(e)}


# ── Schedules ────────────────────────────────────────────────────────────────

@mcp.tool()
def get_schedules(feed_type: str | None = None,
                  limit: int = 10,
                  offset: int = 0) -> dict:
    """
    Retrieve feed schedules.

    Args:
        feed_type: Filter by feed type name.
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    return api_get("/sell/feed/v1/schedule", params=params)


@mcp.tool()
def get_schedule(schedule_id: str) -> dict:
    """
    Retrieve a single feed schedule by ID.

    Args:
        schedule_id: The schedule ID.
    """
    return api_get(f"/sell/feed/v1/schedule/{schedule_id}")


@mcp.tool()
def create_schedule(feed_type: str, marketplace_id: str,
                    schedule_name: str,
                    preferred_trigger_cron_expression: str,
                    schema_version: str | None = None,
                    filter_criteria: dict | None = None) -> dict:
    """
    Create a recurring feed schedule.

    Args:
        feed_type: Feed type name.
        marketplace_id: eBay marketplace ID.
        schedule_name: Human-readable name for the schedule.
        preferred_trigger_cron_expression: Cron expression for the schedule.
        schema_version: Optional schema version.
        filter_criteria: Optional filter criteria dict.
    """
    body: dict = {
        "feedType": feed_type,
        "marketplaceIds": [marketplace_id],
        "scheduleName": schedule_name,
        "preferredTriggerCronExpression": preferred_trigger_cron_expression,
    }
    if schema_version:
        body["schemaVersion"] = schema_version
    if filter_criteria:
        body["filterCriteria"] = filter_criteria
    return api_post("/sell/feed/v1/schedule", body=body)


@mcp.tool()
def update_schedule(schedule_id: str,
                    schedule_name: str | None = None,
                    preferred_trigger_cron_expression: str | None = None,
                    filter_criteria: dict | None = None) -> dict:
    """
    Update an existing feed schedule.

    Args:
        schedule_id: The schedule ID to update.
        schedule_name: New schedule name.
        preferred_trigger_cron_expression: New cron expression.
        filter_criteria: New filter criteria dict.
    """
    body: dict = {}
    if schedule_name:
        body["scheduleName"] = schedule_name
    if preferred_trigger_cron_expression:
        body["preferredTriggerCronExpression"] = preferred_trigger_cron_expression
    if filter_criteria:
        body["filterCriteria"] = filter_criteria
    from .auth import auth_headers, get_base_url
    import requests
    url = get_base_url() + f"/sell/feed/v1/schedule/{schedule_id}"
    try:
        r = requests.put(url, headers=auth_headers(), json=body, timeout=30)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json() if r.text else {"status": "ok"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def delete_schedule(schedule_id: str) -> dict:
    """
    Delete a feed schedule.

    Args:
        schedule_id: The schedule ID to delete.
    """
    return api_delete(f"/sell/feed/v1/schedule/{schedule_id}")


@mcp.tool()
def get_schedule_template(schedule_template_id: str) -> dict:
    """
    Retrieve a schedule template by ID.

    Args:
        schedule_template_id: The schedule template ID.
    """
    return api_get(f"/sell/feed/v1/schedule_template/{schedule_template_id}")


@mcp.tool()
def get_schedule_templates(feed_type: str | None = None,
                            limit: int = 10,
                            offset: int = 0) -> dict:
    """
    Retrieve available schedule templates.

    Args:
        feed_type: Filter by feed type.
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if feed_type:
        params["feed_type"] = feed_type
    return api_get("/sell/feed/v1/schedule_template", params=params)
