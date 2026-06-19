from typing import Any, Dict, Optional

from .client import MastodonClient


def accounts_verify_credentials(client: MastodonClient) -> Any:
    return client.request("GET", "/api/v1/accounts/verify_credentials")


def accounts_get(client: MastodonClient, account_id: str) -> Any:
    return client.request("GET", f"/api/v1/accounts/{account_id}")


def accounts_follow(client: MastodonClient, account_id: str, *, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages=None) -> Any:
    payload: Dict[str, Any] = {"reblogs": reblogs, "notify": notify, "languages": languages}
    return client.request("POST", f"/api/v1/accounts/{account_id}/follow", json=payload)


def accounts_unfollow(client: MastodonClient, account_id: str) -> Any:
    return client.request("POST", f"/api/v1/accounts/{account_id}/unfollow")


def accounts_followers(client: MastodonClient, account_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        f"/api/v1/accounts/{account_id}/followers",
        params={"limit": limit, "max_id": max_id, "since_id": since_id},
    )


def accounts_following(client: MastodonClient, account_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        f"/api/v1/accounts/{account_id}/following",
        params={"limit": limit, "max_id": max_id, "since_id": since_id},
    )
