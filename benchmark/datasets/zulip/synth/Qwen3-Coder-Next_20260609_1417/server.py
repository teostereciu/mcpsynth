#!/usr/bin/env python3
"""
Zulip MCP Server

An MCP server with comprehensive coverage of the Zulip REST API,
suitable for use by an autonomous agent completing real-world tasks.
"""

import os
import json
import requests
from typing import Any, Dict, List, Optional
from fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP(name="zulip", description="Zulip REST API server")

# Base URL template
BASE_URL = "{zulip_site}/api/v1"

# Environment variable names
ENV_VARS = {
    "email": "ZULIP_EMAIL",
    "api_key": "ZULIP_API_KEY",
    "site": "ZULIP_SITE",
}


def get_env(name: str) -> str:
    """Get environment variable, raise if missing."""
    value = os.environ.get(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def make_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to the Zulip API."""
    site = get_env(ENV_VARS["site"])
    email = get_env(ENV_VARS["email"])
    api_key = get_env(ENV_VARS["api_key"])

    url = BASE_URL.format(zulip_site=site.rstrip("/")) + endpoint

    auth = (email, api_key)

    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params, auth=auth)
        elif method.upper() == "POST":
            response = requests.post(url, params=params, json=data, auth=auth)
        elif method.upper() == "PATCH":
            response = requests.patch(url, params=params, json=data, auth=auth)
        elif method.upper() == "DELETE":
            response = requests.delete(url, auth=auth)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        # Handle response
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"raw_response": response.text}
        else:
            # Return error response from Zulip
            try:
                error_data = response.json()
                return error_data
            except json.JSONDecodeError:
                return {
                    "error": True,
                    "status_code": response.status_code,
                    "raw_response": response.text,
                }
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# Message Operations
# ============================================================================


@mcp.tool()
def send_stream_message(
    to: str,
    topic: str,
    content: str,
) -> Dict[str, Any]:
    """Send a stream (channel) message."""
    data = {"type": "stream", "to": to, "topic": topic, "content": content}
    return make_request("POST", "/messages", data=data)


@mcp.tool()
def send_private_message(
    to: List[int],
    content: str,
) -> Dict[str, Any]:
    """Send a private (direct) message."""
    data = {"type": "direct", "to": to, "content": content}
    return make_request("POST", "/messages", data=data)


@mcp.tool()
def get_messages(
    anchor: str = "newest",
    num_before: int = 100,
    num_after: int = 0,
    narrow: Optional[List[Dict[str, Any]]] = None,
    apply_markdown: bool = True,
    client_gravatar: bool = True,
) -> Dict[str, Any]:
    """Retrieve messages matching a narrow filter."""
    params = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "apply_markdown": apply_markdown,
        "client_gravatar": client_gravatar,
    }
    if narrow:
        params["narrow"] = json.dumps(narrow)
    return make_request("GET", "/messages", params=params)


@mcp.tool()
def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: str = "change_one",
    send_notification_to_old_thread: bool = False,
    send_notification_to_new_thread: bool = True,
) -> Dict[str, Any]:
    """Update a message's content or topic."""
    data = {
        "message_id": message_id,
        "propagate_mode": propagate_mode,
        "send_notification_to_old_thread": send_notification_to_old_thread,
        "send_notification_to_new_thread": send_notification_to_new_thread,
    }
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    return make_request("PATCH", f"/messages/{message_id}", data=data)


@mcp.tool()
def delete_message(message_id: int) -> Dict[str, Any]:
    """Delete a message permanently."""
    return make_request("DELETE", f"/messages/{message_id}")


@mcp.tool()
def get_message(message_id: int) -> Dict[str, Any]:
    """Fetch a single message by ID."""
    return make_request("GET", f"/messages/{message_id}")


@mcp.tool()
def get_message_history(message_id: int) -> Dict[str, Any]:
    """Get the edit history of a message."""
    return make_request("GET", f"/messages/{message_id}/history")


@mcp.tool()
def update_message_flags(
    flag: str,
    messages: List[int],
    operation: str = "add",
) -> Dict[str, Any]:
    """Update personal message flags (e.g., read, starred, collapsed)."""
    data = {"flag": flag, "messages": messages, "operator": operation}
    return make_request("POST", "/messages/flags", data=data)


@mcp.tool()
def add_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None) -> Dict[str, Any]:
    """Add an emoji reaction to a message."""
    data = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    return make_request("POST", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None) -> Dict[str, Any]:
    """Remove an emoji reaction from a message."""
    params = {"emoji_name": emoji_name}
    if emoji_code:
        params["emoji_code"] = emoji_code
    return make_request("DELETE", f"/messages/{message_id}/reactions", params=params)


@mcp.tool()
def mark_all_as_read() -> Dict[str, Any]:
    """Mark all unread messages as read."""
    return make_request("POST", "/mark_all_as_read")


@mcp.tool()
def mark_stream_as_read(stream_id: int) -> Dict[str, Any]:
    """Mark all messages in a stream as read."""
    return make_request("POST", f"/streams/{stream_id}/mark_all_as_read")


@mcp.tool()
def mark_topic_as_read(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """Mark all messages in a topic as read."""
    return make_request(
        "POST",
        f"/streams/{stream_id}/mark_topic_as_read",
        data={"topic_name": topic_name},
    )


@mcp.tool()
def render_message(content: str) -> Dict[str, Any]:
    """Render message content to HTML (for preview)."""
    return make_request("POST", "/render_message", data={"content": content})


# ============================================================================
# Scheduled Messages
# ============================================================================


@mcp.tool()
def create_scheduled_message(
    delivery_type: str,
    timestamp: str,
    type: str,
    to: str,
    topic: Optional[str] = None,
    content: Optional[str] = None,
) -> Dict[str, Any]:
    """Schedule a message to be sent later."""
    data = {"delivery_type": delivery_type, "timestamp": timestamp, "type": type, "to": to}
    if topic:
        data["topic"] = topic
    if content:
        data["content"] = content
    return make_request("POST", "/scheduled_messages", data=data)


@mcp.tool()
def get_scheduled_messages() -> Dict[str, Any]:
    """Get all scheduled messages."""
    return make_request("GET", "/scheduled_messages")


@mcp.tool()
def update_scheduled_message(
    scheduled_message_id: int,
    delivery_type: Optional[str] = None,
    timestamp: Optional[str] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a scheduled message."""
    data = {}
    if delivery_type:
        data["delivery_type"] = delivery_type
    if timestamp:
        data["timestamp"] = timestamp
    if content:
        data["content"] = content
    if topic:
        data["topic"] = topic
    return make_request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


@mcp.tool()
def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """Delete a scheduled message."""
    return make_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")


# ============================================================================
# Drafts
# ============================================================================


@mcp.tool()
def get_drafts() -> Dict[str, Any]:
    """Get all drafts for the current user."""
    return make_request("GET", "/drafts")


@mcp.tool()
def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create one or more drafts."""
    return make_request("POST", "/drafts", data={"drafts": drafts})


@mcp.tool()
def update_draft(draft_id: int, content: Optional[str] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """Update a draft."""
    data = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    return make_request("PATCH", f"/drafts/{draft_id}", data=data)


@mcp.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    """Delete a draft."""
    return make_request("DELETE", f"/drafts/{draft_id}")


# ============================================================================
# Streams (Channels)
# ============================================================================


@mcp.tool()
def get_streams(
    include_public: bool = True,
    include_subscribed: bool = True,
    exclude_archived: bool = True,
) -> Dict[str, Any]:
    """Get streams the user has access to."""
    params = {
        "include_public": include_public,
        "include_subscribed": include_subscribed,
        "exclude_archived": exclude_archived,
    }
    return make_request("GET", "/streams", params=params)


@mcp.tool()
def subscribe(
    streams: List[Dict[str, Any]],
    principals: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Subscribe users to streams."""
    data = {"subscriptions": json.dumps(streams)}
    if principals:
        data["principals"] = json.dumps(principals)
    return make_request("POST", "/users/me/subscriptions", data=data)


@mcp.tool()
def unsubscribe(streams: List[str]) -> Dict[str, Any]:
    """Unsubscribe from streams."""
    return make_request("POST", "/users/me/subscriptions", data={"subscriptions": json.dumps(streams)})


@mcp.tool()
def get_subscriptions() -> Dict[str, Any]:
    """Get streams the current user is subscribed to."""
    return make_request("GET", "/users/me/subscriptions")


@mcp.tool()
def get_subscribers(stream_id: int) -> Dict[str, Any]:
    """Get users subscribed to a stream."""
    return make_request("GET", f"/streams/{stream_id}/members")


@mcp.tool()
def create_stream(
    name: str,
    description: Optional[str] = None,
    invite_only: bool = False,
    is_web_public: bool = False,
    is_default_stream: bool = False,
) -> Dict[str, Any]:
    """Create a new stream."""
    streams = [{"name": name}]
    if description:
        streams[0]["description"] = description
    return subscribe(streams=streams)


@mcp.tool()
def update_stream(
    stream_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    is_private: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a stream's settings."""
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if is_private is not None:
        data["invite_only"] = is_private
    return make_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    """Archive a stream."""
    return make_request("DELETE", f"/streams/{stream_id}")


@mcp.tool()
def get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    """Get information about a specific stream."""
    return make_request("GET", f"/streams/{stream_id}")


@mcp.tool()
def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """Get topics in a stream."""
    return make_request("GET", f"/streams/{stream_id}/topics")


@mcp.tool()
def update_subscription_settings(
    stream_id: int,
    property: str,
    value: Any,
) -> Dict[str, Any]:
    """Update a subscription property for the current user."""
    return make_request("PATCH", f"/users/me/subscriptions/{stream_id}", data={"property": property, "value": value})


# ============================================================================
# Topics
# ============================================================================


@mcp.tool()
def rename_topic(
    stream_id: int,
    old_topic: str,
    new_topic: str,
    propagate_mode: str = "change_all",
) -> Dict[str, Any]:
    """Rename a topic in a stream."""
    return make_request(
        "POST",
        f"/streams/{stream_id}/rename_topic",
        data={"old_topic": old_topic, "new_topic": new_topic, "propagate_mode": propagate_mode},
    )


@mcp.tool()
def resolve_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """Mark a topic as resolved."""
    return make_request(
        "POST",
        f"/streams/{stream_id}/resolve_topic",
        data={"topic_name": topic_name},
    )


@mcp.tool()
def delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """Delete a topic by moving all its messages to the void."""
    return make_request(
        "POST",
        f"/streams/{stream_id}/delete_topic",
        data={"topic_name": topic_name},
    )


@mcp.tool()
def mute_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """Mute a topic."""
    return make_request(
        "POST",
        f"/users/me/subscriptions/muted_topics",
        data={"stream_id": stream_id, "topic_name": topic_name},
    )


@mcp.tool()
def unmute_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """Unmute a topic."""
    return make_request(
        "DELETE",
        f"/users/me/subscriptions/muted_topics",
        data={"stream_id": stream_id, "topic_name": topic_name},
    )


# ============================================================================
# Users
# ============================================================================


@mcp.tool()
def get_users() -> Dict[str, Any]:
    """Get all users in the organization."""
    return make_request("GET", "/users")


@mcp.tool()
def get_user(user_id: int) -> Dict[str, Any]:
    """Get a specific user by ID."""
    return make_request("GET", f"/users/{user_id}")


@mcp.tool()
def get_user_by_email(email: str) -> Dict[str, Any]:
    """Get a specific user by email."""
    return make_request("GET", f"/users/{email}")


@mcp.tool()
def get_own_user() -> Dict[str, Any]:
    """Get information about the current user."""
    return make_request("GET", "/users/me")


@mcp.tool()
def create_user(
    email: str,
    full_name: str,
    password: Optional[str] = None,
    short_name: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a new user."""
    data = {"email": email, "full_name": full_name}
    if password:
        data["password"] = password
    if short_name:
        data["short_name"] = short_name
    return make_request("POST", "/users", data=data)


@mcp.tool()
def update_user(user_id: int, **kwargs) -> Dict[str, Any]:
    """Update a user's profile information."""
    return make_request("PATCH", f"/users/{user_id}", data=kwargs)


@mcp.tool()
def update_user_by_email(email: str, **kwargs) -> Dict[str, Any]:
    """Update a user's profile information by email."""
    return make_request("PATCH", f"/users/{email}", data=kwargs)


@mcp.tool()
def deactivate_user(user_id: int) -> Dict[str, Any]:
    """Deactivate a user account."""
    return make_request("DELETE", f"/users/{user_id}")


@mcp.tool()
def reactivate_user(user_id: int) -> Dict[str, Any]:
    """Reactivate a deactivated user."""
    return make_request("POST", f"/users/{user_id}/reactivate")


@mcp.tool()
def get_user_presence(user_id: int) -> Dict[str, Any]:
    """Get presence information for a user."""
    return make_request("GET", f"/users/{user_id}/presence")


@mcp.tool()
def get_presence() -> Dict[str, Any]:
    """Get presence information for all users."""
    return make_request("GET", "/presence")


@mcp.tool()
def update_presence(status: str = "active", from_idle: bool = False) -> Dict[str, Any]:
    """Update your own presence status."""
    return make_request("POST", "/presence", data={"status": status, "from_idle": from_idle})


@mcp.tool()
def set_typing_status(to: List[int], op: str = "start") -> Dict[str, Any]:
    """Set the typing status for a direct message conversation."""
    return make_request("POST", "/typing", data={"to": to, "op": op})


@mcp.tool()
def update_user_status(
    away: Optional[bool] = None,
    status_text: Optional[str] = None,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
) -> Dict[str, Any]:
    """Update your own status."""
    data = {}
    if away is not None:
        data["away"] = away
    if status_text is not None:
        data["status_text"] = status_text
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    return make_request("POST", "/users/me/status", data=data)


@mcp.tool()
def update_user_topic(user_id: int, stream_id: int, mode: str) -> Dict[str, Any]:
    """Update a user's personal preferences for a topic."""
    return make_request("PATCH", f"/users/{user_id}/topics/{stream_id}", data={"mode": mode})


# ============================================================================
# User Groups
# ============================================================================


@mcp.tool()
def get_user_groups() -> Dict[str, Any]:
    """Get all user groups in the organization."""
    return make_request("GET", "/user_groups")


@mcp.tool()
def create_user_group(name: str, description: str, members: Optional[List[int]] = None) -> Dict[str, Any]:
    """Create a new user group."""
    data = {"name": name, "description": description}
    if members:
        data["members"] = json.dumps(members)
    return make_request("POST", "/user_groups", data=data)


@mcp.tool()
def update_user_group(user_group_id: int, **kwargs) -> Dict[str, Any]:
    """Update a user group."""
    return make_request("PATCH", f"/user_groups/{user_group_id}", data=kwargs)


@mcp.tool()
def delete_user_group(user_group_id: int) -> Dict[str, Any]:
    """Delete a user group."""
    return make_request("DELETE", f"/user_groups/{user_group_id}")


@mcp.tool()
def update_user_group_members(
    user_group_id: int,
    add: Optional[List[int]] = None,
    remove: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Update members of a user group."""
    data = {}
    if add:
        data["add"] = json.dumps(add)
    if remove:
        data["remove"] = json.dumps(remove)
    return make_request("POST", f"/user_groups/{user_group_id}/members", data=data)


@mcp.tool()
def get_user_group_members(user_group_id: int) -> Dict[str, Any]:
    """Get members of a user group."""
    return make_request("GET", f"/user_groups/{user_group_id}/members")


@mcp.tool()
def get_user_group_subgroups(user_group_id: int) -> Dict[str, Any]:
    """Get subgroups of a user group."""
    return make_request("GET", f"/user_groups/{user_group_id}/subgroups")


@mcp.tool()
def update_user_group_subgroups(
    user_group_id: int,
    add: Optional[List[int]] = None,
    remove: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Update subgroups of a user group."""
    data = {}
    if add:
        data["add"] = json.dumps(add)
    if remove:
        data["remove"] = json.dumps(remove)
    return make_request("POST", f"/user_groups/{user_group_id}/subgroups", data=data)


@mcp.tool()
def get_is_user_group_member(user_group_id: int, user_id: int) -> Dict[str, Any]:
    """Check if a user is a member of a user group."""
    return make_request("GET", f"/user_groups/{user_group_id}/members/{user_id}")


# ============================================================================
# File Upload and Attachments
# ============================================================================


@mcp.tool()
def upload_file(file_path: str, file_name: Optional[str] = None) -> Dict[str, Any]:
    """Upload a file to Zulip."""
    import os

    site = get_env(ENV_VARS["site"])
    email = get_env(ENV_VARS["email"])
    api_key = get_env(ENV_VARS["api_key"])

    url = BASE_URL.format(zulip_site=site.rstrip("/")) + "/user_uploads"
    auth = (email, api_key)

    try:
        with open(file_path, "rb") as f:
            files = {"file": (file_name or os.path.basename(file_path), f)}
            response = requests.post(url, files=files, auth=auth)

        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        else:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"error": True, "status_code": response.status_code, "raw_response": response.text}
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Upload failed: {str(e)}"}


@mcp.tool()
def get_attachments() -> Dict[str, Any]:
    """Get all attachments for the current user."""
    return make_request("GET", "/attachments")


@mcp.tool()
def delete_attachment(attachment_id: int) -> Dict[str, Any]:
    """Delete an attachment."""
    return make_request("DELETE", f"/attachments/{attachment_id}")


@mcp.tool()
def get_file_temporary_url(attachment_id: int) -> Dict[str, Any]:
    """Get a temporary URL for an attachment."""
    return make_request("GET", f"/user_uploads/temporary/{attachment_id}")


# ============================================================================
# Server Information
# ============================================================================


@mcp.tool()
def get_server_settings() -> Dict[str, Any]:
    """Get Zulip server settings."""
    return make_request("GET", "/server_settings")


@mcp.tool()
def get_realm_exports() -> Dict[str, Any]:
    """Get realm data export records."""
    return make_request("GET", "/export/realm")


@mcp.tool()
def export_realm(export_public_policy: str = "own", export_typ: str = "full") -> Dict[str, Any]:
    """Export realm data."""
    return make_request(
        "POST",
        "/export/realm",
        data={"public_policy": export_public_policy, "type": export_typ},
    )


# ============================================================================
# Custom Emoji
# ============================================================================


@mcp.tool()
def get_custom_emoji() -> Dict[str, Any]:
    """Get all custom emoji in the realm."""
    return make_request("GET", "/custom_emoji")


@mcp.tool()
def upload_custom_emoji(name: str, file_path: str) -> Dict[str, Any]:
    """Upload a custom emoji."""
    site = get_env(ENV_VARS["site"])
    email = get_env(ENV_VARS["email"])
    api_key = get_env(ENV_VARS["api_key"])

    url = BASE_URL.format(zulip_site=site.rstrip("/")) + "/custom_emoji"
    auth = (email, api_key)

    try:
        with open(file_path, "rb") as f:
            files = {"file": (name, f)}
            response = requests.post(url, files=files, auth=auth)

        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        else:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"error": True, "status_code": response.status_code, "raw_response": response.text}
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Upload failed: {str(e)}"}


@mcp.tool()
def deactivate_custom_emoji(emoji_id: int) -> Dict[str, Any]:
    """Deactivate a custom emoji."""
    return make_request("DELETE", f"/custom_emoji/{emoji_id}")


# ============================================================================
# Custom Profile Fields
# ============================================================================


@mcp.tool()
def get_custom_profile_fields() -> Dict[str, Any]:
    """Get all custom profile fields."""
    return make_request("GET", "/realm/profile_fields")


@mcp.tool()
def create_custom_profile_field(
    name: str,
    field_type: int,
    hint: str = "",
    required: bool = False,
    display_in_profile_summary: bool = False,
) -> Dict[str, Any]:
    """Create a custom profile field."""
    return make_request(
        "POST",
        "/realm/profile_fields",
        data={
            "name": name,
            "field_type": field_type,
            "hint": hint,
            "required": required,
            "display_in_profile_summary": display_in_profile_summary,
        },
    )


@mcp.tool()
def update_custom_profile_field(field_id: int, **kwargs) -> Dict[str, Any]:
    """Update a custom profile field."""
    return make_request("PATCH", f"/realm/profile_fields/{field_id}", data=kwargs)


@mcp.tool()
def reorder_custom_profile_fields(order: List[int]) -> Dict[str, Any]:
    """Reorder custom profile fields."""
    return make_request("POST", "/realm/profile_fields/order", data={"order": json.dumps(order)})


# ============================================================================
# Navigation Views
# ============================================================================


@mcp.tool()
def get_navigation_views() -> Dict[str, Any]:
    """Get all navigation views for the current user."""
    return make_request("GET", "/navigation_views")


@mcp.tool()
def add_navigation_view(name: str, fragment: str, is_pinned: bool = False) -> Dict[str, Any]:
    """Add a navigation view."""
    return make_request("POST", "/navigation_views", data={"name": name, "fragment": fragment, "is_pinned": is_pinned})


@mcp.tool()
def update_navigation_view(
    navigation_view_id: int,
    name: Optional[str] = None,
    fragment: Optional[str] = None,
    is_pinned: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a navigation view."""
    data = {}
    if name is not None:
        data["name"] = name
    if fragment is not None:
        data["fragment"] = fragment
    if is_pinned is not None:
        data["is_pinned"] = is_pinned
    return make_request("PATCH", f"/navigation_views/{navigation_view_id}", data=data)


@mcp.tool()
def remove_navigation_view(navigation_view_id: int) -> Dict[str, Any]:
    """Remove a navigation view."""
    return make_request("DELETE", f"/navigation_views/{navigation_view_id}")


# ============================================================================
# Channel Folders
# ============================================================================


@mcp.tool()
def get_channel_folders() -> Dict[str, Any]:
    """Get all channel folders for the current user."""
    return make_request("GET", "/channels/folders")


@mcp.tool()
def create_channel_folder(name: str, children: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Create a channel folder."""
    data = {"name": name}
    if children:
        data["children"] = json.dumps(children)
    return make_request("POST", "/channels/folders", data=data)


@mcp.tool()
def update_channel_folder(
    folder_id: int,
    name: Optional[str] = None,
    children: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Update a channel folder."""
    data = {}
    if name is not None:
        data["name"] = name
    if children is not None:
        data["children"] = json.dumps(children)
    return make_request("PATCH", f"/channels/folders/{folder_id}", data=data)


@mcp.tool()
def patch_channel_folders(folders: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Reorder channel folders."""
    return make_request("PATCH", "/channels/folders", data={"folders": json.dumps(folders)})


# ============================================================================
# Linkifiers
# ============================================================================


@mcp.tool()
def get_linkifiers() -> Dict[str, Any]:
    """Get all linkifiers in the realm."""
    return make_request("GET", "/realm/linkifiers")


@mcp.tool()
def add_linkifier(
    pattern: str,
    url_template: str,
    example_input: Optional[str] = None,
    reverse_template: Optional[str] = None,
) -> Dict[str, Any]:
    """Add a linkifier."""
    data = {"pattern": pattern, "url_template": url_template}
    if example_input:
        data["example_input"] = example_input
    if reverse_template:
        data["reverse_template"] = reverse_template
    return make_request("POST", "/realm/filters", data=data)


@mcp.tool()
def update_linkifier(filter_id: int, pattern: Optional[str] = None, url_template: Optional[str] = None) -> Dict[str, Any]:
    """Update a linkifier."""
    data = {}
    if pattern is not None:
        data["pattern"] = pattern
    if url_template is not None:
        data["url_template"] = url_template
    return make_request("PATCH", f"/realm/filters/{filter_id}", data=data)


@mcp.tool()
def remove_linkifier(filter_id: int) -> Dict[str, Any]:
    """Remove a linkifier."""
    return make_request("DELETE", f"/realm/filters/{filter_id}")


@mcp.tool()
def reorder_linkifiers(order: List[int]) -> Dict[str, Any]:
    """Reorder linkifiers."""
    return make_request("POST", "/realm/linkifiers/order", data={"order": json.dumps(order)})


# ============================================================================
# Code Playgrounds
# ============================================================================


@mcp.tool()
def add_code_playground(name: str, pygments_language: str, url_template: str) -> Dict[str, Any]:
    """Add a code playground."""
    return make_request(
        "POST",
        "/realm/playgrounds",
        data={"name": name, "pygments_language": pygments_language, "url_template": url_template},
    )


@mcp.tool()
def remove_code_playground(playground_id: int) -> Dict[str, Any]:
    """Remove a code playground."""
    return make_request("DELETE", f"/realm/playgrounds/{playground_id}")


# ============================================================================
# Alerts and Reminders
# ============================================================================


@mcp.tool()
def create_message_reminder(message_id: int, timestamp: str) -> Dict[str, Any]:
    """Create a message reminder."""
    return make_request("POST", "/reminders", data={"message_id": message_id, "timestamp": timestamp})


@mcp.tool()
def get_reminders() -> Dict[str, Any]:
    """Get all message reminders for the current user."""
    return make_request("GET", "/reminders")


@mcp.tool()
def delete_reminder(reminder_id: int) -> Dict[str, Any]:
    """Delete a message reminder."""
    return make_request("DELETE", f"/reminders/{reminder_id}")


# ============================================================================
# Default Streams
# ============================================================================


@mcp.tool()
def add_default_stream(stream_id: int) -> Dict[str, Any]:
    """Add a stream as a default stream."""
    return make_request("POST", "/default_streams", data={"stream_id": stream_id})


@mcp.tool()
def remove_default_stream(stream_id: int) -> Dict[str, Any]:
    """Remove a stream from default streams."""
    return make_request("DELETE", "/default_streams", data={"stream_id": stream_id})


# ============================================================================
# Saved Snippets
# ============================================================================


@mcp.tool()
def get_saved_snippets() -> Dict[str, Any]:
    """Get all saved snippets for the current user."""
    return make_request("GET", "/saved_snippets")


@mcp.tool()
def create_saved_snippet(name: str, content: str) -> Dict[str, Any]:
    """Create a saved snippet."""
    return make_request("POST", "/saved_snippets", data={"name": name, "content": content})


@mcp.tool()
def update_saved_snippet(snippet_id: int, name: Optional[str] = None, content: Optional[str] = None) -> Dict[str, Any]:
    """Update a saved snippet."""
    data = {}
    if name is not None:
        data["name"] = name
    if content is not None:
        data["content"] = content
    return make_request("PATCH", f"/saved_snippets/{snippet_id}", data=data)


@mcp.tool()
def delete_saved_snippet(snippet_id: int) -> Dict[str, Any]:
    """Delete a saved snippet."""
    return make_request("DELETE", f"/saved_snippets/{snippet_id}")


# ============================================================================
# Settings
# ============================================================================


@mcp.tool()
def update_settings(**kwargs) -> Dict[str, Any]:
    """Update user settings."""
    return make_request("PATCH", "/settings", data=kwargs)


@mcp.tool()
def update_user_settings_defaults(**kwargs) -> Dict[str, Any]:
    """Update realm-level defaults for user settings."""
    return make_request("PATCH", "/realm/user_settings_defaults", data=kwargs)


# ============================================================================
# Invitations
# ============================================================================


@mcp.tool()
def get_invites() -> Dict[str, Any]:
    """Get all invitations for the current user."""
    return make_request("GET", "/invites")


@mcp.tool()
def send_invites(invitee_emails: List[str], invitee_realm: int = 1) -> Dict[str, Any]:
    """Send email invitations."""
    return make_request("POST", "/invites", data={"invitee_emails": json.dumps(invitee_emails), "invitee_realm": invitee_realm})


@mcp.tool()
def create_invite_link(
    stream_ids: Optional[List[int]] = None,
    invite_expires_minutes: int = 7 * 24 * 60,
) -> Dict[str, Any]:
    """Create a reusable invitation link."""
    data = {"invite_expires_minutes": invite_expires_minutes}
    if stream_ids:
        data["stream_ids"] = json.dumps(stream_ids)
    return make_request("POST", "/invites/me", data=data)


@mcp.tool()
def resend_email_invite(invite_id: int) -> Dict[str, Any]:
    """Resend an email invitation."""
    return make_request("POST", f"/invites/{invite_id}/resend")


@mcp.tool()
def revoke_email_invite(invite_id: int) -> Dict[str, Any]:
    """Revoke an email invitation."""
    return make_request("DELETE", f"/invites/{invite_id}")


@mcp.tool()
def revoke_invite_link(invite_link_id: int) -> Dict[str, Any]:
    """Revoke a reusable invitation link."""
    return make_request("DELETE", f"/invites/me/{invite_link_id}")


# ============================================================================
# Additional Utilities
# ============================================================================


@mcp.tool()
def get_user_channels(user_id: int) -> Dict[str, Any]:
    """Get channels a user is subscribed to."""
    return make_request("GET", f"/users/{user_id}/channels")


@mcp.tool()
def get_subscription_status(stream_id: int) -> Dict[str, Any]:
    """Get subscription status for the current user."""
    return make_request("GET", f"/users/me/subscriptions/{stream_id}")


@mcp.tool()
def update_subscription_property(stream_id: int, property: str, value: Any) -> Dict[str, Any]:
    """Update a subscription property for the current user."""
    return make_request("PATCH", f"/users/me/subscriptions/{stream_id}", data={"property": property, "value": value})


@mcp.tool()
def bulk_update_subscription_settings(stream_id: int, settings: Dict[str, Any]) -> Dict[str, Any]:
    """Bulk update subscription settings."""
    return make_request("PATCH", f"/users/me/subscriptions/{stream_id}/settings", data=settings)


@mcp.tool()
def get_alert_words() -> Dict[str, Any]:
    """Get the user's alert words."""
    return make_request("GET", "/users/me/alert_words")


@mcp.tool()
def add_alert_words(words: List[str]) -> Dict[str, Any]:
    """Add alert words."""
    return make_request("POST", "/users/me/alert_words", data={"alert_words": json.dumps(words)})


@mcp.tool()
def remove_alert_words(words: List[str]) -> Dict[str, Any]:
    """Remove alert words."""
    return make_request("DELETE", "/users/me/alert_words", data={"alert_words": json.dumps(words)})


@mcp.tool()
def get_read_receipts(message_id: int) -> Dict[str, Any]:
    """Get read receipts for a message."""
    return make_request("GET", f"/messages/{message_id}/read_receipts")


@mcp.tool()
def regenerate_api_key() -> Dict[str, Any]:
    """Regenerate the current user's API key."""
    return make_request("POST", "/users/me/api_key/regenerate")


@mcp.tool()
def get_bot_api_key(bot_id: int) -> Dict[str, Any]:
    """Get a bot's API key."""
    return make_request("GET", f"/bots/{bot_id}/api_key")


@mcp.tool()
def regenerate_bot_api_key(bot_id: int) -> Dict[str, Any]:
    """Regenerate a bot's API key."""
    return make_request("POST", f"/bots/{bot_id}/api_key/regenerate")


@mcp.tool()
def mute_user(user_id: int) -> Dict[str, Any]:
    """Mute a user."""
    return make_request("POST", f"/users/{user_id}/mute")


@mcp.tool()
def unmute_user(user_id: int) -> Dict[str, Any]:
    """Unmute a user."""
    return make_request("DELETE", f"/users/{user_id}/mute")


@mcp.tool()
def get_stream_id(name: str) -> Dict[str, Any]:
    """Get the ID of a stream by name."""
    return make_request("GET", f"/streams/{name}/id")


@mcp.tool()
def get_stream_email_address(stream_id: int) -> Dict[str, Any]:
    """Get the email address of a stream."""
    return make_request("GET", f"/streams/{stream_id}/email_address")


@mcp.tool()
def deactivate_own_user(password: str) -> Dict[str, Any]:
    """Deactivate your own user account."""
    return make_request("DELETE", "/users/me", data={"password": password})


@mcp.tool()
def update_message_flags_for_narrow(flag: str, operation: str, narrow: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Update message flags for messages matching a narrow."""
    return make_request("POST", "/messages/flags/narrow", data={"flag": flag, "operator": operation, "narrow": json.dumps(narrow)})


@mcp.tool()
def test_notify(user_id: Optional[int] = None, email: Optional[str] = None, content: str = "Test notification") -> Dict[str, Any]:
    """Send a test notification to a user."""
    if user_id is not None:
        return make_request("POST", f"/users/{user_id}/notify", data={"content": content})
    elif email is not None:
        return make_request("POST", f"/users/{email}/notify", data={"content": content})
    else:
        return {"error": "Either user_id or email must be provided"}


@mcp.tool()
def report_message(message_id: int, reason: str) -> Dict[str, Any]:
    """Report a message."""
    return make_request("POST", f"/messages/{message_id}/report", data={"reason": reason})


if __name__ == "__main__":
    mcp.run()
