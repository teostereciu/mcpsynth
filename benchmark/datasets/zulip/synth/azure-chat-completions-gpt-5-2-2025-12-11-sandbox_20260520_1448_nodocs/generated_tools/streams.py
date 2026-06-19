from __future__ import annotations

from typing import Any, Optional

from zulip_client import ZulipClient


def get_streams(client: ZulipClient, *, include_public: bool = True, include_subscribed: bool = True, include_all_active: bool = False) -> dict:
    params = {
        "include_public": include_public,
        "include_subscribed": include_subscribed,
        "include_all_active": include_all_active,
    }
    return client.request("GET", "/streams", params=params)


def create_stream(client: ZulipClient, *, subscriptions: list[dict[str, Any]], invite_only: Optional[bool] = None, history_public_to_subscribers: Optional[bool] = None) -> dict:
    data: dict[str, Any] = {"subscriptions": subscriptions}
    if invite_only is not None:
        data["invite_only"] = invite_only
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = history_public_to_subscribers
    return client.request("POST", "/users/me/subscriptions", data=data)


def update_stream(client: ZulipClient, *, stream_id: int, description: Optional[str] = None, new_name: Optional[str] = None, is_private: Optional[bool] = None, is_announcement_only: Optional[bool] = None) -> dict:
    data: dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if new_name is not None:
        data["new_name"] = new_name
    if is_private is not None:
        data["is_private"] = is_private
    if is_announcement_only is not None:
        data["is_announcement_only"] = is_announcement_only
    return client.request("PATCH", f"/streams/{stream_id}", data=data)


def archive_stream(client: ZulipClient, *, stream_id: int) -> dict:
    return client.request("DELETE", f"/streams/{stream_id}")


def subscribe(client: ZulipClient, *, subscriptions: list[dict[str, Any]], principals: Optional[list[int]] = None, authorization_errors_fatal: Optional[bool] = None) -> dict:
    data: dict[str, Any] = {"subscriptions": subscriptions}
    if principals is not None:
        data["principals"] = principals
    if authorization_errors_fatal is not None:
        data["authorization_errors_fatal"] = authorization_errors_fatal
    return client.request("POST", "/users/me/subscriptions", data=data)


def unsubscribe(client: ZulipClient, *, subscriptions: list[str], principals: Optional[list[int]] = None) -> dict:
    data: dict[str, Any] = {"subscriptions": subscriptions}
    if principals is not None:
        data["principals"] = principals
    return client.request("DELETE", "/users/me/subscriptions", data=data)
