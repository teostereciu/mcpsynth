from typing import Any, Dict, Optional

from .ebay_client import EbayClient, omit_none


client = EbayClient()


def feed_create_task(task: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/feed/v1/task", json_body=task)


def feed_get_task(task_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/feed/v1/task/{task_id}")


def feed_get_tasks(
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params = omit_none({"feed_type": feed_type, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/feed/v1/task", params=params)


def feed_get_result_file(file_id: str) -> Dict[str, Any]:
    # Result files are often binary; request JSON and fall back to text.
    return client.request("GET", f"/sell/feed/v1/task/{file_id}/download")
