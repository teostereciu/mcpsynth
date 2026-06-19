from typing import Any, Dict, Optional

from .http_client import MastodonClient


def list_notifications(*, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/notifications"""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/notifications", params=params)


def get_notification(*, notification_id: str, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/notifications/:id"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/notifications/{notification_id}")


def dismiss_notification(*, notification_id: str, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/notifications/:id/dismiss"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/notifications/{notification_id}/dismiss")


def clear_notifications(*, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/notifications/clear"""
    client = client or MastodonClient()
    return client.request("POST", "/api/v1/notifications/clear")
