"""Mastodon search API tools."""
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
        """Search for accounts, statuses, and hashtags.

        Args:
            q: The search query string.
            type: Limit results to 'accounts', 'statuses', or 'hashtags'.
            resolve: Attempt WebFinger lookup for remote accounts/URLs.
            following: Only include accounts the user is following.
            account_id: Only return statuses from this account ID.
            exclude_unreviewed: Filter out unreviewed tags (use for trending).
            max_id: Return results older than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Max results per category (default 20, max 40).
            offset: Skip first n results (only with type specified).
        """
        try:
            params = {"q": q}
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
            resp = requests.get(_api("/api/v2/search"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
