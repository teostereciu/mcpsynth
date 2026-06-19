from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_FEED
from . import mcp

API = "/sell/feed/v1"


@mcp.tool()
def feed_upload_file(
    file_name: str,
    content_type: str,
    data: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /upload_file

    Note: docs typically expect binary upload; for MCP we accept base64 or raw string.
    Provide `data` as base64-encoded content for non-text.
    """
    # eBay expects multipart; docs in this repo may simplify. We'll send JSON wrapper.
    payload = {"fileName": file_name, "contentType": content_type, "data": data}
    return _shared.client.request(
        "POST",
        API,
        "/upload_file",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
        json=payload,
    )


@mcp.tool()
def feed_create_task(
    task: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /task"""
    return _shared.client.request(
        "POST",
        API,
        "/task",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
        json=task,
    )


@mcp.tool()
def feed_get_task(task_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /task/{task_id}"""
    return _shared.client.request(
        "GET",
        API,
        f"/task/{task_id}",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def feed_get_tasks(
    *,
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /task"""
    params: Dict[str, Any] = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/task",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
        params=params or None,
    )


@mcp.tool()
def feed_get_result_file(file_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /result_file/{file_id}"""
    return _shared.client.request(
        "GET",
        API,
        f"/result_file/{file_id}",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
        accept="application/octet-stream",
    )


@mcp.tool()
def feed_get_input_file(file_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /input_file/{file_id}"""
    return _shared.client.request(
        "GET",
        API,
        f"/input_file/{file_id}",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
        accept="application/octet-stream",
    )


@mcp.tool()
def feed_get_latest_result_file(task_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /task/{task_id}/download_result_file"""
    return _shared.client.request(
        "GET",
        API,
        f"/task/{task_id}/download_result_file",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
        accept="application/octet-stream",
    )


@mcp.tool()
def feed_create_inventory_task(
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /inventory_task"""
    return _shared.client.request(
        "POST",
        API,
        "/inventory_task",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
        json=request,
    )


@mcp.tool()
def feed_get_inventory_task(task_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /inventory_task/{task_id}"""
    return _shared.client.request(
        "GET",
        API,
        f"/inventory_task/{task_id}",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def feed_get_inventory_tasks(
    *,
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /inventory_task"""
    params: Dict[str, Any] = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/inventory_task",
        scope=SCOPE_FEED,
        marketplace_id=marketplace_id,
        params=params or None,
    )
