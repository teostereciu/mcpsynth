"""
Zulip MCP Tools — Webhooks / Bots / Integrations domain
Covers: bots (list, create, update, deactivate), webhooks, API keys
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_webhook_tools(mcp: FastMCP):

    @mcp.tool()
    def get_bots() -> dict:
        """List all bots in the organisation."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/bots", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_own_bots() -> dict:
        """List all bots owned by the current user."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/users/me/bots", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_bot(
        full_name: str,
        short_name: str,
        bot_type: int = 1,
        default_sending_stream: str = "",
        default_events_register_stream: str = "",
        default_all_public_streams: bool = False,
        service_name: str = "",
        config_data: str = "",
    ) -> dict:
        """Create a new bot account.

        Args:
            full_name: The display name of the bot.
            short_name: The short name (used to form the bot's email address).
            bot_type: 1=generic bot (default), 2=incoming webhook, 3=outgoing webhook,
                      4=embedded bot.
            default_sending_stream: Default stream for the bot to send messages to.
            default_events_register_stream: Default stream for event registration.
            default_all_public_streams: Whether the bot receives events from all public streams.
            service_name: For embedded bots, the service name.
            config_data: JSON object of configuration data for the bot service.
        """
        base, auth = _client()
        payload: dict = {
            "full_name": full_name,
            "short_name": short_name,
            "bot_type": bot_type,
            "default_all_public_streams": default_all_public_streams,
        }
        if default_sending_stream:
            payload["default_sending_stream"] = default_sending_stream
        if default_events_register_stream:
            payload["default_events_register_stream"] = default_events_register_stream
        if service_name:
            payload["service_name"] = service_name
        if config_data:
            payload["config_data"] = config_data
        try:
            r = requests.post(f"{base}/bots", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_bot(
        bot_id: int,
        full_name: str = "",
        default_sending_stream: str = "",
        default_events_register_stream: str = "",
        default_all_public_streams: bool = False,
    ) -> dict:
        """Update a bot's settings.

        Args:
            bot_id: The numeric ID of the bot to update.
            full_name: New display name (leave blank to keep current).
            default_sending_stream: New default sending stream.
            default_events_register_stream: New default events stream.
            default_all_public_streams: Whether the bot receives all public stream events.
        """
        base, auth = _client()
        payload: dict = {
            "default_all_public_streams": default_all_public_streams,
        }
        if full_name:
            payload["full_name"] = full_name
        if default_sending_stream:
            payload["default_sending_stream"] = default_sending_stream
        if default_events_register_stream:
            payload["default_events_register_stream"] = default_events_register_stream
        try:
            r = requests.patch(f"{base}/bots/{bot_id}", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def deactivate_bot(bot_id: int) -> dict:
        """Deactivate a bot account.

        Args:
            bot_id: The numeric ID of the bot to deactivate.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/bots/{bot_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def reactivate_bot(bot_id: int) -> dict:
        """Reactivate a previously deactivated bot.

        Args:
            bot_id: The numeric ID of the bot to reactivate.
        """
        base, auth = _client()
        try:
            r = requests.post(f"{base}/bots/{bot_id}/reactivate", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_bot_api_key(bot_id: int) -> dict:
        """Retrieve the API key for a bot (owner or admin only).

        Args:
            bot_id: The numeric ID of the bot.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/bots/{bot_id}/api_key/regenerate", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def regenerate_bot_api_key(bot_id: int) -> dict:
        """Regenerate the API key for a bot (owner or admin only).

        Args:
            bot_id: The numeric ID of the bot.
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/bots/{bot_id}/api_key/regenerate", auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}
