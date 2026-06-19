#!/usr/bin/env python3
"""Zulip MCP Server - An MCP server for the Zulip REST API."""

import os
import json
from typing import Any
import requests

from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("zulip")

# Base URL for Zulip API
ZULIP_API_BASE = "{zulip_site}/api/v1"


def get_auth() -> tuple[str, str]:
    """Get authentication credentials from environment variables."""
    email = os.environ.get("ZULIP_EMAIL")
    api_key = os.environ.get("ZULIP_API_KEY")
    
    if not email or not api_key:
        raise ValueError("ZULIP_EMAIL and ZULIP_API_KEY environment variables must be set")
    
    return email, api_key


def get_base_url() -> str:
    """Get the Zulip base URL from environment variables."""
    zulip_site = os.environ.get("ZULIP_SITE")
    
    if not zulip_site:
        raise ValueError("ZULIP_SITE environment variable must be set")
    
    return zulip_site


def make_request(method: str, endpoint: str, params: dict | None = None, 
                 data: dict | None = None) -> dict[str, Any]:
    """Make a request to the Zulip API with error handling."""
    try:
        base_url = get_base_url()
        url = f"{base_url}{endpoint}"
        email, api_key = get_auth()
        
        response = requests.request(
            method=method,
            url=url,
            auth=(email, api_key),
            params=params,
            data=data,
            timeout=30
        )
        
        # Parse response
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = {"raw_response": response.text}
        
        # Add HTTP status code to result
        result["_http_status_code"] = response.status_code
        
        # Return the result directly (success or error)
        return result
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# ============================================================================
# Message Operations
# ============================================================================

@mcp.tool()
def send_message(type_: str, to: str | list[int] | list[str], content: str,
                 message_topic: str | None = None) -> dict[str, Any]:
    """Send a channel message or direct message.
    
    Args:
        type_: "direct" for direct message, "channel_name" or "channel" for channel message
        to: For channel messages, either the name or integer ID of the channel.
            For direct messages, either a list containing integer user IDs or a list
            containing string Zulip API email addresses.
        content: The content of the message.
        message_topic: The message_topic of the message. Only required for channel messages.
    """
    data = {
        "type": type_,
        "to": json.dumps(to) if isinstance(to, list) else to,
        "content": content
    }
    
    if message_topic is not None:
        data["message_topic"] = message_topic
    
    return make_request("POST", "/messages", data=data)


@mcp.tool()
def get_messages(start_message_id: str = "newest", before_count: int = 100,
                 after_count: int = 0, filter_spec: str | None = None,
                 apply_markdown: bool = True, client_gravatar: bool = True) -> dict[str, Any]:
    """Get messages with optional filtering.
    
    Args:
        start_message_id: Integer message ID or "newest", "oldest", "first_unread"
        before_count: Number of messages with IDs less than start_message_id to retrieve
        after_count: Number of messages with IDs greater than start_message_id to retrieve
        filter_spec: JSON-encoded filter_spec where you want to fetch the messages from
        apply_markdown: If true, message content is returned in rendered HTML format
        client_gravatar: Whether the client supports computing gravatars URLs
    """
    params = {
        "start_message_id": start_message_id,
        "before_count": before_count,
        "after_count": after_count,
        "apply_markdown": "true" if apply_markdown else "false",
        "client_gravatar": "true" if client_gravatar else "false"
    }
    
    if filter_spec is not None:
        params["filter_spec"] = filter_spec
    
    return make_request("GET", "/messages", params=params)


@mcp.tool()
def update_message(message_id: int, content: str | None = None,
                   propagate_mode: str = "change_one",
                   send_notification_to_old_thread: bool = False,
                   send_notification_to_new_thread: bool = True,
                   topic: str | None = None,
                   stream_id: int | None = None) -> dict[str, Any]:
    """Update the content, topic, or channel of a message.
    
    Args:
        message_id: The target message's ID
        content: The updated content of the target message
        propagate_mode: Which messages should be edited: "change_later", "change_one", "change_all"
        send_notification_to_old_thread: Whether to send an automated message to the old topic
        send_notification_to_new_thread: Whether to send an automated message to the new topic
        topic: The topic to move the message(s) to
        stream_id: The channel ID to move the message(s) to
    """
    data = {
        "message_id": str(message_id),
        "propagate_mode": propagate_mode,
        "send_notification_to_old_thread": "true" if send_notification_to_old_thread else "false",
        "send_notification_to_new_thread": "true" if send_notification_to_new_thread else "false"
    }
    
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if stream_id is not None:
        data["stream_id"] = str(stream_id)
    
    return make_request("PATCH", f"/messages/{message_id}", data=data)


@mcp.tool()
def delete_message(message_id: int) -> dict[str, Any]:
    """Permanently delete a message.
    
    Args:
        message_id: The target message's ID
    """
    return make_request("DELETE", f"/messages/{message_id}")


@mcp.tool()
def add_reaction(message_id: int, emoji_name: str,
                 reaction_type: str = "unicode_emoji") -> dict[str, Any]:
    """Add an emoji reaction to a message.
    
    Args:
        message_id: The target message's ID
        emoji_name: The target emoji's human-readable name
        reaction_type: Type of emoji: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji"
    """
    data = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type
    }
    
    return make_request("POST", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str,
                    reaction_type: str = "unicode_emoji") -> dict[str, Any]:
    """Remove an emoji reaction from a message.
    
    Args:
        message_id: The target message's ID
        emoji_name: The target emoji's human-readable name
        reaction_type: Type of emoji: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji"
    """
    data = {
        "emoji_name": emoji_name,
        "reaction_type": reaction_type
    }
    
    return make_request("DELETE", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def update_message_flags(message_ids: list[int], operation: str,
                         flag: str) -> dict[str, Any]:
    """Update personal message flags for one or more messages.
    
    Args:
        message_ids: List of message IDs
        operation: Either "add" or "remove"
        flag: The flag to update: "read", "alerted", "narrowed", "wildcard_mentioned",
              "has_link", "has_image", "has_uploaded_file"
    """
    data = {
        "message_ids": json.dumps(message_ids),
        "operation": operation,
        "flag": flag
    }
    
    return make_request("POST", "/messages/flags", data=data)


@mcp.tool()
def get_message_history(message_id: int) -> dict[str, Any]:
    """Fetch a message's edit history.
    
    Args:
        message_id: The target message's ID
    """
    return make_request("GET", f"/messages/{message_id}/history")


@mcp.tool()
def get_scheduled_messages() -> dict[str, Any]:
    """Get all scheduled messages for the user."""
    return make_request("GET", "/scheduled_messages")


@mcp.tool()
def create_scheduled_message(type_: str, to: str | list[int] | list[str],
                             content: str, scheduled_delivery_timestamp: int,
                             message_topic: str | None = None) -> dict[str, Any]:
    """Create a scheduled message.
    
    Args:
        type_: "direct" for direct message, "channel_name" or "channel" for channel message
        to: For channel messages, either the name or integer ID of the channel.
            For direct messages, a list containing integer user IDs.
        content: The content of the message.
        scheduled_delivery_timestamp: The UNIX timestamp for when the message will be sent
        message_topic: The message_topic of the message. Only required for channel messages.
    """
    data = {
        "type": type_,
        "to": json.dumps(to) if isinstance(to, list) else to,
        "content": content,
        "scheduled_delivery_timestamp": str(scheduled_delivery_timestamp)
    }
    
    if message_topic is not None:
        data["message_topic"] = message_topic
    
    return make_request("POST", "/scheduled_messages", data=data)


@mcp.tool()
def update_scheduled_message(scheduled_message_id: int, topic: str | None = None,
                             content: str | None = None,
                             scheduled_delivery_timestamp: int | None = None,
                             stream_id: int | None = None) -> dict[str, Any]:
    """Update a scheduled message.
    
    Args:
        scheduled_message_id: The ID of the scheduled message
        topic: The message_topic to move the scheduled message to
        content: The updated content of the scheduled message
        scheduled_delivery_timestamp: The new UNIX timestamp for when the message will be sent
        stream_id: The channel ID to move the scheduled message to
    """
    data = {}
    
    if topic is not None:
        data["topic"] = topic
    if content is not None:
        data["content"] = content
    if scheduled_delivery_timestamp is not None:
        data["scheduled_delivery_timestamp"] = str(scheduled_delivery_timestamp)
    if stream_id is not None:
        data["stream_id"] = str(stream_id)
    
    return make_request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


@mcp.tool()
def delete_scheduled_message(scheduled_message_id: int) -> dict[str, Any]:
    """Delete a scheduled message.
    
    Args:
        scheduled_message_id: The ID of the scheduled message
    """
    return make_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")


# ============================================================================
# Stream Operations
# ============================================================================

@mcp.tool()
def get_streams(include_public: bool = True, include_subscribed: bool = True,
                include_archived: bool = False) -> dict[str, Any]:
    """Get all channels that the user has access to.
    
    Args:
        include_public: Include all public channels
        include_subscribed: Include all channels that the user is subscribed to
        include_archived: Include archived channels
    """
    params = {
        "include_public": "true" if include_public else "false",
        "include_subscribed": "true" if include_subscribed else "false",
        "exclude_archived": "false" if include_archived else "true"
    }
    
    return make_request("GET", "/streams", params=params)


@mcp.tool()
def subscribe(streams: list[str], principals: list[str] | list[int] | None = None,
              announce: bool = False, invite_only: bool = False) -> dict[str, Any]:
    """Subscribe one or more users to one or more channels.
    
    Args:
        streams: List of channel names to subscribe to
        principals: List of user IDs or email addresses to subscribe
        announce: Whether to send an announcement about new channel creation
        invite_only: Whether to create private channels
    """
    data = {
        "subscriptions": json.dumps([{"name": name} for name in streams])
    }
    
    if principals is not None:
        data["principals"] = json.dumps(principals)
    
    if announce:
        data["announce"] = "true"
    
    if invite_only:
        data["invite_only"] = "true"
    
    return make_request("POST", "/users/me/subscriptions", data=data)


@mcp.tool()
def unsubscribe(streams: list[str], principals: list[str] | list[int] | None = None) -> dict[str, Any]:
    """Unsubscribe one or more users from one or more channels.
    
    Args:
        streams: List of channel names to unsubscribe from
        principals: List of user IDs or email addresses to unsubscribe
    """
    data = {
        "subscriptions": json.dumps([{"name": name} for name in streams])
    }
    
    if principals is not None:
        data["principals"] = json.dumps(principals)
    
    return make_request("DELETE", "/users/me/subscriptions", data=data)


@mcp.tool()
def create_stream(name: str, description: str = "", invite_only: bool = False,
                  is_web_public: bool = False) -> dict[str, Any]:
    """Create a new channel.
    
    Args:
        name: The name of the channel
        description: The description of the channel
        invite_only: Whether the channel should be private
        is_web_public: Whether the channel should be web-public
    """
    streams = [{"name": name, "description": description}]
    data = {"subscriptions": json.dumps(streams)}
    
    if invite_only:
        data["invite_only"] = "true"
    
    if is_web_public:
        data["is_web_public"] = "true"
    
    return make_request("POST", "/users/me/subscriptions", data=data)


@mcp.tool()
def update_stream(stream_id: int, name: str | None = None,
                  description: str | None = None) -> dict[str, Any]:
    """Update a channel's name or description.
    
    Args:
        stream_id: The channel ID
        name: The new name of the channel
        description: The new description of the channel
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    
    return make_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def archive_stream(stream_id: int) -> dict[str, Any]:
    """Archive a channel.
    
    Args:
        stream_id: The channel ID
    """
    data = {"is_archived": "true"}
    return make_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def get_stream_by_id(stream_id: int) -> dict[str, Any]:
    """Get a channel by its ID.
    
    Args:
        stream_id: The channel ID
    """
    return make_request("GET", f"/streams/{stream_id}")


@mcp.tool()
def get_stream_topics(stream_id: int) -> dict[str, Any]:
    """Get topics in a channel.
    
    Args:
        stream_id: The channel ID
    """
    return make_request("GET", f"/streams/{stream_id}/topics")


@mcp.tool()
def get_subscribers(stream_id: int) -> dict[str, Any]:
    """Get subscribers for a channel.
    
    Args:
        stream_id: The channel ID
    """
    return make_request("GET", f"/streams/{stream_id}/subscribers")


@mcp.tool()
def update_subscription_property(stream_id: int, property_name: str,
                                 property_value: str | int | bool) -> dict[str, Any]:
    """Update a subscription property for the current user.
    
    Args:
        stream_id: The channel ID
        property_name: The property to update (e.g., "pin", "color", "desktop_notifications",
                      "email_notifications", "wildcard_mentions_notify")
        property_value: The new value for the property
    """
    data = {
        "stream_id": str(stream_id),
        "property": property_name,
        "value": str(property_value).lower() if isinstance(property_value, bool) else str(property_value)
    }
    
    return make_request("PATCH", "/users/me/subscriptions/properties", data=data)


@mcp.tool()
def update_subscription_settings(settings: dict[str, str | int | bool]) -> dict[str, Any]:
    """Bulk update subscription settings for the current user.
    
    Args:
        settings: Dictionary of subscription properties to update
    """
    data = {"subscriptions": json.dumps([settings])}
    return make_request("PATCH", "/users/me/subscriptions", data=data)


# ============================================================================
# User Operations
# ============================================================================

@mcp.tool()
def get_users(client_gravatar: bool = True,
              include_custom_profile_fields: bool = False) -> dict[str, Any]:
    """Get all users in the organization.
    
    Args:
        client_gravatar: Whether the client supports computing gravatars URLs
        include_custom_profile_fields: Whether to include custom profile field data
    """
    params = {
        "client_gravatar": "true" if client_gravatar else "false",
        "include_custom_profile_fields": "true" if include_custom_profile_fields else "false"
    }
    
    return make_request("GET", "/users", params=params)


@mcp.tool()
def get_user(user_id: int) -> dict[str, Any]:
    """Get details on a single user.
    
    Args:
        user_id: The user's ID
    """
    return make_request("GET", f"/users/{user_id}")


@mcp.tool()
def get_user_by_email(email: str) -> dict[str, Any]:
    """Get details on a single user by email.
    
    Args:
        email: The user's email address
    """
    return make_request("GET", f"/users/{email}")


@mcp.tool()
def get_own_user() -> dict[str, Any]:
    """Get details on the current user."""
    return make_request("GET", "/users/me")


@mcp.tool()
def update_user(user_id: int, full_name: str | None = None,
                role: int | None = None,
                profile_data: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Update a user's details (admin only).
    
    Args:
        user_id: The target user's ID
        full_name: The user's full name
        role: New role for the user (100=owner, 200=admin, 300=moderator, 400=member, 600=guest)
        profile_data: Dictionary containing updated custom profile field data
    """
    data = {}
    
    if full_name is not None:
        data["full_name"] = full_name
    if role is not None:
        data["role"] = str(role)
    if profile_data is not None:
        data["profile_data"] = json.dumps(profile_data)
    
    return make_request("PATCH", f"/users/{user_id}", data=data)


@mcp.tool()
def update_user_by_email(email: str, full_name: str | None = None,
                         role: int | None = None) -> dict[str, Any]:
    """Update a user's details by email (admin only).
    
    Args:
        email: The user's email address
        full_name: The user's full name
        role: New role for the user (100=owner, 200=admin, 300=moderator, 400=member, 600=guest)
    """
    data = {}
    
    if full_name is not None:
        data["full_name"] = full_name
    if role is not None:
        data["role"] = str(role)
    
    return make_request("PATCH", f"/users/{email}", data=data)


@mcp.tool()
def deactivate_user(user_id: int) -> dict[str, Any]:
    """Deactivate a user (admin only).
    
    Args:
        user_id: The user's ID
    """
    return make_request("DELETE", f"/users/{user_id}")


@mcp.tool()
def reactivate_user(user_id: int) -> dict[str, Any]:
    """Reactivate a user (admin only).
    
    Args:
        user_id: The user's ID
    """
    data = {"user_id": str(user_id)}
    return make_request("POST", "/users/reactivate", data=data)


@mcp.tool()
def get_users_by_email(emails: list[str]) -> dict[str, Any]:
    """Get details on multiple users by email.
    
    Args:
        emails: List of user email addresses
    """
    params = {"email": emails}
    return make_request("GET", "/users", params=params)


@mcp.tool()
def get_user_presence(user_id: int) -> dict[str, Any]:
    """Get presence of a specific user.
    
    Args:
        user_id: The user's ID
    """
    return make_request("GET", f"/users/{user_id}/presence")


@mcp.tool()
def update_presence(status: str = "active", emoji_name: str | None = None,
                    emoji_code: str | None = None,
                    reaction_type: str = "unicode_emoji") -> dict[str, Any]:
    """Update the current user's presence.
    
    Args:
        status: Either "active" or "offline"
        emoji_name: The name of the emoji to set as your presence
        emoji_code: The emoji code
        reaction_type: Type of emoji: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji"
    """
    data = {
        "status": status
    }
    
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    
    return make_request("PATCH", "/presence", data=data)


@mcp.tool()
def set_typing_status(to: list[int], operator: str) -> dict[str, Any]:
    """Set the "typing" status for a direct message conversation.
    
    Args:
        to: List of recipient user IDs
        operator: Either "start" or "stop"
    """
    data = {
        "to": json.dumps(to),
        "operator": operator
    }
    
    return make_request("POST", "/typing", data=data)


@mcp.tool()
def get_subscriptions() -> dict[str, Any]:
    """Get the current user's subscriptions."""
    return make_request("GET", "/users/me/subscriptions")


@mcp.tool()
def get_user_subscriptions(user_id: int) -> dict[str, Any]:
    """Get a user's subscriptions.
    
    Args:
        user_id: The user's ID
    """
    return make_request("GET", f"/users/{user_id}/subscriptions")


# ============================================================================
# Draft Operations
# ============================================================================

@mcp.tool()
def get_drafts() -> dict[str, Any]:
    """Get all drafts for the current user."""
    return make_request("GET", "/drafts")


@mcp.tool()
def create_drafts(drafts: list[dict[str, Any]]) -> dict[str, Any]:
    """Create one or more drafts.
    
    Args:
        drafts: List of draft objects with type, to, message_topic, and content
    """
    data = {"drafts": json.dumps(drafts)}
    return make_request("POST", "/drafts", data=data)


@mcp.tool()
def edit_draft(draft_id: int, content: str, message_topic: str | None = None,
               to: list[int] | None = None, timestamp: int | None = None) -> dict[str, Any]:
    """Edit an existing draft.
    
    Args:
        draft_id: The draft's ID
        content: The updated content of the draft
        message_topic: The message_topic of the draft
        to: List of recipient user IDs
        timestamp: Unix timestamp of when the draft was last edited
    """
    data = {"content": content}
    
    if message_topic is not None:
        data["message_topic"] = message_topic
    if to is not None:
        data["to"] = json.dumps(to)
    if timestamp is not None:
        data["timestamp"] = str(timestamp)
    
    return make_request("PATCH", f"/drafts/{draft_id}", data=data)


@mcp.tool()
def delete_draft(draft_id: int) -> dict[str, Any]:
    """Delete a draft.
    
    Args:
        draft_id: The draft's ID
    """
    return make_request("DELETE", f"/drafts/{draft_id}")


# ============================================================================
# File Operations
# ============================================================================

@mcp.tool()
def upload_file(file_path: str) -> dict[str, Any]:
    """Upload a file and get the URL.
    
    Args:
        file_path: Path to the file to upload
    """
    try:
        with open(file_path, "rb") as fp:
            files = {"filename": fp}
            return make_request("POST", "/user_uploads", data={}, files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Failed to upload file: {str(e)}"}


@mcp.tool()
def get_file_temporary_url(attachment_id: str) -> dict[str, Any]:
    """Get a temporary URL for an attachment.
    
    Args:
        attachment_id: The ID of the attachment
    """
    return make_request("GET", f"/user_uploads/{attachment_id}/temporary_url")


@mcp.tool()
def delete_attachment(attachment_id: str) -> dict[str, Any]:
    """Delete an attachment.
    
    Args:
        attachment_id: The ID of the attachment
    """
    return make_request("DELETE", f"/user_uploads/{attachment_id}")


@mcp.tool()
def get_attachments() -> dict[str, Any]:
    """Get all attachments for the current user."""
    return make_request("GET", "/attachments")


# ============================================================================
# User Group Operations
# ============================================================================

@mcp.tool()
def get_user_groups() -> dict[str, Any]:
    """Get all user groups in the organization."""
    return make_request("GET", "/user_groups")


@mcp.tool()
def create_user_group(name: str, description: str, 
                      members: list[int] | None = None) -> dict[str, Any]:
    """Create a new user group.
    
    Args:
        name: The name of the user group
        description: The description of the user group
        members: List of user IDs to add to the group
    """
    data = {
        "name": name,
        "description": description
    }
    
    if members is not None:
        data["members"] = json.dumps(members)
    
    return make_request("POST", "/user_groups", data=data)


@mcp.tool()
def update_user_group(user_group_id: int, name: str | None = None,
                      description: str | None = None) -> dict[str, Any]:
    """Update a user group.
    
    Args:
        user_group_id: The user group's ID
        name: The new name of the user group
        description: The new description of the user group
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    
    return make_request("PATCH", f"/user_groups/{user_group_id}", data=data)


@mcp.tool()
def deactivate_user_group(user_group_id: int) -> dict[str, Any]:
    """Deactivate a user group.
    
    Args:
        user_group_id: The user group's ID
    """
    return make_request("DELETE", f"/user_groups/{user_group_id}")


@mcp.tool()
def get_user_group_members(user_group_id: int) -> dict[str, Any]:
    """Get members of a user group.
    
    Args:
        user_group_id: The user group's ID
    """
    return make_request("GET", f"/user_groups/{user_group_id}/members")


@mcp.tool()
def update_user_group_members(user_group_id: int, add: list[int] | None = None,
                              remove: list[int] | None = None) -> dict[str, Any]:
    """Update members of a user group.
    
    Args:
        user_group_id: The user group's ID
        add: List of user IDs to add to the group
        remove: List of user IDs to remove from the group
    """
    data = {}
    
    if add is not None:
        data["add"] = json.dumps(add)
    if remove is not None:
        data["remove"] = json.dumps(remove)
    
    return make_request("PATCH", f"/user_groups/{user_group_id}/members", data=data)


@mcp.tool()
def get_user_group_subgroups(user_group_id: int) -> dict[str, Any]:
    """Get subgroups of a user group.
    
    Args:
        user_group_id: The user group's ID
    """
    return make_request("GET", f"/user_groups/{user_group_id}/subgroups")


@mcp.tool()
def update_user_group_subgroups(user_group_id: int, add: list[int] | None = None,
                                remove: list[int] | None = None) -> dict[str, Any]:
    """Update subgroups of a user group.
    
    Args:
        user_group_id: The user group's ID
        add: List of user group IDs to add as subgroups
        remove: List of user group IDs to remove as subgroups
    """
    data = {}
    
    if add is not None:
        data["add"] = json.dumps(add)
    if remove is not None:
        data["remove"] = json.dumps(remove)
    
    return make_request("PATCH", f"/user_groups/{user_group_id}/subgroups", data=data)


# ============================================================================
# Topic Operations
# ============================================================================

@mcp.tool()
def delete_topic(stream_id: int, topic_name: str) -> dict[str, Any]:
    """Delete a topic in a channel.
    
    Args:
        stream_id: The channel ID
        topic_name: The name of the topic to delete
    """
    data = {
        "stream_id": str(stream_id),
        "topic_name": topic_name
    }
    
    return make_request("DELETE", "/messages", data=data)


@mcp.tool()
def rename_topic(stream_id: int, old_topic: str, new_topic: str,
                 propagate_mode: str = "change_one") -> dict[str, Any]:
    """Rename a topic in a channel.
    
    Args:
        stream_id: The channel ID
        old_topic: The current topic name
        new_topic: The new topic name
        propagate_mode: Which messages to update: "change_all", "change_later", "change_one"
    """
    data = {
        "stream_id": str(stream_id),
        "old_topic": old_topic,
        "new_topic": new_topic,
        "propagate_mode": propagate_mode
    }
    
    return make_request("POST", "/topics/rename", data=data)


@mcp.tool()
def update_user_topic(topic_name: str, visibility_policy: int) -> dict[str, Any]:
    """Update personal preferences for a topic.
    
    Args:
        topic_name: The topic name
        visibility_policy: The visibility policy (0=default, 1=unmuted, 2=ignored)
    """
    data = {
        "topic_name": topic_name,
        "visibility_policy": str(visibility_policy)
    }
    
    return make_request("PATCH", "/user_topics", data=data)


@mcp.tool()
def mute_topic(topic_name: str) -> dict[str, Any]:
    """Mute a topic.
    
    Args:
        topic_name: The topic name
    """
    data = {"topic_name": topic_name, "visibility_policy": "2"}
    return make_request("PATCH", "/user_topics", data=data)


@mcp.tool()
def unmute_topic(topic_name: str) -> dict[str, Any]:
    """Unmute a topic.
    
    Args:
        topic_name: The topic name
    """
    data = {"topic_name": topic_name, "visibility_policy": "1"}
    return make_request("PATCH", "/user_topics", data=data)


# ============================================================================
# Message Reminder Operations
# ============================================================================

@mcp.tool()
def create_message_reminder(to: list[int] | list[str], content: str,
                            scheduled_delivery_timestamp: int,
                            type_: str = "direct", message_topic: str | None = None) -> dict[str, Any]:
    """Create a message reminder.
    
    Args:
        to: List of recipient user IDs or email addresses
        content: The content of the message
        scheduled_delivery_timestamp: The UNIX timestamp for when the message will be sent
        type_: "direct" for direct message, "channel_name" for channel message
        message_topic: The message_topic of the message. Only required for channel messages.
    """
    data = {
        "type": type_,
        "to": json.dumps(to) if isinstance(to, list) else to,
        "content": content,
        "scheduled_delivery_timestamp": str(scheduled_delivery_timestamp)
    }
    
    if message_topic is not None:
        data["message_topic"] = message_topic
    
    return make_request("POST", "/reminders", data=data)


@mcp.tool()
def get_reminders() -> dict[str, Any]:
    """Get all message reminders for the current user."""
    return make_request("GET", "/reminders")


@mcp.tool()
def delete_reminder(reminder_id: int) -> dict[str, Any]:
    """Delete a message reminder.
    
    Args:
        reminder_id: The reminder's ID
    """
    return make_request("DELETE", f"/reminders/{reminder_id}")


# ============================================================================
# Flag/Status Operations
# ============================================================================

@mcp.tool()
def mark_all_as_read() -> dict[str, Any]:
    """Mark all messages as read."""
    return make_request("POST", "/mark_all_as_read")


@mcp.tool()
def mark_stream_as_read(stream_id: int) -> dict[str, Any]:
    """Mark all messages in a channel as read.
    
    Args:
        stream_id: The channel ID
    """
    data = {"stream_id": str(stream_id)}
    return make_request("POST", "/mark_stream_as_read", data=data)


@mcp.tool()
def mark_topic_as_read(stream_id: int, topic_name: str) -> dict[str, Any]:
    """Mark all messages in a topic as read.
    
    Args:
        stream_id: The channel ID
        topic_name: The topic name
    """
    data = {
        "stream_id": str(stream_id),
        "topic_name": topic_name
    }
    return make_request("POST", "/mark_topic_as_read", data=data)


@mcp.tool()
def update_status(status: str = "active", emoji_name: str | None = None,
                  emoji_code: str | None = None,
                  reaction_type: str = "unicode_emoji") -> dict[str, Any]:
    """Update the current user's status.
    
    Args:
        status: Either "active" or "offline"
        emoji_name: The name of the emoji to set as your status
        emoji_code: The emoji code
        reaction_type: Type of emoji: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji"
    """
    data = {"status": status}
    
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    
    return make_request("POST", "/user_status", data=data)


@mcp.tool()
def update_status_for_user(user_id: int, status: str | None = None,
                           emoji_name: str | None = None,
                           emoji_code: str | None = None,
                           reaction_type: str = "unicode_emoji") -> dict[str, Any]:
    """Update another user's status (admin only).
    
    Args:
        user_id: The target user's ID
        status: Either "active" or "offline"
        emoji_name: The name of the emoji to set as the user's status
        emoji_code: The emoji code
        reaction_type: Type of emoji: "unicode_emoji", "realm_emoji", or "zulip_extra_emoji"
    """
    data = {"user_id": str(user_id)}
    
    if status is not None:
        data["status"] = status
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    
    return make_request("POST", "/user_status", data=data)


@mcp.tool()
def get_user_status(user_id: int) -> dict[str, Any]:
    """Get a user's status.
    
    Args:
        user_id: The user's ID
    """
    return make_request("GET", f"/users/{user_id}/status")


# ============================================================================
# Navigation View Operations
# ============================================================================

@mcp.tool()
def get_navigation_views() -> dict[str, Any]:
    """Get all navigation views for the current user."""
    return make_request("GET", "/navigation_views")


@mcp.tool()
def add_navigation_view(name: str, icon: str = "hashtag",
                        operator: str = "channel",
                        operand: str | None = None) -> dict[str, Any]:
    """Add a navigation view.
    
    Args:
        name: The name of the navigation view
        icon: The icon for the navigation view
        operator: The operator for the filter ("channel", "is", "starred", etc.)
        operand: The operand for the filter
    """
    data = {
        "name": name,
        "icon": icon,
        "operator": operator
    }
    
    if operand is not None:
        data["operand"] = operand
    
    return make_request("POST", "/navigation_views", data=data)


@mcp.tool()
def update_navigation_view(navigation_view_id: int, name: str | None = None,
                           icon: str | None = None) -> dict[str, Any]:
    """Update a navigation view.
    
    Args:
        navigation_view_id: The navigation view's ID
        name: The new name of the navigation view
        icon: The new icon for the navigation view
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if icon is not None:
        data["icon"] = icon
    
    return make_request("PATCH", f"/navigation_views/{navigation_view_id}", data=data)


@mcp.tool()
def remove_navigation_view(navigation_view_id: int) -> dict[str, Any]:
    """Remove a navigation view.
    
    Args:
        navigation_view_id: The navigation view's ID
    """
    return make_request("DELETE", f"/navigation_views/{navigation_view_id}")


@mcp.tool()
def patch_channel_folders(channel_folders: list[dict[str, Any]]) -> dict[str, Any]:
    """Update channel folders configuration.
    
    Args:
        channel_folders: List of channel folder configurations
    """
    data = {"channel_folders": json.dumps(channel_folders)}
    return make_request("PATCH", "/channel_folders", data=data)


@mcp.tool()
def get_channel_folders() -> dict[str, Any]:
    """Get all channel folders for the current user."""
    return make_request("GET", "/channel_folders")


@mcp.tool()
def create_channel_folder(name: str, channels: list[int]) -> dict[str, Any]:
    """Create a channel folder.
    
    Args:
        name: The name of the channel folder
        channels: List of channel IDs to include in the folder
    """
    data = {
        "name": name,
        "channels": json.dumps(channels)
    }
    
    return make_request("POST", "/channel_folders/create", data=data)


@mcp.tool()
def update_channel_folder(folder_id: int, name: str | None = None,
                          channels: list[int] | None = None) -> dict[str, Any]:
    """Update a channel folder.
    
    Args:
        folder_id: The channel folder's ID
        name: The new name of the channel folder
        channels: List of channel IDs to include in the folder
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if channels is not None:
        data["channels"] = json.dumps(channels)
    
    return make_request("PATCH", f"/channel_folders/{folder_id}", data=data)


# ============================================================================
# Message Report Operations
# ============================================================================

@mcp.tool()
def report_message(message_id: int, reason: str | None = None) -> dict[str, Any]:
    """Report a message.
    
    Args:
        message_id: The message's ID
        reason: The reason for reporting the message
    """
    data = {"message_id": str(message_id)}
    
    if reason is not None:
        data["reason"] = reason
    
    return make_request("POST", "/messages/report", data=data)


# ============================================================================
# Server Operations
# ============================================================================

@mcp.tool()
def get_server_settings() -> dict[str, Any]:
    """Get server settings."""
    return make_request("GET", "/server_settings")


@mcp.tool()
def get_linkifiers() -> dict[str, Any]:
    """Get all linkifiers in the organization."""
    return make_request("GET", "/realm/linkifiers")


@mcp.tool()
def add_linkifier(pattern: str, url_format: str) -> dict[str, Any]:
    """Add a linkifier.
    
    Args:
        pattern: The regex pattern to match
        url_format: The URL format to link to (e.g., "https://example.com/{0}")
    """
    data = {
        "pattern": pattern,
        "url_format": url_format
    }
    
    return make_request("POST", "/realm/linkifiers", data=data)


@mcp.tool()
def update_linkifier(linkifier_id: int, pattern: str | None = None,
                     url_format: str | None = None) -> dict[str, Any]:
    """Update a linkifier.
    
    Args:
        linkifier_id: The linkifier's ID
        pattern: The new regex pattern
        url_format: The new URL format
    """
    data = {}
    
    if pattern is not None:
        data["pattern"] = pattern
    if url_format is not None:
        data["url_format"] = url_format
    
    return make_request("PATCH", f"/realm/linkifiers/{linkifier_id}", data=data)


@mcp.tool()
def remove_linkifier(linkifier_id: int) -> dict[str, Any]:
    """Remove a linkifier.
    
    Args:
        linkifier_id: The linkifier's ID
    """
    return make_request("DELETE", f"/realm/linkifiers/{linkifier_id}")


# ============================================================================
# Alert Words Operations
# ============================================================================

@mcp.tool()
def get_alert_words() -> dict[str, Any]:
    """Get all alert words for the current user."""
    return make_request("GET", "/alert_words")


@mcp.tool()
def add_alert_words(words: list[str]) -> dict[str, Any]:
    """Add alert words.
    
    Args:
        words: List of words to add
    """
    data = {"alert_words": json.dumps(words)}
    return make_request("POST", "/alert_words", data=data)


@mcp.tool()
def remove_alert_words(words: list[str]) -> dict[str, Any]:
    """Remove alert words.
    
    Args:
        words: List of words to remove
    """
    data = {"alert_words": json.dumps(words)}
    return make_request("DELETE", "/alert_words", data=data)


# ============================================================================
# Presence Operations
# ============================================================================

@mcp.tool()
def get_presence() -> dict[str, Any]:
    """Get presence of all users."""
    return make_request("GET", "/presence")


if __name__ == "__main__":
    mcp.run()
