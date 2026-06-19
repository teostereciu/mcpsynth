from typing import Any, Optional

from generated_tools.common import client, compact_kwargs, parse_json_body


API_BASE = "/sell/feed/v1"


def create_task(body: str, marketplace_id: str, accept_language: Optional[str] = None) -> Any:
    try:
        headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
        if accept_language:
            headers["Accept-Language"] = accept_language
        return client.request(API_BASE, "POST", "/task", json_body=parse_json_body(body), headers=headers)
    except Exception as e:
        return {"error": str(e)}


def get_tasks(feed_type: Optional[str] = None, date_range: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/task", params=compact_kwargs(feed_type=feed_type, date_range=date_range, limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def get_task(task_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/task/{task_id}")
    except Exception as e:
        return {"error": str(e)}


def upload_file(task_id: str, content: str, content_type: str = "application/octet-stream") -> Any:
    try:
        return client.request(API_BASE, "POST", f"/task/{task_id}/upload_file", headers={"Content-Type": content_type}, data=content)
    except Exception as e:
        return {"error": str(e)}


def get_input_file(task_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/task/{task_id}/download_input_file")
    except Exception as e:
        return {"error": str(e)}


def get_result_file(task_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/task/{task_id}/download_result_file")
    except Exception as e:
        return {"error": str(e)}


def create_schedule(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/schedule", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def get_schedules(limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/schedule", params=compact_kwargs(limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def get_schedule(schedule_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/schedule/{schedule_id}")
    except Exception as e:
        return {"error": str(e)}


def delete_schedule(schedule_id: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/schedule/{schedule_id}")
    except Exception as e:
        return {"error": str(e)}


def get_latest_result_file(schedule_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/schedule/{schedule_id}/download_result_file")
    except Exception as e:
        return {"error": str(e)}
