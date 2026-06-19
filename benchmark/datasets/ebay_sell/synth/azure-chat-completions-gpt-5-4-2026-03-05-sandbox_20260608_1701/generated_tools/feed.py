from typing import Any, Optional

from generated_tools.ebay_common import client


def create_task(body: dict, marketplace_id: str, accept_language: Optional[str] = None) -> Any:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if accept_language:
        headers["Accept-Language"] = accept_language
    return client.request("POST", "/task", api_group="feed", json_body=body, headers=headers)


def get_task(task_id: str) -> Any:
    return client.request("GET", f"/task/{task_id}", api_group="feed")
