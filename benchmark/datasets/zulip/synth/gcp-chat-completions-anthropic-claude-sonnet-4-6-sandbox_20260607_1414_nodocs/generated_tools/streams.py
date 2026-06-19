"""
Zulip MCP Tools — Streams domain
Covers: list, create, subscribe, unsubscribe, archive, settings, membership
"""

from typing import Optional
from .client import zulip_get, zulip_post, zulip_patch, zulip_delete


def get_streams(
    include_public: bool = True,
    include_subscribed: bool = True,
    include_all_active: bool = False,
    include_default: bool = False,
    include_owner_subscribed: bool = False,
) -> dict:
    """List streams visible to the current user.

    Args:
        include_public: Include all public streams.
        include_subscribed: Include streams the user is subscribed to.
        include_all_active: Include all active streams (requires admin).
        include_default: Include default streams for the realm.
        include_owner_subscribed: Include streams the bot owner is subscribed to.
    """
    return zulip_get(
        "/streams",
        {
            "include_public": include_public,
            "include_subscribed": include_subscribed,
            "include_all_active": include_all_active,
            "include_default": include_default,
            "include_owner_subscribed": include_owner_subscribed,
        },
    )


def get_stream_by_id(stream_id: int) -> dict:
    """Get details about a specific stream by its ID.

    Args:
        stream_id: The unique ID of the stream.
    """
    return zulip_get(f"/streams/{stream_id}")


def get_stream_id(stream_name: str) -> dict:
    """Look up the numeric ID of a stream by its name.

    Args:
        stream_name: The name of the stream.
    """
    return zulip_get("/get_stream_id", {"stream": stream_name})


def create_stream(
    subscriptions: str,
    invite_only: bool = False,
    is_web_public: bool = False,
    history_public_to_subscribers: Optional[bool] = None,
    stream_post_policy: int = 1,
    message_retention_days: Optional[str] = None,
    announce: bool = False,
    principals: Optional[str] = None,
    authorization_errors_fatal: bool = True,
) -> dict:
    """Create one or more streams (via the subscribe endpoint).

    Args:
        subscriptions: JSON-encoded list of objects with "name" (and optionally
                       "description"), e.g. '[{"name":"new-stream","description":"..."}]'.
        invite_only: If True, the stream is private.
        is_web_public: If True, the stream is web-public.
        history_public_to_subscribers: Whether stream history is public to subscribers.
        stream_post_policy: Who can post: 1=any subscriber, 2=admins, 3=full members, 4=moderators.
        message_retention_days: "realm_default", "unlimited", or an integer string.
        announce: If True, announce the new stream in the configured announcement stream.
        principals: JSON-encoded list of user emails/IDs to subscribe.
        authorization_errors_fatal: If True, return error if any principal is unauthorized.
    """
    params: dict = {
        "subscriptions": subscriptions,
        "invite_only": invite_only,
        "is_web_public": is_web_public,
        "stream_post_policy": stream_post_policy,
        "announce": announce,
        "authorization_errors_fatal": authorization_errors_fatal,
    }
    if history_public_to_subscribers is not None:
        params["history_public_to_subscribers"] = history_public_to_subscribers
    if message_retention_days is not None:
        params["message_retention_days"] = message_retention_days
    if principals is not None:
        params["principals"] = principals
    return zulip_post("/users/me/subscriptions", params)


def subscribe_to_streams(
    subscriptions: str,
    principals: Optional[str] = None,
    authorization_errors_fatal: bool = True,
    announce: bool = False,
    invite_only: bool = False,
    is_web_public: bool = False,
    history_public_to_subscribers: Optional[bool] = None,
    stream_post_policy: int = 1,
) -> dict:
    """Subscribe the current user (or specified users) to one or more streams.

    Args:
        subscriptions: JSON-encoded list of objects with "name" key,
                       e.g. '[{"name":"general"}]'.
        principals: JSON-encoded list of user emails or IDs to subscribe.
        authorization_errors_fatal: Raise error if any principal is unauthorized.
        announce: Announce newly created streams.
        invite_only: Make newly created streams private.
        is_web_public: Make newly created streams web-public.
        history_public_to_subscribers: History visibility for new streams.
        stream_post_policy: Post policy for new streams.
    """
    params: dict = {
        "subscriptions": subscriptions,
        "authorization_errors_fatal": authorization_errors_fatal,
        "announce": announce,
        "invite_only": invite_only,
        "is_web_public": is_web_public,
        "stream_post_policy": stream_post_policy,
    }
    if principals is not None:
        params["principals"] = principals
    if history_public_to_subscribers is not None:
        params["history_public_to_subscribers"] = history_public_to_subscribers
    return zulip_post("/users/me/subscriptions", params)


def unsubscribe_from_streams(subscriptions: str, principals: Optional[str] = None) -> dict:
    """Unsubscribe the current user (or specified users) from streams.

    Args:
        subscriptions: JSON-encoded list of objects with "name" key,
                       e.g. '[{"name":"general"}]'.
        principals: JSON-encoded list of user emails or IDs to unsubscribe.
    """
    params: dict = {"subscriptions": subscriptions}
    if principals is not None:
        params["principals"] = principals
    return zulip_delete("/users/me/subscriptions", params)


def archive_stream(stream_id: int) -> dict:
    """Archive (deactivate) a stream. Requires admin privileges.

    Args:
        stream_id: The ID of the stream to archive.
    """
    return zulip_delete(f"/streams/{stream_id}")


def update_stream(
    stream_id: int,
    description: Optional[str] = None,
    new_name: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    stream_post_policy: Optional[int] = None,
    message_retention_days: Optional[str] = None,
) -> dict:
    """Update the settings of a stream.

    Args:
        stream_id: The ID of the stream to update.
        description: New description for the stream.
        new_name: New name for the stream.
        is_private: Change privacy setting.
        is_web_public: Change web-public setting.
        history_public_to_subscribers: Change history visibility.
        stream_post_policy: Change post policy (1/2/3/4).
        message_retention_days: "realm_default", "unlimited", or integer string.
    """
    params: dict = {}
    if description is not None:
        params["description"] = description
    if new_name is not None:
        params["new_name"] = new_name
    if is_private is not None:
        params["is_private"] = is_private
    if is_web_public is not None:
        params["is_web_public"] = is_web_public
    if history_public_to_subscribers is not None:
        params["history_public_to_subscribers"] = history_public_to_subscribers
    if stream_post_policy is not None:
        params["stream_post_policy"] = stream_post_policy
    if message_retention_days is not None:
        params["message_retention_days"] = message_retention_days
    return zulip_patch(f"/streams/{stream_id}", params)


def get_subscribers(stream_id: int) -> dict:
    """Get the list of user IDs subscribed to a stream.

    Args:
        stream_id: The ID of the stream.
    """
    return zulip_get(f"/streams/{stream_id}/members")


def get_subscriptions() -> dict:
    """Get all streams the current user is subscribed to, with subscription metadata."""
    return zulip_get("/users/me/subscriptions")


def get_subscription_status(user_id: int, stream_id: int) -> dict:
    """Check whether a specific user is subscribed to a stream.

    Args:
        user_id: The ID of the user.
        stream_id: The ID of the stream.
    """
    return zulip_get(f"/users/{user_id}/subscriptions/{stream_id}")


def mute_topic_in_stream(stream_name: str, topic: str, op: str = "add") -> dict:
    """Mute or unmute a topic within a stream for the current user.

    Args:
        stream_name: The name of the stream containing the topic.
        topic: The name of the topic to mute/unmute.
        op: "add" to mute, "remove" to unmute.
    """
    return zulip_patch(
        "/users/me/subscriptions/muted_topics",
        {"stream": stream_name, "topic": topic, "op": op},
    )


def update_subscription_settings(subscription_data: str) -> dict:
    """Update per-subscription settings (e.g. color, pin, notifications).

    Args:
        subscription_data: JSON-encoded list of objects with "stream_id" and
                           setting key/value pairs, e.g.
                           '[{"stream_id":1,"color":"#aabbcc"}]'.
    """
    return zulip_post(
        "/users/me/subscriptions/properties", {"subscription_data": subscription_data}
    )


def get_stream_email_address(stream_id: int) -> dict:
    """Get the email address that can be used to send messages to a stream.

    Args:
        stream_id: The ID of the stream.
    """
    return zulip_get(f"/streams/{stream_id}/email_address")
