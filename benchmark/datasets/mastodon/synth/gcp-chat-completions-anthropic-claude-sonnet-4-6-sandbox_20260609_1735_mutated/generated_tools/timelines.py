"""Mastodon timelines API tools."""
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
    def get_home_timeline(
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list:
        """Get the home timeline (statuses from followed accounts and hashtags).

        Args:
            max_id: Return results older than this ID.
            since_id: Return results newer than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Maximum number of results (default 20, max 40).
        """
        try:
            params = {}
            if max_id:
                params["max_id"] = max_id
            if since_id:
                params["since_id"] = since_id
            if min_id:
                params["min_id"] = min_id
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api("/api/v1/timelines/home"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_public_timeline(
        local: Optional[bool] = None,
        remote: Optional[bool] = None,
        only_media: Optional[bool] = None,
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list:
        """Get the public (federated) timeline.

        Args:
            local: Show only local statuses.
            remote: Show only remote statuses.
            only_media: Show only statuses with media.
            max_id: Return results older than this ID.
            since_id: Return results newer than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Maximum number of results (default 20, max 40).
        """
        try:
            params = {}
            if local is not None:
                params["local"] = str(local).lower()
            if remote is not None:
                params["remote"] = str(remote).lower()
            if only_media is not None:
                params["only_media"] = str(only_media).lower()
            if max_id:
                params["max_id"] = max_id
            if since_id:
                params["since_id"] = since_id
            if min_id:
                params["min_id"] = min_id
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api("/api/v1/timelines/public"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_hashtag_timeline(
        hashtag: str,
        local: Optional[bool] = None,
        remote: Optional[bool] = None,
        only_media: Optional[bool] = None,
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list:
        """Get public statuses containing a given hashtag.

        Args:
            hashtag: The hashtag name (without the # symbol).
            local: Return only local statuses.
            remote: Return only remote statuses.
            only_media: Return only statuses with media.
            max_id: Return results older than this ID.
            since_id: Return results newer than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Maximum number of results (default 20, max 40).
        """
        try:
            params = {}
            if local is not None:
                params["local"] = str(local).lower()
            if remote is not None:
                params["remote"] = str(remote).lower()
            if only_media is not None:
                params["only_media"] = str(only_media).lower()
            if max_id:
                params["max_id"] = max_id
            if since_id:
                params["since_id"] = since_id
            if min_id:
                params["min_id"] = min_id
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api(f"/api/v1/timelines/tag/{hashtag}"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_list_timeline(
        list_id: str,
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list:
        """Get statuses from a specific list timeline.

        Args:
            list_id: The ID of the list.
            max_id: Return results older than this ID.
            since_id: Return results newer than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Maximum number of results (default 20, max 40).
        """
        try:
            params = {}
            if max_id:
                params["max_id"] = max_id
            if since_id:
                params["since_id"] = since_id
            if min_id:
                params["min_id"] = min_id
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api(f"/api/v1/timelines/list/{list_id}"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]
