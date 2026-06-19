from typing import Any, Dict, List, Optional

from ._client import request_json


def create_status(
    status: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    in_reply_to_id: Optional[str] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
    poll_options: Optional[List[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = None,
    poll_hide_totals: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
) -> Any:
    data: Dict[str, Any] = {}
    if status is not None:
        data["status"] = status
    if media_ids:
        for i, mid in enumerate(media_ids):
            data[f"media_ids[{i}]"] = mid
    if poll_options:
        for i, opt in enumerate(poll_options):
            data[f"poll[options][{i}]"] = opt
    if poll_expires_in is not None:
        data["poll[expires_in]"] = str(poll_expires_in)
    if poll_multiple is not None:
        data["poll[multiple]"] = "true" if poll_multiple else "false"
    if poll_hide_totals is not None:
        data["poll[hide_totals]"] = "true" if poll_hide_totals else "false"
    if in_reply_to_id is not None:
        data["in_reply_to_id"] = in_reply_to_id
    if sensitive is not None:
        data["sensitive"] = "true" if sensitive else "false"
    if spoiler_text is not None:
        data["spoiler_text"] = spoiler_text
    if visibility is not None:
        data["visibility"] = visibility
    if language is not None:
        data["language"] = language
    if scheduled_at is not None:
        data["scheduled_at"] = scheduled_at
    if quoted_status_id is not None:
        data["quoted_status_id"] = quoted_status_id
    if quote_approval_policy is not None:
        data["quote_approval_policy"] = quote_approval_policy

    headers = {}
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    return request_json("POST", "/api/v1/statuses", data=data, headers=headers)


def get_status(status_id: str) -> Any:
    return request_json("GET", f"/api/v1/statuses/{status_id}")


def get_statuses(ids: List[str]) -> Any:
    params: Dict[str, Any] = {}
    for i, sid in enumerate(ids):
        params[f"id[{i}]"] = sid
    return request_json("GET", "/api/v1/statuses", params=params)


def delete_status(status_id: str, delete_media: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if delete_media is not None:
        params["delete_media"] = "true" if delete_media else "false"
    return request_json("DELETE", f"/api/v1/statuses/{status_id}", params=params)


def get_status_context(status_id: str) -> Any:
    return request_json("GET", f"/api/v1/statuses/{status_id}/context")


def favourite_status(status_id: str) -> Any:
    return request_json("POST", f"/api/v1/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str) -> Any:
    return request_json("POST", f"/api/v1/statuses/{status_id}/unfavourite")


def reblog_status(status_id: str, visibility: Optional[str] = None) -> Any:
    data: Dict[str, Any] = {}
    if visibility is not None:
        data["visibility"] = visibility
    return request_json("POST", f"/api/v1/statuses/{status_id}/reblog", data=data)


def unreblog_status(status_id: str) -> Any:
    return request_json("POST", f"/api/v1/statuses/{status_id}/unreblog")
