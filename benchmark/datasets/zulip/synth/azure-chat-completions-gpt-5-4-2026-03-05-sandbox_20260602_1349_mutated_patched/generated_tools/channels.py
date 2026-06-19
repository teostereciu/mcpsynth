from typing import Any, Dict, List, Optional

from .common import client


def get_channels(
    include_public: Optional[bool] = None,
    include_web_public: Optional[bool] = None,
    include_subscribed: Optional[bool] = None,
    exclude_archived: Optional[bool] = None,
    include_all: Optional[bool] = None,
    include_default: Optional[bool] = None,
    include_owner_subscribed: Optional[bool] = None,
    include_can_access_content: Optional[bool] = None,
    include_all_active: Optional[bool] = None,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/streams",
        params={
            "include_public": include_public,
            "include_web_public": include_web_public,
            "include_subscribed": include_subscribed,
            "exclude_archived": exclude_archived,
            "include_all": include_all,
            "include_default": include_default,
            "include_owner_subscribed": include_owner_subscribed,
            "include_can_access_content": include_can_access_content,
            "include_all_active": include_all_active,
        },
    )


def get_channel_by_id(stream_id: int) -> Dict[str, Any]:
    return client.request("GET", f"/streams/{stream_id}")


def get_channel_id(stream: str) -> Dict[str, Any]:
    return client.request("GET", "/get_stream_id", params={"stream": stream})


def update_channel(
    stream_id: int,
    description: Optional[str] = None,
    new_name: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    message_retention_days: Optional[Any] = None,
    is_archived: Optional[bool] = None,
    folder_id: Optional[int] = None,
    topics_policy: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "PATCH",
        f"/streams/{stream_id}",
        data={
            "description": description,
            "new_name": new_name,
            "is_private": is_private,
            "is_web_public": is_web_public,
            "history_public_to_subscribers": history_public_to_subscribers,
            "is_default_stream": is_default_stream,
            "message_retention_days": message_retention_days,
            "is_archived": is_archived,
            "folder_id": folder_id,
            "topics_policy": topics_policy,
        },
    )


def archive_channel(stream_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/streams/{stream_id}")


def get_channel_topics(stream_id: int, allow_empty_topic_name: Optional[bool] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/users/me/{stream_id}/topics",
        params={"allow_empty_topic_name": allow_empty_topic_name},
    )
