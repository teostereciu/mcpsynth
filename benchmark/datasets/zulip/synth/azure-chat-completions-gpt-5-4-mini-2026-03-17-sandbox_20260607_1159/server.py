import json
import os
from typing import Any

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("zulip-rest-api")

BASE_URL = os.environ.get("ZULIP_SITE", "").rstrip("/") + "/api/v1"
EMAIL = os.environ.get("ZULIP_EMAIL")
API_KEY = os.environ.get("ZULIP_API_KEY")
AUTH = (EMAIL, API_KEY) if EMAIL and API_KEY else None


def _request(method: str, path: str, *, params: dict[str, Any] | None = None, data: dict[str, Any] | None = None, files: dict[str, Any] | None = None) -> Any:
    try:
        resp = requests.request(method, BASE_URL + path, params=params, data=data, files=files, auth=AUTH, timeout=30)
        try:
            payload = resp.json()
        except Exception:
            payload = resp.text
        if resp.status_code >= 400:
            return {"error": payload if isinstance(payload, str) else payload}
        return payload
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def send_message(type: str, to: Any, content: str, topic: str | None = None, queue_id: str | None = None, local_id: str | None = None, read_by_sender: bool | None = None):
    data: dict[str, Any] = {"type": type, "to": json.dumps(to) if isinstance(to, (list, dict)) else to, "content": content}
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = json.dumps(read_by_sender)
    return _request("POST", "/messages", data=data)


@mcp.tool()
def get_messages(anchor: str | int | None = None, num_before: int | None = None, num_after: int | None = None, narrow: Any | None = None, message_ids: list[int] | None = None, include_anchor: bool | None = None, apply_markdown: bool | None = None, client_gravatar: bool | None = None, allow_empty_topic_name: bool | None = None):
    params: dict[str, Any] = {}
    for k, v in {"anchor": anchor, "num_before": num_before, "num_after": num_after, "narrow": narrow, "message_ids": message_ids, "include_anchor": include_anchor, "apply_markdown": apply_markdown, "client_gravatar": client_gravatar, "allow_empty_topic_name": allow_empty_topic_name}.items():
        if v is not None:
            params[k] = json.dumps(v) if isinstance(v, (list, dict)) else v
    return _request("GET", "/messages", params=params)


@mcp.tool()
def get_message(message_id: int):
    return _request("GET", f"/messages/{message_id}")


@mcp.tool()
def delete_message(message_id: int):
    return _request("DELETE", f"/messages/{message_id}")


@mcp.tool()
def edit_message(message_id: int, content: str, topic: str | None = None, stream_id: int | None = None):
    data: dict[str, Any] = {"content": content}
    if topic is not None:
        data["topic"] = topic
    if stream_id is not None:
        data["stream_id"] = stream_id
    return _request("PATCH", f"/messages/{message_id}", data=data)


@mcp.tool()
def add_reaction(message_id: int, emoji_name: str, emoji_code: str | None = None, reaction_type: str | None = None):
    data: dict[str, Any] = {"message_id": message_id, "emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return _request("POST", "/messages/{message_id}/reactions", data=data)


@mcp.tool()
def remove_reaction(message_id: int, emoji_name: str, emoji_code: str | None = None, reaction_type: str | None = None):
    data: dict[str, Any] = {"message_id": message_id, "emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return _request("DELETE", "/messages/{message_id}/reactions", data=data)


if __name__ == "__main__":
    mcp.run()
