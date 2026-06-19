"""Mastodon Statuses API tools."""
import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers(auth: bool = True) -> dict:
    h = {"Accept": "application/json"}
    if auth and ACCESS_TOKEN:
        h["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    return h


def _api(path: str) -> str:
    return f"{BASE_URL}{path}"


def register_statuses(mcp: FastMCP) -> None:

    @mcp.tool()
    def post_status(
        status: Optional[str] = None,
        media_ids: Optional[list] = None,
        in_reply_to_id: Optional[str] = None,
        sensitive: Optional[bool] = None,
        spoiler_text: Optional[str] = None,
        visibility: Optional[str] = None,
        language: Optional[str] = None,
        scheduled_at: Optional[str] = None,
        quoted_status_id: Optional[str] = None,
    ) -> dict:
        """Post a new status to Mastodon. visibility: public, unlisted, private, direct."""
        data = {}
        if status is not None:
            data["status"] = status
        if media_ids:
            data["media_ids[]"] = media_ids
        if in_reply_to_id:
            data["in_reply_to_id"] = in_reply_to_id
        if sensitive is not None:
            data["sensitive"] = str(sensitive).lower()
        if spoiler_text:
            data["spoiler_text"] = spoiler_text
        if visibility:
            data["visibility"] = visibility
        if language:
            data["language"] = language
        if scheduled_at:
            data["scheduled_at"] = scheduled_at
        if quoted_status_id:
            data["quoted_status_id"] = quoted_status_id
        try:
            r = requests.post(_api("/api/v1/statuses"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_status(status_id: str) -> dict:
        """Get a single status by ID."""
        try:
            r = requests.get(_api(f"/api/v1/statuses/{status_id}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_status(status_id: str) -> dict:
        """Delete one of your own statuses."""
        try:
            r = requests.delete(_api(f"/api/v1/statuses/{status_id}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_status_context(status_id: str) -> dict:
        """Get parent and child statuses (thread context) for a status."""
        try:
            r = requests.get(_api(f"/api/v1/statuses/{status_id}/context"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def favourite_status(status_id: str) -> dict:
        """Favourite (like) a status."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/favourite"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unfavourite_status(status_id: str) -> dict:
        """Remove a favourite from a status."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/unfavourite"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def reblog_status(status_id: str, visibility: Optional[str] = None) -> dict:
        """Boost (reblog) a status. visibility: public, unlisted, private."""
        data = {}
        if visibility:
            data["visibility"] = visibility
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/reblog"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unreblog_status(status_id: str) -> dict:
        """Undo a boost (reblog) of a status."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/unreblog"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def bookmark_status(status_id: str) -> dict:
        """Bookmark a status."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/bookmark"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unbookmark_status(status_id: str) -> dict:
        """Remove a bookmark from a status."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/unbookmark"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def pin_status(status_id: str) -> dict:
        """Pin a status to your profile."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/pin"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unpin_status(status_id: str) -> dict:
        """Unpin a status from your profile."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/unpin"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mute_status(status_id: str) -> dict:
        """Mute notifications for a status thread."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/mute"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unmute_status(status_id: str) -> dict:
        """Unmute notifications for a status thread."""
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/unmute"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_status_reblogged_by(status_id: str) -> list:
        """Get accounts that reblogged a status."""
        try:
            r = requests.get(_api(f"/api/v1/statuses/{status_id}/reblogged_by"), headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_status_favourited_by(status_id: str) -> list:
        """Get accounts that favourited a status."""
        try:
            r = requests.get(_api(f"/api/v1/statuses/{status_id}/favourited_by"), headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def translate_status(status_id: str, lang: Optional[str] = None) -> dict:
        """Translate a status into another language. lang: ISO 639-1 code (e.g. 'en')."""
        data = {}
        if lang:
            data["lang"] = lang
        try:
            r = requests.post(_api(f"/api/v1/statuses/{status_id}/translate"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_status_history(status_id: str) -> list:
        """Get edit history of a status."""
        try:
            r = requests.get(_api(f"/api/v1/statuses/{status_id}/history"), headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_status_source(status_id: str) -> dict:
        """Get the source (plain text) of a status for editing."""
        try:
            r = requests.get(_api(f"/api/v1/statuses/{status_id}/source"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def edit_status(
        status_id: str,
        status: Optional[str] = None,
        spoiler_text: Optional[str] = None,
        sensitive: Optional[bool] = None,
        language: Optional[str] = None,
        media_ids: Optional[list] = None,
    ) -> dict:
        """Edit an existing status."""
        data = {}
        if status is not None:
            data["status"] = status
        if spoiler_text is not None:
            data["spoiler_text"] = spoiler_text
        if sensitive is not None:
            data["sensitive"] = str(sensitive).lower()
        if language:
            data["language"] = language
        if media_ids:
            data["media_ids[]"] = media_ids
        try:
            r = requests.put(_api(f"/api/v1/statuses/{status_id}"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}
