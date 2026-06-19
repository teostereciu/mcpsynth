from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def feed_create_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/feed/v1/task"""
    c = EbayClient()
    return c.request("POST", "/sell/feed/v1/task", json=task)


def feed_get_tasks(
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /sell/feed/v1/task"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return c.request("GET", "/sell/feed/v1/task", params=params)


def feed_get_task(task_id: str) -> Dict[str, Any]:
    """GET /sell/feed/v1/task/{taskId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/feed/v1/task/{task_id}")


def feed_get_task_download_url(task_id: str) -> Dict[str, Any]:
    """GET /sell/feed/v1/task/{taskId}/download_result_file"""
    c = EbayClient()
    return c.request("GET", f"/sell/feed/v1/task/{task_id}/download_result_file")
