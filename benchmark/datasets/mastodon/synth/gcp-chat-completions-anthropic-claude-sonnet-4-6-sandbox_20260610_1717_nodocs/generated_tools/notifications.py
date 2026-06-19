"""
Mastodon API — Notifications domain tools.
Covers: list, get, dismiss, clear all notifications.
"""

import os
import requests


def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update(
        {"Authorization": f"Bearer {os.environ.get('MASTODON_ACCESS_TOKEN', '')}"}
    )
    return s


def _base() -> str:
    return os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"


# ---------------------------------------------------------------------------
# List notifications
# ---------------------------------------------------------------------------
def list_notifications(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 15,
    types: list = None,
    exclude_types: list = None,
    account_id: str = None,
) -> list:
    """
    Return notifications for the authenticated account.

    Args:
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 15, max 30).
        types: List of notification types to include
               ('mention', 'status', 'reblog', 'follow', 'follow_request',
                'favourite', 'poll', 'update').
        exclude_types: List of notification types to exclude.
        account_id: Only return notifications from this account.

    Returns:
        A list of Notification objects or an error dict.
    """
    params: dict = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    if account_id:
        params["account_id"] = account_id

    session = _session()
    req = requests.Request("GET", f"{_base()}/notifications", params=params)
    if types:
        req.params = list(params.items()) + [("types[]", t) for t in types]
    if exclude_types:
        extra = [("exclude_types[]", t) for t in exclude_types]
        if isinstance(req.params, list):
            req.params += extra
        else:
            req.params = list(params.items()) + extra

    try:
        prepared = session.prepare_request(req)
        resp = session.send(prepared)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get a single notification
# ---------------------------------------------------------------------------
def get_notification(notification_id: str) -> dict:
    """
    Fetch a single notification by its ID.

    Args:
        notification_id: The ID of the notification.

    Returns:
        A Notification object or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/notifications/{notification_id}")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Dismiss a single notification
# ---------------------------------------------------------------------------
def dismiss_notification(notification_id: str) -> dict:
    """
    Dismiss (delete) a single notification.

    Args:
        notification_id: The ID of the notification to dismiss.

    Returns:
        An empty dict on success, or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/notifications/{notification_id}/dismiss")
        r.raise_for_status()
        return {} if r.status_code == 200 and not r.text.strip() else r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Clear all notifications
# ---------------------------------------------------------------------------
def clear_all_notifications() -> dict:
    """
    Delete all notifications for the authenticated account.

    Returns:
        An empty dict on success, or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/notifications/clear")
        r.raise_for_status()
        return {} if r.status_code == 200 and not r.text.strip() else r.json()
    except Exception as exc:
        return {"error": str(exc)}
