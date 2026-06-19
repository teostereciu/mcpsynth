from typing import Any, Optional

from .common import client

API_PATH = "/sell/feed/v1"


def create_task(body: dict, marketplace_id: str, accept_language: Optional[str] = None) -> Any:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if accept_language:
        headers["Accept-Language"] = accept_language
    return client.request(API_PATH, "POST", "/task", json_body=body, headers=headers)


def get_task(task_id: str) -> Any:
    return client.request(API_PATH, "GET", f"/task/{task_id}")


def get_tasks(
    date_range: Optional[str] = None,
    feed_type: Optional[str] = None,
    limit: Optional[int] = None,
    look_back_days: Optional[int] = None,
    offset: Optional[int] = None,
    schedule_id: Optional[str] = None,
) -> Any:
    return client.request(
        API_PATH,
        "GET",
        "/task",
        params={
            "date_range": date_range,
            "feed_type": feed_type,
            "limit": limit,
            "look_back_days": look_back_days,
            "offset": offset,
            "schedule_id": schedule_id,
        },
    )


def get_result_file(task_id: str) -> Any:
    return client.request(API_PATH, "GET", f"/task/{task_id}/download_result_file")
