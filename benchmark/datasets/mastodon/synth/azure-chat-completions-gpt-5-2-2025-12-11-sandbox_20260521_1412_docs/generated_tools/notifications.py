from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http_client import request_json


def list_notifications(
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    types: Optional[List[str]] = None,
    exclude_types: Optional[List[str]] = None,
    account_id: Optional[str] = None,
    include_filtered: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if types is not None:
        params["types[]"] = types
    if exclude_types is not None:
        params["exclude_types[]"] = exclude_types
    if account_id is not None:
        params["account_id"] = account_id
    if include_filtered is not None:
        params["include_filtered"] = str(bool(include_filtered)).lower()
    return request_json("GET", "/api/v1/notifications", params=params or None, require_auth=True)


def get_notification(notification_id: str) -> Dict[str, Any]:
    return request_json("GET", f"/api/v1/notifications/{notification_id}", require_auth=True)


def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    return request_json("POST", f"/api/v1/notifications/{notification_id}/dismiss", require_auth=True)


def clear_notifications() -> Dict[str, Any]:
    return request_json("POST", "/api/v1/notifications/clear", require_auth=True)
