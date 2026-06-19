from __future__ import annotations

from zulip_client import ZulipClient


def register(mcp, client: ZulipClient):
    @mcp.tool()
    def zulip_send_message(type: str, to, content: str, topic: str | None = None, queue_id: str | None = None, local_id: str | None = None):
        """Send a message to a stream or as a private message.

        Args:
          type: "stream" or "private".
          to: For stream: stream name or ID. For private: list of recipient emails/user_ids.
          content: Message content.
          topic: Stream topic (required for stream messages).
          queue_id/local_id: Optional for local echo.
        """
        data = {"type": type, "to": to, "content": content}
        if topic is not None:
            data["topic"] = topic
        if queue_id is not None:
            data["queue_id"] = queue_id
        if local_id is not None:
            data["local_id"] = local_id
        return client.request("POST", "/messages", data=data)

    @mcp.tool()
    def zulip_get_messages(anchor: int | str = "newest", num_before: int = 50, num_after: int = 0, narrow=None, client_gravatar: bool | None = None, apply_markdown: bool | None = None, use_first_unread_anchor: bool | None = None):
        """Fetch message history."""
        params = {
            "anchor": anchor,
            "num_before": num_before,
            "num_after": num_after,
        }
        if narrow is not None:
            params["narrow"] = narrow
        if client_gravatar is not None:
            params["client_gravatar"] = client_gravatar
        if apply_markdown is not None:
            params["apply_markdown"] = apply_markdown
        if use_first_unread_anchor is not None:
            params["use_first_unread_anchor"] = use_first_unread_anchor
        return client.request("GET", "/messages", params=params)

    @mcp.tool()
    def zulip_get_message(message_id: int, apply_markdown: bool | None = None):
        """Get a single message by ID."""
        params = {}
        if apply_markdown is not None:
            params["apply_markdown"] = apply_markdown
        return client.request("GET", f"/messages/{message_id}", params=params)

    @mcp.tool()
    def zulip_update_message(message_id: int, content: str | None = None, topic: str | None = None, propagate_mode: str | None = None, send_notification_to_old_thread: bool | None = None, send_notification_to_new_thread: bool | None = None):
        """Edit a message's content and/or topic."""
        data = {}
        if content is not None:
            data["content"] = content
        if topic is not None:
            data["topic"] = topic
        if propagate_mode is not None:
            data["propagate_mode"] = propagate_mode
        if send_notification_to_old_thread is not None:
            data["send_notification_to_old_thread"] = send_notification_to_old_thread
        if send_notification_to_new_thread is not None:
            data["send_notification_to_new_thread"] = send_notification_to_new_thread
        return client.request("PATCH", f"/messages/{message_id}", data=data)

    @mcp.tool()
    def zulip_delete_message(message_id: int):
        """Delete a message."""
        return client.request("DELETE", f"/messages/{message_id}")

    @mcp.tool()
    def zulip_add_reaction(message_id: int, emoji_name: str | None = None, emoji_code: str | None = None, reaction_type: str | None = None):
        """Add a reaction to a message."""
        data = {}
        if emoji_name is not None:
            data["emoji_name"] = emoji_name
        if emoji_code is not None:
            data["emoji_code"] = emoji_code
        if reaction_type is not None:
            data["reaction_type"] = reaction_type
        return client.request("POST", f"/messages/{message_id}/reactions", data=data)

    @mcp.tool()
    def zulip_remove_reaction(message_id: int, emoji_name: str | None = None, emoji_code: str | None = None, reaction_type: str | None = None):
        """Remove a reaction from a message."""
        params = {}
        if emoji_name is not None:
            params["emoji_name"] = emoji_name
        if emoji_code is not None:
            params["emoji_code"] = emoji_code
        if reaction_type is not None:
            params["reaction_type"] = reaction_type
        return client.request("DELETE", f"/messages/{message_id}/reactions", params=params)

    @mcp.tool()
    def zulip_update_message_flags(messages: list[int], op: str, flag: str):
        """Add/remove a flag (e.g. read/starred) on messages."""
        data = {"messages": messages, "op": op, "flag": flag}
        return client.request("POST", "/messages/flags", data=data)

    @mcp.tool()
    def zulip_render_markdown(content: str):
        """Render Zulip-flavored Markdown."""
        return client.request("POST", "/messages/render", data={"content": content})
