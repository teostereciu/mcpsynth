from typing import Any, Dict, Optional

from .client import MastodonClient


def accounts_verify_credentials(client: MastodonClient) -> Any:
    return client.request("GET", "/api/v1/accounts/verify_credentials")


def accounts_get(client: MastodonClient, account_id: str) -> Any:
    return client.request("GET", f"/api/v1/accounts/{account_id}")


def accounts_follow(client: MastodonClient, account_id: str, *, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages: Optional[list[str]] = None) -> Any:
    payload: Dict[str, Any] = {}
    if reblogs is not None:
        payload["reblogs"] = reblogs
    if notify is not None:
        payload["notify"] = notify
    if languages is not None:
        payload["languages"] = languages
    return client.request("POST", f"/api/v1/accounts/{account_id}/follow", json=payload or None)


def accounts_unfollow(client: MastodonClient, account_id: str) -> Any:
    return client.request("POST", f"/api/v1/accounts/{account_id}/unfollow")


def accounts_followers(client: MastodonClient, account_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/api/v1/accounts/{account_id}/followers", params=params or None)


def accounts_following(client: MastodonClient, account_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/api/v1/accounts/{account_id}/following", params=params or None)
