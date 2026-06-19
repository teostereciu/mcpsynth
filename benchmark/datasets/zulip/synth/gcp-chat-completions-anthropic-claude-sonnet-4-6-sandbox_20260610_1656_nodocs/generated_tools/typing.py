"""
Zulip MCP Tools — Typing Notifications domain
Covers: send typing start/stop notifications for direct and stream messages
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_typing_tools(mcp: FastMCP):

    @mcp.tool()
    def send_typing_notification(
        op: str,
        to: str,
        type: str = "direct",
        stream_id: int = 0,
        topic: str = "",
    ) -> dict:
        """Send a typing notification (start or stop) to a conversation.

        Args:
            op: 'start' to indicate the user started typing, 'stop' to indicate they stopped.
            to: For direct messages, a JSON list of user IDs, e.g. '[4, 5]'.
                For stream messages, leave empty and use stream_id + topic.
            type: 'direct' (default) or 'stream'.
            stream_id: Stream ID (required when type='stream').
            topic: Topic name (required when type='stream').
        """
        base, auth = _client()
        payload: dict = {"op": op, "type": type}
        if type == "direct":
            payload["to"] = to
        else:
            payload["stream_id"] = stream_id
            payload["topic"] = topic
        try:
            r = requests.post(f"{base}/typing", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}
