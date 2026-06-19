from typing import Any, Dict, Optional

from .client import MastodonClient


def list_notifications(client: MastodonClient, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, types: Optional[list] = None, exclude_types: Optional[list] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    if types is not None:
        params["types[]"] = types
    if exclude_types is not None:
        params["exclude_types[]"] = exclude_types
    return client.request("GET", "/api/v1/notifications", params=params or None)


def get_notification(client: MastodonClient, notification_id: str) -> Any:
    return client.request("GET", f"/api/v1/notifications/{notification_id}")


def dismiss_notification(client: MastodonClient, notification_id: str) -> Any:
    return client.request("POST", "/api/v1/notifications/dismiss", json={"id": notification_id})


def clear_notifications(client: MastodonClient) -> Any:
    return client.request("POST", "/api/v1/notifications/clear")
