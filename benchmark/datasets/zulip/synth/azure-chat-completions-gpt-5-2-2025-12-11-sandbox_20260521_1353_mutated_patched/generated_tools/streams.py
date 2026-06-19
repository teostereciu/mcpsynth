from typing import Any, Dict, List, Optional, Union

from .http_client import ZulipClient, dumps_if_needed


def get_streams(*, include_public: Optional[bool] = None, include_subscribed: Optional[bool] = None, include_all_active: Optional[bool] = None, include_default: Optional[bool] = None, include_owner_subscribed: Optional[bool] = None) -> Dict[str, Any]:
    """GET /streams

    Doc: docs/api_get-streams.md
    """
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if include_public is not None:
        params["include_public"] = include_public
    if include_subscribed is not None:
        params["include_subscribed"] = include_subscribed
    if include_all_active is not None:
        params["include_all_active"] = include_all_active
    if include_default is not None:
        params["include_default"] = include_default
    if include_owner_subscribed is not None:
        params["include_owner_subscribed"] = include_owner_subscribed
    return client.request("GET", "/streams", params=params)


def get_stream_id(*, stream: str) -> Dict[str, Any]:
    """GET /get_stream_id

    Doc: docs/api_get-stream-id.md
    """
    client = ZulipClient()
    return client.request("GET", "/get_stream_id", params={"stream": stream})


def get_stream_by_id(*, stream_id: int, include_subscribers: Optional[bool] = None) -> Dict[str, Any]:
    """GET /streams/{stream_id}

    Doc: docs/api_get-stream-by-id.md
    """
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if include_subscribers is not None:
        params["include_subscribers"] = include_subscribers
    return client.request("GET", f"/streams/{stream_id}", params=params)


def create_stream(*, name: str, description: Optional[str] = None, is_private: Optional[bool] = None, stream_post_policy: Optional[int] = None, history_public_to_subscribers: Optional[bool] = None, message_retention_days: Optional[Union[int, str]] = None) -> Dict[str, Any]:
    """POST /streams

    Doc: docs/api_create-stream.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {"name": name}
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = is_private
    if stream_post_policy is not None:
        data["stream_post_policy"] = stream_post_policy
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = history_public_to_subscribers
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    return client.request("POST", "/streams", data=data)


def update_stream(*, stream_id: int, new_name: Optional[str] = None, description: Optional[str] = None, is_private: Optional[bool] = None, is_announcement_only: Optional[bool] = None, stream_post_policy: Optional[int] = None, history_public_to_subscribers: Optional[bool] = None, message_retention_days: Optional[Union[int, str]] = None) -> Dict[str, Any]:
    """PATCH /streams/{stream_id}

    Doc: docs/api_update-stream.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {}
    if new_name is not None:
        data["new_name"] = new_name
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = is_private
    if is_announcement_only is not None:
        data["is_announcement_only"] = is_announcement_only
    if stream_post_policy is not None:
        data["stream_post_policy"] = stream_post_policy
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = history_public_to_subscribers
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    return client.request("PATCH", f"/streams/{stream_id}", data=data)


def archive_stream(*, stream_id: int) -> Dict[str, Any]:
    """DELETE /streams/{stream_id}

    Doc: docs/api_archive-stream.md
    """
    client = ZulipClient()
    return client.request("DELETE", f"/streams/{stream_id}")


def get_subscriptions(*, include_subscribers: Optional[bool] = None) -> Dict[str, Any]:
    """GET /users/me/subscriptions

    Doc: docs/api_get-subscriptions.md
    """
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if include_subscribers is not None:
        params["include_subscribers"] = include_subscribers
    return client.request("GET", "/users/me/subscriptions", params=params)


def subscribe(*, subscriptions: List[Dict[str, Any]], principals: Optional[List[Union[int, str]]] = None, authorization_errors_fatal: Optional[bool] = None, announce: Optional[bool] = None, invite_only: Optional[bool] = None, history_public_to_subscribers: Optional[bool] = None, stream_post_policy: Optional[int] = None, message_retention_days: Optional[Union[int, str]] = None) -> Dict[str, Any]:
    """POST /users/me/subscriptions

    Doc: docs/api_subscribe.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {"subscriptions": dumps_if_needed(subscriptions)}
    if principals is not None:
        data["principals"] = dumps_if_needed(principals)
    if authorization_errors_fatal is not None:
        data["authorization_errors_fatal"] = authorization_errors_fatal
    if announce is not None:
        data["announce"] = announce
    if invite_only is not None:
        data["invite_only"] = invite_only
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = history_public_to_subscribers
    if stream_post_policy is not None:
        data["stream_post_policy"] = stream_post_policy
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    return client.request("POST", "/users/me/subscriptions", data=data)


def unsubscribe(*, subscriptions: List[str], principals: Optional[List[Union[int, str]]] = None) -> Dict[str, Any]:
    """DELETE /users/me/subscriptions

    Doc: docs/api_unsubscribe.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {"subscriptions": dumps_if_needed(subscriptions)}
    if principals is not None:
        data["principals"] = dumps_if_needed(principals)
    return client.request("DELETE", "/users/me/subscriptions", data=data)


def get_stream_topics(*, stream_id: int) -> Dict[str, Any]:
    """GET /users/me/{stream_id}/topics

    Doc: docs/api_get-stream-topics.md
    """
    client = ZulipClient()
    return client.request("GET", f"/users/me/{stream_id}/topics")
