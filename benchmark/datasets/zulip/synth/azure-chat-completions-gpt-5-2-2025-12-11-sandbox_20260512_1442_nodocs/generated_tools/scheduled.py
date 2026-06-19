from __future__ import annotations

from zulip_client import ZulipClient


def register(mcp, client: ZulipClient):
    @mcp.tool()
    def zulip_create_scheduled_message(type: str, to, content: str, scheduled_delivery_timestamp: int, topic: str | None = None):
        """Schedule a message."""
        data = {
            "type": type,
            "to": to,
            "content": content,
            "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
        }
        if topic is not None:
            data["topic"] = topic
        return client.request("POST", "/scheduled_messages", data=data)

    @mcp.tool()
    def zulip_get_scheduled_messages():
        """List scheduled messages."""
        return client.request("GET", "/scheduled_messages")

    @mcp.tool()
    def zulip_delete_scheduled_message(scheduled_message_id: int):
        """Delete a scheduled message."""
        return client.request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
