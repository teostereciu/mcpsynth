"""Zulip Users API tools."""
import json
from typing import Optional, List, Any
from .client import zulip_request


def get_users(
    include_custom_profile_fields: bool = False,
    client_gravatar: bool = True,
) -> dict:
    """Get all users in the organization.

    Args:
        include_custom_profile_fields: Whether to include custom profile field data.
        client_gravatar: Whether the client supports computing gravatar URLs.
    """
    try:
        params = {
            "include_custom_profile_fields": json.dumps(include_custom_profile_fields),
            "client_gravatar": json.dumps(client_gravatar),
        }
        return zulip_request("GET", "users", params=params)
    except Exception as e:
        return {"error": str(e)}


def get_user(user_id: int, include_custom_profile_fields: bool = False) -> dict:
    """Get details for a single user by ID.

    Args:
        user_id: The target user's ID.
        include_custom_profile_fields: Whether to include custom profile field data.
    """
    try:
        params = {
            "include_custom_profile_fields": json.dumps(include_custom_profile_fields),
        }
        return zulip_request("GET", f"users/{user_id}", params=params)
    except Exception as e:
        return {"error": str(e)}


def get_user_by_email(email: str, include_custom_profile_fields: bool = False) -> dict:
    """Get details for a user by their Zulip API email address.

    Args:
        email: The user's Zulip API email address.
        include_custom_profile_fields: Whether to include custom profile field data.
    """
    try:
        params = {
            "include_custom_profile_fields": json.dumps(include_custom_profile_fields),
        }
        return zulip_request("GET", f"users/{email}", params=params)
    except Exception as e:
        return {"error": str(e)}


def get_own_user() -> dict:
    """Get basic data about the current user/bot."""
    try:
        return zulip_request("GET", "users/me")
    except Exception as e:
        return {"error": str(e)}


def create_user(email: str, password: str, full_name: str) -> dict:
    """Create a new user account (admin only).

    Args:
        email: The email address of the new user.
        password: The password for the new user.
        full_name: The full name of the new user.
    """
    try:
        data = {"email": email, "password": password, "full_name": full_name}
        return zulip_request("POST", "users", data=data)
    except Exception as e:
        return {"error": str(e)}


def update_user(
    user_id: int,
    full_name: Optional[str] = None,
    role: Optional[int] = None,
    profile_data: Optional[List[dict]] = None,
    new_email: Optional[str] = None,
) -> dict:
    """Update a user's details (admin only).

    Args:
        user_id: The target user's ID.
        full_name: New full name for the user.
        role: New role (100=owner, 200=admin, 300=moderator, 400=member, 600=guest).
        profile_data: List of custom profile field updates e.g. [{"id": 4, "value": "..."}].
        new_email: New email address for the user (owner only).
    """
    try:
        data: dict = {}
        if full_name is not None:
            data["full_name"] = full_name
        if role is not None:
            data["role"] = role
        if profile_data is not None:
            data["profile_data"] = json.dumps(profile_data)
        if new_email is not None:
            data["new_email"] = new_email
        return zulip_request("PATCH", f"users/{user_id}", data=data)
    except Exception as e:
        return {"error": str(e)}


def deactivate_user(user_id: int) -> dict:
    """Deactivate a user account (admin only).

    Args:
        user_id: The target user's ID.
    """
    try:
        return zulip_request("DELETE", f"users/{user_id}")
    except Exception as e:
        return {"error": str(e)}


def reactivate_user(user_id: int) -> dict:
    """Reactivate a deactivated user account (admin only).

    Args:
        user_id: The target user's ID.
    """
    try:
        return zulip_request("POST", f"users/{user_id}/reactivate")
    except Exception as e:
        return {"error": str(e)}


def deactivate_own_user() -> dict:
    """Deactivate the current user's own account."""
    try:
        return zulip_request("DELETE", "users/me")
    except Exception as e:
        return {"error": str(e)}


def get_user_presence(user_id_or_email: str) -> dict:
    """Get the presence status for a specific user.

    Args:
        user_id_or_email: The user's ID or Zulip API email address.
    """
    try:
        return zulip_request("GET", f"users/{user_id_or_email}/presence")
    except Exception as e:
        return {"error": str(e)}


def get_presence() -> dict:
    """Get presence information for all users in the organization."""
    try:
        return zulip_request("GET", "realm/presence")
    except Exception as e:
        return {"error": str(e)}


def update_presence(
    status: str,
    ping_only: bool = False,
    new_user_input: bool = False,
) -> dict:
    """Update the current user's presence status.

    Args:
        status: Presence status - 'active' or 'idle'.
        ping_only: If True, only update the timestamp without changing status.
        new_user_input: Whether the user has had new input since the last update.
    """
    try:
        data = {
            "status": status,
            "ping_only": json.dumps(ping_only),
            "new_user_input": json.dumps(new_user_input),
        }
        return zulip_request("POST", "users/me/presence", data=data)
    except Exception as e:
        return {"error": str(e)}


def get_user_status(user_id: int) -> dict:
    """Get a user's status (emoji and text).

    Args:
        user_id: The target user's ID.
    """
    try:
        return zulip_request("GET", f"users/{user_id}/status")
    except Exception as e:
        return {"error": str(e)}


def update_status(
    status_text: Optional[str] = None,
    away: Optional[bool] = None,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> dict:
    """Update the current user's status.

    Args:
        status_text: The text content of the status message.
        away: Whether the user is away (deprecated, use emoji instead).
        emoji_name: The emoji name for the status.
        emoji_code: The emoji code for the status.
        reaction_type: The type of emoji reaction.
    """
    try:
        data: dict = {}
        if status_text is not None:
            data["status_text"] = status_text
        if away is not None:
            data["away"] = json.dumps(away)
        if emoji_name is not None:
            data["emoji_name"] = emoji_name
        if emoji_code is not None:
            data["emoji_code"] = emoji_code
        if reaction_type is not None:
            data["reaction_type"] = reaction_type
        return zulip_request("POST", "users/me/status", data=data)
    except Exception as e:
        return {"error": str(e)}


def mute_user(muted_user_id: int) -> dict:
    """Mute a user.

    Args:
        muted_user_id: The ID of the user to mute.
    """
    try:
        return zulip_request("POST", f"users/me/muted_users/{muted_user_id}")
    except Exception as e:
        return {"error": str(e)}


def unmute_user(muted_user_id: int) -> dict:
    """Unmute a previously muted user.

    Args:
        muted_user_id: The ID of the user to unmute.
    """
    try:
        return zulip_request("DELETE", f"users/me/muted_users/{muted_user_id}")
    except Exception as e:
        return {"error": str(e)}


def get_alert_words() -> dict:
    """Get all alert words for the current user."""
    try:
        return zulip_request("GET", "users/me/alert_words")
    except Exception as e:
        return {"error": str(e)}


def add_alert_words(alert_words: List[str]) -> dict:
    """Add alert words for the current user.

    Args:
        alert_words: List of alert words to add.
    """
    try:
        return zulip_request("POST", "users/me/alert_words", data={"alert_words": json.dumps(alert_words)})
    except Exception as e:
        return {"error": str(e)}


def remove_alert_words(alert_words: List[str]) -> dict:
    """Remove alert words for the current user.

    Args:
        alert_words: List of alert words to remove.
    """
    try:
        return zulip_request("DELETE", "users/me/alert_words", data={"alert_words": json.dumps(alert_words)})
    except Exception as e:
        return {"error": str(e)}


def get_attachments() -> dict:
    """Get all file attachments uploaded by the current user."""
    try:
        return zulip_request("GET", "attachments")
    except Exception as e:
        return {"error": str(e)}


def remove_attachment(attachment_id: int) -> dict:
    """Delete an uploaded file attachment.

    Args:
        attachment_id: The ID of the attachment to delete.
    """
    try:
        return zulip_request("DELETE", f"attachments/{attachment_id}")
    except Exception as e:
        return {"error": str(e)}


def set_typing_status(
    op: str,
    to: List[int],
    type: str = "direct",
    topic: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> dict:
    """Set the typing status for a conversation.

    Args:
        op: 'start' or 'stop' typing.
        to: List of user IDs for direct messages, or empty for channel messages.
        type: 'direct' for DMs or 'channel' for channel messages.
        topic: Topic name for channel messages.
        stream_id: Channel ID for channel messages.
    """
    try:
        data: dict = {"op": op, "to": json.dumps(to), "type": type}
        if topic is not None:
            data["topic"] = topic
        if stream_id is not None:
            data["stream_id"] = stream_id
        return zulip_request("POST", "typing", data=data)
    except Exception as e:
        return {"error": str(e)}


def regenerate_api_key() -> dict:
    """Regenerate the current user's API key."""
    try:
        return zulip_request("POST", "users/me/api_key/regenerate")
    except Exception as e:
        return {"error": str(e)}
