from typing import Any, Dict, List, Optional

from .client import MastodonClient


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
    """POST /api/v1/statuses"""
    client = MastodonClient()
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
    return client.request("POST", "/api/v1/statuses", json=payload)


def get_status(status_id: str) -> Any:
    """GET /api/v1/statuses/{id}"""
    client = MastodonClient()
    return client.request("GET", f"/api/v1/statuses/{status_id}")


def delete_status(status_id: str) -> Any:
    """DELETE /api/v1/statuses/{id}"""
    client = MastodonClient()
    return client.request("DELETE", f"/api/v1/statuses/{status_id}")


def reblog_status(status_id: str) -> Any:
    """POST /api/v1/statuses/{id}/reblog"""
    client = MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/reblog")


def unreblog_status(status_id: str) -> Any:
    """POST /api/v1/statuses/{id}/unreblog"""
    client = MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/unreblog")


def favourite_status(status_id: str) -> Any:
    """POST /api/v1/statuses/{id}/favourite"""
    client = MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str) -> Any:
    """POST /api/v1/statuses/{id}/unfavourite"""
    client = MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/unfavourite")


def get_status_context(status_id: str) -> Any:
    """GET /api/v1/statuses/{id}/context"""
    client = MastodonClient()
    return client.request("GET", f"/api/v1/statuses/{status_id}/context")
