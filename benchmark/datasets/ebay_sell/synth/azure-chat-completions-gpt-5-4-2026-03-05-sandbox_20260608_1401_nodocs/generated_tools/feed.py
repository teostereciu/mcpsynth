from typing import Any, Dict, Optional

from generated_tools.common import client


def create_task(task_type: str, schema_version: str, feed_type: Optional[str] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {"taskType": task_type, "schemaVersion": schema_version}
    if feed_type is not None:
        body["feedType"] = feed_type
    return client.request("POST", "/sell/feed/v1/task", json_body=body)


def get_tasks(feed_type: Optional[str] = None, date_range: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if feed_type is not None:
        params["feed_type"] = feed_type
    if date_range is not None:
        params["date_range"] = date_range
    return client.request("GET", "/sell/feed/v1/task", params=params)


def get_task(task_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/feed/v1/task/{task_id}")


def upload_file(file_id: str, content: str, content_type: str = "application/json") -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/sell/feed/v1/task/{file_id}/upload_file",
        json_body={"content": content, "contentType": content_type},
    )


def download_result_file(task_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/feed/v1/task/{task_id}/download_result_file")
