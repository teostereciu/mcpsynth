"""Zulip Streams/Channels API tools."""
import json
from typing import Optional, List, Any
from .client import zulip_request


def get_streams(
    include_public: bool = True,
    include_subscribed: bool = True,
    include_all: bool = False,
    exclude_archived: bool = True,
    include_default: bool = False,
) -> dict:
    """Get all channels the user has access to.

    Args:
        include_public: Include all public channels.
        include_subscribed: Include all channels the user is subscribed to.
        include_all: Include all channels the user has metadata access to.
        exclude_archived: Whether to exclude archived channels.
        include_default: Include all default channels for the user's realm.
    """
    params = {
        "include_public": json.dumps(include_public),
        "include_subscribed": json.dumps(include_subscribed),
        "include_all": json.dumps(include_all),
        "exclude_archived": json.dumps(exclude_archived),
        "include_default": json.dumps(include_default),
    }
    return zulip_request("GET", "streams", params=params)


def get_subscriptions() -> dict:
    """Get all channels the current user is subscribed to."""
    return zulip_request("GET", "users/me/subscriptions")


def subscribe_to_stream(
    subscriptions: List[dict],
    principals: Optional[List[Any]] = None,
    invite_only: bool = False,
    is_web_public: bool = False,
    announce: bool = False,
    history_public_to_subscribers: Optional[bool] = None,
) -> dict:
    """Subscribe one or more users to one or more channels.

    Args:
        subscriptions: List of dicts with 'name' (required) and optional 'description'.
                       e.g. [{"name": "general", "description": "General chat"}]
        principals: List of user IDs or email addresses to subscribe. Defaults to self.
        invite_only: Whether newly created channels should be private.
        is_web_public: Whether newly created channels should be web-public.
        announce: Whether to announce newly created channels.
        history_public_to_subscribers: Whether channel history is public to new subscribers.
    """
    data: dict = {"subscriptions": json.dumps(subscriptions)}
    if principals is not None:
        data["principals"] = json.dumps(principals)
    data["invite_only"] = json.dumps(invite_only)
    data["is_web_public"] = json.dumps(is_web_public)
    data["announce"] = json.dumps(announce)
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = json.dumps(history_public_to_subscribers)
    return zulip_request("POST", "users/me/subscriptions", data=data)


def unsubscribe_from_stream(
    subscriptions: List[str],
    principals: Optional[List[Any]] = None,
) -> dict:
    """Unsubscribe yourself or other users from one or more channels.

    Args:
        subscriptions: List of channel names to unsubscribe from.
        principals: List of user IDs or email addresses to unsubscribe. Defaults to self.
    """
    data: dict = {"subscriptions": json.dumps(subscriptions)}
    if principals is not None:
        data["principals"] = json.dumps(principals)
    return zulip_request("DELETE", "users/me/subscriptions", data=data)


def get_stream_by_id(stream_id: int) -> dict:
    """Get a channel by its ID.

    Args:
        stream_id: The ID of the channel.
    """
    return zulip_request("GET", f"streams/{stream_id}")


def get_stream_id(stream: str) -> dict:
    """Get the ID of a channel by name.

    Args:
        stream: The name of the channel.
    """
    return zulip_request("GET", "get_stream_id", params={"stream": stream})


def update_stream(
    stream_id: int,
    description: Optional[str] = None,
    new_name: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    message_retention_days: Optional[Any] = None,
) -> dict:
    """Update a channel's settings.

    Args:
        stream_id: The ID of the channel to update.
        description: New description for the channel.
        new_name: New name for the channel.
        is_private: Change whether the channel is private.
        is_web_public: Change whether the channel is web-public.
        history_public_to_subscribers: Whether history is public to new subscribers.
        is_default_stream: Add or remove as a default channel for new users.
        message_retention_days: Days to retain messages, or "realm_default"/"unlimited".
    """
    data: dict = {}
    if description is not None:
        data["description"] = description
    if new_name is not None:
        data["new_name"] = new_name
    if is_private is not None:
        data["is_private"] = json.dumps(is_private)
    if is_web_public is not None:
        data["is_web_public"] = json.dumps(is_web_public)
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = json.dumps(history_public_to_subscribers)
    if is_default_stream is not None:
        data["is_default_stream"] = json.dumps(is_default_stream)
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    return zulip_request("PATCH", f"streams/{stream_id}", data=data)


def archive_stream(stream_id: int) -> dict:
    """Archive (delete) a channel.

    Args:
        stream_id: The ID of the channel to archive.
    """
    return zulip_request("DELETE", f"streams/{stream_id}")


def get_stream_topics(stream_id: int) -> dict:
    """Get all topics in a channel.

    Args:
        stream_id: The ID of the channel.
    """
    return zulip_request("GET", f"users/me/{stream_id}/topics")


def delete_topic(stream_id: int, topic_name: str) -> dict:
    """Delete all messages in a topic (admin only).

    Args:
        stream_id: The ID of the channel.
        topic_name: The name of the topic to delete.
    """
    return zulip_request(
        "POST",
        f"streams/{stream_id}/delete_topic",
        data={"topic_name": topic_name},
    )


def get_subscribers(stream_id: int) -> dict:
    """Get the subscribers of a channel.

    Args:
        stream_id: The ID of the channel.
    """
    return zulip_request("GET", f"streams/{stream_id}/members")


def get_subscription_status(user_id: int, stream_id: int) -> dict:
    """Check if a user is subscribed to a channel.

    Args:
        user_id: The ID of the user.
        stream_id: The ID of the channel.
    """
    return zulip_request("GET", f"users/{user_id}/subscriptions/{stream_id}")


def mute_topic(stream_name: str, topic_name: str, op: str = "add") -> dict:
    """Mute or unmute a topic.

    Args:
        stream_name: The name of the channel.
        topic_name: The name of the topic.
        op: "add" to mute, "remove" to unmute.
    """
    data = {
        "stream": stream_name,
        "topic": topic_name,
        "op": op,
    }
    return zulip_request("PATCH", "users/me/subscriptions/muted_topics", data=data)


def update_user_topic(
    stream_id: int,
    topic_name: str,
    visibility_policy: int,
) -> dict:
    """Update personal preferences for a topic.

    Args:
        stream_id: The ID of the channel.
        topic_name: The name of the topic.
        visibility_policy: 0=default, 1=muted, 2=unmuted, 3=followed.
    """
    data = {
        "stream_id": stream_id,
        "topic": topic_name,
        "visibility_policy": visibility_policy,
    }
    return zulip_request("POST", "user_topics", data=data)


def get_stream_email_address(stream_id: int) -> dict:
    """Get the email address for a channel (for sending messages via email).

    Args:
        stream_id: The ID of the channel.
    """
    return zulip_request("GET", f"streams/{stream_id}/email_address")


def add_default_stream(stream_id: int) -> dict:
    """Add a channel to the default channels for new users.

    Args:
        stream_id: The ID of the channel.
    """
    return zulip_request("POST", "default_streams", data={"stream_id": stream_id})


def remove_default_stream(stream_id: int) -> dict:
    """Remove a channel from the default channels for new users.

    Args:
        stream_id: The ID of the channel.
    """
    return zulip_request("DELETE", "default_streams", data={"stream_id": stream_id})


def get_user_channels(user_id: int) -> dict:
    """Get the channels a user is subscribed to.

    Args:
        user_id: The ID of the user.
    """
    return zulip_request("GET", f"users/{user_id}/channels")
