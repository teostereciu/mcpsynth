from typing import Any, Dict, Union

from .http_client import JiraClient


def get_task(task_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /task/{taskId}"""
    client = JiraClient()
    return client.request("GET", f"/task/{task_id}")


def cancel_task(task_id: str) -> Union[Dict[str, Any], list, str]:
    """POST /task/{taskId}/cancel"""
    client = JiraClient()
    return client.request("POST", f"/task/{task_id}/cancel")
