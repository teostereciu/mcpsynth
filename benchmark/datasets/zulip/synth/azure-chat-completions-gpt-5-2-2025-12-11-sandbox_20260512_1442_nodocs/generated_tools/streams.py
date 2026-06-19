from __future__ import annotations

from zulip_client import ZulipClient


def register(mcp, client: ZulipClient):
    @mcp.tool()
    def zulip_get_streams(include_public: bool = True, include_subscribed: bool = True, include_all_active: bool = False, include_default: bool = False, include_owner_subscribed: bool = False):
        """List streams."""
        params = {
            "include_public": include_public,
            "include_subscribed": include_subscribed,
            "include_all_active": include_all_active,
            "include_default": include_default,
            "include_owner_subscribed": include_owner_subscribed,
        }
        return client.request("GET", "/streams", params=params)

    @mcp.tool()
    def zulip_create_streams(streams: list[dict], announce: bool | None = None, principals=None):
        """Create one or more streams.

        streams: list of {"name": ..., "description": ...}
        """
        data = {"streams": streams}
        if announce is not None:
            data["announce"] = announce
        if principals is not None:
            data["principals"] = principals
        return client.request("POST", "/streams", data=data)

    @mcp.tool()
    def zulip_update_stream(stream_id: int, description: str | None = None, new_name: str | None = None, is_private: bool | None = None, is_announcement_only: bool | None = None, stream_post_policy: int | None = None, history_public_to_subscribers: bool | None = None, message_retention_days: int | None = None):
        """Update stream settings."""
        data = {}
        if description is not None:
            data["description"] = description
        if new_name is not None:
            data["new_name"] = new_name
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

    @mcp.tool()
    def zulip_archive_stream(stream_id: int):
        """Archive (delete) a stream."""
        return client.request("DELETE", f"/streams/{stream_id}")

    @mcp.tool()
    def zulip_get_subscriptions(include_subscribers: bool = False):
        """List your subscriptions."""
        return client.request("GET", "/users/me/subscriptions", params={"include_subscribers": include_subscribers})

    @mcp.tool()
    def zulip_subscribe(streams: list[dict], principals=None, authorization_errors_fatal: bool | None = None, announce: bool | None = None, invite_only: bool | None = None, history_public_to_subscribers: bool | None = None):
        """Subscribe users to streams."""
        data = {"subscriptions": streams}
        if principals is not None:
            data["principals"] = principals
        if authorization_errors_fatal is not None:
            data["authorization_errors_fatal"] = authorization_errors_fatal
        if announce is not None:
            data["announce"] = announce
        if invite_only is not None:
            data["invite_only"] = invite_only
        if history_public_to_subscribers is not None:
            data["history_public_to_subscribers"] = history_public_to_subscribers
        return client.request("POST", "/users/me/subscriptions", data=data)

    @mcp.tool()
    def zulip_unsubscribe(streams: list[str], principals=None):
        """Unsubscribe from streams."""
        data = {"subscriptions": streams}
        if principals is not None:
            data["principals"] = principals
        return client.request("DELETE", "/users/me/subscriptions", data=data)

    @mcp.tool()
    def zulip_update_subscription_settings(stream_id: int, color: str | None = None, is_muted: bool | None = None, pin_to_top: bool | None = None, desktop_notifications: bool | None = None, audible_notifications: bool | None = None, push_notifications: bool | None = None, email_notifications: bool | None = None, wildcard_mentions_notify: bool | None = None):
        """Update per-stream subscription settings."""
        data = {"stream_id": stream_id}
        if color is not None:
            data["color"] = color
        if is_muted is not None:
            data["is_muted"] = is_muted
        if pin_to_top is not None:
            data["pin_to_top"] = pin_to_top
        if desktop_notifications is not None:
            data["desktop_notifications"] = desktop_notifications
        if audible_notifications is not None:
            data["audible_notifications"] = audible_notifications
        if push_notifications is not None:
            data["push_notifications"] = push_notifications
        if email_notifications is not None:
            data["email_notifications"] = email_notifications
        if wildcard_mentions_notify is not None:
            data["wildcard_mentions_notify"] = wildcard_mentions_notify
        return client.request("POST", "/users/me/subscriptions/properties", data=data)
