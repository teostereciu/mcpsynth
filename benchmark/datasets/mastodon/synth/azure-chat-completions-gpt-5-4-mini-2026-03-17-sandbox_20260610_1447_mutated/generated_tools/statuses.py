from typing import Any, Dict, Optional

from .mastodon_client import MastodonClient

client = MastodonClient()


def post_status(status: str, media_ids: Optional[list[str]] = None, reply_to_id: Optional[str] = None, is_sensitive: Optional[bool] = None, content_warning: Optional[str] = None, post_visibility: Optional[str] = None, lang: Optional[str] = None, scheduled_at: Optional[str] = None, quoted_status_id: Optional[str] = None, quote_approval_policy: Optional[str] = None, poll: Optional[Dict[str, Any]] = None) -> Any:
    data: Dict[str, Any] = {"status": status}
    if media_ids is not None:
        for i, mid in enumerate(media_ids):
            data[f"media_ids[{i}]"] = mid
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
    if poll is not None:
        for k, v in poll.items():
            data[f"poll[{k}]"] = v
    return client.request("POST", "/statuses", data=data)


def get_status(status_id: str) -> Any:
    return client.request("GET", f"/statuses/{status_id}")


def delete_status(status_id: str, delete_media: Optional[bool] = None) -> Any:
    params = {}
    if delete_media is not None:
        params["delete_media"] = str(delete_media).lower()
    return client.request("DELETE", f"/statuses/{status_id}", params=params)


def get_status_context(status_id: str) -> Any:
    return client.request("GET", f"/statuses/{status_id}/context")


def favourite_status(status_id: str) -> Any:
    return client.request("POST", f"/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str) -> Any:
    return client.request("POST", f"/statuses/{status_id}/unfavourite")


def boost_status(status_id: str) -> Any:
    return client.request("POST", f"/statuses/{status_id}/reblog")


def unboost_status(status_id: str) -> Any:
    return client.request("POST", f"/statuses/{status_id}/unreblog")


def bookmark_status(status_id: str) -> Any:
    return client.request("POST", f"/statuses/{status_id}/bookmark")


def unbookmark_status(status_id: str) -> Any:
    return client.request("POST", f"/statuses/{status_id}/unbookmark")
