from typing import Any, Dict, Optional

from .client import MastodonClient


def list_notifications(*, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, types: Optional[list] = None, exclude_types: Optional[list] = None, account_id: Optional[str] = None) -> Any:
    """GET /api/v1/notifications"""
    client = MastodonClient()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id, "account_id": account_id}.items():
        if v is not None:
            params[k] = v
    if types is not None:
        params["types[]"] = types
    if exclude_types is not None:
        params["exclude_types[]"] = exclude_types
    return client.request("GET", "/api/v1/notifications", params=params)


def get_notification(notification_id: str) -> Any:
    """GET /api/v1/notifications/{id}"""
    client = MastodonClient()
    return client.request("GET", f"/api/v1/notifications/{notification_id}")


def dismiss_notification(notification_id: str) -> Any:
    """POST /api/v1/notifications/{id}/dismiss"""
    client = MastodonClient()
    return client.request("POST", f"/api/v1/notifications/{notification_id}/dismiss")


def clear_notifications() -> Any:
    """POST /api/v1/notifications/clear"""
    client = MastodonClient()
    return client.request("POST", "/api/v1/notifications/clear")
