from typing import Any, Dict, Optional

from .http_client import MastodonClient


def verify_credentials(*, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/accounts/verify_credentials"""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/accounts/verify_credentials")


def get_account(*, account_id: str, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/accounts/:id"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/accounts/{account_id}")


def follow_account(*, account_id: str, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/accounts/:id/follow"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/accounts/{account_id}/follow", json=params or {})


def unfollow_account(*, account_id: str, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/accounts/:id/unfollow"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/accounts/{account_id}/unfollow")


def get_followers(*, account_id: str, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/accounts/:id/followers"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/accounts/{account_id}/followers", params=params)


def get_following(*, account_id: str, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/accounts/:id/following"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/accounts/{account_id}/following", params=params)
