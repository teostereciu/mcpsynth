from typing import Any, Dict
from urllib.parse import quote

from generated_tools.common import client


def create_inventory_task(body: Dict[str, Any]) -> Any:
    return client.request(
        "POST",
        "/sell/feed/v1/inventory_task",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )


def get_task(task_id: str) -> Any:
    return client.request("GET", f"/sell/feed/v1/task/{quote(task_id, safe='')}")
