from typing import Any, Optional

from generated_tools.common import mastodon_request


def list_notifications(limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", "/api/v1/notifications", params={"limit": limit})


def get_notification(notification_id: str) -> Any:
    return mastodon_request("GET", f"/api/v1/notifications/{notification_id}")


def dismiss_notification(notification_id: str) -> Any:
    return mastodon_request("POST", f"/api/v1/notifications/{notification_id}/dismiss")


def clear_notifications() -> Any:
    return mastodon_request("POST", "/api/v1/notifications/clear")
