"""
Zulip MCP Tools — Users domain
Covers: profiles, presence, create, update, deactivate, groups, settings
"""

from typing import Optional
from .client import zulip_get, zulip_post, zulip_patch, zulip_delete


def get_users(
    client_gravatar: bool = False,
    include_custom_profile_fields: bool = False,
) -> dict:
    """Get all users (members) in the Zulip organization.

    Args:
        client_gravatar: If True, the server will not compute Gravatar URLs.
        include_custom_profile_fields: If True, include custom profile field data.
    """
    return zulip_get(
        "/users",
        {
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        },
    )


def get_user(
    user_id: int,
    client_gravatar: bool = False,
    include_custom_profile_fields: bool = False,
) -> dict:
    """Get details about a specific user by their ID.

    Args:
        user_id: The unique ID of the user.
        client_gravatar: If True, the server will not compute Gravatar URLs.
        include_custom_profile_fields: If True, include custom profile field data.
    """
    return zulip_get(
        f"/users/{user_id}",
        {
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        },
    )


def get_user_by_email(
    email: str,
    client_gravatar: bool = False,
    include_custom_profile_fields: bool = False,
) -> dict:
    """Get details about a user by their email address.

    Args:
        email: The email address of the user.
        client_gravatar: If True, the server will not compute Gravatar URLs.
        include_custom_profile_fields: If True, include custom profile field data.
    """
    return zulip_get(
        f"/users/{email}",
        {
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        },
    )


def get_own_user() -> dict:
    """Get the profile of the currently authenticated user."""
    return zulip_get("/users/me")


def create_user(email: str, password: str, full_name: str) -> dict:
    """Create a new user account. Requires admin privileges.

    Args:
        email: The email address for the new user.
        password: The password for the new user.
        full_name: The full name of the new user.
    """
    return zulip_post(
        "/users", {"email": email, "password": password, "full_name": full_name}
    )


def update_user(
    user_id: int,
    full_name: Optional[str] = None,
    role: Optional[int] = None,
    profile_data: Optional[str] = None,
    new_email: Optional[str] = None,
) -> dict:
    """Update a user's profile. Requires admin privileges.

    Args:
        user_id: The ID of the user to update.
        full_name: New full name for the user.
        role: New role: 100=owner, 200=admin, 300=moderator, 400=member, 600=guest.
        profile_data: JSON-encoded list of custom profile field updates,
                      e.g. '[{"id":1,"value":"new value"}]'.
        new_email: New email address for the user.
    """
    params: dict = {}
    if full_name is not None:
        params["full_name"] = full_name
    if role is not None:
        params["role"] = role
    if profile_data is not None:
        params["profile_data"] = profile_data
    if new_email is not None:
        params["new_email"] = new_email
    return zulip_patch(f"/users/{user_id}", params)


def deactivate_user(user_id: int) -> dict:
    """Deactivate a user account. Requires admin privileges.

    Args:
        user_id: The ID of the user to deactivate.
    """
    return zulip_delete(f"/users/{user_id}")


def reactivate_user(user_id: int) -> dict:
    """Reactivate a previously deactivated user. Requires admin privileges.

    Args:
        user_id: The ID of the user to reactivate.
    """
    return zulip_post(f"/users/{user_id}/reactivate", {})


def get_user_presence(user_id_or_email: str) -> dict:
    """Get the presence (online status) of a specific user.

    Args:
        user_id_or_email: The user's ID or email address.
    """
    return zulip_get(f"/users/{user_id_or_email}/presence")


def get_all_presence() -> dict:
    """Get the presence information for all users in the organization."""
    return zulip_get("/realm/presence")


def update_own_presence(status: str, slim_presence: bool = False) -> dict:
    """Update the current user's presence status.

    Args:
        status: "active" or "idle".
        slim_presence: If True, use the slim presence format.
    """
    return zulip_post(
        "/users/me/presence", {"status": status, "slim_presence": slim_presence}
    )


def get_user_groups() -> dict:
    """Get all user groups in the organization."""
    return zulip_get("/user_groups")


def create_user_group(
    name: str, description: str, members: str
) -> dict:
    """Create a new user group.

    Args:
        name: The name of the user group.
        description: A description of the user group.
        members: JSON-encoded list of user IDs to include in the group,
                 e.g. "[1, 2, 3]".
    """
    return zulip_post(
        "/user_groups/create",
        {"name": name, "description": description, "members": members},
    )


def update_user_group(
    group_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a user group's name or description.

    Args:
        group_id: The ID of the user group to update.
        name: New name for the group.
        description: New description for the group.
    """
    params: dict = {}
    if name is not None:
        params["name"] = name
    if description is not None:
        params["description"] = description
    return zulip_patch(f"/user_groups/{group_id}", params)


def delete_user_group(group_id: int) -> dict:
    """Delete a user group.

    Args:
        group_id: The ID of the user group to delete.
    """
    return zulip_delete(f"/user_groups/{group_id}")


def update_user_group_members(
    group_id: int,
    add: Optional[str] = None,
    delete: Optional[str] = None,
) -> dict:
    """Add or remove members from a user group.

    Args:
        group_id: The ID of the user group.
        add: JSON-encoded list of user IDs to add, e.g. "[4, 5]".
        delete: JSON-encoded list of user IDs to remove, e.g. "[2]".
    """
    params: dict = {}
    if add is not None:
        params["add"] = add
    if delete is not None:
        params["delete"] = delete
    return zulip_post(f"/user_groups/{group_id}/members", params)


def get_user_group_members(group_id: int) -> dict:
    """Get the members of a user group.

    Args:
        group_id: The ID of the user group.
    """
    return zulip_get(f"/user_groups/{group_id}/members")


def mute_user(muted_user_id: int) -> dict:
    """Mute a user. Muted users' messages are hidden.

    Args:
        muted_user_id: The ID of the user to mute.
    """
    return zulip_post(f"/users/me/muted_users/{muted_user_id}", {})


def unmute_user(muted_user_id: int) -> dict:
    """Unmute a previously muted user.

    Args:
        muted_user_id: The ID of the user to unmute.
    """
    return zulip_delete(f"/users/me/muted_users/{muted_user_id}")


def get_muted_users() -> dict:
    """Get the list of users muted by the current user."""
    return zulip_get("/users/me/muted_users")


def update_own_settings(
    full_name: Optional[str] = None,
    email: Optional[str] = None,
    old_password: Optional[str] = None,
    new_password: Optional[str] = None,
    twenty_four_hour_time: Optional[bool] = None,
    dense_mode: Optional[bool] = None,
    starred_message_counts: Optional[bool] = None,
    fluid_layout_width: Optional[bool] = None,
    high_contrast_mode: Optional[bool] = None,
    color_scheme: Optional[int] = None,
    enable_drafts_synchronization: Optional[bool] = None,
    translate_emoticons: Optional[bool] = None,
    default_language: Optional[str] = None,
    default_view: Optional[str] = None,
    escape_navigates_to_default_view: Optional[bool] = None,
    send_stream: Optional[str] = None,
    wildcard_mentions_notify: Optional[bool] = None,
    enable_stream_desktop_notifications: Optional[bool] = None,
    enable_stream_email_notifications: Optional[bool] = None,
    enable_stream_push_notifications: Optional[bool] = None,
    enable_stream_audible_notifications: Optional[bool] = None,
    enable_desktop_notifications: Optional[bool] = None,
    enable_sounds: Optional[bool] = None,
    email_notifications_batching_period_seconds: Optional[int] = None,
    enable_offline_email_notifications: Optional[bool] = None,
    enable_offline_push_notifications: Optional[bool] = None,
    enable_online_push_notifications: Optional[bool] = None,
    enable_digest_emails: Optional[bool] = None,
    enable_marketing_emails: Optional[bool] = None,
    enable_login_emails: Optional[bool] = None,
    message_content_in_email_notifications: Optional[bool] = None,
    pm_content_in_desktop_notifications: Optional[bool] = None,
    presence_enabled: Optional[bool] = None,
    enter_sends: Optional[bool] = None,
) -> dict:
    """Update the current user's personal settings.

    Args:
        full_name: New display name.
        email: New email address.
        old_password: Current password (required when changing password).
        new_password: New password.
        twenty_four_hour_time: Use 24-hour clock format.
        dense_mode: Enable dense mode UI.
        starred_message_counts: Show starred message counts.
        fluid_layout_width: Use fluid layout width.
        high_contrast_mode: Enable high contrast mode.
        color_scheme: 1=automatic, 2=night, 3=day.
        enable_drafts_synchronization: Sync drafts across devices.
        translate_emoticons: Translate emoticons to emoji.
        default_language: Default language code, e.g. "en".
        default_view: Default view, e.g. "recent_topics" or "all_messages".
        escape_navigates_to_default_view: Escape key navigates to default view.
        send_stream: Default stream for sending messages.
        wildcard_mentions_notify: Notify on wildcard mentions.
        enable_stream_desktop_notifications: Desktop notifications for streams.
        enable_stream_email_notifications: Email notifications for streams.
        enable_stream_push_notifications: Push notifications for streams.
        enable_stream_audible_notifications: Audible notifications for streams.
        enable_desktop_notifications: Enable desktop notifications.
        enable_sounds: Enable notification sounds.
        email_notifications_batching_period_seconds: Batching period for emails.
        enable_offline_email_notifications: Email when offline.
        enable_offline_push_notifications: Push when offline.
        enable_online_push_notifications: Push when online.
        enable_digest_emails: Receive digest emails.
        enable_marketing_emails: Receive marketing emails.
        enable_login_emails: Receive login notification emails.
        message_content_in_email_notifications: Include content in email notifications.
        pm_content_in_desktop_notifications: Include DM content in desktop notifications.
        presence_enabled: Share presence information.
        enter_sends: Enter key sends messages.
    """
    params: dict = {}
    local_vars = locals()
    for key, val in local_vars.items():
        if key != "params" and val is not None:
            params[key] = val
    return zulip_patch("/settings", params)
