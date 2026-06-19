"""Mastodon Notifications API tools."""
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


def register_notifications(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_notifications(
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
        types: Optional[list] = None,
        exclude_types: Optional[list] = None,
        account_id: Optional[str] = None,
    ) -> list:
        """Get all notifications. types/exclude_types: mention, status, reblog, follow, favourite, poll, update."""
        params: dict = {}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        if limit is not None:
            params["limit"] = limit
        if account_id:
            params["account_id"] = account_id
        try:
            req_params = list(params.items())
            if types:
                req_params += [("types[]", t) for t in types]
            if exclude_types:
                req_params += [("exclude_types[]", t) for t in exclude_types]
            r = requests.get(_api("/api/v1/notifications"), params=req_params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_notification(notification_id: str) -> dict:
        """Get a single notification by ID."""
        try:
            r = requests.get(_api(f"/api/v1/notifications/{notification_id}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def dismiss_notification(notification_id: str) -> dict:
        """Dismiss a single notification by ID."""
        try:
            r = requests.post(_api(f"/api/v1/notifications/{notification_id}/dismiss"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def clear_notifications() -> dict:
        """Clear all notifications from the server."""
        try:
            r = requests.post(_api("/api/v1/notifications/clear"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_notification_unread_count(
        limit: Optional[int] = None,
        types: Optional[list] = None,
        exclude_types: Optional[list] = None,
        account_id: Optional[str] = None,
    ) -> dict:
        """Get the number of unread notifications (capped count)."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        if account_id:
            params["account_id"] = account_id
        try:
            req_params = list(params.items())
            if types:
                req_params += [("types[]", t) for t in types]
            if exclude_types:
                req_params += [("exclude_types[]", t) for t in exclude_types]
            r = requests.get(_api("/api/v1/notifications/unread_count"), params=req_params, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}
