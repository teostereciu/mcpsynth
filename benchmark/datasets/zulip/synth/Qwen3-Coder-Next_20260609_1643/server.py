#!/usr/bin/env python3
"""Zulip MCP Server - A Model Context Protocol server for Zulip REST API."""

import os
import json
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

# Environment variables
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

if not all([ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE]):
    raise ValueError("ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set")

# Base URL for Zulip API
BASE_URL = f"{ZULIP_SITE.rstrip('/')}/api/v1"

# Create MCP server
mcp = FastMCP("zulip")

# Helper function to make HTTP requests to Zulip API
def zulip_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Make a request to the Zulip API."""
    url = f"{BASE_URL}{endpoint}"
    auth = (ZULIP_EMAIL, ZULIP_API_KEY)
    
    try:
        if method.upper() in ["GET", "DELETE"]:
            response = requests.request(method, url, params=params, auth=auth)
        else:
            response = requests.request(method, url, json=data, params=params, auth=auth)
        
        # Parse JSON response or return text for non-JSON
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"raw_response": response.text}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# ============================================================================
# Messages endpoints
# ============================================================================

@mcp.tool()
def send_message(
    message_type: str,
    to: str | List[int] | List[str],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """Send a stream or direct message.
    
    Args:
        message_type: Must be one of: "direct", "channel", "stream", "private"
        to: For channel messages, either the name or integer ID of the channel. 
            For direct messages, either a list containing integer user IDs or 
            a list containing string Zulip API email addresses.
        content: The content of the message.
        topic: The topic of the message. Only required for channel messages.
        queue_id: Event queue ID for clients supporting local echo.
        local_id: Unique string-format identifier for local echo.
        read_by_sender: Whether the message should be initially marked read by its sender.
    """
    data = {
        "type": message_type,
        "to": json.dumps(to) if isinstance(to, list) else to,
        "content": content,
    }
    
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = str(read_by_sender)
    
    return zulip_request("POST", "/messages", data=data)


@mcp.tool()
def get_messages(
    anchor: str | int = "newest",
    num_before: int = 100,
    num_after: int = 0,
    narrow: Optional[List[Dict[str, Any]]] = None,
    client_gravatar: Optional[bool] = True,
    apply_markdown: Optional[bool] = True,
    message_ids: Optional[List[int]] = None,
    allow_empty_topic_name: Optional[bool] = False,
) -> Dict[str, Any]:
    """Get messages matching a narrow filter.
    
    Args:
        anchor: Integer message ID or special string value ("newest", "oldest", "first_unread", "date").
        num_before: Number of messages with IDs less than the anchor to retrieve.
        num_after: Number of messages with IDs greater than the anchor to retrieve.
        narrow: List of narrow objects to filter messages.
        client_gravatar: Whether the client supports computing gravatars URLs.
        apply_markdown: If true, message content is returned in HTML format.
        message_ids: A list of message IDs to fetch (alternative to anchor-based range).
        allow_empty_topic_name: Whether the client supports empty string topics.
    """
    params = {
        "anchor": str(anchor) if not isinstance(anchor, int) else anchor,
        "num_before": num_before,
        "num_after": num_after,
    }
    
    if narrow is not None:
        params["narrow"] = json.dumps(narrow)
    if client_gravatar is not None:
        params["client_gravatar"] = str(client_gravatar)
    if apply_markdown is not None:
        params["apply_markdown"] = str(apply_markdown)
    if message_ids is not None:
        params["message_ids"] = json.dumps(message_ids)
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = str(allow_empty_topic_name)
    
    return zulip_request("GET", "/messages", params=params)


@mcp.tool()
def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    prev_content_sha256: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> Dict[str, Any]:
    """Update the content, topic, or channel of a message.
    
    Args:
        message_id: The target message's ID.
        content: The updated content of the message.
        topic: The topic to move the message(s) to.
        propagate_mode: Which messages should be edited: "change_one", "change_later", "change_all".
        send_notification_to_old_thread: Whether to send an automated message to the old topic.
        send_notification_to_new_thread: Whether to send an automated message to the new topic.
        prev_content_sha256: SHA-256 hash of the previous raw content.
        stream_id: The channel ID to move the message(s) to.
    """
    data = {"message_id": message_id}
    
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = str(send_notification_to_old_thread)
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = str(send_notification_to_new_thread)
    if prev_content_sha256 is not None:
        data["prev_content_sha256"] = prev_content_sha256
    if stream_id is not None:
        data["stream_id"] = stream_id
    
    return zulip_request("PATCH", f"/messages/{message_id}", data=data)


@mcp.tool()
def delete_message(message_id: int) -> Dict[str, Any]:
    """Permanently delete a message.
    
    Args:
        message_id: The target message's ID.
    """
    return zulip_request("DELETE", f"/messages/{message_id}")


@mcp.tool()
def get_message(message_id: int) -> Dict[str, Any]:
    """Fetch a single message by ID.
    
    Args:
        message_id: The target message's ID.
    """
    return zulip_request("GET", f"/messages/{message_id}")


@mcp.tool()
def add_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: Optional[str] = "unicode_emoji") -> Dict[str, Any]:
    """Add an emoji reaction to a message.
    
    Args:
        message_id: The ID of the message to add the reaction to.
        emoji_name: The name of the emoji (e.g., "grinning").
        emoji_code: The emoji code, required for custom emojis.
        reaction_type: One of "unicode_emoji", "realm_emoji", "emoji_code".
    """
    data = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type,
    }
    
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    
    return zulip_request("POST", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: Optional[str] = "unicode_emoji") -> Dict[str, Any]:
    """Remove an emoji reaction from a message.
    
    Args:
        message_id: The ID of the message to remove the reaction from.
        emoji_name: The name of the emoji.
        emoji_code: The emoji code, required for custom emojis.
        reaction_type: One of "unicode_emoji", "realm_emoji", "emoji_code".
    """
    data = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type,
    }
    
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    
    return zulip_request("DELETE", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def update_message_flags(
    flag: str,
    messages: List[int],
    state: bool = True,
) -> Dict[str, Any]:
    """Update personal message flags.
    
    Args:
        flag: The flag to update (e.g., "read", "starred", "collapsed", "mentioned", "wildcard_mentioned", "has_alert_word", "active_all).
        messages: List of message IDs to update.
        state: Whether to add (true) or remove (false) the flag.
    """
    data = {
        "messages": json.dumps(messages),
        "flag": flag,
        "state": str(state).lower(),
    }
    
    return zulip_request("POST", "/messages/flags", data=data)


@mcp.tool()
def update_message_flags_for_narrow(
    flag: str,
    narrow: List[Dict[str, Any]],
    state: bool = True,
) -> Dict[str, Any]:
    """Update personal message flags for messages matching a narrow.
    
    Args:
        flag: The flag to update.
        narrow: The narrow filter to select messages.
        state: Whether to add (true) or remove (false) the flag.
    """
    data = {
        "narrow": json.dumps(narrow),
        "flag": flag,
        "state": str(state).lower(),
    }
    
    return zulip_request("POST", "/messages/flags/narrow", data=data)


@mcp.tool()
def mark_all_as_read() -> Dict[str, Any]:
    """Mark all messages as read."""
    return zulip_request("POST", "/mark_all_as_read")


@mcp.tool()
def mark_stream_as_read(stream_id: int) -> Dict[str, Any]:
    """Mark all messages in a stream as read.
    
    Args:
        stream_id: The ID of the stream.
    """
    data = {"stream_id": stream_id}
    return zulip_request("POST", "/mark_stream_as_read", data=data)


@mcp.tool()
def mark_topic_as_read(stream_id: int, topic: str) -> Dict[str, Any]:
    """Mark all messages in a topic as read.
    
    Args:
        stream_id: The ID of the stream.
        topic: The topic name.
    """
    data = {
        "stream_id": stream_id,
        "topic": topic,
    }
    return zulip_request("POST", "/mark_topic_as_read", data=data)


@mcp.tool()
def render_message(content: str) -> Dict[str, Any]:
    """Render message content to HTML.
    
    Args:
        content: The message content to render.
    """
    data = {"content": content}
    return zulip_request("POST", "/render_message", data=data)


@mcp.tool()
def get_message_history(message_id: int) -> Dict[str, Any]:
    """Get the edit history for a message.
    
    Args:
        message_id: The ID of the message.
    """
    return zulip_request("GET", f"/messages/{message_id}/history")


@mcp.tool()
def construct_narrow(
    operators: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Construct a narrow filter.
    
    Args:
        operators: List of narrow operator objects.
    """
    return operators


@mcp.tool()
def check_messages_match_narrow(
    narrow: List[Dict[str, Any]],
    start: int,
    end: int,
) -> Dict[str, Any]:
    """Check whether messages match a narrow filter.
    
    Args:
        narrow: The narrow filter to check.
        start: Start message ID range.
        end: End message ID range.
    """
    data = {
        "narrow": json.dumps(narrow),
        "start": start,
        "end": end,
    }
    return zulip_request("GET", "/messages/matches_narrow", params=data)


@mcp.tool()
def get_read_receipts(message_id: int) -> Dict[str, Any]:
    """Get the read receipts for a message.
    
    Args:
        message_id: The ID of the message.
    """
    return zulip_request("GET", f"/messages/{message_id}/read_receipts")


@mcp.tool()
def report_message(
    message_id: int,
    reason: Optional[str] = None,
    stream_id: Optional[int] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """Report a message to administrators.
    
    Args:
        message_id: The ID of the message to report.
        reason: A string explaining why the message is being reported.
        stream_id: The ID of the channel where the message was sent.
        topic: The topic of the message.
    """
    data = {"message_id": message_id}
    
    if reason is not None:
        data["reason"] = reason
    if stream_id is not None:
        data["stream_id"] = stream_id
    if topic is not None:
        data["topic"] = topic
    
    return zulip_request("POST", "/reports", data=data)


# ============================================================================
# Scheduled messages endpoints
# ============================================================================

@mcp.tool()
def create_scheduled_message(
    delivery_type: str,
    to: List[int] | List[str] | str,
    content: str,
    topic: Optional[str] = None,
    schedule_for: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a scheduled message.
    
    Args:
        delivery_type: Either "send_later" or "repeat".
        to: For channel messages, the channel name or ID. For direct messages, list of user IDs or emails.
        content: The content of the message.
        topic: The topic of the message (required for channel messages).
        schedule_for: ISO 8601 timestamp for when to send the message.
    """
    data = {
        "type": "stream" if isinstance(to, str) else "direct",
        "to": json.dumps(to) if isinstance(to, list) else to,
        "content": content,
        "delivery_type": delivery_type,
    }
    
    if topic is not None:
        data["topic"] = topic
    if schedule_for is not None:
        data["schedule_for"] = schedule_for
    
    return zulip_request("POST", "/scheduled_messages", data=data)


@mcp.tool()
def get_scheduled_messages() -> Dict[str, Any]:
    """Get all scheduled messages."""
    return zulip_request("GET", "/scheduled_messages")


@mcp.tool()
def update_scheduled_message(
    scheduled_message_id: int,
    delivery_type: Optional[str] = None,
    to: Optional[List[int] | List[str] | str] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    schedule_for: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a scheduled message.
    
    Args:
        scheduled_message_id: The ID of the scheduled message to update.
        delivery_type: Either "send_later" or "repeat".
        to: For channel messages, the channel name or ID. For direct messages, list of user IDs or emails.
        content: The new content of the message.
        topic: The new topic of the message.
        schedule_for: New ISO 8601 timestamp for when to send the message.
    """
    data = {}
    
    if delivery_type is not None:
        data["delivery_type"] = delivery_type
    if to is not None:
        data["to"] = json.dumps(to) if isinstance(to, list) else to
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if schedule_for is not None:
        data["schedule_for"] = schedule_for
    
    return zulip_request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


@mcp.tool()
def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """Delete a scheduled message.
    
    Args:
        scheduled_message_id: The ID of the scheduled message to delete.
    """
    return zulip_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")


# ============================================================================
# Message reminders endpoints
# ============================================================================

@mcp.tool()
def create_reminder(
    message: str,
    delivery_type: str,
    to: List[int] | List[str] | str,
    topic: Optional[str] = None,
    schedule_for: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a message reminder.
    
    Args:
        message: The message content.
        delivery_type: Either "send_later" or "repeat".
        to: For channel messages, the channel name or ID. For direct messages, list of user IDs or emails.
        topic: The topic of the message (required for channel messages).
        schedule_for: ISO 8601 timestamp for when to send the reminder.
    """
    data = {
        "type": "stream" if isinstance(to, str) else "direct",
        "to": json.dumps(to) if isinstance(to, list) else to,
        "content": message,
        "delivery_type": delivery_type,
    }
    
    if topic is not None:
        data["topic"] = topic
    if schedule_for is not None:
        data["schedule_for"] = schedule_for
    
    return zulip_request("POST", "/reminders", data=data)


@mcp.tool()
def get_reminders() -> Dict[str, Any]:
    """Get all message reminders."""
    return zulip_request("GET", "/reminders")


@mcp.tool()
def delete_reminder(reminder_id: int) -> Dict[str, Any]:
    """Delete a message reminder.
    
    Args:
        reminder_id: The ID of the reminder to delete.
    """
    return zulip_request("DELETE", f"/reminders/{reminder_id}")


# ============================================================================
# Drafts endpoints
# ============================================================================

@mcp.tool()
def get_drafts() -> Dict[str, Any]:
    """Get all drafts for the current user."""
    return zulip_request("GET", "/drafts")


@mcp.tool()
def create_drafts(
    drafts: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Create new drafts.
    
    Args:
        drafts: List of draft objects with type, to, subject (optional), and content.
    """
    data = {"drafts": json.dumps(drafts)}
    return zulip_request("POST", "/drafts", data=data)


@mcp.tool()
def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    """Edit an existing draft.
    
    Args:
        draft_id: The ID of the draft to edit.
        draft: Draft object with updated fields.
    """
    return zulip_request("PATCH", f"/drafts/{draft_id}", data=draft)


@mcp.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    """Delete a draft.
    
    Args:
        draft_id: The ID of the draft to delete.
    """
    return zulip_request("DELETE", f"/drafts/{draft_id}")


# ============================================================================
# Streams endpoints
# ============================================================================

@mcp.tool()
def subscribe(
    subscriptions: List[Dict[str, Any]],
    principals: Optional[List[int] | List[str]] = None,
    authorization_errors_fatal: Optional[bool] = True,
    announce: Optional[bool] = False,
    invite_only: Optional[bool] = False,
    is_web_public: Optional[bool] = False,
    is_default_stream: Optional[bool] = False,
    history_public_to_subscribers: Optional[bool] = None,
    message_retention_days: Optional[int | str] = None,
    topics_policy: Optional[str] = None,
    can_add_subscribers_group: Optional[int | Dict[str, Any]] = None,
    can_remove_subscribers_group: Optional[int | Dict[str, Any]] = None,
    can_administer_channel_group: Optional[int | Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Subscribe users to channels.
    
    Args:
        subscriptions: List of channel dictionaries with name and optional description.
        principals: List of user IDs or emails to subscribe (defaults to current user).
        authorization_errors_fatal: Whether authorization errors should be fatal.
        announce: Whether to send an announcement for new channels.
        invite_only: Whether new channels should be private.
        is_web_public: Whether new channels should be web-public.
        is_default_stream: Whether new channels should be default channels.
        history_public_to_subscribers: Whether message history is available to new members.
        message_retention_days: Number of days to retain messages.
        topics_policy: Topic policy for the channel.
        can_add_subscribers_group: Group with permission to add subscribers.
        can_remove_subscribers_group: Group with permission to remove subscribers.
        can_administer_channel_group: Group with permission to administer the channel.
    """
    data = {"subscriptions": json.dumps(subscriptions)}
    
    if principals is not None:
        data["principals"] = json.dumps(principals)
    if authorization_errors_fatal is not None:
        data["authorization_errors_fatal"] = str(authorization_errors_fatal)
    if announce is not None:
        data["announce"] = str(announce)
    if invite_only is not None:
        data["invite_only"] = str(invite_only)
    if is_web_public is not None:
        data["is_web_public"] = str(is_web_public)
    if is_default_stream is not None:
        data["is_default_stream"] = str(is_default_stream)
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = str(history_public_to_subscribers)
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    if topics_policy is not None:
        data["topics_policy"] = topics_policy
    if can_add_subscribers_group is not None:
        data["can_add_subscribers_group"] = json.dumps(can_add_subscribers_group) if isinstance(can_add_subscribers_group, dict) else can_add_subscribers_group
    if can_remove_subscribers_group is not None:
        data["can_remove_subscribers_group"] = json.dumps(can_remove_subscribers_group) if isinstance(can_remove_subscribers_group, dict) else can_remove_subscribers_group
    if can_administer_channel_group is not None:
        data["can_administer_channel_group"] = json.dumps(can_administer_channel_group) if isinstance(can_administer_channel_group, dict) else can_administer_channel_group
    
    return zulip_request("POST", "/users/me/subscriptions", data=data)


@mcp.tool()
def unsubscribe(
    subscriptions: List[Dict[str, Any]],
    principals: Optional[List[int] | List[str]] = None,
) -> Dict[str, Any]:
    """Unsubscribe users from channels.
    
    Args:
        subscriptions: List of channel dictionaries with name.
        principals: List of user IDs or emails to unsubscribe (defaults to current user).
    """
    data = {"subscriptions": json.dumps(subscriptions)}
    
    if principals is not None:
        data["principals"] = json.dumps(principals)
    
    return zulip_request("POST", "/users/me/subscriptions/delete", data=data)


@mcp.tool()
def get_subscriptions() -> Dict[str, Any]:
    """Get all channels the current user is subscribed to."""
    return zulip_request("GET", "/users/me/subscriptions")


@mcp.tool()
def get_subscriptions_for_user(user_id: int) -> Dict[str, Any]:
    """Get all channels a user is subscribed to.
    
    Args:
        user_id: The ID of the user.
    """
    return zulip_request("GET", f"/users/{user_id}/subscriptions")


@mcp.tool()
def get_subscriber_status(stream_id: int, user_id: Optional[int] = None) -> Dict[str, Any]:
    """Get subscription status for a user in a stream.
    
    Args:
        stream_id: The ID of the stream.
        user_id: The ID of the user (defaults to current user).
    """
    params = {}
    if user_id is not None:
        params["user_id"] = user_id
    
    return zulip_request("GET", f"/users/me/subscriptions/{stream_id}", params=params)


@mcp.tool()
def get_subscribers(stream_id: int) -> Dict[str, Any]:
    """Get subscribers for a stream.
    
    Args:
        stream_id: The ID of the stream.
    """
    return zulip_request("GET", f"/streams/{stream_id}/members")


@mcp.tool()
def create_stream(
    name: str,
    description: Optional[str] = None,
    invite_only: Optional[bool] = False,
    is_web_public: Optional[bool] = False,
    is_default_stream: Optional[bool] = False,
    history_public_to_subscribers: Optional[bool] = None,
    message_retention_days: Optional[int | str] = None,
    topics_policy: Optional[str] = None,
    can_add_subscribers_group: Optional[int | Dict[str, Any]] = None,
    can_remove_subscribers_group: Optional[int | Dict[str, Any]] = None,
    can_administer_channel_group: Optional[int | Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a new channel.
    
    Args:
        name: The name of the channel.
        description: The description of the channel.
        invite_only: Whether the channel should be private.
        is_web_public: Whether the channel should be web-public.
        is_default_stream: Whether the channel should be a default channel.
        history_public_to_subscribers: Whether message history is available to new members.
        message_retention_days: Number of days to retain messages.
        topics_policy: Topic policy for the channel.
        can_add_subscribers_group: Group with permission to add subscribers.
        can_remove_subscribers_group: Group with permission to remove subscribers.
        can_administer_channel_group: Group with permission to administer the channel.
    """
    data = {"name": name}
    
    if description is not None:
        data["description"] = description
    if invite_only is not None:
        data["invite_only"] = str(invite_only)
    if is_web_public is not None:
        data["is_web_public"] = str(is_web_public)
    if is_default_stream is not None:
        data["is_default_stream"] = str(is_default_stream)
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = str(history_public_to_subscribers)
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    if topics_policy is not None:
        data["topics_policy"] = topics_policy
    if can_add_subscribers_group is not None:
        data["can_add_subscribers_group"] = json.dumps(can_add_subscribers_group) if isinstance(can_add_subscribers_group, dict) else can_add_subscribers_group
    if can_remove_subscribers_group is not None:
        data["can_remove_subscribers_group"] = json.dumps(can_remove_subscribers_group) if isinstance(can_remove_subscribers_group, dict) else can_remove_subscribers_group
    if can_administer_channel_group is not None:
        data["can_administer_channel_group"] = json.dumps(can_administer_channel_group) if isinstance(can_administer_channel_group, dict) else can_administer_channel_group
    
    return zulip_request("POST", "/streams", data=data)


@mcp.tool()
def get_streams() -> Dict[str, Any]:
    """Get all channels in the organization."""
    return zulip_request("GET", "/streams")


@mcp.tool()
def get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    """Get a channel by ID.
    
    Args:
        stream_id: The ID of the channel.
    """
    return zulip_request("GET", f"/streams/{stream_id}")


@mcp.tool()
def get_stream_id(stream_name: str) -> Dict[str, Any]:
    """Get a channel's ID by name.
    
    Args:
        stream_name: The name of the channel.
    """
    return zulip_request("GET", f"/streams/{stream_name}/stream_id")


@mcp.tool()
def update_stream(
    stream_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    invite_only: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    message_retention_days: Optional[int | str] = None,
    topics_policy: Optional[str] = None,
    can_add_subscribers_group: Optional[int | Dict[str, Any]] = None,
    can_remove_subscribers_group: Optional[int | Dict[str, Any]] = None,
    can_administer_channel_group: Optional[int | Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Update a channel's settings.
    
    Args:
        stream_id: The ID of the channel.
        name: New channel name.
        description: New channel description.
        invite_only: Whether the channel should be private.
        is_web_public: Whether the channel should be web-public.
        is_default_stream: Whether the channel should be a default channel.
        history_public_to_subscribers: Whether message history is available to new members.
        message_retention_days: Number of days to retain messages.
        topics_policy: Topic policy for the channel.
        can_add_subscribers_group: Group with permission to add subscribers.
        can_remove_subscribers_group: Group with permission to remove subscribers.
        can_administer_channel_group: Group with permission to administer the channel.
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if invite_only is not None:
        data["invite_only"] = str(invite_only)
    if is_web_public is not None:
        data["is_web_public"] = str(is_web_public)
    if is_default_stream is not None:
        data["is_default_stream"] = str(is_default_stream)
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = str(history_public_to_subscribers)
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    if topics_policy is not None:
        data["topics_policy"] = topics_policy
    if can_add_subscribers_group is not None:
        data["can_add_subscribers_group"] = json.dumps(can_add_subscribers_group) if isinstance(can_add_subscribers_group, dict) else can_add_subscribers_group
    if can_remove_subscribers_group is not None:
        data["can_remove_subscribers_group"] = json.dumps(can_remove_subscribers_group) if isinstance(can_remove_subscribers_group, dict) else can_remove_subscribers_group
    if can_administer_channel_group is not None:
        data["can_administer_channel_group"] = json.dumps(can_administer_channel_group) if isinstance(can_administer_channel_group, dict) else can_administer_channel_group
    
    return zulip_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    """Archive a channel (deletes it).
    
    Args:
        stream_id: The ID of the channel to archive.
    """
    return zulip_request("DELETE", f"/streams/{stream_id}")


@mcp.tool()
def get_topics(stream_id: int) -> Dict[str, Any]:
    """Get all topics in a stream.
    
    Args:
        stream_id: The ID of the stream.
    """
    return zulip_request("GET", f"/streams/{stream_id}/topics")


@mcp.tool()
def update_topic(
    stream_id: int,
    message_id: int,
    topic_name: str,
    propagate_mode: Optional[str] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    send_notification_to_old_thread: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update the topic of messages in a stream.
    
    Args:
        stream_id: The ID of the stream.
        message_id: The ID of the message to update.
        topic_name: New topic name.
        propagate_mode: How many messages to update ("change_one", "change_later", "change_all").
        send_notification_to_new_thread: Whether to send notification to new thread.
        send_notification_to_old_thread: Whether to send notification to old thread.
    """
    data = {
        "stream_id": stream_id,
        "message_id": message_id,
        "topic_name": topic_name,
    }
    
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = str(send_notification_to_new_thread)
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = str(send_notification_to_old_thread)
    
    return zulip_request("PATCH", "/messages/property/topic", data=data)


@mcp.tool()
def delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """Delete a topic (delete all messages in it).
    
    Args:
        stream_id: The ID of the stream.
        topic_name: The topic name to delete.
    """
    data = {
        "stream_id": stream_id,
        "topic_name": topic_name,
    }
    return zulip_request("DELETE", "/topics", data=data)


@mcp.tool()
def mute_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """Mute a topic.
    
    Args:
        stream_id: The ID of the stream.
        topic_name: The topic name to mute.
    """
    data = {
        "stream_id": stream_id,
        "topic_name": topic_name,
    }
    return zulip_request("POST", "/users/me/subscriptions/muted_topics", data=data)


@mcp.tool()
def unmute_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """Unmute a topic.
    
    Args:
        stream_id: The ID of the stream.
        topic_name: The topic name to unmute.
    """
    data = {
        "stream_id": stream_id,
        "topic_name": topic_name,
    }
    return zulip_request("DELETE", "/users/me/subscriptions/muted_topics", data=data)


@mcp.tool()
def update_topic_preferences(
    stream_id: int,
    topic_name: str,
    push_notification_enabled: Optional[bool] = None,
    audible_notifications: Optional[bool] = None,
    pin_enabled: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update personal preferences for a topic.
    
    Args:
        stream_id: The ID of the stream.
        topic_name: The topic name.
        push_notification_enabled: Whether push notifications are enabled.
        audible_notifications: Whether audible notifications are enabled.
        pin_enabled: Whether pinning is enabled.
    """
    data = {
        "stream_id": stream_id,
        "topic_name": topic_name,
    }
    
    if push_notification_enabled is not None:
        data["push_notification_enabled"] = str(push_notification_enabled)
    if audible_notifications is not None:
        data["audible_notifications"] = str(audible_notifications)
    if pin_enabled is not None:
        data["pin_enabled"] = str(pin_enabled)
    
    return zulip_request("PATCH", "/users/me/subscriptions/muted_topics", data=data)


@mcp.tool()
def add_default_stream(stream_id: int) -> Dict[str, Any]:
    """Add a stream as a default channel.
    
    Args:
        stream_id: The ID of the stream.
    """
    data = {"stream_id": stream_id}
    return zulip_request("POST", "/default_streams", data=data)


@mcp.tool()
def remove_default_stream(stream_id: int) -> Dict[str, Any]:
    """Remove a stream from default channels.
    
    Args:
        stream_id: The ID of the stream.
    """
    data = {"stream_id": stream_id}
    return zulip_request("DELETE", "/default_streams", data=data)


@mcp.tool()
def get_default_streams() -> Dict[str, Any]:
    """Get all default channels."""
    return zulip_request("GET", "/default_streams")


# ============================================================================
# User endpoints
# ============================================================================

@mcp.tool()
def get_user(user_id: int) -> Dict[str, Any]:
    """Get a user by ID.
    
    Args:
        user_id: The ID of the user.
    """
    return zulip_request("GET", f"/users/{user_id}")


@mcp.tool()
def get_user_by_email(email: str) -> Dict[str, Any]:
    """Get a user by email address.
    
    Args:
        email: The email address of the user.
    """
    return zulip_request("GET", f"/users/{email}")


@mcp.tool()
def get_own_user() -> Dict[str, Any]:
    """Get the current user's profile."""
    return zulip_request("GET", "/users/me")


@mcp.tool()
def get_users() -> Dict[str, Any]:
    """Get all users in the organization."""
    return zulip_request("GET", "/users")


@mcp.tool()
def get_users_for_role(role_id: int) -> Dict[str, Any]:
    """Get users with a specific role.
    
    Args:
        role_id: Role ID (100: Realm admin, 200: Realm moderator, 300: Full member, 400: Member, 600: Guest).
    """
    return zulip_request("GET", f"/users/{role_id}")


@mcp.tool()
def create_user(
    email: str,
    full_name: str,
    password: Optional[str] = None,
    short_name: Optional[str] = None,
    avatar_source: Optional[str] = None,
    default_language: Optional[str] = None,
    timezone: Optional[str] = None,
    role: Optional[int] = None,
    bot_type: Optional[int] = None,
    bot_owner_id: Optional[int] = None,
    service_url: Optional[str] = None,
    extra_base_payload: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a new user.
    
    Args:
        email: The email address for the new user.
        full_name: The full name for the new user.
        password: Password for the new user (required for regular users).
        short_name: The short/username for the new user.
        avatar_source: Source for user's avatar.
        default_language: Default language for the user.
        timezone: Default timezone for the user.
        role: Role for the user (100: Admin, 200: Moderator, 300: Full member, 400: Member, 600: Guest).
        bot_type: Type of bot (1: Outgoing webhook, 2: Generic bot, 3: Incoming webhook).
        bot_owner_id: ID of the bot owner (required for bots).
        service_url: URL for bot's service (required for outgoing webhook bots).
        extra_base_payload: Additional data for bot creation.
    """
    data = {
        "email": email,
        "full_name": full_name,
    }
    
    if password is not None:
        data["password"] = password
    if short_name is not None:
        data["short_name"] = short_name
    if avatar_source is not None:
        data["avatar_source"] = avatar_source
    if default_language is not None:
        data["default_language"] = default_language
    if timezone is not None:
        data["timezone"] = timezone
    if role is not None:
        data["role"] = role
    if bot_type is not None:
        data["bot_type"] = bot_type
    if bot_owner_id is not None:
        data["bot_owner_id"] = bot_owner_id
    if service_url is not None:
        data["service_url"] = service_url
    if extra_base_payload is not None:
        data["extra_base_payload"] = json.dumps(extra_base_payload)
    
    return zulip_request("POST", "/users", data=data)


@mcp.tool()
def update_user(user_id: int, **kwargs) -> Dict[str, Any]:
    """Update a user's profile.
    
    Args:
        user_id: The ID of the user to update.
        **kwargs: User fields to update (full_name, avatar_source, timezone, role, is_active, bot_type, bot_owner_id, service_url, extra_base_payload).
    """
    data = {}
    
    if "full_name" in kwargs:
        data["full_name"] = kwargs["full_name"]
    if "avatar_source" in kwargs:
        data["avatar_source"] = kwargs["avatar_source"]
    if "timezone" in kwargs:
        data["timezone"] = kwargs["timezone"]
    if "role" in kwargs:
        data["role"] = kwargs["role"]
    if "is_active" in kwargs:
        data["is_active"] = str(kwargs["is_active"]).lower()
    if "bot_type" in kwargs:
        data["bot_type"] = kwargs["bot_type"]
    if "bot_owner_id" in kwargs:
        data["bot_owner_id"] = kwargs["bot_owner_id"]
    if "service_url" in kwargs:
        data["service_url"] = kwargs["service_url"]
    if "extra_base_payload" in kwargs:
        data["extra_base_payload"] = json.dumps(kwargs["extra_base_payload"])
    
    return zulip_request("PATCH", f"/users/{user_id}", data=data)


@mcp.tool()
def update_user_by_email(email: str, **kwargs) -> Dict[str, Any]:
    """Update a user's profile by email.
    
    Args:
        email: The email of the user to update.
        **kwargs: User fields to update.
    """
    data = {}
    
    if "full_name" in kwargs:
        data["full_name"] = kwargs["full_name"]
    if "avatar_source" in kwargs:
        data["avatar_source"] = kwargs["avatar_source"]
    if "timezone" in kwargs:
        data["timezone"] = kwargs["timezone"]
    if "role" in kwargs:
        data["role"] = kwargs["role"]
    if "is_active" in kwargs:
        data["is_active"] = str(kwargs["is_active"]).lower()
    if "bot_type" in kwargs:
        data["bot_type"] = kwargs["bot_type"]
    if "bot_owner_id" in kwargs:
        data["bot_owner_id"] = kwargs["bot_owner_id"]
    if "service_url" in kwargs:
        data["service_url"] = kwargs["service_url"]
    if "extra_base_payload" in kwargs:
        data["extra_base_payload"] = json.dumps(kwargs["extra_base_payload"])
    
    return zulip_request("PATCH", f"/users/{email}", data=data)


@mcp.tool()
def deactivate_user(user_id: int) -> Dict[str, Any]:
    """Deactivate a user.
    
    Args:
        user_id: The ID of the user to deactivate.
    """
    return zulip_request("DELETE", f"/users/{user_id}")


@mcp.tool()
def deactivate_own_user() -> Dict[str, Any]:
    """Deactivate own user account."""
    return zulip_request("DELETE", "/users/me")


@mcp.tool()
def reactivate_user(user_id: int) -> Dict[str, Any]:
    """Reactivate a deactivated user.
    
    Args:
        user_id: The ID of the user to reactivate.
    """
    data = {"user_id": user_id}
    return zulip_request("POST", "/users/me/reactivate", data=data)


@mcp.tool()
def get_user_presences() -> Dict[str, Any]:
    """Get presence information for all users in the organization."""
    return zulip_request("GET", "/users/me/presence")


@mcp.tool()
def get_user_presence(user_id: int) -> Dict[str, Any]:
    """Get presence information for a specific user.
    
    Args:
        user_id: The ID of the user.
    """
    return zulip_request("GET", f"/users/{user_id}/presence")


@mcp.tool()
def update_presence(
    status: str = "active",
    away: bool = False,
    timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    """Update your presence status.
    
    Args:
        status: The presence status ("active" or "idle").
        away: Whether the user is away.
        timestamp: UNIX timestamp for when the status change occurred.
    """
    data = {"status": status, "away": str(away).lower()}
    
    if timestamp is not None:
        data["timestamp"] = timestamp
    
    return zulip_request("PATCH", "/users/me/presence", data=data)


@mcp.tool()
def set_typing_status(
    operator: str,
    recipient_id: int,
    message_type: str = "stream",
) -> Dict[str, Any]:
    """Set the "typing" status.
    
    Args:
        operator: The operator ("start" or "stop").
        recipient_id: The ID of the channel or user to send the typing status to.
        message_type: The type ("stream" or "private").
    """
    data = {
        "operator": operator,
        "to": recipient_id,
        "type": message_type,
    }
    return zulip_request("POST", "/users/me/set_typing", data=data)


@mcp.tool()
def get_user_status(user_id: Optional[int] = None) -> Dict[str, Any]:
    """Get a user's status.
    
    Args:
        user_id: The ID of the user (defaults to current user).
    """
    if user_id is None:
        return zulip_request("GET", "/users/me/status")
    return zulip_request("GET", f"/users/{user_id}/status")


@mcp.tool()
def update_status(
    status: Optional[str] = None,
    presence: Optional[str] = None,
    message: Optional[str] = None,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = "unicode_emoji",
    duration: Optional[int] = None,
) -> Dict[str, Any]:
    """Update your status.
    
    Args:
        status: The status ("active", "idle", or "offline").
        presence: The presence status ("active" or "idle").
        message: The status message.
        emoji_name: The name of the emoji to display.
        emoji_code: The emoji code.
        reaction_type: One of "unicode_emoji", "realm_emoji", "emoji_code".
        duration: Duration in minutes for the status.
    """
    data = {}
    
    if status is not None:
        data["status"] = status
    if presence is not None:
        data["presence"] = presence
    if message is not None:
        data["message"] = message
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    if duration is not None:
        data["duration"] = duration
    
    return zulip_request("POST", "/users/me/status", data=data)


@mcp.tool()
def update_user_status(
    user_id: int,
    status: Optional[str] = None,
    presence: Optional[str] = None,
    message: Optional[str] = None,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = "unicode_emoji",
) -> Dict[str, Any]:
    """Update another user's status.
    
    Args:
        user_id: The ID of the user to update.
        status: The status ("active", "idle", or "offline").
        presence: The presence status ("active" or "idle").
        message: The status message.
        emoji_name: The name of the emoji to display.
        emoji_code: The emoji code.
        reaction_type: One of "unicode_emoji", "realm_emoji", "emoji_code".
    """
    data = {"user_id": user_id}
    
    if status is not None:
        data["status"] = status
    if presence is not None:
        data["presence"] = presence
    if message is not None:
        data["message"] = message
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    
    return zulip_request("PATCH", "/users/me/status", data=data)


@mcp.tool()
def get_alert_words() -> Dict[str, Any]:
    """Get all alert words for the current user."""
    return zulip_request("GET", "/users/me/alert_words")


@mcp.tool()
def add_alert_words(alert_words: List[str]) -> Dict[str, Any]:
    """Add alert words for the current user.
    
    Args:
        alert_words: List of alert words to add.
    """
    data = {"alert_words": json.dumps(alert_words)}
    return zulip_request("POST", "/users/me/alert_words", data=data)


@mcp.tool()
def remove_alert_words(alert_words: List[str]) -> Dict[str, Any]:
    """Remove alert words for the current user.
    
    Args:
        alert_words: List of alert words to remove.
    """
    data = {"alert_words": json.dumps(alert_words)}
    return zulip_request("DELETE", "/users/me/alert_words", data=data)


@mcp.tool()
def get_user_groups() -> Dict[str, Any]:
    """Get all user groups in the organization."""
    return zulip_request("GET", "/user_groups")


@mcp.tool()
def create_user_group(
    name: str,
    description: str,
    members: Optional[List[int]] = None,
    direct_subgroups: Optional[List[int]] = None,
    can_mention_group: Optional[int | Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a new user group.
    
    Args:
        name: Name of the user group.
        description: Description of the user group.
        members: List of member IDs to add to the group.
        direct_subgroups: List of subgroup IDs.
        can_mention_group: Group that can mention this group.
    """
    data = {
        "name": name,
        "description": description,
    }
    
    if members is not None:
        data["members"] = json.dumps(members)
    if direct_subgroups is not None:
        data["direct_subgroups"] = json.dumps(direct_subgroups)
    if can_mention_group is not None:
        data["can_mention_group"] = json.dumps(can_mention_group) if isinstance(can_mention_group, dict) else can_mention_group
    
    return zulip_request("POST", "/user_groups", data=data)


@mcp.tool()
def update_user_group(
    user_group_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    can_mention_group: Optional[int | Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Update a user group.
    
    Args:
        user_group_id: The ID of the user group.
        name: New name for the group.
        description: New description for the group.
        can_mention_group: Group that can mention this group.
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if can_mention_group is not None:
        data["can_mention_group"] = json.dumps(can_mention_group) if isinstance(can_mention_group, dict) else can_mention_group
    
    return zulip_request("PATCH", f"/user_groups/{user_group_id}", data=data)


@mcp.tool()
def delete_user_group(user_group_id: int) -> Dict[str, Any]:
    """Delete a user group.
    
    Args:
        user_group_id: The ID of the user group to delete.
    """
    return zulip_request("DELETE", f"/user_groups/{user_group_id}")


@mcp.tool()
def update_user_group_members(
    user_group_id: int,
    add: Optional[List[int]] = None,
    remove: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Update user group members.
    
    Args:
        user_group_id: The ID of the user group.
        add: List of member IDs to add.
        remove: List of member IDs to remove.
    """
    data = {}
    
    if add is not None:
        data["add"] = json.dumps(add)
    if remove is not None:
        data["remove"] = json.dumps(remove)
    
    return zulip_request("POST", f"/user_groups/{user_group_id}/members", data=data)


@mcp.tool()
def get_user_group_members(user_group_id: int) -> Dict[str, Any]:
    """Get members of a user group.
    
    Args:
        user_group_id: The ID of the user group.
    """
    return zulip_request("GET", f"/user_groups/{user_group_id}/members")


@mcp.tool()
def get_user_group_subgroups(user_group_id: int) -> Dict[str, Any]:
    """Get subgroups of a user group.
    
    Args:
        user_group_id: The ID of the user group.
    """
    return zulip_request("GET", f"/user_groups/{user_group_id}/subgroups")


@mcp.tool()
def update_user_group_subgroups(
    user_group_id: int,
    add: Optional[List[int]] = None,
    remove: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Update user group subgroups.
    
    Args:
        user_group_id: The ID of the user group.
        add: List of subgroup IDs to add.
        remove: List of subgroup IDs to remove.
    """
    data = {}
    
    if add is not None:
        data["add"] = json.dumps(add)
    if remove is not None:
        data["remove"] = json.dumps(remove)
    
    return zulip_request("POST", f"/user_groups/{user_group_id}/subgroups", data=data)


@mcp.tool()
def get_user_group_membership_status(
    user_group_id: int,
    user_id: Optional[int] = None,
) -> Dict[str, Any]:
    """Check if a user is a member of a user group.
    
    Args:
        user_group_id: The ID of the user group.
        user_id: The ID of the user (defaults to current user).
    """
    params = {}
    if user_id is not None:
        params["user_id"] = user_id
    
    return zulip_request("GET", f"/user_groups/{user_group_id}/members/{user_id if user_id is not None else 'me'}", params=params)


@mcp.tool()
def mute_user(user_id: int) -> Dict[str, Any]:
    """Mute a user.
    
    Args:
        user_id: The ID of the user to mute.
    """
    data = {"user_id": user_id}
    return zulip_request("POST", "/users/me/muted_users", data=data)


@mcp.tool()
def unmute_user(user_id: int) -> Dict[str, Any]:
    """Unmute a user.
    
    Args:
        user_id: The ID of the user to unmute.
    """
    data = {"user_id": user_id}
    return zulip_request("DELETE", "/users/me/muted_users", data=data)


# ============================================================================
# Server/organization endpoints
# ============================================================================

@mcp.tool()
def get_server_settings() -> Dict[str, Any]:
    """Get server settings and configuration."""
    return zulip_request("GET", "/server_settings")


@mcp.tool()
def get_linkifiers() -> Dict[str, Any]:
    """Get all linkifiers in the organization."""
    return zulip_request("GET", "/realm/linkifiers")


@mcp.tool()
def add_linkifier(
    pattern: str,
    url_template: str,
    example_input: Optional[str] = None,
    reverse_template: Optional[str] = None,
) -> Dict[str, Any]:
    """Add a linkifier to automatically linkify patterns in messages.
    
    Args:
        pattern: The regex pattern to match.
        url_template: The URL template to link to.
        example_input: Example input to show in the admin UI.
        reverse_template: Template for generating the linkifier from the matched value.
    """
    data = {
        "pattern": pattern,
        "url_template": url_template,
    }
    
    if example_input is not None:
        data["example_input"] = example_input
    if reverse_template is not None:
        data["reverse_template"] = reverse_template
    
    return zulip_request("POST", "/realm/filters", data=data)


@mcp.tool()
def update_linkifier(
    filter_id: int,
    pattern: Optional[str] = None,
    url_template: Optional[str] = None,
    example_input: Optional[str] = None,
    reverse_template: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a linkifier.
    
    Args:
        filter_id: The ID of the linkifier to update.
        pattern: New regex pattern.
        url_template: New URL template.
        example_input: New example input.
        reverse_template: New reverse template.
    """
    data = {}
    
    if pattern is not None:
        data["pattern"] = pattern
    if url_template is not None:
        data["url_template"] = url_template
    if example_input is not None:
        data["example_input"] = example_input
    if reverse_template is not None:
        data["reverse_template"] = reverse_template
    
    return zulip_request("PATCH", f"/realm/filters/{filter_id}", data=data)


@mcp.tool()
def delete_linkifier(filter_id: int) -> Dict[str, Any]:
    """Delete a linkifier.
    
    Args:
        filter_id: The ID of the linkifier to delete.
    """
    return zulip_request("DELETE", f"/realm/filters/{filter_id}")


@mcp.tool()
def reorder_linkifiers(
    linkifiers: List[int],
) -> Dict[str, Any]:
    """Reorder linkifiers.
    
    Args:
        linkifiers: List of linkifier IDs in the desired order.
    """
    data = {"linkifiers": json.dumps(linkifiers)}
    return zulip_request("POST", "/realm/filters/order", data=data)


@mcp.tool()
def get_custom_profile_fields() -> Dict[str, Any]:
    """Get all custom profile fields."""
    return zulip_request("GET", "/realm/profile_fields")


@mcp.tool()
def create_custom_profile_field(
    name: str,
    field_type: int,
    hint: Optional[str] = None,
    required: Optional[bool] = None,
    show_on_profile_page: Optional[bool] = None,
    display_in_profile_summary: Optional[bool] = None,
    choices: Optional[List[str]] = None,
    validator: Optional[Dict[str, Any]] = None,
    sort_order: Optional[int] = None,
) -> Dict[str, Any]:
    """Create a custom profile field.
    
    Args:
        name: Name of the field.
        field_type: Type of field (1: Text, 2: Long text, 3: Date, 4: Link, 5: Person, 6: External account, 7: Undef).
        hint: Hint text to display.
        required: Whether the field is required.
        show_on_profile_page: Whether to show on the profile page.
        display_in_profile_summary: Whether to display in profile summary.
        choices: List of choices for dropdown field.
        validator: Validation settings.
        sort_order: Sort order for the field.
    """
    data = {
        "name": name,
        "field_type": field_type,
    }
    
    if hint is not None:
        data["hint"] = hint
    if required is not None:
        data["required"] = str(required).lower()
    if show_on_profile_page is not None:
        data["show_on_profile_page"] = str(show_on_profile_page).lower()
    if display_in_profile_summary is not None:
        data["display_in_profile_summary"] = str(display_in_profile_summary).lower()
    if choices is not None:
        data["choices"] = json.dumps(choices)
    if validator is not None:
        data["validator"] = json.dumps(validator)
    if sort_order is not None:
        data["sort_order"] = sort_order
    
    return zulip_request("POST", "/realm/profile_fields", data=data)


@mcp.tool()
def update_custom_profile_field(
    field_id: int,
    name: Optional[str] = None,
    field_type: Optional[int] = None,
    hint: Optional[str] = None,
    required: Optional[bool] = None,
    show_on_profile_page: Optional[bool] = None,
    display_in_profile_summary: Optional[bool] = None,
    choices: Optional[List[str]] = None,
    validator: Optional[Dict[str, Any]] = None,
    sort_order: Optional[int] = None,
) -> Dict[str, Any]:
    """Update a custom profile field.
    
    Args:
        field_id: The ID of the field to update.
        name: New name for the field.
        field_type: New type for the field.
        hint: New hint text.
        required: Whether the field is required.
        show_on_profile_page: Whether to show on the profile page.
        display_in_profile_summary: Whether to display in profile summary.
        choices: List of choices for dropdown field.
        validator: Validation settings.
        sort_order: Sort order for the field.
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if field_type is not None:
        data["field_type"] = field_type
    if hint is not None:
        data["hint"] = hint
    if required is not None:
        data["required"] = str(required).lower()
    if show_on_profile_page is not None:
        data["show_on_profile_page"] = str(show_on_profile_page).lower()
    if display_in_profile_summary is not None:
        data["display_in_profile_summary"] = str(display_in_profile_summary).lower()
    if choices is not None:
        data["choices"] = json.dumps(choices)
    if validator is not None:
        data["validator"] = json.dumps(validator)
    if sort_order is not None:
        data["sort_order"] = sort_order
    
    return zulip_request("PATCH", f"/realm/profile_fields/{field_id}", data=data)


@mcp.tool()
def delete_custom_profile_field(field_id: int) -> Dict[str, Any]:
    """Delete a custom profile field.
    
    Args:
        field_id: The ID of the field to delete.
    """
    return zulip_request("DELETE", f"/realm/profile_fields/{field_id}")


@mcp.tool()
def reorder_custom_profile_fields(
    profile_fields: List[int],
) -> Dict[str, Any]:
    """Reorder custom profile fields.
    
    Args:
        profile_fields: List of field IDs in the desired order.
    """
    data = {"profile_fields": json.dumps(profile_fields)}
    return zulip_request("POST", "/realm/profile_fields/order", data=data)


@mcp.tool()
def get_realm_exports() -> Dict[str, Any]:
    """Get all realm export requests."""
    return zulip_request("GET", "/export/realm")


@mcp.tool()
def create_realm_export(
    export_type: str,
    output_format: str = "json",
) -> Dict[str, Any]:
    """Create a realm export request.
    
    Args:
        export_type: Type of export ("full", "deactivated", "active").
        output_format: Output format ("json" or "csv").
    """
    data = {
        "export_type": export_type,
        "output_format": output_format,
    }
    return zulip_request("POST", "/export/realm", data=data)


@mcp.tool()
def get_realm_export_consents() -> Dict[str, Any]:
    """Get realm export consents."""
    return zulip_request("GET", "/export/realm/consents")


@mcp.tool()
def get_attachments() -> Dict[str, Any]:
    """Get all attachments for the current user."""
    return zulip_request("GET", "/attachments")


@mcp.tool()
def delete_attachment(attachment_id: int) -> Dict[str, Any]:
    """Delete an attachment.
    
    Args:
        attachment_id: The ID of the attachment to delete.
    """
    return zulip_request("DELETE", f"/attachments/{attachment_id}")


@mcp.tool()
def get_saved_snippets() -> Dict[str, Any]:
    """Get all saved snippets for the current user."""
    return zulip_request("GET", "/saved_snippets")


@mcp.tool()
def create_saved_snippet(
    name: str,
    content: str,
) -> Dict[str, Any]:
    """Create a saved snippet.
    
    Args:
        name: Name of the snippet.
        content: Content of the snippet.
    """
    data = {
        "name": name,
        "content": content,
    }
    return zulip_request("POST", "/saved_snippets", data=data)


@mcp.tool()
def update_saved_snippet(
    snippet_id: int,
    name: Optional[str] = None,
    content: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a saved snippet.
    
    Args:
        snippet_id: The ID of the snippet to update.
        name: New name for the snippet.
        content: New content for the snippet.
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if content is not None:
        data["content"] = content
    
    return zulip_request("PATCH", f"/saved_snippets/{snippet_id}", data=data)


@mcp.tool()
def delete_saved_snippet(snippet_id: int) -> Dict[str, Any]:
    """Delete a saved snippet.
    
    Args:
        snippet_id: The ID of the snippet to delete.
    """
    return zulip_request("DELETE", f"/saved_snippets/{snippet_id}")


@mcp.tool()
def get_navigation_views() -> Dict[str, Any]:
    """Get all navigation views."""
    return zulip_request("GET", "/navigation_views")


@mcp.tool()
def add_navigation_view(
    name: str,
    fragment: str,
    is_pinned: bool = True,
) -> Dict[str, Any]:
    """Add a navigation view.
    
    Args:
        name: Name of the navigation view.
        fragment: Navigation fragment (e.g., "narrow/is/alerted").
        is_pinned: Whether the view should be pinned.
    """
    data = {
        "name": name,
        "fragment": fragment,
        "is_pinned": str(is_pinned).lower(),
    }
    return zulip_request("POST", "/navigation_views", data=data)


@mcp.tool()
def update_navigation_view(
    navigation_view_id: int,
    name: Optional[str] = None,
    fragment: Optional[str] = None,
    is_pinned: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a navigation view.
    
    Args:
        navigation_view_id: The ID of the navigation view to update.
        name: New name for the view.
        fragment: New navigation fragment.
        is_pinned: Whether the view should be pinned.
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if fragment is not None:
        data["fragment"] = fragment
    if is_pinned is not None:
        data["is_pinned"] = str(is_pinned).lower()
    
    return zulip_request("PATCH", f"/navigation_views/{navigation_view_id}", data=data)


@mcp.tool()
def remove_navigation_view(navigation_view_id: int) -> Dict[str, Any]:
    """Remove a navigation view.
    
    Args:
        navigation_view_id: The ID of the navigation view to remove.
    """
    return zulip_request("DELETE", f"/navigation_views/{navigation_view_id}")


@mcp.tool()
def get_channel_folders() -> Dict[str, Any]:
    """Get all channel folders."""
    return zulip_request("GET", "/channels/folders")


@mcp.tool()
def create_channel_folder(
    name: str,
    channel_ids: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Create a channel folder.
    
    Args:
        name: Name of the folder.
        channel_ids: List of channel IDs to include in the folder.
    """
    data = {"name": name}
    
    if channel_ids is not None:
        data["channel_ids"] = json.dumps(channel_ids)
    
    return zulip_request("POST", "/channels/folders", data=data)


@mcp.tool()
def update_channel_folder(
    folder_id: int,
    name: Optional[str] = None,
    channel_ids: Optional[List[int]] = None,
    order: Optional[int] = None,
) -> Dict[str, Any]:
    """Update a channel folder.
    
    Args:
        folder_id: The ID of the folder to update.
        name: New name for the folder.
        channel_ids: New list of channel IDs in the folder.
        order: New order for the folder.
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if channel_ids is not None:
        data["channel_ids"] = json.dumps(channel_ids)
    if order is not None:
        data["order"] = order
    
    return zulip_request("PATCH", f"/channels/folders/{folder_id}", data=data)


@mcp.tool()
def delete_channel_folder(folder_id: int) -> Dict[str, Any]:
    """Delete a channel folder.
    
    Args:
        folder_id: The ID of the folder to delete.
    """
    return zulip_request("DELETE", f"/channels/folders/{folder_id}")


@mcp.tool()
def patch_channel_folders(
    folders: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Patch channel folders.
    
    Args:
        folders: List of folder objects with id and channel_ids.
    """
    data = {"folders": json.dumps(folders)}
    return zulip_request("PATCH", "/channels/folders", data=data)


@mcp.tool()
def get_invites() -> Dict[str, Any]:
    """Get all invitations for the current user."""
    return zulip_request("GET", "/invites")


@mcp.tool()
def send_invites(
    invitee_emails: List[str],
    invitee_realm: Optional[str] = None,
    invite_text: Optional[str] = None,
    auto_subscribe: Optional[bool] = False,
    invite_as: Optional[int] = None,
) -> Dict[str, Any]:
    """Send email invitations.
    
    Args:
        invitee_emails: List of email addresses to invite.
        invitee_realm: The realm to invite users to.
        invite_text: Text to include in the invitation email.
        auto_subscribe: Whether to automatically subscribe invites to channels.
        invite_as: Role for invited users (300: Full member, 400: Member, 600: Guest).
    """
    data = {"invitees": json.dumps(invitee_emails)}
    
    if invitee_realm is not None:
        data["invitee_realm"] = invitee_realm
    if invite_text is not None:
        data["invite_text"] = invite_text
    if auto_subscribe is not None:
        data["auto_subscribe"] = str(auto_subscribe).lower()
    if invite_as is not None:
        data["invite_as"] = invite_as
    
    return zulip_request("POST", "/invites", data=data)


@mcp.tool()
def create_invite_link(
    invite_expires_in_minutes: int,
    invitee_emails: Optional[List[str]] = None,
    invitee_realm: Optional[str