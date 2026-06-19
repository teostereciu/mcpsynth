import os
import requests
from typing import Optional, List, Dict, Any, Union
from fastmcp import FastMCP

mcp = FastMCP("zulip")

def get_auth():
    email = os.environ.get("ZULIP_EMAIL")
    api_key = os.environ.get("ZULIP_API_KEY")
    if not email or not api_key:
        raise ValueError("ZULIP_EMAIL and ZULIP_API_KEY must be set")
    return (email, api_key)

def get_base_url():
    site = os.environ.get("ZULIP_SITE")
    if not site:
        raise ValueError("ZULIP_SITE must be set")
    return f"{site.rstrip('/')}/api/v1"

def make_request(method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
    try:
        url = f"{get_base_url()}{endpoint}"
        auth = get_auth()
        response = requests.request(method, url, auth=auth, **kwargs)
        if response.status_code == 204:
            return {"result": "success"}
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def send_message(type: str, to: Union[str, List[int]], content: str, topic: Optional[str] = None) -> Dict[str, Any]:
    """Send a message to a stream or a private message."""
    data = {"type": type, "to": to, "content": content}
    if type == "stream" and topic:
        data["topic"] = topic
    return make_request("POST", "/messages", data=data)

@mcp.tool()
def edit_message(message_id: int, content: Optional[str] = None, topic: Optional[str] = None, propagate_mode: Optional[str] = None, send_notification_to_old_thread: Optional[bool] = None, send_notification_to_new_thread: Optional[bool] = None) -> Dict[str, Any]:
    """Edit a message."""
    data = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = str(send_notification_to_old_thread).lower()
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = str(send_notification_to_new_thread).lower()
    return make_request("PATCH", f"/messages/{message_id}", data=data)

@mcp.tool()
def delete_message(message_id: int) -> Dict[str, Any]:
    """Delete a message."""
    return make_request("DELETE", f"/messages/{message_id}")

@mcp.tool()
def get_messages(anchor: Union[str, int], num_before: int, num_after: int, narrow: Optional[str] = None, client_gravatar: Optional[bool] = None, apply_markdown: Optional[bool] = None) -> Dict[str, Any]:
    """Fetch messages."""
    params = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after
    }
    if narrow is not None:
        params["narrow"] = narrow
    if client_gravatar is not None:
        params["client_gravatar"] = str(client_gravatar).lower()
    if apply_markdown is not None:
        params["apply_markdown"] = str(apply_markdown).lower()
    return make_request("GET", "/messages", params=params)

@mcp.tool()
def update_message_flags(messages: List[int], op: str, flag: str) -> Dict[str, Any]:
    """Add or remove personal message flags like 'read' or 'starred'."""
    data = {
        "messages": str(messages),
        "op": op,
        "flag": flag
    }
    return make_request("POST", "/messages/flags", data=data)

@mcp.tool()
def get_message_history(message_id: int) -> Dict[str, Any]:
    """Fetch the edit history of a message."""
    return make_request("GET", f"/messages/{message_id}/history")

@mcp.tool()
def get_streams(include_public: Optional[bool] = None, include_web_public: Optional[bool] = None, include_subscribed: Optional[bool] = None, include_all_active: Optional[bool] = None, include_default: Optional[bool] = None, include_owner_subscribed: Optional[bool] = None) -> Dict[str, Any]:
    """Get all streams."""
    params = {}
    if include_public is not None: params["include_public"] = str(include_public).lower()
    if include_web_public is not None: params["include_web_public"] = str(include_web_public).lower()
    if include_subscribed is not None: params["include_subscribed"] = str(include_subscribed).lower()
    if include_all_active is not None: params["include_all_active"] = str(include_all_active).lower()
    if include_default is not None: params["include_default"] = str(include_default).lower()
    if include_owner_subscribed is not None: params["include_owner_subscribed"] = str(include_owner_subscribed).lower()
    return make_request("GET", "/streams", params=params)

@mcp.tool()
def get_stream_id(stream: str) -> Dict[str, Any]:
    """Get the ID of a stream."""
    return make_request("GET", "/get_stream_id", params={"stream": stream})

@mcp.tool()
def subscribe_streams(subscriptions: str, principals: Optional[str] = None, authorization_errors_fatal: Optional[bool] = None, announce: Optional[bool] = None, invite_only: Optional[bool] = None, history_public_to_subscribers: Optional[bool] = None, stream_post_policy: Optional[int] = None, message_retention_days: Optional[Union[int, str]] = None) -> Dict[str, Any]:
    """Subscribe to a stream."""
    data = {"subscriptions": subscriptions}
    if principals is not None: data["principals"] = principals
    if authorization_errors_fatal is not None: data["authorization_errors_fatal"] = str(authorization_errors_fatal).lower()
    if announce is not None: data["announce"] = str(announce).lower()
    if invite_only is not None: data["invite_only"] = str(invite_only).lower()
    if history_public_to_subscribers is not None: data["history_public_to_subscribers"] = str(history_public_to_subscribers).lower()
    if stream_post_policy is not None: data["stream_post_policy"] = stream_post_policy
    if message_retention_days is not None: data["message_retention_days"] = message_retention_days
    return make_request("POST", "/users/me/subscriptions", data=data)

@mcp.tool()
def unsubscribe_streams(subscriptions: str, principals: Optional[str] = None) -> Dict[str, Any]:
    """Unsubscribe from a stream."""
    data = {"subscriptions": subscriptions}
    if principals is not None: data["principals"] = principals
    return make_request("DELETE", "/users/me/subscriptions", data=data)

@mcp.tool()
def get_subscriptions(include_subscribers: Optional[bool] = None) -> Dict[str, Any]:
    """Get subscribed streams."""
    params = {}
    if include_subscribers is not None: params["include_subscribers"] = str(include_subscribers).lower()
    return make_request("GET", "/users/me/subscriptions", params=params)

@mcp.tool()
def update_stream(stream_id: int, description: Optional[str] = None, new_name: Optional[str] = None, is_private: Optional[bool] = None, is_announcement_only: Optional[bool] = None, stream_post_policy: Optional[int] = None, history_public_to_subscribers: Optional[bool] = None, message_retention_days: Optional[Union[int, str]] = None) -> Dict[str, Any]:
    """Update a stream."""
    data = {}
    if description is not None: data["description"] = description
    if new_name is not None: data["new_name"] = new_name
    if is_private is not None: data["is_private"] = str(is_private).lower()
    if is_announcement_only is not None: data["is_announcement_only"] = str(is_announcement_only).lower()
    if stream_post_policy is not None: data["stream_post_policy"] = stream_post_policy
    if history_public_to_subscribers is not None: data["history_public_to_subscribers"] = str(history_public_to_subscribers).lower()
    if message_retention_days is not None: data["message_retention_days"] = message_retention_days
    return make_request("PATCH", f"/streams/{stream_id}", data=data)

@mcp.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    """Archive a stream."""
    return make_request("DELETE", f"/streams/{stream_id}")

@mcp.tool()
def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """Get topics in a stream."""
    return make_request("GET", f"/users/me/{stream_id}/topics")

@mcp.tool()
def mute_topic(stream: str, stream_id: int, topic: str, op: str) -> Dict[str, Any]:
    """Mute or unmute a topic."""
    data = {
        "stream": stream,
        "stream_id": stream_id,
        "topic": topic,
        "op": op
    }
    return make_request("PATCH", "/users/me/subscriptions/muted_topics", data=data)

@mcp.tool()
def get_users(client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    """Get all users."""
    params = {}
    if client_gravatar is not None: params["client_gravatar"] = str(client_gravatar).lower()
    if include_custom_profile_fields is not None: params["include_custom_profile_fields"] = str(include_custom_profile_fields).lower()
    return make_request("GET", "/users", params=params)

@mcp.tool()
def get_own_user() -> Dict[str, Any]:
    """Get own user."""
    return make_request("GET", "/users/me")

@mcp.tool()
def get_user_by_id(user_id: int, client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    """Get a user by ID."""
    params = {}
    if client_gravatar is not None: params["client_gravatar"] = str(client_gravatar).lower()
    if include_custom_profile_fields is not None: params["include_custom_profile_fields"] = str(include_custom_profile_fields).lower()
    return make_request("GET", f"/users/{user_id}", params=params)

@mcp.tool()
def get_user_by_email(email: str, client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    """Get a user by email."""
    params = {}
    if client_gravatar is not None: params["client_gravatar"] = str(client_gravatar).lower()
    if include_custom_profile_fields is not None: params["include_custom_profile_fields"] = str(include_custom_profile_fields).lower()
    return make_request("GET", f"/users/{email}", params=params)

@mcp.tool()
def get_user_presence(user_id_or_email: str) -> Dict[str, Any]:
    """Get user presence."""
    return make_request("GET", f"/users/{user_id_or_email}/presence")

@mcp.tool()
def add_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    """Add a reaction to a message."""
    data = {"emoji_name": emoji_name}
    if emoji_code is not None: data["emoji_code"] = emoji_code
    if reaction_type is not None: data["reaction_type"] = reaction_type
    return make_request("POST", f"/messages/{message_id}/reactions", data=data)

@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    """Remove a reaction from a message."""
    data = {"emoji_name": emoji_name}
    if emoji_code is not None: data["emoji_code"] = emoji_code
    if reaction_type is not None: data["reaction_type"] = reaction_type
    return make_request("DELETE", f"/messages/{message_id}/reactions", data=data)

@mcp.tool()
def get_scheduled_messages() -> Dict[str, Any]:
    """Get scheduled messages."""
    return make_request("GET", "/scheduled_messages")

@mcp.tool()
def create_scheduled_message(type: str, to: Union[str, List[int]], content: str, scheduled_delivery_timestamp: int, topic: Optional[str] = None) -> Dict[str, Any]:
    """Create a scheduled message."""
    data = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp
    }
    if type == "stream" and topic:
        data["topic"] = topic
    return make_request("POST", "/scheduled_messages", data=data)

@mcp.tool()
def edit_scheduled_message(scheduled_message_id: int, req_to: Optional[str] = None, topic: Optional[str] = None, content: Optional[str] = None, scheduled_delivery_timestamp: Optional[int] = None) -> Dict[str, Any]:
    """Edit a scheduled message."""
    data = {}
    if req_to is not None: data["req_to"] = req_to
    if topic is not None: data["topic"] = topic
    if content is not None: data["content"] = content
    if scheduled_delivery_timestamp is not None: data["scheduled_delivery_timestamp"] = scheduled_delivery_timestamp
    return make_request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)

@mcp.tool()
def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """Delete a scheduled message."""
    return make_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")

@mcp.tool()
def get_drafts() -> Dict[str, Any]:
    """Get drafts."""
    return make_request("GET", "/drafts")

@mcp.tool()
def create_drafts(drafts: str) -> Dict[str, Any]:
    """Create drafts."""
    return make_request("POST", "/drafts", data={"drafts": drafts})

@mcp.tool()
def edit_draft(draft_id: int, draft: str) -> Dict[str, Any]:
    """Edit a draft."""
    return make_request("PATCH", f"/drafts/{draft_id}", data={"draft": draft})

@mcp.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    """Delete a draft."""
    return make_request("DELETE", f"/drafts/{draft_id}")

@mcp.tool()
def upload_file(filename: str, content: str) -> Dict[str, Any]:
    """Upload a file."""
    # Note: Zulip file upload requires multipart/form-data
    try:
        url = f"{get_base_url()}/user_uploads"
        auth = get_auth()
        files = {'file': (filename, content)}
        response = requests.post(url, auth=auth, files=files)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
