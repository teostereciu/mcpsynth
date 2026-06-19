"""Mastodon API — Notifications domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def list_notifications(
    limit: int = 15,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    types: list = None,
    exclude_types: list = None,
    account_id: str = None,
) -> list:
    """Fetch notifications for the authenticated account.

    Args:
        limit: Maximum number of notifications to return (default 15, max 30).
        max_id: Return results older than this notification ID.
        since_id: Return results newer than this notification ID.
        min_id: Return results immediately newer than this notification ID.
        types: List of notification types to include (e.g. ['mention', 'reblog']).
        exclude_types: List of notification types to exclude.
        account_id: Return only notifications from this account ID.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    if account_id:
        params["account_id"] = account_id
    try:
        # types and exclude_types are array params
        extra = []
        if types:
            extra += [("types[]", t) for t in types]
        if exclude_types:
            extra += [("exclude_types[]", t) for t in exclude_types]
        r = requests.get(
            f"{BASE_URL}/notifications",
            headers=_headers(),
            params=list(params.items()) + extra,
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_notification(notification_id: str) -> dict:
    """Fetch a single notification by its ID.

    Args:
        notification_id: The ID of the notification to retrieve.
    """
    try:
        r = requests.get(
            f"{BASE_URL}/notifications/{notification_id}", headers=_headers()
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def dismiss_notification(notification_id: str) -> dict:
    """Dismiss (delete) a single notification.

    Args:
        notification_id: The ID of the notification to dismiss.
    """
    try:
        r = requests.post(
            f"{BASE_URL}/notifications/{notification_id}/dismiss", headers=_headers()
        )
        r.raise_for_status()
        return r.json() if r.content else {"status": "dismissed"}
    except Exception as e:
        return {"error": str(e)}


def clear_notifications() -> dict:
    """Clear all notifications for the authenticated account."""
    try:
        r = requests.post(f"{BASE_URL}/notifications/clear", headers=_headers())
        r.raise_for_status()
        return r.json() if r.content else {"status": "cleared"}
    except Exception as e:
        return {"error": str(e)}
