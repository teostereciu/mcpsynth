"""
Zulip MCP Tools — Reactions domain
Covers: add and remove emoji reactions on messages
"""

from typing import Optional
from .client import zulip_post, zulip_delete


def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> dict:
    """Add an emoji reaction to a message.

    Args:
        message_id: The ID of the message to react to.
        emoji_name: The name of the emoji, e.g. "thumbs_up" or "octopus".
        emoji_code: The code for the emoji (optional; derived from emoji_name if omitted).
                    For Unicode emoji this is the hex codepoint, e.g. "1f44d".
        reaction_type: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji".
                       Defaults to "unicode_emoji" if omitted.
    """
    params: dict = {"emoji_name": emoji_name}
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    return zulip_post(f"/messages/{message_id}/reactions", params)


def remove_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> dict:
    """Remove an emoji reaction from a message.

    Args:
        message_id: The ID of the message to remove the reaction from.
        emoji_name: The name of the emoji to remove.
        emoji_code: The code for the emoji (optional).
        reaction_type: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji".
    """
    params: dict = {"emoji_name": emoji_name}
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    return zulip_delete(f"/messages/{message_id}/reactions", params)
