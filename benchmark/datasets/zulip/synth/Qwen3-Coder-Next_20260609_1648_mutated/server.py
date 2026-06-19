#!/usr/bin/env python3
"""Zulip MCP Server - An MCP server with comprehensive coverage of the Zulip REST API."""

import os
import requests
from typing import Any, Dict, List
from fastmcp import FastMCP
from fastmcp.tools import Tool

# Initialize MCP server
mcp = FastMCP("zulip")

# Configuration
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

# Base URL
BASE_URL = f"{ZULIP_SITE.rstrip('/')}/api/v1"


def make_request(method: str, path: str, params: Dict[str, Any] = None, 
                 data: Dict[str, Any] = None) -> Dict[str, Any]:
    """Make a request to the Zulip API with basic auth."""
    auth = (ZULIP_EMAIL, ZULIP_API_KEY)
    url = f"{BASE_URL}{path}"
    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params, auth=auth)
        elif method.upper() == "POST":
            response = requests.post(url, data=data, auth=auth)
        elif method.upper() == "PATCH":
            response = requests.patch(url, data=data, auth=auth)
        elif method.upper() == "DELETE":
            response = requests.delete(url, auth=auth)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_json = e.response.json()
            return {"error": error_json.get("msg", str(e)), "code": error_json.get("code")}
        except:
            return {"error": str(e), "status_code": e.response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ===================== MESSAGE ENDPOINTS =====================

@mcp.tool()
def send_message(
    type: str, 
    to: str | List[int] | List[str], 
    content: str,
    message_topic: str | None = None,
    topic: str | None = None,
    read_by_sender: bool | None = None
) -> Dict[str, Any]:
    """Send a channel message or direct message.
    
    Args:
        type: "direct" for DMs, "channel_name" or "channel" for channel messages
        to: Channel name/string or list of user IDs/emails for DMs
        content: Message content
        message_topic: Message topic (required for channel messages)
        topic: Deprecated alias for message_topic
        read_by_sender: Whether message is marked read by sender
    """
    data = {
        "type": type,
        "to": ",".join(to) if isinstance(to, list) else to,
        "content": content,
    }
    if message_topic:
        data["message_topic"] = message_topic
    if topic:
        data["topic"] = topic  # deprecated alias
    if read_by_sender is not None:
        data["read_by_sender"] = str(read_by_sender).lower()
    
    return make_request("POST", "/messages", data=data)


@mcp.tool()
def fetch_message(message_id: int, 
                  apply_markdown: bool = True,
                  allow_empty_topic_name: bool = False) -> Dict[str, Any]:
    """Fetch a single message by ID.
    
    Args:
        message_id: The ID of the message to fetch
        apply_markdown: Whether to return HTML-rendered content
        allow_empty_topic_name: Whether to support empty topic names
    """
    params = {
        "apply_markdown": str(apply_markdown).lower(),
        "allow_empty_topic_name": str(allow_empty_topic_name).lower()
    }
    return make_request("GET", f"/messages/{message_id}", params=params)


@mcp.tool()
def get_messages(
    start_message_id: str = "newest",
    before_count: int = 100,
    after_count: int = 0,
    filter_spec: List[Dict[str, Any]] | None = None,
    client_gravatar: bool = True,
    apply_markdown: bool = True
) -> Dict[str, Any]:
    """Get messages matching a filter_spec.
    
    Args:
        start_message_id: Anchor message ID or special value ("newest", "oldest", "first_unread")
        before_count: Number of messages before anchor
        after_count: Number of messages after anchor
        filter_spec: Filter specification for narrowing messages
        client_gravatar: Whether client can compute gravatars
        apply_markdown: Whether to return HTML-rendered content
    """
    data = {
        "start_message_id": start_message_id,
        "before_count": str(before_count),
        "after_count": str(after_count),
        "client_gravatar": str(client_gravatar).lower(),
        "apply_markdown": str(apply_markdown).lower(),
    }
    if filter_spec:
        import json
        data["filter_spec"] = json.dumps(filter_spec)
    
    return make_request("GET", "/messages", params=data)


@mcp.tool()
def edit_message(message_id: int, 
                 content: str | None = None,
                 message_topic: str | None = None,
                 topic: str | None = None,
                 propagate_mode: str = "change_one",
                 send_notification_to_old_thread: bool = False,
                 send_notification_to_new_thread: bool = True,
                 stream_id: int | None = None) -> Dict[str, Any]:
    """Edit a message's content, topic, or channel.
    
    Args:
        message_id: ID of message to edit
        content: New content for message
        message_topic: New topic for message
        topic: Deprecated alias for message_topic
        propagate_mode: How to propagate changes ("change_one", "change_later", "change_all")
        send_notification_to_old_thread: Send notification to old thread
        send_notification_to_new_thread: Send notification to new thread
        stream_id: New channel ID to move message to
    """
    data = {
        "propagate_mode": propagate_mode,
        "send_notification_to_old_thread": str(send_notification_to_old_thread).lower(),
        "send_notification_to_new_thread": str(send_notification_to_new_thread).lower(),
    }
    if content:
        data["content"] = content
    if message_topic:
        data["message_topic"] = message_topic
    if topic:
        data["topic"] = topic  # deprecated alias
    if stream_id:
        data["stream_id"] = str(stream_id)
    
    return make_request("PATCH", f"/messages/{message_id}", data=data)


@mcp.tool()
def delete_message(message_id: int) -> Dict[str, Any]:
    """Permanently delete a message.
    
    Args:
        message_id: ID of message to delete
    """
    return make_request("DELETE", f"/messages/{message_id}")


@mcp.tool()
def get_message_history(message_id: int, 
                        allow_empty_topic_name: bool = False) -> Dict[str, Any]:
    """Get the edit history of a message.
    
    Args:
        message_id: ID of message to get history for
        allow_empty_topic_name: Whether to support empty topic names
    """
    params = {
        "allow_empty_topic_name": str(allow_empty_topic_name).lower()
    }
    return make_request("GET", f"/messages/{message_id}/history", params=params)


@mcp.tool()
def add_reaction(message_id: int, emoji_name: str, 
                 emoji_code: str | None = None,
                 reaction_type: str | None = None) -> Dict[str, Any]:
    """Add an emoji reaction to a message.
    
    Args:
        message_id: ID of message to react to
        emoji_name: Name of emoji to add
        emoji_code: Optional emoji code for specificity
        reaction_type: Type of emoji (unicode_emoji, realm_emoji, zulip_extra_emoji)
    """
    data = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    if reaction_type:
        data["reaction_type"] = reaction_type
    
    return make_request("POST", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str,
                    emoji_code: str | None = None,
                    reaction_type: str | None = None) -> Dict[str, Any]:
    """Remove an emoji reaction from a message.
    
    Args:
        message_id: ID of message to remove reaction from
        emoji_name: Name of emoji to remove
        emoji_code: Optional emoji code for specificity
        reaction_type: Type of emoji (unicode_emoji, realm_emoji, zulip_extra_emoji)
    """
    data = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    if reaction_type:
        data["reaction_type"] = reaction_type
    
    return make_request("DELETE", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def update_message_flags(messages: List[int], 
                         op: str, 
                         flag: str) -> Dict[str, Any]:
    """Update personal message flags (read, starred, etc.) on messages.
    
    Args:
        messages: List of message IDs to update
        op: Operation ("add" or "remove")
        flag: Flag to update (read, starred, mentioned, etc.)
    """
    data = {
        "messages": ",".join(str(m) for m in messages),
        "op": op,
        "flag": flag,
    }
    return make_request("POST", "/messages/flags", data=data)


@mcp.tool()
def mark_all_as_read() -> Dict[str, Any]:
    """Mark all of the current user's unread messages as read.
    
    Deprecated - clients should use update_message_flags instead.
    """
    return make_request("POST", "/mark_all_as_read")


@mcp.tool()
def update_message_flags_for_narrow(filter_spec: List[Dict[str, Any]], 
                                     op: str, 
                                     flag: str) -> Dict[str, Any]:
    """Update message flags for messages matching a filter_spec.
    
    Args:
        filter_spec: Filter specification for narrowing messages
        op: Operation ("add" or "remove")
        flag: Flag to update (read, starred, mentioned, etc.)
    """
    import json
    data = {
        "filter_spec": json.dumps(filter_spec),
        "op": op,
        "flag": flag,
    }
    return make_request("POST", "/messages/flags/narrow", data=data)


@mcp.tool()
def mark_stream_as_read(stream_id: int) -> Dict[str, Any]:
    """Mark all messages in a channel as read.
    
    Args:
        stream_id: ID of channel to mark as read
    """
    data = {"stream_id": str(stream_id)}
    return make_request("POST", "/mark_stream_as_read", data=data)


@mcp.tool()
def mark_topic_as_read(stream_id: int, topic: str) -> Dict[str, Any]:
    """Mark all messages in a channel topic as read.
    
    Args:
        stream_id: ID of channel
        topic: Topic name to mark as read
    """
    data = {
        "stream_id": str(stream_id),
        "topic": topic,
    }
    return make_request("POST", "/mark_topic_as_read", data=data)


@mcp.tool()
def get_scheduled_messages() -> Dict[str, Any]:
    """Fetch all scheduled messages for the current user."""
    return make_request("GET", "/scheduled_messages")


@mcp.tool()
def create_scheduled_message(
    type: str,
    to: str | List[int],
    content: str,
    scheduled_delivery_timestamp: int,
    message_topic: str | None = None,
    topic: str | None = None,
    read_by_sender: bool | None = None
) -> Dict[str, Any]:
    """Create a scheduled message.
    
    Args:
        type: "direct" for DMs, "channel_name" or "channel" for channel messages
        to: Channel ID or list of user IDs
        content: Message content
        scheduled_delivery_timestamp: Unix timestamp for when to send
        message_topic: Message topic (required for channel messages)
        topic: Deprecated alias for message_topic
        read_by_sender: Whether message is marked read by sender
    """
    data = {
        "type": type,
        "to": ",".join(str(t) for t in to) if isinstance(to, list) else str(to),
        "content": content,
        "scheduled_delivery_timestamp": str(scheduled_delivery_timestamp),
    }
    if message_topic:
        data["message_topic"] = message_topic
    if topic:
        data["topic"] = topic
    if read_by_sender is not None:
        data["read_by_sender"] = str(read_by_sender).lower()
    
    return make_request("POST", "/scheduled_messages", data=data)


@mcp.tool()
def update_scheduled_message(
    scheduled_message_id: int,
    type: str | None = None,
    to: str | List[int] | None = None,
    content: str | None = None,
    scheduled_delivery_timestamp: int | None = None,
    message_topic: str | None = None,
    topic: str | None = None,
    read_by_sender: bool | None = None
) -> Dict[str, Any]:
    """Update a scheduled message.
    
    Args:
        scheduled_message_id: ID of scheduled message to update
        type: New type
        to: New target
        content: New content
        scheduled_delivery_timestamp: New delivery timestamp
        message_topic: New topic
        topic: Deprecated alias for message_topic
        read_by_sender: Whether message is marked read by sender
    """
    data = {}
    if type:
        data["type"] = type
    if to:
        data["to"] = ",".join(str(t) for t in to) if isinstance(to, list) else str(to)
    if content:
        data["content"] = content
    if scheduled_delivery_timestamp:
        data["scheduled_delivery_timestamp"] = str(scheduled_delivery_timestamp)
    if message_topic:
        data["message_topic"] = message_topic
    if topic:
        data["topic"] = topic
    if read_by_sender is not None:
        data["read_by_sender"] = str(read_by_sender).lower()
    
    return make_request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


@mcp.tool()
def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """Delete a scheduled message.
    
    Args:
        scheduled_message_id: ID of scheduled message to delete
    """
    return make_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")


@mcp.tool()
def create_message_reminder(
    type: str,
    to: str | List[int],
    content: str,
    scheduled_delivery_timestamp: int,
    message_topic: str | None = None,
    topic: str | None = None
) -> Dict[str, Any]:
    """Create a message reminder.
    
    Args:
        type: "direct" for DMs, "channel_name" or "channel" for channel messages
        to: Channel ID or list of user IDs
        content: Message content
        scheduled_delivery_timestamp: Unix timestamp for when to send
        message_topic: Message topic (required for channel messages)
        topic: Deprecated alias for message_topic
    """
    data = {
        "type": type,
        "to": ",".join(str(t) for t in to) if isinstance(to, list) else str(to),
        "content": content,
        "scheduled_delivery_timestamp": str(scheduled_delivery_timestamp),
    }
    if message_topic:
        data["message_topic"] = message_topic
    if topic:
        data["topic"] = topic
    
    return make_request("POST", "/messages/reminder", data=data)


@mcp.tool()
def get_reminders() -> Dict[str, Any]:
    """Fetch all message reminders for the current user."""
    return make_request("GET", "/ reminders")


@mcp.tool()
def delete_reminder(reminder_id: int) -> Dict[str, Any]:
    """Delete a message reminder.
    
    Args:
        reminder_id: ID of reminder to delete
    """
    return make_request("DELETE", f"/messages/reminder/{reminder_id}")


@mcp.tool()
def upload_file(file_path: str) -> Dict[str, Any]:
    """Upload a file to Zulip.
    
    Args:
        file_path: Path to file to upload
    """
    try:
        with open(file_path, 'rb') as f:
            files = {'filename': f}
            return make_request("POST", "/user_uploads", data={}, files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_attachment(attachment_id: int) -> Dict[str, Any]:
    """Get an attachment by ID.
    
    Args:
        attachment_id: ID of attachment to fetch
    """
    return make_request("GET", f"/user_uploads/{attachment_id}")


@mcp.tool()
def delete_attachment(attachment_id: int) -> Dict[str, Any]:
    """Delete an attachment by ID.
    
    Args:
        attachment_id: ID of attachment to delete
    """
    return make_request("DELETE", f"/user_uploads/{attachment_id}")


@mcp.tool()
def report_message(message_id: int, reason: str | None = None) -> Dict[str, Any]:
    """Report a message to moderators.
    
    Args:
        message_id: ID of message to report
        reason: Optional reason for reporting
    """
    data = {"message_id": str(message_id)}
    if reason:
        data["reason"] = reason
    
    return make_request("POST", "/messages/report", data=data)


# ===================== STREAM/CHANNEL ENDPOINTS =====================

@mcp.tool()
def get_streams(
    include_public: bool = True,
    include_web_public: bool = False,
    include_subscribed: bool = True,
    exclude_archived: bool = True
) -> Dict[str, Any]:
    """Get all channels the user has access to.
    
    Args:
        include_public: Include public channels
        include_web_public: Include web-public channels
        include_subscribed: Include subscribed channels
        exclude_archived: Exclude archived channels
    """
    params = {
        "include_public": str(include_public).lower(),
        "include_web_public": str(include_web_public).lower(),
        "include_subscribed": str(include_subscribed).lower(),
        "exclude_archived": str(exclude_archived).lower(),
    }
    return make_request("GET", "/streams", params=params)


@mcp.tool()
def get_subscribed_streams() -> Dict[str, Any]:
    """Get channels the current user is subscribed to."""
    return make_request("GET", "/users/me/subscriptions")


@mcp.tool()
def subscribe_streams(streams: List[str] | List[Dict[str, Any]],
                      principals: List[str] | List[int] | None = None,
                      announce: bool = False) -> Dict[str, Any]:
    """Subscribe users to channels.
    
    Args:
        streams: List of channel names or channel info dicts with name and optional description
        principals: Optional list of user IDs or emails to subscribe
        announce: Whether to send announcement for new channels
    """
    import json
    data = {
        "subscriptions": json.dumps(streams),
        "announce": str(announce).lower(),
    }
    if principals:
        data["principals"] = json.dumps(
            [str(p) for p in principals]
        )
    
    return make_request("POST", "/users/me/subscriptions", data=data)


@mcp.tool()
def unsubscribe_streams(streams: List[str],
                        principals: List[str] | List[int] | None = None) -> Dict[str, Any]:
    """Unsubscribe users from channels.
    
    Args:
        streams: List of channel names to unsubscribe from
        principals: Optional list of user IDs or emails to unsubscribe
    """
    import json
    data = {
        "subscriptions": json.dumps(streams),
    }
    if principals:
        data["principals"] = json.dumps(
            [str(p) for p in principals]
        )
    
    return make_request("DELETE", "/users/me/subscriptions", data=data)


@mcp.tool()
def get_stream_id(stream_name: str) -> Dict[str, Any]:
    """Get a channel's ID by name.
    
    Args:
        stream_name: Name of channel
    """
    return make_request("GET", f"/streams/{stream_name}/stream_id")


@mcp.tool()
def get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    """Get a channel by ID.
    
    Args:
        stream_id: ID of channel
    """
    return make_request("GET", f"/streams/{stream_id}")


@mcp.tool()
def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """Get topics in a channel.
    
    Args:
        stream_id: ID of channel
    """
    return make_request("GET", f"/streams/{stream_id}/topics")


@mcp.tool()
def get_subscribers(stream_id: int) -> Dict[str, Any]:
    """Get subscribers of a channel.
    
    Args:
        stream_id: ID of channel
    """
    return make_request("GET", f"/streams/{stream_id}/members")


@mcp.tool()
def get_subscription_status(user_id: int, stream_id: int) -> Dict[str, Any]:
    """Get subscription status for a user in a channel.
    
    Args:
        user_id: ID of user
        stream_id: ID of channel
    """
    return make_request("GET", f"/users/{user_id}/subscriptions/{stream_id}")


@mcp.tool()
def update_subscription_settings(
    stream_id: int,
    property_name: str,
    property_value: Any
) -> Dict[str, Any]:
    """Update a subscription property.
    
    Args:
        stream_id: ID of channel
        property_name: Name of property to update
        property_value: New value for property
    """
    data = {
        "stream_id": str(stream_id),
        "property": property_name,
        "value": str(property_value),
    }
    return make_request("PATCH", "/users/me/subscriptions/properties", data=data)


@mcp.tool()
def update_subscription_property(
    stream_id: int,
    property_name: str,
    property_value: Any
) -> Dict[str, Any]:
    """Update a subscription property.
    
    Args:
        stream_id: ID of channel
        property_name: Name of property to update
        property_value: New value for property
    """
    return update_subscription_settings(stream_id, property_name, property_value)


@mcp.tool()
def create_stream(
    name: str,
    description: str | None = None,
    invite_only: bool = False,
    is_web_public: bool = False,
    is_default_stream: bool = False,
    history_public_to_subscribers: bool = True,
    message_retention_days: str | int | None = None,
    topics_policy: str | None = None
) -> Dict[str, Any]:
    """Create a new channel.
    
    Args:
        name: Channel name
        description: Channel description
        invite_only: Whether channel is private
        is_web_public: Whether channel is web-public
        is_default_stream: Whether channel is default for new users
        history_public_to_subscribers: Whether history is public to subscribers
        message_retention_days: Message retention policy
        topics_policy: Topic policy ("inherit", "allow_empty_topic", "disable_empty_topic", "empty_topic_only")
    """
    data = {"name": name}
    if description:
        data["description"] = description
    data["invite_only"] = str(invite_only).lower()
    data["is_web_public"] = str(is_web_public).lower()
    data["is_default_stream"] = str(is_default_stream).lower()
    data["history_public_to_subscribers"] = str(history_public_to_subscribers).lower()
    
    if message_retention_days:
        data["message_retention_days"] = str(message_retention_days)
    
    if topics_policy:
        data["topics_policy"] = topics_policy
    
    return subscribe_streams([data], announce=True)


@mcp.tool()
def update_stream(
    stream_id: int,
    name: str | None = None,
    description: str | None = None,
    invite_only: bool | None = None,
    is_web_public: bool | None = None,
    message_retention_days: str | int | None = None,
    topics_policy: str | None = None
) -> Dict[str, Any]:
    """Update a channel's settings.
    
    Args:
        stream_id: ID of channel
        name: New channel name
        description: New channel description
        invite_only: New private/public status
        is_web_public: New web-public status
        message_retention_days: New message retention policy
        topics_policy: New topic policy
    """
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if invite_only is not None:
        data["invite_only"] = str(invite_only).lower()
    if is_web_public is not None:
        data["is_web_public"] = str(is_web_public).lower()
    if message_retention_days:
        data["message_retention_days"] = str(message_retention_days)
    if topics_policy:
        data["topics_policy"] = topics_policy
    
    return make_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    """Archive a channel.
    
    Args:
        stream_id: ID of channel to archive
    """
    return make_request("DELETE", f"/streams/{stream_id}")


@mcp.tool()
def add_default_stream(stream_id: int) -> Dict[str, Any]:
    """Add a channel as default for new users.
    
    Args:
        stream_id: ID of channel to add as default
    """
    return make_request("POST", f"/default_channels/{stream_id}")


@mcp.tool()
def remove_default_stream(stream_id: int) -> Dict[str, Any]:
    """Remove a channel from default channels for new users.
    
    Args:
        stream_id: ID of channel to remove
    """
    return make_request("DELETE", f"/default_channels/{stream_id}")


@mcp.tool()
def get_subscribers_for_user(user_id: int) -> Dict[str, Any]:
    """Get channels a user is subscribed to.
    
    Args:
        user_id: ID of user
    """
    return make_request("GET", f"/users/{user_id}/subscriptions")


# ===================== TOPIC ENDPOINTS =====================

@mcp.tool()
def update_user_topic(stream_id: int, topic: str, 
                      visibility_policy: int) -> Dict[str, Any]:
    """Update personal preferences for a topic.
    
    Args:
        stream_id: ID of channel
        topic: Topic name
        visibility_policy: Visibility policy (1=normal, 2=pin, 3=mute, 4=follow)
    """
    data = {
        "stream_id": str(stream_id),
        "topic": topic,
        "visibility_policy": str(visibility_policy),
    }
    return make_request("PATCH", "/users/me/subscriptions/mute", data=data)


@mcp.tool()
def delete_topic(stream_id: int, topic: str) -> Dict[str, Any]:
    """Delete (archive) a topic.
    
    Args:
        stream_id: ID of channel
        topic: Topic name to delete
    """
    data = {
        "stream_id": str(stream_id),
        "topic_name": topic,
    }
    return make_request("DELETE", "/topics", data=data)


@mcp.tool()
def mute_topic(stream_id: int, topic: str) -> Dict[str, Any]:
    """Mute a topic.
    
    Args:
        stream_id: ID of channel
        topic: Topic name to mute
    """
    return update_user_topic(stream_id, topic, 3)


@mcp.tool()
def unmute_topic(stream_id: int, topic: str) -> Dict[str, Any]:
    """Unmute a topic.
    
    Args:
        stream_id: ID of channel
        topic: Topic name to unmute
    """
    return update_user_topic(stream_id, topic, 1)


@mcp.tool()
def rename_topic(stream_id: int, old_topic: str, new_topic: str) -> Dict[str, Any]:
    """Rename a topic in a channel.
    
    Args:
        stream_id: ID of channel
        old_topic: Current topic name
        new_topic: New topic name
    """
    data = {
        "stream_id": str(stream_id),
        "old_topic_name": old_topic,
        "new_topic_name": new_topic,
    }
    return make_request("POST", "/topics/rename", data=data)


# ===================== USER ENDPOINTS =====================

@mcp.tool()
def get_user(user_id: int, 
             client_gravatar: bool = True,
             include_custom_profile_fields: bool = False) -> Dict[str, Any]:
    """Get a user by ID.
    
    Args:
        user_id: ID of user
        client_gravatar: Whether client can compute gravatars
        include_custom_profile_fields: Whether to include custom profile fields
    """
    params = {
        "client_gravatar": str(client_gravatar).lower(),
        "include_custom_profile_fields": str(include_custom_profile_fields).lower(),
    }
    return make_request("GET", f"/users/{user_id}", params=params)


@mcp.tool()
def get_user_by_email(email: str) -> Dict[str, Any]:
    """Get a user by email address.
    
    Args:
        email: Email address of user
    """
    return make_request("GET", f"/users?email={email}")


@mcp.tool()
def get_users(
    include_active: bool = True,
    include_bot_users: bool = True,
    include_deactivated: bool = False
) -> Dict[str, Any]:
    """Get all users in the organization.
    
    Args:
        include_active: Include active users
        include_bot_users: Include bot users
        include_deactivated: Include deactivated users
    """
    params = {
        "include_active": str(include_active).lower(),
        "include_bot_users": str(include_bot_users).lower(),
        "include_deactivated": str(include_deactivated).lower(),
    }
    return make_request("GET", "/users", params=params)


@mcp.tool()
def get_user_presences() -> Dict[str, Any]:
    """Get presence information for all users."""
    return make_request("GET", "/users/presences")


@mcp.tool()
def get_user_presence(user_id: int) -> Dict[str, Any]:
    """Get presence information for a specific user.
    
    Args:
        user_id: ID of user
    """
    return make_request("GET", f"/users/{user_id}/presence")


@mcp.tool()
def update_presence(
    status: str,
    active: bool = True,
    ping_only: bool = False
) -> Dict[str, Any]:
    """Update your presence status.
    
    Args:
        status: Presence status ("active", "idle", "offline")
        active: Whether user is active
        ping_only: Whether to only ping server
    """
    data = {
        "status": status,
        "active": str(active).lower(),
    }
    if ping_only:
        data["ping_only"] = str(ping_only).lower()
    
    return make_request("POST", "/users/me/presence", data=data)


@mcp.tool()
def set_typing_status(
    operator: str,
    to: List[int] | List[str],
    message_topic: str | None = None,
    topic: str | None = None
) -> Dict[str, Any]:
    """Set typing status for messages.
    
    Args:
        operator: "start" or "stop"
        to: List of user IDs or channel name
        message_topic: Message topic for channel messages
        topic: Deprecated alias for message_topic
    """
    data = {
        "operator": operator,
        "to": ",".join(str(t) for t in to),
    }
    if message_topic:
        data["message_topic"] = message_topic
    if topic:
        data["topic"] = topic
    
    return make_request("POST", "/typing", data=data)


@mcp.tool()
def set_typing_status_for_message_edit(
    operator: str,
    to: List[int] | List[str]
) -> Dict[str, Any]:
    """Set typing status for message editing.
    
    Args:
        operator: "start" or "stop"
        to: List of user IDs or channel name
    """
    data = {
        "operator": operator,
        "to": ",".join(str(t) for t in to),
    }
    return make_request("POST", "/typing", data=data)


@mcp.tool()
def create_user(
    email: str,
    password: str,
    full_name: str,
    short_name: str | None = None
) -> Dict[str, Any]:
    """Create a new user account (admin only).
    
    Args:
        email: Email address of new user
        password: Password for new user
        full_name: Full name of new user
        short_name: Optional short name
    """
    data = {
        "email": email,
        "password": password,
        "full_name": full_name,
    }
    if short_name:
        data["short_name"] = short_name
    
    return make_request("POST", "/users", data=data)


@mcp.tool()
def update_user(user_id: int,
                full_name: str | None = None,
                role: int | None = None,
                profile_data: List[Dict[str, Any]] | None = None,
                new_email: str | None = None) -> Dict[str, Any]:
    """Update a user's details (admin only).
    
    Args:
        user_id: ID of user to update
        full_name: New full name
        role: New role (100=owner, 200=admin, 300=moderator, 400=member, 600=guest)
        profile_data: Custom profile field data
        new_email: New email address (owner only)
    """
    data = {}
    if full_name:
        data["full_name"] = full_name
    if role:
        data["role"] = str(role)
    if profile_data:
        import json
        data["profile_data"] = json.dumps(profile_data)
    if new_email:
        data["new_email"] = new_email
    
    return make_request("PATCH", f"/users/{user_id}", data=data)


@mcp.tool()
def update_user_by_email(
    email: str,
    full_name: str | None = None,
    role: int | None = None,
    profile_data: List[Dict[str, Any]] | None = None,
    new_email: str | None = None
) -> Dict[str, Any]:
    """Update a user's details by email (admin only).
    
    Args:
        email: Email of user to update
        full_name: New full name
        role: New role
        profile_data: Custom profile field data
        new_email: New email address
    """
    data = {}
    if full_name:
        data["full_name"] = full_name
    if role:
        data["role"] = str(role)
    if profile_data:
        import json
        data["profile_data"] = json.dumps(profile_data)
    if new_email:
        data["new_email"] = new_email
    
    return make_request("PATCH", f"/users/by-email/{email}", data=data)


@mcp.tool()
def deactivate_user(user_id: int,
                    actions: Dict[str, bool] | None = None,
                    deactivation_notification_comment: str | None = None) -> Dict[str, Any]:
    """Deactivate a user account (admin only).
    
    Args:
        user_id: ID of user to deactivate
        actions: Additional actions (delete_profile, delete_public_channel_messages, etc.)
        deactivation_notification_comment: Optional comment for notification email
    """
    data = {}
    if actions:
        import json
        data["actions"] = json.dumps(actions)
    if deactivation_notification_comment:
        data["deactivation_notification_comment"] = deactivation_notification_comment
    
    return make_request("DELETE", f"/users/{user_id}", data=data)


@mcp.tool()
def reactivate_user(user_id: int) -> Dict[str, Any]:
    """Reactivate a deactivated user (admin only).
    
    Args:
        user_id: ID of user to reactivate
    """
    return make_request("POST", f"/users/{user_id}/reactivate")


@mcp.tool()
def get_own_user() -> Dict[str, Any]:
    """Get information about the current user."""
    return make_request("GET", "/users/me")


@mcp.tool()
def update_user_topic(
    stream_id: int,
    topic: str,
    visibility_policy: int
) -> Dict[str, Any]:
    """Update personal preferences for a topic.
    
    Args:
        stream_id: ID of channel
        topic: Topic name
        visibility_policy: Visibility policy (1=normal, 2=pin, 3=mute, 4=follow)
    """
    data = {
        "stream_id": str(stream_id),
        "topic": topic,
        "visibility_policy": str(visibility_policy),
    }
    return make_request("PATCH", "/users/me/subscriptions/mute", data=data)


@mcp.tool()
def get_user_topics(user_id: int) -> Dict[str, Any]:
    """Get topics a user has interacted with.
    
    Args:
        user_id: ID of user
    """
    return make_request("GET", f"/users/{user_id}/topics")


@mcp.tool()
def mute_user(user_id: int) -> Dict[str, Any]:
    """Mute a user.
    
    Args:
        user_id: ID of user to mute
    """
    data = {"user_id": str(user_id)}
    return make_request("POST", "/users/me/mute", data=data)


@mcp.tool()
def unmute_user(user_id: int) -> Dict[str, Any]:
    """Unmute a user.
    
    Args:
        user_id: ID of user to unmute
    """
    data = {"user_id": str(user_id)}
    return make_request("DELETE", "/users/me/mute", data=data)


@mcp.tool()
def update_status(
    status: str,
    emoji_name: str | None = None,
    emoji_code: str | None = None,
    duration: int | None = None,
    notice: str | None = None
) -> Dict[str, Any]:
    """Update your status.
    
    Args:
        status: Status text
        emoji_name: Optional emoji name
        emoji_code: Optional emoji code
        duration: Optional duration in seconds
        notice: Optional notice text
    """
    data = {"status": status}
    if emoji_name:
        data["emoji_name"] = emoji_name
    if emoji_code:
        data["emoji_code"] = emoji_code
    if duration:
        data["duration"] = str(duration)
    if notice:
        data["notice"] = notice
    
    return make_request("POST", "/users/me/status", data=data)


@mcp.tool()
def update_status_for_user(
    user_id: int,
    status: str,
    emoji_name: str | None = None,
    emoji_code: str | None = None,
    duration: int | None = None,
    notice: str | None = None
) -> Dict[str, Any]:
    """Update another user's status (admin only).
    
    Args:
        user_id: ID of user
        status: Status text
        emoji_name: Optional emoji name
        emoji_code: Optional emoji code
        duration: Optional duration in seconds
        notice: Optional notice text
    """
    data = {"status": status}
    if emoji_name:
        data["emoji_name"] = emoji_name
    if emoji_code:
        data["emoji_code"] = emoji_code
    if duration:
        data["duration"] = str(duration)
    if notice:
        data["notice"] = notice
    
    return make_request("PATCH", f"/users/{user_id}/status", data=data)


@mcp.tool()
def get_user_status(user_id: int) -> Dict[str, Any]:
    """Get a user's status.
    
    Args:
        user_id: ID of user
    """
    return make_request("GET", f"/users/{user_id}/status")


# ===================== USER GROUP ENDPOINTS =====================

@mcp.tool()
def get_user_groups() -> Dict[str, Any]:
    """Get all user groups in the organization."""
    return make_request("GET", "/user_groups")


@mcp.tool()
def get_user_group_members(group_id: int) -> Dict[str, Any]:
    """Get members of a user group.
    
    Args:
        group_id: ID of user group
    """
    return make_request("GET", f"/user_groups/{group_id}/members")


@mcp.tool()
def get_user_group_subgroups(group_id: int) -> Dict[str, Any]:
    """Get subgroups of a user group.
    
    Args:
        group_id: ID of user group
    """
    return make_request("GET", f"/user_groups/{group_id}/subgroups")


@mcp.tool()
def get_is_user_group_member(group_id: int, user_id: int) -> Dict[str, Any]:
    """Check if a user is a member of a user group.
    
    Args:
        group_id: ID of user group
        user_id: ID of user
    """
    return make_request("GET", f"/user_groups/{group_id}/members/{user_id}")


@mcp.tool()
def create_user_group(
    name: str,
    description: str,
    members: List[int] | None = None,
    subgroups: List[int] | None = None
) -> Dict[str, Any]:
    """Create a new user group.
    
    Args:
        name: Name of group
        description: Description of group
        members: List of member user IDs
        subgroups: List of subgroup IDs
    """
    data = {
        "name": name,
        "description": description,
    }
    if members:
        data["members"] = ",".join(str(m) for m in members)
    if subgroups:
        data["subgroups"] = ",".join(str(s) for s in subgroups)
    
    return make_request("POST", "/user_groups", data=data)


@mcp.tool()
def update_user_group(
    group_id: int,
    name: str | None = None,
    description: str | None = None
) -> Dict[str, Any]:
    """Update a user group.
    
    Args:
        group_id: ID of user group
        name: New name
        description: New description
    """
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    
    return make_request("PATCH", f"/user_groups/{group_id}", data=data)


@mcp.tool()
def update_user_group_members(
    group_id: int,
    delete: List[int] | None = None,
    add: List[int] | None = None
) -> Dict[str, Any]:
    """Update members of a user group.
    
    Args:
        group_id: ID of user group
        delete: List of user IDs to remove
        add: List of user IDs to add
    """
    data = {}
    if delete:
        data["delete"] = ",".join(str(m) for m in delete)
    if add:
        data["add"] = ",".join(str(m) for m in add)
    
    return make_request("PATCH", f"/user_groups/{group_id}/members", data=data)


@mcp.tool()
def update_user_group_subgroups(
    group_id: int,
    delete: List[int] | None = None,
    add: List[int] | None = None
) -> Dict[str, Any]:
    """Update subgroups of a user group.
    
    Args:
        group_id: ID of user group
        delete: List of subgroup IDs to remove
        add: List of subgroup IDs to add
    """
    data = {}
    if delete:
        data["delete"] = ",".join(str(s) for s in delete)
    if add:
        data["add"] = ",".join(str(s) for s in add)
    
    return make_request("PATCH", f"/user_groups/{group_id}/subgroups", data=data)


@mcp.tool()
def deactivate_user_group(group_id: int) -> Dict[str, Any]:
    """Deactivate a user group.
    
    Args:
        group_id: ID of user group to deactivate
    """
    return make_request("DELETE", f"/user_groups/{group_id}")


# ===================== INVITATION ENDPOINTS =====================

@mcp.tool()
def get_invites() -> Dict[str, Any]:
    """Get all invitations for the current user."""
    return make_request("GET", "/invites")


@mcp.tool()
def send_invites(
    invitee_emails: List[str],
    invitee_names: List[str] | None = None,
    streams: List[int] | None = None,
    include_welcome_email: bool = True
) -> Dict[str, Any]:
    """Send email invitations to users.
    
    Args:
        invitee_emails: List of email addresses to invite
        invitee_names: Optional list of names for invitees
        streams: Optional list of channel IDs to subscribe invitees to
        include_welcome_email: Whether to include welcome email
    """
    data = {
        "invitee_emails": ",".join(invitee_emails),
        "include_welcome_email": str(include_welcome_email).lower(),
    }
    if invitee_names:
        data["invitee_names"] = ",".join(invitee_names)
    if streams:
        data["stream_ids"] = ",".join(str(s) for s in streams)
    
    return make_request("POST", "/invites", data=data)


@mcp.tool()
def create_invite_link(
    invitee_emails: List[str],
    stream_ids: List[int] | None = None,
    include_welcome_email: bool = True,
    invite_expires_in_minutes: int | None = None
) -> Dict[str, Any]:
    """Create a reusable invitation link.
    
    Args:
        invitee_emails: List of email addresses
        stream_ids: Optional list of channel IDs
        include_welcome_email: Whether to include welcome email
        invite_expires_in_minutes: Optional expiration in minutes
    """
    data = {
        "invitee_emails": ",".join(invitee_emails),
        "include_welcome_email": str(include_welcome_email).lower(),
    }
    if stream_ids:
        data["stream_ids"] = ",".join(str(s) for s in stream_ids)
    if invite_expires_in_minutes:
        data["invite_expires_in_minutes"] = str(invite_expires_in_minutes)
    
    return make_request("POST", "/invites/link", data=data)


@mcp.tool()
def revoke_invite(invite_id: int) -> Dict[str, Any]:
    """Revoke an email invitation.
    
    Args:
        invite_id: ID of invitation to revoke
    """
    return make_request("DELETE", f"/invites/{invite_id}")


@mcp.tool()
def resend_invite(invite_id: int) -> Dict[str, Any]:
    """Resend an email invitation.
    
    Args:
        invite_id: ID of invitation to resend
    """
    return make_request("POST", f"/invites/{invite_id}/resend")


@mcp.tool()
def revoke_invite_link(link_id: int) -> Dict[str, Any]:
    """Revoke a reusable invitation link.
    
    Args:
        link_id: ID of link to revoke
    """
    return make_request("DELETE", f"/invites/link/{link_id}")


# ===================== DRAFTS =====================

@mcp.tool()
def get_drafts() -> Dict[str, Any]:
    """Get all drafts for the current user."""
    return make_request("GET", "/drafts")


@mcp.tool()
def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create drafts.
    
    Args:
        drafts: List of draft objects with type, to, content, topic, etc.
    """
    import json
    data = {"drafts": json.dumps(drafts)}
    return make_request("POST", "/drafts", data=data)


@mcp.tool()
def update_draft(
    draft_id: int,
    type: str | None = None,
    to: str | List[int] | None = None,
    content: str | None = None,
    topic: str | None = None
) -> Dict[str, Any]:
    """Update a draft.
    
    Args:
        draft_id: ID of draft to update
        type: New type
        to: New recipients
        content: New content
        topic: New topic
    """
    data = {}
    if type:
        data["type"] = type
    if to:
        data["to"] = ",".join(str(t) for t in to) if isinstance(to, list) else str(to)
    if content:
        data["content"] = content
    if topic:
        data["topic"] = topic
    
    return make_request("patch", f"/drafts/{draft_id}", data=data)


@mcp.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    """Delete a draft.
    
    Args:
        draft_id: ID of draft to delete
    """
    return make_request("DELETE", f"/drafts/{draft_id}")


# ===================== NAVIGATION VIEWS =====================

@mcp.tool()
def get_navigation_views() -> Dict[str, Any]:
    """Get all navigation views for the current user."""
    return make_request("GET", "/user_settings/navigation_views")


@mcp.tool()
def add_navigation_view(view_name: str, view_data: Dict[str, Any]) -> Dict[str, Any]:
    """Add a navigation view.
    
    Args:
        view_name: Name of view
        view_data: View configuration data
    """
    data = {"view_name": view_name, "view_data": str(view_data)}
    return make_request("POST", "/user_settings/navigation_views", data=data)


@mcp.tool()
def update_navigation_view(
    view_id: int,
    view_name: str | None = None,
    view_data: Dict[str, Any] | None = None
) -> Dict[str, Any]:
    """Update a navigation view.
    
    Args:
        view_id: ID of view to update
        view_name: New name
        view_data: New configuration data
    """
    data = {}
    if view_name:
        data["view_name"] = view_name
    if view_data:
        data["view_data"] = str(view_data)
    
    return make_request("PATCH", f"/user_settings/navigation_views/{view_id}", data=data)


@mcp.tool()
def remove_navigation_view(view_id: int) -> Dict[str, Any]:
    """Remove a navigation view.
    
    Args:
        view_id: ID of view to remove
    """
    return make_request("DELETE", f"/user_settings/navigation_views/{view_id}")


# ===================== FILE OPERATIONS =====================

@mcp.tool()
def get_temporary_file_url(attachment_id: int) -> Dict[str, Any]:
    """Get a temporary URL for an attachment.
    
    Args:
        attachment_id: ID of attachment
    """
    return make_request("GET", f"/user_uploads/{attachment_id}/temporary")


@mcp.tool()
def get_attachments() -> Dict[str, Any]:
    """Get all attachments for the current user."""
    return make_request("GET", "/user_uploads")


@mcp.tool()
def render_message(content: str) -> Dict[str, Any]:
    """Render message content to HTML.
    
    Args:
        content: Raw message content to render
    """
    data = {"content": content}
    return make_request("POST", "/render_message", data=data)


# ===================== SERVER & ORGANIZATION =====================

@mcp.tool()
def get_server_settings() -> Dict[str, Any]:
    """Get server settings."""
    return make_request("GET", "/server_settings")


@mcp.tool()
def get_alert_words() -> Dict[str, Any]:
    """Get alert words for the current user."""
    return make_request("GET", "/alert_words")


@mcp.tool()
def add_alert_words(words: List[str]) -> Dict[str, Any]:
    """Add alert words.
    
    Args:
        words: List of words to add
    """
    import json
    data = {"alert_words": json.dumps(words)}
    return make_request("POST", "/alert_words", data=data)


@mcp.tool()
def remove_alert_words(words: List[str]) -> Dict[str, Any]:
    """Remove alert words.
    
    Args:
        words: List of words to remove
    """
    import json
    data = {"alert_words": json.dumps(words)}
    return make_request("DELETE", "/alert_words", data=data)


@mcp.tool()
def get_linkifiers() -> Dict[str, Any]:
    """Get linkifiers for the organization."""
    return make_request("GET", "/realm/linkifiers")


@mcp.tool()
def add_linkifier(pattern: str, url_template: str) -> Dict[str, Any]:
    """Add a linkifier.
    
    Args:
        pattern: Regex pattern to match
        url_template: URL template with match groups
    """
    data = {
        "pattern": pattern,
        "url_template": url_template,
    }
    return make_request("POST", "/realm/linkifiers", data=data)


@mcp.tool()
def update_linkifier(linkifier_id: int, 
                     pattern: str | None = None,
                     url_template: str | None = None) -> Dict[str, Any]:
    """Update a linkifier.
    
    Args:
        linkifier_id: ID of linkifier to update
        pattern: New regex pattern
        url_template: New URL template
    """
    data = {}
    if pattern:
        data["pattern"] = pattern
    if url_template:
        data["url_template"] = url_template
    
    return make_request("PATCH", f"/realm/linkifiers/{linkifier_id}", data=data)


@mcp.tool()
def remove_linkifier(linkifier_id: int) -> Dict[str, Any]:
    """Remove a linkifier.
    
    Args:
        linkifier_id: ID of linkifier to remove
    """
    return make_request("DELETE", f"/realm/linkifiers/{linkifier_id}")


@mcp.tool()
def reorder_linkifiers(linkifier_ids: List[int]) -> Dict[str, Any]:
    """Reorder linkifiers.
    
    Args:
        linkifier_ids: New order of linkifier IDs
    """
    import json
    data = {"linkifier_ids": json.dumps(linkifier_ids)}
    return make_request("PATCH", "/realm/linkifiers", data=data)


@mcp.tool()
def get_custom_emoji() -> Dict[str, Any]:
    """Get custom emoji for the organization."""
    return make_request("GET", "/emoji")


@mcp.tool()
def upload_custom_emoji(emoji_name: str, file_path: str) -> Dict[str, Any]:
    """Upload a custom emoji.
    
    Args:
        emoji_name: Name of emoji
        file_path: Path to image file
    """
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            return make_request("POST", f"/emoji/{emoji_name}", data={}, files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def deactivate_custom_emoji(emoji_id: int) -> Dict[str, Any]:
    """Deactivate a custom emoji.
    
    Args:
        emoji_id: ID of custom emoji to deactivate
    """
    return make_request("DELETE", f"/emoji/{emoji_id}")


@mcp.tool()
def get_custom_profile_fields() -> Dict[str, Any]:
    """Get custom profile fields for the organization."""
    return make_request("GET", "/realm/profile_fields")


@mcp.tool()
def create_custom_profile_field(
    name: str,
    type: int,
    hint: str | None = None,
    field_data: Dict[str, Any] | None = None
) -> Dict[str, Any]:
    """Create a custom profile field.
    
    Args:
        name: Field name
        type: Field type (1=Text, 2=Choice, 3=External account, etc.)
        hint: Optional field hint
        field_data: Optional field-specific data
    """
    data = {
        "name": name,
        "type": str(type),
    }
    if hint:
        data["hint"] = hint
    if field_data:
        import json
        data["field_data"] = json.dumps(field_data)
    
    return make_request("POST", "/realm/profile_fields", data=data)


@mcp.tool()
def update_custom_profile_field(
    field_id: int,
    name: str | None = None,
    hint: str | None = None,
    field_data: Dict[str, Any] | None = None
) -> Dict[str, Any]:
    """Update a custom profile field.
    
    Args:
        field_id: ID of field to update
        name: New name
        hint: New hint
        field_data: New field-specific data
    """
    data = {}
    if name:
        data["name"] = name
    if hint:
        data["hint"] = hint
    if field_data:
        import json
        data["field_data"] = json.dumps(field_data)
    
    return make_request("PATCH", f"/realm/profile_fields/{field_id}", data=data)


@mcp.tool()
def reorder_custom_profile_fields(field_ids: List[int]) -> Dict[str, Any]:
    """Reorder custom profile fields.
    
    Args:
        field_ids: New order of field IDs
    """
    import json
    data = {"field_ids": json.dumps(field_ids)}
    return make_request("PATCH", "/realm/profile_fields", data=data)


@mcp.tool()
def delete_custom_profile_field(field_id: int) -> Dict[str, Any]:
    """Delete a custom profile field.
    
    Args:
        field_id: ID of field to delete
    """
    return make_request("DELETE", f"/realm/profile_fields/{field_id}")


@mcp.tool()
def get_saved_snippets() -> Dict[str, Any]:
    """Get saved snippets for the current user."""
    return make_request("GET", "/saved_snippets")


@mcp.tool()
def create_saved_snippet(
    title: str,
    content: str,
    icon: str | None = None,
    url: str | None = None
) -> Dict[str, Any]:
    """Create a saved snippet.
    
    Args:
        title: Snippet title
        content: Snippet content
        icon: Optional icon name
        url: Optional URL for snippet
    """
    data = {
        "title": title,
        "content": content,
    }
    if icon:
        data["icon"] = icon
    if url:
        data["url"] = url
    
    return make_request("POST", "/saved_snippets", data=data)


@mcp.tool()
def update_saved_snippet(
    snippet_id: int,
    title: str | None = None,
    content: str | None = None,
    icon: str | None = None,
    url: str | None = None
) -> Dict[str, Any]:
    """Update a saved snippet.
    
    Args:
        snippet_id: ID of snippet to update
        title: New title
        content: New content
        icon: New icon
        url: New URL
    """
    data = {}
    if title:
        data["title"] = title
    if content:
        data["content"] = content
    if icon:
        data["icon"] = icon
    if url:
        data["url"] = url
    
    return make_request("PATCH", f"/saved_snippets/{snippet_id}", data=data)


@mcp.tool()
def delete_saved_snippet(snippet_id: int) -> Dict[str, Any]:
    """Delete a saved snippet.
    
    Args:
        snippet_id: ID of snippet to delete
    """
    return make_request("DELETE", f"/saved_snippets/{snippet_id}")


# ===================== PRESENCE =====================

@mcp.tool()
def update_presence(status: str, active: bool = True) -> Dict[str, Any]:
    """Update your presence status.
    
    Args:
        status: Status ("active", "idle", "offline")
        active: Whether user is active
    """
    data = {
        "status": status,
        "active": str(active).lower(),
    }
    return make_request("POST", "/users/me/presence", data=data)


@mcp.tool()
def get_presence() -> Dict[str, Any]:
    """Get presence information for all users."""
    return make_request("GET", "/users/presences")


# ===================== SETTINGS =====================

@mcp.tool()
def update_settings(
    full_name: str | None = None,
    email: str | None = None,
    timezone: str | None = None,
    default_language: str | None = None,
    web_refresh_interval: int | None = None,
    demote_inactive_streams: str | None = None,
    notification_settings_null: bool | None = None
) -> Dict[str, Any]:
    """Update user settings.
    
    Args:
        full_name: New full name
        email: New email address
        timezone: New timezone
        default_language: New default language
        web_refresh_interval: New refresh interval
        demote_inactive_streams: Demote inactive streams setting
        notification_settings_null: Whether to reset notification settings
    """
    data = {}
    if full_name:
        data["full_name"] = full_name
    if email:
        data["email"] = email
    if timezone:
        data["timezone"] = timezone
    if default_language:
        data["default_language"] = default_language
    if web_refresh_interval:
        data["web_refresh_interval"] = str(web_refresh_interval)
    if demote_inactive_streams:
        data["demote_inactive_streams"] = demote_inactive_streams
    if notification_settings_null is not None:
        data["notification_settings_null"] = str(notification_settings_null).lower()
    
    return make_request("PATCH", "/settings", data=data)


@mcp.tool()
def update_realm_user_settings_defaults(
    default_language: str | None = None,
    enable_spam_checking: bool | None = None,
    default_twenty_four_hour_time: bool | None = None
) -> Dict[str, Any]:
    """Update realm-level user settings defaults (admin only).
    
    Args:
        default_language: New default language
        enable_spam_checking: Whether to enable spam checking
        default_twenty_four_hour_time: Whether to use 24-hour time by default
    """
    data = {}
    if default_language:
        data["default_language"] = default_language
    if enable_spam_checking is not None:
        data["enable_spam_checking"] = str(enable_spam_checking).lower()
    if default_twenty_four_hour_time is not None:
        data["default_twenty_four_hour_time"] = str(default_twenty_four_hour_time).lower()
    
    return make_request("PATCH", "/settings/default", data=data)


@mcp.tool()
def get_user_channels(user_id: int) -> Dict[str, Any]:
    """Get channels a user is subscribed to.
    
    Args:
        user_id: ID of user
    """
    return make_request("GET", f"/users/{user_id}/subscriptions")


# ===================== REGISTRATION =====================

@mcp.tool()
def register_client() -> Dict[str, Any]:
    """Register a client for real-time events."""
    return make_request("POST", "/register")


@mcp.tool()
def get_events(queue_id: str) -> Dict[str, Any]:
    """Get events from a client queue.
    
    Args:
        queue_id: ID of event queue
    """
    return make_request("GET", f"/events?queue_id={queue_id}")


@mcp.tool()
def delete_event_queue(queue_id: str) -> Dict[str, Any]:
    """Delete a client event queue.
    
    Args:
        queue_id: ID of event queue to delete
    """
    return make_request("DELETE", f"/events?queue_id={queue_id}")


# ===================== REPORTING =====================

@mcp.tool()
def report_message(message_id: int, reason: str | None = None) -> Dict[str, Any]:
    """Report a message to moderators.
    
    Args:
        message_id: ID of message to report
        reason: Optional reason for reporting
    """
    data = {"message_id": str(message_id)}
    if reason:
        data["reason"] = reason
    
    return make_request("POST", "/messages/report", data=data)


if __name__ == "__main__":
    # Validate configuration
    if not ZULIP_EMAIL or not ZULIP_API_KEY or not ZULIP_SITE:
        print("Error: ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set")
        exit(1)
    
    # Run the MCP server
    mcp.run()
