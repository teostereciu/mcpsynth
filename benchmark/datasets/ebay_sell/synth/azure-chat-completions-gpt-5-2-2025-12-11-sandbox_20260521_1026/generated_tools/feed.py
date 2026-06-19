from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


def create_inventory_task(task: Dict[str, Any], *, client: Optional[EbayClient] = None) -> Any:
    """POST /inventory_task

    Doc: docs/api_feed_create-inventory-task.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("POST", "/inventory_task", json=task, content_type="application/json")
    return c.ok_or_error(status, body, headers)


def get_inventory_task(task_id: str, *, client: Optional[EbayClient] = None) -> Any:
    """GET /inventory_task/{task_id}

    Doc: docs/api_feed_get-inventory-task.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("GET", f"/inventory_task/{task_id}")
    return c.ok_or_error(status, body, headers)


def get_inventory_tasks(
    *,
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /inventory_task

    Doc: docs/api_feed_get-inventory-tasks.md
    """
    c = client or EbayClient()
    params: Dict[str, str] = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    status, body, headers = c.request("GET", "/inventory_task", params=params or None)
    return c.ok_or_error(status, body, headers)


def get_task(task_id: str, *, client: Optional[EbayClient] = None) -> Any:
    """GET /task/{task_id}

    Doc: docs/api_feed_get-task.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("GET", f"/task/{task_id}")
    return c.ok_or_error(status, body, headers)


def get_tasks(
    *,
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /task

    Doc: docs/api_feed_get-tasks.md
    """
    c = client or EbayClient()
    params: Dict[str, str] = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    status, body, headers = c.request("GET", "/task", params=params or None)
    return c.ok_or_error(status, body, headers)
