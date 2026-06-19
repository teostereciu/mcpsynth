from typing import Optional

from generated_tools.common import clean_params, mastodon_request


def list_notifications(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, types: Optional[list[str]] = None, exclude_types: Optional[list[str]] = None, account_id: Optional[str] = None, include_filtered: Optional[bool] = None):
    params = clean_params(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id, account_id=account_id, include_filtered=include_filtered)
    if types is not None:
        params["types[]"] = types
    if exclude_types is not None:
        params["exclude_types[]"] = exclude_types
    return mastodon_request("GET", "/api/v1/notifications", params=params)


def get_notification(notification_id: str):
    return mastodon_request("GET", f"/api/v1/notifications/{notification_id}")


def dismiss_notification(notification_id: str):
    return mastodon_request("POST", f"/api/v1/notifications/{notification_id}/dismiss")


def clear_notifications():
    return mastodon_request("POST", "/api/v1/notifications/clear")
