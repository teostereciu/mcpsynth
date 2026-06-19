"""
Zulip MCP Tools — Event Queues domain
Covers: register queue, get events, delete queue
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_event_tools(mcp: FastMCP):

    @mcp.tool()
    def register_event_queue(
        event_types: str = "[]",
        narrow: str = "[]",
        all_public_streams: bool = False,
        include_subscribers: bool = False,
        client_gravatar: bool = False,
        apply_markdown: bool = True,
        slim_presence: bool = False,
    ) -> dict:
        """Register an event queue to receive real-time updates.

        Args:
            event_types: JSON list of event type strings to subscribe to,
                e.g. '["message","reaction"]'. Empty list means all events.
            narrow: JSON list of narrow filter objects to limit message events.
            all_public_streams: Whether to receive events from all public streams.
            include_subscribers: Include subscriber lists in stream data.
            client_gravatar: Return gravatar URLs for avatars.
            apply_markdown: Render message content as HTML.
            slim_presence: Use the slim presence format.
        """
        base, auth = _client()
        payload = {
            "event_types": event_types,
            "narrow": narrow,
            "all_public_streams": all_public_streams,
            "include_subscribers": include_subscribers,
            "client_gravatar": client_gravatar,
            "apply_markdown": apply_markdown,
            "slim_presence": slim_presence,
        }
        try:
            r = requests.post(f"{base}/register", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_events(
        queue_id: str,
        last_event_id: int = -1,
        dont_block: bool = True,
    ) -> dict:
        """Fetch events from a registered event queue.

        Args:
            queue_id: The queue ID returned by register_event_queue.
            last_event_id: The ID of the last event received (-1 for all events).
            dont_block: If True, return immediately even if no new events.
                        If False, long-poll until an event arrives.
        """
        base, auth = _client()
        params = {
            "queue_id": queue_id,
            "last_event_id": last_event_id,
            "dont_block": dont_block,
        }
        try:
            r = requests.get(f"{base}/events", params=params, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_event_queue(queue_id: str) -> dict:
        """Delete (deregister) an event queue.

        Args:
            queue_id: The queue ID to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(
                f"{base}/events", params={"queue_id": queue_id}, auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_server_settings_no_auth() -> dict:
        """Fetch server settings without authentication (useful for login flows)."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/server_settings")
            return r.json()
        except Exception as e:
            return {"error": str(e)}
