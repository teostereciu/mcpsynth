from typing import Any, Dict, Optional

from ._client import request_json


def list_notifications(*, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, types: Optional[list[str]] = None, exclude_types: Optional[list[str]] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    if types is not None:
        params["types[]"] = types
    if exclude_types is not None:
        params["exclude_types[]"] = exclude_types
    return request_json("GET", "/api/v1/notifications", params=params or None)


def get_notification(notification_id: str) -> Any:
    return request_json("GET", f"/api/v1/notifications/{notification_id}")


def dismiss_notification(notification_id: str) -> Any:
    return request_json("POST", f"/api/v1/notifications/{notification_id}/dismiss")


def clear_notifications() -> Any:
    return request_json("POST", "/api/v1/notifications/clear")
