from typing import Any, Dict, List, Optional

from ._client import request_json


def create_status(
    status: str,
    *,
    in_reply_to_id: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    poll: Optional[Dict[str, Any]] = None,
) -> Any:
    data: Dict[str, Any] = {"status": status}
    if in_reply_to_id is not None:
        data["in_reply_to_id"] = in_reply_to_id
    if media_ids is not None:
        data["media_ids"] = media_ids
    if sensitive is not None:
        data["sensitive"] = sensitive
    if spoiler_text is not None:
        data["spoiler_text"] = spoiler_text
    if visibility is not None:
        data["visibility"] = visibility
    if language is not None:
        data["language"] = language
    if scheduled_at is not None:
        data["scheduled_at"] = scheduled_at
    if poll is not None:
        data["poll"] = poll
    return request_json("POST", "/api/v1/statuses", data=data)


def get_status(status_id: str) -> Any:
    return request_json("GET", f"/api/v1/statuses/{status_id}")


def delete_status(status_id: str) -> Any:
    return request_json("DELETE", f"/api/v1/statuses/{status_id}")


def reblog_status(status_id: str) -> Any:
    return request_json("POST", f"/api/v1/statuses/{status_id}/reblog")


def unreblog_status(status_id: str) -> Any:
    return request_json("POST", f"/api/v1/statuses/{status_id}/unreblog")


def favourite_status(status_id: str) -> Any:
    return request_json("POST", f"/api/v1/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str) -> Any:
    return request_json("POST", f"/api/v1/statuses/{status_id}/unfavourite")


def get_status_context(status_id: str) -> Any:
    return request_json("GET", f"/api/v1/statuses/{status_id}/context")
