from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="bookmarks_list")
def bookmarks_list(channel_id: str) -> Dict[str, Any]:
    """Lists bookmarks for a channel (bookmarks.list)."""

    try:
        return slack_api_call("bookmarks.list", http_method="POST", json={"channel_id": channel_id})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="bookmarks_add")
def bookmarks_add(
    channel_id: str,
    title: str,
    link: str,
    emoji: Optional[str] = None,
    entity_id: Optional[str] = None,
    type: Optional[str] = None,
) -> Dict[str, Any]:
    """Adds a bookmark to a channel (bookmarks.add)."""

    payload: Dict[str, Any] = {"channel_id": channel_id, "title": title, "link": link}
    if emoji is not None:
        payload["emoji"] = emoji
    if entity_id is not None:
        payload["entity_id"] = entity_id
    if type is not None:
        payload["type"] = type

    try:
        return slack_api_call("bookmarks.add", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="bookmarks_edit")
def bookmarks_edit(
    bookmark_id: str,
    channel_id: str,
    title: Optional[str] = None,
    link: Optional[str] = None,
    emoji: Optional[str] = None,
) -> Dict[str, Any]:
    """Edits a bookmark (bookmarks.edit)."""

    payload: Dict[str, Any] = {"bookmark_id": bookmark_id, "channel_id": channel_id}
    if title is not None:
        payload["title"] = title
    if link is not None:
        payload["link"] = link
    if emoji is not None:
        payload["emoji"] = emoji

    try:
        return slack_api_call("bookmarks.edit", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="bookmarks_remove")
def bookmarks_remove(bookmark_id: str, channel_id: str) -> Dict[str, Any]:
    """Removes a bookmark (bookmarks.remove)."""

    try:
        return slack_api_call(
            "bookmarks.remove", http_method="POST", json={"bookmark_id": bookmark_id, "channel_id": channel_id}
        )
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
