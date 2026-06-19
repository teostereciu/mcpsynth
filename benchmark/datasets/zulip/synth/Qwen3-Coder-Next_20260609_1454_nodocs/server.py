#!/usr/bin/env python3
"""MCP Server for Zulip REST API."""

import os
import requests
from typing import Any, Optional
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="zulip", instruction="Zulip REST API MCP server")

# Zulip API base URL
ZULIP_API_BASE = "{site}/api/v1"


def get_auth() -> tuple[str, str]:
    """Get Zulip authentication credentials."""
    email = os.environ.get("ZULIP_EMAIL")
    api_key = os.environ.get("ZULIP_API_KEY")
    if not email or not api_key:
        raise ValueError("ZULIP_EMAIL and ZULIP_API_KEY environment variables must be set")
    return email, api_key


def get_site() -> str:
    """Get Zulip site URL."""
    site = os.environ.get("ZULIP_SITE")
    if not site:
        raise ValueError("ZULIP_SITE environment variable must be set")
    return site


def zulip_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    data: Optional[dict] = None,
) -> dict:
    """Make a request to the Zulip API."""
    site = get_site()
    email, api_key = get_auth()
    url = f"{site.rstrip('/')}/api/v1/{endpoint.lstrip('/')}"
    
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            auth=(email, api_key),
            params=params,
            json=data,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_data = e.response.json()
            return {"error": error_data.get("msg", str(e))}
        except:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


# ====================
# Message Endpoints
# ====================

@mcp.tool()
def send_message(
    to: str,
    type: str,
    content: str,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
) -> dict:
    """
    Send a message to a stream or user.
    
    Args:
        to: Stream ID (as integer) or user email (as string)
        type: Message type - 'stream' or 'private'
        content: Content of the message
        subject: Subject line for stream messages (required for stream type)
        topic: Topic for stream messages (deprecated, use subject instead)
    
    Returns:
        API response with message details
    """
    data = {
        "to": to,
        "type": type,
        "content": content,
    }
    if subject:
        data["subject"] = subject
    if topic:
        data["topic"] = topic
    return zulip_request("POST", "/messages", data=data)


@mcp.tool()
def get_messages(
    anchor: Optional[int] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    use_first_unread: Optional[bool] = None,
    narrow: Optional[list] = None,
    client_gravatar: Optional[bool] = None,
) -> dict:
    """
    Fetch a list of messages.
    
    Args:
        anchor: Message ID to anchor the query
        num_before: Number of messages before the anchor
        num_after: Number of messages after the anchor
        use_first_unread: Use the first unread message as anchor
        narrow: Narrow the search with a list of operators
        client_gravatar: Compute gravatars on the server side
    
    Returns:
        Response with messages array and other metadata
    """
    params = {}
    if anchor is not None:
        params["anchor"] = anchor
    if num_before is not None:
        params["num_before"] = num_before
    if num_after is not None:
        params["num_after"] = num_after
    if use_first_unread is not None:
        params["use_first_unread"] = use_first_unread
    if narrow is not None:
        params["narrow"] = narrow
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    return zulip_request("GET", "/messages", params=params)


@mcp.tool()
def get_message_history(
    message_id: int,
) -> dict:
    """
    Get the edit history of a message.
    
    Args:
        message_id: ID of the message
    
    Returns:
        Message edit history
    """
    return zulip_request("GET", f"/messages/{message_id}/history")


@mcp.tool()
def update_message(
    message_id: int,
    topic: Optional[str] = None,
    content: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
) -> dict:
    """
    Update a message (edit content or topic).
    
    Args:
        message_id: ID of the message to update
        topic: New topic (for stream messages)
        content: New content
        propagate_mode: How to propagate topic changes ('change_all', 'change_later', 'change_one')
        send_notification_to_old_thread: Send notification to old thread
        send_notification_to_new_thread: Send notification to new thread
    
    Returns:
        API response
    """
    data = {}
    if topic is not None:
        data["topic"] = topic
    if content is not None:
        data["content"] = content
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = send_notification_to_old_thread
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = send_notification_to_new_thread
    return zulip_request("PATCH", f"/messages/{message_id}", data=data)


@mcp.tool()
def delete_message(
    message_id: int,
) -> dict:
    """
    Delete a message.
    
    Args:
        message_id: ID of the message to delete
    
    Returns:
        API response
    """
    return zulip_request("DELETE", f"/messages/{message_id}")


@mcp.tool()
def get_raw_message(
    message_id: int,
) -> dict:
    """
    Get the raw content of a message.
    
    Args:
        message_id: ID of the message
    
    Returns:
        Raw message content
    """
    return zulip_request("GET", f"/messages/{message_id}")


@mcp.tool()
def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = "unicode_emoji",
) -> dict:
    """
    Add a reaction to a message.
    
    Args:
        message_id: ID of the message
        emoji_name: Name of the emoji
        emoji_code: Emoji code (for custom emoji)
        reaction_type: Type of emoji ('unicode_emoji', 'realm_emoji', 'emoji_code')
    
    Returns:
        API response
    """
    data = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type,
    }
    if emoji_code:
        data["emoji_code"] = emoji_code
    return zulip_request("POST", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def remove_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = "unicode_emoji",
) -> dict:
    """
    Remove a reaction from a message.
    
    Args:
        message_id: ID of the message
        emoji_name: Name of the emoji
        emoji_code: Emoji code (for custom emoji)
        reaction_type: Type of emoji ('unicode_emoji', 'realm_emoji', 'emoji_code')
    
    Returns:
        API response
    """
    params = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type,
    }
    if emoji_code:
        params["emoji_code"] = emoji_code
    return zulip_request("DELETE", f"/messages/{message_id}/reactions", params=params)


@mcp.tool()
def update_message_flags(
    operation: str,
    flag: str,
    messages: list,
) -> dict:
    """
    Update flags on one or more messages.
    
    Args:
        operation: 'add' or 'remove'
        flag: Flag name (e.g., 'read', 'wildcard_mentioned', 'starred')
        messages: List of message IDs
    
    Returns:
        API response
    """
    data = {
        "operation": operation,
        "flag": flag,
        "messages": messages,
    }
    return zulip_request("POST", "/messages/flags", data=data)


@mcp.tool()
def get_user_messages(
    user_id: int,
    anchor: Optional[int] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    narrow: Optional[list] = None,
) -> dict:
    """
    Get messages sent to or from a specific user.
    
    Args:
        user_id: ID of the user
        anchor: Message ID to anchor the query
        num_before: Number of messages before the anchor
        num_after: Number of messages after the anchor
        narrow: Narrow the search with a list of operators
    
    Returns:
        Response with messages array
    """
    params = {}
    if anchor is not None:
        params["anchor"] = anchor
    if num_before is not None:
        params["num_before"] = num_before
    if num_after is not None:
        params["num_after"] = num_after
    if narrow is not None:
        params["narrow"] = narrow
    return zulip_request("GET", f"/users/{user_id}/messages", params=params)


# ====================
# Stream Endpoints
# ====================

@mcp.tool()
def create_stream(
    name: str,
    description: Optional[str] = None,
    invite_only: Optional[bool] = False,
    is_announcement_only: Optional[bool] = False,
) -> dict:
    """
    Create a new stream.
    
    Args:
        name: Name of the stream
        description: Description of the stream
        invite_only: Whether the stream is invite-only
        is_announcement_only: Whether only admins can post to the stream
    
    Returns:
        API response with stream details
    """
    data = {
        "name": name,
    }
    if description:
        data["description"] = description
    if invite_only:
        data["invite_only"] = invite_only
    if is_announcement_only:
        data["is_announcement_only"] = is_announcement_only
    return zulip_request("POST", "/streams", data=data)


@mcp.tool()
def get_streams(
    include_public: Optional[bool] = True,
    include_public_description_only: Optional[bool] = None,
) -> dict:
    """
    List streams the current user has access to.
    
    Args:
        include_public: Whether to include public streams
        include_public_description_only: Whether to include public description-only streams
    
    Returns:
        Response with streams array
    """
    params = {}
    if include_public is not None:
        params["include_public"] = include_public
    if include_public_description_only is not None:
        params["include_public_description_only"] = include_public_description_only
    return zulip_request("GET", "/streams", params=params)


@mcp.tool()
def get_stream_id(
    stream_name: str,
) -> dict:
    """
    Get the ID of a stream by name.
    
    Args:
        stream_name: Name of the stream
    
    Returns:
        Response with stream_id
    """
    params = {"stream_name": stream_name}
    return zulip_request("GET", "/streams/get_id", params=params)


@mcp.tool()
def update_stream(
    stream_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    invite_only: Optional[bool] = None,
    is_announcement_only: Optional[bool] = None,
) -> dict:
    """
    Update a stream's settings.
    
    Args:
        stream_id: ID of the stream
        name: New name for the stream
        description: New description
        invite_only: New invite-only setting
        is_announcement_only: New announcement-only setting
    
    Returns:
        API response
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if invite_only is not None:
        data["invite_only"] = invite_only
    if is_announcement_only is not None:
        data["is_announcement_only"] = is_announcement_only
    return zulip_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def delete_stream(
    stream_id: int,
) -> dict:
    """
    Delete a stream.
    
    Args:
        stream_id: ID of the stream to delete
    
    Returns:
        API response
    """
    return zulip_request("DELETE", f"/streams/{stream_id}")


@mcp.tool()
def archive_stream(
    stream_id: int,
) -> dict:
    """
    Archive a stream.
    
    Args:
        stream_id: ID of the stream to archive
    
    Returns:
        API response
    """
    return zulip_request("POST", f"/streams/{stream_id}/delete")


@mcp.tool()
def subscribe(
    subscriptions: list,
    principals: Optional[list] = None,
    is_old_stream: Optional[bool] = None,
) -> dict:
    """
    Subscribe users to streams.
    
    Args:
        subscriptions: List of stream names or IDs
        principals: List of user emails or IDs (default: current user)
        is_old_stream: Whether to treat streams as old (skip welcome message)
    
    Returns:
        API response
    """
    data = {
        "subscriptions": subscriptions,
    }
    if principals:
        data["principals"] = principals
    if is_old_stream is not None:
        data["is_old_stream"] = is_old_stream
    return zulip_request("POST", "/users/me/subscriptions", data=data)


@mcp.tool()
def unsubscribe(
    subscriptions: list,
    principals: Optional[list] = None,
) -> dict:
    """
    Unsubscribe users from streams.
    
    Args:
        subscriptions: List of stream names or IDs
        principals: List of user emails or IDs (default: current user)
    
    Returns:
        API response
    """
    data = {
        "subscriptions": subscriptions,
    }
    if principals:
        data["principals"] = principals
    return zulip_request("DELETE", "/users/me/subscriptions", data=data)


@mcp.tool()
def get_subscribers(
    stream_id: int,
) -> dict:
    """
    Get subscribers of a stream.
    
    Args:
        stream_id: ID of the stream
    
    Returns:
        Response with subscribers array
    """
    return zulip_request("GET", f"/streams/{stream_id}/members")


# ====================
# Topic Endpoints
# ====================

@mcp.tool()
def list_topics(
    stream_id: int,
) -> dict:
    """
    List topics in a stream.
    
    Args:
        stream_id: ID of the stream
    
    Returns:
        Response with topics array
    """
    return zulip_request("GET", f"/streams/{stream_id}/topics")


@mcp.tool()
def rename_topic(
    stream_id: int,
    old_topic: str,
    new_topic: str,
) -> dict:
    """
    Rename a topic in a stream.
    
    Args:
        stream_id: ID of the stream
        old_topic: Current topic name
        new_topic: New topic name
    
    Returns:
        API response
    """
    data = {
        "old_topic": old_topic,
        "new_topic": new_topic,
    }
    return zulip_request("POST", f"/streams/{stream_id}/rename_topic", data=data)


@mcp.tool()
def delete_topic(
    stream_id: int,
    topic_name: str,
) -> dict:
    """
    Delete a topic in a stream (marks all messages as matched in the search).
    
    Args:
        stream_id: ID of the stream
        topic_name: Name of the topic to delete
    
    Returns:
        API response
    """
    data = {
        "topic_name": topic_name,
    }
    return zulip_request("DELETE", f"/streams/{stream_id}/topics", data=data)


@mcp.tool()
def resolve_topic(
    stream_id: int,
    topic_name: str,
) -> dict:
    """
    Resolve a topic in a stream.
    
    Args:
        stream_id: ID of the stream
        topic_name: Name of the topic to resolve
    
    Returns:
        API response
    """
    data = {
        "topic_name": topic_name,
    }
    return zulip_request("POST", f"/streams/{stream_id}/resolve_topic", data=data)


# ====================
# User Endpoints
# ====================

@mcp.tool()
def get_user_by_id(
    user_id: int,
) -> dict:
    """
    Get a user's profile by ID.
    
    Args:
        user_id: ID of the user
    
    Returns:
        User profile data
    """
    return zulip_request("GET", f"/users/{user_id}")


@mcp.tool()
def get_user_profile(
    user_id: Optional[int] = None,
    email: Optional[str] = None,
) -> dict:
    """
    Get a user's profile (for yourself or another user).
    
    Args:
        user_id: ID of the user (optional if email provided)
        email: Email of the user (optional if user_id provided)
    
    Returns:
        User profile data
    """
    if user_id:
        return zulip_request("GET", f"/users/{user_id}")
    elif email:
        params = {"email": email}
        return zulip_request("GET", "/users/me", params=params)
    else:
        return zulip_request("GET", "/users/me")


@mcp.tool()
def list_users(
    bot_type: Optional[int] = None,
    include_custom_profile_fields: Optional[bool] = True,
) -> dict:
    """
    List users in the organization.
    
    Args:
        bot_type: Filter by bot type (0=normal, 1=bot, 2=outgoing webhook, 3=embedded bot)
        include_custom_profile_fields: Include custom profile field values
    
    Returns:
        Response with members array
    """
    params = {}
    if bot_type is not None:
        params["bot_type"] = bot_type
    if include_custom_profile_fields is not None:
        params["include_custom_profile_fields"] = include_custom_profile_fields
    return zulip_request("GET", "/users", params=params)


@mcp.tool()
def update_user_profile(
    full_name: Optional[str] = None,
    avatar_url: Optional[str] = None,
    custom_profile_field: Optional[dict] = None,
) -> dict:
    """
    Update the current user's profile.
    
    Args:
        full_name: New full name
        avatar_url: URL for new avatar
        custom_profile_field: Dict of custom field data
    
    Returns:
        API response
    """
    data = {}
    if full_name is not None:
        data["full_name"] = full_name
    if avatar_url is not None:
        data["avatar_url"] = avatar_url
    if custom_profile_field is not None:
        data["custom_profile_field"] = custom_profile_field
    return zulip_request("PATCH", "/users/me", data=data)


@mcp.tool()
def get_user_presence(
    user_id: int,
) -> dict:
    """
    Get presence information for a user.
    
    Args:
        user_id: ID of the user
    
    Returns:
        Presence data
    """
    return zulip_request("GET", f"/users/{user_id}/presence")


@mcp.tool()
def get_presences(
) -> dict:
    """
    Get presence information for all users in the organization.
    
    Returns:
        Presence data for all users
    """
    return zulip_request("GET", "/users/me/presence")


# ====================
# Scheduled Messages
# ====================

@mcp.tool()
def create_scheduled_message(
    to: str,
    type: str,
    content: str,
    scheduled_delivery_timestamp: int,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
) -> dict:
    """
    Create a scheduled message.
    
    Args:
        to: Stream ID or user email
        type: Message type ('stream' or 'private')
        content: Message content
        scheduled_delivery_timestamp: Unix timestamp for delivery
        subject: Subject for stream messages
        topic: Topic for stream messages
    
    Returns:
        API response with scheduled message details
    """
    data = {
        "to": to,
        "type": type,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if subject:
        data["subject"] = subject
    if topic:
        data["topic"] = topic
    return zulip_request("POST", "/scheduled_messages", data=data)


@mcp.tool()
def list_scheduled_messages(
) -> dict:
    """
    List all scheduled messages.
    
    Returns:
        Response with scheduled_messages array
    """
    return zulip_request("GET", "/scheduled_messages")


@mcp.tool()
def get_scheduled_message(
    scheduled_message_id: int,
) -> dict:
    """
    Get a scheduled message by ID.
    
    Args:
        scheduled_message_id: ID of the scheduled message
    
    Returns:
        Scheduled message details
    """
    return zulip_request("GET", f"/scheduled_messages/{scheduled_message_id}")


@mcp.tool()
def update_scheduled_message(
    scheduled_message_id: int,
    to: Optional[str] = None,
    type: Optional[str] = None,
    content: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
) -> dict:
    """
    Update a scheduled message.
    
    Args:
        scheduled_message_id: ID of the scheduled message
        to: New destination
        type: New message type
        content: New content
        scheduled_delivery_timestamp: New delivery timestamp
        subject: New subject
        topic: New topic
    
    Returns:
        API response
    """
    data = {}
    if to is not None:
        data["to"] = to
    if type is not None:
        data["type"] = type
    if content is not None:
        data["content"] = content
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    if subject is not None:
        data["subject"] = subject
    if topic is not None:
        data["topic"] = topic
    return zulip_request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


@mcp.tool()
def delete_scheduled_message(
    scheduled_message_id: int,
) -> dict:
    """
    Delete a scheduled message.
    
    Args:
        scheduled_message_id: ID of the scheduled message
    
    Returns:
        API response
    """
    return zulip_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")


# ====================
# Drafts
# ====================

@mcp.tool()
def get_drafts(
) -> dict:
    """
    Get all drafts for the current user.
    
    Returns:
        Response with drafts array
    """
    return zulip_request("GET", "/drafts")


@mcp.tool()
def create_draft(
    type: str,
    to: list,
    content: str,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
) -> dict:
    """
    Create a new draft.
    
    Args:
        type: Draft type ('private' or 'stream')
        to: List of user emails or stream ID
        content: Draft content
        subject: Subject for stream drafts
        topic: Topic for stream drafts
    
    Returns:
        API response with draft details
    """
    data = {
        "type": type,
        "to": to,
        "content": content,
    }
    if subject:
        data["subject"] = subject
    if topic:
        data["topic"] = topic
    return zulip_request("POST", "/drafts", data=data)


@mcp.tool()
def update_draft(
    draft_id: int,
    type: Optional[str] = None,
    to: Optional[list] = None,
    content: Optional[str] = None,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
) -> dict:
    """
    Update an existing draft.
    
    Args:
        draft_id: ID of the draft
        type: New draft type
        to: New destinations
        content: New content
        subject: New subject
        topic: New topic
    
    Returns:
        API response
    """
    data = {}
    if type is not None:
        data["type"] = type
    if to is not None:
        data["to"] = to
    if content is not None:
        data["content"] = content
    if subject is not None:
        data["subject"] = subject
    if topic is not None:
        data["topic"] = topic
    return zulip_request("PATCH", f"/drafts/{draft_id}", data=data)


@mcp.tool()
def delete_draft(
    draft_id: int,
) -> dict:
    """
    Delete a draft.
    
    Args:
        draft_id: ID of the draft
    
    Returns:
        API response
    """
    return zulip_request("DELETE", f"/drafts/{draft_id}")


# ====================
# File Uploads
# ====================

@mcp.tool()
def upload_file(
    file_path: str,
    filename: Optional[str] = None,
) -> dict:
    """
    Upload a file to Zulip.
    
    Args:
        file_path: Path to the file to upload
        filename: Optional filename (defaults to basename of path)
    
    Returns:
        Response with url and checksum
    """
    try:
        site = get_site()
        email, api_key = get_auth()
        
        if filename is None:
            filename = os.path.basename(file_path)
        
        with open(file_path, "rb") as f:
            response = requests.post(
                url=f"{site.rstrip('/')}/api/v1/user_uploads",
                auth=(email, api_key),
                files={"file": (filename, f)},
            )
        
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_file_url(
    url: str,
) -> dict:
    """
    Get a download URL for a file.
    
    Args:
        url: The file URL from upload response
    
    Returns:
        Response with image_url (direct download URL)
    """
    return zulip_request("GET", "/user_uploads", params={"url": url})


# ====================
# Reaction Endpoints
# ====================

@mcp.tool()
def get_reactions(
    message_id: int,
) -> dict:
    """
    Get all reactions on a message.
    
    Args:
        message_id: ID of the message
    
    Returns:
        Response with reactions array
    """
    return zulip_request("GET", f"/messages/{message_id}/reactions")


# ====================
# Notification Endpoints
# ====================

@mcp.tool()
def get_notifications(
) -> dict:
    """
    Get notification settings for the current user.
    
    Returns:
        Notification settings
    """
    return zulip_request("GET", "/settings/notifications")


@mcp.tool()
def update_notification_settings(
    **kwargs,
) -> dict:
    """
    Update notification settings for the current user.
    
    Args:
        **kwargs: Notification settings to update
    
    Returns:
        API response
    """
    return zulip_request("PATCH", "/settings/notifications", data=kwargs)


# ====================
# Custom Profile Fields
# ====================

@mcp.tool()
def list_custom_profile_fields(
) -> dict:
    """
    List all custom profile fields in the organization.
    
    Returns:
        Response with custom_profile_fields array
    """
    return zulip_request("GET", "/custom_profile_fields")


@mcp.tool()
def create_custom_profile_field(
    name: str,
    field_type: int,
    hint: Optional[str] = None,
    field_data: Optional[str] = None,
) -> dict:
    """
    Create a new custom profile field.
    
    Args:
        name: Name of the field
        field_type: Type of field (1=Text, 2=Date, 3=Link, 4=User, 5=List, 6=External account)
        hint: Hint text
        field_data: JSON string for field options (for list type)
    
    Returns:
        API response with field details
    """
    data = {
        "name": name,
        "field_type": field_type,
    }
    if hint:
        data["hint"] = hint
    if field_data:
        data["field_data"] = field_data
    return zulip_request("POST", "/custom_profile_fields", data=data)


# ====================
# Realm Endpoints
# ====================

@mcp.tool()
def get_realm(
) -> dict:
    """
    Get information about the realm (organization).
    
    Returns:
        Realm data
    """
    return zulip_request("GET", "/realm")


@mcp.tool()
def list_bot_members(
) -> dict:
    """
    List all bots in the organization.
    
    Returns:
        Response with bots array
    """
    return zulip_request("GET", "/bots")


@mcp.tool()
def create_bot(
    full_name: str,
    short_name: str,
    bot_type: Optional[int] = 1,
    payload_url: Optional[str] = None,
    abstract: Optional[str] = None,
    default_echo_bot: Optional[bool] = False,
) -> dict:
    """
    Create a new bot.
    
    Args:
        full_name: Full name for the bot
        short_name: Short name for the bot
        bot_type: Bot type (1=generic, 2=outgoing webhook)
        payload_url: URL for outgoing webhook bots
        abstract: Abstract description
        default_echo_bot: Whether to create an echo bot
    
    Returns:
        API response with bot credentials
    """
    data = {
        "full_name": full_name,
        "short_name": short_name,
        "bot_type": bot_type,
    }
    if payload_url:
        data["payload_url"] = payload_url
    if abstract:
        data["abstract"] = abstract
    if default_echo_bot:
        data["default_echo_bot"] = default_echo_bot
    return zulip_request("POST", "/bots", data=data)


# ====================
# Subscription Property Endpoints
# ====================

@mcp.tool()
def update_subscription_settings(
    stream_id: int,
    property: str,
    value: bool,
) -> dict:
    """
    Update a subscription property for a user.
    
    Args:
        stream_id: ID of the stream
        property: Property name (e.g., 'is_muted', 'pin_to_top', 'color')
        value: Property value
    
    Returns:
        API response
    """
    data = {
        "property": property,
        "value": value,
    }
    return zulip_request("PATCH", f"/users/me/subscriptions/{stream_id}", data=data)


# ====================
# Message Send Endpoints
# ====================

@mcp.tool()
def send_messages(
    messages: list,
) -> dict:
    """
    Send multiple messages in a single request.
    
    Args:
        messages: List of message objects with 'to', 'type', 'content', and optionally 'subject'
    
    Returns:
        Response with results array
    """
    return zulip_request("POST", "/messages", data={"messages": messages})


if __name__ == "__main__":
    mcp.run()
