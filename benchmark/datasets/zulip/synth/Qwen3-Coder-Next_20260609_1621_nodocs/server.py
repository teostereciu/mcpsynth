"""
Zulip REST API MCP Server

This server provides MCP tools for interacting with the Zulip REST API.
"""

import os
import json
from typing import Any
from fastmcp.server import FastMCP
import requests

# Create the MCP server
mcp = FastMCP("zulip")

# Base URL for the Zulip API
ZULIP_API_URL = "{site}/api/v1"


def get_auth() -> tuple[str, str]:
    """Get authentication credentials from environment variables."""
    email = os.environ.get("ZULIP_EMAIL")
    api_key = os.environ.get("ZULIP_API_KEY")
    if not email or not api_key:
        raise ValueError("ZULIP_EMAIL and ZULIP_API_KEY environment variables must be set")
    return email, api_key


def get_site() -> str:
    """Get Zulip site URL from environment variables."""
    site = os.environ.get("ZULIP_SITE")
    if not site:
        raise ValueError("ZULIP_SITE environment variable must be set")
    return site


def api_request(method: str, endpoint: str, data: dict | None = None, params: dict | None = None) -> dict[str, Any]:
    """Make an authenticated request to the Zulip API."""
    site = get_site()
    email, api_key = get_auth()
    url = f"{ZULIP_API_URL.format(site=site)}{endpoint}"
    
    auth = (email, api_key)
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, auth=auth, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, auth=auth, data=data, params=params)
        elif method.upper() == "DELETE":
            response = requests.delete(url, auth=auth, params=params)
        elif method.upper() == "PATCH":
            response = requests.patch(url, auth=auth, json=data, params=params)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_detail = response.json()
            return {"error": str(error_detail), "status_code": response.status_code}
        except:
            return {"error": str(e), "status_code": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def send_message(
    type: str,
    to: str | list[str],
    subject: str | None = None,
    content: str | None = None,
    **kwargs
) -> dict[str, Any]:
    """Send a message to a stream or a user.
    
    Args:
        type: 'stream' or 'private'
        to: For streams, the stream name. For private messages, a single email address or a list of email addresses.
        subject: Required for stream messages.
        content: The content of the message.
        **kwargs: Additional parameters like mime_type, forward_original, etc.
    """
    data = {
        "type": type,
        "to": ",".join(to) if isinstance(to, list) else to,
        **kwargs
    }
    if subject:
        data["subject"] = subject
    if content:
        data["content"] = content
    
    return api_request("POST", "/messages", data=data)


@mcp.tool()
def get_messages(
    anchor: int | str = "newest",
    num_before: int = 100,
    num_after: int = 100,
    narrow: list[dict] | None = None,
    include_owner: bool = False,
    use_first_unread_anchor: bool = False,
) -> dict[str, Any]:
    """Fetch messages with optional narrowing.
    
    Args:
        anchor: Message ID to anchor the query, or 'oldest', 'newest', 'first_unread'
        num_before: Number of messages to fetch before the anchor
        num_after: Number of messages to fetch after the anchor
        narrow: List of narrowing criteria
        include_owner: Whether to include message owner information
        use_first_unread_anchor: Whether to use the first unread message as anchor
    """
    params = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "include_owner": str(include_owner).lower(),
        "use_first_unread_anchor": str(use_first_unread_anchor).lower()
    }
    if narrow:
        params["narrow"] = json.dumps(narrow)
    
    return api_request("GET", "/messages", params=params)


@mcp.tool()
def get_message_history(message_id: int) -> dict[str, Any]:
    """Get edit history for a message.
    
    Args:
        message_id: The ID of the message
    """
    return api_request("GET", f"/messages/{message_id}/history")


@mcp.tool()
def update_message(
    message_id: int,
    topic: str | None = None,
    content: str | None = None,
    send_notification_to_old_thread: bool | None = None,
    send_notification_to_new_thread: bool | None = None,
    propagate_mode: str | None = None,
    move_messages_to_existing_topic: bool | None = None,
) -> dict[str, Any]:
    """Update an existing message.
    
    Args:
        message_id: The ID of the message to update
        topic: New topic for the message (only for stream messages)
        content: New content for the message
        send_notification_to_old_thread: Whether to send a transition notification to the old thread
        send_notification_to_new_thread: Whether to send a transition notification to the new thread
        propagate_mode: How to propagate the change ('none', 'direct', 'all', 'historical')
        move_messages_to_existing_topic: Whether to move messages to an existing topic
    """
    data = {}
    if topic is not None:
        data["topic"] = topic
    if content is not None:
        data["content"] = content
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = str(send_notification_to_old_thread).lower()
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = str(send_notification_to_new_thread).lower()
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if move_messages_to_existing_topic is not None:
        data["move_messages_to_existing_topic"] = str(move_messages_to_existing_topic).lower()
    
    return api_request("PATCH", f"/messages/{message_id}", data=data)


@mcp.tool()
def delete_message(message_id: int) -> dict[str, Any]:
    """Delete a message.
    
    Args:
        message_id: The ID of the message to delete
    """
    return api_request("DELETE", f"/messages/{message_id}")


@mcp.tool()
def add_reaction(message_id: int, emoji_name: str, emoji_code: str | None = None, 
                 reaction_type: str | None = None) -> dict[str, Any]:
    """Add a reaction to a message.
    
    Args:
        message_id: The ID of the message
        emoji_name: The name of the emoji
        emoji_code: The emoji code (optional, auto-detected if not provided)
        reaction_type: Type of reaction ('unicode_emoji', 'realm_emoji', 'zulip_extra_emoji')
    """
    data = {
        "emoji_name": emoji_name,
        "emoji_code": emoji_code,
        "reaction_type": reaction_type
    }
    # Remove None values
    data = {k: v for k, v in data.items() if v is not None}
    
    return api_request("POST", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str, emoji_code: str | None = None,
                    reaction_type: str | None = None) -> dict[str, Any]:
    """Remove a reaction from a message.
    
    Args:
        message_id: The ID of the message
        emoji_name: The name of the emoji
        emoji_code: The emoji code (optional)
        reaction_type: Type of reaction ('unicode_emoji', 'realm_emoji', 'zulip_extra_emoji')
    """
    data = {
        "emoji_name": emoji_name,
        "emoji_code": emoji_code,
        "reaction_type": reaction_type
    }
    data = {k: v for k, v in data.items() if v is not None}
    
    return api_request("DELETE", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def create_stream(
    name: str,
    description: str,
    type: str | None = None,
    invite_only: bool | None = None,
    is_web_public: bool | None = None,
    history_public_to_subscribers: bool | None = None,
    visible_in_directory: bool | None = None,
    send_welcome_messages: bool | None = None,
    default_stream_group: str | None = None,
) -> dict[str, Any]:
    """Create a new stream.
    
    Args:
        name: The name of the stream (required)
        description: The description of the stream (required)
        type: 'public' or 'private' (default: 'public')
        invite_only: Whether the stream is invite-only
        is_web_public: Whether the stream is web-public
        history_public_to_subscribers: Whether message history is public to subscribers
        visible_in_directory: Whether the stream appears in the organization directory
        send_welcome_messages: Whether to send welcome messages to new subscribers
        default_stream_group: Name of a default stream group to add the stream to
    """
    data = {
        "name": name,
        "description": description,
    }
    if type is not None:
        data["type"] = type
    if invite_only is not None:
        data["invite_only"] = str(invite_only).lower()
    if is_web_public is not None:
        data["is_web_public"] = str(is_web_public).lower()
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = str(history_public_to_subscribers).lower()
    if visible_in_directory is not None:
        data["visible_in_directory"] = str(visible_in_directory).lower()
    if send_welcome_messages is not None:
        data["send_welcome_messages"] = str(send_welcome_messages).lower()
    if default_stream_group is not None:
        data["default_stream_group"] = default_stream_group
    
    return api_request("POST", "/streams", data=data)


@mcp.tool()
def update_stream(
    stream_id: int,
    name: str | None = None,
    description: str | None = None,
    is_private: bool | None = None,
    is_web_public: bool | None = None,
    history_public_to_subscribers: bool | None = None,
    visible_in_directory: bool | None = None,
) -> dict[str, Any]:
    """Update a stream.
    
    Args:
        stream_id: The ID of the stream to update
        name: New name for the stream
        description: New description for the stream
        is_private: Whether the stream is private
        is_web_public: Whether the stream is web-public
        history_public_to_subscribers: Whether message history is public to subscribers
        visible_in_directory: Whether the stream appears in the directory
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = str(is_private).lower()
    if is_web_public is not None:
        data["is_web_public"] = str(is_web_public).lower()
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = str(history_public_to_subscribers).lower()
    if visible_in_directory is not None:
        data["visible_in_directory"] = str(visible_in_directory).lower()
    
    return api_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def delete_stream(stream_id: int) -> dict[str, Any]:
    """Delete a stream.
    
    Args:
        stream_id: The ID of the stream to delete
    """
    return api_request("DELETE", f"/streams/{stream_id}")


@mcp.tool()
def archive_stream(stream_id: int) -> dict[str, Any]:
    """Archive a stream.
    
    Args:
        stream_id: The ID of the stream to archive
    """
    data = {"flag": "is_archived"}
    return api_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def subscribe(
    target: str | list[str],
    streams: str | list[str],
    principals: str | list[str] | None = None,
    authorization_errors_fatal: bool = True,
) -> dict[str, Any]:
    """Subscribe users to streams.
    
    Args:
        target: 'stream' to subscribe users to streams, or 'user' to subscribe the current user
        streams: Stream name(s) to subscribe to
        principals: User(s) to subscribe (email addresses or 'all')
        authorization_errors_fatal: Whether to fail on authorization errors
    """
    data = {
        "streams": json.dumps(streams) if isinstance(streams, list) else streams,
        "principals": json.dumps(principals) if isinstance(principals, list) else principals,
        "authorization_errors_fatal": str(authorization_errors_fatal).lower()
    }
    
    if target == "user":
        data.pop("principals")
    
    return api_request("POST", "/users/me/memberships", data=data)


@mcp.tool()
def unsubscribe(
    target: str | list[str],
    streams: str | list[str],
    principals: str | list[str] | None = None,
) -> dict[str, Any]:
    """Unsubscribe users from streams.
    
    Args:
        target: 'stream' to unsubscribe users from streams, or 'user' to unsubscribe the current user
        streams: Stream name(s) to unsubscribe from
        principals: User(s) to unsubscribe (email addresses or 'all')
    """
    data = {
        "streams": json.dumps(streams) if isinstance(streams, list) else streams,
    }
    
    if target == "user":
        return api_request("DELETE", "/users/me/memberships", data=data)
    else:
        data["principals"] = json.dumps(principals) if isinstance(principals, list) else principals
        return api_request("DELETE", "/users/memberships", data=data)


@mcp.tool()
def get_stream_id(stream_name: str) -> dict[str, Any]:
    """Get the ID for a stream.
    
    Args:
        stream_name: The name of the stream
    """
    return api_request("GET", f"/streams/{stream_name}/id")


@mcp.tool()
def get_stream_topics(stream_id: int) -> dict[str, Any]:
    """Get all topics in a stream.
    
    Args:
        stream_id: The ID of the stream
    """
    return api_request("GET", f"/streams/{stream_id}/topics")


@mcp.tool()
def update_message_flags(
    operation: str,
    flag: str,
    messages: list[int],
    stream: int | None = None,
    topic: str | None = None,
) -> dict[str, Any]:
    """Update message flags.
    
    Args:
        operation: 'add' or 'remove'
        flag: The flag to update ('read', 'mentioned', 'wildcard_mentioned', 
              'subscribed', 'has_alert_word', 'is_me_message', 'historical', 
              'cross_posted', 'has_reaction_emoji')
        messages: List of message IDs
        stream: Stream ID (optional, for stream-level operations)
        topic: Topic name (optional, for topic-level operations)
    """
    data = {
        "operation": operation,
        "flag": flag,
        "messages": json.dumps(messages)
    }
    if stream is not None:
        data["stream"] = stream
    if topic is not None:
        data["topic"] = topic
    
    return api_request("POST", "/messages/flags", data=data)


@mcp.tool()
def get_user_by_email(email: str) -> dict[str, Any]:
    """Get a user's profile by email address.
    
    Args:
        email: The user's email address
    """
    return api_request("GET", f"/users/{email}")


@mcp.tool()
def get_user_profile(user_id: int) -> dict[str, Any]:
    """Get a user's profile by user ID.
    
    Args:
        user_id: The user's ID
    """
    return api_request("GET", f"/users/{user_id}")


@mcp.tool()
def get_users() -> dict[str, Any]:
    """Get all users in the organization."""
    return api_request("GET", "/users")


@mcp.tool()
def get_user_presence(email: str) -> dict[str, Any]:
    """Get presence information for a user.
    
    Args:
        email: The user's email address
    """
    return api_request("GET", f"/users/{email}/presence")


@mcp.tool()
def get_presences() -> dict[str, Any]:
    """Get presence information for all users in the organization."""
    return api_request("GET", "/presence")


@mcp.tool()
def update_presence(
    status: str = "active",
    ping_only: bool = False,
) -> dict[str, Any]:
    """Update your presence.
    
    Args:
        status: 'active' or 'idle'
        ping_only: If True, just ping the server without updating status
    """
    data = {
        "status": status,
        "ping_only": str(ping_only).lower()
    }
    
    return api_request("POST", "/settings/presence", data=data)


@mcp.tool()
def upload_file(file_path: str, filename: str | None = None) -> dict[str, Any]:
    """Upload a file to Zulip.
    
    Args:
        file_path: Path to the file to upload
        filename: Optional filename to use instead of the actual file name
    """
    try:
        with open(file_path, "rb") as f:
            files = {"file": (filename or os.path.basename(file_path), f)}
            return api_request("POST", "/user_uploads", files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_user_groups() -> dict[str, Any]:
    """Get all user groups in the organization."""
    return api_request("GET", "/user_groups")


@mcp.tool()
def create_user_group(
    name: str,
    members: list[int] | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Create a new user group.
    
    Args:
        name: Name of the group
        members: List of user IDs to add to the group
        description: Description of the group
    """
    data = {"name": name}
    if members:
        data["members"] = json.dumps(members)
    if description:
        data["description"] = description
    
    return api_request("POST", "/user_groups", data=data)


@mcp.tool()
def update_user_group(
    group_id: int,
    name: str | None = None,
    description: str | None = None,
    add_members: list[int] | None = None,
    remove_members: list[int] | None = None,
) -> dict[str, Any]:
    """Update a user group.
    
    Args:
        group_id: ID of the group to update
        name: New name for the group
        description: New description for the group
        add_members: List of user IDs to add to the group
        remove_members: List of user IDs to remove from the group
    """
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if add_members:
        data["add_members"] = json.dumps(add_members)
    if remove_members:
        data["remove_members"] = json.dumps(remove_members)
    
    return api_request("PATCH", f"/user_groups/{group_id}", data=data)


@mcp.tool()
def delete_user_group(group_id: int) -> dict[str, Any]:
    """Delete a user group.
    
    Args:
        group_id: ID of the group to delete
    """
    return api_request("DELETE", f"/user_groups/{group_id}")


@mcp.tool()
def get_scheduled_messages() -> dict[str, Any]:
    """Get all scheduled messages."""
    return api_request("GET", "/scheduled_messages")


@mcp.tool()
def create_scheduled_message(
    type: str,
    to: str | list[str],
    content: str,
    delivery_type: str,
    deliver_at: str,
    subject: str | None = None,
) -> dict[str, Any]:
    """Create a scheduled message.
    
    Args:
        type: 'stream' or 'private'
        to: Stream name or user email(s)
        content: Message content
        delivery_type: 'send_later' or 'send_asap'
        deliver_at: ISO 8601 timestamp for when to send
        subject: Required for stream messages
    """
    data = {
        "type": type,
        "to": ",".join(to) if isinstance(to, list) else to,
        "content": content,
        "delivery_type": delivery_type,
        "deliver_at": deliver_at
    }
    if subject:
        data["subject"] = subject
    
    return api_request("POST", "/scheduled_messages", data=data)


@mcp.tool()
def delete_scheduled_message(scheduled_message_id: int) -> dict[str, Any]:
    """Delete a scheduled message.
    
    Args:
        scheduled_message_id: ID of the scheduled message to delete
    """
    return api_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")


@mcp.tool()
def get_drafts() -> dict[str, Any]:
    """Get all drafts for the current user."""
    return api_request("GET", "/drafts")


@mcp.tool()
def create_draft(
    type: str,
    to: str | list[str],
    content: str,
    subject: str | None = None,
    *args, **kwargs
) -> dict[str, Any]:
    """Create a draft.
    
    Args:
        type: 'stream' or 'private'
        to: Stream name or user email(s)
        content: Draft content
        subject: Required for stream drafts
    """
    data = {
        "type": type,
        "to": ",".join(to) if isinstance(to, list) else to,
        "content": content,
    }
    if subject:
        data["subject"] = subject
    
    return api_request("POST", "/drafts", data=data)


@mcp.tool()
def update_draft(
    draft_id: int,
    type: str,
    to: str | list[str],
    content: str,
    subject: str | None = None,
) -> dict[str, Any]:
    """Update an existing draft.
    
    Args:
        draft_id: ID of the draft to update
        type: 'stream' or 'private'
        to: Stream name or user email(s)
        content: Draft content
        subject: Required for stream drafts
    """
    data = {
        "type": type,
        "to": ",".join(to) if isinstance(to, list) else to,
        "content": content,
    }
    if subject:
        data["subject"] = subject
    
    return api_request("PATCH", f"/drafts/{draft_id}", data=data)


@mcp.tool()
def delete_draft(draft_id: int) -> dict[str, Any]:
    """Delete a draft.
    
    Args:
        draft_id: ID of the draft to delete
    """
    return api_request("DELETE", f"/drafts/{draft_id}")


@mcp.tool()
def get_stream_settings(stream_id: int) -> dict[str, Any]:
    """Get settings for a stream.
    
    Args:
        stream_id: ID of the stream
    """
    return api_request("GET", f"/streams/{stream_id}")


@mcp.tool()
def update_stream_settings(
    stream_id: int,
    name: str | None = None,
    description: str | None = None,
    is_private: bool | None = None,
    is_web_public: bool | None = None,
    history_public_to_subscribers: bool | None = None,
    visible_in_directory: bool | None = None,
    send_welcome_messages: bool | None = None,
    default_stream_group: str | None = None,
    invite_only: bool | None = None,
) -> dict[str, Any]:
    """Update stream settings.
    
    Args:
        stream_id: ID of the stream
        name: New name for the stream
        description: New description
        is_private: Whether the stream is private
        is_web_public: Whether the stream is web-public
        history_public_to_subscribers: Whether message history is public to subscribers
        visible_in_directory: Whether the stream appears in directory
        send_welcome_messages: Whether to send welcome messages
        default_stream_group: Default stream group
        invite_only: Whether the stream is invite-only
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = str(is_private).lower()
    if is_web_public is not None:
        data["is_web_public"] = str(is_web_public).lower()
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = str(history_public_to_subscribers).lower()
    if visible_in_directory is not None:
        data["visible_in_directory"] = str(visible_in_directory).lower()
    if send_welcome_messages is not None:
        data["send_welcome_messages"] = str(send_welcome_messages).lower()
    if default_stream_group is not None:
        data["default_stream_group"] = default_stream_group
    if invite_only is not None:
        data["invite_only"] = str(invite_only).lower()
    
    return api_request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def get_subscribers(stream_id: int) -> dict[str, Any]:
    """Get subscribers for a stream.
    
    Args:
        stream_id: ID of the stream
    """
    return api_request("GET", f"/streams/{stream_id}/members")


@mcp.tool()
def get_stream_subscribers(stream_id: int) -> dict[str, Any]:
    """Alias for get_subscribers for convenience."""
    return get_subscribers(stream_id)


@mcp.tool()
def add_subscribers(stream_id: int, subscription: list[str]) -> dict[str, Any]:
    """Add subscribers to a stream.
    
    Args:
        stream_id: ID of the stream
        subscription: List of user emails or 'all'
    """
    data = {
        "subscription": json.dumps(subscription)
    }
    
    return api_request("POST", f"/streams/{stream_id}/members", data=data)


@mcp.tool()
def remove_subscribers(stream_id: int, subscription: list[str]) -> dict[str, Any]:
    """Remove subscribers from a stream.
    
    Args:
        stream_id: ID of the stream
        subscription: List of user emails to remove
    """
    data = {
        "subscription": json.dumps(subscription)
    }
    
    return api_request("DELETE", f"/streams/{stream_id}/members", data=data)


if __name__ == "__main__":
    mcp.run()
