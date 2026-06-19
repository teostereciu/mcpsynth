"""Mastodon Timelines API tools."""
import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers() -> dict:
    h = {"Accept": "application/json"}
    if ACCESS_TOKEN:
        h["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    return h


def _api(path: str) -> str:
    return f"{BASE_URL}{path}"


def register_timelines(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_home_timeline(
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list:
        """Get the home timeline (statuses from followed users and hashtags)."""
        params: dict = {}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        if limit is not None:
            params["limit"] = limit
        try:
            r = requests.get(_api("/api/v1/timelines/home"), params=params, headers=_headers())
            return r.json()
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
        """Get the public (federated) timeline. local=True for local-only."""
        params: dict = {}
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
        try:
            r = requests.get(_api("/api/v1/timelines/public"), params=params, headers=_headers())
            return r.json()
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
        """Get statuses for a hashtag timeline. hashtag: tag name without the # symbol."""
        params: dict = {}
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
        try:
            r = requests.get(_api(f"/api/v1/timelines/tag/{hashtag}"), params=params, headers=_headers())
            return r.json()
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
        """Get statuses from a list timeline."""
        params: dict = {}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        if limit is not None:
            params["limit"] = limit
        try:
            r = requests.get(_api(f"/api/v1/timelines/list/{list_id}"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]
