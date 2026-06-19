from typing import Any, Dict, List, Optional

from .http_client import MastodonClient


def list_statuses(*, client: Optional[MastodonClient] = None, params: Optional[Dict[str, Any]] = None) -> Any:
    """GET /api/v1/statuses (rarely used; included for completeness)."""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/statuses", params=params)


def create_status(
    *,
    status: str,
    in_reply_to_id: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    poll: Optional[Dict[str, Any]] = None,
    quote_id: Optional[str] = None,
    client: Optional[MastodonClient] = None,
) -> Any:
    """POST /api/v1/statuses"""
    client = client or MastodonClient()
    payload: Dict[str, Any] = {"status": status}
    if in_reply_to_id is not None:
        payload["in_reply_to_id"] = in_reply_to_id
    if media_ids is not None:
        payload["media_ids"] = media_ids
    if sensitive is not None:
        payload["sensitive"] = sensitive
    if spoiler_text is not None:
        payload["spoiler_text"] = spoiler_text
    if visibility is not None:
        payload["visibility"] = visibility
    if language is not None:
        payload["language"] = language
    if scheduled_at is not None:
        payload["scheduled_at"] = scheduled_at
    if poll is not None:
        payload["poll"] = poll
    if quote_id is not None:
        payload["quote_id"] = quote_id
    return client.request("POST", "/api/v1/statuses", json=payload)


def get_status(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/statuses/:id"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/statuses/{status_id}")


def update_status(*, status_id: str, params: Dict[str, Any], client: Optional[MastodonClient] = None) -> Any:
    """PUT/PATCH /api/v1/statuses/:id (Mastodon uses PUT for edit)."""
    client = client or MastodonClient()
    return client.request("PUT", f"/api/v1/statuses/{status_id}", json=params)


def delete_status(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """DELETE /api/v1/statuses/:id"""
    client = client or MastodonClient()
    return client.request("DELETE", f"/api/v1/statuses/{status_id}")


def reblog_status(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/statuses/:id/reblog"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/reblog")


def unreblog_status(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/statuses/:id/unreblog"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/unreblog")


def favourite_status(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/statuses/:id/favourite"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/favourite")


def unfavourite_status(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/statuses/:id/unfavourite"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/unfavourite")


def bookmark_status(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/statuses/:id/bookmark"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/bookmark")


def unbookmark_status(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/statuses/:id/unbookmark"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/unbookmark")


def get_status_context(*, status_id: str, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/statuses/:id/context"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/statuses/{status_id}/context")
