from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from zulip_client import ZulipClient

from generated_tools.messages import (
    send_message,
    get_messages,
    update_message,
    delete_message,
    add_reaction,
    remove_reaction,
    update_message_flags,
)
from generated_tools.streams import (
    get_streams,
    create_stream,
    update_stream,
    archive_stream,
    subscribe,
    unsubscribe,
)
from generated_tools.topics import (
    get_topics,
    update_topic,
)
from generated_tools.users import (
    get_own_profile,
    get_user,
    get_users,
    get_presence,
    update_own_status,
)
from generated_tools.scheduled import (
    create_scheduled_message,
    get_scheduled_messages,
    delete_scheduled_message,
)
from generated_tools.drafts import (
    get_drafts,
    create_drafts,
    delete_draft,
)
from generated_tools.files import upload_file


mcp = FastMCP("zulip")


def _client() -> ZulipClient:
    try:
        return ZulipClient()
    except Exception as e:
        # Return a sentinel client-like object? We'll just raise and catch in tools.
        raise e


@mcp.tool()
def zulip_send_message(type: str, content: str, to, topic: str | None = None, queue_id: str | None = None, local_id: str | None = None):
    """Send a message to a stream or via direct message."""
    try:
        return send_message(_client(), type=type, content=content, to=to, topic=topic, queue_id=queue_id, local_id=local_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_messages(anchor="newest", num_before: int = 30, num_after: int = 0, narrow=None, client_gravatar: bool | None = None, apply_markdown: bool | None = None, use_first_unread_anchor: bool | None = None):
    """Fetch message history."""
    try:
        return get_messages(_client(), anchor=anchor, num_before=num_before, num_after=num_after, narrow=narrow, client_gravatar=client_gravatar, apply_markdown=apply_markdown, use_first_unread_anchor=use_first_unread_anchor)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_update_message(message_id: int, content: str | None = None, topic: str | None = None, propagate_mode: str | None = None, send_notification_to_old_thread: bool | None = None, send_notification_to_new_thread: bool | None = None):
    """Edit a message's content and/or topic."""
    try:
        return update_message(_client(), message_id=message_id, content=content, topic=topic, propagate_mode=propagate_mode, send_notification_to_old_thread=send_notification_to_old_thread, send_notification_to_new_thread=send_notification_to_new_thread)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_delete_message(message_id: int):
    """Delete a message."""
    try:
        return delete_message(_client(), message_id=message_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_add_reaction(message_id: int, emoji_name: str | None = None, emoji_code: str | None = None, reaction_type: str | None = None):
    """Add an emoji reaction to a message."""
    try:
        return add_reaction(_client(), message_id=message_id, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_remove_reaction(message_id: int, emoji_name: str | None = None, emoji_code: str | None = None, reaction_type: str | None = None):
    """Remove an emoji reaction from a message."""
    try:
        return remove_reaction(_client(), message_id=message_id, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_update_message_flags(messages: list[int], op: str, flag: str):
    """Add/remove flags (e.g. read/starred) on messages."""
    try:
        return update_message_flags(_client(), messages=messages, op=op, flag=flag)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_streams(include_public: bool = True, include_subscribed: bool = True, include_all_active: bool = False):
    """List streams."""
    try:
        return get_streams(_client(), include_public=include_public, include_subscribed=include_subscribed, include_all_active=include_all_active)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_create_stream(subscriptions, invite_only: bool | None = None, history_public_to_subscribers: bool | None = None):
    """Create stream(s) / subscribe self."""
    try:
        return create_stream(_client(), subscriptions=subscriptions, invite_only=invite_only, history_public_to_subscribers=history_public_to_subscribers)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_update_stream(stream_id: int, description: str | None = None, new_name: str | None = None, is_private: bool | None = None, is_announcement_only: bool | None = None):
    """Update stream settings."""
    try:
        return update_stream(_client(), stream_id=stream_id, description=description, new_name=new_name, is_private=is_private, is_announcement_only=is_announcement_only)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_archive_stream(stream_id: int):
    """Archive (delete) a stream."""
    try:
        return archive_stream(_client(), stream_id=stream_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_subscribe(subscriptions, principals: list[int] | None = None, authorization_errors_fatal: bool | None = None):
    """Subscribe users to streams."""
    try:
        return subscribe(_client(), subscriptions=subscriptions, principals=principals, authorization_errors_fatal=authorization_errors_fatal)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_unsubscribe(subscriptions: list[str], principals: list[int] | None = None):
    """Unsubscribe users from streams."""
    try:
        return unsubscribe(_client(), subscriptions=subscriptions, principals=principals)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_topics(stream_id: int):
    """List topics in a stream."""
    try:
        return get_topics(_client(), stream_id=stream_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_update_topic(stream_id: int, topic: str, new_topic: str, propagate_mode: str | None = None):
    """Rename/move a topic within a stream."""
    try:
        return update_topic(_client(), stream_id=stream_id, topic=topic, new_topic=new_topic, propagate_mode=propagate_mode)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_own_profile():
    """Get the authenticated user's profile."""
    try:
        return get_own_profile(_client())
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_user(user_id: int):
    """Get a user by ID."""
    try:
        return get_user(_client(), user_id=user_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_users(client_gravatar: bool | None = None, include_custom_profile_fields: bool | None = None):
    """List users."""
    try:
        return get_users(_client(), client_gravatar=client_gravatar, include_custom_profile_fields=include_custom_profile_fields)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_presence(user_id_or_email: str):
    """Get presence for a user (by ID or email depending on server config)."""
    try:
        return get_presence(_client(), user_id_or_email=user_id_or_email)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_update_own_status(status_text: str | None = None, away: bool | None = None, emoji_name: str | None = None, emoji_code: str | None = None, reaction_type: str | None = None):
    """Update the authenticated user's status."""
    try:
        return update_own_status(_client(), status_text=status_text, away=away, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_create_scheduled_message(type: str, to, content: str, scheduled_delivery_timestamp: int, topic: str | None = None):
    """Schedule a message for future delivery."""
    try:
        return create_scheduled_message(_client(), type=type, to=to, content=content, scheduled_delivery_timestamp=scheduled_delivery_timestamp, topic=topic)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_scheduled_messages():
    """List scheduled messages."""
    try:
        return get_scheduled_messages(_client())
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_delete_scheduled_message(scheduled_message_id: int):
    """Delete a scheduled message."""
    try:
        return delete_scheduled_message(_client(), scheduled_message_id=scheduled_message_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_get_drafts():
    """List drafts."""
    try:
        return get_drafts(_client())
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_create_drafts(drafts):
    """Create drafts."""
    try:
        return create_drafts(_client(), drafts=drafts)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_delete_draft(draft_id: int):
    """Delete a draft."""
    try:
        return delete_draft(_client(), draft_id=draft_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def zulip_upload_file(file_path: str):
    """Upload a file to Zulip and get a URL."""
    try:
        return upload_file(_client(), file_path=file_path)
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
