from typing import Any, Dict, List, Optional

from .common import mastodon_request


def create_status(
    status: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    poll_options: Optional[List[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = None,
    poll_hide_totals: Optional[bool] = None,
    reply_to_id: Optional[str] = None,
    is_sensitive: Optional[bool] = None,
    content_warning: Optional[str] = None,
    post_visibility: Optional[str] = None,
    lang: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
) -> Any:
    data: Dict[str, Any] = {}
    if status is not None:
        data["status"] = status
    if media_ids is not None:
        for idx, value in enumerate(media_ids):
            data[f"media_ids[{idx}]"] = value
    if poll_options is not None:
        for idx, value in enumerate(poll_options):
            data[f"poll[options][{idx}]"] = value
    if poll_expires_in is not None:
        data["poll[expires_in]"] = poll_expires_in
    if poll_multiple is not None:
        data["poll[multiple]"] = str(poll_multiple).lower()
    if poll_hide_totals is not None:
        data["poll[hide_totals]"] = str(poll_hide_totals).lower()
    if reply_to_id is not None:
        data["in_reply_to_id"] = reply_to_id
    if is_sensitive is not None:
        data["sensitive"] = str(is_sensitive).lower()
    if content_warning is not None:
        data["spoiler_text"] = content_warning
    if post_visibility is not None:
        data["visibility"] = post_visibility
    if lang is not None:
        data["language"] = lang
    if scheduled_at is not None:
        data["scheduled_at"] = scheduled_at
    if quoted_status_id is not None:
        data["quoted_status_id"] = quoted_status_id
    if quote_approval_policy is not None:
        data["quote_approval_policy"] = quote_approval_policy
    return mastodon_request("POST", "/statuses", data=data)


def get_status(status_id: str) -> Any:
    return mastodon_request("GET", f"/statuses/{status_id}")


def delete_status(status_id: str, delete_media: Optional[bool] = None) -> Any:
    params = {}
    if delete_media is not None:
        params["delete_media"] = str(delete_media).lower()
    return mastodon_request("DELETE", f"/statuses/{status_id}", params=params)


def get_status_context(status_id: str) -> Any:
    return mastodon_request("GET", f"/statuses/{status_id}/context")


def favourite_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/statuses/{status_id}/unfavourite")


def boost_status(status_id: str, visibility: Optional[str] = None) -> Any:
    data = {}
    if visibility is not None:
        data["visibility"] = visibility
    return mastodon_request("POST", f"/statuses/{status_id}/reblog", data=data)


def unboost_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/statuses/{status_id}/unreblog")


def bookmark_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/statuses/{status_id}/bookmark")


def unbookmark_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/statuses/{status_id}/unbookmark")
