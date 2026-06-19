from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http_client import request_json


def create_status(
    status: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    in_reply_to_id: Optional[str] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    poll_options: Optional[List[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = None,
    poll_hide_totals: Optional[bool] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if status is not None:
        data["status"] = status
    if media_ids:
        data["media_ids[]"] = media_ids
    if in_reply_to_id is not None:
        data["in_reply_to_id"] = in_reply_to_id
    if sensitive is not None:
        data["sensitive"] = str(bool(sensitive)).lower()
    if spoiler_text is not None:
        data["spoiler_text"] = spoiler_text
    if visibility is not None:
        data["visibility"] = visibility
    if language is not None:
        data["language"] = language
    if scheduled_at is not None:
        data["scheduled_at"] = scheduled_at
    if poll_options is not None:
        data["poll[options][]"] = poll_options
    if poll_expires_in is not None:
        data["poll[expires_in]"] = str(int(poll_expires_in))
    if poll_multiple is not None:
        data["poll[multiple]"] = str(bool(poll_multiple)).lower()
    if poll_hide_totals is not None:
        data["poll[hide_totals]"] = str(bool(poll_hide_totals)).lower()
    if quoted_status_id is not None:
        data["quoted_status_id"] = quoted_status_id
    if quote_approval_policy is not None:
        data["quote_approval_policy"] = quote_approval_policy

    headers = {"Idempotency-Key": idempotency_key} if idempotency_key else None
    return request_json(
        "POST",
        "/api/v1/statuses",
        data=data,
        require_auth=True,
        extra_headers=headers,
    )


def get_status(status_id: str) -> Dict[str, Any]:
    return request_json("GET", f"/api/v1/statuses/{status_id}", require_auth=False)


def delete_status(status_id: str, delete_media: Optional[bool] = None) -> Dict[str, Any]:
    params = {}
    if delete_media is not None:
        params["delete_media"] = str(bool(delete_media)).lower()
    return request_json("DELETE", f"/api/v1/statuses/{status_id}", params=params or None, require_auth=True)


def get_status_context(status_id: str) -> Dict[str, Any]:
    return request_json("GET", f"/api/v1/statuses/{status_id}/context", require_auth=False)


def favourite_status(status_id: str) -> Dict[str, Any]:
    return request_json("POST", f"/api/v1/statuses/{status_id}/favourite", require_auth=True)


def unfavourite_status(status_id: str) -> Dict[str, Any]:
    return request_json("POST", f"/api/v1/statuses/{status_id}/unfavourite", require_auth=True)


def reblog_status(status_id: str) -> Dict[str, Any]:
    return request_json("POST", f"/api/v1/statuses/{status_id}/reblog", require_auth=True)


def unreblog_status(status_id: str) -> Dict[str, Any]:
    return request_json("POST", f"/api/v1/statuses/{status_id}/unreblog", require_auth=True)


def bookmark_status(status_id: str) -> Dict[str, Any]:
    return request_json("POST", f"/api/v1/statuses/{status_id}/bookmark", require_auth=True)


def unbookmark_status(status_id: str) -> Dict[str, Any]:
    return request_json("POST", f"/api/v1/statuses/{status_id}/unbookmark", require_auth=True)
