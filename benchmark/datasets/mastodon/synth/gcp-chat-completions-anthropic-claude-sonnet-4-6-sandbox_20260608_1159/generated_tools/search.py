"""Mastodon Search API tools."""
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


def register_search(mcp: FastMCP) -> None:

    @mcp.tool()
    def search(
        q: str,
        type: Optional[str] = None,
        resolve: Optional[bool] = None,
        following: Optional[bool] = None,
        account_id: Optional[str] = None,
        exclude_unreviewed: Optional[bool] = None,
        max_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> dict:
        """Search for accounts, statuses, and hashtags. type: 'accounts', 'statuses', or 'hashtags'."""
        params: dict = {"q": q}
        if type:
            params["type"] = type
        if resolve is not None:
            params["resolve"] = str(resolve).lower()
        if following is not None:
            params["following"] = str(following).lower()
        if account_id:
            params["account_id"] = account_id
        if exclude_unreviewed is not None:
            params["exclude_unreviewed"] = str(exclude_unreviewed).lower()
        if max_id:
            params["max_id"] = max_id
        if min_id:
            params["min_id"] = min_id
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        try:
            r = requests.get(_api("/api/v2/search"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}
