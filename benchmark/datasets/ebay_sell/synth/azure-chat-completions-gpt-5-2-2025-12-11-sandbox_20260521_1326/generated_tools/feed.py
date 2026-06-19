from typing import Any, Dict, Optional

from .client import EbayClient


def get_inventory_task(task_id: str) -> Dict[str, Any]:
    """GET /inventory_task/{task_id}

    Retrieves an inventory task by id.

    Doc: docs/api_feed_get-inventory-task.md
    """

    client = EbayClient()
    return client.request_json("GET", f"/sell/feed/v1/inventory_task/{task_id}")


def get_result_file(task_id: str) -> Dict[str, Any]:
    """GET /task/{task_id}/download_result_file

    Downloads the result file for a completed task.

    Note: This endpoint returns file content; this tool returns text body.

    Doc: docs/api_feed_get-result-file.md
    """

    client = EbayClient()
    # Accept anything; eBay returns CSV/XML/JSON (possibly gz). We'll return raw text.
    return client.request_json(
        "GET",
        f"/sell/feed/v1/task/{task_id}/download_result_file",
        accept="*/*",
    )


def create_inventory_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """POST /inventory_task

    Creates an inventory-related download task.

    Doc: docs/api_feed_create-inventory-task.md
    """

    client = EbayClient()
    return client.request_json(
        "POST",
        "/sell/feed/v1/inventory_task",
        json=task,
        content_type="application/json",
    )
