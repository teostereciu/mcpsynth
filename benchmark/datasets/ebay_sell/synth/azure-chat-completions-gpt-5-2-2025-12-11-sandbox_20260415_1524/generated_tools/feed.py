from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def create_task(
    marketplace_id: str,
    task: Dict[str, Any],
    *,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /task

    Creates an upload or download task.
    """
    client = EbayClient()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if accept_language:
        headers["Accept-Language"] = accept_language
    return client.request(
        "POST",
        "/sell/feed/v1/task",
        json=task,
        headers=headers,
        content_type="application/json",
    )


def get_task(task_id: str) -> Dict[str, Any]:
    """GET /task/{taskId}"""
    client = EbayClient()
    return client.request("GET", f"/sell/feed/v1/task/{task_id}")


def get_tasks(
    *,
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /task"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/feed/v1/task", params=params or None)


def upload_file(task_id: str, content: str, *, content_type: str = "application/xml") -> Dict[str, Any]:
    """POST /task/{taskId}/upload_file

    Uploads the feed file content for an upload task.
    """
    client = EbayClient()
    return client.request(
        "POST",
        f"/sell/feed/v1/task/{task_id}/upload_file",
        data=content.encode("utf-8"),
        headers={"Content-Type": content_type},
        accept="application/json",
    )
