from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests

from .http import get_user_access_token, request_json

API_ROOT = "/sell/feed/v1"

# Feed API uses varying scopes depending on feedType; we allow caller to pass scope.
DEFAULT_SCOPE = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def register(mcp):
    @mcp.tool()
    def feed_create_task(payload: Dict[str, Any], *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """POST /task - Create an upload/download task."""
        return request_json(
            "POST",
            API_ROOT,
            "/task",
            scope=scope,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def feed_get_task(task_id: str, *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """GET /task/{task_id} - Get a task."""
        return request_json("GET", API_ROOT, f"/task/{task_id}", scope=scope)

    @mcp.tool()
    def feed_get_tasks(
        *,
        feed_type: Optional[str] = None,
        schedule_id: Optional[str] = None,
        created_date_range: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        scope: str = DEFAULT_SCOPE,
    ) -> Dict[str, Any]:
        """GET /task - Get tasks."""
        params: Dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if schedule_id is not None:
            params["schedule_id"] = schedule_id
        if created_date_range is not None:
            params["created_date_range"] = created_date_range
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json("GET", API_ROOT, "/task", scope=scope, params=params or None)

    @mcp.tool()
    def feed_upload_file(
        task_id: str,
        file_path: str,
        *,
        scope: str = DEFAULT_SCOPE,
    ) -> Dict[str, Any]:
        """POST /task/{task_id}/upload_file - Upload a file as multipart/form-data."""
        token = get_user_access_token(scope)
        env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
        base_url = "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"
        url = f"{base_url}{API_ROOT}/task/{task_id}/upload_file"

        try:
            with open(file_path, "rb") as f:
                files = {"file": (os.path.basename(file_path), f)}
                resp = requests.post(
                    url,
                    headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
                    files=files,
                    timeout=120,
                )
        except FileNotFoundError:
            return {"error": {"message": f"File not found: {file_path}"}}
        except requests.RequestException as e:
            return {"error": {"message": str(e)}}

        if resp.status_code >= 400:
            try:
                return {"error": {"status_code": resp.status_code, "details": resp.json()}}
            except Exception:
                return {"error": {"status_code": resp.status_code, "details": resp.text}}

        try:
            return resp.json()
        except Exception:
            return {"status": resp.status_code, "text": resp.text}

    @mcp.tool()
    def feed_get_result_file(task_id: str, *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """GET /task/{task_id}/download_result_file - Download result file (returns text)."""
        return request_json("GET", API_ROOT, f"/task/{task_id}/download_result_file", scope=scope)

    @mcp.tool()
    def feed_get_input_file(task_id: str, *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """GET /task/{task_id}/download_input_file - Download input file (returns text)."""
        return request_json("GET", API_ROOT, f"/task/{task_id}/download_input_file", scope=scope)

    # Inventory tasks
    @mcp.tool()
    def feed_create_inventory_task(payload: Dict[str, Any], *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """POST /inventory_task - Create an inventory task."""
        return request_json(
            "POST",
            API_ROOT,
            "/inventory_task",
            scope=scope,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def feed_get_inventory_task(task_id: str, *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """GET /inventory_task/{task_id} - Get an inventory task."""
        return request_json("GET", API_ROOT, f"/inventory_task/{task_id}", scope=scope)

    @mcp.tool()
    def feed_get_inventory_tasks(
        *,
        feed_type: Optional[str] = None,
        created_date_range: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        scope: str = DEFAULT_SCOPE,
    ) -> Dict[str, Any]:
        """GET /inventory_task - Get inventory tasks."""
        params: Dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if created_date_range is not None:
            params["created_date_range"] = created_date_range
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json("GET", API_ROOT, "/inventory_task", scope=scope, params=params or None)

    # Order tasks
    @mcp.tool()
    def feed_create_order_task(payload: Dict[str, Any], *, scope: str = "https://api.ebay.com/oauth/api_scope/sell.fulfillment") -> Dict[str, Any]:
        """POST /order_task - Create an order task."""
        return request_json(
            "POST",
            API_ROOT,
            "/order_task",
            scope=scope,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def feed_get_order_task(task_id: str, *, scope: str = "https://api.ebay.com/oauth/api_scope/sell.fulfillment") -> Dict[str, Any]:
        """GET /order_task/{task_id} - Get an order task."""
        return request_json("GET", API_ROOT, f"/order_task/{task_id}", scope=scope)

    @mcp.tool()
    def feed_get_order_tasks(
        *,
        feed_type: Optional[str] = None,
        created_date_range: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        scope: str = "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
    ) -> Dict[str, Any]:
        """GET /order_task - Get order tasks."""
        params: Dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if created_date_range is not None:
            params["created_date_range"] = created_date_range
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json("GET", API_ROOT, "/order_task", scope=scope, params=params or None)

    # Customer service metric tasks
    @mcp.tool()
    def feed_create_customer_service_metric_task(payload: Dict[str, Any], *, scope: str = "https://api.ebay.com/oauth/api_scope/sell.analytics") -> Dict[str, Any]:
        """POST /customer_service_metric_task - Create a customer service metric task."""
        return request_json(
            "POST",
            API_ROOT,
            "/customer_service_metric_task",
            scope=scope,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def feed_get_customer_service_metric_task(task_id: str, *, scope: str = "https://api.ebay.com/oauth/api_scope/sell.analytics") -> Dict[str, Any]:
        """GET /customer_service_metric_task/{task_id} - Get a customer service metric task."""
        return request_json("GET", API_ROOT, f"/customer_service_metric_task/{task_id}", scope=scope)

    @mcp.tool()
    def feed_get_customer_service_metric_tasks(
        *,
        feed_type: Optional[str] = None,
        created_date_range: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        scope: str = "https://api.ebay.com/oauth/api_scope/sell.analytics",
    ) -> Dict[str, Any]:
        """GET /customer_service_metric_task - Get customer service metric tasks."""
        params: Dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if created_date_range is not None:
            params["created_date_range"] = created_date_range
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json("GET", API_ROOT, "/customer_service_metric_task", scope=scope, params=params or None)

    # Schedules
    @mcp.tool()
    def feed_get_schedule_templates(*, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """GET /schedule_template - Get schedule templates."""
        return request_json("GET", API_ROOT, "/schedule_template", scope=scope)

    @mcp.tool()
    def feed_get_schedule_template(schedule_template_id: str, *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """GET /schedule_template/{schedule_template_id} - Get schedule template."""
        return request_json("GET", API_ROOT, f"/schedule_template/{schedule_template_id}", scope=scope)

    @mcp.tool()
    def feed_create_schedule(payload: Dict[str, Any], *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """POST /schedule - Create a schedule."""
        return request_json(
            "POST",
            API_ROOT,
            "/schedule",
            scope=scope,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def feed_get_schedule(schedule_id: str, *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """GET /schedule/{schedule_id} - Get a schedule."""
        return request_json("GET", API_ROOT, f"/schedule/{schedule_id}", scope=scope)

    @mcp.tool()
    def feed_get_schedules(
        *,
        feed_type: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        scope: str = DEFAULT_SCOPE,
    ) -> Dict[str, Any]:
        """GET /schedule - Get schedules."""
        params: Dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json("GET", API_ROOT, "/schedule", scope=scope, params=params or None)

    @mcp.tool()
    def feed_update_schedule(schedule_id: str, payload: Dict[str, Any], *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """PUT /schedule/{schedule_id} - Update a schedule."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/schedule/{schedule_id}",
            scope=scope,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def feed_delete_schedule(schedule_id: str, *, scope: str = DEFAULT_SCOPE) -> Dict[str, Any]:
        """DELETE /schedule/{schedule_id} - Delete a schedule."""
        return request_json("DELETE", API_ROOT, f"/schedule/{schedule_id}", scope=scope)
