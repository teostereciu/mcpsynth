"""
Zulip MCP Tools — Users domain
Covers: list, get, create, update, deactivate, reactivate, presence, groups
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_user_tools(mcp: FastMCP):

    @mcp.tool()
    def get_users(
        client_gravatar: bool = False,
        include_custom_profile_fields: bool = False,
    ) -> dict:
        """List all users in the organisation.

        Args:
            client_gravatar: If True, return gravatar URLs instead of server-hosted avatars.
            include_custom_profile_fields: Include custom profile field data.
        """
        base, auth = _client()
        params = {
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        }
        try:
            r = requests.get(f"{base}/users", params=params, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_user(
        user_id: int,
        client_gravatar: bool = False,
        include_custom_profile_fields: bool = False,
    ) -> dict:
        """Get details of a specific user by ID.

        Args:
            user_id: The numeric ID of the user.
            client_gravatar: If True, return gravatar URLs.
            include_custom_profile_fields: Include custom profile field data.
        """
        base, auth = _client()
        params = {
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        }
        try:
            r = requests.get(f"{base}/users/{user_id}", params=params, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_user_by_email(
        email: str,
        client_gravatar: bool = False,
        include_custom_profile_fields: bool = False,
    ) -> dict:
        """Look up a user by their email address.

        Args:
            email: The email address of the user.
            client_gravatar: If True, return gravatar URLs.
            include_custom_profile_fields: Include custom profile field data.
        """
        base, auth = _client()
        params = {
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        }
        try:
            r = requests.get(
                f"{base}/users/{email}", params=params, auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_own_user() -> dict:
        """Get the profile of the currently authenticated user (self)."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/users/me", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_user(
        email: str,
        password: str,
        full_name: str,
    ) -> dict:
        """Create a new user account (admin only).

        Args:
            email: The email address for the new user.
            password: The initial password for the new user.
            full_name: The full display name for the new user.
        """
        base, auth = _client()
        payload = {"email": email, "password": password, "full_name": full_name}
        try:
            r = requests.post(f"{base}/users", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_user(
        user_id: int,
        full_name: str = "",
        role: int = 0,
        profile_data: str = "",
    ) -> dict:
        """Update a user's profile or role (admin only).

        Args:
            user_id: The numeric ID of the user to update.
            full_name: New full name (leave blank to keep current).
            role: New role integer — 100=owner, 200=admin, 300=moderator,
                  400=member, 600=guest (0 = no change).
            profile_data: JSON list of custom profile field updates,
                e.g. '[{"id":1,"value":"New value"}]'.
        """
        base, auth = _client()
        payload: dict = {}
        if full_name:
            payload["full_name"] = full_name
        if role:
            payload["role"] = role
        if profile_data:
            payload["profile_data"] = profile_data
        try:
            r = requests.patch(f"{base}/users/{user_id}", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def deactivate_user(user_id: int) -> dict:
        """Deactivate a user account (admin only).

        Args:
            user_id: The numeric ID of the user to deactivate.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/users/{user_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def reactivate_user(user_id: int) -> dict:
        """Reactivate a previously deactivated user account (admin only).

        Args:
            user_id: The numeric ID of the user to reactivate.
        """
        base, auth = _client()
        try:
            r = requests.post(f"{base}/users/{user_id}/reactivate", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_user_presence(user_id_or_email: str) -> dict:
        """Get the presence (online/idle/offline) status of a user.

        Args:
            user_id_or_email: The numeric user ID or email address.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/users/{user_id_or_email}/presence", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_all_presence() -> dict:
        """Get presence information for all users in the organisation."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/realm/presence", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_own_presence(
        status: str,
        slim_presence: bool = True,
        ping_only: bool = False,
    ) -> dict:
        """Update the presence status of the current user.

        Args:
            status: 'active' or 'idle'.
            slim_presence: Use the slim presence format.
            ping_only: If True, only ping without updating status.
        """
        base, auth = _client()
        payload = {
            "status": status,
            "slim_presence": slim_presence,
            "ping_only": ping_only,
        }
        try:
            r = requests.post(f"{base}/users/me/presence", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_user_groups() -> dict:
        """List all user groups in the organisation."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/user_groups", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_user_group(
        name: str,
        description: str,
        members: str,
    ) -> dict:
        """Create a new user group.

        Args:
            name: The name of the user group.
            description: A description of the user group.
            members: JSON list of user IDs to add as initial members, e.g. '[1, 2, 3]'.
        """
        base, auth = _client()
        payload = {"name": name, "description": description, "members": members}
        try:
            r = requests.post(f"{base}/user_groups/create", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_user_group(
        group_id: int,
        name: str = "",
        description: str = "",
    ) -> dict:
        """Update the name or description of a user group.

        Args:
            group_id: The numeric ID of the user group.
            name: New name (leave blank to keep current).
            description: New description (leave blank to keep current).
        """
        base, auth = _client()
        payload: dict = {}
        if name:
            payload["name"] = name
        if description:
            payload["description"] = description
        try:
            r = requests.patch(
                f"{base}/user_groups/{group_id}", data=payload, auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_user_group(group_id: int) -> dict:
        """Delete a user group.

        Args:
            group_id: The numeric ID of the user group to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/user_groups/{group_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_user_group_members(
        group_id: int,
        add: str = "[]",
        delete: str = "[]",
    ) -> dict:
        """Add or remove members from a user group.

        Args:
            group_id: The numeric ID of the user group.
            add: JSON list of user IDs to add, e.g. '[4, 5]'.
            delete: JSON list of user IDs to remove, e.g. '[2]'.
        """
        base, auth = _client()
        payload = {"add": add, "delete": delete}
        try:
            r = requests.post(
                f"{base}/user_groups/{group_id}/members", data=payload, auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_user_group_members(group_id: int) -> dict:
        """List all members of a user group.

        Args:
            group_id: The numeric ID of the user group.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/user_groups/{group_id}/members", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mute_user(muted_user_id: int) -> dict:
        """Mute a user so their messages are hidden.

        Args:
            muted_user_id: The numeric ID of the user to mute.
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/users/me/muted_users/{muted_user_id}", auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unmute_user(muted_user_id: int) -> dict:
        """Unmute a previously muted user.

        Args:
            muted_user_id: The numeric ID of the user to unmute.
        """
        base, auth = _client()
        try:
            r = requests.delete(
                f"{base}/users/me/muted_users/{muted_user_id}", auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_muted_users() -> dict:
        """List all users muted by the current user."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/users/me/muted_users", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_user_status(
        status_text: str = "",
        away: bool = False,
        emoji_name: str = "",
        emoji_code: str = "",
        reaction_type: str = "",
    ) -> dict:
        """Update the status of the current user.

        Args:
            status_text: Status message text (empty string clears it).
            away: Whether to set the user as away.
            emoji_name: Name of the status emoji (e.g. 'car').
            emoji_code: Code of the status emoji.
            reaction_type: Type of emoji — 'unicode_emoji', 'realm_emoji', or 'zulip_extra_emoji'.
        """
        base, auth = _client()
        payload: dict = {"status_text": status_text, "away": away}
        if emoji_name:
            payload["emoji_name"] = emoji_name
        if emoji_code:
            payload["emoji_code"] = emoji_code
        if reaction_type:
            payload["reaction_type"] = reaction_type
        try:
            r = requests.post(f"{base}/users/me/status", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_user_status(user_id: int) -> dict:
        """Get the status of a specific user.

        Args:
            user_id: The numeric ID of the user.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/users/{user_id}/status", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}
