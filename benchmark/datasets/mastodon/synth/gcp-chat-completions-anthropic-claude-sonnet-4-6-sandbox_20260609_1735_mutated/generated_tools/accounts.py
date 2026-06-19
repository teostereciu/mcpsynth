"""Mastodon accounts API tools."""
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
    def verify_account_credentials() -> dict:
        """Get the authenticated account's own profile (verify token works)."""
        try:
            resp = requests.get(_api("/api/v1/accounts/verify_credentials"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_account(account_id: str) -> dict:
        """Get a public account by ID.

        Args:
            account_id: The ID of the account.
        """
        try:
            resp = requests.get(_api(f"/api/v1/accounts/{account_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_account_statuses(
        account_id: str,
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
        only_media: Optional[bool] = None,
        exclude_replies: Optional[bool] = None,
        exclude_reblogs: Optional[bool] = None,
        pinned: Optional[bool] = None,
        tagged: Optional[str] = None,
    ) -> list:
        """Get statuses posted by an account.

        Args:
            account_id: The ID of the account.
            max_id: Return results older than this ID.
            since_id: Return results newer than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Maximum number of results (default 20, max 40).
            only_media: Show only statuses with media.
            exclude_replies: Exclude replies.
            exclude_reblogs: Exclude boosts.
            pinned: Show only pinned statuses.
            tagged: Filter by hashtag (without #).
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
            if only_media is not None:
                params["only_media"] = str(only_media).lower()
            if exclude_replies is not None:
                params["exclude_replies"] = str(exclude_replies).lower()
            if exclude_reblogs is not None:
                params["exclude_reblogs"] = str(exclude_reblogs).lower()
            if pinned is not None:
                params["pinned"] = str(pinned).lower()
            if tagged:
                params["tagged"] = tagged
            resp = requests.get(_api(f"/api/v1/accounts/{account_id}/statuses"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_account_followers(
        account_id: str,
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list:
        """Get followers of an account.

        Args:
            account_id: The ID of the account.
            max_id: Return results older than this ID.
            since_id: Return results newer than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Maximum number of results (default 40, max 80).
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
            resp = requests.get(_api(f"/api/v1/accounts/{account_id}/followers"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_account_following(
        account_id: str,
        max_id: Optional[str] = None,
        since_id: Optional[str] = None,
        min_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list:
        """Get accounts that an account is following.

        Args:
            account_id: The ID of the account.
            max_id: Return results older than this ID.
            since_id: Return results newer than this ID.
            min_id: Return results immediately newer than this ID.
            limit: Maximum number of results (default 40, max 80).
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
            resp = requests.get(_api(f"/api/v1/accounts/{account_id}/following"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def follow_account(account_id: str, reblogs: Optional[bool] = None, notify: Optional[bool] = None) -> dict:
        """Follow an account.

        Args:
            account_id: The ID of the account to follow.
            reblogs: Whether to receive boosts from this account. Defaults to true.
            notify: Whether to receive notifications when this account posts. Defaults to false.
        """
        try:
            data = {}
            if reblogs is not None:
                data["reblogs"] = str(reblogs).lower()
            if notify is not None:
                data["notify"] = str(notify).lower()
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/follow"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unfollow_account(account_id: str) -> dict:
        """Unfollow an account.

        Args:
            account_id: The ID of the account to unfollow.
        """
        try:
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/unfollow"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def block_account(account_id: str) -> dict:
        """Block an account.

        Args:
            account_id: The ID of the account to block.
        """
        try:
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/block"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unblock_account(account_id: str) -> dict:
        """Unblock an account.

        Args:
            account_id: The ID of the account to unblock.
        """
        try:
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/unblock"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mute_account(account_id: str, notifications: Optional[bool] = None, duration: Optional[int] = None) -> dict:
        """Mute an account.

        Args:
            account_id: The ID of the account to mute.
            notifications: Whether to mute notifications from this account. Defaults to true.
            duration: Duration of the mute in seconds. 0 = indefinite.
        """
        try:
            data = {}
            if notifications is not None:
                data["notifications"] = str(notifications).lower()
            if duration is not None:
                data["duration"] = duration
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/mute"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unmute_account(account_id: str) -> dict:
        """Unmute an account.

        Args:
            account_id: The ID of the account to unmute.
        """
        try:
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/unmute"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_account_relationships(account_ids: list) -> list:
        """Get relationship info between the authenticated user and given accounts.

        Args:
            account_ids: List of account IDs to check relationships for.
        """
        try:
            params = [("id[]", aid) for aid in account_ids]
            resp = requests.get(_api("/api/v1/accounts/relationships"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def search_accounts(
        q: str,
        limit: Optional[int] = None,
        resolve: Optional[bool] = None,
        following: Optional[bool] = None,
    ) -> list:
        """Search for accounts by username, display name, or domain.

        Args:
            q: The search query string.
            limit: Maximum number of results (default 40, max 80).
            resolve: Attempt WebFinger lookup for remote accounts.
            following: Only include accounts the user is following.
        """
        try:
            params = {"q": q}
            if limit is not None:
                params["limit"] = limit
            if resolve is not None:
                params["resolve"] = str(resolve).lower()
            if following is not None:
                params["following"] = str(following).lower()
            resp = requests.get(_api("/api/v1/accounts/search"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def lookup_account(acct: str) -> dict:
        """Look up an account by its webfinger address (username@domain).

        Args:
            acct: The account's webfinger address (e.g. 'user@mastodon.social').
        """
        try:
            params = {"acct": acct}
            resp = requests.get(_api("/api/v1/accounts/lookup"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_account_lists(account_id: str) -> list:
        """Get lists that contain a given account (that the authenticated user owns).

        Args:
            account_id: The ID of the account.
        """
        try:
            resp = requests.get(_api(f"/api/v1/accounts/{account_id}/lists"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def pin_account(account_id: str) -> dict:
        """Endorse / pin an account on your profile.

        Args:
            account_id: The ID of the account to endorse.
        """
        try:
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/pin"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unpin_account(account_id: str) -> dict:
        """Remove endorsement / unpin an account from your profile.

        Args:
            account_id: The ID of the account to unendorse.
        """
        try:
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/unpin"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_account_note(account_id: str, comment: str) -> dict:
        """Set a private note on an account.

        Args:
            account_id: The ID of the account.
            comment: The note text (use empty string to clear).
        """
        try:
            data = {"comment": comment}
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/note"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_from_followers(account_id: str) -> dict:
        """Remove an account from your followers.

        Args:
            account_id: The ID of the account to remove from followers.
        """
        try:
            resp = requests.post(_api(f"/api/v1/accounts/{account_id}/remove_from_followers"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
