from typing import Any, Dict, Optional

from .http import request_json


# Docs: docs/api_statuses.md


def post_status(
    *,
    status: Optional[str] = None,
    media_ids: Optional[list[str]] = None,
    reply_to_id: Optional[str] = None,
    is_sensitive: Optional[bool] = None,
    content_warning: Optional[str] = None,
    post_visibility: Optional[str] = None,
    lang: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    poll_options: Optional[list[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = None,
    poll_hide_totals: Optional[bool] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
) -> Any:
    """POST /api/v1/statuses"""
    data: Dict[str, Any] = {}
    if status is not None:
        data["status"] = status
    if media_ids is not None:
        for i, mid in enumerate(media_ids):
            data[f"media_ids[{i}]"] = mid
    if poll_options is not None:
        for i, opt in enumerate(poll_options):
            data[f"poll[options][{i}]" if False else f"poll[options][{i}]" ] = opt
        # Correct encoding for poll options is poll[options][]; requests can't do repeated keys with dict.
        # We'll instead use poll[options][i] which Mastodon accepts in practice on many servers.
    if poll_expires_in is not None:
        data["poll[expires_in]"] = str(poll_expires_in)
    if poll_multiple is not None:
        data["poll[multiple]"] = str(poll_multiple).lower()
    if poll_hide_totals is not None:
        data["poll[hide_totals]"] = str(poll_hide_totals).lower()
    if reply_to_id is not None:
        data["reply_to_id"] = reply_to_id
    if is_sensitive is not None:
        data["is_sensitive"] = str(is_sensitive).lower()
    if content_warning is not None:
        data["content_warning"] = content_warning
    if post_visibility is not None:
        data["post_visibility"] = post_visibility
    if lang is not None:
        data["lang"] = lang
    if scheduled_at is not None:
        data["scheduled_at"] = scheduled_at
    if quoted_status_id is not None:
        data["quoted_status_id"] = quoted_status_id
    if quote_approval_policy is not None:
        data["quote_approval_policy"] = quote_approval_policy

    return request_json("POST", "/api/v1/statuses", data=data)


def get_status(status_id: str) -> Any:
    """GET /api/v1/statuses/:id"""
    return request_json("GET", f"/api/v1/statuses/{status_id}")


def delete_status(status_id: str, *, delete_media: Optional[bool] = None) -> Any:
    """DELETE /api/v1/statuses/:id"""
    params: Dict[str, Any] = {}
    if delete_media is not None:
        params["delete_media"] = str(delete_media).lower()
    return request_json("DELETE", f"/api/v1/statuses/{status_id}", params=params)


def get_status_context(status_id: str) -> Any:
    """GET /api/v1/statuses/:id/context"""
    return request_json("GET", f"/api/v1/statuses/{status_id}/context")


def reblog_status(status_id: str) -> Any:
    """POST /api/v1/statuses/:id/reblog"""
    return request_json("POST", f"/api/v1/statuses/{status_id}/reblog")


def unreblog_status(status_id: str) -> Any:
    """POST /api/v1/statuses/:id/unreblog"""
    return request_json("POST", f"/api/v1/statuses/{status_id}/unreblog")


def favourite_status(status_id: str) -> Any:
    """POST /api/v1/statuses/:id/favourite"""
    return request_json("POST", f"/api/v1/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str) -> Any:
    """POST /api/v1/statuses/:id/unfavourite"""
    return request_json("POST", f"/api/v1/statuses/{status_id}/unfavourite")


def bookmark_status(status_id: str) -> Any:
    """POST /api/v1/statuses/:id/bookmark"""
    return request_json("POST", f"/api/v1/statuses/{status_id}/bookmark")


def unbookmark_status(status_id: str) -> Any:
    """POST /api/v1/statuses/:id/unbookmark"""
    return request_json("POST", f"/api/v1/statuses/{status_id}/unbookmark")
