"""
Zulip MCP Tools — Scheduled Messages domain
Covers: list, create, edit, delete scheduled messages
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_scheduled_message_tools(mcp: FastMCP):

    @mcp.tool()
    def get_scheduled_messages() -> dict:
        """List all scheduled messages for the current user."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/scheduled_messages", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_scheduled_message(
        type: str,
        to: str,
        content: str,
        scheduled_delivery_timestamp: int,
        topic: str = "",
    ) -> dict:
        """Schedule a message to be sent at a future time.

        Args:
            type: 'stream' or 'direct'.
            to: For stream messages, the stream name or ID.
                For direct messages, a JSON list of user IDs or emails.
            content: The message content (Markdown supported).
            scheduled_delivery_timestamp: Unix timestamp (seconds) for when to send.
            topic: Required for stream messages; the topic name.
        """
        base, auth = _client()
        payload: dict = {
            "type": type,
            "to": to,
            "content": content,
            "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
        }
        if topic:
            payload["topic"] = topic
        try:
            r = requests.post(f"{base}/scheduled_messages", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_scheduled_message(
        scheduled_message_id: int,
        type: str = "",
        to: str = "",
        content: str = "",
        topic: str = "",
        scheduled_delivery_timestamp: int = 0,
    ) -> dict:
        """Edit an existing scheduled message.

        Args:
            scheduled_message_id: The numeric ID of the scheduled message.
            type: New type ('stream' or 'direct'); leave blank to keep current.
            to: New recipient; leave blank to keep current.
            content: New content; leave blank to keep current.
            topic: New topic; leave blank to keep current.
            scheduled_delivery_timestamp: New Unix timestamp; 0 to keep current.
        """
        base, auth = _client()
        payload: dict = {}
        if type:
            payload["type"] = type
        if to:
            payload["to"] = to
        if content:
            payload["content"] = content
        if topic:
            payload["topic"] = topic
        if scheduled_delivery_timestamp:
            payload["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
        try:
            r = requests.patch(
                f"{base}/scheduled_messages/{scheduled_message_id}",
                data=payload,
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_scheduled_message(scheduled_message_id: int) -> dict:
        """Delete a scheduled message.

        Args:
            scheduled_message_id: The numeric ID of the scheduled message to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(
                f"{base}/scheduled_messages/{scheduled_message_id}", auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}
