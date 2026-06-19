#!/usr/bin/env python3
"""
Zulip REST API MCP Server

This server provides comprehensive access to the Zulip REST API through MCP tools.
Authentication uses HTTP Basic Auth with ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables.
"""

import os
import json
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
server = FastMCP("zulip-api")

# Configuration from environment variables
ZULIP_EMAIL = os.getenv("ZULIP_EMAIL", "")
ZULIP_API_KEY = os.getenv("ZULIP_API_KEY", "")
ZULIP_SITE = os.getenv("ZULIP_SITE", "")

if not all([ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE]):
    raise ValueError("Missing required environment variables: ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE")

BASE_URL = f"{ZULIP_SITE}/api/v1"
AUTH = (ZULIP_EMAIL, ZULIP_API_KEY)


def make_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Make an HTTP request to the Zulip API.
    
    Args:
        method: HTTP method (GET, POST, PATCH, DELETE, PUT)
        endpoint: API endpoint path (without /api/v1 prefix)
        params: Query parameters
        data: Form data
        json_data: JSON body data
    
    Returns:
        Response JSON as dict, or error dict if request fails
    """
    url = f"{BASE_URL}/{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, params=params, auth=AUTH, timeout=30)
        elif method == "POST":
            response = requests.post(url, params=params, data=data, json=json_data, auth=AUTH, timeout=30)
        elif method == "PATCH":
            response = requests.patch(url, params=params, data=data, json=json_data, auth=AUTH, timeout=30)
        elif method == "PUT":
            response = requests.put(url, params=params, data=data, json=json_data, auth=AUTH, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, params=params, auth=AUTH, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ============================================================================
# MESSAGES
# ============================================================================

@server.tool()
def send_message(
    type: str,
    to: str | int | List[int] | List[str],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Send a message to a channel or direct message.
    
    Args:
        type: Message type - "direct", "channel", "channel_name", or "private"
        to: For channel messages: channel name or ID. For direct messages: list of user IDs or emails
        content: Message content
        topic: Topic name (required for channel messages)
        queue_id: Event queue ID for local echo support
        local_id: Local message ID for local echo support
        read_by_sender: Whether message should be marked read by sender
    
    Returns:
        Response with message ID and status
    """
    payload = {
        "type": type,
        "to": to,
        "content": content,
    }
    if topic is not None:
        payload["topic"] = topic
    if queue_id is not None:
        payload["queue_id"] = queue_id
    if local_id is not None:
        payload["local_id"] = local_id
    if read_by_sender is not None:
        payload["read_by_sender"] = read_by_sender
    
    return make_request("POST", "messages", json_data=payload)


@server.tool()
def get_messages(
    start_message_id: str | int = "newest",
    num_before: int = 0,
    num_after: int = 0,
    filter_spec: Optional[List[Dict[str, str]]] = None,
    client_gravatar: bool = True,
    apply_markdown: bool = True,
    message_ids: Optional[List[int]] = None,
    allow_empty_topic_name: bool = False,
    anchor_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Fetch messages from the Zulip server.
    
    Args:
        start_message_id: Message ID to anchor around (or "newest", "oldest", "first_unread", "date")
        num_before: Number of messages before anchor to fetch
        num_after: Number of messages after anchor to fetch
        filter_spec: Filter specification for narrowing messages
        client_gravatar: Whether client supports gravatar computation
        apply_markdown: Whether to return rendered HTML
        message_ids: Specific message IDs to fetch
        allow_empty_topic_name: Whether client supports empty topic names
        anchor_date: Date for anchor when start_message_id is "date"
    
    Returns:
        Messages and metadata
    """
    params = {
        "start_message_id": start_message_id,
        "num_before": num_before,
        "num_after": num_after,
        "client_gravatar": client_gravatar,
        "apply_markdown": apply_markdown,
        "allow_empty_topic_name": allow_empty_topic_name,
    }
    if filter_spec is not None:
        params["filter_spec"] = json.dumps(filter_spec)
    if message_ids is not None:
        params["message_ids"] = json.dumps(message_ids)
    if anchor_date is not None:
        params["anchor_date"] = anchor_date
    
    return make_request("GET", "messages", params=params)


@server.tool()
def get_message(message_id: int) -> Dict[str, Any]:
    """
    Fetch a single message by ID.
    
    Args:
        message_id: The message ID to fetch
    
    Returns:
        Message object
    """
    return make_request("GET", f"messages/{message_id}")


@server.tool()
def edit_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: str = "change_one",
) -> Dict[str, Any]:
    """
    Edit a message.
    
    Args:
        message_id: The message ID to edit
        content: New message content
        topic: New topic name
        propagate_mode: How to propagate topic changes ("change_one", "change_later", "change_all")
    
    Returns:
        Response with status
    """
    payload = {"propagate_mode": propagate_mode}
    if content is not None:
        payload["content"] = content
    if topic is not None:
        payload["topic"] = topic
    
    return make_request("PATCH", f"messages/{message_id}", json_data=payload)


@server.tool()
def delete_message(message_id: int) -> Dict[str, Any]:
    """
    Delete a message.
    
    Args:
        message_id: The message ID to delete
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"messages/{message_id}")


@server.tool()
def get_message_history(message_id: int) -> Dict[str, Any]:
    """
    Get the edit history of a message.
    
    Args:
        message_id: The message ID
    
    Returns:
        Edit history
    """
    return make_request("GET", f"messages/{message_id}/history")


@server.tool()
def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: str = "unicode_emoji",
) -> Dict[str, Any]:
    """
    Add an emoji reaction to a message.
    
    Args:
        message_id: The message ID
        emoji_name: Name of the emoji
        emoji_code: Code of the emoji (optional)
        reaction_type: Type of reaction ("unicode_emoji", "realm_emoji", "zulip_extra_emoji")
    
    Returns:
        Response with status
    """
    payload = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type,
    }
    if emoji_code is not None:
        payload["emoji_code"] = emoji_code
    
    return make_request("POST", f"messages/{message_id}/reactions", json_data=payload)


@server.tool()
def remove_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: str = "unicode_emoji",
) -> Dict[str, Any]:
    """
    Remove an emoji reaction from a message.
    
    Args:
        message_id: The message ID
        emoji_name: Name of the emoji
        emoji_code: Code of the emoji (optional)
        reaction_type: Type of reaction ("unicode_emoji", "realm_emoji", "zulip_extra_emoji")
    
    Returns:
        Response with status
    """
    params = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type,
    }
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    
    return make_request("DELETE", f"messages/{message_id}/reactions", params=params)


@server.tool()
def update_message_flags(
    messages: List[int],
    flag: str,
    op: str = "add",
) -> Dict[str, Any]:
    """
    Update flags on messages.
    
    Args:
        messages: List of message IDs
        flag: Flag to update ("read", "starred", "collapsed", "mentioned")
        op: Operation ("add" or "remove")
    
    Returns:
        Response with status
    """
    payload = {
        "messages": messages,
        "flag": flag,
        "op": op,
    }
    return make_request("POST", "messages/flags", json_data=payload)


@server.tool()
def mark_all_as_read() -> Dict[str, Any]:
    """
    Mark all messages as read for the current user.
    
    Returns:
        Response with status
    """
    return make_request("POST", "messages/flags/all", json_data={"op": "add", "flag": "read"})


@server.tool()
def mark_stream_as_read(stream_id: int) -> Dict[str, Any]:
    """
    Mark all messages in a stream as read.
    
    Args:
        stream_id: The stream/channel ID
    
    Returns:
        Response with status
    """
    payload = {"stream_id": stream_id}
    return make_request("POST", "messages/flags/all", json_data=payload)


@server.tool()
def mark_topic_as_read(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Mark all messages in a topic as read.
    
    Args:
        stream_id: The stream/channel ID
        topic_name: The topic name
    
    Returns:
        Response with status
    """
    payload = {
        "stream_id": stream_id,
        "topic_name": topic_name,
    }
    return make_request("POST", "messages/flags/all", json_data=payload)


@server.tool()
def get_read_receipts(message_id: int) -> Dict[str, Any]:
    """
    Get read receipts for a message.
    
    Args:
        message_id: The message ID
    
    Returns:
        Read receipt information
    """
    return make_request("GET", f"messages/{message_id}/read_receipts")


# ============================================================================
# SCHEDULED MESSAGES
# ============================================================================

@server.tool()
def get_scheduled_messages() -> Dict[str, Any]:
    """
    Get all scheduled messages for the current user.
    
    Returns:
        List of scheduled messages
    """
    return make_request("GET", "scheduled_messages")


@server.tool()
def create_scheduled_message(
    type: str,
    to: str | int | List[int] | List[str],
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a scheduled message.
    
    Args:
        type: Message type ("direct", "channel", "channel_name", or "private")
        to: Recipient (channel name/ID or list of user IDs/emails)
        content: Message content
        scheduled_delivery_timestamp: Unix timestamp for when to send
        topic: Topic name (required for channel messages)
    
    Returns:
        Response with scheduled message ID
    """
    payload = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        payload["topic"] = topic
    
    return make_request("POST", "scheduled_messages", json_data=payload)


@server.tool()
def edit_scheduled_message(
    scheduled_message_id: int,
    type: Optional[str] = None,
    to: Optional[str | int | List[int] | List[str]] = None,
    content: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Edit a scheduled message.
    
    Args:
        scheduled_message_id: The scheduled message ID
        type: Message type
        to: Recipient
        content: Message content
        scheduled_delivery_timestamp: Unix timestamp for when to send
        topic: Topic name
    
    Returns:
        Response with status
    """
    payload = {}
    if type is not None:
        payload["type"] = type
    if to is not None:
        payload["to"] = to
    if content is not None:
        payload["content"] = content
    if scheduled_delivery_timestamp is not None:
        payload["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    if topic is not None:
        payload["topic"] = topic
    
    return make_request("PATCH", f"scheduled_messages/{scheduled_message_id}", json_data=payload)


@server.tool()
def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """
    Delete a scheduled message.
    
    Args:
        scheduled_message_id: The scheduled message ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"scheduled_messages/{scheduled_message_id}")


# ============================================================================
# DRAFTS
# ============================================================================

@server.tool()
def get_drafts() -> Dict[str, Any]:
    """
    Get all drafts for the current user.
    
    Returns:
        List of drafts
    """
    return make_request("GET", "drafts")


@server.tool()
def create_draft(
    type: str,
    to: str | int | List[int] | List[str],
    content: str,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a draft message.
    
    Args:
        type: Message type ("direct", "channel", "channel_name", or "private")
        to: Recipient (channel name/ID or list of user IDs/emails)
        content: Message content
        topic: Topic name (required for channel messages)
    
    Returns:
        Response with draft ID
    """
    payload = {
        "type": type,
        "to": to,
        "content": content,
    }
    if topic is not None:
        payload["topic"] = topic
    
    return make_request("POST", "drafts", json_data=payload)


@server.tool()
def edit_draft(
    draft_id: int,
    type: Optional[str] = None,
    to: Optional[str | int | List[int] | List[str]] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Edit a draft message.
    
    Args:
        draft_id: The draft ID
        type: Message type
        to: Recipient
        content: Message content
        topic: Topic name
    
    Returns:
        Response with status
    """
    payload = {}
    if type is not None:
        payload["type"] = type
    if to is not None:
        payload["to"] = to
    if content is not None:
        payload["content"] = content
    if topic is not None:
        payload["topic"] = topic
    
    return make_request("PATCH", f"drafts/{draft_id}", json_data=payload)


@server.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    """
    Delete a draft message.
    
    Args:
        draft_id: The draft ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"drafts/{draft_id}")


# ============================================================================
# STREAMS/CHANNELS
# ============================================================================

@server.tool()
def get_streams(
    include_public: bool = True,
    include_subscribed: bool = True,
    include_all_public: bool = False,
    include_default: bool = False,
) -> Dict[str, Any]:
    """
    Get all streams/channels.
    
    Args:
        include_public: Include public streams
        include_subscribed: Include subscribed streams
        include_all_public: Include all public streams (requires admin)
        include_default: Include default streams
    
    Returns:
        List of streams
    """
    params = {
        "include_public": include_public,
        "include_subscribed": include_subscribed,
        "include_all_public": include_all_public,
        "include_default": include_default,
    }
    return make_request("GET", "streams", params=params)


@server.tool()
def get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    """
    Get a stream/channel by ID.
    
    Args:
        stream_id: The stream ID
    
    Returns:
        Stream object
    """
    return make_request("GET", f"streams/{stream_id}")


@server.tool()
def get_stream_id(stream: str) -> Dict[str, Any]:
    """
    Get the ID of a stream by name.
    
    Args:
        stream: The stream name
    
    Returns:
        Stream ID
    """
    params = {"stream": stream}
    return make_request("GET", "get_stream_id", params=params)


@server.tool()
def create_stream(
    name: str,
    description: str = "",
    subscribers: Optional[List[int]] = None,
    invite_only: bool = False,
    is_web_public: bool = False,
    is_default_stream: bool = False,
    announce: bool = False,
) -> Dict[str, Any]:
    """
    Create a new stream/channel.
    
    Args:
        name: Stream name
        description: Stream description
        subscribers: List of user IDs to subscribe
        invite_only: Whether stream is private
        is_web_public: Whether stream is web-public
        is_default_stream: Whether stream is default for new users
        announce: Whether to announce creation
    
    Returns:
        Response with stream ID
    """
    payload = {
        "name": name,
        "description": description,
        "invite_only": invite_only,
        "is_web_public": is_web_public,
        "is_default_stream": is_default_stream,
        "announce": announce,
    }
    if subscribers is not None:
        payload["subscribers"] = subscribers
    
    return make_request("POST", "channels/create", json_data=payload)


@server.tool()
def update_stream(
    stream_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Update a stream/channel.
    
    Args:
        stream_id: The stream ID
        name: New stream name
        description: New description
        is_private: Whether to make private
        is_default_stream: Whether to make default
    
    Returns:
        Response with status
    """
    payload = {}
    if name is not None:
        payload["name"] = name
    if description is not None:
        payload["description"] = description
    if is_private is not None:
        payload["is_private"] = is_private
    if is_default_stream is not None:
        payload["is_default_stream"] = is_default_stream
    
    return make_request("PATCH", f"streams/{stream_id}", json_data=payload)


@server.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    """
    Archive a stream/channel.
    
    Args:
        stream_id: The stream ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"streams/{stream_id}")


@server.tool()
def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """
    Get all topics in a stream.
    
    Args:
        stream_id: The stream ID
    
    Returns:
        List of topics
    """
    return make_request("GET", f"streams/{stream_id}/topics")


@server.tool()
def delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Delete a topic from a stream.
    
    Args:
        stream_id: The stream ID
        topic_name: The topic name
    
    Returns:
        Response with status
    """
    params = {"topic_name": topic_name}
    return make_request("DELETE", f"streams/{stream_id}/topics/{topic_name}", params=params)


@server.tool()
def get_subscriptions() -> Dict[str, Any]:
    """
    Get all subscribed streams for the current user.
    
    Returns:
        List of subscriptions
    """
    return make_request("GET", "subscriptions")


@server.tool()
def subscribe(
    subscriptions: List[Dict[str, Any]],
    principals: Optional[List[int]] = None,
    authorization_errors_fatal: bool = True,
) -> Dict[str, Any]:
    """
    Subscribe to streams.
    
    Args:
        subscriptions: List of stream subscription objects with "name" and optional "description"
        principals: List of user IDs to subscribe (admin only)
        authorization_errors_fatal: Whether to fail if any subscription fails
    
    Returns:
        Response with status
    """
    payload = {
        "subscriptions": subscriptions,
        "authorization_errors_fatal": authorization_errors_fatal,
    }
    if principals is not None:
        payload["principals"] = principals
    
    return make_request("POST", "subscriptions", json_data=payload)


@server.tool()
def unsubscribe(streams: List[str]) -> Dict[str, Any]:
    """
    Unsubscribe from streams.
    
    Args:
        streams: List of stream names to unsubscribe from
    
    Returns:
        Response with status
    """
    payload = {"subscriptions": streams}
    return make_request("DELETE", "subscriptions", json_data=payload)


@server.tool()
def get_stream_subscribers(stream_id: int) -> Dict[str, Any]:
    """
    Get subscribers of a stream.
    
    Args:
        stream_id: The stream ID
    
    Returns:
        List of subscriber user IDs
    """
    return make_request("GET", f"streams/{stream_id}/subscribers")


@server.tool()
def mute_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Mute a topic.
    
    Args:
        stream_id: The stream ID
        topic_name: The topic name
    
    Returns:
        Response with status
    """
    payload = {
        "stream_id": stream_id,
        "topic": topic_name,
        "op": "add",
    }
    return make_request("PATCH", "user_topics", json_data=payload)


@server.tool()
def unmute_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Unmute a topic.
    
    Args:
        stream_id: The stream ID
        topic_name: The topic name
    
    Returns:
        Response with status
    """
    payload = {
        "stream_id": stream_id,
        "topic": topic_name,
        "op": "remove",
    }
    return make_request("PATCH", "user_topics", json_data=payload)


# ============================================================================
# USERS
# ============================================================================

@server.tool()
def get_users() -> Dict[str, Any]:
    """
    Get all users in the organization.
    
    Returns:
        List of users
    """
    return make_request("GET", "users")


@server.tool()
def get_user(user_id: int) -> Dict[str, Any]:
    """
    Get a user by ID.
    
    Args:
        user_id: The user ID
    
    Returns:
        User object
    """
    return make_request("GET", f"users/{user_id}")


@server.tool()
def get_user_by_email(email: str) -> Dict[str, Any]:
    """
    Get a user by email address.
    
    Args:
        email: The user's email address
    
    Returns:
        User object
    """
    params = {"email": email}
    return make_request("GET", "users/by_email", params=params)


@server.tool()
def get_own_user() -> Dict[str, Any]:
    """
    Get the current user's profile.
    
    Returns:
        Current user object
    """
    return make_request("GET", "users/me")


@server.tool()
def create_user(
    email: str,
    password: str,
    full_name: str,
    short_name: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new user (admin only).
    
    Args:
        email: User's email address
        password: User's password
        full_name: User's full name
        short_name: User's short name (username)
    
    Returns:
        Response with user ID
    """
    payload = {
        "email": email,
        "password": password,
        "full_name": full_name,
    }
    if short_name is not None:
        payload["short_name"] = short_name
    
    return make_request("POST", "users", json_data=payload)


@server.tool()
def update_user(
    user_id: int,
    full_name: Optional[str] = None,
    email: Optional[str] = None,
    is_admin: Optional[bool] = None,
    is_guest: Optional[bool] = None,
    is_active: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Update a user (admin only).
    
    Args:
        user_id: The user ID
        full_name: New full name
        email: New email address
        is_admin: Whether user is admin
        is_guest: Whether user is guest
        is_active: Whether user is active
    
    Returns:
        Response with status
    """
    payload = {}
    if full_name is not None:
        payload["full_name"] = full_name
    if email is not None:
        payload["email"] = email
    if is_admin is not None:
        payload["is_admin"] = is_admin
    if is_guest is not None:
        payload["is_guest"] = is_guest
    if is_active is not None:
        payload["is_active"] = is_active
    
    return make_request("PATCH", f"users/{user_id}", json_data=payload)


@server.tool()
def deactivate_user(user_id: int) -> Dict[str, Any]:
    """
    Deactivate a user (admin only).
    
    Args:
        user_id: The user ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"users/{user_id}")


@server.tool()
def reactivate_user(user_id: int) -> Dict[str, Any]:
    """
    Reactivate a deactivated user (admin only).
    
    Args:
        user_id: The user ID
    
    Returns:
        Response with status
    """
    payload = {"is_active": True}
    return make_request("PATCH", f"users/{user_id}", json_data=payload)


@server.tool()
def get_user_status(user_id: int) -> Dict[str, Any]:
    """
    Get a user's status.
    
    Args:
        user_id: The user ID
    
    Returns:
        User status object
    """
    return make_request("GET", f"users/{user_id}/status")


@server.tool()
def update_status(
    status_text: Optional[str] = None,
    status_emoji: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update the current user's status.
    
    Args:
        status_text: Status text
        status_emoji: Status emoji name
    
    Returns:
        Response with status
    """
    payload = {}
    if status_text is not None:
        payload["status_text"] = status_text
    if status_emoji is not None:
        payload["status_emoji"] = status_emoji
    
    return make_request("POST", "users/me/status", json_data=payload)


@server.tool()
def get_presence() -> Dict[str, Any]:
    """
    Get presence information for all users.
    
    Returns:
        Presence data for all users
    """
    return make_request("GET", "users/presence")


@server.tool()
def get_user_presence(user_id: int) -> Dict[str, Any]:
    """
    Get presence information for a specific user.
    
    Args:
        user_id: The user ID
    
    Returns:
        User presence data
    """
    return make_request("GET", f"users/{user_id}/presence")


@server.tool()
def update_presence(
    status: str = "active",
    ping_only: bool = False,
) -> Dict[str, Any]:
    """
    Update the current user's presence.
    
    Args:
        status: Presence status ("active" or "idle")
        ping_only: Whether this is just a ping
    
    Returns:
        Response with status
    """
    payload = {
        "status": status,
        "ping_only": ping_only,
    }
    return make_request("POST", "users/me/presence", json_data=payload)


@server.tool()
def mute_user(user_id: int) -> Dict[str, Any]:
    """
    Mute a user.
    
    Args:
        user_id: The user ID to mute
    
    Returns:
        Response with status
    """
    payload = {"muted_user_id": user_id}
    return make_request("POST", "users/me/muted_users", json_data=payload)


@server.tool()
def unmute_user(user_id: int) -> Dict[str, Any]:
    """
    Unmute a user.
    
    Args:
        user_id: The user ID to unmute
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"users/me/muted_users/{user_id}")


# ============================================================================
# USER GROUPS
# ============================================================================

@server.tool()
def get_user_groups() -> Dict[str, Any]:
    """
    Get all user groups.
    
    Returns:
        List of user groups
    """
    return make_request("GET", "user_groups")


@server.tool()
def create_user_group(
    name: str,
    description: str = "",
    members: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """
    Create a new user group.
    
    Args:
        name: Group name
        description: Group description
        members: List of user IDs to add to group
    
    Returns:
        Response with group ID
    """
    payload = {
        "name": name,
        "description": description,
    }
    if members is not None:
        payload["members"] = members
    
    return make_request("POST", "user_groups/create", json_data=payload)


@server.tool()
def update_user_group(
    user_group_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a user group.
    
    Args:
        user_group_id: The group ID
        name: New group name
        description: New description
    
    Returns:
        Response with status
    """
    payload = {}
    if name is not None:
        payload["name"] = name
    if description is not None:
        payload["description"] = description
    
    return make_request("PATCH", f"user_groups/{user_group_id}", json_data=payload)


@server.tool()
def deactivate_user_group(user_group_id: int) -> Dict[str, Any]:
    """
    Deactivate a user group.
    
    Args:
        user_group_id: The group ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"user_groups/{user_group_id}")


@server.tool()
def get_user_group_members(user_group_id: int) -> Dict[str, Any]:
    """
    Get members of a user group.
    
    Args:
        user_group_id: The group ID
    
    Returns:
        List of member user IDs
    """
    return make_request("GET", f"user_groups/{user_group_id}/members")


@server.tool()
def update_user_group_members(
    user_group_id: int,
    add: Optional[List[int]] = None,
    remove: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """
    Update members of a user group.
    
    Args:
        user_group_id: The group ID
        add: List of user IDs to add
        remove: List of user IDs to remove
    
    Returns:
        Response with status
    """
    payload = {}
    if add is not None:
        payload["add"] = add
    if remove is not None:
        payload["remove"] = remove
    
    return make_request("POST", f"user_groups/{user_group_id}/members", json_data=payload)


# ============================================================================
# FILE UPLOADS
# ============================================================================

@server.tool()
def upload_file(file_path: str) -> Dict[str, Any]:
    """
    Upload a file to Zulip.
    
    Args:
        file_path: Path to the file to upload
    
    Returns:
        Response with file URI
    """
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            url = f"{BASE_URL}/user_uploads"
            response = requests.post(url, files=files, auth=AUTH, timeout=30)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}


@server.tool()
def get_attachments() -> Dict[str, Any]:
    """
    Get all attachments uploaded by the current user.
    
    Returns:
        List of attachments
    """
    return make_request("GET", "attachments")


@server.tool()
def delete_attachment(attachment_id: int) -> Dict[str, Any]:
    """
    Delete an attachment.
    
    Args:
        attachment_id: The attachment ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"attachments/{attachment_id}")


# ============================================================================
# SETTINGS
# ============================================================================

@server.tool()
def get_settings() -> Dict[str, Any]:
    """
    Get the current user's settings.
    
    Returns:
        User settings
    """
    return make_request("GET", "settings")


@server.tool()
def update_settings(
    twenty_four_hour_time: Optional[bool] = None,
    dense_mode: Optional[bool] = None,
    starred_message_counts: Optional[bool] = None,
    fluid_layout_width: Optional[bool] = None,
    high_contrast_mode: Optional[bool] = None,
    translate_emoticons: Optional[bool] = None,
    display_emoji_reaction_users: Optional[bool] = None,
    user_display_strategy: Optional[str] = None,
    emoji_alt_code: Optional[bool] = None,
    left_side_userlist: Optional[bool] = None,
    timezone: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update the current user's settings.
    
    Args:
        twenty_four_hour_time: Use 24-hour time format
        dense_mode: Use dense UI mode
        starred_message_counts: Show starred message counts
        fluid_layout_width: Use fluid layout width
        high_contrast_mode: Use high contrast mode
        translate_emoticons: Translate emoticons to emoji
        display_emoji_reaction_users: Display users who reacted
        user_display_strategy: How to display users ("full_name", "username")
        emoji_alt_code: Use emoji alt codes
        left_side_userlist: Show user list on left side
        timezone: User's timezone
    
    Returns:
        Response with status
    """
    payload = {}
    if twenty_four_hour_time is not None:
        payload["twenty_four_hour_time"] = twenty_four_hour_time
    if dense_mode is not None:
        payload["dense_mode"] = dense_mode
    if starred_message_counts is not None:
        payload["starred_message_counts"] = starred_message_counts
    if fluid_layout_width is not None:
        payload["fluid_layout_width"] = fluid_layout_width
    if high_contrast_mode is not None:
        payload["high_contrast_mode"] = high_contrast_mode
    if translate_emoticons is not None:
        payload["translate_emoticons"] = translate_emoticons
    if display_emoji_reaction_users is not None:
        payload["display_emoji_reaction_users"] = display_emoji_reaction_users
    if user_display_strategy is not None:
        payload["user_display_strategy"] = user_display_strategy
    if emoji_alt_code is not None:
        payload["emoji_alt_code"] = emoji_alt_code
    if left_side_userlist is not None:
        payload["left_side_userlist"] = left_side_userlist
    if timezone is not None:
        payload["timezone"] = timezone
    
    return make_request("PATCH", "settings", json_data=payload)


# ============================================================================
# EMOJI AND REACTIONS
# ============================================================================

@server.tool()
def get_custom_emoji() -> Dict[str, Any]:
    """
    Get all custom emoji in the organization.
    
    Returns:
        List of custom emoji
    """
    return make_request("GET", "emoji")


@server.tool()
def upload_custom_emoji(
    emoji_name: str,
    file_path: str,
) -> Dict[str, Any]:
    """
    Upload a custom emoji.
    
    Args:
        emoji_name: Name for the emoji
        file_path: Path to the emoji image file
    
    Returns:
        Response with status
    """
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            url = f"{BASE_URL}/emoji/{emoji_name}"
            response = requests.post(url, files=files, auth=AUTH, timeout=30)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}


@server.tool()
def deactivate_custom_emoji(emoji_name: str) -> Dict[str, Any]:
    """
    Deactivate a custom emoji.
    
    Args:
        emoji_name: Name of the emoji to deactivate
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"emoji/{emoji_name}")


# ============================================================================
# ALERT WORDS
# ============================================================================

@server.tool()
def get_alert_words() -> Dict[str, Any]:
    """
    Get all alert words for the current user.
    
    Returns:
        List of alert words
    """
    return make_request("GET", "user_alert_words")


@server.tool()
def add_alert_words(alert_words: List[str]) -> Dict[str, Any]:
    """
    Add alert words for the current user.
    
    Args:
        alert_words: List of words to add as alert words
    
    Returns:
        Response with status
    """
    payload = {"alert_words": alert_words}
    return make_request("POST", "user_alert_words", json_data=payload)


@server.tool()
def remove_alert_words(alert_words: List[str]) -> Dict[str, Any]:
    """
    Remove alert words for the current user.
    
    Args:
        alert_words: List of words to remove from alert words
    
    Returns:
        Response with status
    """
    payload = {"alert_words": alert_words}
    return make_request("DELETE", "user_alert_words", json_data=payload)


# ============================================================================
# SERVER AND ORGANIZATION
# ============================================================================

@server.tool()
def get_server_settings() -> Dict[str, Any]:
    """
    Get server settings (no authentication required).
    
    Returns:
        Server settings
    """
    url = f"{ZULIP_SITE}/api/v1/server_settings"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@server.tool()
def get_linkifiers() -> Dict[str, Any]:
    """
    Get all linkifiers in the organization.
    
    Returns:
        List of linkifiers
    """
    return make_request("GET", "realm/linkifiers")


@server.tool()
def add_linkifier(
    pattern: str,
    url_template: str,
) -> Dict[str, Any]:
    """
    Add a linkifier to the organization.
    
    Args:
        pattern: Regex pattern to match
        url_template: URL template for replacement
    
    Returns:
        Response with linkifier ID
    """
    payload = {
        "pattern": pattern,
        "url_template": url_template,
    }
    return make_request("POST", "realm/linkifiers", json_data=payload)


@server.tool()
def update_linkifier(
    linkifier_id: int,
    pattern: Optional[str] = None,
    url_template: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a linkifier.
    
    Args:
        linkifier_id: The linkifier ID
        pattern: New regex pattern
        url_template: New URL template
    
    Returns:
        Response with status
    """
    payload = {}
    if pattern is not None:
        payload["pattern"] = pattern
    if url_template is not None:
        payload["url_template"] = url_template
    
    return make_request("PATCH", f"realm/linkifiers/{linkifier_id}", json_data=payload)


@server.tool()
def remove_linkifier(linkifier_id: int) -> Dict[str, Any]:
    """
    Remove a linkifier.
    
    Args:
        linkifier_id: The linkifier ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"realm/linkifiers/{linkifier_id}")


@server.tool()
def get_custom_profile_fields() -> Dict[str, Any]:
    """
    Get all custom profile fields in the organization.
    
    Returns:
        List of custom profile fields
    """
    return make_request("GET", "custom_profile_fields")


@server.tool()
def create_custom_profile_field(
    type: int,
    name: str,
    hint: Optional[str] = None,
    field_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Create a custom profile field.
    
    Args:
        type: Field type (1=text, 2=number, 3=date, 4=select, 5=user, 6=external_account)
        name: Field name
        hint: Help text for the field
        field_data: Additional field data (e.g., options for select fields)
    
    Returns:
        Response with field ID
    """
    payload = {
        "type": type,
        "name": name,
    }
    if hint is not None:
        payload["hint"] = hint
    if field_data is not None:
        payload["field_data"] = field_data
    
    return make_request("POST", "custom_profile_fields", json_data=payload)


# ============================================================================
# INVITATIONS
# ============================================================================

@server.tool()
def get_invites() -> Dict[str, Any]:
    """
    Get all pending invitations.
    
    Returns:
        List of invitations
    """
    return make_request("GET", "invites")


@server.tool()
def send_invites(
    invitees: List[Dict[str, str]],
    invite_expires_days: int = 30,
) -> Dict[str, Any]:
    """
    Send invitations to users.
    
    Args:
        invitees: List of dicts with "email" and optional "custom_profile_field_*" keys
        invite_expires_days: Days until invitation expires
    
    Returns:
        Response with status
    """
    payload = {
        "invitees": invitees,
        "invite_expires_days": invite_expires_days,
    }
    return make_request("POST", "invites", json_data=payload)


@server.tool()
def create_invite_link(
    num_use: int = 1,
    invite_expires_days: int = 30,
) -> Dict[str, Any]:
    """
    Create a reusable invitation link.
    
    Args:
        num_use: Number of times the link can be used
        invite_expires_days: Days until link expires
    
    Returns:
        Response with invitation link
    """
    payload = {
        "num_use": num_use,
        "invite_expires_days": invite_expires_days,
    }
    return make_request("POST", "invites/link", json_data=payload)


@server.tool()
def revoke_invite_link(invite_link_id: int) -> Dict[str, Any]:
    """
    Revoke an invitation link.
    
    Args:
        invite_link_id: The invitation link ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"invites/link/{invite_link_id}")


# ============================================================================
# MESSAGE REMINDERS
# ============================================================================

@server.tool()
def get_reminders() -> Dict[str, Any]:
    """
    Get all message reminders for the current user.
    
    Returns:
        List of reminders
    """
    return make_request("GET", "reminders")


@server.tool()
def create_reminder(
    message_id: int,
    reminder_timestamp: int,
) -> Dict[str, Any]:
    """
    Create a message reminder.
    
    Args:
        message_id: The message ID to remind about
        reminder_timestamp: Unix timestamp for when to remind
    
    Returns:
        Response with reminder ID
    """
    payload = {
        "message_id": message_id,
        "reminder_timestamp": reminder_timestamp,
    }
    return make_request("POST", "reminders", json_data=payload)


@server.tool()
def delete_reminder(reminder_id: int) -> Dict[str, Any]:
    """
    Delete a message reminder.
    
    Args:
        reminder_id: The reminder ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"reminders/{reminder_id}")


# ============================================================================
# SAVED SNIPPETS
# ============================================================================

@server.tool()
def get_saved_snippets() -> Dict[str, Any]:
    """
    Get all saved snippets for the current user.
    
    Returns:
        List of saved snippets
    """
    return make_request("GET", "saved_snippets")


@server.tool()
def create_saved_snippet(
    title: str,
    content: str,
) -> Dict[str, Any]:
    """
    Create a saved snippet.
    
    Args:
        title: Snippet title
        content: Snippet content
    
    Returns:
        Response with snippet ID
    """
    payload = {
        "title": title,
        "content": content,
    }
    return make_request("POST", "saved_snippets", json_data=payload)


@server.tool()
def edit_saved_snippet(
    snippet_id: int,
    title: Optional[str] = None,
    content: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Edit a saved snippet.
    
    Args:
        snippet_id: The snippet ID
        title: New title
        content: New content
    
    Returns:
        Response with status
    """
    payload = {}
    if title is not None:
        payload["title"] = title
    if content is not None:
        payload["content"] = content
    
    return make_request("PATCH", f"saved_snippets/{snippet_id}", json_data=payload)


@server.tool()
def delete_saved_snippet(snippet_id: int) -> Dict[str, Any]:
    """
    Delete a saved snippet.
    
    Args:
        snippet_id: The snippet ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"saved_snippets/{snippet_id}")


# ============================================================================
# API KEYS
# ============================================================================

@server.tool()
def regenerate_api_key() -> Dict[str, Any]:
    """
    Regenerate the current user's API key.
    
    Returns:
        Response with new API key
    """
    return make_request("POST", "user_me/api_key/regenerate")


@server.tool()
def get_bot_api_key(bot_id: int) -> Dict[str, Any]:
    """
    Get a bot's API key.
    
    Args:
        bot_id: The bot user ID
    
    Returns:
        Bot's API key
    """
    return make_request("GET", f"bots/{bot_id}/api_key")


@server.tool()
def regenerate_bot_api_key(bot_id: int) -> Dict[str, Any]:
    """
    Regenerate a bot's API key.
    
    Args:
        bot_id: The bot user ID
    
    Returns:
        Response with new API key
    """
    return make_request("POST", f"bots/{bot_id}/api_key/regenerate")


# ============================================================================
# ADDITIONAL MESSAGE OPERATIONS
# ============================================================================

@server.tool()
def render_message(content: str) -> Dict[str, Any]:
    """
    Render a message to HTML.
    
    Args:
        content: The message content to render
    
    Returns:
        Rendered HTML
    """
    payload = {"content": content}
    return make_request("POST", "messages/render", json_data=payload)


@server.tool()
def check_messages_match_narrow(
    message_ids: List[int],
    filter_spec: List[Dict[str, str]],
) -> Dict[str, Any]:
    """
    Check if messages match a narrow/filter.
    
    Args:
        message_ids: List of message IDs to check
        filter_spec: Filter specification to check against
    
    Returns:
        List of booleans indicating which messages match
    """
    payload = {
        "message_ids": message_ids,
        "filter_spec": filter_spec,
    }
    return make_request("GET", "messages/matches_narrow", params=payload)


@server.tool()
def update_message_flags_for_narrow(
    filter_spec: List[Dict[str, str]],
    flag: str,
    op: str = "add",
) -> Dict[str, Any]:
    """
    Update flags on messages matching a narrow.
    
    Args:
        filter_spec: Filter specification for messages to update
        flag: Flag to update ("read", "starred", "collapsed", "mentioned")
        op: Operation ("add" or "remove")
    
    Returns:
        Response with status
    """
    payload = {
        "filter_spec": filter_spec,
        "flag": flag,
        "op": op,
    }
    return make_request("POST", "messages/flags", json_data=payload)


# ============================================================================
# SUBSCRIPTION MANAGEMENT
# ============================================================================

@server.tool()
def get_subscription_status(stream: str) -> Dict[str, Any]:
    """
    Check if the current user is subscribed to a stream.
    
    Args:
        stream: The stream name
    
    Returns:
        Subscription status
    """
    params = {"stream": stream}
    return make_request("GET", "subscriptions/exists", params=params)


@server.tool()
def update_subscription_property(
    stream_id: int,
    property: str,
    value: Any,
) -> Dict[str, Any]:
    """
    Update a subscription property.
    
    Args:
        stream_id: The stream ID
        property: Property to update (e.g., "is_muted", "pin_to_top", "color")
        value: New value for the property
    
    Returns:
        Response with status
    """
    payload = {
        "stream_id": stream_id,
        "property": property,
        "value": value,
    }
    return make_request("POST", "user_topics", json_data=payload)


# ============================================================================
# TYPING STATUS
# ============================================================================

@server.tool()
def set_typing_status(
    type: str,
    to: str | int | List[int] | List[str],
    op: str = "start",
) -> Dict[str, Any]:
    """
    Set typing status for a message.
    
    Args:
        type: Message type ("direct" or "channel")
        to: Recipient (channel name/ID or list of user IDs/emails)
        op: Operation ("start" or "stop")
    
    Returns:
        Response with status
    """
    payload = {
        "type": type,
        "to": to,
        "op": op,
    }
    return make_request("POST", "typing", json_data=payload)


# ============================================================================
# CHANNEL FOLDERS
# ============================================================================

@server.tool()
def get_channel_folders() -> Dict[str, Any]:
    """
    Get all channel folders for the current user.
    
    Returns:
        List of channel folders
    """
    return make_request("GET", "user_topic_objects")


@server.tool()
def create_channel_folder(
    name: str,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a channel folder.
    
    Args:
        name: Folder name
        description: Folder description
    
    Returns:
        Response with folder ID
    """
    payload = {"name": name}
    if description is not None:
        payload["description"] = description
    
    return make_request("POST", "user_topic_objects", json_data=payload)


@server.tool()
def update_channel_folder(
    folder_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a channel folder.
    
    Args:
        folder_id: The folder ID
        name: New folder name
        description: New description
    
    Returns:
        Response with status
    """
    payload = {}
    if name is not None:
        payload["name"] = name
    if description is not None:
        payload["description"] = description
    
    return make_request("PATCH", f"user_topic_objects/{folder_id}", json_data=payload)


# ============================================================================
# REPORT MESSAGE
# ============================================================================

@server.tool()
def report_message(message_id: int) -> Dict[str, Any]:
    """
    Report a message to moderators.
    
    Args:
        message_id: The message ID to report
    
    Returns:
        Response with status
    """
    return make_request("POST", f"messages/{message_id}/report")


# ============================================================================
# DEACTIVATE OWN USER
# ============================================================================

@server.tool()
def deactivate_own_user() -> Dict[str, Any]:
    """
    Deactivate the current user's account.
    
    Returns:
        Response with status
    """
    return make_request("DELETE", "users/me")


# ============================================================================
# GET FILE TEMPORARY URL
# ============================================================================

@server.tool()
def get_file_temporary_url(file_path_id: str) -> Dict[str, Any]:
    """
    Get a temporary URL for an uploaded file.
    
    Args:
        file_path_id: The file path ID from an attachment
    
    Returns:
        Temporary URL for the file
    """
    params = {"file_path_id": file_path_id}
    return make_request("GET", "user_uploads", params=params)


# ============================================================================
# USER CHANNELS
# ============================================================================

@server.tool()
def get_user_channels(user_id: int) -> Dict[str, Any]:
    """
    Get all channels a user is subscribed to.
    
    Args:
        user_id: The user ID
    
    Returns:
        List of subscribed channel IDs
    """
    return make_request("GET", f"users/{user_id}/channels")


# ============================================================================
# USER GROUP SUBGROUPS
# ============================================================================

@server.tool()
def get_user_group_subgroups(user_group_id: int) -> Dict[str, Any]:
    """
    Get subgroups of a user group.
    
    Args:
        user_group_id: The group ID
    
    Returns:
        List of subgroup IDs
    """
    return make_request("GET", f"user_groups/{user_group_id}/subgroups")


@server.tool()
def update_user_group_subgroups(
    user_group_id: int,
    add: Optional[List[int]] = None,
    remove: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """
    Update subgroups of a user group.
    
    Args:
        user_group_id: The group ID
        add: List of subgroup IDs to add
        remove: List of subgroup IDs to remove
    
    Returns:
        Response with status
    """
    payload = {}
    if add is not None:
        payload["add"] = add
    if remove is not None:
        payload["remove"] = remove
    
    return make_request("POST", f"user_groups/{user_group_id}/subgroups", json_data=payload)


@server.tool()
def get_user_group_membership_status(
    user_group_id: int,
    user_id: int,
) -> Dict[str, Any]:
    """
    Check if a user is a member of a group.
    
    Args:
        user_group_id: The group ID
        user_id: The user ID
    
    Returns:
        Membership status
    """
    return make_request("GET", f"user_groups/{user_group_id}/members/{user_id}")


# ============================================================================
# UPDATE USER BY EMAIL
# ============================================================================

@server.tool()
def update_user_by_email(
    email: str,
    full_name: Optional[str] = None,
    is_admin: Optional[bool] = None,
    is_guest: Optional[bool] = None,
    is_active: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Update a user by email address.
    
    Args:
        email: The user's email address
        full_name: New full name
        is_admin: Whether user is admin
        is_guest: Whether user is guest
        is_active: Whether user is active
    
    Returns:
        Response with status
    """
    payload = {}
    if full_name is not None:
        payload["full_name"] = full_name
    if is_admin is not None:
        payload["is_admin"] = is_admin
    if is_guest is not None:
        payload["is_guest"] = is_guest
    if is_active is not None:
        payload["is_active"] = is_active
    
    return make_request("PATCH", f"users/{email}", json_data=payload)


# ============================================================================
# UPDATE USER TOPIC
# ============================================================================

@server.tool()
def update_user_topic(
    stream_id: int,
    topic_name: str,
    visibility_policy: int,
) -> Dict[str, Any]:
    """
    Update visibility policy for a topic.
    
    Args:
        stream_id: The stream ID
        topic_name: The topic name
        visibility_policy: Visibility policy (0=inherit, 1=muted, 2=unmuted, 3=followed)
    
    Returns:
        Response with status
    """
    payload = {
        "stream_id": stream_id,
        "topic": topic_name,
        "visibility_policy": visibility_policy,
    }
    return make_request("PATCH", "user_topics", json_data=payload)


# ============================================================================
# ADD/REMOVE DEFAULT STREAMS
# ============================================================================

@server.tool()
def add_default_stream(stream_id: int) -> Dict[str, Any]:
    """
    Add a stream as a default stream for new users.
    
    Args:
        stream_id: The stream ID
    
    Returns:
        Response with status
    """
    payload = {"stream_id": stream_id}
    return make_request("POST", "default_streams", json_data=payload)


@server.tool()
def remove_default_stream(stream_id: int) -> Dict[str, Any]:
    """
    Remove a stream as a default stream for new users.
    
    Args:
        stream_id: The stream ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"default_streams/{stream_id}")


# ============================================================================
# STREAM EMAIL ADDRESS
# ============================================================================

@server.tool()
def get_stream_email_address(stream_id: int) -> Dict[str, Any]:
    """
    Get the email address for posting to a stream.
    
    Args:
        stream_id: The stream ID
    
    Returns:
        Email address for the stream
    """
    return make_request("GET", f"streams/{stream_id}/email_address")


# ============================================================================
# TYPING STATUS FOR MESSAGE EDITING
# ============================================================================

@server.tool()
def set_typing_status_for_message_edit(
    message_id: int,
    op: str = "start",
) -> Dict[str, Any]:
    """
    Set typing status while editing a message.
    
    Args:
        message_id: The message ID being edited
        op: Operation ("start" or "stop")
    
    Returns:
        Response with status
    """
    payload = {"op": op}
    return make_request("POST", f"messages/{message_id}/typing", json_data=payload)


# ============================================================================
# RESEND EMAIL INVITE
# ============================================================================

@server.tool()
def resend_email_invite(email: str) -> Dict[str, Any]:
    """
    Resend an email invitation.
    
    Args:
        email: Email address to resend invitation to
    
    Returns:
        Response with status
    """
    payload = {"email": email}
    return make_request("POST", "invites/send/email", json_data=payload)


# ============================================================================
# REVOKE EMAIL INVITE
# ============================================================================

@server.tool()
def revoke_email_invite(email: str) -> Dict[str, Any]:
    """
    Revoke an email invitation.
    
    Args:
        email: Email address of the invitation to revoke
    
    Returns:
        Response with status
    """
    payload = {"email": email}
    return make_request("DELETE", "invites/send/email", json_data=payload)


# ============================================================================
# REORDER LINKIFIERS
# ============================================================================

@server.tool()
def reorder_linkifiers(ordered_linkifier_ids: List[int]) -> Dict[str, Any]:
    """
    Reorder linkifiers.
    
    Args:
        ordered_linkifier_ids: List of linkifier IDs in desired order
    
    Returns:
        Response with status
    """
    payload = {"ordered_linkifier_ids": ordered_linkifier_ids}
    return make_request("PATCH", "realm/linkifiers", json_data=payload)


# ============================================================================
# REORDER CUSTOM PROFILE FIELDS
# ============================================================================

@server.tool()
def reorder_custom_profile_fields(order: List[int]) -> Dict[str, Any]:
    """
    Reorder custom profile fields.
    
    Args:
        order: List of field IDs in desired order
    
    Returns:
        Response with status
    """
    payload = {"order": order}
    return make_request("PATCH", "custom_profile_fields", json_data=payload)


# ============================================================================
# CODE PLAYGROUNDS
# ============================================================================

@server.tool()
def add_code_playground(
    name: str,
    pygments_language: str,
    url_template: str,
) -> Dict[str, Any]:
    """
    Add a code playground.
    
    Args:
        name: Name of the playground
        pygments_language: Pygments language identifier
        url_template: URL template for the playground
    
    Returns:
        Response with playground ID
    """
    payload = {
        "name": name,
        "pygments_language": pygments_language,
        "url_template": url_template,
    }
    return make_request("POST", "realm/code_playgrounds", json_data=payload)


@server.tool()
def remove_code_playground(playground_id: int) -> Dict[str, Any]:
    """
    Remove a code playground.
    
    Args:
        playground_id: The playground ID
    
    Returns:
        Response with status
    """
    return make_request("DELETE", f"realm/code_playgrounds/{playground_id}")


# ============================================================================
# BULK SUBSCRIPTION SETTINGS
# ============================================================================

@server.tool()
def update_subscription_settings(
    stream_id: int,
    is_muted: Optional[bool] = None,
    pin_to_top: Optional[bool] = None,
    color: Optional[str] = None,
    desktop_notifications: Optional[bool] = None,
    email_notifications: Optional[bool] = None,
    push_notifications: Optional[bool] = None,
    audible_notifications: Optional[bool] = None,
    wildcard_mentions_notify: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Update subscription settings for a stream.
    
    Args:
        stream_id: The stream ID
        is_muted: Whether to mute the stream
        pin_to_top: Whether to pin stream to top
        color: Stream color (hex code)
        desktop_notifications: Enable desktop notifications
        email_notifications: Enable email notifications
        push_notifications: Enable push notifications
        audible_notifications: Enable audible notifications
        wildcard_mentions_notify: Notify on wildcard mentions
    
    Returns:
        Response with status
    """
    payload = {"stream_id": stream_id}
    if is_muted is not None:
        payload["is_muted"] = is_muted
    if pin_to_top is not None:
        payload["pin_to_top"] = pin_to_top
    if color is not None:
        payload["color"] = color
    if desktop_notifications is not None:
        payload["desktop_notifications"] = desktop_notifications
    if email_notifications is not None:
        payload["email_notifications"] = email_notifications
    if push_notifications is not None:
        payload["push_notifications"] = push_notifications
    if audible_notifications is not None:
        payload["audible_notifications"] = audible_notifications
    if wildcard_mentions_notify is not None:
        payload["wildcard_mentions_notify"] = wildcard_mentions_notify
    
    return make_request("POST", "user_subscription_settings", json_data=payload)


if __name__ == "__main__":
    server.run(transport="stdio")
