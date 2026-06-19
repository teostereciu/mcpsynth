import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("ZULIP_SITE", "").rstrip("/") + "/api/v1"
EMAIL = os.environ.get("ZULIP_EMAIL", "")
API_KEY = os.environ.get("ZULIP_API_KEY", "")

mcp = FastMCP("zulip-rest-api")


def _client():
    s = requests.Session()
    s.auth = (EMAIL, API_KEY)
    return s


def _result(resp: requests.Response) -> Dict[str, Any]:
    try:
        data = resp.json()
    except Exception:
        data = {"text": resp.text}
    if resp.ok:
        return data if isinstance(data, dict) else {"result": data}
    return {"error": data if isinstance(data, str) else data}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["send_message", "get_messages", "delete_message", "create_stream", "subscribe_streams"]}


@mcp.tool()
def send_message(to: str, content: str, topic: str) -> Dict[str, Any]:
    resp = _client().post(f"{BASE_URL}/messages", data={"type": "stream", "to": to, "topic": topic, "content": content})
    return _result(resp)


@mcp.tool()
def get_messages(anchor: int = -1, num_before: int = 10, num_after: int = 10) -> Dict[str, Any]:
    resp = _client().get(f"{BASE_URL}/messages", params={"anchor": anchor, "num_before": num_before, "num_after": num_after})
    return _result(resp)


def delete_message(message_id: int) -> Dict[str, Any]:
    resp = _client().delete(f"{BASE_URL}/messages/{message_id}")
    return _result(resp)


@mcp.tool()
def create_stream(name: str, description: str = "") -> Dict[str, Any]:
    resp = _client().post(f"{BASE_URL}/streams", json={"subscriptions": [{"name": name, "description": description}]})
    return _result(resp)


@mcp.tool()
def subscribe_streams(streams: list[str]) -> Dict[str, Any]:
    resp = _client().post(f"{BASE_URL}/users/me/subscriptions", json={"subscriptions": [{"name": s} for s in streams]})
    return _result(resp)


if __name__ == "__main__":
    mcp.run()
