import os
import json
import requests
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Zulip")

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

def get_base_url() -> str:
    site = ZULIP_SITE.rstrip("/") if ZULIP_SITE else ""
    return f"{site}/api/v1"

def get_auth() -> tuple[str, str]:
    return (ZULIP_EMAIL or "", ZULIP_API_KEY or "")

def make_request(method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
    url = f"{get_base_url()}{endpoint}"
    auth = get_auth()
    try:
        response = requests.request(method, url, auth=auth, **kwargs)
        if response.status_code == 204:
            return {"result": "success"}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except ValueError:
        return {"error": "Invalid JSON response", "status_code": response.status_code, "text": response.text}

# --- Messages ---

@mcp.tool()
def send_message(type: str, to: Union[int, List[int], str], content: str, topic: Optional[str] = None) -> Dict[str, Any]:
    """Send a message to a stream or private message."""
    data = {"type": type, "to": to, "content": content}
    if type == "stream" and topic:
        data["topic"] = topic
    return make_request("POST", "/messages", data=data)

@mcp.tool()
def update_message(message_id: int, content: Optional[str] = None, topic: Optional[str] = None, propagate_mode: Optional[str] = None) -> Dict[str, Any]:
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
def get_messages(anchor: Union[str, int], num_before: int, num_after: int, narrow: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
    """Fetch message history."""
    params = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after
    }
    if narrow:
        params["narrow"] = json.dumps(narrow)
    return make_request("GET", "/messages", params=params)

@mcp.tool()
def update_message_flags(messages: List[int], op: str, flag: str) -> Dict[str, Any]:
    """Update message flags (e.g., mark as read)."""
    data = {
        "messages": json.dumps(messages),
        "op": op,
        "flag": flag
    }
    return make_request("POST", "/messages/flags", data=data)

# --- Streams ---

@mcp.tool()
def get_streams(include_public: bool = True, include_web_public: bool = False, include_subscribed: bool = True, include_all_active: bool = False) -> Dict[str, Any]:
    """Get all streams."""
    params = {
        "include_public": str(include_public).lower(),
        "include_web_public": str(include_web_public).lower(),
        "include_subscribed": str(include_subscribed).lower(),
        "include_all_active": str(include_all_active).lower()
    }
    return make_request("GET", "/streams", params=params)

@mcp.tool()
def get_stream_id(stream: str) -> Dict[str, Any]:
    """Get the ID of a stream."""
    return make_request("GET", "/get_stream_id", params={"stream": stream})

@mcp.tool()
def subscribe_streams(subscriptions: List[Dict[str, str]]) -> Dict[str, Any]:
    """Subscribe to streams."""
    data = {"subscriptions": json.dumps(subscriptions)}
    return make_request("POST", "/users/me/subscriptions", data=data)

@mcp.tool()
def unsubscribe_streams(subscriptions: List[str]) -> Dict[str, Any]:
    """Unsubscribe from streams."""
    data = {"subscriptions": json.dumps(subscriptions)}
    return make_request("DELETE", "/users/me/subscriptions", data=data)

@mcp.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    """Archive a stream."""
    return make_request("DELETE", f"/streams/{stream_id}")

# --- Topics ---

@mcp.tool()
def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """Get topics in a stream."""
    return make_request("GET", f"/users/me/{stream_id}/topics")

@mcp.tool()
def mute_topic(stream: str, stream_id: int, topic: str, op: str = "add") -> Dict[str, Any]:
    """Mute or unmute a topic."""
    data = {
        "stream": stream,
        "stream_id": stream_id,
        "topic": topic,
        "op": op
    }
    return make_request("PATCH", "/users/me/subscriptions/muted_topics", data=data)

# --- Users ---

@mcp.tool()
def get_users() -> Dict[str, Any]:
    """Get all users."""
    return make_request("GET", "/users")

@mcp.tool()
def get_own_user() -> Dict[str, Any]:
    """Get own user profile."""
    return make_request("GET", "/users/me")

@mcp.tool()
def get_presence(user_id_or_email: str) -> Dict[str, Any]:
    """Get user presence."""
    return make_request("GET", f"/users/{user_id_or_email}/presence")

# --- Reactions ---

@mcp.tool()
def add_reaction(message_id: int, emoji_name: str) -> Dict[str, Any]:
    """Add a reaction to a message."""
    data = {"emoji_name": emoji_name}
    return make_request("POST", f"/messages/{message_id}/reactions", data=data)

@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str) -> Dict[str, Any]:
    """Remove a reaction from a message."""
    data = {"emoji_name": emoji_name}
    return make_request("DELETE", f"/messages/{message_id}/reactions", data=data)

# --- Scheduled Messages ---

@mcp.tool()
def get_scheduled_messages() -> Dict[str, Any]:
    """Get scheduled messages."""
    return make_request("GET", "/scheduled_messages")

@mcp.tool()
def create_scheduled_message(type: str, to: Union[int, List[int]], content: str, scheduled_delivery_timestamp: int, topic: Optional[str] = None) -> Dict[str, Any]:
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

# --- Drafts ---

@mcp.tool()
def get_drafts() -> Dict[str, Any]:
    """Get drafts."""
    return make_request("GET", "/drafts")

@mcp.tool()
def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create drafts."""
    data = {"drafts": json.dumps(drafts)}
    return make_request("POST", "/drafts", data=data)

@mcp.tool()
def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    """Edit a draft."""
    data = {"draft": json.dumps(draft)}
    return make_request("PATCH", f"/drafts/{draft_id}", data=data)

@mcp.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    """Delete a draft."""
    return make_request("DELETE", f"/drafts/{draft_id}")

if __name__ == "__main__":
    mcp.run()
