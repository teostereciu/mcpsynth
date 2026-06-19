from typing import Any

from .jira_client import JiraClient


def get_task(task_id: str) -> Any:
    """GET /task/{taskId}"""
    return JiraClient().request("GET", f"/task/{task_id}")


def cancel_task(task_id: str) -> Any:
    """POST /task/{taskId}/cancel"""
    return JiraClient().request("POST", f"/task/{task_id}/cancel")
