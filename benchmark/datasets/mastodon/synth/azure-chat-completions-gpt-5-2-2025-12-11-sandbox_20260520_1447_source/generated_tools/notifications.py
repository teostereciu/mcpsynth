from typing import Any, Dict, List, Optional

from .client import MastodonClient


def notifications_list(
    client: MastodonClient,
    *,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    account_id: Optional[str] = None,
    types: Optional[List[str]] = None,
    exclude_types: Optional[List[str]] = None,
    include_filtered: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if account_id is not None:
        params["account_id"] = account_id
    if types is not None:
        params["types"] = types
    if exclude_types is not None:
        params["exclude_types"] = exclude_types
    if include_filtered is not None:
        params["include_filtered"] = "true" if include_filtered else "false"

    return client.request("GET", "/api/v1/notifications", params=params or None)


def notifications_get(client: MastodonClient, notification_id: str) -> Any:
    return client.request("GET", f"/api/v1/notifications/{notification_id}")


def notifications_dismiss(client: MastodonClient, notification_id: str) -> Any:
    return client.request("POST", f"/api/v1/notifications/{notification_id}/dismiss")


def notifications_clear(client: MastodonClient) -> Any:
    return client.request("POST", "/api/v1/notifications/clear")


def notifications_unread_count(client: MastodonClient, *, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return client.request("GET", "/api/v1/notifications/unread_count", params=params or None)
