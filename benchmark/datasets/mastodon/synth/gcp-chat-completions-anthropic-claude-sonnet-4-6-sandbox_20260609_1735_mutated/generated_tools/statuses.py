"""Mastodon statuses API tools."""
import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def _api(path: str) -> str:
    return f"{BASE_URL}{path}"


def register(mcp: FastMCP):

    @mcp.tool()
    def post_status(
        status: Optional[str] = None,
        media_ids: Optional[list] = None,
        reply_to_id: Optional[str] = None,
        is_sensitive: Optional[bool] = None,
        content_warning: Optional[str] = None,
        post_visibility: Optional[str] = None,
        lang: Optional[str] = None,
        scheduled_at: Optional[str] = None,
        quoted_status_id: Optional[str] = None,
        poll_options: Optional[list] = None,
        poll_expires_in: Optional[int] = None,
        poll_multiple: Optional[bool] = None,
        poll_hide_totals: Optional[bool] = None,
    ) -> dict:
        """Post a new status to Mastodon.

        Args:
            status: Text content of the status.
            media_ids: List of media attachment IDs to attach.
            reply_to_id: ID of the status being replied to.
            is_sensitive: Mark status as sensitive.
            content_warning: Subject/warning text shown before content.
            post_visibility: 'public', 'unlisted', 'private', or 'direct'.
            lang: ISO 639-1 language code.
            scheduled_at: ISO datetime to schedule the post (min 5 min future).
            quoted_status_id: ID of the status being quoted.
            poll_options: List of poll answer strings.
            poll_expires_in: Poll duration in seconds.
            poll_multiple: Allow multiple poll choices.
            poll_hide_totals: Hide poll vote counts until ended.
        """
        try:
            data = {}
            if status is not None:
                data["status"] = status
            if media_ids:
                data["media_ids[]"] = media_ids
            if reply_to_id:
                data["reply_to_id"] = reply_to_id
            if is_sensitive is not None:
                data["is_sensitive"] = str(is_sensitive).lower()
            if content_warning:
                data["content_warning"] = content_warning
            if post_visibility:
                data["post_visibility"] = post_visibility
            if lang:
                data["lang"] = lang
            if scheduled_at:
                data["scheduled_at"] = scheduled_at
            if quoted_status_id:
                data["quoted_status_id"] = quoted_status_id
            if poll_options:
                data["poll[options][]"] = poll_options
            if poll_expires_in is not None:
                data["poll[expires_in]"] = poll_expires_in
            if poll_multiple is not None:
                data["poll[multiple]"] = str(poll_multiple).lower()
            if poll_hide_totals is not None:
                data["poll[hide_totals]"] = str(poll_hide_totals).lower()
            resp = requests.post(_api("/api/v1/statuses"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_status(status_id: str) -> dict:
        """Get a single status by ID.

        Args:
            status_id: The ID of the status.
        """
        try:
            resp = requests.get(_api(f"/api/v1/statuses/{status_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_status(status_id: str) -> dict:
        """Delete one of your own statuses.

        Args:
            status_id: The ID of the status to delete.
        """
        try:
            resp = requests.delete(_api(f"/api/v1/statuses/{status_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_status_context(status_id: str) -> dict:
        """Get parent and child statuses (thread context) for a status.

        Args:
            status_id: The ID of the status.
        """
        try:
            resp = requests.get(_api(f"/api/v1/statuses/{status_id}/context"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def favourite_status(status_id: str) -> dict:
        """Favourite (like) a status.

        Args:
            status_id: The ID of the status to favourite.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/favourite"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unfavourite_status(status_id: str) -> dict:
        """Remove a favourite from a status.

        Args:
            status_id: The ID of the status to unfavourite.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/unfavourite"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def reblog_status(status_id: str, visibility: Optional[str] = None) -> dict:
        """Boost (reblog) a status.

        Args:
            status_id: The ID of the status to boost.
            visibility: Visibility of the boost: 'public', 'unlisted', 'private'.
        """
        try:
            data = {}
            if visibility:
                data["visibility"] = visibility
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/reblog"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unreblog_status(status_id: str) -> dict:
        """Undo a boost (reblog) of a status.

        Args:
            status_id: The ID of the status to unreblog.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/unreblog"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def bookmark_status(status_id: str) -> dict:
        """Bookmark a status.

        Args:
            status_id: The ID of the status to bookmark.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/bookmark"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unbookmark_status(status_id: str) -> dict:
        """Remove a bookmark from a status.

        Args:
            status_id: The ID of the status to unbookmark.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/unbookmark"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_status_reblogged_by(status_id: str, max_id: Optional[str] = None, limit: Optional[int] = None) -> list:
        """Get accounts that boosted a status.

        Args:
            status_id: The ID of the status.
            max_id: Return results older than this ID.
            limit: Maximum number of results (default 40, max 80).
        """
        try:
            params = {}
            if max_id:
                params["max_id"] = max_id
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api(f"/api/v1/statuses/{status_id}/reblogged_by"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_status_favourited_by(status_id: str, max_id: Optional[str] = None, limit: Optional[int] = None) -> list:
        """Get accounts that favourited a status.

        Args:
            status_id: The ID of the status.
            max_id: Return results older than this ID.
            limit: Maximum number of results (default 40, max 80).
        """
        try:
            params = {}
            if max_id:
                params["max_id"] = max_id
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api(f"/api/v1/statuses/{status_id}/favourited_by"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def pin_status(status_id: str) -> dict:
        """Pin a status to your profile.

        Args:
            status_id: The ID of the status to pin.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/pin"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unpin_status(status_id: str) -> dict:
        """Unpin a status from your profile.

        Args:
            status_id: The ID of the status to unpin.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/unpin"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mute_status(status_id: str) -> dict:
        """Mute notifications for a status thread.

        Args:
            status_id: The ID of the status to mute.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/mute"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unmute_status(status_id: str) -> dict:
        """Unmute notifications for a status thread.

        Args:
            status_id: The ID of the status to unmute.
        """
        try:
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/unmute"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def translate_status(status_id: str, lang: Optional[str] = None) -> dict:
        """Translate a status into another language.

        Args:
            status_id: The ID of the status to translate.
            lang: ISO 639-1 target language code (e.g. 'en', 'fr').
        """
        try:
            data = {}
            if lang:
                data["lang"] = lang
            resp = requests.post(_api(f"/api/v1/statuses/{status_id}/translate"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_status_history(status_id: str) -> list:
        """Get edit history of a status.

        Args:
            status_id: The ID of the status.
        """
        try:
            resp = requests.get(_api(f"/api/v1/statuses/{status_id}/history"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_status_source(status_id: str) -> dict:
        """Get the source (plain text) of a status for editing.

        Args:
            status_id: The ID of the status.
        """
        try:
            resp = requests.get(_api(f"/api/v1/statuses/{status_id}/source"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def edit_status(
        status_id: str,
        status: Optional[str] = None,
        content_warning: Optional[str] = None,
        is_sensitive: Optional[bool] = None,
        post_visibility: Optional[str] = None,
        lang: Optional[str] = None,
        media_ids: Optional[list] = None,
    ) -> dict:
        """Edit an existing status.

        Args:
            status_id: The ID of the status to edit.
            status: New text content.
            content_warning: New subject/warning text.
            is_sensitive: Mark as sensitive.
            post_visibility: New visibility setting.
            lang: ISO 639-1 language code.
            media_ids: New list of media attachment IDs.
        """
        try:
            data = {}
            if status is not None:
                data["status"] = status
            if content_warning is not None:
                data["content_warning"] = content_warning
            if is_sensitive is not None:
                data["is_sensitive"] = str(is_sensitive).lower()
            if post_visibility:
                data["post_visibility"] = post_visibility
            if lang:
                data["lang"] = lang
            if media_ids:
                data["media_ids[]"] = media_ids
            resp = requests.put(_api(f"/api/v1/statuses/{status_id}"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
