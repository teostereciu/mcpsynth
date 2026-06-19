from typing import Any

from ._client import JiraClient


def get_task(client: JiraClient, task_id: str) -> Any:
    return client.request("GET", f"/task/{task_id}")


def cancel_task(client: JiraClient, task_id: str) -> Any:
    return client.request("POST", f"/task/{task_id}/cancel")
