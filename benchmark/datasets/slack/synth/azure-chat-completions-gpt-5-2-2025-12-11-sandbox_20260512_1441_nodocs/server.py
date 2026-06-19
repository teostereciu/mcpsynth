import os
import json
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://slack.com/api"


def _slack_request(method: str, endpoint: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, files: Any = None) -> Dict[str, Any]:
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        return {"error": "Missing SLACK_BOT_TOKEN env var"}

    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        resp = requests.request(method, url, headers=headers, params=params, data=data, files=files, timeout=60)
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}

    try:
        payload = resp.json()
    except ValueError:
        return {"error": f"Non-JSON response (status {resp.status_code})", "text": resp.text}

    # Slack Web API uses ok=false with error string
    if isinstance(payload, dict) and payload.get("ok") is False:
        return payload

    return payload if isinstance(payload, dict) else {"result": payload}


mcp = FastMCP("slack-web-api")


# -------------------- Conversations --------------------

@mcp.tool()
def conversations_list(limit: int = 200, cursor: Optional[str] = None, types: str = "public_channel,private_channel", exclude_archived: bool = True) -> Dict[str, Any]:
    """List conversations (channels, groups, IMs)."""
    params = {
        "limit": limit,
        "types": types,
        "exclude_archived": str(exclude_archived).lower(),
    }
    if cursor:
        params["cursor"] = cursor
    return _slack_request("GET", "conversations.list", params=params)


@mcp.tool()
def conversations_info(channel: str, include_num_members: bool = False) -> Dict[str, Any]:
    """Get information about a conversation."""
    params = {"channel": channel, "include_num_members": str(include_num_members).lower()}
    return _slack_request("GET", "conversations.info", params=params)


@mcp.tool()
def conversations_history(channel: str, limit: int = 100, cursor: Optional[str] = None, oldest: Optional[str] = None, latest: Optional[str] = None, inclusive: bool = False) -> Dict[str, Any]:
    """Fetch conversation message history."""
    params: Dict[str, Any] = {"channel": channel, "limit": limit, "inclusive": str(inclusive).lower()}
    if cursor:
        params["cursor"] = cursor
    if oldest is not None:
        params["oldest"] = oldest
    if latest is not None:
        params["latest"] = latest
    return _slack_request("GET", "conversations.history", params=params)


@mcp.tool()
def conversations_replies(channel: str, ts: str, limit: int = 100, cursor: Optional[str] = None, inclusive: bool = False) -> Dict[str, Any]:
    """Fetch a thread's replies."""
    params: Dict[str, Any] = {"channel": channel, "ts": ts, "limit": limit, "inclusive": str(inclusive).lower()}
    if cursor:
        params["cursor"] = cursor
    return _slack_request("GET", "conversations.replies", params=params)


@mcp.tool()
def conversations_members(channel: str, limit: int = 200, cursor: Optional[str] = None) -> Dict[str, Any]:
    """List members of a conversation."""
    params: Dict[str, Any] = {"channel": channel, "limit": limit}
    if cursor:
        params["cursor"] = cursor
    return _slack_request("GET", "conversations.members", params=params)


@mcp.tool()
def conversations_create(name: str, is_private: bool = False, team_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a conversation."""
    data: Dict[str, Any] = {"name": name, "is_private": json.dumps(is_private)}
    if team_id:
        data["team_id"] = team_id
    return _slack_request("POST", "conversations.create", data=data)


@mcp.tool()
def conversations_invite(channel: str, users: str) -> Dict[str, Any]:
    """Invite users (comma-separated user IDs) to a conversation."""
    data = {"channel": channel, "users": users}
    return _slack_request("POST", "conversations.invite", data=data)


@mcp.tool()
def conversations_join(channel: str) -> Dict[str, Any]:
    """Join a conversation."""
    data = {"channel": channel}
    return _slack_request("POST", "conversations.join", data=data)


@mcp.tool()
def conversations_leave(channel: str) -> Dict[str, Any]:
    """Leave a conversation."""
    data = {"channel": channel}
    return _slack_request("POST", "conversations.leave", data=data)


@mcp.tool()
def conversations_archive(channel: str) -> Dict[str, Any]:
    """Archive a conversation."""
    data = {"channel": channel}
    return _slack_request("POST", "conversations.archive", data=data)


@mcp.tool()
def conversations_unarchive(channel: str) -> Dict[str, Any]:
    """Unarchive a conversation."""
    data = {"channel": channel}
    return _slack_request("POST", "conversations.unarchive", data=data)


@mcp.tool()
def conversations_rename(channel: str, name: str) -> Dict[str, Any]:
    """Rename a conversation."""
    data = {"channel": channel, "name": name}
    return _slack_request("POST", "conversations.rename", data=data)


@mcp.tool()
def conversations_set_topic(channel: str, topic: str) -> Dict[str, Any]:
    """Set conversation topic."""
    data = {"channel": channel, "topic": topic}
    return _slack_request("POST", "conversations.setTopic", data=data)


@mcp.tool()
def conversations_set_purpose(channel: str, purpose: str) -> Dict[str, Any]:
    """Set conversation purpose."""
    data = {"channel": channel, "purpose": purpose}
    return _slack_request("POST", "conversations.setPurpose", data=data)


# -------------------- Chat / Messages --------------------

@mcp.tool()
def chat_post_message(channel: str, text: str, thread_ts: Optional[str] = None, blocks_json: Optional[str] = None, attachments_json: Optional[str] = None, mrkdwn: bool = True, unfurl_links: Optional[bool] = None, unfurl_media: Optional[bool] = None) -> Dict[str, Any]:
    """Post a message to a channel. blocks_json/attachments_json should be JSON strings."""
    data: Dict[str, Any] = {"channel": channel, "text": text, "mrkdwn": json.dumps(mrkdwn)}
    if thread_ts:
        data["thread_ts"] = thread_ts
    if blocks_json:
        data["blocks"] = blocks_json
    if attachments_json:
        data["attachments"] = attachments_json
    if unfurl_links is not None:
        data["unfurl_links"] = json.dumps(unfurl_links)
    if unfurl_media is not None:
        data["unfurl_media"] = json.dumps(unfurl_media)
    return _slack_request("POST", "chat.postMessage", data=data)


@mcp.tool()
def chat_update(channel: str, ts: str, text: Optional[str] = None, blocks_json: Optional[str] = None, attachments_json: Optional[str] = None) -> Dict[str, Any]:
    """Update a message."""
    data: Dict[str, Any] = {"channel": channel, "ts": ts}
    if text is not None:
        data["text"] = text
    if blocks_json is not None:
        data["blocks"] = blocks_json
    if attachments_json is not None:
        data["attachments"] = attachments_json
    return _slack_request("POST", "chat.update", data=data)


@mcp.tool()
def chat_delete(channel: str, ts: str) -> Dict[str, Any]:
    """Delete a message."""
    data = {"channel": channel, "ts": ts}
    return _slack_request("POST", "chat.delete", data=data)


@mcp.tool()
def chat_schedule_message(channel: str, post_at: int, text: str, thread_ts: Optional[str] = None, blocks_json: Optional[str] = None, attachments_json: Optional[str] = None) -> Dict[str, Any]:
    """Schedule a message. post_at is a Unix timestamp (seconds)."""
    data: Dict[str, Any] = {"channel": channel, "post_at": str(post_at), "text": text}
    if thread_ts:
        data["thread_ts"] = thread_ts
    if blocks_json:
        data["blocks"] = blocks_json
    if attachments_json:
        data["attachments"] = attachments_json
    return _slack_request("POST", "chat.scheduleMessage", data=data)


@mcp.tool()
def chat_delete_scheduled_message(channel: str, scheduled_message_id: str) -> Dict[str, Any]:
    """Delete a scheduled message."""
    data = {"channel": channel, "scheduled_message_id": scheduled_message_id}
    return _slack_request("POST", "chat.deleteScheduledMessage", data=data)


@mcp.tool()
def chat_scheduled_messages_list(channel: Optional[str] = None, limit: int = 100, cursor: Optional[str] = None, oldest: Optional[str] = None, latest: Optional[str] = None) -> Dict[str, Any]:
    """List scheduled messages."""
    params: Dict[str, Any] = {"limit": limit}
    if channel:
        params["channel"] = channel
    if cursor:
        params["cursor"] = cursor
    if oldest is not None:
        params["oldest"] = oldest
    if latest is not None:
        params["latest"] = latest
    return _slack_request("GET", "chat.scheduledMessages.list", params=params)


# -------------------- Users --------------------

@mcp.tool()
def users_list(limit: int = 200, cursor: Optional[str] = None) -> Dict[str, Any]:
    """List users in the workspace."""
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return _slack_request("GET", "users.list", params=params)


@mcp.tool()
def users_info(user: str, include_locale: bool = False) -> Dict[str, Any]:
    """Get info for a user."""
    params = {"user": user, "include_locale": str(include_locale).lower()}
    return _slack_request("GET", "users.info", params=params)


@mcp.tool()
def users_lookup_by_email(email: str) -> Dict[str, Any]:
    """Lookup a user by email."""
    params = {"email": email}
    return _slack_request("GET", "users.lookupByEmail", params=params)


@mcp.tool()
def users_get_presence(user: str) -> Dict[str, Any]:
    """Get a user's presence."""
    params = {"user": user}
    return _slack_request("GET", "users.getPresence", params=params)


# -------------------- Reactions --------------------

@mcp.tool()
def reactions_add(name: str, channel: str, timestamp: str) -> Dict[str, Any]:
    """Add a reaction to a message."""
    data = {"name": name, "channel": channel, "timestamp": timestamp}
    return _slack_request("POST", "reactions.add", data=data)


@mcp.tool()
def reactions_remove(name: str, channel: str, timestamp: str) -> Dict[str, Any]:
    """Remove a reaction from a message."""
    data = {"name": name, "channel": channel, "timestamp": timestamp}
    return _slack_request("POST", "reactions.remove", data=data)


@mcp.tool()
def reactions_get(channel: str, timestamp: str, full: bool = True) -> Dict[str, Any]:
    """Get reactions for a message."""
    params = {"channel": channel, "timestamp": timestamp, "full": str(full).lower()}
    return _slack_request("GET", "reactions.get", params=params)


# -------------------- Files --------------------

@mcp.tool()
def files_list(count: int = 100, page: int = 1, types: Optional[str] = None, user: Optional[str] = None, channel: Optional[str] = None) -> Dict[str, Any]:
    """List files."""
    params: Dict[str, Any] = {"count": count, "page": page}
    if types:
        params["types"] = types
    if user:
        params["user"] = user
    if channel:
        params["channel"] = channel
    return _slack_request("GET", "files.list", params=params)


@mcp.tool()
def files_info(file: str, count: int = 100, page: int = 1) -> Dict[str, Any]:
    """Get file info."""
    params = {"file": file, "count": count, "page": page}
    return _slack_request("GET", "files.info", params=params)


@mcp.tool()
def files_delete(file: str) -> Dict[str, Any]:
    """Delete a file."""
    data = {"file": file}
    return _slack_request("POST", "files.delete", data=data)


@mcp.tool()
def files_upload(channels: Optional[str] = None, content: Optional[str] = None, filename: Optional[str] = None, filetype: Optional[str] = None, initial_comment: Optional[str] = None, title: Optional[str] = None, file_path: Optional[str] = None) -> Dict[str, Any]:
    """Upload a file. Provide either content (text) or file_path (local path). channels is comma-separated channel IDs."""
    data: Dict[str, Any] = {}
    if channels:
        data["channels"] = channels
    if filename:
        data["filename"] = filename
    if filetype:
        data["filetype"] = filetype
    if initial_comment:
        data["initial_comment"] = initial_comment
    if title:
        data["title"] = title

    files = None
    if file_path:
        try:
            files = {"file": open(file_path, "rb")}
        except OSError as e:
            return {"error": f"Unable to open file_path: {e}"}
    else:
        if content is not None:
            data["content"] = content
        else:
            return {"error": "Provide either content or file_path"}

    try:
        return _slack_request("POST", "files.upload", data=data, files=files)
    finally:
        if files and "file" in files:
            try:
                files["file"].close()
            except Exception:
                pass


# -------------------- Search --------------------

@mcp.tool()
def search_messages(query: str, count: int = 20, page: int = 1, sort: Optional[str] = None, sort_dir: Optional[str] = None) -> Dict[str, Any]:
    """Search messages."""
    params: Dict[str, Any] = {"query": query, "count": count, "page": page}
    if sort:
        params["sort"] = sort
    if sort_dir:
        params["sort_dir"] = sort_dir
    return _slack_request("GET", "search.messages", params=params)


@mcp.tool()
def search_files(query: str, count: int = 20, page: int = 1, sort: Optional[str] = None, sort_dir: Optional[str] = None) -> Dict[str, Any]:
    """Search files."""
    params: Dict[str, Any] = {"query": query, "count": count, "page": page}
    if sort:
        params["sort"] = sort
    if sort_dir:
        params["sort_dir"] = sort_dir
    return _slack_request("GET", "search.files", params=params)


# -------------------- Pins --------------------

@mcp.tool()
def pins_add(channel: str, timestamp: str) -> Dict[str, Any]:
    """Pin a message."""
    data = {"channel": channel, "timestamp": timestamp}
    return _slack_request("POST", "pins.add", data=data)


@mcp.tool()
def pins_remove(channel: str, timestamp: str) -> Dict[str, Any]:
    """Unpin a message."""
    data = {"channel": channel, "timestamp": timestamp}
    return _slack_request("POST", "pins.remove", data=data)


@mcp.tool()
def pins_list(channel: str) -> Dict[str, Any]:
    """List pinned items in a channel."""
    params = {"channel": channel}
    return _slack_request("GET", "pins.list", params=params)


# -------------------- Reminders --------------------

@mcp.tool()
def reminders_add(text: str, time: str, user: Optional[str] = None) -> Dict[str, Any]:
    """Create a reminder. time can be Unix timestamp or natural language (per Slack)."""
    data: Dict[str, Any] = {"text": text, "time": time}
    if user:
        data["user"] = user
    return _slack_request("POST", "reminders.add", data=data)


@mcp.tool()
def reminders_list() -> Dict[str, Any]:
    """List reminders."""
    return _slack_request("GET", "reminders.list")


@mcp.tool()
def reminders_complete(reminder: str) -> Dict[str, Any]:
    """Mark a reminder complete."""
    data = {"reminder": reminder}
    return _slack_request("POST", "reminders.complete", data=data)


@mcp.tool()
def reminders_delete(reminder: str) -> Dict[str, Any]:
    """Delete a reminder."""
    data = {"reminder": reminder}
    return _slack_request("POST", "reminders.delete", data=data)


# -------------------- Team --------------------

@mcp.tool()
def team_info() -> Dict[str, Any]:
    """Get team/workspace info."""
    return _slack_request("GET", "team.info")


@mcp.tool()
def auth_test() -> Dict[str, Any]:
    """Test authentication and get basic bot identity."""
    return _slack_request("GET", "auth.test")


if __name__ == "__main__":
    mcp.run()
