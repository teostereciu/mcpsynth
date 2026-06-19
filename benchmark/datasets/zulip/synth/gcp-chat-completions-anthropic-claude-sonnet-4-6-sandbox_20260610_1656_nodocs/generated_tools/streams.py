"""
Zulip MCP Tools — Streams domain
Covers: list, create, subscribe, unsubscribe, archive, settings, topics
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_stream_tools(mcp: FastMCP):

    @mcp.tool()
    def get_streams(
        include_public: bool = True,
        include_subscribed: bool = True,
        include_all_active: bool = False,
        include_default: bool = False,
        include_owner_subscribed: bool = False,
    ) -> dict:
        """List streams visible to the current user.

        Args:
            include_public: Include public streams.
            include_subscribed: Include streams the user is subscribed to.
            include_all_active: Include all active streams (admin only).
            include_default: Include default streams.
            include_owner_subscribed: Include streams the bot owner is subscribed to.
        """
        base, auth = _client()
        params = {
            "include_public": include_public,
            "include_subscribed": include_subscribed,
            "include_all_active": include_all_active,
            "include_default": include_default,
            "include_owner_subscribed": include_owner_subscribed,
        }
        try:
            r = requests.get(f"{base}/streams", params=params, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_stream_by_id(stream_id: int) -> dict:
        """Get details of a specific stream by its ID.

        Args:
            stream_id: The numeric ID of the stream.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/streams/{stream_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_stream_id(stream_name: str) -> dict:
        """Look up the numeric ID of a stream by name.

        Args:
            stream_name: The exact name of the stream.
        """
        base, auth = _client()
        try:
            r = requests.get(
                f"{base}/get_stream_id",
                params={"stream": stream_name},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_stream(
        subscriptions: str,
        invite_only: bool = False,
        is_web_public: bool = False,
        description: str = "",
        announce: bool = False,
        history_public_to_subscribers: bool = True,
        message_retention_days: str = "realm_default",
    ) -> dict:
        """Create one or more streams (by subscribing to streams that don't exist yet).

        Args:
            subscriptions: JSON list of objects with 'name' (and optional 'description'),
                           e.g. '[{"name":"new-stream","description":"My stream"}]'.
            invite_only: Make the stream private.
            is_web_public: Make the stream web-public.
            description: Default description (overridden per-stream in subscriptions).
            announce: Announce the new stream in the configured announcement stream.
            history_public_to_subscribers: Whether history is visible to new subscribers.
            message_retention_days: 'realm_default', 'unlimited', or an integer string.
        """
        base, auth = _client()
        payload = {
            "subscriptions": subscriptions,
            "invite_only": invite_only,
            "is_web_public": is_web_public,
            "announce": announce,
            "history_public_to_subscribers": history_public_to_subscribers,
            "message_retention_days": message_retention_days,
        }
        if description:
            payload["description"] = description
        try:
            r = requests.post(f"{base}/users/me/subscriptions", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def subscribe_to_stream(
        subscriptions: str,
        invite_only: bool = False,
        principals: str = "[]",
        authorization_errors_fatal: bool = True,
    ) -> dict:
        """Subscribe the current user (or specified users) to one or more streams.

        Args:
            subscriptions: JSON list of objects with 'name', e.g. '[{"name":"general"}]'.
            invite_only: Create as private if the stream doesn't exist.
            principals: JSON list of user emails or IDs to subscribe instead of self.
            authorization_errors_fatal: Raise error if user can't subscribe to a stream.
        """
        base, auth = _client()
        payload = {
            "subscriptions": subscriptions,
            "invite_only": invite_only,
            "principals": principals,
            "authorization_errors_fatal": authorization_errors_fatal,
        }
        try:
            r = requests.post(f"{base}/users/me/subscriptions", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unsubscribe_from_stream(
        subscriptions: str,
        principals: str = "[]",
    ) -> dict:
        """Unsubscribe the current user (or specified users) from streams.

        Args:
            subscriptions: JSON list of stream name objects, e.g. '[{"name":"general"}]'.
            principals: JSON list of user emails or IDs to unsubscribe instead of self.
        """
        base, auth = _client()
        payload: dict = {"subscriptions": subscriptions}
        if principals and principals != "[]":
            payload["principals"] = principals
        try:
            r = requests.delete(
                f"{base}/users/me/subscriptions", data=payload, auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_subscriptions() -> dict:
        """List all streams the current user is subscribed to."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/users/me/subscriptions", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_subscription_status(user_id: int, stream_id: int) -> dict:
        """Check whether a user is subscribed to a stream.

        Args:
            user_id: The numeric ID of the user.
            stream_id: The numeric ID of the stream.
        """
        base, auth = _client()
        try:
            r = requests.get(
                f"{base}/users/{user_id}/subscriptions/{stream_id}", auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_stream(
        stream_id: int,
        description: str = "",
        new_name: str = "",
        is_private: bool = False,
        is_web_public: bool = False,
        history_public_to_subscribers: bool = True,
        stream_post_policy: int = 1,
        message_retention_days: str = "",
    ) -> dict:
        """Update the settings of a stream.

        Args:
            stream_id: The numeric ID of the stream to update.
            description: New description (leave blank to keep current).
            new_name: New stream name (leave blank to keep current).
            is_private: Whether the stream should be private.
            is_web_public: Whether the stream should be web-public.
            history_public_to_subscribers: Whether history is visible to new subscribers.
            stream_post_policy: Who can post — 1=any, 2=admins, 3=full members, 4=moderators.
            message_retention_days: 'realm_default', 'unlimited', or integer string.
        """
        base, auth = _client()
        payload: dict = {
            "is_private": is_private,
            "is_web_public": is_web_public,
            "history_public_to_subscribers": history_public_to_subscribers,
            "stream_post_policy": stream_post_policy,
        }
        if description:
            payload["description"] = description
        if new_name:
            payload["new_name"] = new_name
        if message_retention_days:
            payload["message_retention_days"] = message_retention_days
        try:
            r = requests.patch(
                f"{base}/streams/{stream_id}", data=payload, auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def archive_stream(stream_id: int) -> dict:
        """Archive (deactivate) a stream.

        Args:
            stream_id: The numeric ID of the stream to archive.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/streams/{stream_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_stream_topics(stream_id: int) -> dict:
        """List all topics in a stream.

        Args:
            stream_id: The numeric ID of the stream.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/users/me/{stream_id}/topics", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_stream_members(stream_id: int) -> dict:
        """List all subscribers (members) of a stream.

        Args:
            stream_id: The numeric ID of the stream.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/streams/{stream_id}/members", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mute_topic(stream_name: str, topic: str) -> dict:
        """Mute a topic so its messages are hidden by default.

        Args:
            stream_name: The name of the stream containing the topic.
            topic: The name of the topic to mute.
        """
        base, auth = _client()
        try:
            r = requests.patch(
                f"{base}/users/me/subscriptions/muted_topics",
                data={"stream": stream_name, "topic": topic, "op": "add"},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unmute_topic(stream_name: str, topic: str) -> dict:
        """Unmute a previously muted topic.

        Args:
            stream_name: The name of the stream containing the topic.
            topic: The name of the topic to unmute.
        """
        base, auth = _client()
        try:
            r = requests.patch(
                f"{base}/users/me/subscriptions/muted_topics",
                data={"stream": stream_name, "topic": topic, "op": "remove"},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_subscription_settings(
        subscription_data: str,
    ) -> dict:
        """Update per-subscription settings (e.g. notifications, color) for the current user.

        Args:
            subscription_data: JSON list of objects with 'stream_id' and setting key/value,
                e.g. '[{"stream_id":1,"property":"color","value":"#aabbcc"}]'.
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/users/me/subscriptions/properties",
                data={"subscription_data": subscription_data},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_default_streams() -> dict:
        """List the default streams for the organisation."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/default_streams", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def add_default_stream(stream_id: int) -> dict:
        """Add a stream to the organisation's default stream list.

        Args:
            stream_id: The numeric ID of the stream.
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/default_streams",
                data={"stream_id": stream_id},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_default_stream(stream_id: int) -> dict:
        """Remove a stream from the organisation's default stream list.

        Args:
            stream_id: The numeric ID of the stream.
        """
        base, auth = _client()
        try:
            r = requests.delete(
                f"{base}/default_streams",
                data={"stream_id": stream_id},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}
