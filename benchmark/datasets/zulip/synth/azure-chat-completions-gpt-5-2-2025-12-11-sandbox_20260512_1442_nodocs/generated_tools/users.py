from __future__ import annotations

from zulip_client import ZulipClient


def register(mcp, client: ZulipClient):
    @mcp.tool()
    def zulip_get_own_profile():
        """Get the authenticated user's profile."""
        return client.request("GET", "/users/me")

    @mcp.tool()
    def zulip_get_users(client_gravatar: bool | None = None, include_custom_profile_fields: bool | None = None):
        """List users."""
        params = {}
        if client_gravatar is not None:
            params["client_gravatar"] = client_gravatar
        if include_custom_profile_fields is not None:
            params["include_custom_profile_fields"] = include_custom_profile_fields
        return client.request("GET", "/users", params=params)

    @mcp.tool()
    def zulip_get_user(user_id: int, client_gravatar: bool | None = None):
        """Get a user by ID."""
        params = {}
        if client_gravatar is not None:
            params["client_gravatar"] = client_gravatar
        return client.request("GET", f"/users/{user_id}", params=params)

    @mcp.tool()
    def zulip_get_presence(user_id_or_email: str):
        """Get presence for a user (by email or user_id as string)."""
        return client.request("GET", f"/users/{user_id_or_email}/presence")

    @mcp.tool()
    def zulip_update_own_status_text(status_text: str | None = None, away: bool | None = None, emoji_name: str | None = None, emoji_code: str | None = None, reaction_type: str | None = None):
        """Update your status."""
        data = {}
        if status_text is not None:
            data["status_text"] = status_text
        if away is not None:
            data["away"] = away
        if emoji_name is not None:
            data["emoji_name"] = emoji_name
        if emoji_code is not None:
            data["emoji_code"] = emoji_code
        if reaction_type is not None:
            data["reaction_type"] = reaction_type
        return client.request("POST", "/users/me/status", data=data)
