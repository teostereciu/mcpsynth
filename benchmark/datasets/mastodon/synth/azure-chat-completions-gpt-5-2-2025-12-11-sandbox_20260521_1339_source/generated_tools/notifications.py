from typing import Any, List, Optional

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
    return client.request(
        "GET",
        "/api/v1/notifications",
        params={
            "limit": limit,
            "max_id": max_id,
            "since_id": since_id,
            "min_id": min_id,
            "account_id": account_id,
            "types": types,
            "exclude_types": exclude_types,
            "include_filtered": include_filtered,
        },
    )


def notifications_get(client: MastodonClient, notification_id: str) -> Any:
    return client.request("GET", f"/api/v1/notifications/{notification_id}")


def notifications_dismiss(client: MastodonClient, notification_id: str) -> Any:
    return client.request("POST", f"/api/v1/notifications/{notification_id}/dismiss")


def notifications_clear(client: MastodonClient) -> Any:
    return client.request("POST", "/api/v1/notifications/clear")


def notifications_unread_count(client: MastodonClient, *, limit: Optional[int] = None) -> Any:
    return client.request("GET", "/api/v1/notifications/unread_count", params={"limit": limit})
