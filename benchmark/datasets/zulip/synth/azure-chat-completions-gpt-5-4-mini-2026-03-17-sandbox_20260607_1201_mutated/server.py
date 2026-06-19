import json
import os
from typing import Any

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("zulip-rest-api")


def _base_url() -> str:
    site = os.environ.get("ZULIP_SITE", "").rstrip("/")
    return f"{site}/api/v1"


def _auth():
    return (os.environ.get("ZULIP_EMAIL", ""), os.environ.get("ZULIP_API_KEY", ""))


def _request(method: str, path: str, *, params: dict[str, Any] | None = None, data: dict[str, Any] | None = None, files=None):
    try:
        resp = requests.request(method, _base_url() + path, params=params, data=data, files=files, auth=_auth(), timeout=30)
        try:
            payload = resp.json()
        except Exception:
            payload = {"text": resp.text}
        if resp.status_code >= 400:
            return {"error": payload if isinstance(payload, dict) else {"msg": str(payload)}}
        return payload
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def send_message(type: str, to: Any, content: str, message_topic: str | None = None, queue_id: str | None = None, local_id: str | None = None, read_by_sender: bool | None = None):
    data: dict[str, Any] = {"type": type, "to": json.dumps(to) if isinstance(to, (list, dict)) else to, "content": content}
    if message_topic is not None:
        data["message_topic"] = message_topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = str(read_by_sender).lower()
    return _request("POST", "/messages", data=data)


@mcp.tool()
def get_messages(**params):
    return _request("GET", "/messages", params=params)


@mcp.tool()
def get_message(message_id: int):
    return _request("GET", f"/messages/{message_id}")


@mcp.tool()
def update_message(message_id: int, content: str):
    return _request("PATCH", f"/messages/{message_id}", data={"content": content})


@mcp.tool()
def delete_message(message_id: int):
    return _request("DELETE", f"/messages/{message_id}")


@mcp.tool()
def add_reaction(message_id: int, emoji_name: str, emoji_code: str | None = None, reaction_type: str | None = None):
    data = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return _request("POST", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str, emoji_code: str | None = None, reaction_type: str | None = None):
    data = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return _request("DELETE", f"/messages/{message_id}/reactions", data=data)


@mcp.tool()
def get_streams(**params):
    return _request("GET", "/streams", params=params)


@mcp.tool()
def create_stream(name: str, description: str | None = None, invite_only: bool | None = None):
    data = {"name": name}
    if description is not None:
        data["description"] = description
    if invite_only is not None:
        data["invite_only"] = str(invite_only).lower()
    return _request("POST", "/channels/create", data=data)


@mcp.tool()
def update_stream(stream_id: int, **data):
    return _request("PATCH", f"/streams/{stream_id}", data=data)


@mcp.tool()
def archive_stream(stream_id: int):
    return _request("DELETE", f"/streams/{stream_id}")


@mcp.tool()
def get_users(**params):
    return _request("GET", "/users", params=params)


@mcp.tool()
def get_user(user_id: int):
    return _request("GET", f"/users/{user_id}")


@mcp.tool()
def get_own_user():
    return _request("GET", "/users/me")


@mcp.tool()
def get_presence():
    return _request("GET", "/realm/presence")


@mcp.tool()
def get_drafts():
    return _request("GET", "/drafts")


@mcp.tool()
def create_drafts(drafts: str):
    return _request("POST", "/drafts", data={"drafts": drafts})


@mcp.tool()
def get_scheduled_messages():
    return _request("GET", "/scheduled_messages")


@mcp.tool()
def create_scheduled_message(**data):
    return _request("POST", "/scheduled_messages", data=data)


@mcp.tool()
def update_scheduled_message(scheduled_message_id: int, **data):
    return _request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data)


@mcp.tool()
def delete_scheduled_message(scheduled_message_id: int):
    return _request("DELETE", f"/scheduled_messages/{scheduled_message_id}")


if __name__ == "__main__":
    mcp.run(transport="stdio")
