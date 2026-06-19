#!/usr/bin/env python3
"""
MCP Server for Zulip REST API
Provides tools for interacting with Zulip messaging platform
"""

import os
import json
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("zulip-mcp")

# Configuration from environment
ZULIP_EMAIL = os.getenv("ZULIP_EMAIL", "")
ZULIP_API_KEY = os.getenv("ZULIP_API_KEY", "")
ZULIP_SITE = os.getenv("ZULIP_SITE", "https://zulip.example.com")

BASE_URL = f"{ZULIP_SITE}/api/v1"
AUTH = (ZULIP_EMAIL, ZULIP_API_KEY)


def api_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to the Zulip API."""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params, auth=AUTH, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(url, params=params, json=json_data, auth=AUTH, timeout=30)
        elif method.upper() == "PATCH":
            response = requests.patch(url, params=params, json=json_data, auth=AUTH, timeout=30)
        elif method.upper() == "DELETE":
            response = requests.delete(url, params=params, auth=AUTH, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        if response.status_code >= 400:
            return {"error": f"HTTP {response.status_code}: {response.text}"}

        return response.json()
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# MESSAGES
# ============================================================================


@server.tool()
def send_message(
    type: str,
    to: str,
    content: str,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Send a message to a stream or user.
    
    Args:
        type: "stream" or "private"
        to: Stream name (for stream) or user email/ID (for private)
        content: Message content
        topic: Topic name (required for stream messages)
    """
    if type == "stream" and not topic:
        return {"error": "topic is required for stream messages"}

    data = {
        "type": type,
        "to": to,
        "content": content,
    }
    if topic:
        data["topic"] = topic

    return api_request("POST", "/messages", json_data=data)


@server.tool()
def get_messages(
    anchor: Optional[int] = None,
    num_before: int = 0,
    num_after: int = 10,
    narrow: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Fetch messages from the server.
    
    Args:
        anchor: Message ID to anchor around
        num_before: Number of messages before anchor
        num_after: Number of messages after anchor
        narrow: JSON-encoded narrow filter (e.g., '[["stream", "general"]]')
    """
    params = {
        "num_before": num_before,
        "num_after": num_after,
    }
    if anchor is not None:
        params["anchor"] = anchor
    if narrow:
        params["narrow"] = narrow

    return api_request("GET", "/messages", params=params)


@server.tool()
def edit_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Edit a message's content or topic.
    
    Args:
        message_id: ID of the message to edit
        content: New message content
        topic: New topic name
    """
    data = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic

    if not data:
        return {"error": "At least one of content or topic must be provided"}

    return api_request("PATCH", f"/messages/{message_id}", json_data=data)


@server.tool()
def delete_message(message_id: int) -> Dict[str, Any]:
    """Delete a message."""
    return api_request("DELETE", f"/messages/{message_id}")


@server.tool()
def get_message_history(message_id: int) -> Dict[str, Any]:
    """Get the edit history of a message."""
    return api_request("GET", f"/messages/{message_id}/history")


@server.tool()
def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: str = "unicode_emoji",
) -> Dict[str, Any]:
    """
    Add a reaction to a message.
    
    Args:
        message_id: ID of the message
        emoji_name: Name of the emoji
        emoji_code: Unicode code point (optional)
        reaction_type: Type of reaction (unicode_emoji, realm_emoji, zulip_extra_emoji)
    """
    data = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type,
    }
    if emoji_code:
        data["emoji_code"] = emoji_code

    return api_request("POST", f"/messages/{message_id}/reactions", json_data=data)


@server.tool()
def remove_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: str = "unicode_emoji",
) -> Dict[str, Any]:
    """
    Remove a reaction from a message.
    
    Args:
        message_id: ID of the message
        emoji_name: Name of the emoji
        emoji_code: Unicode code point (optional)
        reaction_type: Type of reaction
    """
    params = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type,
    }
    if emoji_code:
        params["emoji_code"] = emoji_code

    return api_request("DELETE", f"/messages/{message_id}/reactions", params=params)


@server.tool()
def add_flag(message_id: int, flag: str) -> Dict[str, Any]:
    """
    Add a flag to a message.
    
    Args:
        message_id: ID of the message
        flag: Flag name (read, starred, collapsed, mentioned, wildcard_mentioned)
    """
    data = {"messages": [message_id], "flag": flag}
    return api_request("POST", "/messages/flags", json_data=data)


@server.tool()
def remove_flag(message_id: int, flag: str) -> Dict[str, Any]:
    """
    Remove a flag from a message.
    
    Args:
        message_id: ID of the message
        flag: Flag name
    """
    data = {"messages": [message_id], "flag": flag}
    return api_request("POST", "/messages/flags/remove", json_data=data)


@server.tool()
def move_message(
    message_id: int,
    stream_id: Optional[int] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Move a message to a different stream/topic.
    
    Args:
        message_id: ID of the message
        stream_id: Destination stream ID
        topic: Destination topic name
    """
    data = {}
    if stream_id is not None:
        data["stream_id"] = stream_id
    if topic is not None:
        data["topic"] = topic

    if not data:
        return {"error": "At least one of stream_id or topic must be provided"}

    return api_request("PATCH", f"/messages/{message_id}", json_data=data)


# ============================================================================
# STREAMS
# ============================================================================


@server.tool()
def list_streams(include_all_default: bool = False) -> Dict[str, Any]:
    """
    List all streams.
    
    Args:
        include_all_default: Include all default streams
    """
    params = {"include_all_default": include_all_default}
    return api_request("GET", "/streams", params=params)


@server.tool()
def get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    """Get details of a stream by ID."""
    return api_request("GET", f"/streams/{stream_id}")


@server.tool()
def create_stream(
    name: str,
    description: str = "",
    is_private: bool = False,
    is_announcement_only: bool = False,
) -> Dict[str, Any]:
    """
    Create a new stream.
    
    Args:
        name: Stream name
        description: Stream description
        is_private: Whether the stream is private
        is_announcement_only: Whether only admins can post
    """
    data = {
        "name": name,
        "description": description,
        "is_private": is_private,
        "is_announcement_only": is_announcement_only,
    }
    return api_request("POST", "/streams", json_data=data)


@server.tool()
def update_stream(
    stream_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_announcement_only: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Update stream settings.
    
    Args:
        stream_id: ID of the stream
        name: New stream name
        description: New description
        is_private: New privacy setting
        is_announcement_only: New announcement-only setting
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = is_private
    if is_announcement_only is not None:
        data["is_announcement_only"] = is_announcement_only

    if not data:
        return {"error": "At least one field must be provided"}

    return api_request("PATCH", f"/streams/{stream_id}", json_data=data)


@server.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    """Archive a stream."""
    data = {}
    return api_request("DELETE", f"/streams/{stream_id}", json_data=data)


@server.tool()
def subscribe_to_stream(stream_id: int) -> Dict[str, Any]:
    """Subscribe to a stream."""
    data = {"subscriptions": [{"name": "", "stream_id": stream_id}]}
    return api_request("POST", "/users/me/subscriptions", json_data=data)


@server.tool()
def unsubscribe_from_stream(stream_id: int) -> Dict[str, Any]:
    """Unsubscribe from a stream."""
    return api_request("DELETE", f"/users/me/subscriptions", params={"stream_id": stream_id})


@server.tool()
def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """Get all topics in a stream."""
    return api_request("GET", f"/streams/{stream_id}/topics")


# ============================================================================
# TOPICS
# ============================================================================


@server.tool()
def rename_topic(
    stream_id: int,
    topic_name: str,
    new_topic_name: str,
) -> Dict[str, Any]:
    """
    Rename a topic.
    
    Args:
        stream_id: ID of the stream
        topic_name: Current topic name
        new_topic_name: New topic name
    """
    data = {"topic_name": new_topic_name}
    params = {"stream_id": stream_id}
    return api_request("PATCH", f"/topics/{topic_name}", params=params, json_data=data)


@server.tool()
def delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Delete all messages in a topic.
    
    Args:
        stream_id: ID of the stream
        topic_name: Name of the topic
    """
    params = {"stream_id": stream_id}
    return api_request("DELETE", f"/topics/{topic_name}", params=params)


@server.tool()
def resolve_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Mark a topic as resolved.
    
    Args:
        stream_id: ID of the stream
        topic_name: Name of the topic
    """
    data = {"resolved": True}
    params = {"stream_id": stream_id}
    return api_request("PATCH", f"/topics/{topic_name}", params=params, json_data=data)


@server.tool()
def unresolve_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Mark a topic as unresolved.
    
    Args:
        stream_id: ID of the stream
        topic_name: Name of the topic
    """
    data = {"resolved": False}
    params = {"stream_id": stream_id}
    return api_request("PATCH", f"/topics/{topic_name}", params=params, json_data=data)


# ============================================================================
# USERS
# ============================================================================


@server.tool()
def get_user_profile(user_id: Optional[int] = None) -> Dict[str, Any]:
    """
    Get user profile information.
    
    Args:
        user_id: ID of the user (if None, returns current user)
    """
    if user_id is None:
        return api_request("GET", "/users/me")
    return api_request("GET", f"/users/{user_id}")


@server.tool()
def list_users() -> Dict[str, Any]:
    """List all users in the organization."""
    return api_request("GET", "/users")


@server.tool()
def get_user_presence(user_id: int) -> Dict[str, Any]:
    """Get presence information for a user."""
    return api_request("GET", f"/users/{user_id}/presence")


@server.tool()
def update_user_status(
    status_text: Optional[str] = None,
    status_emoji: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update current user's status.
    
    Args:
        status_text: Status text message
        status_emoji: Status emoji name
    """
    data = {}
    if status_text is not None:
        data["status_text"] = status_text
    if status_emoji is not None:
        data["status_emoji"] = status_emoji

    if not data:
        return {"error": "At least one field must be provided"}

    return api_request("POST", "/users/me/status", json_data=data)


@server.tool()
def get_user_by_email(email: str) -> Dict[str, Any]:
    """Get user information by email address."""
    return api_request("GET", "/users/by_email", params={"email": email})


@server.tool()
def create_user(
    email: str,
    password: str,
    full_name: str,
) -> Dict[str, Any]:
    """
    Create a new user (admin only).
    
    Args:
        email: User email
        password: User password
        full_name: User's full name
    """
    data = {
        "email": email,
        "password": password,
        "full_name": full_name,
    }
    return api_request("POST", "/users", json_data=data)


@server.tool()
def deactivate_user(user_id: int) -> Dict[str, Any]:
    """Deactivate a user (admin only)."""
    data = {}
    return api_request("DELETE", f"/users/{user_id}", json_data=data)


# ============================================================================
# SCHEDULED MESSAGES
# ============================================================================


@server.tool()
def schedule_message(
    type: str,
    to: str,
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Schedule a message to be sent at a later time.
    
    Args:
        type: "stream" or "private"
        to: Stream name or user email
        content: Message content
        scheduled_delivery_timestamp: Unix timestamp for delivery
        topic: Topic name (required for stream messages)
    """
    if type == "stream" and not topic:
        return {"error": "topic is required for stream messages"}

    data = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic:
        data["topic"] = topic

    return api_request("POST", "/scheduled_messages", json_data=data)


@server.tool()
def list_scheduled_messages() -> Dict[str, Any]:
    """List all scheduled messages for the current user."""
    return api_request("GET", "/scheduled_messages")


@server.tool()
def edit_scheduled_message(
    scheduled_message_id: int,
    content: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Edit a scheduled message.
    
    Args:
        scheduled_message_id: ID of the scheduled message
        content: New message content
        scheduled_delivery_timestamp: New delivery timestamp
    """
    data = {}
    if content is not None:
        data["content"] = content
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp

    if not data:
        return {"error": "At least one field must be provided"}

    return api_request("PATCH", f"/scheduled_messages/{scheduled_message_id}", json_data=data)


@server.tool()
def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """Delete a scheduled message."""
    return api_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")


# ============================================================================
# DRAFTS
# ============================================================================


@server.tool()
def create_draft(
    type: str,
    to: str,
    content: str,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a draft message.
    
    Args:
        type: "stream" or "private"
        to: Stream name or user email
        content: Message content
        topic: Topic name (required for stream messages)
    """
    if type == "stream" and not topic:
        return {"error": "topic is required for stream messages"}

    data = {
        "type": type,
        "to": to,
        "content": content,
    }
    if topic:
        data["topic"] = topic

    return api_request("POST", "/drafts", json_data=data)


@server.tool()
def list_drafts() -> Dict[str, Any]:
    """List all drafts for the current user."""
    return api_request("GET", "/drafts")


@server.tool()
def edit_draft(
    draft_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Edit a draft message.
    
    Args:
        draft_id: ID of the draft
        content: New message content
        topic: New topic name
    """
    data = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic

    if not data:
        return {"error": "At least one field must be provided"}

    return api_request("PATCH", f"/drafts/{draft_id}", json_data=data)


@server.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    """Delete a draft message."""
    return api_request("DELETE", f"/drafts/{draft_id}")


# ============================================================================
# FILE UPLOADS
# ============================================================================


@server.tool()
def upload_file(file_path: str) -> Dict[str, Any]:
    """
    Upload a file to Zulip.
    
    Args:
        file_path: Path to the file to upload
    """
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            url = f"{BASE_URL}/user_uploads"
            response = requests.post(url, files=files, auth=AUTH, timeout=30)

        if response.status_code >= 400:
            return {"error": f"HTTP {response.status_code}: {response.text}"}

        return response.json()
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# SEARCH
# ============================================================================


@server.tool()
def search_messages(query: str, num_before: int = 0, num_after: int = 10) -> Dict[str, Any]:
    """
    Search for messages.
    
    Args:
        query: Search query
        num_before: Number of messages before match
        num_after: Number of messages after match
    """
    params = {
        "query": query,
        "num_before": num_before,
        "num_after": num_after,
    }
    return api_request("GET", "/search_messages", params=params)


# ============================================================================
# EMOJI
# ============================================================================


@server.tool()
def list_emoji() -> Dict[str, Any]:
    """List all custom emoji in the organization."""
    return api_request("GET", "/emoji")


# ============================================================================
# ORGANIZATION
# ============================================================================


@server.tool()
def get_organization_info() -> Dict[str, Any]:
    """Get information about the organization."""
    return api_request("GET", "/server_settings")


@server.tool()
def get_user_groups() -> Dict[str, Any]:
    """List all user groups in the organization."""
    return api_request("GET", "/user_groups")


@server.tool()
def create_user_group(
    name: str,
    description: str = "",
    members: Optional[list] = None,
) -> Dict[str, Any]:
    """
    Create a new user group.
    
    Args:
        name: Group name
        description: Group description
        members: List of user IDs to add to the group
    """
    data = {
        "name": name,
        "description": description,
    }
    if members:
        data["members"] = members

    return api_request("POST", "/user_groups", json_data=data)


@server.tool()
def update_user_group(
    group_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a user group.
    
    Args:
        group_id: ID of the group
        name: New group name
        description: New description
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description

    if not data:
        return {"error": "At least one field must be provided"}

    return api_request("PATCH", f"/user_groups/{group_id}", json_data=data)


@server.tool()
def delete_user_group(group_id: int) -> Dict[str, Any]:
    """Delete a user group."""
    return api_request("DELETE", f"/user_groups/{group_id}")


@server.tool()
def add_user_to_group(group_id: int, user_id: int) -> Dict[str, Any]:
    """Add a user to a group."""
    data = {"members": [user_id]}
    return api_request("POST", f"/user_groups/{group_id}/members", json_data=data)


@server.tool()
def remove_user_from_group(group_id: int, user_id: int) -> Dict[str, Any]:
    """Remove a user from a group."""
    return api_request("DELETE", f"/user_groups/{group_id}/members/{user_id}")


# ============================================================================
# SUBSCRIPTIONS
# ============================================================================


@server.tool()
def get_subscriptions() -> Dict[str, Any]:
    """Get all streams the current user is subscribed to."""
    return api_request("GET", "/users/me/subscriptions")


@server.tool()
def update_subscription_settings(
    stream_id: int,
    is_muted: Optional[bool] = None,
    pin_to_top: Optional[bool] = None,
    color: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update subscription settings for a stream.
    
    Args:
        stream_id: ID of the stream
        is_muted: Whether to mute the stream
        pin_to_top: Whether to pin to top
        color: Hex color code
    """
    data = {}
    if is_muted is not None:
        data["is_muted"] = is_muted
    if pin_to_top is not None:
        data["pin_to_top"] = pin_to_top
    if color is not None:
        data["color"] = color

    if not data:
        return {"error": "At least one field must be provided"}

    params = {"stream_id": stream_id}
    return api_request("PATCH", "/users/me/subscriptions/properties", params=params, json_data=data)


# ============================================================================
# NARROW FILTERS
# ============================================================================


@server.tool()
def get_narrow_messages(
    narrow_filter: str,
    anchor: Optional[int] = None,
    num_before: int = 0,
    num_after: int = 10,
) -> Dict[str, Any]:
    """
    Get messages matching a narrow filter.
    
    Args:
        narrow_filter: JSON-encoded narrow filter (e.g., '[["stream", "general"]]')
        anchor: Message ID to anchor around
        num_before: Number of messages before anchor
        num_after: Number of messages after anchor
    """
    params = {
        "narrow": narrow_filter,
        "num_before": num_before,
        "num_after": num_after,
    }
    if anchor is not None:
        params["anchor"] = anchor

    return api_request("GET", "/messages", params=params)


# ============================================================================
# MUTING
# ============================================================================


@server.tool()
def mute_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Mute a topic.
    
    Args:
        stream_id: ID of the stream
        topic_name: Name of the topic
    """
    data = {
        "stream_id": stream_id,
        "topic": topic_name,
        "op": "add",
    }
    return api_request("PATCH", "/user_topics", json_data=data)


@server.tool()
def unmute_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Unmute a topic.
    
    Args:
        stream_id: ID of the stream
        topic_name: Name of the topic
    """
    data = {
        "stream_id": stream_id,
        "topic": topic_name,
        "op": "remove",
    }
    return api_request("PATCH", "/user_topics", json_data=data)


# ============================================================================
# TYPING INDICATORS
# ============================================================================


@server.tool()
def set_typing_status(
    type: str,
    to: str,
    op: str = "start",
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Set typing status.
    
    Args:
        type: "stream" or "private"
        to: Stream name or user email
        op: "start" or "stop"
        topic: Topic name (required for stream)
    """
    data = {
        "type": type,
        "to": to,
        "op": op,
    }
    if topic:
        data["topic"] = topic

    return api_request("POST", "/typing", json_data=data)


if __name__ == "__main__":
    server.run()
