from __future__ import annotations

from zulip_client import ZulipClient


def register(mcp, client: ZulipClient):
    @mcp.tool()
    def zulip_get_stream_topics(stream_id: int):
        """Get topics in a stream."""
        return client.request("GET", f"/users/me/{stream_id}/topics")

    @mcp.tool()
    def zulip_rename_topic(stream_id: int, topic: str, new_topic: str, propagate_mode: str | None = None):
        """Rename a topic within a stream."""
        data = {"stream_id": stream_id, "topic": topic, "new_topic": new_topic}
        if propagate_mode is not None:
            data["propagate_mode"] = propagate_mode
        return client.request("POST", "/rename_topic", data=data)

    @mcp.tool()
    def zulip_mark_topic_as_resolved(stream_id: int, topic: str, resolved: bool = True):
        """Mark/unmark a topic as resolved."""
        data = {"stream_id": stream_id, "topic": topic, "resolved": resolved}
        return client.request("POST", "/mark_topic_as_resolved", data=data)

    @mcp.tool()
    def zulip_delete_topic(stream_id: int, topic_name: str):
        """Delete all messages in a topic."""
        return client.request("POST", "/delete_topic", data={"stream_id": stream_id, "topic_name": topic_name})
