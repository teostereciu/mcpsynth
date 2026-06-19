import os
import logging
from typing import Dict, Any, Optional, List
from fastmcp import FastMCP, Context, ToolContext
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create MCP server
app = FastMCP(
    name="zulip-mcp",
    version="1.0.0",
)

# Zulip configuration
ZULIP_EMAIL = os.getenv("ZULIP_EMAIL")
ZULIP_API_KEY = os.getenv("ZULIP_API_KEY")
ZULIP_SITE = os.getenv("ZULIP_SITE", "https://your-org.zulipchat.com")

if not ZULIP_EMAIL or not ZULIP_API_KEY:
    logger.warning("ZULIP_EMAIL or ZULIP_API_KEY environment variables not set")

BASE_URL = f"{ZULIP_SITE.rstrip('/')}/api/v1"

def _build_auth() -> requests.auth.HTTPBasicAuth:
    """Build HTTP Basic Auth credentials"""
    return requests.auth.HTTPBasicAuth(ZULIP_EMAIL, ZULIP_API_KEY)

def _make_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Make a request to the Zulip API"""
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    auth = _build_auth()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            auth=auth,
            params=params,
            data=data,
            json=json,
            files=files,
            timeout=30
        )
        
        result = response.json()
        
        # Return error as dict instead of raising exception
        if response.status_code >= 400:
            logger.error(f"Zulip API error: {response.status_code} - {result.get('msg', 'Unknown error')}")
            return {"error": result.get("msg", "API request failed"), "code": result.get("code")}
        
        return result
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return {"error": f"Request failed: {str(e)}"}
    except ValueError as e:
        logger.error(f"Failed to parse JSON response: {e}")
        return {"error": f"Failed to parse response: {str(e)}"}


# ===== Messages =====

@app.tool(title="send_message")
async def send_message(
    ctx: Context,
    message_type: str,
    to: str,
    content: str,
    topic: Optional[str] = None
) -> Dict[str, Any]:
    """Send a Zulip message (channel or direct).
    
    message_type: 'channel' for channel messages, 'direct' for direct messages
    to: For channels, the name or ID; for direct messages, a list of user IDs or emails
    content: The message content
    topic: Optional topic for channel messages"""
    
    data = {
        "type": message_type,
        "to": to,
        "content": content,
    }
    
    if topic is not None:
        data["topic"] = topic
    
    return _make_request("POST", "messages", json=data)


@app.tool(title="edit_message")
async def edit_message(
    ctx: Context,
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Edit a Zulip message.
    
    message_id: ID of the message to edit
    content: New message content (optional)
    topic: New topic name (optional)
    propagate_mode: 'change_later', 'change_one', 'change_all'"""
    
    data = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    
    return _make_request("PATCH", f"messages/{message_id}", json=data)


@app.tool(title="delete_message")
async def delete_message(
    ctx: Context,
    message_id: int,
) -> Dict[str, Any]:
    """Delete a Zulip message.
    
    message_id: ID of the message to delete"""
    
    return _make_request("DELETE", f"messages/{message_id}")


@app.tool(title="get_message")
async def get_message(
    ctx: Context,
    message_id: int,
    apply_markdown: Optional[bool] = None,
    allow_empty_topic_name: Optional[bool] = None,
) -> Dict[str, Any]:
    """Fetch a single Zulip message by ID.
    
    message_id: ID of the message to fetch
    apply_markdown: Whether to apply Markdown rendering
    allow_empty_topic_name: Whether to support empty topics"""
    
    params = {}
    if apply_markdown is not None:
        params["apply_markdown"] = str(apply_markdown).lower()
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = str(allow_empty_topic_name).lower()
    
    return _make_request("GET", f"messages/{message_id}", params=params)


@app.tool(title="get_messages")
async def get_messages(
    ctx: Context,
    anchor: Optional[int] = None,
    num_before: int = 100,
    num_after: int = 0,
    narrow: Optional[List[Dict[str, str]]] = None,
) -> Dict[str, Any]:
    """Get messages with optional filtering.
    
    anchor: ID around which to fetch messages
    num_before: Number of messages before anchor
    num_after: Number of messages after anchor
    narrow: Optional narrow filter specification"""
    
    params = {
        "num_before": num_before,
        "num_after": num_after,
    }
    
    if anchor is not None:
        params["anchor"] = anchor
    if narrow is not None:
        params["narrow"] = str(narrow)
    
    return _make_request("GET", "messages", params=params)


@app.tool(title="add_reaction")
async def add_reaction(
    ctx: Context,
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """Add an emoji reaction to a Zulip message.
    
    message_id: ID of the target message
    emoji_name: Name of the emoji (e.g., 'octopus')
    emoji_code: Optional emoji code for specificity
    reaction_type: Optional type ('unicode_emoji', 'realm_emoji', 'zulip_extra_emoji')"""
    
    data = {"emoji_name": emoji_name}
    
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    
    return _make_request("POST", f"messages/{message_id}/reactions", json=data)


@app.tool(title="remove_reaction")
async def remove_reaction(
    ctx: Context,
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """Remove an emoji reaction from a Zulip message.
    
    message_id: ID of the target message
    emoji_name: Name of the emoji to remove
    emoji_code: Optional emoji code
    reaction_type: Optional reaction type"""
    
    data = {"emoji_name": emoji_name}
    
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    
    return _make_request("DELETE", f"messages/{message_id}/reactions", json=data)


@app.tool(title="update_message_flags")
async def update_message_flags(
    ctx: Context,
    flag: str,
    messages: List[int],
    op: str = "add",
) -> Dict[str, Any]:
    """Update personal message flags for specific messages.
    
    flag: The flag name (e.g., 'read', 'starred', 'wildcard_mentioned')
    messages: List of message IDs
    op: Operation ('add' or 'remove')"""
    
    return _make_request("POST", "messages/flags", json={
        "flag": flag,
        "messages": messages,
        "op": op,
    })


@app.tool(title="report_message")
async def report_message(
    ctx: Context,
    message_id: int,
    reason: str,
) -> Dict[str, Any]:
    """Report a Zulip message.
    
    message_id: ID of the message to report
    reason: Reason for reporting"""
    
    return _make_request("POST", "reports", json={
        "content": f"Message {message_id}: {reason}"
    })


@app.tool(title="mark_all_as_read")
async def mark_all_as_read(
    ctx: Context,
) -> Dict[str, Any]:
    """Mark all messages as read."""
    
    return _make_request("POST", "mark_all_as_read")


@app.tool(title="mark_stream_as_read")
async def mark_stream_as_read(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Mark all messages in a stream as read.
    
    stream_id: ID of the stream"""
    
    return _make_request("POST", "mark_stream_as_read", json={
        "stream_id": stream_id,
    })


@app.tool(title="mark_topic_as_read")
async def mark_topic_as_read(
    ctx: Context,
    stream_id: int,
    topic_name: str,
) -> Dict[str, Any]:
    """Mark all messages in a topic as read.
    
    stream_id: ID of the stream
    topic_name: Name of the topic"""
    
    return _make_request("POST", "mark_topic_as_read", json={
        "stream_id": stream_id,
        "topic_name": topic_name,
    })


@app.tool(title="get_message_history")
async def get_message_history(
    ctx: Context,
    message_id: int,
) -> Dict[str, Any]:
    """Get a message's edit history.
    
    message_id: ID of the message"""
    
    return _make_request("GET", f"messages/{message_id}/history")


@app.tool(title="render_message")
async def render_message(
    ctx: Context,
    content: str,
) -> Dict[str, Any]:
    """Render Zulip-flavored Markdown to HTML.
    
    content: Raw Markdown content"""
    
    return _make_request("POST", "render", json={"content": content})


@app.tool(title="check_messages_match_narrow")
async def check_messages_match_narrow(
    ctx: Context,
    narrow: List[Dict[str, str]],
) -> Dict[str, Any]:
    """Check if messages match a narrow filter.
    
    narrow: Narrow filter specification"""
    
    return _make_request("POST", "messages/matches_narrow", json={"narrow": narrow})


# ===== Scheduled Messages & Reminders =====

@app.tool(title="get_scheduled_messages")
async def get_scheduled_messages(
    ctx: Context,
) -> Dict[str, Any]:
    """Get all scheduled messages."""
    
    return _make_request("GET", "scheduled_messages")


@app.tool(title="create_scheduled_message")
async def create_scheduled_message(
    ctx: Context,
    type: str,
    to: str,
    content: str,
    scheduled_timestamp: int,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a scheduled Zulip message.
    
    type: 'channel' or 'direct'
    to: Recipients (channel name or user list)
    content: Message content
    scheduled_timestamp: UNIX timestamp for scheduling
    topic: Optional topic for channel messages"""
    
    data = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_timestamp": scheduled_timestamp,
    }
    
    if topic is not None:
        data["topic"] = topic
    
    return _make_request("POST", "scheduled_messages", json=data)


@app.tool(title="update_scheduled_message")
async def update_scheduled_message(
    ctx: Context,
    scheduled_message_id: int,
    content: Optional[str] = None,
    scheduled_timestamp: Optional[int] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a scheduled Zulip message.
    
    scheduled_message_id: ID of the scheduled message
    content: New content (optional)
    scheduled_timestamp: New timestamp (optional)
    topic: New topic (optional)"""
    
    data = {}
    if content is not None:
        data["content"] = content
    if scheduled_timestamp is not None:
        data["scheduled_timestamp"] = scheduled_timestamp
    if topic is not None:
        data["topic"] = topic
    
    return _make_request("PATCH", f"scheduled_messages/{scheduled_message_id}", json=data)


@app.tool(title="delete_scheduled_message")
async def delete_scheduled_message(
    ctx: Context,
    scheduled_message_id: int,
) -> Dict[str, Any]:
    """Delete a scheduled Zulip message.
    
    scheduled_message_id: ID of the scheduled message"""
    
    return _make_request("DELETE", f"scheduled_messages/{scheduled_message_id}")


@app.tool(title="get_reminders")
async def get_reminders(
    ctx: Context,
) -> Dict[str, Any]:
    """Get all message reminders."""
    
    return _make_request("GET", "reminders")


@app.tool(title="create_reminder")
async def create_reminder(
    ctx: Context,
    content: str,
    timestamp: int,
) -> Dict[str, Any]:
    """Create a message reminder.
    
    content: Reminder message content
    timestamp: UNIX timestamp for the reminder"""
    
    return _make_request("POST", "reminders", json={
        "content": content,
        "timestamp": timestamp,
    })


@app.tool(title="delete_reminder")
async def delete_reminder(
    ctx: Context,
    reminder_id: int,
) -> Dict[str, Any]:
    """Delete a message reminder.
    
    reminder_id: ID of the reminder"""
    
    return _make_request("DELETE", f"reminders/{reminder_id}")


# ===== Drafts & Saved Snippets =====

@app.tool(title="get_drafts")
async def get_drafts(
    ctx: Context,
) -> Dict[str, Any]:
    """Get all drafts."""
    
    return _make_request("GET", "drafts")


@app.tool(title="create_drafts")
async def create_drafts(
    ctx: Context,
    drafts: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Create drafts.
    
    drafts: List of draft objects"""
    
    return _make_request("POST", "drafts", json={"drafts": drafts})


@app.tool(title="update_draft")
async def update_draft(
    ctx: Context,
    draft_id: int,
    saved_snippet_id: Optional[int] = None,
) -> Dict[str, Any]:
    """Update a draft.
    
    draft_id: ID of the draft
    saved_snippet_id: ID of saved snippet to link (optional)"""
    
    data = {}
    if saved_snippet_id is not None:
        data["saved_snippet_id"] = saved_snippet_id
    
    return _make_request("PATCH", f"drafts/{draft_id}", json=data)


@app.tool(title="delete_draft")
async def delete_draft(
    ctx: Context,
    draft_id: int,
) -> Dict[str, Any]:
    """Delete a draft.
    
    draft_id: ID of the draft"""
    
    return _make_request("DELETE", f"drafts/{draft_id}")


@app.tool(title="get_saved_snippets")
async def get_saved_snippets(
    ctx: Context,
) -> Dict[str, Any]:
    """Get all saved snippets."""
    
    return _make_request("GET", "saved_snippets")


@app.tool(title="create_saved_snippet")
async def create_saved_snippet(
    ctx: Context,
    name: str,
    content: str,
) -> Dict[str, Any]:
    """Create a saved snippet.
    
    name: Snippet name
    content: Snippet content"""
    
    return _make_request("POST", "saved_snippets", json={
        "name": name,
        "content": content,
    })


@app.tool(title="update_saved_snippet")
async def update_saved_snippet(
    ctx: Context,
    snippet_id: int,
    name: Optional[str] = None,
    content: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a saved snippet.
    
    snippet_id: ID of the snippet
    name: New name (optional)
    content: New content (optional)"""
    
    data = {}
    if name is not None:
        data["name"] = name
    if content is not None:
        data["content"] = content
    
    return _make_request("PATCH", f"saved_snippets/{snippet_id}", json=data)


@app.tool(title="delete_saved_snippet")
async def delete_saved_snippet(
    ctx: Context,
    snippet_id: int,
) -> Dict[str, Any]:
    """Delete a saved snippet.
    
    snippet_id: ID of the snippet"""
    
    return _make_request("DELETE", f"saved_snippets/{snippet_id}")


# ===== Files & Attachments =====

@app.tool(title="upload_file")
async def upload_file(
    ctx: Context,
    filename: str,
    path: str,
) -> Dict[str, Any]:
    """Upload a file to Zulip.
    
    filename: Name of the file
    path: Path to the file on disk"""
    
    files = {"file": (filename, open(path, "rb"))}
    result = _make_request("POST", "user_uploads", files=files)
    
    # Close the file
    if "file" in files:
        files["file"][1].close()
    
    return result


@app.tool(title="get_file_temporary_url")
async def get_file_temporary_url(
    ctx: Context,
    path_id: str,
) -> Dict[str, Any]:
    """Get a temporary URL for an uploaded file.
    
    path_id: Path ID from the upload response"""
    
    return _make_request("GET", f"user_uploads/{path_id}", params={"temporary": "true"})


@app.tool(title="delete_attachment")
async def delete_attachment(
    ctx: Context,
    file_name: str,
) -> Dict[str, Any]:
    """Delete an attachment.
    
    file_name: Name of the file to delete"""
    
    return _make_request("DELETE", f"attachments/{file_name}")


@app.tool(title="get_attachments")
async def get_attachments(
    ctx: Context,
) -> Dict[str, Any]:
    """Get all attachments."""
    
    return _make_request("GET", "attachments")


@app.tool(title="upload_custom_emoji")
async def upload_custom_emoji(
    ctx: Context,
    emoji_name: str,
    path: str,
) -> Dict[str, Any]:
    """Upload a custom emoji.
    
    emoji_name: Name for the emoji
    path: Path to the emoji image file"""
    
    files = {"file": (emoji_name, open(path, "rb"))}
    result = _make_request("POST", "realm/emoji", files=files)
    
    # Close the file
    if "file" in files:
        files["file"][1].close()
    
    return result


@app.tool(title="get_custom_emoji")
async def get_custom_emoji(
    ctx: Context,
) -> Dict[str, Any]:
    """Get all custom emoji."""
    
    return _make_request("GET", "realm/emoji")


@app.tool(title="deactivate_custom_emoji")
async def deactivate_custom_emoji(
    ctx: Context,
    emoji_name: str,
) -> Dict[str, Any]:
    """Deactivate a custom emoji.
    
    emoji_name: Name of the emoji to deactivate"""
    
    return _make_request("DELETE", f"realm/emoji/{emoji_name}")


# ===== Channels/Streams =====

@app.tool(title="get_streams")
async def get_streams(
    ctx: Context,
    include_public: Optional[bool] = None,
    include_web_public: Optional[bool] = None,
    include_subscribed: Optional[bool] = None,
    exclude_archived: Optional[bool] = None,
) -> Dict[str, Any]:
    """Get all accessible channels.
    
    include_public: Include public channels
    include_web_public: Include web-public channels
    include_subscribed: Include subscribed channels
    exclude_archived: Exclude archived channels"""
    
    params = {}
    if include_public is not None:
        params["include_public"] = str(include_public).lower()
    if include_web_public is not None:
        params["include_web_public"] = str(include_web_public).lower()
    if include_subscribed is not None:
        params["include_subscribed"] = str(include_subscribed).lower()
    if exclude_archived is not None:
        params["exclude_archived"] = str(exclude_archived).lower()
    
    return _make_request("GET", "streams", params=params)


@app.tool(title="create_stream")
async def create_stream(
    ctx: Context,
    name: str,
    description: str,
    invite_only: bool = False,
    is_web_public: bool = False,
) -> Dict[str, Any]:
    """Create a new channel.
    
    name: Channel name
    description: Channel description
    invite_only: Whether to create private channel
    is_web_public: Whether to make channel web-public"""
    
    return _make_request("POST", "streams", json={
        "name": name,
        "description": description,
        "invite_only": invite_only,
        "is_web_public": is_web_public,
    })


@app.tool(title="subscribe")
async def subscribe(
    ctx: Context,
    streams: List[str],
    principals: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Subscribe users to channels.
    
    streams: List of channel names or IDs
    principals: List of user IDs (default: current user)"""
    
    data = {"streams": streams}
    
    if principals is not None:
        data["principals"] = principals
    
    return _make_request("POST", "users/me/subscriptions", json=data)


@app.tool(title="unsubscribe")
async def unsubscribe(
    ctx: Context,
    streams: List[str],
    principals: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Unsubscribe users from channels.
    
    streams: List of channel names or IDs
    principals: List of user IDs (default: current user)"""
    
    data = {"subscriptions": streams}
    
    if principals is not None:
        data["principals"] = principals
    
    return _make_request("DELETE", "users/me/subscriptions", json=data)


@app.tool(title="get_subscriptions")
async def get_subscriptions(
    ctx: Context,
) -> Dict[str, Any]:
    """Get user's subscriptions."""
    
    return _make_request("GET", "users/me/subscriptions")


@app.tool(title="get_stream_by_id")
async def get_stream_by_id(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Get details of a specific stream.
    
    stream_id: ID of the stream"""
    
    return _make_request("GET", f"streams/{stream_id}")


@app.tool(title="get_stream_topics")
async def get_stream_topics(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Get topics in a stream.
    
    stream_id: ID of the stream"""
    
    return _make_request("GET", f"streams/{stream_id}/topics")


@app.tool(title="update_subscription_settings")
async def update_subscription_settings(
    ctx: Context,
    stream_id: int,
    notification_settings_levels: Optional[Dict[str, int]] = None,
) -> Dict[str, Any]:
    """Update subscription settings for a stream.
    
    stream_id: ID of the stream
    notification_settings_levels: Notification settings"""
    
    data = {}
    if notification_settings_levels is not None:
        data["notification_settings_levels"] = notification_settings_levels
    
    return _make_request("PATCH", f"streams/{stream_id}/subscription", json=data)


@app.tool(title="get_subscribers")
async def get_subscribers(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Get subscribers of a stream.
    
    stream_id: ID of the stream"""
    
    return _make_request("GET", f"streams/{stream_id}/members")


@app.tool(title="get_subscription_status")
async def get_subscription_status(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Check if user is subscribed to a stream.
    
    stream_id: ID of the stream"""
    
    return _make_request("GET", f"users/me/subscriptions/{stream_id}")


@app.tool(title="add_default_stream")
async def add_default_stream(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Add a channel as default for new users.
    
    stream_id: ID of the channel"""
    
    return _make_request("POST", "default_channels", json={
        "stream_id": stream_id,
    })


@app.tool(title="remove_default_stream")
async def remove_default_stream(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Remove a channel from default channels.
    
    stream_id: ID of the channel"""
    
    return _make_request("DELETE", f"default_channels/{stream_id}")


@app.tool(title="update_stream")
async def update_stream(
    ctx: Context,
    stream_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    is_announcement_only: Optional[bool] = None,
    is_private: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a stream's properties.
    
    stream_id: ID of the stream
    name: New name (optional)
    description: New description (optional)
    is_announcement_only: Announcement setting (optional)
    is_private: Privacy setting (optional)
    is_web_public: Web-public setting (optional)"""
    
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if is_announcement_only is not None:
        data["is_announcement_only"] = is_announcement_only
    if is_private is not None:
        data["is_private"] = is_private
    if is_web_public is not None:
        data["is_web_public"] = is_web_public
    
    return _make_request("PATCH", f"streams/{stream_id}", json=data)


@app.tool(title="archive_stream")
async def archive_stream(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Archive a stream.
    
    stream_id: ID of the stream"""
    
    return _make_request("POST", f"streams/{stream_id}/archive")


@app.tool(title="delete_topic")
async def delete_topic(
    ctx: Context,
    stream_id: int,
    topic_name: str,
) -> Dict[str, Any]:
    """Delete all messages in a topic.
    
    stream_id: ID of the stream
    topic_name: Name of the topic"""
    
    return _make_request("DELETE", f"streams/{stream_id}/delete_topic", json={
        "topic_name": topic_name,
    })


@app.tool(title="mute_topic")
async def mute_topic(
    ctx: Context,
    stream_id: int,
    topic_name: str,
) -> Dict[str, Any]:
    """Mute a topic.
    
    stream_id: ID of the stream
    topic_name: Name of the topic"""
    
    return _make_request("POST", f"users/me/muted_topics/{stream_id}/{topic_name}")


@app.tool(title="update_user_topic")
async def update_user_topic(
    ctx: Context,
    stream_id: int,
    topic_name: str,
    muted: bool,
) -> Dict[str, Any]:
    """Update topic mute status.
    
    stream_id: ID of the stream
    topic_name: Name of the topic
    muted: Whether to mute the topic"""
    
    return _make_request("PATCH", f"users/me/muted_topics/{stream_id}/{topic_name}", json={
        "op": "add" if muted else "remove",
    })


@app.tool(title="get_stream_email_address")
async def get_stream_email_address(
    ctx: Context,
    stream_id: int,
) -> Dict[str, Any]:
    """Get a stream's email address.
    
    stream_id: ID of the stream"""
    
    return _make_request("GET", f"streams/{stream_id}/email_address")


# ===== Users =====

@app.tool(title="get_user")
async def get_user(
    ctx: Context,
    user_id: int,
) -> Dict[str, Any]:
    """Get a user's profile.
    
    user_id: ID of the user"""
    
    return _make_request("GET", f"users/{user_id}")


@app.tool(title="get_user_by_email")
async def get_user_by_email(
    ctx: Context,
    email: str,
) -> Dict[str, Any]:
    """Get a user's profile by email.
    
    email: User's email address"""
    
    return _make_request("GET", f"users/{email}")


@app.tool(title="get_own_user")
async def get_own_user(
    ctx: Context,
) -> Dict[str, Any]:
    """Get current user's profile."""
    
    return _make_request("GET", "users/me")


@app.tool(title="get_users")
async def get_users(
    ctx: Context,
    client_gravatar: Optional[bool] = None,
    include_custom_profile_fields: Optional[bool] = None,
) -> Dict[str, Any]:
    """Get multiple users.
    
    client_gravatar: Whether to calculate gravatars on client
    include_custom_profile_fields: Whether to include custom profile fields"""
    
    params = {}
    if client_gravatar is not None:
        params["client_gravatar"] = str(client_gravatar).lower()
    if include_custom_profile_fields is not None:
        params["include_custom_profile_fields"] = str(include_custom_profile_fields).lower()
    
    return _make_request("GET", "users", params=params)


@app.tool(title="create_user")
async def create_user(
    ctx: Context,
    email: str,
    password: str,
    full_name: str,
    short_name: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a new user.
    
    email: User's email
    password: User's password
    full_name: Full name
    short_name: Optional short name"""
    
    data = {
        "email": email,
        "password": password,
        "full_name": full_name,
    }
    
    if short_name is not None:
        data["short_name"] = short_name
    
    return _make_request("POST", "users", json=data)


@app.tool(title="update_user")
async def update_user(
    ctx: Context,
    user_id: int,
    full_name: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a user's properties.
    
    user_id: ID of the user
    full_name: New full name (optional)
    is_active: Active status (optional)"""
    
    data = {}
    if full_name is not None:
        data["full_name"] = full_name
    if is_active is not None:
        data["is_active"] = is_active
    
    return _make_request("PATCH", f"users/{user_id}", json=data)


@app.tool(title="update_user_by_email")
async def update_user_by_email(
    ctx: Context,
    email: str,
    full_name: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a user's properties by email.
    
    email: User's email
    full_name: New full name (optional)
    is_active: Active status (optional)"""
    
    data = {}
    if full_name is not None:
        data["full_name"] = full_name
    if is_active is not None:
        data["is_active"] = is_active
    
    return _make_request("PATCH", f"users/{email}", json=data)


@app.tool(title="deactivate_user")
async def deactivate_user(
    ctx: Context,
    user_id: int,
) -> Dict[str, Any]:
    """Deactivate a user.
    
    user_id: ID of the user"""
    
    return _make_request("POST", f"users/{user_id}/deactivate")


@app.tool(title="deactivate_own_user")
async def deactivate_own_user(
    ctx: Context,
) -> Dict[str, Any]:
    """Deactivate the current user."""
    
    return _make_request("POST", "users/me/deactivate")


@app.tool(title="reactivate_user")
async def reactivate_user(
    ctx: Context,
    user_id: int,
) -> Dict[str, Any]:
    """Reactivate a user.
    
    user_id: ID of the user"""
    
    return _make_request("POST", f"users/{user_id}/reactivate")


@app.tool(title="get_user_status")
async def get_user_status(
    ctx: Context,
    user_id: int,
) -> Dict[str, Any]:
    """Get a user's status.
    
    user_id: ID of the user"""
    
    return _make_request("GET", f"users/{user_id}/status")


@app.tool(title="update_status")
async def update_status(
    ctx: Context,
    status_text: str,
) -> Dict[str, Any]:
    """Update your status.
    
    status_text: Status message text"""
    
    return _make_request("PATCH", "users/me/status", json={
        "status_text": status_text,
    })


@app.tool(title="update_status_for_user")
async def update_status_for_user(
    ctx: Context,
    user_id: int,
    status_text: str,
) -> Dict[str, Any]:
    """Update another user's status.
    
    user_id: ID of the user
    status_text: Status message text"""
    
    return _make_request("POST", f"users/{user_id}/status", json={
        "status_text": status_text,
    })


@app.tool(title="get_presence")
async def get_presence(
    ctx: Context,
) -> Dict[str, Any]:
    """Get presence of all users."""
    
    return _make_request("GET", "users/me/presence")


@app.tool(title="get_user_presence")
async def get_user_presence(
    ctx: Context,
    email: str,
) -> Dict[str, Any]:
    """Get a user's presence.
    
    email: User's email address"""
    
    return _make_request("GET", f"users/{email}/presence")


@app.tool(title="update_presence")
async def update_presence(
    ctx: Context,
    status: str,
    ping_only: bool = False,
    new_user_input: bool = True,
) -> Dict[str, Any]:
    """Update presence status.
    
    status: Presence status ('active' or 'inactive')
    ping_only: Whether to just ping
    new_user_input: Whether user input occurred"""
    
    return _make_request("POST", "users/me/presence", json={
        "status": status,
        "ping_only": ping_only,
        "new_user_input": new_user_input,
    })


@app.tool(title="mute_user")
async def mute_user(
    ctx: Context,
    user_id: int,
    muted: bool,
) -> Dict[str, Any]:
    """Mute or unmute a user.
    
    user_id: ID of the user
    muted: Whether to mute the user"""
    
    return _make_request("POST", f"users/{user_id}/mute", json={
        "muted": muted,
    })


@app.tool(title="unmute_user")
async def unmute_user(
    ctx: Context,
    user_id: int,
) -> Dict[str, Any]:
    """Unmute a user.
    
    user_id: ID of the user"""
    
    return _make_request("DELETE", f"users/{user_id}/mute")


@app.tool(title="get_read_receipts")
async def get_read_receipts(
    ctx: Context,
    message_id: int,
) -> Dict[str, Any]:
    """Get read receipts for a message.
    
    message_id: ID of the message"""
    
    return _make_request("GET", f"messages/{message_id}/read_receipts")


@app.tool(title="set_typing_status")
async def set_typing_status(
    ctx: Context,
    to: List[int],
    op: str,
) -> Dict[str, Any]:
    """Set typing status for direct messages.
    
    to: List of user IDs
    op: Operation ('start' or 'stop')"""
    
    return _make_request("POST", "typing", json={
        "to": to,
        "op": op,
    })


@app.tool(title="set_typing_status_for_message_edit")
async def set_typing_status_for_message_edit(
    ctx: Context,
    to: List[int],
    op: str,
) -> Dict[str, Any]:
    """Set typing status for message editing.
    
    to: List of user IDs
    op: Operation ('start' or 'stop')"""
    
    return _make_request("POST", "typing", json={
        "to": to,
        "op": op,
        "message_content": "Editing...",
    })


# ===== User Groups =====

@app.tool(title="get_user_groups")
async def get_user_groups(
    ctx: Context,
) -> Dict[str, Any]:
    """Get all user groups."""
    
    return _make_request("GET", "user_groups")


@app.tool(title="get_user_group_members")
async def get_user_group_members(
    ctx: Context,
    user_group_id: int,
) -> Dict[str, Any]:
    """Get members of a user group.
    
    user_group_id: ID of the user group"""
    
    return _make_request("GET", f"user_groups/{user_group_id}/members")


@app.tool(title="get_user_group_subgroups")
async def get_user_group_subgroups(
    ctx: Context,
    user_group_id: int,
) -> Dict[str, Any]:
    """Get subgroups of a user group.
    
    user_group_id: ID of the user group"""
    
    return _make_request("GET", f"user_groups/{user_group_id}/subgroups")


@app.tool(title="get_is_user_group_member")
async def get_is_user_group_member(
    ctx: Context,
    user_id: int,
    user_group_id: int,
) -> Dict[str, Any]:
    """Check if user is member of a group.
    
    user_id: User ID
    user_group_id: Group ID"""
    
    return _make_request("GET", f"users/{user_id}/groups/{user_group_id}")


@app.tool(title="create_user_group")
async def create_user_group(
    ctx: Context,
    name: str,
    members: List[int],
    description: str,
) -> Dict[str, Any]:
    """Create a user group.
    
    name: Group name
    members: List of member user IDs
    description: Group description"""
    
    return _make_request("POST", "user_groups", json={
        "name": name,
        "members": members,
        "description": description,
    })


@app.tool(title="update_user_group")
async def update_user_group(
    ctx: Context,
    user_group_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a user group.
    
    user_group_id: ID of the group
    name: New name (optional)
    description: New description (optional)"""
    
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    
    return _make_request("PATCH", f"user_groups/{user_group_id}", json=data)


@app.tool(title="deactivate_user_group")
async def deactivate_user_group(
    ctx: Context,
    user_group_id: int,
) -> Dict[str, Any]:
    """Deactivate a user group.
    
    user_group_id: ID of the group"""
    
    return _make_request("POST", f"user_groups/{user_group_id}/deactivate")


@app.tool(title="update_user_group_members")
async def update_user_group_members(
    ctx: Context,
    user_group_id: int,
    delete: Optional[List[int]] = None,
    add: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Update user group members.
    
    user_group_id: ID of the group
    delete: Users to remove (optional)
    add: Users to add (optional)"""
    
    data = {}
    if delete is not None:
        data["delete"] = delete
    if add is not None:
        data["add"] = add
    
    return _make_request("PATCH", f"user_groups/{user_group_id}/members", json=data)


@app.tool(title="update_user_group_subgroups")
async def update_user_group_subgroups(
    ctx: Context,
    user_group_id: int,
    delete: Optional[List[int]] = None,
    add: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Update user group subgroups.
    
    user_group_id: ID of the group
    delete: Subgroups to remove (optional)
    add: Subgroups to add (optional)"""
    
    data = {}
    if delete is not None:
        data["delete"] = delete
    if add is not None:
        data["add"] = add
    
    return _make_request("PATCH", f"user_groups/{user_group_id}/subgroups", json=data)


# ===== Server Settings & Admin =====

@app.tool(title="get_server_settings")
async def get_server_settings(
    ctx: Context,
) -> Dict[str, Any]:
    """Get server settings."""
    
    return _make_request("GET", "server_settings")


@app.tool(title="get_linkifiers")
async def get_linkifiers(
    ctx: Context,
) -> Dict[str, Any]:
    """Get all linkifiers."""
    
    return _make_request("GET", "linkifiers")


@app.tool(title="add_linkifier")
async def add_linkifier(
    ctx: Context,
    pattern: str,
    url_template: str,
) -> Dict[str, Any]:
    """Add a linkifier.
    
    pattern: Regex pattern
    url_template: URL template"""
    
    return _make_request("POST", "realm/linkifiers", json={
        "pattern": pattern,
        "url_template": url_template,
    })


@app.tool(title="update_linkifier")
async def update_linkifier(
    ctx: Context,
    linkifier_id: int,
    pattern: Optional[str] = None,
    url_template: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a linkifier.
    
    linkifier_id: ID of the linkifier
    pattern: New pattern (optional)
    url_template: New URL template (optional)"""
    
    data = {}
    if pattern is not None:
        data["pattern"] = pattern
    if url_template is not None:
        data["url_template"] = url_template
    
    return _make_request("PATCH", f"realm/linkifiers/{linkifier_id}", json=data)


@app.tool(title="remove_linkifier")
async def remove_linkifier(
    ctx: Context,
    linkifier_id: int,
) -> Dict[str, Any]:
    """Remove a linkifier.
    
    linkifier_id: ID of the linkifier"""
    
    return _make_request("DELETE", f"realm/linkifiers/{linkifier_id}")


@app.tool(title="reorder_linkifiers")
async def reorder_linkifiers(
    ctx: Context,
    linkifier_ids: List[int],
) -> Dict[str, Any]:
    """Reorder linkifiers.
    
    linkifier_ids: Ordered list of linkifier IDs"""
    
    return _make_request("POST", "realm/linkifiers/reorder", json={
        "order": linkifier_ids,
    })


@app.tool(title="get_alert_words")
async def get_alert_words(
    ctx: Context,
) -> Dict[str, Any]:
    """Get alert words."""
    
    return _make_request("GET", "realm/alert_words")


@app.tool(title="add_alert_words")
async def add_alert_words(
    ctx: Context,
    alert_words: List[str],
) -> Dict[str, Any]:
    """Add alert words.
    
    alert_words: List of alert words"""
    
    return _make_request("POST", "realm/alert_words", json={
        "alert_words": alert_words,
    })


@app.tool(title="remove_alert_words")
async def remove_alert_words(
    ctx: Context,
    alert_words: List[str],
) -> Dict[str, Any]:
    """Remove alert words.
    
    alert_words: List of alert words"""
    
    return _make_request("DELETE", "realm/alert_words", json={
        "alert_words": alert_words,
    })


@app.tool(title="get_custom_profile_fields")
async def get_custom_profile_fields(
    ctx: Context,
) -> Dict[str, Any]:
    """Get custom profile fields."""
    
    return _make_request("GET", "realm/profile_fields")


@app.tool(title="create_custom_profile_field")
async def create_custom_profile_field(
    ctx: Context,
    name: str,
    field_type: int,
    hint: str,
    display_in_profile_summary: bool = False,
) -> Dict[str, Any]:
    """Create a custom profile field.
    
    name: Field name
    field_type: Field type
    hint: Hint text
    display_in_profile_summary: Whether to display in summary"""
    
    return _make_request("POST", "realm/profile_fields", json={
        "name": name,
        "field_type": field_type,
        "hint": hint,
        "display_in_profile_summary": display_in_profile_summary,
    })


@app.tool(title="update_custom_profile_field")
async def update_custom_profile_field(
    ctx: Context,
    field_id: int,
    name: Optional[str] = None,
    hint: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a custom profile field.
    
    field_id: ID of the field
    name: New name (optional)
    hint: New hint (optional)"""
    
    data = {}
    if name is not None:
        data["name"] = name
    if hint is not None:
        data["hint"] = hint
    
    return _make_request("PATCH", f"realm/profile_fields/{field_id}", json=data)


@app.tool(title="reorder_custom_profile_fields")
async def reorder_custom_profile_fields(
    ctx: Context,
    order: List[int],
) -> Dict[str, Any]:
    """Reorder custom profile fields.
    
    order: Ordered list of field IDs"""
    
    return _make_request("POST", "realm/profile_fields/reorder", json={
        "order": order,
    })


@app.tool(title="get_custom_profile_field")
async def get_custom_profile_field(
    ctx: Context,
    user_id: int,
    field_id: int,
) -> Dict[str, Any]:
    """Get custom profile field value for user.
    
    user_id: User ID
    field_id: Field ID"""
    
    return _make_request("GET", f"users/{user_id}/profile/{field_id}")


@app.tool(title="update_custom_profile_field")
async def update_custom_profile_field(
    ctx: Context,
    user_id: int,
    field_id: int,
    value: str,
) -> Dict[str, Any]:
    """Update custom profile field value for user.
    
    user_id: User ID
    field_id: Field ID
    value: New value"""
    
    return _make_request("PATCH", f"users/{user_id}/profile/{field_id}", json={
        "value": value,
    })


@app.tool(title="get_navigation_views")
async def get_navigation_views(
    ctx: Context,
) -> Dict[str, Any]:
    """Get navigation views."""
    
    return _make_request("GET", "navigation_views")


@app.tool(title="add_navigation_view")
async def add_navigation_view(
    ctx: Context,
    name: str,
    uri: str,
) -> Dict[str, Any]:
    """Add a navigation view.
    
    name: View name
    uri: URI"""
    
    return _make_request("POST", "navigation_views", json={
        "name": name,
        "uri": uri,
    })


@app.tool(title="update_navigation_view")
async def update_navigation_view(
    ctx: Context,
    navigation_view_id: int,
    name: Optional[str] = None,
    uri: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a navigation view.
    
    navigation_view_id: ID of the view
    name: New name (optional)
    uri: New URI (optional)"""
    
    data = {}
    if name is not None:
        data["name"] = name
    if uri is not None:
        data["uri"] = uri
    
    return _make_request("PATCH", f"navigation_views/{navigation_view_id}", json=data)


@app.tool(title="remove_navigation_view")
async def remove_navigation_view(
    ctx: Context,
    navigation_view_id: int,
) -> Dict[str, Any]:
    """Remove a navigation view.
    
    navigation_view_id: ID of the view"""
    
    return _make_request("DELETE", f"navigation_views/{navigation_view_id}")


@app.tool(title="get_channel_folders")
async def get_channel_folders(
    ctx: Context,
) -> Dict[str, Any]:
    """Get channel folders."""
    
    return _make_request("GET", "user_settings/channel_folders")


@app.tool(title="create_channel_folder")
async def create_channel_folder(
    ctx: Context,
    name: str,
    stream_ids: List[int],
) -> Dict[str, Any]:
    """Create a channel folder.
    
    name: Folder name
    stream_ids: List of stream IDs"""
    
    return _make_request("POST", "user_settings/channel_folders", json={
        "name": name,
        "stream_ids": stream_ids,
    })


@app.tool(title="update_channel_folder")
async def update_channel_folder(
    ctx: Context,
    folder_id: int,
    name: Optional[str] = None,
    stream_ids: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Update a channel folder.
    
    folder_id: ID of the folder
    name: New name (optional)
    stream_ids: New stream IDs (optional)"""
    
    data = {}
    if name is not None:
        data["name"] = name
    if stream_ids is not None:
        data["stream_ids"] = stream_ids
    
    return _make_request("PATCH", f"user_settings/channel_folders/{folder_id}", json=data)


@app.tool(title="patch_channel_folders")
async def patch_channel_folders(
    ctx: Context,
    folders: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Reorder channel folders.
    
    folders: Ordered list of folder objects"""
    
    return _make_request("PATCH", "user_settings/channel_folders", json={
        "folders": folders,
    })


@app.tool(title="get_realm_exports")
async def get_realm_exports(
    ctx: Context,
) -> Dict[str, Any]:
    """Get data exports."""
    
    return _make_request("GET", "exports")


@app.tool(title="create_realm_export")
async def create_realm_export(
    ctx: Context,
    export_type: str,
) -> Dict[str, Any]:
    """Request a data export.
    
    export_type: Type of export (e.g., 'public_data')"""
    
    return _make_request("POST", "exports", json={
        "export_type": export_type,
    })


@app.tool(title="get_realm_export_consents")
async def get_realm_export_consents(
    ctx: Context,
) -> Dict[str, Any]:
    """Get data export consent states."""
    
    return _make_request("GET", "exports/consents")


@app.tool(title="get_events")
async def get_events(
    ctx: Context,
    last_event_id: int = 0,
    queue_id: str,
) -> Dict[str, Any]:
    """Get events from event queue.
    
    last_event_id: Last event ID processed
    queue_id: Event queue ID"""
    
    return _make_request("GET", "events", params={
        "queue_id": queue_id,
        "last_event_id": last_event_id,
    })


@app.tool(title="register_queue")
async def register_queue(
    ctx: Context,
    event_types: Optional[List[str]] = None,
    apply_markdown: bool = True,
    client_gravatar: bool = True,
) -> Dict[str, Any]:
    """Register an event queue.
    
    event_types: Types of events to receive (optional)
    apply_markdown: Whether to apply Markdown
    client_gravatar: Whether to use client gravatar"""
    
    data = {
        "apply_markdown": apply_markdown,
        "client_gravatar": client_gravatar,
    }
    
    if event_types is not None:
        data["event_types"] = event_types
    
    return _make_request("POST", "register", json=data)


@app.tool(title="unregister_queue")
async def unregister_queue(
    ctx: Context,
    queue_id: str,
) -> Dict[str, Any]:
    """Delete an event queue.
    
    queue_id: Event queue ID"""
    
    return _make_request("DELETE", "events", params={
        "queue_id": queue_id,
    })


@app.tool(title="test_notify")
async def test_notify(
    ctx: Context,
    type: str,
    user_id: int,
    content: str,
) -> Dict[str, Any]:
    """Send a test notification.
    
    type: Notification type ('stream' or 'private')
    user_id: User ID
    content: Notification content"""
    
    return _make_request("POST", "notify_test", json={
        "type": type,
        "user_id": user_id,
        "content": content,
    })


@app.tool(title="test_welcome_bot_custom_message")
async def test_welcome_bot_custom_message(
    ctx: Context,
    content: str,
) -> Dict[str, Any]:
    """Test custom welcome bot message.
    
    content: Custom message content"""
    
    return _make_request("POST", "bots/welcome", json={
        "content": content,
    })


@app.tool(title="add_apns_token")
async def add_apns_token(
    ctx: Context,
    apns_token: str,
    apns_dev: bool,
) -> Dict[str, Any]:
    """Add APNs device token.
    
    apns_token: APNs token
    apns_dev: Whether development environment"""
    
    return _make_request("POST", "users/me/apns_device_token", json={
        "token": apns_token,
        "app_id": "com.zulip.Zulip" if not apns_dev else "com.zulip.Zulip-Dev",
    })


@app.tool(title="remove_apns_token")
async def remove_apns_token(
    ctx: Context,
    apns_token: str,
) -> Dict[str, Any]:
    """Remove APNs device token.
    
    apns_token: APNs token"""
    
    return _make_request("DELETE", "users/me/apns_device_token", json={
        "token": apns_token,
    })


@app.tool(title="add_fcm_token")
async def add_fcm_token(
    ctx: Context,
    fcm_token: str,
) -> Dict[str, Any]:
    """Add FCM registration token.
    
    fcm_token: FCM token"""
    
    return _make_request("POST", "users/me/mobile_devices", json={
        "token": fcm_token,
    })


@app.tool(title="remove_fcm_token")
async def remove_fcm_token(
    ctx: Context,
    fcm_token: str,
) -> Dict[str, Any]:
    """Remove FCM registration token.
    
    fcm_token: FCM token"""
    
    return _make_request("DELETE", "users/me/mobile_devices", json={
        "token": fcm_token,
    })


@app.tool(title="create_video_call")
async def create_video_call(
    ctx: Context,
    integration: str,
) -> Dict[str, Any]:
    """Create a video call.
    
    integration: Video integration ('big_blue_button', 'constructor_groups', 'nextcloud_talk')"""
    
    return _make_request("POST", "calls", json={
        "integration": integration,
    })


@app.tool(title="get_api_keys")
async def get_api_keys(
    ctx: Context,
) -> Dict[str, Any]:
    """Get API keys."""
    
    return _make_request("GET", "api_key")


@app.tool(title="regenerate_api_key")
async def regenerate_api_key(
    ctx: Context,
) -> Dict[str, Any]:
    """Regenerate API key."""
    
    return _make_request("POST", "api_key/regenerate")


@app.tool(title="get_bot_api_key")
async def get_bot_api_key(
    ctx: Context,
    bot_user_id: int,
) -> Dict[str, Any]:
    """Get bot's API key.
    
    bot_user_id: ID of the bot user"""
    
    return _make_request("GET", f"users/{bot_user_id}/api_key")


@app.tool(title="regenerate_bot_api_key")
async def regenerate_bot_api_key(
    ctx: Context,
    bot_user_id: int,
) -> Dict[str, Any]:
    """Regenerate bot's API key.
    
    bot_user_id: ID of the bot user"""
    
    return _make_request("POST", f"users/{bot_user_id}/api_key/regenerate")


@app.tool(title="get_realm_user_settings_defaults")
async def get_realm_user_settings_defaults(
    ctx: Context,
) -> Dict[str, Any]:
    """Get realm-level default user settings."""
    
    return _make_request("GET", "settings/defaults")


@app.tool(title="update_realm_user_settings_defaults")
async def update_realm_user_settings_defaults(
    ctx: Context,
    default_desktop_notifications: Optional[str] = None,
    default_email_notifications: Optional[str] = None,
) -> Dict[str, Any]:
    """Update realm-level default user settings.
    
    default_desktop_notifications: Desktop notification default (optional)
    default_email_notifications: Email notification default (optional)"""
    
    data = {}
    if default_desktop_notifications is not None:
        data["default_desktop_notifications"] = default_desktop_notifications
    if default_email_notifications is not None:
        data["default_email_notifications"] = default_email_notifications
    
    return _make_request("PATCH", "settings/defaults", json=data)


@app.tool(title="get_code_playgrounds")
async def get_code_playgrounds(
    ctx: Context,
) -> Dict[str, Any]:
    """Get code playgrounds."""
    
    return _make_request("GET", "realm/code_playgrounds")


@app.tool(title="add_code_playground")
async def add_code_playground(
    ctx: Context,
    name: str,
    url_pattern: str,
    pygments_language: str,
) -> Dict[str, Any]:
    """Add a code playground.
    
    name: Playground name
    url_pattern: URL pattern template
    pygments_language: Pygments language name"""
    
    return _make_request("POST", "realm/code_playgrounds", json={
        "name": name,
        "url_pattern": url_pattern,
        "pygments_language": pygments_language,
    })


@app.tool(title="remove_code_playground")
async def remove_code_playground(
    ctx: Context,
    playground_id: int,
) -> Dict[str, Any]:
    """Remove a code playground.
    
    playground_id: ID of the playground"""
    
    return _make_request("DELETE", f"realm/code_playgrounds/{playground_id}")


# Register all tools in FastMCP
app.register_tool("send_message")
app.register_tool("edit_message")
app.register_tool("delete_message")
app.register_tool("get_message")
app.register_tool("get_messages")
app.register_tool("add_reaction")
app.register_tool("remove_reaction")
app.register_tool("update_message_flags")
app.register_tool("report_message")
app.register_tool("mark_all_as_read")
app.register_tool("mark_stream_as_read")
app.register_tool("mark_topic_as_read")
app.register_tool("get_message_history")
app.register_tool("render_message")
app.register_tool("check_messages_match_narrow")

app.register_tool("get_scheduled_messages")
app.register_tool("create_scheduled_message")
app.register_tool("update_scheduled_message")
app.register_tool("delete_scheduled_message")
app.register_tool("get_reminders")
app.register_tool("create_reminder")
app.register_tool("delete_reminder")

app.register_tool("get_drafts")
app.register_tool("create_drafts")
app.register_tool("update_draft")
app.register_tool("delete_draft")
app.register_tool("get_saved_snippets")
app.register_tool("create_saved_snippet")
app.register_tool("update_saved_snippet")
app.register_tool("delete_saved_snippet")

app.register_tool("upload_file")
app.register_tool("get_file_temporary_url")
app.register_tool("delete_attachment")
app.register_tool("get_attachments")
app.register_tool("upload_custom_emoji")
app.register_tool("get_custom_emoji")
app.register_tool("deactivate_custom_emoji")

app.register_tool("get_streams")
app.register_tool("create_stream")
app.register_tool("subscribe")
app.register_tool("unsubscribe")
app.register_tool("get_subscriptions")
app.register_tool("get_stream_by_id")
app.register_tool("get_stream_topics")
app.register_tool("update_subscription_settings")
app.register_tool("get_subscribers")
app.register_tool("get_subscription_status")
app.register_tool("add_default_stream")
app.register_tool("remove_default_stream")
app.register_tool("update_stream")
app.register_tool("archive_stream")
app.register_tool("delete_topic")
app.register_tool("mute_topic")
app.register_tool("update_user_topic")
app.register_tool("get_stream_email_address")

app.register_tool("get_user")
app.register_tool("get_user_by_email")
app.register_tool("get_own_user")
app.register_tool("get_users")
app.register_tool("create_user")
app.register_tool("update_user")
app.register_tool("update_user_by_email")
app.register_tool("deactivate_user")
app.register_tool("deactivate_own_user")
app.register_tool("reactivate_user")
app.register_tool("get_user_status")
app.register_tool("update_status")
app.register_tool("update_status_for_user")
app.register_tool("get_presence")
app.register_tool("get_user_presence")
app.register_tool("update_presence")
app.register_tool("mute_user")
app.register_tool("unmute_user")
app.register_tool("get_read_receipts")
app.register_tool("set_typing_status")
app.register_tool("set_typing_status_for_message_edit")

app.register_tool("get_user_groups")
app.register_tool("get_user_group_members")
app.register_tool("get_user_group_subgroups")
app.register_tool("get_is_user_group_member")
app.register_tool("create_user_group")
app.register_tool("update_user_group")
app.register_tool("deactivate_user_group")
app.register_tool("update_user_group_members")
app.register_tool("update_user_group_subgroups")

app.register_tool("get_server_settings")
app.register_tool("get_linkifiers")
app.register_tool("add_linkifier")
app.register_tool("update_linkifier")
app.register_tool("remove_linkifier")
app.register_tool("reorder_linkifiers")
app.register_tool("get_alert_words")
app.register_tool("add_alert_words")
app.register_tool("remove_alert_words")
app.register_tool("get_custom_profile_fields")
app.register_tool("create_custom_profile_field")
app.register_tool("update_custom_profile_field")
app.register_tool("reorder_custom_profile_fields")
app.register_tool("get_custom_profile_field")
app.register_tool("update_custom_profile_field")
app.register_tool("get_navigation_views")
app.register_tool("add_navigation_view")
app.register_tool("update_navigation_view")
app.register_tool("remove_navigation_view")
app.register_tool("get_channel_folders")
app.register_tool("create_channel_folder")
app.register_tool("update_channel_folder")
app.register_tool("patch_channel_folders")
app.register_tool("get_realm_exports")
app.register_tool("create_realm_export")
app.register_tool("get_realm_export_consents")
app.register_tool("get_events")
app.register_tool("register_queue")
app.register_tool("unregister_queue")
app.register_tool("test_notify")
app.register_tool("test_welcome_bot_custom_message")
app.register_tool("add_apns_token")
app.register_tool("remove_apns_token")
app.register_tool("add_fcm_token")
app.register_tool("remove_fcm_token")
app.register_tool("create_video_call")
app.register_tool("get_api_keys")
app.register_tool("regenerate_api_key")
app.register_tool("get_bot_api_key")
app.register_tool("regenerate_bot_api_key")
app.register_tool("get_realm_user_settings_defaults")
app.register_tool("update_realm_user_settings_defaults")
app.register_tool("get_code_playgrounds")
app.register_tool("add_code_playground")
app.register_tool("remove_code_playground")


@app.run_if_main()
async def main():
    app.run(transport="stdio")
