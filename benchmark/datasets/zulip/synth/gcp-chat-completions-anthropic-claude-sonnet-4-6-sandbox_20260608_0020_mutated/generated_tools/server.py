"""Zulip Server/Organization API tools."""
import json
from typing import Optional, List
from .client import zulip_request


def get_server_settings() -> dict:
    """Get global settings for the Zulip server (no authentication required)."""
    try:
        return zulip_request("GET", "server_settings")
    except Exception as e:
        return {"error": str(e)}


def get_linkifiers() -> dict:
    """Get all linkifiers (URL patterns) configured for the organization."""
    try:
        return zulip_request("GET", "realm/linkifiers")
    except Exception as e:
        return {"error": str(e)}


def add_linkifier(pattern: str, url_template: str) -> dict:
    """Add a new linkifier to the organization.

    Args:
        pattern: The Python regular expression pattern to match.
        url_template: The RFC 6570 URL template to use for the linkifier.
    """
    try:
        return zulip_request("POST", "realm/filters", data={"pattern": pattern, "url_template": url_template})
    except Exception as e:
        return {"error": str(e)}


def update_linkifier(filter_id: int, pattern: str, url_template: str) -> dict:
    """Update an existing linkifier.

    Args:
        filter_id: The ID of the linkifier to update.
        pattern: The new Python regular expression pattern.
        url_template: The new RFC 6570 URL template.
    """
    try:
        return zulip_request(
            "PATCH",
            f"realm/filters/{filter_id}",
            data={"pattern": pattern, "url_template": url_template},
        )
    except Exception as e:
        return {"error": str(e)}


def remove_linkifier(filter_id: int) -> dict:
    """Remove a linkifier from the organization.

    Args:
        filter_id: The ID of the linkifier to remove.
    """
    try:
        return zulip_request("DELETE", f"realm/filters/{filter_id}")
    except Exception as e:
        return {"error": str(e)}


def reorder_linkifiers(ordered_linkifier_ids: List[int]) -> dict:
    """Reorder the linkifiers in the organization.

    Args:
        ordered_linkifier_ids: List of linkifier IDs in the desired order.
    """
    try:
        return zulip_request(
            "PATCH",
            "realm/linkifiers",
            data={"ordered_linkifier_ids": json.dumps(ordered_linkifier_ids)},
        )
    except Exception as e:
        return {"error": str(e)}


def add_code_playground(name: str, pygments_language: str, url_template: str) -> dict:
    """Add a code playground to the organization.

    Args:
        name: The name of the code playground.
        pygments_language: The Pygments language identifier.
        url_template: The RFC 6570 URL template for the playground.
    """
    try:
        data = {
            "name": name,
            "pygments_language": pygments_language,
            "url_template": url_template,
        }
        return zulip_request("POST", "realm/playgrounds", data=data)
    except Exception as e:
        return {"error": str(e)}


def remove_code_playground(playground_id: int) -> dict:
    """Remove a code playground from the organization.

    Args:
        playground_id: The ID of the code playground to remove.
    """
    try:
        return zulip_request("DELETE", f"realm/playgrounds/{playground_id}")
    except Exception as e:
        return {"error": str(e)}


def get_custom_emoji() -> dict:
    """Get all custom emoji in the organization."""
    try:
        return zulip_request("GET", "realm/emoji")
    except Exception as e:
        return {"error": str(e)}


def deactivate_custom_emoji(emoji_name: str) -> dict:
    """Deactivate a custom emoji in the organization.

    Args:
        emoji_name: The name of the custom emoji to deactivate.
    """
    try:
        return zulip_request("DELETE", f"realm/emoji/{emoji_name}")
    except Exception as e:
        return {"error": str(e)}


def get_custom_profile_fields() -> dict:
    """Get all custom profile fields defined in the organization."""
    try:
        return zulip_request("GET", "realm/profile_fields")
    except Exception as e:
        return {"error": str(e)}


def create_custom_profile_field(
    field_type: int,
    name: Optional[str] = None,
    hint: Optional[str] = None,
    field_data: Optional[dict] = None,
    display_in_profile_summary: Optional[bool] = None,
) -> dict:
    """Create a new custom profile field.

    Args:
        field_type: The type of field (1=short text, 2=long text, 3=select, 4=date, 5=link, 6=user, 7=external account, 8=pronouns).
        name: The name of the custom profile field.
        hint: Hint text for the field.
        field_data: Additional data for select/external account fields.
        display_in_profile_summary: Whether to display in profile summary.
    """
    try:
        data: dict = {"field_type": field_type}
        if name is not None:
            data["name"] = name
        if hint is not None:
            data["hint"] = hint
        if field_data is not None:
            data["field_data"] = json.dumps(field_data)
        if display_in_profile_summary is not None:
            data["display_in_profile_summary"] = json.dumps(display_in_profile_summary)
        return zulip_request("POST", "realm/profile_fields", data=data)
    except Exception as e:
        return {"error": str(e)}


def reorder_custom_profile_fields(order: List[int]) -> dict:
    """Reorder the custom profile fields in the organization.

    Args:
        order: List of custom profile field IDs in the desired order.
    """
    try:
        return zulip_request("PATCH", "realm/profile_fields", data={"order": json.dumps(order)})
    except Exception as e:
        return {"error": str(e)}


def get_realm_exports() -> dict:
    """Get all data exports for the organization."""
    try:
        return zulip_request("GET", "export/realm")
    except Exception as e:
        return {"error": str(e)}


def export_realm() -> dict:
    """Create a new data export for the organization (admin only)."""
    try:
        return zulip_request("POST", "export/realm")
    except Exception as e:
        return {"error": str(e)}


def get_realm_export_consents() -> dict:
    """Get the data export consent state for all users in the organization."""
    try:
        return zulip_request("GET", "export/realm/consents")
    except Exception as e:
        return {"error": str(e)}


def get_invites() -> dict:
    """Get all pending invitations for the organization."""
    try:
        return zulip_request("GET", "invites")
    except Exception as e:
        return {"error": str(e)}


def send_invites(
    invitee_emails: str,
    stream_ids: List[int],
    invite_as: int = 400,
    invite_expires_in_minutes: Optional[int] = None,
    include_realm_default_subscriptions: bool = False,
) -> dict:
    """Send email invitations to join the organization.

    Args:
        invitee_emails: Comma or newline-separated email addresses to invite.
        stream_ids: List of channel IDs to subscribe new users to.
        invite_as: Role for invited users (100=owner, 200=admin, 300=moderator, 400=member, 600=guest).
        invite_expires_in_minutes: Minutes until invitation expires (None = never expires).
        include_realm_default_subscriptions: Whether to subscribe to default channels.
    """
    try:
        data: dict = {
            "invitee_emails": invitee_emails,
            "stream_ids": json.dumps(stream_ids),
            "invite_as": invite_as,
            "include_realm_default_subscriptions": json.dumps(include_realm_default_subscriptions),
        }
        if invite_expires_in_minutes is not None:
            data["invite_expires_in_minutes"] = invite_expires_in_minutes
        return zulip_request("POST", "invites", data=data)
    except Exception as e:
        return {"error": str(e)}


def revoke_email_invite(invite_id: int) -> dict:
    """Revoke a pending email invitation.

    Args:
        invite_id: The ID of the invitation to revoke.
    """
    try:
        return zulip_request("DELETE", f"invites/{invite_id}")
    except Exception as e:
        return {"error": str(e)}


def resend_email_invite(invite_id: int) -> dict:
    """Resend a pending email invitation.

    Args:
        invite_id: The ID of the invitation to resend.
    """
    try:
        return zulip_request("POST", f"invites/{invite_id}/resend")
    except Exception as e:
        return {"error": str(e)}


def create_invite_link(
    invite_expires_in_minutes: Optional[int] = None,
    invite_as: int = 400,
    stream_ids: Optional[List[int]] = None,
) -> dict:
    """Create a reusable invitation link.

    Args:
        invite_expires_in_minutes: Minutes until the link expires (None = never).
        invite_as: Role for users who join via this link.
        stream_ids: List of channel IDs to subscribe new users to.
    """
    try:
        data: dict = {"invite_as": invite_as}
        if invite_expires_in_minutes is not None:
            data["invite_expires_in_minutes"] = invite_expires_in_minutes
        if stream_ids is not None:
            data["stream_ids"] = json.dumps(stream_ids)
        return zulip_request("POST", "invites/multiuse", data=data)
    except Exception as e:
        return {"error": str(e)}


def revoke_invite_link(invite_id: int) -> dict:
    """Revoke a reusable invitation link.

    Args:
        invite_id: The ID of the invitation link to revoke.
    """
    try:
        return zulip_request("DELETE", f"invites/multiuse/{invite_id}")
    except Exception as e:
        return {"error": str(e)}
