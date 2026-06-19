"""
Zulip MCP Tools — Messages domain
Covers: send, fetch, edit, delete, move, history, flags, search
"""
import os, requests
from mcp.server.fastmcp import FastMCP

def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_message_tools(mcp: FastMCP):

    @mcp.tool()
    def send_message(
        type: str,
        to: str,
        content: str,
        topic: str = "",
        queue_id: str = "",
        local_id: str = "",
    ) -> dict:
        """Send a message to a stream or direct message.

        Args:
            type: 'stream' or 'direct'
            to: For stream messages, the stream name or ID. For direct messages,
                a comma-separated list of user email addresses or IDs.
            content: The message content (Markdown supported).
            topic: Required for stream messages; the topic name.
            queue_id: Optional event queue ID for local echo.
            local_id: Optional local message ID for local echo.
        """
        base, auth = _client()
        payload: dict = {"type": type, "to": to, "content": content}
        if topic:
            payload["topic"] = topic
        if queue_id:
            payload["queue_id"] = queue_id
        if local_id:
            payload["local_id"] = local_id
        try:
            r = requests.post(f"{base}/messages", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_messages(
        anchor: str = "newest",
        num_before: int = 100,
        num_after: int = 0,
        narrow: str = "[]",
        client_gravatar: bool = False,
        apply_markdown: bool = True,
        include_anchor: bool = True,
    ) -> dict:
        """Fetch a batch of messages from the message history.

        Args:
            anchor: Message ID to anchor the fetch, or 'newest'/'oldest'/'first_unread'.
            num_before: Number of messages before the anchor (max 5000).
            num_after: Number of messages after the anchor (max 5000).
            narrow: JSON-encoded list of narrow filter objects, e.g.
                    '[{"operator":"stream","operand":"general"}]'.
            client_gravatar: Whether to return gravatar URLs.
            apply_markdown: Whether to render Markdown server-side.
            include_anchor: Whether to include the anchor message in results.
        """
        base, auth = _client()
        params = {
            "anchor": anchor,
            "num_before": num_before,
            "num_after": num_after,
            "narrow": narrow,
            "client_gravatar": client_gravatar,
            "apply_markdown": apply_markdown,
            "include_anchor": include_anchor,
        }
        try:
            r = requests.get(f"{base}/messages", params=params, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_message(message_id: int, apply_markdown: bool = True) -> dict:
        """Fetch a single message by ID.

        Args:
            message_id: The numeric ID of the message.
            apply_markdown: Whether to render Markdown server-side.
        """
        base, auth = _client()
        try:
            r = requests.get(
                f"{base}/messages/{message_id}",
                params={"apply_markdown": apply_markdown},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def edit_message(
        message_id: int,
        content: str = "",
        topic: str = "",
        propagate_mode: str = "change_one",
        send_notification_to_old_thread: bool = True,
        send_notification_to_new_thread: bool = True,
    ) -> dict:
        """Edit the content and/or topic of a message.

        Args:
            message_id: The numeric ID of the message to edit.
            content: New message content (leave blank to keep unchanged).
            topic: New topic name (leave blank to keep unchanged).
            propagate_mode: 'change_one', 'change_later', or 'change_all' —
                            controls which messages get the new topic.
            send_notification_to_old_thread: Notify old thread of the move.
            send_notification_to_new_thread: Notify new thread of the move.
        """
        base, auth = _client()
        payload: dict = {}
        if content:
            payload["content"] = content
        if topic:
            payload["topic"] = topic
            payload["propagate_mode"] = propagate_mode
            payload["send_notification_to_old_thread"] = send_notification_to_old_thread
            payload["send_notification_to_new_thread"] = send_notification_to_new_thread
        try:
            r = requests.patch(f"{base}/messages/{message_id}", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_message(message_id: int) -> dict:
        """Permanently delete a message.

        Args:
            message_id: The numeric ID of the message to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/messages/{message_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def move_message(
        message_id: int,
        stream_id: int,
        topic: str,
        propagate_mode: str = "change_all",
        send_notification_to_old_thread: bool = True,
        send_notification_to_new_thread: bool = True,
    ) -> dict:
        """Move a message (and optionally its thread) to a different stream/topic.

        Args:
            message_id: The numeric ID of the message to move.
            stream_id: Destination stream ID.
            topic: Destination topic name.
            propagate_mode: 'change_one', 'change_later', or 'change_all'.
            send_notification_to_old_thread: Post a notification in the old thread.
            send_notification_to_new_thread: Post a notification in the new thread.
        """
        base, auth = _client()
        payload = {
            "stream_id": stream_id,
            "topic": topic,
            "propagate_mode": propagate_mode,
            "send_notification_to_old_thread": send_notification_to_old_thread,
            "send_notification_to_new_thread": send_notification_to_new_thread,
        }
        try:
            r = requests.patch(f"{base}/messages/{message_id}", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_message_history(message_id: int) -> dict:
        """Retrieve the edit history of a message.

        Args:
            message_id: The numeric ID of the message.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/messages/{message_id}/history", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def add_message_flag(messages: str, flag: str) -> dict:
        """Add a flag (e.g. 'read', 'starred') to a list of messages.

        Args:
            messages: JSON-encoded list of message IDs, e.g. '[1, 2, 3]'.
            flag: The flag to add ('read', 'starred', 'collapsed', 'mentioned', etc.).
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/messages/flags",
                data={"messages": messages, "flag": flag, "op": "add"},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_message_flag(messages: str, flag: str) -> dict:
        """Remove a flag (e.g. 'read', 'starred') from a list of messages.

        Args:
            messages: JSON-encoded list of message IDs, e.g. '[1, 2, 3]'.
            flag: The flag to remove ('read', 'starred', 'collapsed', etc.).
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/messages/flags",
                data={"messages": messages, "flag": flag, "op": "remove"},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mark_all_as_read() -> dict:
        """Mark all messages in the organisation as read for the current user."""
        base, auth = _client()
        try:
            r = requests.post(f"{base}/mark_all_as_read", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mark_stream_as_read(stream_id: int) -> dict:
        """Mark all messages in a stream as read.

        Args:
            stream_id: The numeric ID of the stream.
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/mark_stream_as_read",
                data={"stream_id": stream_id},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mark_topic_as_read(stream_id: int, topic_name: str) -> dict:
        """Mark all messages in a topic as read.

        Args:
            stream_id: The numeric ID of the stream.
            topic_name: The name of the topic.
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/mark_topic_as_read",
                data={"stream_id": stream_id, "topic_name": topic_name},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_raw_message(message_id: int) -> dict:
        """Fetch the raw (un-rendered) Markdown source of a message.

        Args:
            message_id: The numeric ID of the message.
        """
        base, auth = _client()
        try:
            r = requests.get(
                f"{base}/messages/{message_id}",
                params={"apply_markdown": False},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def render_message(content: str) -> dict:
        """Render a Markdown string to HTML without sending it.

        Args:
            content: The Markdown content to render.
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/messages/render",
                data={"content": content},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_message_flags_for_narrow(
        anchor: str,
        num_before: int,
        num_after: int,
        narrow: str,
        op: str,
        flag: str,
        include_anchor: bool = True,
    ) -> dict:
        """Bulk-update message flags using a narrow filter.

        Args:
            anchor: Message ID anchor or 'newest'/'oldest'/'first_unread'.
            num_before: Number of messages before anchor.
            num_after: Number of messages after anchor.
            narrow: JSON-encoded narrow filter list.
            op: 'add' or 'remove'.
            flag: The flag to update ('read', 'starred', etc.).
            include_anchor: Whether to include the anchor message.
        """
        base, auth = _client()
        payload = {
            "anchor": anchor,
            "num_before": num_before,
            "num_after": num_after,
            "narrow": narrow,
            "op": op,
            "flag": flag,
            "include_anchor": include_anchor,
        }
        try:
            r = requests.post(f"{base}/messages/flags/narrow", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}
