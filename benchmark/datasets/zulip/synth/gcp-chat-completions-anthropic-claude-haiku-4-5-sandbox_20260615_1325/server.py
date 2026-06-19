#!/usr/bin/env python3
"""MCP Server for Zulip REST API"""
import os, json, requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

server = FastMCP("zulip-api")
ZULIP_EMAIL = os.getenv("ZULIP_EMAIL")
ZULIP_API_KEY = os.getenv("ZULIP_API_KEY")
ZULIP_SITE = os.getenv("ZULIP_SITE")
if not all([ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE]):
    raise ValueError("Missing required environment variables")
BASE_URL = f"{ZULIP_SITE}/api/v1"

def make_request(method: str, endpoint: str, params: Optional[dict] = None, json_data: Optional[dict] = None) -> dict:
    url = f"{BASE_URL}/{endpoint}"
    try:
        r = requests.request(method, url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), params=params, json=json_data, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}

@server.tool()
def send_message(type: str, to: str, content: str, topic: Optional[str] = None) -> dict:
    data = {"type": type, "to": to, "content": content}
    if topic: data["topic"] = topic
    return make_request("POST", "messages", json_data=data)

@server.tool()
def get_messages(anchor: str = "newest", num_before: int = 50, num_after: int = 0, narrow: Optional[list] = None) -> dict:
    params = {"anchor": anchor, "num_before": num_before, "num_after": num_after}
    if narrow: params["narrow"] = json.dumps(narrow)
    return make_request("GET", "messages", params=params)

@server.tool()
def get_message(message_id: int) -> dict:
    return make_request("GET", f"messages/{message_id}")

@server.tool()
def edit_message(message_id: int, content: Optional[str] = None, topic: Optional[str] = None) -> dict:
    data = {}
    if content: data["content"] = content
    if topic: data["topic"] = topic
    return make_request("PATCH", f"messages/{message_id}", json_data=data)

@server.tool()
def delete_message(message_id: int) -> dict:
    return make_request("DELETE", f"messages/{message_id}")

@server.tool()
def get_message_history(message_id: int) -> dict:
    return make_request("GET", f"messages/{message_id}/history")

@server.tool()
def add_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: str = "unicode_emoji") -> dict:
    data = {"emoji_name": emoji_name, "reaction_type": reaction_type}
    if emoji_code: data["emoji_code"] = emoji_code
    return make_request("POST", f"messages/{message_id}/reactions", json_data=data)

@server.tool()
def remove_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: str = "unicode_emoji") -> dict:
    params = {"emoji_name": emoji_name, "reaction_type": reaction_type}
    if emoji_code: params["emoji_code"] = emoji_code
    return make_request("DELETE", f"messages/{message_id}/reactions", params=params)

@server.tool()
def update_message_flags(messages: list, flag: str, op: str = "add") -> dict:
    return make_request("POST", "messages/flags", json_data={"messages": messages, "flag": flag, "op": op})

@server.tool()
def mark_all_as_read() -> dict:
    return make_request("POST", "messages/flags", json_data={"op": "add", "flag": "read"})

@server.tool()
def mark_stream_as_read(stream_id: int) -> dict:
    return make_request("POST", "messages/flags/narrow", json_data={"op": "add", "flag": "read", "narrow": [{"operator": "stream", "operand": stream_id}]})

@server.tool()
def mark_topic_as_read(stream_id: int, topic_name: str) -> dict:
    return make_request("POST", "messages/flags/narrow", json_data={"op": "add", "flag": "read", "narrow": [{"operator": "stream", "operand": stream_id}, {"operator": "topic", "operand": topic_name}]})

@server.tool()
def upload_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as f:
            r = requests.post(f"{BASE_URL}/user_uploads", auth=(ZULIP_EMAIL, ZULIP_API_KEY), files={"file": f}, timeout=30)
            r.raise_for_status()
            return r.json()
    except Exception as e:
        return {"error": str(e)}

@server.tool()
def render_message(content: str) -> dict:
    return make_request("POST", "messages/render", json_data={"content": content})

@server.tool()
def get_read_receipts(message_id: int) -> dict:
    return make_request("GET", f"messages/{message_id}/read_receipts")

@server.tool()
def get_scheduled_messages() -> dict:
    return make_request("GET", "scheduled_messages")

@server.tool()
def create_scheduled_message(type: str, to: str, content: str, scheduled_delivery_timestamp: int, topic: Optional[str] = None) -> dict:
    data = {"type": type, "to": to, "content": content, "scheduled_delivery_timestamp": scheduled_delivery_timestamp}
    if topic: data["topic"] = topic
    return make_request("POST", "scheduled_messages", json_data=data)

@server.tool()
def edit_scheduled_message(scheduled_message_id: int, content: Optional[str] = None, scheduled_delivery_timestamp: Optional[int] = None) -> dict:
    data = {}
    if content: data["content"] = content
    if scheduled_delivery_timestamp: data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    return make_request("PATCH", f"scheduled_messages/{scheduled_message_id}", json_data=data)

@server.tool()
def delete_scheduled_message(scheduled_message_id: int) -> dict:
    return make_request("DELETE", f"scheduled_messages/{scheduled_message_id}")

@server.tool()
def get_drafts() -> dict:
    return make_request("GET", "drafts")

@server.tool()
def create_draft(type: str, to: str, content: str, topic: Optional[str] = None) -> dict:
    data = {"type": type, "to": to, "content": content}
    if topic: data["topic"] = topic
    return make_request("POST", "drafts", json_data=data)

@server.tool()
def edit_draft(draft_id: int, content: Optional[str] = None, topic: Optional[str] = None) -> dict:
    data = {}
    if content: data["content"] = content
    if topic: data["topic"] = topic
    return make_request("PATCH", f"drafts/{draft_id}", json_data=data)

@server.tool()
def delete_draft(draft_id: int) -> dict:
    return make_request("DELETE", f"drafts/{draft_id}")

@server.tool()
def get_subscriptions() -> dict:
    return make_request("GET", "subscriptions")

@server.tool()
def get_streams(include_all_active: bool = False) -> dict:
    params = {"include_all_active": "true"} if include_all_active else {}
    return make_request("GET", "streams", params=params)

@server.tool()
def get_stream_by_id(stream_id: int) -> dict:
    return make_request("GET", f"streams/{stream_id}")

@server.tool()
def get_stream_id(stream: str) -> dict:
    return make_request("GET", "get_stream_id", params={"stream": stream})

@server.tool()
def create_channel(name: str, description: str = "", subscribers: Optional[list] = None, invite_only: bool = False, is_web_public: bool = False) -> dict:
    data = {"name": name, "description": description, "subscribers": subscribers or [], "invite_only": invite_only, "is_web_public": is_web_public}
    return make_request("POST", "channels/create", json_data=data)

@server.tool()
def update_channel(stream_id: int, name: Optional[str] = None, description: Optional[str] = None) -> dict:
    data = {}
    if name: data["name"] = name
    if description: data["description"] = description
    return make_request("PATCH", f"streams/{stream_id}", json_data=data)

@server.tool()
def archive_channel(stream_id: int) -> dict:
    return make_request("DELETE", f"streams/{stream_id}")

@server.tool()
def subscribe(streams: list, principals: Optional[list] = None) -> dict:
    data = {"subscriptions": [{"name": s} if isinstance(s, str) else {"stream_id": s} for s in streams]}
    if principals: data["principals"] = principals
    return make_request("POST", "users/me/subscriptions", json_data=data)

@server.tool()
def unsubscribe(streams: list) -> dict:
    return make_request("DELETE", "users/me/subscriptions", json_data={"subscriptions": streams})

@server.tool()
def get_stream_topics(stream_id: int) -> dict:
    return make_request("GET", f"streams/{stream_id}/topics")

@server.tool()
def delete_topic(stream_id: int, topic_name: str) -> dict:
    return make_request("DELETE", f"streams/{stream_id}/topics/{topic_name}", params={"topic_name": topic_name})

@server.tool()
def mute_topic(stream_id: int, topic_name: str) -> dict:
    return make_request("PATCH", "user_topics", json_data={"stream_id": stream_id, "topic": topic_name, "op": "add"})

@server.tool()
def unmute_topic(stream_id: int, topic_name: str) -> dict:
    return make_request("PATCH", "user_topics", json_data={"stream_id": stream_id, "topic": topic_name, "op": "remove"})

@server.tool()
def get_subscription_status(stream_id: int) -> dict:
    return make_request("GET", f"users/me/subscriptions/{stream_id}")

@server.tool()
def get_stream_subscribers(stream_id: int) -> dict:
    return make_request("GET", f"streams/{stream_id}/members")

@server.tool()
def get_user_channels(user_id: int) -> dict:
    return make_request("GET", f"users/{user_id}/subscriptions")

@server.tool()
def get_users(include_custom_profile_fields: bool = False) -> dict:
    params = {"include_custom_profile_fields": "true"} if include_custom_profile_fields else {}
    return make_request("GET", "users", params=params)

@server.tool()
def get_user(user_id: int) -> dict:
    return make_request("GET", f"users/{user_id}")

@server.tool()
def get_user_by_email(email: str) -> dict:
    return make_request("GET", "users/by_email", params={"email": email})

@server.tool()
def get_own_user() -> dict:
    return make_request("GET", "users/me")

@server.tool()
def create_user(email: str, password: str, full_name: str, short_name: Optional[str] = None) -> dict:
    data = {"email": email, "password": password, "full_name": full_name}
    if short_name: data["short_name"] = short_name
    return make_request("POST", "users", json_data=data)

@server.tool()
def update_user(user_id: int, full_name: Optional[str] = None, email: Optional[str] = None) -> dict:
    data = {}
    if full_name: data["full_name"] = full_name
    if email: data["email"] = email
    return make_request("PATCH", f"users/{user_id}", json_data=data)

@server.tool()
def deactivate_user(user_id: int) -> dict:
    return make_request("DELETE", f"users/{user_id}")

@server.tool()
def reactivate_user(user_id: int) -> dict:
    return make_request("PATCH", f"users/{user_id}", json_data={"is_active": True})

@server.tool()
def deactivate_own_user() -> dict:
    return make_request("DELETE", "users/me")

@server.tool()
def get_user_presence(user_id: int) -> dict:
    return make_request("GET", f"users/{user_id}/presence")

@server.tool()
def get_presence() -> dict:
    return make_request("GET", "presence")

@server.tool()
def update_presence(status: str = "active", ping_only: bool = False) -> dict:
    return make_request("POST", "users/me/presence", json_data={"status": status, "ping_only": ping_only})

@server.tool()
def get_user_status(user_id: int) -> dict:
    return make_request("GET", f"users/{user_id}/status")

@server.tool()
def update_status(status_text: str, status_emoji: Optional[str] = None) -> dict:
    data = {"status_text": status_text}
    if status_emoji: data["status_emoji"] = status_emoji
    return make_request("POST", "users/me/status", json_data=data)

@server.tool()
def mute_user(user_id: int) -> dict:
    return make_request("PATCH", f"users/{user_id}/mute", json_data={"op": "add"})

@server.tool()
def unmute_user(user_id: int) -> dict:
    return make_request("PATCH", f"users/{user_id}/mute", json_data={"op": "remove"})

@server.tool()
def get_user_groups() -> dict:
    return make_request("GET", "user_groups")

@server.tool()
def create_user_group(name: str, description: str = "", members: Optional[list] = None) -> dict:
    return make_request("POST", "user_groups/create", json_data={"name": name, "description": description, "members": members or []})

@server.tool()
def update_user_group(user_group_id: int, name: Optional[str] = None, description: Optional[str] = None) -> dict:
    data = {}
    if name: data["name"] = name
    if description: data["description"] = description
    return make_request("PATCH", f"user_groups/{user_group_id}", json_data=data)

@server.tool()
def deactivate_user_group(user_group_id: int) -> dict:
    return make_request("DELETE", f"user_groups/{user_group_id}")

@server.tool()
def get_user_group_members(user_group_id: int) -> dict:
    return make_request("GET", f"user_groups/{user_group_id}/members")

@server.tool()
def update_user_group_members(user_group_id: int, add: Optional[list] = None, remove: Optional[list] = None) -> dict:
    data = {}
    if add: data["add"] = add
    if remove: data["remove"] = remove
    return make_request("POST", f"user_groups/{user_group_id}/members", json_data=data)

@server.tool()
def update_settings(full_name: Optional[str] = None, email: Optional[str] = None, old_password: Optional[str] = None, new_password: Optional[str] = None) -> dict:
    data = {}
    if full_name: data["full_name"] = full_name
    if email: data["email"] = email
    if old_password: data["old_password"] = old_password
    if new_password: data["new_password"] = new_password
    return make_request("PATCH", "settings", json_data=data)

@server.tool()
def get_server_settings() -> dict:
    return make_request("GET", "server_settings")

@server.tool()
def get_attachments() -> dict:
    return make_request("GET", "attachments")

@server.tool()
def delete_attachment(attachment_id: int) -> dict:
    return make_request("DELETE", f"attachments/{attachment_id}")

@server.tool()
def get_custom_emoji() -> dict:
    return make_request("GET", "custom_emoji")

@server.tool()
def upload_custom_emoji(emoji_name: str, file_path: str) -> dict:
    try:
        with open(file_path, "rb") as f:
            r = requests.post(f"{BASE_URL}/custom_emoji/{emoji_name}", auth=(ZULIP_EMAIL, ZULIP_API_KEY), files={"file": f}, timeout=30)
            r.raise_for_status()
            return r.json()
    except Exception as e:
        return {"error": str(e)}

@server.tool()
def deactivate_custom_emoji(emoji_name: str) -> dict:
    return make_request("DELETE", f"custom_emoji/{emoji_name}")

@server.tool()
def get_invites() -> dict:
    return make_request("GET", "invites")

@server.tool()
def send_invites(invitee_emails: list, stream_ids: Optional[list] = None, invite_expires_in_days: int = 30) -> dict:
    data = {"invitee_emails": invitee_emails, "invite_expires_in_days": invite_expires_in_days}
    if stream_ids: data["stream_ids"] = stream_ids
    return make_request("POST", "invites", json_data=data)

@server.tool()
def revoke_email_invite(email: str, invite_id: Optional[int] = None) -> dict:
    if invite_id:
        return make_request("DELETE", f"invites/{invite_id}")
    return make_request("DELETE", "invites", params={"email": email})

@server.tool()
def get_alert_words() -> dict:
    return make_request("GET", "user_topics")

@server.tool()
def add_alert_words(alert_words: list) -> dict:
    return make_request("POST", "user_topics", json_data={"alert_words": alert_words})

@server.tool()
def remove_alert_words(alert_words: list) -> dict:
    return make_request("DELETE", "user_topics", json_data={"alert_words": alert_words})

@server.tool()
def get_api_key(password: str) -> dict:
    return make_request("POST", "fetch_api_key", json_data={"password": password})

@server.tool()
def regenerate_api_key() -> dict:
    return make_request("POST", "users/me/api_key/regenerate")

@server.tool()
def get_reminders() -> dict:
    return make_request("GET", "reminders")

@server.tool()
def create_reminder(message_id: int, reminder_timestamp: int) -> dict:
    return make_request("POST", "reminders", json_data={"message_id": message_id, "reminder_timestamp": reminder_timestamp})

@server.tool()
def delete_reminder(reminder_id: int) -> dict:
    return make_request("DELETE", f"reminders/{reminder_id}")

@server.tool()
def set_typing_status(op: str, to: str, type: str = "direct", topic: Optional[str] = None) -> dict:
    data = {"op": op, "to": to, "type": type}
    if topic: data["topic"] = topic
    return make_request("POST", "typing", json_data=data)

@server.tool()
def get_linkifiers() -> dict:
    return make_request("GET", "linkifiers")

@server.tool()
def add_linkifier(pattern: str, url_template: str) -> dict:
    return make_request("POST", "linkifiers", json_data={"pattern": pattern, "url_template": url_template})

@server.tool()
def update_linkifier(linkifier_id: int, pattern: str, url_template: str) -> dict:
    return make_request("PATCH", f"linkifiers/{linkifier_id}", json_data={"pattern": pattern, "url_template": url_template})

@server.tool()
def remove_linkifier(linkifier_id: int) -> dict:
    return make_request("DELETE", f"linkifiers/{linkifier_id}")

@server.tool()
def get_channel_folders() -> dict:
    return make_request("GET", "channel_folders")

@server.tool()
def create_channel_folder(name: str) -> dict:
    return make_request("POST", "channel_folders", json_data={"name": name})

@server.tool()
def update_channel_folder(folder_id: int, name: str) -> dict:
    return make_request("PATCH", f"channel_folders/{folder_id}", json_data={"name": name})

@server.tool()
def delete_channel_folder(folder_id: int) -> dict:
    return make_request("DELETE", f"channel_folders/{folder_id}")

@server.tool()
def get_custom_profile_fields() -> dict:
    return make_request("GET", "custom_profile_fields")

@server.tool()
def create_custom_profile_field(type: str, name: str, hint: str = "") -> dict:
    return make_request("POST", "custom_profile_fields", json_data={"type": type, "name": name, "hint": hint})

@server.tool()
def register_queue(event_types: Optional[list] = None, all_public_streams: bool = False) -> dict:
    data = {}
    if event_types: data["event_types"] = event_types
    if all_public_streams: data["all_public_streams"] = all_public_streams
    return make_request("POST", "register", json_data=data)

@server.tool()
def get_events(queue_id: str, last_event_id: int = -1) -> dict:
    return make_request("GET", "events", params={"queue_id": queue_id, "last_event_id": last_event_id})

@server.tool()
def delete_queue(queue_id: str) -> dict:
    return make_request("DELETE", "events", params={"queue_id": queue_id})

@server.tool()
def get_code_playgrounds() -> dict:
    return make_request("GET", "code_playgrounds")

@server.tool()
def add_code_playground(name: str, pygments_language: str, url_template: str) -> dict:
    return make_request("POST", "code_playgrounds", json_data={"name": name, "pygments_language": pygments_language, "url_template": url_template})

@server.tool()
def remove_code_playground(playground_id: int) -> dict:
    return make_request("DELETE", f"code_playgrounds/{playground_id}")

@server.tool()
def get_saved_snippets() -> dict:
    return make_request("GET", "saved_snippets")

@server.tool()
def create_saved_snippet(title: str, content: str) -> dict:
    return make_request("POST", "saved_snippets", json_data={"title": title, "content": content})

@server.tool()
def edit_saved_snippet(snippet_id: int, title: Optional[str] = None, content: Optional[str] = None) -> dict:
    data = {}
    if title: data["title"] = title
    if content: data["content"] = content
    return make_request("PATCH", f"saved_snippets/{snippet_id}", json_data=data)

@server.tool()
def delete_saved_snippet(snippet_id: int) -> dict:
    return make_request("DELETE", f"saved_snippets/{snippet_id}")

if __name__ == "__main__":
    server.run()
