import os
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Zulip")

def get_client():
    email = os.environ.get("ZULIP_EMAIL")
    api_key = os.environ.get("ZULIP_API_KEY")
    site = os.environ.get("ZULIP_SITE")
    if not email or not api_key or not site:
        return None, None
    
    session = requests.Session()
    session.auth = (email, api_key)
    return session, f"{site.rstrip('/')}/api/v1"

def make_request(method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
    session, base_url = get_client()
    if not session:
        return {"error": "ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set"}
    
    url = f"{base_url}{endpoint}"
    try:
        response = session.request(method, url, **kwargs)
        if response.status_code == 204:
            return {"result": "success"}
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def send_message(type: str, to: Any, content: str, topic: Optional[str] = None) -> Dict[str, Any]:
    """Send a message to a stream or a private message."""
    data = {"type": type, "to": to, "content": content}
    if type == "stream" and topic:
        data["topic"] = topic
    return make_request("POST", "/messages", data=data)

@mcp.tool()
def edit_message(message_id: int, content: Optional[str] = None, topic: Optional[str] = None, propagate_mode: Optional[str] = None) -> Dict[str, Any]:
    """Edit a message."""
    data = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    return make_request("PATCH", f"/messages/{message_id}", data=data)

@mcp.tool()
def delete_message(message_id: int) -> Dict[str, Any]:
    """Delete a message."""
    return make_request("DELETE", f"/messages/{message_id}")

@mcp.tool()
def get_messages(anchor: Any, num_before: int, num_after: int, narrow: Optional[str] = None) -> Dict[str, Any]:
    """Fetch message history."""
    params = {"anchor": anchor, "num_before": num_before, "num_after": num_after}
    if narrow:
        params["narrow"] = narrow
    return make_request("GET", "/messages", params=params)

@mcp.tool()
def update_message_flags(messages: List[int], op: str, flag: str) -> Dict[str, Any]:
    """Add or remove personal message flags like 'read' or 'starred'."""
    data = {"messages": messages, "op": op, "flag": flag}
    return make_request("POST", "/messages/flags", data=data)

@mcp.tool()
def get_streams(include_public: bool = True, include_web_public: bool = False, include_subscribed: bool = True, include_all_active: bool = False) -> Dict[str, Any]:
    """Get all streams."""
    params = {
        "include_public": include_public,
        "include_web_public": include_web_public,
        "include_subscribed": include_subscribed,
        "include_all_active": include_all_active
    }
    return make_request("GET", "/streams", params=params)

@mcp.tool()
def get_stream_id(stream: str) -> Dict[str, Any]:
    """Get the ID of a stream."""
    return make_request("GET", "/get_stream_id", params={"stream": stream})

@mcp.tool()
def subscribe_streams(subscriptions: str) -> Dict[str, Any]:
    """Subscribe to streams. subscriptions is a JSON-encoded list of dictionaries."""
    return make_request("POST", "/users/me/subscriptions", data={"subscriptions": subscriptions})

@mcp.tool()
def unsubscribe_streams(subscriptions: str) -> Dict[str, Any]:
    """Unsubscribe from streams. subscriptions is a JSON-encoded list of stream names."""
    return make_request("DELETE", "/users/me/subscriptions", data={"subscriptions": subscriptions})

@mcp.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    """Archive a stream."""
    return make_request("DELETE", f"/streams/{stream_id}")

@mcp.tool()
def update_stream(stream_id: int, description: Optional[str] = None, new_name: Optional[str] = None, is_private: Optional[bool] = None) -> Dict[str, Any]:
    """Update a stream."""
    data = {}
    if description is not None:
        data["description"] = description
    if new_name is not None:
        data["new_name"] = new_name
    if is_private is not None:
        data["is_private"] = is_private
    return make_request("PATCH", f"/streams/{stream_id}", data=data)

@mcp.tool()
def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """Get topics in a stream."""
    return make_request("GET", f"/users/me/{stream_id}/topics")

@mcp.tool()
def mute_topic(stream: str, stream_id: int, topic: str, op: str) -> Dict[str, Any]:
    """Mute or unmute a topic. op can be 'add' or 'remove'."""
    data = {"stream": stream, "stream_id": stream_id, "topic": topic, "op": op}
    return make_request("PATCH", "/users/me/subscriptions/muted_topics", data=data)

@mcp.tool()
def get_users() -> Dict[str, Any]:
    """Get all users."""
    return make_request("GET", "/users")

@mcp.tool()
def get_own_user() -> Dict[str, Any]:
    """Get own user."""
    return make_request("GET", "/users/me")

@mcp.tool()
def get_user_presence(user_id_or_email: str) -> Dict[str, Any]:
    """Get user presence."""
    return make_request("GET", f"/users/{user_id_or_email}/presence")

@mcp.tool()
def update_status(status_text: Optional[str] = None, emoji_name: Optional[str] = None, emoji_code: Optional[str] = None) -> Dict[str, Any]:
    """Update user status."""
    data = {}
    if status_text is not None:
        data["status_text"] = status_text
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    return make_request("POST", "/users/me/status", data=data)

@mcp.tool()
def add_reaction(message_id: int, emoji_name: str) -> Dict[str, Any]:
    """Add a reaction to a message."""
    return make_request("POST", f"/messages/{message_id}/reactions", data={"emoji_name": emoji_name})

@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str) -> Dict[str, Any]:
    """Remove a reaction from a message."""
    return make_request("DELETE", f"/messages/{message_id}/reactions", data={"emoji_name": emoji_name})

@mcp.tool()
def get_scheduled_messages() -> Dict[str, Any]:
    """Get scheduled messages."""
    return make_request("GET", "/scheduled_messages")

@mcp.tool()
def create_scheduled_message(type: str, to: Any, content: str, scheduled_delivery_timestamp: int, topic: Optional[str] = None) -> Dict[str, Any]:
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
def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """Delete a scheduled message."""
    return make_request("DELETE", f"/scheduled_messages/{scheduled_message_id}")

@mcp.tool()
def get_drafts() -> Dict[str, Any]:
    """Get drafts."""
    return make_request("GET", "/drafts")

@mcp.tool()
def create_drafts(drafts: str) -> Dict[str, Any]:
    """Create drafts. drafts is a JSON-encoded list of dictionaries."""
    return make_request("POST", "/drafts", data={"drafts": drafts})

@mcp.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    """Delete a draft."""
    return make_request("DELETE", f"/drafts/{draft_id}")

@mcp.tool()
def upload_file(file_path: str) -> Dict[str, Any]:
    """Upload a file."""
    try:
        with open(file_path, 'rb') as f:
            session, base_url = get_client()
            if not session:
                return {"error": "ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set"}
            response = session.post(f"{base_url}/user_uploads", files={'file': f})
            return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
