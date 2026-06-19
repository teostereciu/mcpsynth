"""Zulip Invitations API tools."""
import json
from typing import Optional, List
from .client import zulip_request


def get_invites() -> dict:
    """Get all unexpired invitations (email and reusable links) that the user can manage."""
    return zulip_request("GET", "invites")


def send_invites(
    invitee_emails: str,
    stream_ids: List[int],
    invite_as: int = 400,
    invite_expires_in_minutes: Optional[int] = None,
    include_realm_default_subscriptions: bool = False,
    notify_referrer_on_join: bool = True,
) -> dict:
    """Send email invitations to one or more email addresses.

    Args:
        invitee_emails: Comma or newline-separated email addresses to invite.
        stream_ids: List of channel IDs to subscribe the new user to.
        invite_as: Role for invited users: 100=owner, 200=admin, 300=moderator,
                   400=member (default), 600=guest.
        invite_expires_in_minutes: Minutes until invitation expires. None = never expires.
        include_realm_default_subscriptions: Whether to subscribe to default channels.
        notify_referrer_on_join: Whether to notify the referrer when the invite is accepted.
    """
    data: dict = {
        "invitee_emails": invitee_emails,
        "stream_ids": json.dumps(stream_ids),
        "invite_as": invite_as,
        "include_realm_default_subscriptions": json.dumps(include_realm_default_subscriptions),
        "notify_referrer_on_join": json.dumps(notify_referrer_on_join),
    }
    if invite_expires_in_minutes is not None:
        data["invite_expires_in_minutes"] = invite_expires_in_minutes
    return zulip_request("POST", "invites", data=data)


def create_invite_link(
    stream_ids: List[int],
    invite_as: int = 400,
    invite_expires_in_minutes: Optional[int] = None,
    include_realm_default_subscriptions: bool = False,
    notify_referrer_on_join: bool = True,
) -> dict:
    """Create a reusable invitation link.

    Args:
        stream_ids: List of channel IDs to subscribe new users to.
        invite_as: Role for invited users: 100=owner, 200=admin, 300=moderator,
                   400=member (default), 600=guest.
        invite_expires_in_minutes: Minutes until the link expires. None = never expires.
        include_realm_default_subscriptions: Whether to subscribe to default channels.
        notify_referrer_on_join: Whether to notify the referrer when the invite is accepted.
    """
    data: dict = {
        "stream_ids": json.dumps(stream_ids),
        "invite_as": invite_as,
        "include_realm_default_subscriptions": json.dumps(include_realm_default_subscriptions),
        "notify_referrer_on_join": json.dumps(notify_referrer_on_join),
    }
    if invite_expires_in_minutes is not None:
        data["invite_expires_in_minutes"] = invite_expires_in_minutes
    return zulip_request("POST", "invites/multiuse", data=data)


def resend_email_invite(invite_id: int) -> dict:
    """Resend an email invitation.

    Args:
        invite_id: The ID of the email invitation to resend.
    """
    return zulip_request("POST", f"invites/{invite_id}/resend")


def revoke_email_invite(invite_id: int) -> dict:
    """Revoke an email invitation.

    Args:
        invite_id: The ID of the email invitation to revoke.
    """
    return zulip_request("DELETE", f"invites/{invite_id}")


def revoke_invite_link(invite_id: int) -> dict:
    """Revoke a reusable invitation link.

    Args:
        invite_id: The ID of the reusable invitation link to revoke.
    """
    return zulip_request("DELETE", f"invites/multiuse/{invite_id}")
