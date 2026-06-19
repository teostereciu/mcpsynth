from typing import Any, Dict, Optional

from .client import MastodonClient


def verify_credentials() -> Any:
    """GET /api/v1/accounts/verify_credentials"""
    client = MastodonClient()
    return client.request("GET", "/api/v1/accounts/verify_credentials")


def get_account(account_id: str) -> Any:
    """GET /api/v1/accounts/{id}"""
    client = MastodonClient()
    return client.request("GET", f"/api/v1/accounts/{account_id}")


def follow_account(account_id: str, *, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages: Optional[list] = None) -> Any:
    """POST /api/v1/accounts/{id}/follow"""
    client = MastodonClient()
    payload: Dict[str, Any] = {}
    if reblogs is not None:
        payload["reblogs"] = reblogs
    if notify is not None:
        payload["notify"] = notify
    if languages is not None:
        payload["languages"] = languages
    return client.request("POST", f"/api/v1/accounts/{account_id}/follow", json=payload)


def unfollow_account(account_id: str) -> Any:
    """POST /api/v1/accounts/{id}/unfollow"""
    client = MastodonClient()
    return client.request("POST", f"/api/v1/accounts/{account_id}/unfollow")


def get_followers(account_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    """GET /api/v1/accounts/{id}/followers"""
    client = MastodonClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/api/v1/accounts/{account_id}/followers", params=params)


def get_following(account_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    """GET /api/v1/accounts/{id}/following"""
    client = MastodonClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/api/v1/accounts/{account_id}/following", params=params)
