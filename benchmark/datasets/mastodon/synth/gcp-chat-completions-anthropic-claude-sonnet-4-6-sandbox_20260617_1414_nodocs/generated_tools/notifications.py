"""
Mastodon API — Notifications domain tools.
Covers: list notifications, get single notification, dismiss notification, clear all.
"""

import requests
from config import BASE_URL, HEADERS


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
    List notifications for the authenticated account.

    Args:
        max_id: Return results older than this notification ID.
        since_id: Return results newer than this notification ID.
        min_id: Return results immediately newer than this notification ID.
        limit: Maximum number of results (default 15, max 30).
        types: List of notification types to include (e.g. ['mention', 'reblog']).
        exclude_types: List of notification types to exclude.
        account_id: Return only notifications from this account ID.

    Returns:
        A list of Notification objects, or an error dict.
    """
    url = f"{BASE_URL}/notifications"
    params: dict = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    if account_id:
        params["account_id"] = account_id

    # Build the request manually to support repeated keys for arrays
    try:
        req_params = list(params.items())
        if types:
            req_params += [("types[]", t) for t in types]
        if exclude_types:
            req_params += [("exclude_types[]", t) for t in exclude_types]
        resp = requests.get(url, headers=HEADERS, params=req_params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_notification(notification_id: str) -> dict:
    """
    Retrieve a single notification by its ID.

    Args:
        notification_id: The ID of the notification.

    Returns:
        A Notification object, or an error dict.
    """
    url = f"{BASE_URL}/notifications/{notification_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def dismiss_notification(notification_id: str) -> dict:
    """
    Dismiss (delete) a single notification.

    Args:
        notification_id: The ID of the notification to dismiss.

    Returns:
        An empty dict on success, or an error dict.
    """
    url = f"{BASE_URL}/notifications/{notification_id}/dismiss"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json() if resp.text.strip() else {}
    except requests.RequestException as e:
        return {"error": str(e)}


def clear_all_notifications() -> dict:
    """
    Clear all notifications for the authenticated account.

    Returns:
        An empty dict on success, or an error dict.
    """
    url = f"{BASE_URL}/notifications/clear"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json() if resp.text.strip() else {}
    except requests.RequestException as e:
        return {"error": str(e)}
