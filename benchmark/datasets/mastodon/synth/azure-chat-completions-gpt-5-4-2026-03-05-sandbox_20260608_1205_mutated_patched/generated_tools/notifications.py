from typing import Any, Dict, List, Optional

from .common import mastodon_request


def list_notifications(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, types: Optional[List[str]] = None, exclude_types: Optional[List[str]] = None, account_id: Optional[str] = None, include_filtered: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id, "account_id": account_id, "include_filtered": include_filtered}
    if types is not None:
        for idx, value in enumerate(types):
            params[f"types[{idx}]"] = value
    if exclude_types is not None:
        for idx, value in enumerate(exclude_types):
            params[f"exclude_types[{idx}]"] = value
    return mastodon_request("GET", "/notifications", params={k: v for k, v in params.items() if v is not None})


def get_notification(notification_id: str) -> Any:
    return mastodon_request("GET", f"/notifications/{notification_id}")


def dismiss_notification(notification_id: str) -> Any:
    return mastodon_request("POST", f"/notifications/{notification_id}/dismiss")


def clear_notifications() -> Any:
    return mastodon_request("POST", "/notifications/clear")
