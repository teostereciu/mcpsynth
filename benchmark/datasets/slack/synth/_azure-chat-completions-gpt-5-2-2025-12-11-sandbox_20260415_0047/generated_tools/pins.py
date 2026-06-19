from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="pins_add")
def pins_add(channel: str, timestamp: str) -> Dict[str, Any]:
    """Pins an item to a channel (pins.add)."""

    try:
        return slack_api_call("pins.add", http_method="POST", json={"channel": channel, "timestamp": timestamp})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="pins_remove")
def pins_remove(channel: str, timestamp: str) -> Dict[str, Any]:
    """Un-pins an item from a channel (pins.remove)."""

    try:
        return slack_api_call("pins.remove", http_method="POST", json={"channel": channel, "timestamp": timestamp})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="pins_list")
def pins_list(channel: str) -> Dict[str, Any]:
    """Lists items pinned to a channel (pins.list)."""

    try:
        return slack_api_call("pins.list", http_method="GET", params={"channel": channel})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
