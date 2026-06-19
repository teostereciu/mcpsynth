from typing import Any, Dict

from .common import client


def create_task(task_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
    body = dict(data)
    body["taskType"] = task_type
    return client.request("POST", "/sell/feed/v1/task", json_body=body)


def get_task(task_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/feed/v1/task/{task_id}")


def list_tasks(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", "/sell/feed/v1/task", params={"limit": limit, "offset": offset})
