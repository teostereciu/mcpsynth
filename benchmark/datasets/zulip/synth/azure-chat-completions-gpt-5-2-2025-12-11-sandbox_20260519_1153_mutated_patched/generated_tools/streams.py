from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient, _maybe_json_dumps


def get_streams(
    *,
    include_public: Optional[bool] = None,
    include_web_public: Optional[bool] = None,
    include_subscribed: Optional[bool] = None,
    exclude_archived: Optional[bool] = None,
    include_all: Optional[bool] = None,
    include_default: Optional[bool] = None,
    include_owner_subscribed: Optional[bool] = None,
    include_can_access_content: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /streams"""
    client = ZulipClient()
    params: Dict[str, Any] = {}
    for k, v in {
        "include_public": include_public,
        "include_web_public": include_web_public,
        "include_subscribed": include_subscribed,
        "exclude_archived": exclude_archived,
        "include_all": include_all,
        "include_default": include_default,
        "include_owner_subscribed": include_owner_subscribed,
        "include_can_access_content": include_can_access_content,
    }.items():
        if v is not None:
            params[k] = "true" if v else "false"
    return client.request("GET", "/streams", params=params)


def subscribe(
    *,
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
) -> Dict[str, Any]:
    """POST /users/me/subscriptions

    Subscribe self or other users to channels; creates channels if missing.
    """
    client = ZulipClient()
    data: Dict[str, Any] = {
        "subscriptions": _maybe_json_dumps(subscriptions),
    }
    if principals is not None:
        data["principals"] = _maybe_json_dumps(principals)
    for k, v in {
        "authorization_errors_fatal": authorization_errors_fatal,
        "announce": announce,
        "invite_only": invite_only,
        "is_web_public": is_web_public,
        "is_default_stream": is_default_stream,
        "history_public_to_subscribers": history_public_to_subscribers,
    }.items():
        if v is not None:
            data[k] = "true" if v else "false"
    if message_retention_days is not None:
        data["message_retention_days"] = str(message_retention_days)
    if topics_policy is not None:
        data["topics_policy"] = topics_policy

    return client.request("POST", "/users/me/subscriptions", data=data)


def unsubscribe(
    *,
    subscriptions: List[str],
    principals: Optional[List[Union[int, str]]] = None,
) -> Dict[str, Any]:
    """DELETE /users/me/subscriptions"""
    client = ZulipClient()
    data: Dict[str, Any] = {"subscriptions": _maybe_json_dumps(subscriptions)}
    if principals is not None:
        data["principals"] = _maybe_json_dumps(principals)
    return client.request("DELETE", "/users/me/subscriptions", data=data)


def get_stream_topics(*, stream_id: int, allow_empty_topic_name: Optional[bool] = None) -> Dict[str, Any]:
    """GET /users/me/{stream_id}/topics"""
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = "true" if allow_empty_topic_name else "false"
    return client.request("GET", f"/users/me/{stream_id}/topics", params=params)


def delete_topic(*, stream_id: int, topic_name: str) -> Dict[str, Any]:
    """POST /streams/{stream_id}/delete_topic"""
    client = ZulipClient()
    data: Dict[str, Any] = {"topic_name": topic_name}
    return client.request("POST", f"/streams/{stream_id}/delete_topic", data=data)


def archive_stream(*, stream_id: int) -> Dict[str, Any]:
    """DELETE /streams/{stream_id}"""
    client = ZulipClient()
    return client.request("DELETE", f"/streams/{stream_id}")
