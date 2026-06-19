from typing import Any, Dict, List, Optional

from .client import MastodonClient


def statuses_get(client: MastodonClient, status_id: str) -> Any:
    return client.request("GET", f"/api/v1/statuses/{status_id}")


def statuses_create(
    client: MastodonClient,
    status: str,
    *,
    in_reply_to_id: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    allowed_mentions: Optional[List[str]] = None,
    poll: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
) -> Any:
    # Idempotency-Key is supported by Mastodon, but our simple client does not expose custom headers.
    # Keep parameter for tool signature compatibility; server will pass it via a dedicated request if needed.
    payload: Dict[str, Any] = {"status": status}
    if in_reply_to_id is not None:
        payload["in_reply_to_id"] = in_reply_to_id
    if quoted_status_id is not None:
        payload["quoted_status_id"] = quoted_status_id
    if quote_approval_policy is not None:
        payload["quote_approval_policy"] = quote_approval_policy
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
    if allowed_mentions is not None:
        payload["allowed_mentions"] = allowed_mentions
    if poll is not None:
        payload["poll"] = poll

    return client.request("POST", "/api/v1/statuses", json=payload)


def statuses_update(
    client: MastodonClient,
    status_id: str,
    *,
    status: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    media_attributes: Optional[List[Dict[str, Any]]] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    language: Optional[str] = None,
    poll: Optional[Dict[str, Any]] = None,
    quote_approval_policy: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {}
    if status is not None:
        payload["status"] = status
    if media_ids is not None:
        payload["media_ids"] = media_ids
    if media_attributes is not None:
        payload["media_attributes"] = media_attributes
    if sensitive is not None:
        payload["sensitive"] = sensitive
    if spoiler_text is not None:
        payload["spoiler_text"] = spoiler_text
    if language is not None:
        payload["language"] = language
    if poll is not None:
        payload["poll"] = poll
    if quote_approval_policy is not None:
        payload["quote_approval_policy"] = quote_approval_policy

    return client.request("PUT", f"/api/v1/statuses/{status_id}", json=payload)


def statuses_delete(client: MastodonClient, status_id: str, *, delete_media: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if delete_media is not None:
        params["delete_media"] = "true" if delete_media else "false"
    return client.request("DELETE", f"/api/v1/statuses/{status_id}", params=params or None)


def statuses_context(client: MastodonClient, status_id: str) -> Any:
    return client.request("GET", f"/api/v1/statuses/{status_id}/context")


def statuses_reblog(client: MastodonClient, status_id: str, *, visibility: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {}
    if visibility is not None:
        payload["visibility"] = visibility
    return client.request("POST", f"/api/v1/statuses/{status_id}/reblog", json=payload or None)


def statuses_unreblog(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/unreblog")


def statuses_favourite(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/favourite")


def statuses_unfavourite(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/unfavourite")


def statuses_bookmark(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/bookmark")


def statuses_unbookmark(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/unbookmark")
