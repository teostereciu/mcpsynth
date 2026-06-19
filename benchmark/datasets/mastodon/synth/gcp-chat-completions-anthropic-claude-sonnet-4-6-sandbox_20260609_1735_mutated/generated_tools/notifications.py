"""Mastodon notifications API tools."""
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
    def get_notifications(
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
        types: Optional[list] = None,
        exclude_types: Optional[list] = None,
        account_id: Optional[str] = None,
    ) -> list:
        """Get all notifications for the authenticated user.

        Args:
            max_id: Return results older than this ID.
            since_id: Return results newer than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Maximum number of results (default 40, max 80).
            types: List of notification types to include (e.g. ['mention', 'follow']).
            exclude_types: List of notification types to exclude.
            account_id: Only return notifications from this account ID.
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
            if account_id:
                params["account_id"] = account_id
            # Build list params manually
            req_params = list(params.items())
            if types:
                for t in types:
                    req_params.append(("types[]", t))
            if exclude_types:
                for t in exclude_types:
                    req_params.append(("exclude_types[]", t))
            resp = requests.get(_api("/api/v1/notifications"), headers=_headers(), params=req_params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_notification(notification_id: str) -> dict:
        """Get a single notification by ID.

        Args:
            notification_id: The ID of the notification.
        """
        try:
            resp = requests.get(_api(f"/api/v1/notifications/{notification_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def clear_notifications() -> dict:
        """Clear all notifications for the authenticated user."""
        try:
            resp = requests.post(_api("/api/v1/notifications/clear"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def dismiss_notification(notification_id: str) -> dict:
        """Dismiss a single notification.

        Args:
            notification_id: The ID of the notification to dismiss.
        """
        try:
            resp = requests.post(_api(f"/api/v1/notifications/{notification_id}/dismiss"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_notification_unread_count(
        limit: Optional[int] = None,
        types: Optional[list] = None,
        exclude_types: Optional[list] = None,
        account_id: Optional[str] = None,
    ) -> dict:
        """Get the number of unread notifications.

        Args:
            limit: Max notifications to count (default 100, max 1000).
            types: Only count these notification types.
            exclude_types: Exclude these notification types from count.
            account_id: Only count notifications from this account.
        """
        try:
            req_params = []
            if limit is not None:
                req_params.append(("limit", limit))
            if account_id:
                req_params.append(("account_id", account_id))
            if types:
                for t in types:
                    req_params.append(("types[]", t))
            if exclude_types:
                for t in exclude_types:
                    req_params.append(("exclude_types[]", t))
            resp = requests.get(_api("/api/v1/notifications/unread_count"), headers=_headers(), params=req_params)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
