from typing import Any, Dict, List, Optional

from .client import MastodonClient


def statuses_get(client: MastodonClient, status_id: str) -> Any:
    return client.request("GET", f"/api/v1/statuses/{status_id}")


def statuses_context(client: MastodonClient, status_id: str) -> Any:
    return client.request("GET", f"/api/v1/statuses/{status_id}/context")


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
) -> Any:
    payload: Dict[str, Any] = {
        "status": status,
        "in_reply_to_id": in_reply_to_id,
        "quoted_status_id": quoted_status_id,
        "quote_approval_policy": quote_approval_policy,
        "media_ids": media_ids,
        "sensitive": sensitive,
        "spoiler_text": spoiler_text,
        "visibility": visibility,
        "language": language,
        "scheduled_at": scheduled_at,
        "allowed_mentions": allowed_mentions,
        "poll": poll,
    }
    return client.request("POST", "/api/v1/statuses", json=payload)


def statuses_delete(client: MastodonClient, status_id: str, *, delete_media: Optional[bool] = None) -> Any:
    return client.request("DELETE", f"/api/v1/statuses/{status_id}", params={"delete_media": delete_media})


def statuses_reblog(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/reblog")


def statuses_unreblog(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/unreblog")


def statuses_favourite(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/favourite")


def statuses_unfavourite(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/unfavourite")
