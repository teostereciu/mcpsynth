from typing import Any, Dict, List, Optional

from ._client import request_json


def list_notifications(
    *,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
    types: Optional[List[str]] = None,
    exclude_types: Optional[List[str]] = None,
    account_id: Optional[str] = None,
    include_filtered: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    if types:
        for i, t in enumerate(types):
            params[f"types[{i}]"] = t
    if exclude_types:
        for i, t in enumerate(exclude_types):
            params[f"exclude_types[{i}]"] = t
    if account_id is not None:
        params["account_id"] = account_id
    if include_filtered is not None:
        params["include_filtered"] = "true" if include_filtered else "false"
    return request_json("GET", "/api/v1/notifications", params=params)


def get_notification(notification_id: str) -> Any:
    return request_json("GET", f"/api/v1/notifications/{notification_id}")


def clear_notifications() -> Any:
    return request_json("POST", "/api/v1/notifications/clear")


def dismiss_notification(notification_id: str) -> Any:
    return request_json("POST", f"/api/v1/notifications/{notification_id}/dismiss")
