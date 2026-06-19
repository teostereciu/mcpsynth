"""Mastodon scheduled statuses API tools."""
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
    def get_scheduled_statuses(
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list:
        """Get all scheduled statuses for the authenticated user.

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
            resp = requests.get(_api("/api/v1/scheduled_statuses"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_scheduled_status(scheduled_status_id: str) -> dict:
        """Get a single scheduled status by ID.

        Args:
            scheduled_status_id: The ID of the scheduled status.
        """
        try:
            resp = requests.get(_api(f"/api/v1/scheduled_statuses/{scheduled_status_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_scheduled_status(scheduled_status_id: str, scheduled_at: str) -> dict:
        """Update the publish time of a scheduled status.

        Args:
            scheduled_status_id: The ID of the scheduled status.
            scheduled_at: New ISO datetime for publishing (must be at least 5 minutes in the future).
        """
        try:
            data = {"scheduled_at": scheduled_at}
            resp = requests.put(_api(f"/api/v1/scheduled_statuses/{scheduled_status_id}"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def cancel_scheduled_status(scheduled_status_id: str) -> dict:
        """Cancel and delete a scheduled status.

        Args:
            scheduled_status_id: The ID of the scheduled status to cancel.
        """
        try:
            resp = requests.delete(_api(f"/api/v1/scheduled_statuses/{scheduled_status_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
