from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient, _maybe_json_dumps


def get_streams(
    client: ZulipClient,
    include_public: Optional[bool] = None,
    include_web_public: Optional[bool] = None,
    include_subscribed: Optional[bool] = None,
    exclude_archived: Optional[bool] = None,
    include_all: Optional[bool] = None,
    include_default: Optional[bool] = None,
    include_owner_subscribed: Optional[bool] = None,
    include_can_access_content: Optional[bool] = None,
) -> Dict[str, Any]:
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
    return client.request("GET", "/streams", params)


def subscribe(
    client: ZulipClient,
    subscriptions: List[Dict[str, Any]],
    principals: Optional[List[Union[str, int]]] = None,
    authorization_errors_fatal: Optional[bool] = None,
    announce: Optional[bool] = None,
    invite_only: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    message_retention_days: Optional[Union[str, int]] = None,
    topics_policy: Optional[str] = None,
    can_add_subscribers_group: Optional[Union[int, Dict[str, Any]]] = None,
    can_remove_subscribers_group: Optional[Union[int, Dict[str, Any]]] = None,
    can_administer_channel_group: Optional[Union[int, Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"subscriptions": _maybe_json_dumps(subscriptions)}
    if principals is not None:
        params["principals"] = _maybe_json_dumps(principals)
    for k, v in {
        "authorization_errors_fatal": authorization_errors_fatal,
        "announce": announce,
        "invite_only": invite_only,
        "is_web_public": is_web_public,
        "is_default_stream": is_default_stream,
        "history_public_to_subscribers": history_public_to_subscribers,
    }.items():
        if v is not None:
            params[k] = "true" if v else "false"
    if message_retention_days is not None:
        params["message_retention_days"] = message_retention_days
    if topics_policy is not None:
        params["topics_policy"] = topics_policy
    if can_add_subscribers_group is not None:
        params["can_add_subscribers_group"] = _maybe_json_dumps(can_add_subscribers_group)
    if can_remove_subscribers_group is not None:
        params["can_remove_subscribers_group"] = _maybe_json_dumps(can_remove_subscribers_group)
    if can_administer_channel_group is not None:
        params["can_administer_channel_group"] = _maybe_json_dumps(can_administer_channel_group)

    return client.request("POST", "/users/me/subscriptions", params)


def unsubscribe(
    client: ZulipClient,
    subscriptions: List[str],
    principals: Optional[List[Union[str, int]]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"subscriptions": _maybe_json_dumps(subscriptions)}
    if principals is not None:
        params["principals"] = _maybe_json_dumps(principals)
    return client.request("DELETE", "/users/me/subscriptions", params)


def update_stream(
    client: ZulipClient,
    stream_id: int,
    description: Optional[str] = None,
    new_name: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    message_retention_days: Optional[Union[str, int]] = None,
    is_archived: Optional[bool] = None,
    folder_id: Optional[Union[int, None]] = None,
    topics_policy: Optional[str] = None,
    can_add_subscribers_group: Optional[Dict[str, Any]] = None,
    can_remove_subscribers_group: Optional[Dict[str, Any]] = None,
    can_administer_channel_group: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if description is not None:
        params["description"] = description
    if new_name is not None:
        params["new_name"] = new_name
    for k, v in {
        "is_private": is_private,
        "is_web_public": is_web_public,
        "history_public_to_subscribers": history_public_to_subscribers,
        "is_default_stream": is_default_stream,
        "is_archived": is_archived,
    }.items():
        if v is not None:
            params[k] = "true" if v else "false"
    if message_retention_days is not None:
        params["message_retention_days"] = message_retention_days
    if folder_id is not None:
        params["folder_id"] = folder_id
    if topics_policy is not None:
        params["topics_policy"] = topics_policy
    if can_add_subscribers_group is not None:
        params["can_add_subscribers_group"] = _maybe_json_dumps(can_add_subscribers_group)
    if can_remove_subscribers_group is not None:
        params["can_remove_subscribers_group"] = _maybe_json_dumps(can_remove_subscribers_group)
    if can_administer_channel_group is not None:
        params["can_administer_channel_group"] = _maybe_json_dumps(can_administer_channel_group)

    return client.request("PATCH", f"/streams/{stream_id}", params)


def archive_stream(client: ZulipClient, stream_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/streams/{stream_id}")
