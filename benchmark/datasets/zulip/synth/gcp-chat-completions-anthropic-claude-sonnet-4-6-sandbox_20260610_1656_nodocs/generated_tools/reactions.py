"""
Zulip MCP Tools — Reactions domain
Covers: add and remove emoji reactions on messages
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_reaction_tools(mcp: FastMCP):

    @mcp.tool()
    def add_reaction(
        message_id: int,
        emoji_name: str,
        emoji_code: str = "",
        reaction_type: str = "unicode_emoji",
    ) -> dict:
        """Add an emoji reaction to a message.

        Args:
            message_id: The numeric ID of the message to react to.
            emoji_name: The name of the emoji (e.g. 'thumbs_up', '+1').
            emoji_code: The emoji code (optional; derived from emoji_name if omitted).
            reaction_type: 'unicode_emoji' (default), 'realm_emoji', or 'zulip_extra_emoji'.
        """
        base, auth = _client()
        payload: dict = {
            "emoji_name": emoji_name,
            "reaction_type": reaction_type,
        }
        if emoji_code:
            payload["emoji_code"] = emoji_code
        try:
            r = requests.post(
                f"{base}/messages/{message_id}/reactions",
                data=payload,
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_reaction(
        message_id: int,
        emoji_name: str,
        emoji_code: str = "",
        reaction_type: str = "unicode_emoji",
    ) -> dict:
        """Remove an emoji reaction from a message.

        Args:
            message_id: The numeric ID of the message.
            emoji_name: The name of the emoji to remove.
            emoji_code: The emoji code (optional).
            reaction_type: 'unicode_emoji' (default), 'realm_emoji', or 'zulip_extra_emoji'.
        """
        base, auth = _client()
        payload: dict = {
            "emoji_name": emoji_name,
            "reaction_type": reaction_type,
        }
        if emoji_code:
            payload["emoji_code"] = emoji_code
        try:
            r = requests.delete(
                f"{base}/messages/{message_id}/reactions",
                data=payload,
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}
