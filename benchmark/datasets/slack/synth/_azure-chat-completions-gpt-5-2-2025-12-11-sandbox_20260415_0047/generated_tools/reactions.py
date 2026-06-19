from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="reactions_add")
def reactions_add(channel: str, name: str, timestamp: str) -> Dict[str, Any]:
    """Adds a reaction to an item (reactions.add)."""

    try:
        return slack_api_call(
            "reactions.add",
            http_method="POST",
            json={"channel": channel, "name": name, "timestamp": timestamp},
        )
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="reactions_remove")
def reactions_remove(channel: str, name: str, timestamp: str) -> Dict[str, Any]:
    """Removes a reaction from an item (reactions.remove)."""

    try:
        return slack_api_call(
            "reactions.remove",
            http_method="POST",
            json={"channel": channel, "name": name, "timestamp": timestamp},
        )
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="reactions_get")
def reactions_get(
    channel: str,
    timestamp: str,
    full: Optional[bool] = None,
) -> Dict[str, Any]:
    """Gets reactions for an item (reactions.get)."""

    params: Dict[str, Any] = {"channel": channel, "timestamp": timestamp}
    if full is not None:
        params["full"] = full

    try:
        return slack_api_call("reactions.get", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="reactions_list")
def reactions_list(
    user: Optional[str] = None,
    full: Optional[bool] = None,
    count: Optional[int] = None,
    page: Optional[int] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """Lists reactions made by a user (reactions.list)."""

    params: Dict[str, Any] = {}
    if user is not None:
        params["user"] = user
    if full is not None:
        params["full"] = full
    if count is not None:
        params["count"] = count
    if page is not None:
        params["page"] = page
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    try:
        return slack_api_call("reactions.list", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
