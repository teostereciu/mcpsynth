"""
Zulip MCP Tools — Topics domain
Covers: list, rename, resolve/unresolve, delete
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_topic_tools(mcp: FastMCP):

    @mcp.tool()
    def get_topics(stream_id: int) -> dict:
        """List all topics in a stream.

        Args:
            stream_id: The numeric ID of the stream.
        """
        base, auth = _client()
        try:
            r = requests.get(f"{base}/users/me/{stream_id}/topics", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def rename_topic(
        stream_id: int,
        current_topic: str,
        new_topic: str,
        propagate_mode: str = "change_all",
        send_notification_to_old_thread: bool = True,
        send_notification_to_new_thread: bool = True,
    ) -> dict:
        """Rename a topic within a stream (moves all messages to the new topic name).

        Args:
            stream_id: The numeric ID of the stream.
            current_topic: The current topic name.
            new_topic: The new topic name.
            propagate_mode: 'change_one', 'change_later', or 'change_all'.
            send_notification_to_old_thread: Post a notification in the old topic.
            send_notification_to_new_thread: Post a notification in the new topic.
        """
        base, auth = _client()
        # Fetch the first message in the topic to get a message_id anchor
        try:
            search = requests.get(
                f"{base}/messages",
                params={
                    "anchor": "oldest",
                    "num_before": 0,
                    "num_after": 1,
                    "narrow": f'[{{"operator":"stream","operand":{stream_id}}},{{"operator":"topic","operand":"{current_topic}"}}]',
                    "apply_markdown": False,
                },
                auth=auth,
            )
            data = search.json()
            msgs = data.get("messages", [])
            if not msgs:
                return {"error": "No messages found in that topic."}
            message_id = msgs[0]["id"]
            r = requests.patch(
                f"{base}/messages/{message_id}",
                data={
                    "topic": new_topic,
                    "stream_id": stream_id,
                    "propagate_mode": propagate_mode,
                    "send_notification_to_old_thread": send_notification_to_old_thread,
                    "send_notification_to_new_thread": send_notification_to_new_thread,
                },
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def resolve_topic(stream_id: int, topic_name: str) -> dict:
        """Mark a topic as resolved by prepending '✔ ' to its name.

        Args:
            stream_id: The numeric ID of the stream.
            topic_name: The current topic name (without the resolved prefix).
        """
        base, auth = _client()
        resolved_name = f"✔ {topic_name}"
        try:
            search = requests.get(
                f"{base}/messages",
                params={
                    "anchor": "oldest",
                    "num_before": 0,
                    "num_after": 1,
                    "narrow": f'[{{"operator":"stream","operand":{stream_id}}},{{"operator":"topic","operand":"{topic_name}"}}]',
                    "apply_markdown": False,
                },
                auth=auth,
            )
            data = search.json()
            msgs = data.get("messages", [])
            if not msgs:
                return {"error": "No messages found in that topic."}
            message_id = msgs[0]["id"]
            r = requests.patch(
                f"{base}/messages/{message_id}",
                data={
                    "topic": resolved_name,
                    "propagate_mode": "change_all",
                    "send_notification_to_old_thread": True,
                    "send_notification_to_new_thread": True,
                },
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unresolve_topic(stream_id: int, topic_name: str) -> dict:
        """Mark a resolved topic as unresolved by removing the '✔ ' prefix.

        Args:
            stream_id: The numeric ID of the stream.
            topic_name: The current topic name (including the '✔ ' prefix).
        """
        base, auth = _client()
        unresolved_name = topic_name.lstrip("✔ ").strip()
        try:
            search = requests.get(
                f"{base}/messages",
                params={
                    "anchor": "oldest",
                    "num_before": 0,
                    "num_after": 1,
                    "narrow": f'[{{"operator":"stream","operand":{stream_id}}},{{"operator":"topic","operand":"{topic_name}"}}]',
                    "apply_markdown": False,
                },
                auth=auth,
            )
            data = search.json()
            msgs = data.get("messages", [])
            if not msgs:
                return {"error": "No messages found in that topic."}
            message_id = msgs[0]["id"]
            r = requests.patch(
                f"{base}/messages/{message_id}",
                data={
                    "topic": unresolved_name,
                    "propagate_mode": "change_all",
                    "send_notification_to_old_thread": True,
                    "send_notification_to_new_thread": True,
                },
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_topic(stream_id: int, topic_name: str) -> dict:
        """Delete all messages in a topic (effectively deleting the topic).

        Args:
            stream_id: The numeric ID of the stream.
            topic_name: The name of the topic to delete.
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/streams/{stream_id}/delete_topic",
                data={"topic_name": topic_name},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}
