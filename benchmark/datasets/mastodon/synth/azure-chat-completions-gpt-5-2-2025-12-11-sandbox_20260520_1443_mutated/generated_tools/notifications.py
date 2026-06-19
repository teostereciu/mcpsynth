from typing import Any, Dict, Optional

from .http import request_json


# Docs: docs/api_notifications.md


def list_notifications(
    *,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
    types: Optional[list[str]] = None,
    exclude_types: Optional[list[str]] = None,
    account_id: Optional[str] = None,
    include_filtered: Optional[bool] = None,
) -> Any:
    """GET /api/v1/notifications"""
    params: Dict[str, Any] = {}
    for k, v in {"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit, "account_id": account_id}.items():
        if v is not None:
            params[k] = v
    if include_filtered is not None:
        params["include_filtered"] = include_filtered
    if types is not None:
        for i, t in enumerate(types):
            params[f"types[{i}]"] = t
    if exclude_types is not None:
        for i, t in enumerate(exclude_types):
            params[f"exclude_types[{i}]"] = t
    return request_json("GET", "/api/v1/notifications", params=params)


def get_notification(notification_id: str) -> Any:
    """GET /api/v1/notifications/:id"""
    return request_json("GET", f"/api/v1/notifications/{notification_id}")


def clear_notifications() -> Any:
    """POST /api/v1/notifications/clear"""
    return request_json("POST", "/api/v1/notifications/clear")


def dismiss_notification(notification_id: str) -> Any:
    """POST /api/v1/notifications/:id/dismiss"""
    return request_json("POST", f"/api/v1/notifications/{notification_id}/dismiss")
