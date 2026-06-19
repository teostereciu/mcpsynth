from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http_client import MastodonClient, compact_params


def create_status(
    status: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    reply_to_id: Optional[str] = None,
    is_sensitive: Optional[bool] = None,
    content_warning: Optional[str] = None,
    visibility: Optional[str] = None,
    lang: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
    poll_options: Optional[List[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = None,
    poll_hide_totals: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /api/v1/statuses

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    data: Dict[str, Any] = {}
    if status is not None:
        data["status"] = status
    if media_ids:
        for i, mid in enumerate(media_ids):
            data[f"media_ids[{i}]"] = mid
    if reply_to_id is not None:
        data["in_reply_to_id"] = reply_to_id
    if is_sensitive is not None:
        data["sensitive"] = str(bool(is_sensitive)).lower()
    if content_warning is not None:
        data["spoiler_text"] = content_warning
    if visibility is not None:
        data["visibility"] = visibility
    if lang is not None:
        data["language"] = lang
    if scheduled_at is not None:
        data["scheduled_at"] = scheduled_at
    if quoted_status_id is not None:
        data["quoted_status_id"] = quoted_status_id
    if quote_approval_policy is not None:
        data["quote_approval_policy"] = quote_approval_policy

    if poll_options is not None:
        for i, opt in enumerate(poll_options):
            data[f"poll[options][{i}]"] = opt
    if poll_expires_in is not None:
        data["poll[expires_in]"] = str(poll_expires_in)
    if poll_multiple is not None:
        data["poll[multiple]"] = str(bool(poll_multiple)).lower()
    if poll_hide_totals is not None:
        data["poll[hide_totals]"] = str(bool(poll_hide_totals)).lower()

    headers = {}
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    result, meta = client.request("POST", "/api/v1/statuses", data=data, headers=headers)
    return {"result": result, "meta": meta}


def get_status(status_id: str) -> Dict[str, Any]:
    """GET /api/v1/statuses/:id

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", f"/api/v1/statuses/{status_id}")
    return {"result": result, "meta": meta}


def delete_status(status_id: str, delete_media: Optional[bool] = None) -> Dict[str, Any]:
    """DELETE /api/v1/statuses/:id

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    params = compact_params({"delete_media": str(bool(delete_media)).lower() if delete_media is not None else None})
    result, meta = client.request("DELETE", f"/api/v1/statuses/{status_id}", params=params)
    return {"result": result, "meta": meta}


def get_status_context(status_id: str) -> Dict[str, Any]:
    """GET /api/v1/statuses/:id/context

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", f"/api/v1/statuses/{status_id}/context")
    return {"result": result, "meta": meta}


def favourite_status(status_id: str) -> Dict[str, Any]:
    """POST /api/v1/statuses/:id/favourite

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", f"/api/v1/statuses/{status_id}/favourite")
    return {"result": result, "meta": meta}


def unfavourite_status(status_id: str) -> Dict[str, Any]:
    """POST /api/v1/statuses/:id/unfavourite

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", f"/api/v1/statuses/{status_id}/unfavourite")
    return {"result": result, "meta": meta}


def reblog_status(status_id: str) -> Dict[str, Any]:
    """POST /api/v1/statuses/:id/reblog

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", f"/api/v1/statuses/{status_id}/reblog")
    return {"result": result, "meta": meta}


def unreblog_status(status_id: str) -> Dict[str, Any]:
    """POST /api/v1/statuses/:id/unreblog

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", f"/api/v1/statuses/{status_id}/unreblog")
    return {"result": result, "meta": meta}


def bookmark_status(status_id: str) -> Dict[str, Any]:
    """POST /api/v1/statuses/:id/bookmark

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", f"/api/v1/statuses/{status_id}/bookmark")
    return {"result": result, "meta": meta}


def unbookmark_status(status_id: str) -> Dict[str, Any]:
    """POST /api/v1/statuses/:id/unbookmark

    Docs: docs/api_statuses.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", f"/api/v1/statuses/{status_id}/unbookmark")
    return {"result": result, "meta": meta}
