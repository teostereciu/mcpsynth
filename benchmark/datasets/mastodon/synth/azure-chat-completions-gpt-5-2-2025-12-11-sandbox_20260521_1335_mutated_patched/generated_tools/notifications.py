from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import MastodonClient, compact_params


def list_notifications(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
    types: Optional[list[str]] = None,
    exclude_types: Optional[list[str]] = None,
    account_id: Optional[str] = None,
    include_filtered: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /api/v1/notifications

    Docs: docs/api_notifications.md
    """
    client = MastodonClient()
    params: Dict[str, Any] = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit,
        "account_id": account_id,
        "include_filtered": str(bool(include_filtered)).lower() if include_filtered is not None else None,
    }
    if types:
        for i, t in enumerate(types):
            params[f"types[{i}]"] = t
    if exclude_types:
        for i, t in enumerate(exclude_types):
            params[f"exclude_types[{i}]"] = t

    result, meta = client.request("GET", "/api/v1/notifications", params=compact_params(params))
    return {"result": result, "meta": meta}


def get_notification(notification_id: str) -> Dict[str, Any]:
    """GET /api/v1/notifications/:id

    Docs: docs/api_notifications.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", f"/api/v1/notifications/{notification_id}")
    return {"result": result, "meta": meta}


def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    """POST /api/v1/notifications/:id/dismiss

    Docs: docs/api_notifications.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", f"/api/v1/notifications/{notification_id}/dismiss")
    return {"result": result, "meta": meta}


def clear_notifications() -> Dict[str, Any]:
    """POST /api/v1/notifications/clear

    Docs: docs/api_notifications.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", "/api/v1/notifications/clear")
    return {"result": result, "meta": meta}
