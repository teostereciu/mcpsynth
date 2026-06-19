"""Channel/stream tools."""

from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional, Sequence, Union

from .http import zulip_request


JsonDict = Dict[str, Any]


def get_stream_id(*, stream: str) -> JsonDict:
    """GET /get_stream_id"""
    return zulip_request("GET", "/get_stream_id", params={"stream": stream})


def get_stream_topics(*, stream_id: int, allow_empty_topic_name: Optional[bool] = None) -> JsonDict:
    """GET /users/me/{stream_id}/topics"""
    return zulip_request(
        "GET",
        f"/users/me/{stream_id}/topics",
        params={"allow_empty_topic_name": allow_empty_topic_name},
    )


def subscribe(
    *,
    subscriptions: Sequence[Mapping[str, Any]],
    principals: Optional[Sequence[Union[str, int]]] = None,
    authorization_errors_fatal: Optional[bool] = None,
    announce: Optional[bool] = None,
    invite_only: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    message_retention_days: Optional[Union[str, int]] = None,
    topics_policy: Optional[str] = None,
) -> JsonDict:
    """POST /users/me/subscriptions

    Subscribe users to channels; creates channels if missing.
    """
    data: Dict[str, Any] = {
        "subscriptions": list(subscriptions),
        "principals": list(principals) if principals is not None else None,
        "authorization_errors_fatal": authorization_errors_fatal,
        "announce": announce,
        "invite_only": invite_only,
        "is_web_public": is_web_public,
        "is_default_stream": is_default_stream,
        "history_public_to_subscribers": history_public_to_subscribers,
        "message_retention_days": message_retention_days,
        "topics_policy": topics_policy,
    }
    return zulip_request("POST", "/users/me/subscriptions", data=data)


def unsubscribe(*, subscriptions: Sequence[str], principals: Optional[Sequence[Union[str, int]]] = None) -> JsonDict:
    """DELETE /users/me/subscriptions"""
    data: Dict[str, Any] = {
        "subscriptions": list(subscriptions),
        "principals": list(principals) if principals is not None else None,
    }
    return zulip_request("DELETE", "/users/me/subscriptions", data=data)


def get_subscribers(*, stream_id: int) -> JsonDict:
    """GET /streams/{stream_id}/members"""
    return zulip_request("GET", f"/streams/{stream_id}/members")
