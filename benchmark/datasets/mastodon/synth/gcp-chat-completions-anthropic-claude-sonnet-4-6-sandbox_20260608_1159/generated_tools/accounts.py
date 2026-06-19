"""Mastodon Accounts API tools."""
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


def register_accounts(mcp: FastMCP) -> None:

    @mcp.tool()
    def verify_credentials() -> dict:
        """Get the authenticated account (verify token and return own account info)."""
        try:
            r = requests.get(_api("/api/v1/accounts/verify_credentials"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_account(account_id: str) -> dict:
        """Get a Mastodon account by its ID."""
        try:
            r = requests.get(_api(f"/api/v1/accounts/{account_id}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def lookup_account(acct: str) -> dict:
        """Look up an account by username/acct (e.g. 'user' or 'user@instance.social')."""
        try:
            r = requests.get(_api("/api/v1/accounts/lookup"), params={"acct": acct}, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def search_accounts(
        q: str,
        limit: Optional[int] = None,
        resolve: Optional[bool] = None,
        following: Optional[bool] = None,
    ) -> list:
        """Search for accounts by username or display name."""
        params: dict = {"q": q}
        if limit is not None:
            params["limit"] = limit
        if resolve is not None:
            params["resolve"] = str(resolve).lower()
        if following is not None:
            params["following"] = str(following).lower()
        try:
            r = requests.get(_api("/api/v1/accounts/search"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

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
        """Get statuses posted by an account."""
        params: dict = {}
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
        try:
            r = requests.get(_api(f"/api/v1/accounts/{account_id}/statuses"), params=params, headers=_headers())
            return r.json()
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
        """Get followers of an account."""
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
            r = requests.get(_api(f"/api/v1/accounts/{account_id}/followers"), params=params, headers=_headers())
            return r.json()
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
        """Get accounts that an account is following."""
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
            r = requests.get(_api(f"/api/v1/accounts/{account_id}/following"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def follow_account(
        account_id: str,
        reblogs: Optional[bool] = None,
        notify: Optional[bool] = None,
    ) -> dict:
        """Follow an account. reblogs: show boosts in home timeline. notify: get notified of posts."""
        data: dict = {}
        if reblogs is not None:
            data["reblogs"] = str(reblogs).lower()
        if notify is not None:
            data["notify"] = str(notify).lower()
        try:
            r = requests.post(_api(f"/api/v1/accounts/{account_id}/follow"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unfollow_account(account_id: str) -> dict:
        """Unfollow an account."""
        try:
            r = requests.post(_api(f"/api/v1/accounts/{account_id}/unfollow"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def block_account(account_id: str) -> dict:
        """Block an account."""
        try:
            r = requests.post(_api(f"/api/v1/accounts/{account_id}/block"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unblock_account(account_id: str) -> dict:
        """Unblock an account."""
        try:
            r = requests.post(_api(f"/api/v1/accounts/{account_id}/unblock"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mute_account(
        account_id: str,
        notifications: Optional[bool] = None,
        duration: Optional[int] = None,
    ) -> dict:
        """Mute an account. notifications: also mute notifications. duration: seconds (0=indefinite)."""
        data: dict = {}
        if notifications is not None:
            data["notifications"] = str(notifications).lower()
        if duration is not None:
            data["duration"] = duration
        try:
            r = requests.post(_api(f"/api/v1/accounts/{account_id}/mute"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unmute_account(account_id: str) -> dict:
        """Unmute an account."""
        try:
            r = requests.post(_api(f"/api/v1/accounts/{account_id}/unmute"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_account_relationships(account_ids: list) -> list:
        """Get relationships (following, blocking, muting, etc.) with a list of account IDs."""
        try:
            params = [("id[]", aid) for aid in account_ids]
            r = requests.get(_api("/api/v1/accounts/relationships"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def update_account_credentials(
        display_name: Optional[str] = None,
        note: Optional[str] = None,
        locked: Optional[bool] = None,
        bot: Optional[bool] = None,
        discoverable: Optional[bool] = None,
        indexable: Optional[bool] = None,
        source_privacy: Optional[str] = None,
        source_sensitive: Optional[bool] = None,
        source_language: Optional[str] = None,
    ) -> dict:
        """Update the authenticated account's profile credentials."""
        data: dict = {}
        if display_name is not None:
            data["display_name"] = display_name
        if note is not None:
            data["note"] = note
        if locked is not None:
            data["locked"] = str(locked).lower()
        if bot is not None:
            data["bot"] = str(bot).lower()
        if discoverable is not None:
            data["discoverable"] = str(discoverable).lower()
        if indexable is not None:
            data["indexable"] = str(indexable).lower()
        if source_privacy is not None:
            data["source[privacy]"] = source_privacy
        if source_sensitive is not None:
            data["source[sensitive]"] = str(source_sensitive).lower()
        if source_language is not None:
            data["source[language]"] = source_language
        try:
            r = requests.patch(_api("/api/v1/accounts/update_credentials"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_account_lists(account_id: str) -> list:
        """Get lists that contain a given account (that the authenticated user also follows)."""
        try:
            r = requests.get(_api(f"/api/v1/accounts/{account_id}/lists"), headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_familiar_followers(account_ids: list) -> list:
        """Get followers of given accounts that are also followed by the authenticated user."""
        try:
            params = [("id[]", aid) for aid in account_ids]
            r = requests.get(_api("/api/v1/accounts/familiar_followers"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]
