from typing import Any, Dict, List, Optional, Union

from ._client import ZulipClient, dumps_narrow


def subscribe(
    subscriptions: List[Dict[str, Any]],
    principals: Optional[List[Union[int, str]]] = None,
    authorization_errors_fatal: Optional[bool] = None,
    announce: Optional[bool] = None,
    invite_only: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    message_retention_days: Optional[Union[int, str]] = None,
    topics_policy: Optional[str] = None,
    can_add_subscribers_group: Optional[Union[int, Dict[str, Any]]] = None,
    can_remove_subscribers_group: Optional[Union[int, Dict[str, Any]]] = None,
    can_administer_channel_group: Optional[Union[int, Dict[str, Any]]] = None,
    can_send_message_group: Optional[Union[int, Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """POST /users/me/subscriptions"""
    data: Dict[str, Any] = {"subscriptions": dumps_narrow(subscriptions)}
    if principals is not None:
        data["principals"] = dumps_narrow(principals)
    if authorization_errors_fatal is not None:
        data["authorization_errors_fatal"] = authorization_errors_fatal
    if announce is not None:
        data["announce"] = announce
    if invite_only is not None:
        data["invite_only"] = invite_only
    if is_web_public is not None:
        data["is_web_public"] = is_web_public
    if is_default_stream is not None:
        data["is_default_stream"] = is_default_stream
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = history_public_to_subscribers
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    if topics_policy is not None:
        data["topics_policy"] = topics_policy
    if can_add_subscribers_group is not None:
        data["can_add_subscribers_group"] = dumps_narrow(can_add_subscribers_group)
    if can_remove_subscribers_group is not None:
        data["can_remove_subscribers_group"] = dumps_narrow(can_remove_subscribers_group)
    if can_administer_channel_group is not None:
        data["can_administer_channel_group"] = dumps_narrow(can_administer_channel_group)
    if can_send_message_group is not None:
        data["can_send_message_group"] = dumps_narrow(can_send_message_group)
    return ZulipClient().request("POST", "/users/me/subscriptions", data=data)


def get_streams(
    include_public: Optional[bool] = None,
    include_web_public: Optional[bool] = None,
    include_subscribed: Optional[bool] = None,
    include_all_active: Optional[bool] = None,
    include_default: Optional[bool] = None,
    include_owner_subscribed: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /streams"""
    params: Dict[str, Any] = {}
    if include_public is not None:
        params["include_public"] = include_public
    if include_web_public is not None:
        params["include_web_public"] = include_web_public
    if include_subscribed is not None:
        params["include_subscribed"] = include_subscribed
    if include_all_active is not None:
        params["include_all_active"] = include_all_active
    if include_default is not None:
        params["include_default"] = include_default
    if include_owner_subscribed is not None:
        params["include_owner_subscribed"] = include_owner_subscribed
    return ZulipClient().request("GET", "/streams", params=params)


def get_stream_id(stream: str) -> Dict[str, Any]:
    """GET /get_stream_id"""
    return ZulipClient().request("GET", "/get_stream_id", params={"stream": stream})


def get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    """GET /streams/{stream_id}"""
    return ZulipClient().request("GET", f"/streams/{stream_id}")


def update_stream(
    stream_id: int,
    description: Optional[str] = None,
    new_name: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    is_announcement_only: Optional[bool] = None,
    stream_post_policy: Optional[int] = None,
    message_retention_days: Optional[Union[int, str]] = None,
    history_public_to_subscribers: Optional[bool] = None,
) -> Dict[str, Any]:
    """PATCH /streams/{stream_id}"""
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if new_name is not None:
        data["new_name"] = new_name
    if is_private is not None:
        data["is_private"] = is_private
    if is_web_public is not None:
        data["is_web_public"] = is_web_public
    if is_announcement_only is not None:
        data["is_announcement_only"] = is_announcement_only
    if stream_post_policy is not None:
        data["stream_post_policy"] = stream_post_policy
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = history_public_to_subscribers
    return ZulipClient().request("PATCH", f"/streams/{stream_id}", data=data)


def archive_stream(stream_id: int) -> Dict[str, Any]:
    """DELETE /streams/{stream_id}"""
    return ZulipClient().request("DELETE", f"/streams/{stream_id}")


def get_stream_topics(stream_id: int, allow_empty_topic_name: Optional[bool] = None) -> Dict[str, Any]:
    """GET /users/me/{stream_id}/topics"""
    params: Dict[str, Any] = {}
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = allow_empty_topic_name
    return ZulipClient().request("GET", f"/users/me/{stream_id}/topics", params=params)


def update_user_topic(stream_id: int, topic: str, visibility_policy: int) -> Dict[str, Any]:
    """POST /user_topics"""
    data: Dict[str, Any] = {"stream_id": stream_id, "topic": topic, "visibility_policy": visibility_policy}
    return ZulipClient().request("POST", "/user_topics", data=data)


def get_subscriptions(include_subscribers: Optional[bool] = None) -> Dict[str, Any]:
    """GET /users/me/subscriptions"""
    params: Dict[str, Any] = {}
    if include_subscribers is not None:
        params["include_subscribers"] = include_subscribers
    return ZulipClient().request("GET", "/users/me/subscriptions", params=params)


def unsubscribe(subscriptions: List[str], principals: Optional[List[Union[int, str]]] = None) -> Dict[str, Any]:
    """DELETE /users/me/subscriptions"""
    data: Dict[str, Any] = {"subscriptions": dumps_narrow(subscriptions)}
    if principals is not None:
        data["principals"] = dumps_narrow(principals)
    return ZulipClient().request("DELETE", "/users/me/subscriptions", data=data)
